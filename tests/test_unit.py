"""
FindMyOrder Unit Testing
"""
from findmyorder import FindMyOrder


async def test_search():
    """Search Testing"""
    fmo = FindMyOrder()
    assert await fmo.search("hello") is False
    assert await fmo.search("buy btc") is True
    assert await fmo.search("SELL BTC 1%") is True
    assert await fmo.search("BUY BTCUSDT 1%") is True
    assert await fmo.search("buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC") is True
    assert await fmo.search("sell EURGBP sl=200 tp=400 q=2%") is True
    assert await fmo.search("LONG ETHUSD sl=200 tp=400 q=2%") is True
    assert await fmo.search("SHORT CRUDEOIL sl=200 tp=400 q=2%") is True

async def test_identify_order():
    """Identify Testing"""
    fmo = FindMyOrder()
    assert await fmo.identify_order("hello") is None
    assert await fmo.identify_order("buy btc") is not None
    assert await fmo.identify_order("SELL BTC 1%") is not None

async def test_get_order():
    """Get Order Testing"""
    fmo = FindMyOrder()
    assert await fmo.get_order("hello") is None
    assert await fmo.get_order("buy btc") is not None
