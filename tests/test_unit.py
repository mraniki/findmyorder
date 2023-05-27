"""
FindMyOrder Unit Testing
"""

import pytest
from datetime import datetime
from findmyorder import FindMyOrder


@pytest.fixture
def expected_result():
    return {
        "action": "BUY",
        "instrument": "EURUSD",
        "stop_loss": 200,
        "take_profit": 400,
        "quantity": 2,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now()
    }


@pytest.mark.asyncio
async def test_search_valid_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "buy btc"
    assert await fmo.search(mystring) is True


@pytest.mark.asyncio
async def test_search_no_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "This is not an order"
    assert await fmo.search(mystring) is False


@pytest.mark.asyncio
async def test_search_no_order_command():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "/bal"
    assert await fmo.search(mystring) is False


@pytest.mark.asyncio
async def test_search_exception():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = ""
    assert await fmo.search(mystring) is False


@pytest.mark.asyncio
async def test_exception_handling():
    # Simulate an exception
    def func_that_raises():
        raise ValueError("Test error")

    # Call the function and verify that it returns None
    result = None
    try:
        result = func_that_raises()
    except Exception:
        result = None

    # Check that the function returned None
    assert result is None


@pytest.mark.asyncio
async def test_search_normal_order():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "sell EURGBP sl=200 tp=400 q=2%"
    assert await fmo.search(mystring) is True


@pytest.mark.asyncio
async def test_search_normal_order_variation():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = "LONG ETHUSD sl=200 tp=400 q=2%"
    assert await fmo.search(mystring) is True


@pytest.mark.asyncio
async def test_identify_order():
    """Identify Testing"""
    fmo = FindMyOrder()
    mystring = "buy btc"
    result = await fmo.identify_order(mystring)
    assert result is not None


@pytest.mark.asyncio
async def test_identify_order_invalid_input():
    """Identify Testing"""
    fmo = FindMyOrder()
    mystring = "hello"
    result = await fmo.identify_order(mystring)
    assert str(result).startswith("Expected")


@pytest.mark.asyncio
async def test_valid_get_order(expected_result):
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "buy EURUSD sl=200 tp=400 q=2%"
    result = await fmo.get_order(mystring)
    assert result["action"] == expected_result["action"]
    assert result["instrument"] == expected_result["instrument"]
    assert int(result["stop_loss"]) == expected_result["stop_loss"]
    assert int(result["take_profit"]) == expected_result["take_profit"]
    assert int(result["quantity"]) == expected_result["quantity"]
    assert result["order_type"] == expected_result["order_type"]
    assert result["leverage_type"] == expected_result["leverage_type"]
    assert result["comment"] == expected_result["comment"]
    assert type(result["timestamp"] is datetime)


@pytest.mark.asyncio
async def test_short_valid_get_order(expected_result):
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "buy EURUSD"

    result = await fmo.get_order(mystring)
    assert result["action"] == expected_result["action"]
    assert result["instrument"] == expected_result["instrument"]
    assert int(result["quantity"]) == 1
    assert type(result["timestamp"] is datetime)


@pytest.mark.asyncio
async def test_invalid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "ECHO 12345"
    expected = None
    result = await fmo.get_order(mystring)
    assert result == expected
