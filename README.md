# Find my order


| <img width="200" alt="Logo" src="https://user-images.githubusercontent.com/8766259/233823991-cceaa05a-ff15-4796-a6bb-bcb3ee0d8859.jpg"> | A python package to identify and parse order for trade execution. |
| ------------- | ------------- |
|[![Pypi](https://badgen.net/badge/icon/findmyorder?icon=pypi&label)](https://pypi.org/project/findmyorder/) ![Version](https://img.shields.io/pypi/v/findmyorder)<br>  ![Pypi](https://img.shields.io/pypi/dm/findmyorder)<br> [![🐍Build](https://github.com/mraniki/findmyorder/actions/workflows/%F0%9F%90%8DBuild.yml/badge.svg?branch=main)](https://github.com/mraniki/findmyorder/actions/workflows/%F0%9F%90%8DBuild.yml) [![codecov](https://codecov.io/gh/mraniki/findmyorder/branch/dev/graph/badge.svg?token=4838MSZNCC)](https://codecov.io/gh/mraniki/findmyorder) | Find & Parse a trade order for execution|



Key features:

- Identify an order with word `BUY SELL LONG SHORT` or your own `Bull`, `to the moon`, `pump` via config file
- Parse and return a structured order with action and instrument as mandatory
- Settings for custom option




# Install
`pip install findmyorder`

# How to use it
```
fmo = FindMyOrder()
msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
order = await fmo.get_order(msg_order)
#{'action': 'BUY', 'instrument': 'EURUSD', 'stop_loss': '1000', 'take_profit': '1000', 'quantity': '2', 'order_type': None, 'leverage_type': None, 'comment': None, 'timestamp': datetime.datetime(2023, 5, 3, 12, 10, 28, 731282, tzinfo=datetime.timezone.utc)}
```
## Example
[example](https://github.com/mraniki/findmyorder/blob/main/examples/example.py)

## Real use case
[TalkyTrader, submit trading order to CEX & DEX with messaging platform (Telegram, Matrix and Discord)](https://github.com/mraniki/tt)


# Documentation
https://github.com/mraniki/findmyorder/wiki

## 🚧 Roadmap

[🚧 Roadmap](https://github.com/mraniki/findmyorder/milestones)

## Questions? Want to help? 
[![discord](https://badgen.net/badge/icon/discord/purple?icon=discord&label)](https://discord.gg/vegJQGrRRa)
[![telegram](https://badgen.net/badge/icon/telegram?icon=telegram&label)](https://t.me/TTTalkyTraderChat/1)
