import asyncio, logging, re
from datetime import datetime, timezone
from pyparsing import Regex, Optional, one_of, Word
from .config import settings


class findmyorder:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)

    def search(self,message_to_parse: str = None,):
      try:
      #  print(settings.identifier)
        myDict = settings.identifier

        for word in myDict:
            #self.logger.debug(f"Loop check {word}")
            if re.search(word, message_to_parse):
              self.logger.debug(f"found {word} in {message_to_parse}")
              return True
        self.logger.debug(f"no word identified in {message_to_parse}")
        return False
      except Exception as e:
        self.logger.debug(f"error search {e}")
        return False

    def identify_order(self,mystring: str = None,):
      self.logger.debug(f"identify_order for {mystring}")
      try:
        action = one_of("SELL BUY long short", caseless=True)
        # instrument = Regex(r'(?<=SELL|BUY|long|short\s).\w+')
        instrument = Word(alphas)
        stop_loss = Regex(r'sl=(\d+)')
        take_profit = Regex(r'tp=(\d+)')
        quantity = Regex(r'q=(\d+)')
        ordertype = one_of(settings.order_type, caseless=True)
        self.logger.debug(f"settings.order_type {settings.order_type}")
        leverage_type = one_of(settings.leverage_type, caseless=True)

        order_grammar = action('action') + instrument('instrument') + Optional(stop_loss) + Optional(take_profit) + Optional(quantity) 

        order = order_grammar.parse_string(instring=mystring,parse_all=False)
        self.logger.debug(f"identify_order order {order}")
        return order

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

            # order_raw = mystring.split()
            # self.logger.info(msg=f"Order identified: {order_raw}")

            order = {}
            order['action'] = 'BUY'
            order['instrument'] = 'EURUSD'
            order['stoploss'] = 1000
            order['takeprofit'] = {'tp1':10}
            order['quantity'] = 10
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

