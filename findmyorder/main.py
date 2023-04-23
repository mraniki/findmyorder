import asyncio, logging, re

from findmyorder.config import settings
from findmyorder import __version__

# import pyparsing as pp

# from translate import Translator
# translator = Translator(to_lang="en")


class findmyorder:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)
        #self.logger.debug(f"find my order Logger:  {self.logger} on {__name__} version: {__version__}")
        self.settings = settings
        
       # translation = translator.translate("ACHETER")
        
    def search(self,
               message_to_parse: str = None,
               ):
      try:
        myDict = settings.DIRECTION

        for word in myDict:
            self.logger.debug(f"Loop check {word}")
            if re.search(word, message_to_parse):
              self.logger.debug(f"found {word} in {message_to_parse}")
              return True
        self.logger.debug(f"no word identified in {message_to_parse}")
        return False
      except Exception as e:
        self.logger.debug(f"error identify {e}")
        return False

    def identify(self,
               mystring: str = None,
               ):
      try:
        self.logger.debug(f"identify order for {order_string}")
        if (self.search(mystring)):
            order_raw = mystring.split()
            self.logger.info(msg=f"Order identified: {order raw}")
            order = {}
            order['direction'] = 'tbd'
            order['symbol'] = 'tbd'
            order['quantity'] = 'tbd'
            order['amount'] = 'tbd'
            order['stoploss'] = 'tbd'
            order['comments'] = 'tbd'
            order['market'] = 'tbd'
            order['exchange'] = 'tbd'
            order['timestamp'] = 'tbd'
            order['leverage'] = 1
            order['takeprofit'] = {'tp1':'tbd', 'tp2':'tbd'}
          # direction = wordlist[0].upper()
          # stoploss = 100
          # takeprofit = 100
          # quantity = 10
          # # self.direction
          # # self.symbol
          # # self.amount
          # # self.quantity
          # # self.stoploss
          # # self.takeprofit
          # # self.comment
          # # self.exchange
          # if wordlistsize > 2:
          #     stoploss = wordlist[2][3:]
          #     takeprofit = wordlist[3][3:]
          #     quantity = wordlist[4][2:-1]
          # symbol = wordlist[1]
          # order=[direction,symbol,stoploss,takeprofit,quantity]
            return order

      except Exception as e:
          self.logger.debug(f"error identify {e}")
          return
          
# class order:

#      def __init__(self,
#                  ):
#           self.direction = 'buy'
#           self.symbol = 'EURUSD'
