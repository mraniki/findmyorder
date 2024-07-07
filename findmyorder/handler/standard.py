"""
Standard Parser

"""

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

from .handler import ParserClient


class StandardHandler(ParserClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)
        self.client = "standard"

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
        if not await self.search(my_string):
            logger.debug("No order identified")
            return None
        else:
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
