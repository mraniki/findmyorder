# """
# FindMyOrder Unit Testing
# """

# from datetime import datetime

# import pytest

# from findmyorder import FindMyOrder
# from findmyorder.config import settings


# @pytest.fixture(scope="session", autouse=True)
# def set_test_settings():
#     settings.configure(FORCE_ENV_FOR_DYNACONF="fmo")


# @pytest.fixture(name="fmo")
# def fmo():
#     """return fmo"""
#     return FindMyOrder()


# @pytest.fixture
# def order_format_2():
#     """return order 2"""
#     return """
#     📊 FUTURES Exchanges: Binance, ByBit USDT

#     #AAVEUSDT

#     🟢LONG ENTRY :- 65.20 - 63.70

#     Leverage: Cross (2X)

#     👇TAKE PROFIT

#     1) 65.70
#     2) 66.20
#     3) 66.70

#     Stop Loss : - 62.00
# """


# @pytest.fixture
# def order_format_3():
#     """return emoji type order"""
#     return """⚡️⚡️ #BNB/USDT ⚡️⚡️
#     Exchanges: ByBit USDT, Binance Futures
#     Signal Type: Regular (Long)
#     Leverage: Cross (20.0X)"""


# @pytest.fixture
# def result_order():
#     """return standard expected results"""
#     return {
#         "action": "BUY",
#         "instrument": "EURUSD",
#         "stop_loss": 200,
#         "take_profit": 400,
#         "quantity": 2,
#         "order_type": None,
#         "leverage_type": None,
#         "comment": None,
#         "timestamp": datetime.now(),
#     }

# @pytest.mark.asyncio
# async def test_settings():
#     """Search Testing"""
#     assert settings.VALUE == "On Testing"
#     assert settings.findmyorder_enabled is True

# @pytest.mark.asyncio
# async def test_identify_order_2(fmo, order_format_2):
#     """Identify Testing"""
#     result = await fmo.identify_order(order_format_2)
#     assert result is None


# @pytest.mark.asyncio
# async def test_identify_order_3(fmo, order_format_3):
#     """Identify Testing"""
#     result = await fmo.identify_order(order_format_3)
#     assert result is None


# @pytest.mark.asyncio
# async def test_identify_order_2(fmo, order_format_2):
#     """Identify Testing"""
#     result = await fmo.identify_order(order_format_2)
#     assert result is None


# @pytest.mark.asyncio
# async def test_identify_order_3(fmo, order_format_3):
#     """Identify Testing"""
#     result = await fmo.identify_order(order_format_3)
#     assert result is None

# @pytest.mark.asyncio
# async def test_basic_valid_get_order(fmo, order_basic, result_order):
#     """get order Testing"""
#     result = await fmo.get_order(order_basic)
#     assert result["action"] == result_order["action"]
#     assert result["instrument"] == result_order["instrument"]
#     assert int(result["quantity"]) == 1
#     assert type(result["timestamp"] is datetime)


# async def test_standard_get_order(fmo, order_standard, result_order):
#     """get order Testing"""
#     result = await fmo.get_order(order_standard)
#     print(result)
#     assert result["action"] == result_order["action"]
#     assert result["instrument"] == result_order["instrument"]
#     assert int(result["stop_loss"]) == result_order["stop_loss"]
#     assert int(result["take_profit"]) == result_order["take_profit"]
#     assert int(result["quantity"]) == result_order["quantity"]
#     assert result["order_type"] == result_order["order_type"]
#     assert result["leverage_type"] == result_order["leverage_type"]
#     assert result["comment"] == result_order["comment"]
#     assert type(result["timestamp"] is datetime)


# async def test_create_client_exception(fmo, caplog):
#     result = fmo.create_client(parser_library="none")
#     assert result is not None
#     assert "No Client were created" in caplog.text
