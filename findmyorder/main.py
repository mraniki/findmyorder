import os, asyncio, logging, re
import pyparsing as pp

from translate import Translator

from config import settings
from findmyorder import __version__

translator = Translator(to_lang="en")


class findmyorder:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)
        self.logger.debug(f"find my order Logger:  {self.logger} on {__name__} version: {__version__}")

        
       # translation = translator.translate("ACHETER")
        
    def search(self
               message_to_parse: str = None)

      try:
        myDict = settings.DIRECTION

        for word in myDict:
            if re.search(word, message_to_parse):
              self.logger.debug(f"found {word} in {message_to_parse}")
              return True
        self.logger.debug(f"not word identified in {message_to_parse}")
        return False
      except Exception as e:
        self.logger.debug(f"error identify {e}")
        return False

    def identify(self
               message_to_parse: str = None)
      try:
        if (self.search(message_to_parse))
          order = message_to_parse.split()
          # self.logger.info(msg=f"Order parsing: {order}")
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
