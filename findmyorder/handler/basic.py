"""
Basic Parser

"""

from pyparsing import (
    Optional,
    Word,
    alphas,
    nums,
    one_of,
    pyparsing_common,
)

from .handler import ParserClient


class BasicHandler(ParserClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)
        self.client = "basic"

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
            dict with the order parameters:
            action, instrument

        """
        action = (
            one_of(self.action_identifier, caseless=True)
            .set_results_name("action")
            .set_parse_action(pyparsing_common.upcase_tokens)
        )
        instrument = Word(alphas + nums).set_results_name("instrument")
        order_grammar = action("action") + Optional(instrument, default=None)
        order = order_grammar.parse_string(instring=my_string, parse_all=False)
        return order.asDict()
