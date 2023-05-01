"""
FindMyOrder Unit Testing
"""
    
import pytest
from findmyorder import FindMyOrder as fmo


#@pytest.fixture
def find_my_order():
    return fmo()

async def test_search_valid_order(find_my_order):
    """Search Testing"""
    mystring = "buy btc"
    assert await find_my_order.search(mystring) is True

async def test_search_no_order(find_my_order):
    """Search Testing"""
    mystring = "This is not an order"
    assert await find_my_order.search(mystring) is False

async def test_search_no_order_command(find_my_order):
    """Search Testing"""
    mystring = "/bal"
    assert await find_my_order.search(mystring) is False

# async def test_search_exception(find_my_order, caplog):
#     """Search Testing"""
#     mystring = ""
#     await find_my_order.search(mystring)
#     assert "SearchError" in caplog.text

async def test_search_normal_order(find_my_order):
    """Search Testing"""
    mystring = "sell EURGBP sl=200 tp=400 q=2%"
    assert await find_my_order.search(mystring) is True

async def test_search_normal_order_variation(find_my_order):
    """Search Testing"""
    mystring = "LONG ETHUSD sl=200 tp=400 q=2%"
    assert await find_my_order.search(mystring) is True

async def test_identify_order(find_my_order):
    """Identify Testing"""
    mystring = "buy btc"
    result = await find_my_order.identify_order(mystring)
    assert result is not None

async def test_identify_order_invalid_input(find_my_order):
    """Identify Testing"""
    mystring = "hello"
    result = await find_my_order.identify_order(mystring)
    assert result is None

async def test_valid_get_order(find_my_order):
    """get order Testing"""
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
    result = await find_my_order.get_order(mystring)
    assert result == expected

async def test_short_valid_get_order(find_my_order):
    """get order Testing"""
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
    result = await find_my_order.get_order(mystring)
    assert result == expected

async def test_invalid_get_order(find_my_order):
    """get order Testing"""
    mystring = "ECHO 12345"
    expected = None
    result = await find_my_order.get_order(mystring)
    assert result == expected
