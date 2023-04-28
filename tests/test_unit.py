
from findmyorder import findmyorder


def test_search():
    fmo = findmyorder()
    assert fmo.search('buy btc') == True
    assert fmo.search('hello') == False
    assert fmo.search('SELL BTC 1%') == True
    assert fmo.search('BUY BTCUSDT 1%') == True
    assert fmo.search('buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC') == True
    assert fmo.search('sell EURGBP sl=200 tp=400 q=2%') == True

def test_identify_order():
    fmo = findmyorder()
    assert fmo.identify_order('hello') is None

def test_get_order():
    fmo = findmyorder()
    assert fmo.get_order('hello') is None