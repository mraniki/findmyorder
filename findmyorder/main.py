import asyncio, logging, re
from datetime import datetime



from findmyorder import __version__
from findmyorder.config import settings

# import pyparsing as pp

# from translate import Translator
# translator = Translator(to_lang="en")


class findmyorder:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)
        #self.logger.debug(f"find my order Logger:  {self.logger} on {__name__} version: {__version__}")
       # translation = translator.translate("ACHETER")
        
    def search(self,
               message_to_parse: str = None,
               ):
      try:
        print(settings.fmo_identifier)
        myDict = settings.fmo_identifier

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

    # def identify(self,
    #            mystring: str = None,
    #            ):
    #     order_format = self.identify_order_format(mystring)
    #     order_data = self.identify_order_element(mystring)

    # def identify_order_format(self,
    #            mystring: str = None,
    #            ):
    #   return

    def identify(self,
               mystring: str = None,
               ):
      try:
        self.logger.debug(f"identify_order_element for {mystring}")
        if (self.search(mystring)):
            order_raw = mystring.split()
            self.logger.info(msg=f"Order identified: {order_raw}")
            order = {}
            order['direction'] = 'BUY'
            order['symbol'] = 'EURUSD'
            order['quantity'] = 10
            order['amount'] = 100
            order['stoploss'] = 1000
            order['comments'] = 'default comment'
            order['market'] = 'Any'
            order['exchange'] = 'Any'
            order['timestamp'] = datetime.utcnow()
            order['leverage'] = 1
            order['takeprofit'] = {'tp1':1, 'tp2':10, 'tp3':100, 'tp4':1000, 'tp5':1000}

            # if order_raw
            #   order['direction'] = 'BUY'
            return order

      except Exception as e:
          self.logger.debug(f"error identify_order_element {e}")
          return




# class order:

#      def __init__(self,
#                  ):
#           self.direction = 'buy'
#           self.symbol = 'EURUSD'
