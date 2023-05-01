"""
FindMyOrder Unit Testing
"""
    
import pytest
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime, timezone
from findmyorder import FindMyOrder as fmo


@pytest.fixture
def find_my_order():
    return fmo()

def test_search_order(find_my_order):
    mystring = "buy btc"
    assert find_my_order.search(mystring) == True

def test_search_no_order(find_my_order):
    mystring = "This is not an order"
    assert find_my_order.search(mystring) == False

def test_search_exception(find_my_order, caplog):
    mystring = ""
    find_my_order.search(mystring)
    assert "SearchError" in caplog.text
# async def test_search():
#     """Search Testing"""
#     assert await fmo.search("hello") is False
#     assert await fmo.search("buy btc") is True
#     assert await fmo.search("SELL BTC 1%") is True
#     assert await fmo.search("BUY BTCUSDT 1%") is True
#     assert await fmo.search("buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC") is True
#     assert await fmo.search("sell EURGBP sl=200 tp=400 q=2%") is True
#     assert await fmo.search("LONG ETHUSD sl=200 tp=400 q=2%") is True
#     assert await fmo.search("SHORT CRUDEOIL sl=200 tp=400 q=2%") is True

async def test_identify_order():
    """Identify Testing"""
    assert await fmo.identify_order("hello") is None
    assert await fmo.identify_order("buy btc") is not None
# async def test_get_order():
#     """Get Order Testing"""
#     assert await fmo.get_order("hello") is None
#     assert await fmo.get_order("buy btc") is not None
    

@pytest.fixture
def mock_get_order():
    mock = MagicMock()
    mock.search.return_value = True
    mock.identify_order.return_value = {"action": "BUY", "instrument": "EURUSD", "quantity": 1}
    return mock

@pytest.mark.asyncio
async def test_get_order(mock_get_order):
    msg = "BUY EURUSD q=1"
    result = await mock_get_order.get_order(msg)
    assert result is not None
    assert result["action"] == BUY
    assert result["instrument"] == "EURUSD"
    assert result["quantity"] == 1
    assert "timestamp" in result
    assert isinstance(result["timestamp"], datetime)