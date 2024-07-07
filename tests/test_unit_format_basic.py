"""
FindMyOrder Unit Testing
"""

from datetime import datetime

import pytest

from findmyorder import FindMyOrder
from findmyorder.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="basic")


@pytest.fixture(name="fmo")
def fmo():
    """return fmo"""
    return FindMyOrder()


@pytest.fixture
def order():
    """return valid order"""
    return "Short ETH"


@pytest.fixture
def result_order():
    """return standard expected results"""
    return {
        "action": "SHORT",
        "instrument": "WETH",
        "timestamp": datetime.now(),
    }


@pytest.mark.asyncio
async def test_settings():
    """Search Testing"""
    assert settings.VALUE == "On Testing"
    assert settings.findmyorder_enabled is True


@pytest.mark.asyncio
async def test_identify_order(fmo, order, result_order):
    """Identify Testing"""
    result = await fmo.identify_order(order)
    assert result is not None


async def test_standard_get_order(fmo, order, result_order):
    """get order Testing"""
    result = await fmo.get_order(order)
    print(result)
    assert result["action"] == result_order["action"]
    assert result["instrument"] == result_order["instrument"]
    assert type(result["timestamp"] is datetime)
