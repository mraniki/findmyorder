
from pyparsing import Word, alphas, nums, oneOf, Optional, Regex, Suppress, LineEnd, Group, delimitedList



mystring = "this is a test"

action = oneOf("BUY SELL LONG SHORT")
currency_pair = Word(alphas, exact=6)
market = Optional(Word(alphas, exact=4))
leverage = Regex(r'Leverage: \w+ \((\d+(\.\d+)?X)\)')('leverage')
percentage = Regex(r'\d+(\.\d+)?%')
quantity = Regex(r'\d+(\.\d+)?')('quantity')
# stop_loss = Regex(r'sl=\d+')['stop_loss']
# take_profit1 = Regex(r'tp1=\d+')['take_profit1']
# take_profit2 = Regex(r'tp2=\d+')['take_profit2']
# comment = Regex(r'comment=\w+')['comment']

# #order grammar
order_grammar = action('action') + currency_pair('currency_pair') + percentage('percentage') \
        + Optional(quantity)
        # + Optional(stop_loss) 
        # + Optional(take_profit1) 
        # + Optional(take_profit2)  
        # + Optional(comment)
print(order_grammar)
# self.logger.debug(f"order_grammar  {order_grammar}")
result = order_grammar.parseString(mystring)
# self.logger.debug(f"identify_order result {result}")
print(result)
# return results