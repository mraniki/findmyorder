import asyncio, logging, re
from datetime import datetime, timezone
from pyparsing import *
from .config import settings


class findmyorder:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)

    def search(self,mystring: str = None,):
      try:
        self.logger.debug(f"search for {mystring}")
        action = one_of(settings.action_identifier, caseless=True).set_results_name("action")
        order_grammar = action('action')
        order = order_grammar.parse_string(instring=mystring,parse_all=False)
        if order:
          self.logger.debug(f"found {order} in {mystring}")
          return True
        self.logger.debug(f"no order identified in {mystring} using {settings.action_identifier}")
        return False
      except Exception as e:
        self.logger.debug(f"error search {mystring} {e}")
        return False

    def identify_order(self,mystring: str = None,):
      self.logger.debug(f"identify_order for {mystring}")
      try:
        action = one_of(settings.action_identifier, caseless=True).set_results_name("action")
        instrument = Word(alphas).set_results_name("instrument")
        stop_loss = (PrecededBy(Literal(settings.stop_loss_identifier)) & Word(nums)).set_results_name("stop_loss")
        take_profit = Combine(settings.take_profit_identifier + Word(nums)).set_results_name("take_profit")
        quantity = Combine(settings.quantity_identifier + Word(nums)).set_results_name("quantity")+ Suppress("q=")
        ordertype = one_of(settings.order_type_identifier, caseless=True).set_results_name("ordertype")
        leverage_type = one_of(settings.leverage_type_identifier, caseless=True).set_results_name("leverage_type")

        order_grammar = action('action') + Optional(instrument) + Optional(stop_loss) + Optional(take_profit) + Optional(quantity) 

        order = order_grammar.parse_string(instring=mystring,parse_all=False)
        self.logger.debug(f"identify_order order {order}")
        self.logger.debug(f"identify_order order dict {order.asDict()}")
        return order.asDict()

      except Exception as e:
          self.logger.error(f"identify_order {e}")
          return None

    def get_order(self,mystring: str = None,):
      try:
        self.logger.debug(f"get_order for {mystring}")

        if (self.search(mystring)):
            self.logger.info(msg=f"get_order found: {mystring}")
            parsed_order = self.identify_order(mystring)
            self.logger.info(msg=f"get_order parsed_order: {parsed_order}")
            order = {}
            order['action'] = parsed_order['action']
            order['instrument'] =  parsed_order['instrument']
            order['stoploss'] = parsed_order['takeprofit']
            order['takeprofit'] = parsed_order['takeprofit']
            order['quantity'] = parsed_order['quantity']
            order['timestamp'] = datetime.now(timezone.utc)
            # order['comments'] = 'findmyorder'
            # order['ordertype'] = 'spot'
            # order['instrument_type'] = 'Any'
            # order['market'] = 'Any'
            # order['exchange'] = 'Any'
            # order['leverage'] = 1
            # order['leverage_type'] = 'isolated'
            # order['amount'] = 100

            self.logger.info(msg=f"get_order order: {order}")

            return order

        else:
          return None

      except Exception as e:
          self.logger.error(f"get order {e}")
          #return

