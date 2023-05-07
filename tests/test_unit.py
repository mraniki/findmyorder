"""
FindMyOrder Unit Testing
"""

import pytest
from datetime import datetime
from findmyorder import FindMyOrder


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


@pytest.mark.xfail(raises=TypeError)
async def test_search_exception():
    """Search Testing"""
    fmo = FindMyOrder()
    mystring = ""
    await fmo.search(mystring)


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
    assert result is None


@pytest.mark.asyncio
async def test_valid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "sell EURJPY sl=200 tp=400 q=2%"
    expected = {
        "action": "SELL",
        "instrument": "EURJPY",
        "stop_loss": 200,
        "take_profit": 400,
        "quantity": 2,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    result = await fmo.get_order(mystring)
    assert result["action"] == expected["action"]
    assert result["instrument"] == expected["instrument"]
    assert int(result["stop_loss"]) == expected["stop_loss"]
    assert int(result["take_profit"]) == expected["take_profit"]
    assert int(result["quantity"]) == expected["quantity"]
    assert result["order_type"] == expected["order_type"]
    assert result["leverage_type"] == expected["leverage_type"]
    assert result["comment"] == expected["comment"]
    assert type(result["timestamp"] is datetime)


@pytest.mark.asyncio
async def test_short_valid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "buy EURUSD"
    expected = {
        "action": "BUY",
        "instrument": "EURUSD",
        "stop_loss": 1000,
        "take_profit": 1000,
        "quantity": 1,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now()
    }
    result = await fmo.get_order(mystring)
    assert result["action"] == expected["action"]
    assert result["instrument"] == expected["instrument"]
    assert result["stop_loss"] == expected["stop_loss"]
    assert result["take_profit"] == expected["take_profit"]
    assert result["quantity"] == expected["quantity"]
    assert result["order_type"] == expected["order_type"]
    assert result["leverage_type"] == expected["leverage_type"]
    assert result["comment"] == expected["comment"]
    assert type(result["timestamp"] is datetime)


@pytest.mark.asyncio
async def test_invalid_get_order():
    """get order Testing"""
    fmo = FindMyOrder()
    mystring = "ECHO 12345"
    expected = None
    result = await fmo.get_order(mystring)
    assert result == expected
