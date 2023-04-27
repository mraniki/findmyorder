import asyncio, logging
from fastapi import FastAPI
import uvicorn

from findmyorder import findmyorder
from findmyorder import __version__

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level='DEBUG')
logger =  logging.getLogger(__name__)


async def main():
    while True:
        try:
            fmo = findmyorder()
            print(fmo)
            logger.debug(f"findmyorder logger: {__name__} version: {__version__}")
            msg_order = "this is a test"

            order = fmo.search(msg_order)
            logger.debug(f"search 1: {order}")
            order = fmo.identify_order(msg_order)
            logger.info(f"identify_order 1: {order}")

            msg_order = "buy btc"

            order = fmo.search(msg_order)
            logger.debug(f"search 2: {order}")
            order = fmo.identify_order(msg_order)
            logger.info(msg=f"identify_order 2: {order}")

            msg_order = "SELL BTC 1%"
            order = fmo.get_order(msg_order)
            logger.info(f"get_order 1 : {order}")

            msg_order = "SELL BTCUSDT 1%"
            order = fmo.get_order(msg_order)
            logger.info(f"get_order 2: {order}")

            msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
            order = fmo.get_order(msg_order)
            logger.info(f"get_order 3: {order}")


            await asyncio.sleep(10000)
        except Exception as e:
            logger.error(f"error search {e}")


app = FastAPI()

@app.on_event('startup')
async def start():
    asyncio.create_task(main())

@app.get("/")
def read_root():
    return {"FMO is online"}

@app.get("/health")
def health_check():
    return {"FMO is online"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

