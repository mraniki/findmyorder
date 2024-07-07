from datetime import datetime, timezone

from loguru import logger


class ParserClient:
    """
    Parser Handler Base Class

    Args:
        **kwargs:

    Methods:
        search(self)
        identify_order(self)
        get_order(self)
        replace_instrument(self)

    """

    def __init__(self, **kwargs):
        """
        Initialize the chat client.
        """
        self.name = kwargs.get("name", None)
        self.client = None
        self.enabled = kwargs.get("enabled", None)
        self.action_identifier = kwargs.get("action_identifier", "BUY SELL")
        self.action_identifier = self.action_identifier.lower()
        self.stop_loss_identifier = kwargs.get("stop_loss_identifier", None)
        self.take_profit_identifier = kwargs.get("take_profit_identifier", None)
        self.quantity_identifier = kwargs.get("quantity_identifier", None)
        self.order_type_identifier = kwargs.get("order_type_identifier", None)
        self.leverage_type_identifier = kwargs.get("leverage_type_identifier", None)
        self.comment_identifier = kwargs.get("comment_identifier", None)
        self.stop_loss = kwargs.get("stop_loss", None)
        self.take_profit = kwargs.get("take_profit", None)
        self.quantity = kwargs.get("quantity", None)
        self.instrument_mapping = kwargs.get("instrument_mapping", None)
        self.mapping = kwargs.get("mapping", None)
        self.ignore_instrument = kwargs.get("ignore_instrument", None)

    async def identify_order(
        self,
        my_string: str,
    ) -> dict:
        """
        Identify an order and return a dictionary
        with the order parameters to be implemented in
        the child class

        """

    async def search(self, message: str) -> bool:
        """
        Search an order.

        Args:
            message (str): Message

        Returns:
            bool

        """
        if message:
            order_identifier = message.split()[0].lower()
            # logger.debug("Order identifier: {}", order_identifier)
            # logger.debug("Action identifiers: {}", self.action_identifiers)
            if order_identifier in self.action_identifier:

                # logger.debug("Order identifier found in {}", order_identifier)
                return True

        return False

    async def replace_instrument(self, order):
        """
        Replace instrument by an alternative instrument, if the
        instrument is not in the mapping, it will be ignored.

        Args:
            order (dict):

        Returns:
            dict
        """
        instrument = order["instrument"]
        for item in self.mapping:
            if item["id"] == instrument:
                order["instrument"] = item["alt"]
                break
        logger.debug("Instrument symbol changed", order)
        return order

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
        if not await self.search(msg):
            logger.debug("No order identified")
            return None
        order = await self.identify_order(msg)
        if isinstance(order, dict):
            order["timestamp"] = datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
        if self.instrument_mapping:
            logger.debug("mapping")
            await self.replace_instrument(order)
        if order["instrument"] in self.ignore_instrument:
            logger.debug("Ignoring instrument {}", order["instrument"])
            return
        logger.debug("Order identified {}", order)
        return order
