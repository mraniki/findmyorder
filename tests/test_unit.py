"""
FindMyOrder Unit Testing
"""
    
import pytest
from findmyorder import FindMyOrder


async def test_search_valid_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "buy btc"
    assert await fmo.search(mystring) is True

async def test_search_no_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "This is not an order"
    assert await fmo.search(mystring) is False

async def test_search_no_order_command():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "/bal"
    assert await fmo.search(mystring) is False

# async def test_search_exception(find_my_order, caplog):
#     """Search Testing"""
#     mystring = ""
#     await find_my_order.search(mystring)
#     assert "SearchError" in caplog.text

async def test_search_normal_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "sell EURGBP sl=200 tp=400 q=2%"
    assert await fmo.search(mystring) is True

async def test_search_normal_order_variation():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "LONG ETHUSD sl=200 tp=400 q=2%"
    assert await fmo.search(mystring) is True

async def test_identify_order():
    """Identify Testing"""
    fmo = FindMyOrder()
    mystring = "buy btc"
    result = await fmo.identify_order(mystring)
    assert result is not None

async def test_identify_order_invalid_input():
    """Identify Testing"""
    fmo = FindMyOrder()
    mystring = "hello"
    result = await fmo.identify_order(mystring)
    assert result is None

async def test_valid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "buy EURJPY sl=200 tp=400 q=2%"
    expected = {
        "action": "buy",
        "instrument": "EURJPY",
        "stop_loss": "200",
        "take_profit": "400",
        "quantity": "2",
        "order_type": None,
        "leverage_type": None,
        "comment": None
    }
    result = await fmo.get_order(mystring)
    assert result == expected

async def test_short_valid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "buy EURUSD"
    expected = {
        "action": "buy",
        "instrument": "EURJPY",
        "stop_loss": None,
        "take_profit": None,
        "quantity": None,
        "order_type": None,
        "leverage_type": None,
        "comment": None
    }
    result = await fmo.get_order(mystring)
    assert result == expected

async def test_invalid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "ECHO 12345"
    expected = None
    result = await fmo.get_order(mystring)
    assert result == expected
