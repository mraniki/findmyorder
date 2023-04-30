"""
Provides sexample for FindMyOrder
"""

import asyncio
import logging

import uvicorn
from fastapi import FastAPI
from findmyorder import FindMyOrder, __version__

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level="INFO"
)

logger =  logging.getLogger(__name__)

async def main():
    """Main"""
    while True:
        try:

            fmo = FindMyOrder()
            print(fmo)
            logger.debug("findmyorder logger: %s version: %s", __name__, __version__)
            msg_order = "this is a test"

            order = await fmo.search(msg_order)
            logger.debug("search 1: %s", order)

            msg_order = "buy btc"
            order = await fmo.search(msg_order)
            logger.debug("search 2: %s", order)
            order = await fmo.identify_order(msg_order)
            logger.info("identify_order 2: %s", order)

            msg_order = "SELL BTC 1%"
            order = await fmo.get_order(msg_order)
            logger.info("get_order 1 %s", order)
            msg_order = "SELL BTCUSDT 1%"
            order = await fmo.get_order(msg_order)
            logger.info("get_order 2: %s", order)

            msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
            order = await fmo.get_order(msg_order)
            logger.info("get_order 3: %s", order)

            msg_order = "sell EURGBP sl=200 tp=400 q=2%"
            order = await fmo.get_order(msg_order)
            logger.info("get_order 4: %s", order)
            logger.info("action 4: %s",order['action'])
            logger.info("instrument 4: %s", order['instrument'])

            await asyncio.sleep(7200)

        except Exception as e:
            logger.error("error search %s", e)


app = FastAPI()


@app.on_event("startup")
async def start():
    """startup"""
    asyncio.create_task(main())


@app.get("/")
def read_root():
    """root"""
    return {"FMO is online"}


@app.get("/health")
def health_check():
    """healthcheck"""
    return {"FMO is online"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
