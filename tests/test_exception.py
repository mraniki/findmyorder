# """
# FindMyOrder Exception Testing
# """

# import pytest

# from findmyorder import FindMyOrder
# from findmyorder.config import settings


# @pytest.fixture(scope="session", autouse=True)
# def set_test_settings():
#     settings.configure(FORCE_ENV_FOR_DYNACONF="exception")


# @pytest.fixture(name="fmo")
# def fmo():
#     """return fmo"""
#     return FindMyOrder()


# @pytest.mark.asyncio
# async def test_exception(fmo):
#     """Search Testing"""
#     for client in fmo.clients:
#         assert client is None
