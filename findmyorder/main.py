"""
 FindMyOrder Main
"""
import logging
from datetime import datetime

from emoji import is_emoji
from pyparsing import (
    Combine, Optional, Word, alphas,
    nums, one_of, ParseBaseException,
    pyparsing_common, Suppress)

from .config import settings


class FindMyOrder:
    """find an order class """

    def __init__(
        self,
    ):
        self.logger = logging.getLogger(name="FMO")

    async def search(
        self,
        my_string: str,
    ) -> bool:
        """Search an order."""
        try:
            if my_string:
                string_check = my_string.split()[0].lower()
                if string_check in settings.action_identifier.lower():
                    return True
            return False
        except Exception as e:
            return e

    async def contains_emoji(self, input_string: str) -> bool:
        """Check if the input string contains an emoji."""
        print(input_string)
        return is_emoji(input_string)


    async def identify_order(
            self,
            my_string: str,
            ) -> dict:
        """Identify an order."""
        try:
            action = one_of(
                settings.action_identifier, caseless=True
                ).set_results_name("action").set_parse_action(
                    pyparsing_common.upcase_tokens)
            instrument = Word(
                alphas
                ).set_results_name("instrument")
            stop_loss = Combine(
                    Suppress(settings.stop_loss_identifier)
                    + Word(nums)
                ).set_results_name("stop_loss")
            take_profit = Combine(
                Suppress(settings.take_profit_identifier)
                + Word(nums)
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
                    Suppress(settings.comment_identifier)
                    + Word(alphas)
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

            order = order_grammar.parse_string(
                    instring=my_string,
                    parse_all=False
                    )
            return order.asDict()

        except Exception as e:
            return e

    async def get_order(
        self,
        msg: str,
    ):
        """get an order."""
        try:
            logging.debug("get_order %s", msg)

            if await self.search(msg):
                order = await self.identify_order(msg)
                if isinstance(order, dict):
                    order["timestamp"] = datetime.utcnow().strftime(
                        "%Y-%m-%dT%H:%M:%SZ")
                return order
            return None

        except Exception as e:
            return e


# Grammar
# class TradingGrammar:
#     def __init__(self):
#         self.action = self._action()
#         self.instrument = self._instrument()
#         self.exchange = self._exchange()

# grammar = TradingGrammar()

# new_order_grammar = (
#     grammar.currency_pair
#     + grammar.exchange
#     + grammar.take_profit_targets
# )
# CORNIX type
# currency_pair = Combine(Suppress("#") + Word(alphas + "/") + Word(alphas))\
#     .set_results_name("currency_pair")
# exchange = Group(Suppress("Exchanges:")
# + delimitedList(
    # Word(alphas + " "),
    # delim=", ")
    # ).set_results_name("exchanges")
# signal_type = Group(
    # Suppress("Signal Type:")
    # + Word(alphas + " ()"))
#     .set_results_name("signal_type")
# leverage = Group(
    # Suppress("Leverage:")
    # + Word(alphas + " (.)"))\
#     .set_results_name("leverage")
# entry_targets = Group(Suppress("Entry Targets:")
# + OneOrMore(Group(Word(nums
# + ".")
# + Suppress("-")
# + Word(nums + ".%")))).set_results_name("entry_targets")
# take_profit_targets = Group(
    # Suppress("Take-Profit Targets:")
    # + OneOrMore(Word(nums + "."))).set_results_name("take_profit_targets")
# stop_targets = Group(
    # Suppress("Stop Targets:")
    # + OneOrMore(Word(nums + "."))).set_results_name("stop_targets")
# trailing_config = Group(
    # Suppress("Trailing Configuration:")
    # + Group(Word(alphas + ":")
    # + Word(alphas + "-")
    # + Suppress("Trigger:")
    # + Word(alphas + " ()"))).set_results_name("trailing_config")

# new_order_grammar = (
#     currency_pair
#     + exchange
#     + signal_type
#     + leverage
#     + entry_targets
#     + take_profit_targets
#     + stop_targets
#     + trailing_config
# )
