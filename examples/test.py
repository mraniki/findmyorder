import re

myDict = ['BUY', 'SELL', 'buy', 'sell', 'Buy','Sell']
message_to_parse = "buy BTC"

# if any(word in message_to_parse for word in myDict):
#     print("All words in sentence")
#     print(message_to_parse)
#     print(word)
# else:
#     print("Missing")

for word in myDict:
    if re.search(word, message_to_parse):
    	print("found")
    	print(word)
    else:
    	print("not found")