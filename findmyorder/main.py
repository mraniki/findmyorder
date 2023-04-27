import asyncio, logging, re
from datetime import datetime

from findmyorder.config import settings

from pyparsing import Word, alphas, nums, oneOf, Optional, Regex, Suppress, LineEnd, Group, delimitedList


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
        #parsing
        action = oneOf("BUY SELL LONG SHORT")
        currency_pair = Word(alphas, exact=6)
        market = Optional(Word(alphas, exact=4))
        percentage = Regex(r'\d+(\.\d+)?%')
        # quantity = Regex(r'\d+(\.\d+)?')('quantity')
        # stop_loss = Regex(r'sl=\d+')['stop_loss']
        # take_profit1 = Regex(r'tp1=\d+')['take_profit1']
        # take_profit2 = Regex(r'tp2=\d+')['take_profit2']
        # leverage = Regex(r'Leverage: \w+ \((\d+(\.\d+)?X)\)')
        # comment = Regex(r'comment=\w+')['comment']

        #order grammar
        order_grammar = action('action') + currency_pair('currency_pair') + percentage('percentage') 
                        # + Optional(quantity)
                        # + Optional(stop_loss) 
                        # + Optional(take_profit1) 
                        # + Optional(take_profit2)  
                        # + Optional(comment)
        self.logger.debug(f"order_grammar  {order_grammar}")
        result = order_grammar.parseString(mystring)
        self.logger.debug(f"identify_order result {result}")
        return results


      except Exception as e:
          self.logger.debug(f"error identify_order {e}")
          return


    def get_order(self,mystring: str = None,):
      try:
        self.logger.debug(f"get_order for {mystring}")

        if (self.search(mystring)):
            self.logger.info(msg=f"get_order found: {mystring}")
            parsed_order = self.identify_order(mystring)
            self.logger.info(msg=f"parsed_order results: {parsed_order}")

            # order_raw = mystring.split()
            # self.logger.info(msg=f"Order identified: {order_raw}")

            # order = {}
            # order['market'] = 'Any'
            # order['exchange'] = 'Any'
            # order['timestamp'] = datetime.utcnow()
            # order['leverage'] = 1
            # order['ordertype'] = 'spot'
            # order['direction'] = 'BUY'
            # order['symbol'] = 'EURUSD'
            # order['quantity'] = 10
            # order['amount'] = 100
            # order['stoploss'] = 1000
            # order['takeprofit'] = {'tp1':1, 'tp2':10, 'tp3':100, 'tp4':1000, 'tp5':1000}
            # order['comments'] = 'findmyorder'
            return None
        else:
          return None

      except Exception as e:
          self.logger.debug(f"error get order {e}")
          #return

