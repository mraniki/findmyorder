"""
FindMyOrder Unit Testing
"""

from datetime import datetime

import pytest

from findmyorder import FindMyOrder
from findmyorder.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="fmo")


@pytest.fixture(name="fmo")
def fmo():
    """return fmo"""
    return FindMyOrder()


@pytest.fixture
def order():
    """return valid order"""
    return "buy GOLD sl=200 tp=400 q=2%"


@pytest.fixture
def result_order():
    """return standard expected results"""
    return {
        "action": "BUY",
        "instrument": "XAUUSD",
        "stop_loss": 200,
        "take_profit": 400,
        "quantity": 2,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now(),
    }


@pytest.fixture
def ignore_order():
    """return order to ignore"""
    return "buy DOGE"


@pytest.fixture
def invalid_order():
    """return fmo"""
    return "This is not an order"


@pytest.fixture
def bot_command():
    return "/bal"


@pytest.mark.asyncio
async def test_settings():
    """Search Testing"""
    assert settings.VALUE == "On Testing"
    assert settings.findmyorder_enabled is True


@pytest.mark.asyncio
async def test_info(fmo):
    """Search Testing"""
    result = await fmo.get_info()
    print(result)
    assert result is not None
    assert "FindMyOrder" in result
    assert "ℹ️" in result


@pytest.mark.asyncio
async def test_search_valid_order(fmo, order):
    """Search Testing"""
    print(settings)
    assert await fmo.search(order) is True


@pytest.mark.asyncio
async def test_search_no_order(fmo, invalid_order):
    """Search Testing"""
    assert await fmo.search(invalid_order) is False


@pytest.mark.asyncio
async def test_search_no_order_command(fmo, bot_command):
    """Search Testing"""
    assert await fmo.search(bot_command) is False


@pytest.mark.asyncio
async def test_search_exception(fmo):
    """Search Testing"""
    mystring = ""
    assert await fmo.search(mystring) is False


@pytest.mark.asyncio
async def test_identify_order(fmo, order):
    """Identify Testing"""
    result = await fmo.identify_order(order)
    assert result is not None


@pytest.mark.asyncio
async def test_identify_order_invalid_input(fmo, invalid_order):
    """Identify Testing"""
    result = await fmo.identify_order(invalid_order)
    print(result)
    assert result is None


@pytest.mark.asyncio
async def test_replace_instrument(fmo, order, result_order):
    """replace instrument Testing"""
    result = await fmo.get_order(order)
    print(result)
    assert result["instrument"] == result_order["instrument"]
    assert type(result["timestamp"] is datetime)


@pytest.mark.asyncio
async def test_ignore_order(fmo, ignore_order):
    """ignore order Testing"""
    result = await fmo.get_order(ignore_order)
    assert result is None


@pytest.mark.asyncio
async def test_invalid_get_order(fmo, invalid_order):
    """ignore order Testing"""
    result = await fmo.get_order(invalid_order)
    assert result is None


@pytest.mark.asyncio
async def test_standard_get_order(fmo, order, result_order):
    """get order Testing"""
    result = await fmo.get_order(order)
    print(result)
    assert result["action"] == result_order["action"]
    assert result["instrument"] == result_order["instrument"]
    assert int(result["stop_loss"]) == result_order["stop_loss"]
    assert int(result["take_profit"]) == result_order["take_profit"]
    assert int(result["quantity"]) == result_order["quantity"]
    assert result["order_type"] == result_order["order_type"]
    assert result["leverage_type"] == result_order["leverage_type"]
    assert result["comment"] == result_order["comment"]
    assert type(result["timestamp"] is datetime)

