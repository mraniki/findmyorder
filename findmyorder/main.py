import os, asyncio, logging
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
        # self.direction
        # self.symbol
        # self.amount
        # self.quantity
        # self.stoploss
        # self.takeprofit
        # self.comment
        # self.exchange
        
       # translation = translator.translate("ACHETER")
        
    def search(self
               message_to_parse: str = None)
         #wordlist = message_to_parse.split(" ")
        my_dict = settings.DIRECTION
        list_of_words = message_to_parse.split()
        if word in my_dict
            print('success')
             return 1
        # order = self.pp.Word(pp.alphas) 
        # for greeting_str in [
        #     "Hello, World!",
        #     "Bonjour, Monde!",
        #     "Hola, Mundo!",
        #     "Hallo, Welt!",
        # ]:
        # greeting = greet.parse_string(greeting_str)
        # print(greeting)
     def countWords(word, sentence):
      testWord = ' ' + word.lower() + ' '
      testSentence = ' '

      for char in sentence:
          if char.isalpha():
              testSentence = testSentence + char.lower()
          else:
              testSentence = testSentence + ' '
  
      testSentence = testSentence + ' '
  
      return testSentence.count(testWord)