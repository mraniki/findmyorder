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
def order_basic():
    """return valid order"""
    return "Buy EURUSD"


@pytest.fixture
def order_basic_crypto():
    """return valid order"""
    return "Sell ETH"


@pytest.fixture
def ignore_order():
    """return order to ignore"""
    return "buy DOGE"


@pytest.fixture
def order_standard():
    """return valid order"""
    return "buy EURUSD sl=200 tp=400 q=2%"


@pytest.fixture
def order_standard_crypto():
    """return valid order"""
    return "SHORT ETH sl=200 tp=400 q=2%"


@pytest.fixture
def order_format_2():
    """return order 2"""
    return """
    📊 FUTURES Exchanges: Binance, ByBit USDT

    #AAVEUSDT

    🟢LONG ENTRY :- 65.20 - 63.70

    Leverage: Cross (2X)

    👇TAKE PROFIT

    1) 65.70
    2) 66.20
    3) 66.70

    Stop Loss : - 62.00
"""


@pytest.fixture
def order_format_3():
    """return emoji type order"""
    return """⚡️⚡️ #BNB/USDT ⚡️⚡️
    Exchanges: ByBit USDT, Binance Futures
    Signal Type: Regular (Long)
    Leverage: Cross (20.0X)"""


@pytest.fixture
def result_order():
    """return standard expected results"""
    return {
        "action": "BUY",
        "instrument": "EURUSD",
        "stop_loss": 200,
        "take_profit": 400,
        "quantity": 2,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now(),
    }


@pytest.fixture
def result_crypto_order():
    """return standard expected results"""
    return {
        "action": "SHORT",
        "instrument": "WETH",
        "stop_loss": 1000,
        "take_profit": 1000,
        "quantity": 10,
        "order_type": None,
        "leverage_type": None,
        "comment": None,
        "timestamp": datetime.now(),
    }


@pytest.fixture
def bot_command():
    return "/bal"


@pytest.fixture
def invalid_order():
    """return fmo"""
    return "This is not an order"


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
async def test_search_valid_order(fmo, order_standard_crypto):
    """Search Testing"""
    print(settings)
    assert await fmo.search(order_standard_crypto) is True


@pytest.mark.asyncio
async def test_search_normal_order_variation(fmo, order_standard_crypto):
    """Search Testing"""
    assert await fmo.search(order_standard_crypto) is True


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
async def test_search_standard_order(fmo, order_standard):
    """Search Testing"""
    assert await fmo.search(order_standard) is True


@pytest.mark.asyncio
async def test_identify_order(fmo, order_basic):
    """Identify Testing"""
    result = await fmo.identify_order(order_basic)
    assert result is not None


@pytest.mark.asyncio
async def test_identify_order_invalid_input(fmo, invalid_order):
    """Identify Testing"""
    result = await fmo.identify_order(invalid_order)
    print(result)
    assert result is None


@pytest.mark.asyncio
async def test_identify_order_2(fmo, order_format_2):
    """Identify Testing"""
    result = await fmo.identify_order(order_format_2)
    assert result is None


@pytest.mark.asyncio
async def test_identify_order_3(fmo, order_format_3):
    """Identify Testing"""
    result = await fmo.identify_order(order_format_3)
    assert result is None


@pytest.mark.asyncio
async def test_replace_instrument(fmo, order_basic_crypto, result_crypto_order):
    """replace instrument Testing"""
    result = await fmo.get_order(order_basic_crypto)
    print(result)
    assert result["instrument"] == result_crypto_order["instrument"]
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
async def test_basic_valid_get_order(fmo, order_basic, result_order):
    """get order Testing"""
    result = await fmo.get_order(order_basic)
    assert result["action"] == result_order["action"]
    assert result["instrument"] == result_order["instrument"]
    assert int(result["quantity"]) == 1
    assert type(result["timestamp"] is datetime)


async def test_standard_get_order(fmo, order_standard, result_order):
    """get order Testing"""
    result = await fmo.get_order(order_standard)
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
