"""
 FindMyOrder Main
"""
import logging
from datetime import datetime, timezone

from pyparsing import Combine, Optional, Word, alphas, nums, one_of

from .config import settings


class FindMyOrder:
    """Search an order an order."""

    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)

    async def search(
        self,
        mystring: str,
    ):
        """Search an order."""
        try:
            logging.debug(f"search for {mystring}")
            action = one_of(settings.action_identifier, caseless=True).set_results_name("action")
            order_grammar = action('action')
            order = order_grammar.parse_string(instring=mystring,parse_all=False)
            if order:
                logging.debug(f"found {order} in {mystring}")
                return True
            logging.debug(f"no order in {mystring} using {settings.action_identifier}")
            return False
        except Exception as e:
            logging.exception("SearchError: %s", e)
            return False

    async def identify_order(
            self,
            mystring: str,
        ):
        """Identify an order."""
        logging.debug(f"identify_order for {mystring}")
        try:
            action = one_of(
                settings.action_identifier, caseless=True
                ).set_results_name("action")
            instrument = Word(
                alphas
                ).set_results_name("instrument")
            stop_loss = Combine(
                settings.stop_loss_identifier + Word(nums)
                ).set_results_name("stop_loss")
            take_profit = Combine(
                settings.take_profit_identifier + Word(nums)
                ).set_results_name("take_profit")
            quantity = Combine(
                settings.quantity_identifier + Word(nums)
                ).set_results_name("quantity")
            order_type = one_of(
                settings.order_type_identifier, caseless=True
                ).set_results_name("order_type")
            leverage_type = one_of(
                settings.leverage_type_identifier, caseless=True
                ).set_results_name("leverage_type")
            comment = one_of(
                settings.comment_identifier, caseless=True
                ).set_results_name("comment")

            order_grammar = (
                action("action")
                + Optional(instrument,default=None)
                + Optional(stop_loss,default=None)
                + Optional(take_profit,default=None)
                + Optional(quantity,default=None)
                + Optional(order_type,default=None)
                + Optional(leverage_type,default=None)
                + Optional(comment,default=None)
              )

            order = order_grammar.parse_string(
                    instring=mystring,
                    parse_all=False
                    )
            logging.debug(f"identify_order order {order}")
            logging.info(f"identify_order order dict {order.asDict()}")
            return order.asDict()

        except Exception as e:
            logging.exception("IdentifyError: %s", e)
            return None


    async def get_order(
        self,
        mystring: str,
        ):
        """get an order."""
        try:
            logging.debug(f"get_order for {mystring}")

            if await self.search(mystring):
                self.logger.info(msg=f"get_order found in {mystring}")
                order = await self.identify_order(mystring)
                self.logger.info(msg=f"get_order order: {order}")
                order["timestamp"] = datetime.now(timezone.utc)
                return order
            return None

        except Exception as e:
            logging.exception("GetOrderError: %s", e)
            return None
