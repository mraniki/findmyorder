"""
FindMyOrder Exception Testing
"""

import pytest

from findmyorder import FindMyOrder
from findmyorder.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="exception")


@pytest.fixture(name="fmo")
def fmo():
    """return fmo"""
    return FindMyOrder()


async def test_module_exception(fmo, caplog):
    result = FindMyOrder()
    print(result)
    assert any(
        record.message == "FindMyOrder is disabled. No Parser will be created."
        for record in caplog.records
        if record.levelname == "INFO"
    )


async def test_create_client_exception(fmo, caplog):
    fmo.enabled = True
    result = fmo.create_client()
    print(result)
    assert result is not None
    assert any(
        record.message
        == "No Client were created. Check your settings or disable the module."
        for record in caplog.records
        if record.levelname == "WARNING"
    )
