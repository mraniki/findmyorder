
from pyparsing import one_of, Word, alphas, Regex, Optional



mystring = "this is a test"

action = one_of(strs="BUY SELL LONG SHORT",caseless=True)
currency_pair = Word(alphas, exact=6)
percentage = Regex(r'\d+(\.\d+)?%')

# quantity = Regex(r'\d+(\.\d+)?')('quantity')
# market = Optional(Word(alphas, exact=4))
# leverage = Regex(r'Leverage: \w+ \((\d+(\.\d+)?X)\)')('leverage')
# stop_loss = Regex(r'sl=\d+')['stop_loss']
# take_profit1 = Regex(r'tp1=\d+')['take_profit1']
# take_profit2 = Regex(r'tp2=\d+')['take_profit2']
# comment = Regex(r'comment=\w+')['comment']

# #order grammar
order_grammar = action('action') + currency_pair('currency_pair') + percentage('percentage') 
        # + Optional(quantity)
        # + Optional(stop_loss) 
        # + Optional(take_profit1) 
        # + Optional(take_profit2)  
        # + Optional(comment)

# self.logger.debug(f"order_grammar  {order_grammar}")
result = order_grammar.parseString(mystring)
# self.logger.debug(f"identify_order result {result}")
print(result)
# return results