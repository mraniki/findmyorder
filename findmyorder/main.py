"""
 FindMyOrder Main

"""

import importlib

from loguru import logger

from findmyorder import __version__

from .config import settings


class FindMyOrder:
    """
    Class to find and parse trading order

    Args:
        None

    Returns:
        None

    Methods:
        search(my_string: str) -> bool
        get_info() -> str
        identify_order(my_string: str) -> dict
        get_order(msg: str) -> dict
        replace_instrument(order: dict) -> None

    """

    def __init__(
        self,
    ):
        """
        Initializes the class instance.

        Args:
            self (ClassName): The class instance.

        Returns:
            None
        """

        self.enabled = settings.findmyorder_enabled
        if not self.enabled:
            logger.info("FindMyOrder is disabled. No Parser will be created.")
        self.clients = []
        # Create a client for each client in settings.myllm
        for name, client_config in settings.findmyorder.items():
            # Skip template and empty string client names
            if name in ["", "template"] or not client_config.get("enabled"):
                continue
            try:
                # Create the client
                logger.debug("Creating client {}", name)
                client = self._create_client(**client_config, name=name)
                # If the client has a valid client attribute, append it to the list
                if client and getattr(client, "client", None):
                    self.clients.append(client)
            except Exception as e:
                # Log the error if the client fails to be created
                logger.error(f"Failed to create client {name}: {e}")

        # Log the number of clients that were created
        logger.info(f"Loaded {len(self.clients)} clients")
        if not self.clients:
            logger.warning(
                "No clients were created. Check your settings or disable the module."
            )

    def _create_client(self, **kwargs):
        """
        Create a client based on the given protocol.

        This function takes in a dictionary of keyword arguments, `kwargs`,
        containing the necessary information to create a client. The required
        key in `kwargs` is "parser_library", which specifies the parser to use
        to identify the order. The value of "parser_library" must match one of the
        libraries supported by findmyorder.

        This function retrieves the class used to create the client based on the
        value of "parser_library" from the mapping of parser names to client classes
        stored in `self.client_classes`. If the value of "parser_library" does not
        match any of the libraries supported, the function logs an error message
        and returns None.

        If the class used to create the client is found, the function creates a
        new instance of the class using the keyword arguments in `kwargs` and
        returns it.

        The function returns a client object based on the specified protocol
        or None if the library is not supported.

        Parameters:
            **kwargs (dict): A dictionary of keyword arguments containing the
            necessary information for creating the client. The required key is
            "parser_library".

        Returns:
            A client object based on the specified protocol or None if the
            library is not supported.

        """
        library = kwargs.get("parser_library", "standard")
        client_class = self.client_classes.get(f"{library.capitalize()}Handler")

        if client_class is None:
            logger.error(f"library {library} not supported")
            return None

        return client_class(**kwargs)

    def get_all_client_classes(self):
        """
        Retrieves all client classes from the `findmyorder.handler` module.

        This function imports the `findmyorder.handler` module and retrieves
        all the classes defined in it.

        The function returns a dictionary where the keys are the
        names of the classes and the values are the corresponding
        class objects.

        Returns:
            dict: A dictionary containing all the client classes
            from the `findmyorder.handler` module.
        """
        provider_module = importlib.import_module("findmyorder.handler")
        return {
            name: cls
            for name, cls in provider_module.__dict__.items()
            if isinstance(cls, type)
        }

    async def get_info(self):
        """
        get info about the class

        Returns:
            str

        """
        version_info = f"ℹ️ {type(self).__name__} {__version__}\n"
        client_info = "".join(f"🔎 {client.name}\n" for client in self.clients)
        return version_info + client_info.strip()

    async def search(self, message: str) -> bool:
        """
        Search an order.

        Args:
            message (str): Message

        Returns:
            bool

        """
        for client in self.clients:
            yield await client.search()

    async def identify_order(
        self,
        my_string: str,
    ) -> dict:
        """
        Identify an order and return a dictionary
        with the order parameters

        Args:
            my_string (str): Message

        Returns:
            dict

        """
        for client in self.clients:
            yield client.identify_order()

    async def replace_instrument(self, order):
        """
        Replace instrument by an alternative instrument, if the
        instrument is not in the mapping, it will be ignored.

        Args:
            order (dict):

        Returns:
            dict
        """
        for client in self.clients:
            yield client.replace_instrument()

    async def get_order(
        self,
        msg: str,
    ):
        """
        Get an order from a message. The message can be
        an order or an order identifier

        Args:
            msg (str): Message

        Returns:
            dict

        """
        for client in self.clients:
            yield await client.get_order()
