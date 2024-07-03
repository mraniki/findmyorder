"""
 FindMyOrder Main

"""

from datetime import datetime, timezone

from loguru import logger
from pyparsing import (
    Combine,
    Optional,
    Suppress,
    Word,
    alphas,
    nums,
    one_of,
    pyparsing_common,
)

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
            return
        self.handler = settings.handler or None
        self.action_identifier = settings.action_identifier
        self.stop_loss_identifier = settings.stop_loss_identifier
        self.take_profit_identifier = settings.take_profit_identifier
        self.quantity_identifier = settings.quantity_identifier
        self.order_type_identifier = settings.order_type_identifier
        self.leverage_type_identifier = settings.leverage_type_identifier
        self.comment_identifier = settings.comment_identifier
        self.stop_loss = settings.stop_loss
        self.take_profit = settings.take_profit
        self.quantity = settings.quantity
        self.instrument_mapping = settings.instrument_mapping
        self.mapping = settings.mapping
        self.ignore_instrument = settings.ignore_instrument

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
            if order_identifier in (
                action.lower() for action in self.action_identifiers
            ):
                logger.debug("Order identifier found in {}", order_identifier)
                return True

        return False

    async def get_info(self):
        """
        get info about the class

        Returns:
            str

        """
        return f"{__class__.__name__} {__version__}\n"

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
        try:
            action = (
                one_of(self.action_identifier, caseless=True)
                .set_results_name("action")
                .set_parse_action(pyparsing_common.upcase_tokens)
            )
            instrument = Word(alphas + nums).set_results_name("instrument")
            stop_loss = Combine(
                Suppress(self.stop_loss_identifier) + Word(nums)
            ).set_results_name("stop_loss")
            take_profit = Combine(
                Suppress(self.take_profit_identifier) + Word(nums)
            ).set_results_name("take_profit")
            quantity = Combine(
                Suppress(self.quantity_identifier)
                + Word(nums)
                + Optional(Suppress("%"))
            ).set_results_name("quantity")
            order_type = one_of(
                self.order_type_identifier, caseless=True
            ).set_results_name("order_type")
            leverage_type = one_of(
                self.leverage_type_identifier, caseless=True
            ).set_results_name("leverage_type")
            comment = Combine(
                Suppress(self.comment_identifier) + Word(alphas)
            ).set_results_name("comment")

            order_grammar = (
                action("action")
                + Optional(instrument, default=None)
                + Optional(stop_loss, default=self.stop_loss)
                + Optional(take_profit, default=self.take_profit)
                + Optional(quantity, default=self.quantity)
                + Optional(order_type, default=None)
                + Optional(leverage_type, default=None)
                + Optional(comment, default=None)
            )

            order = order_grammar.parse_string(instring=my_string, parse_all=False)
            logger.debug("Order parsed {}", order)
            return order.asDict()

        except Exception as error:
            logger.error(error)
            return error

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
