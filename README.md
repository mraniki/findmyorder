# Find my order

| <img width="200" alt="Logo" src="https://user-images.githubusercontent.com/8766259/233823991-cceaa05a-ff15-4796-a6bb-bcb3ee0d8859.jpg"> | A python package to identify and <br>parse order for trade execution. |
| ------------- | ------------- |
|<br> [![wiki](https://img.shields.io/badge/🪙🗿-wiki-0080ff)](https://talkytrader.gitbook.io/talky/) [![Pypi](https://badgen.net/badge/icon/findmyorder?icon=pypi&label)](https://pypi.org/project/findmyorder/) ![Version](https://img.shields.io/pypi/v/findmyorder)<br>  ![Pypi](https://img.shields.io/pypi/dm/findmyorder)<br> [![👷‍♂️Flow](https://github.com/mraniki/findmyorder/actions/workflows/%F0%9F%91%B7%E2%80%8D%E2%99%82%EF%B8%8FFlow.yml/badge.svg)](https://github.com/mraniki/findmyorder/actions/workflows/%F0%9F%91%B7%E2%80%8D%E2%99%82%EF%B8%8FFlow.yml)  [![codebeat badge](https://codebeat.co/badges/9b113098-d22d-498d-9c61-eb1e96c1311a)](https://codebeat.co/projects/github-com-mraniki-findmyorder-main) [![codecov](https://codecov.io/gh/mraniki/findmyorder/branch/dev/graph/badge.svg?token=4838MSZNCC)](https://codecov.io/gh/mraniki/findmyorder) | Find & Parse a trade order for execution|

Key features:

- Identify an order with word `BUY SELL LONG SHORT` or your own `Bull`, `to the moon`, `pump` via config file
- Parse and return a structured order with action and instrument as mandatory
- Capability to map a given instrument to a new one (e.g BTC to WBTC or ETHUSD to ETH)
- Settings for custom options

## Install

`pip install findmyorder`

## How to use it

```python
>>> from findmyorder import FindMyOrder
fmo = FindMyOrder()
msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
order = await fmo.get_order(msg_order)
#{'action': 'BUY', 'instrument': 'EURUSD', 'stop_loss': '1000', 'take_profit': '1000', 'quantity': '2', 'order_type': None, 'leverage_type': None, 'comment': None, 'timestamp': datetime.datetime(2023, 5, 3, 12, 10, 28, 731282, tzinfo=datetime.timezone.utc)}
```

### Example

[example](https://github.com/mraniki/findmyorder/blob/main/examples/example.py)

### Real use case

[TalkyTrader](https://github.com/mraniki/tt)

## Documentation

[![wiki](https://img.shields.io/badge/🪙🗿-wiki-0080ff)](https://talkytrader.gitbook.io/talky/)
