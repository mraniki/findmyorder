import os, asyncio, logging
import pyparsing as pp


class order:

    def __init__(self,
                 ):
        self.logger =  logging.getLogger(__name__)
        self.logger.debug(f"find my order Logger:  {self.logger} on {__name__} version: {__version__}")
        self.direction
        self.symbol
        self.amount
        self.quantity
        self.stoploss
        self.takeprofit
        self.comment
        self.exchange
        
    def search(self)
        return      
        # order = self.pp.Word(pp.alphas) 
        # for greeting_str in [
        #     "Hello, World!",
        #     "Bonjour, Monde!",
        #     "Hola, Mundo!",
        #     "Hallo, Welt!",
        # ]:
        # greeting = greet.parse_string(greeting_str)
        # print(greeting)