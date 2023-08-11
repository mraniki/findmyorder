"""
 FindMyOrder Main
"""
from datetime import datetime

import emoji
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
    """find an order class"""

    def __init__(
        self,
    ):
        self.logger = logger

    async def search(
        self,
        my_string: str,
    ) -> bool:
        """Search an order."""
        if my_string:
            string_check = my_string.split()[0].lower()
            self.logger.debug("Searching order identifier in {}", string_check)
            if string_check in settings.action_identifier.lower():
                return True
        return False

    async def get_info(self):
        """get info about the class"""
        return f"{__class__.__name__} {__version__}\n"

    async def contains_emoji(self, input_string: str) -> bool:
        """Check if the input string contains an emoji."""
        return any(emoji.is_emoji(character) for character in input_string)

    async def identify_order(
        self,
        my_string: str,
    ) -> dict:
        """Identify an order."""
        try:
            action = (
                one_of(settings.action_identifier, caseless=True)
                .set_results_name("action")
                .set_parse_action(pyparsing_common.upcase_tokens)
            )
            instrument = Word(alphas).set_results_name("instrument")
            stop_loss = Combine(
                Suppress(settings.stop_loss_identifier) + Word(nums)
            ).set_results_name("stop_loss")
            take_profit = Combine(
                Suppress(settings.take_profit_identifier) + Word(nums)
            ).set_results_name("take_profit")
            quantity = Combine(
                Suppress(settings.quantity_identifier)
                + Word(nums)
                + Optional(Suppress("%"))
            ).set_results_name("quantity")
            order_type = one_of(
                settings.order_type_identifier, caseless=True
            ).set_results_name("order_type")
            leverage_type = one_of(
                settings.leverage_type_identifier, caseless=True
            ).set_results_name("leverage_type")
            comment = Combine(
                Suppress(settings.comment_identifier) + Word(alphas)
            ).set_results_name("comment")

            order_grammar = (
                action("action")
                + Optional(instrument, default=None)
                + Optional(stop_loss, default=settings.stop_loss)
                + Optional(take_profit, default=settings.take_profit)
                + Optional(quantity, default=settings.quantity)
                + Optional(order_type, default=None)
                + Optional(leverage_type, default=None)
                + Optional(comment, default=None)
            )

            order = order_grammar.parse_string(instring=my_string, parse_all=False)
            self.logger.debug("Order parsed {}", order)
            return order.asDict()

        except Exception as error:
            self.logger.error(error)
            return error

    async def get_order(
        self,
        msg: str,
    ):
        """get an order."""
        if not await self.search(msg):
            self.logger.debug("No order identified")
            return None
        order = await self.identify_order(msg)
        if isinstance(order, dict):
            order["timestamp"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        if settings.instrument_mapping:
            self.logger.debug("mapping")
            await self.replace_instrument(order)
        if order["instrument"] in settings.ignore_instrument:
            self.logger.debug("Ignoring instrument {}", order["instrument"])
            return
        self.logger.debug("Order identified {}", order)
        return order

    async def replace_instrument(self, order):
        """replace instrument by an alternative instrument"""
        instrument = order["instrument"]
        for item in settings.mapping:
            if item["id"] == instrument:
                order["instrument"] = item["alt"]
                break
        self.logger.debug("Instrument symbol changed", order)
        return order
