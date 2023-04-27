
from pyparsing import one_of, Word, alphas, Regex, Optional



mystring = "this is a test"

action = Regex(r'/(SELL|BUY|long|short)/i')
currency_pair = Regex(r'(?<=SELL|BUY|long|short\s).\w+')
stop_loss = Regex(r'sl=(\d+)')
take_profit = Regex(r'tp=(\d+)')
quantity = Regex(r'q=(\d+)')


order_grammar = action('action') + currency_pair('currency_pair') \
+ Optional(stop_loss) + Optional(take_profit) + Optional(quantity) 

# self.logger.debug(f"order_grammar  {order_grammar}")
try:
    result = order_grammar.parseString(mystring)
except ParseException:
    print("none")
# self.logger.debug(f"identify_order result {result}")
print(result)
# return results