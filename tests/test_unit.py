
from findmyorder import FindMyOrder


def test_search():
    fmo = FindMyOrder()
    assert await fmo.search('hello') == False
    assert await fmo.search('buy btc') == True
    assert await fmo.search('SELL BTC 1%') == True
    assert await fmo.search('BUY BTCUSDT 1%') == True
    assert await fmo.search('buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC') == True
    assert await fmo.search('sell EURGBP sl=200 tp=400 q=2%') == True
    assert await fmo.search('LONG ETHUSD sl=200 tp=400 q=2%') == True
    assert await fmo.search('SHORT CRUDEOIL sl=200 tp=400 q=2%') == True

def test_identify_order():
    fmo = FindMyOrder()
    assert await fmo.identify_order('hello') is None
    assert await fmo.identify_order('buy btc') is not None
    assert await fmo.identify_order('SELL BTC 1%') is not None

def test_get_order():
    fmo = FindMyOrder()
    assert await fmo.get_order('hello') is None
    assert await fmo.get_order('buy btc') is not None
    #assert fmo.get_order('SELL BTC 1%') is not None