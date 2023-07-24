"""
Provides example for FindMyOrder
"""

import asyncio
import sys

import uvicorn
from fastapi import FastAPI
from loguru import logger

from findmyorder import FindMyOrder, __version__

logger.remove()
logger.add(sys.stderr, level="INFO")

async def main():
    """Main"""
    while True:
        fmo = FindMyOrder()
        print(fmo)

        msg_order = ""
        await fmo.search(msg_order)

        msg_order = "this is a test"
        await fmo.search(msg_order)

        msg_order = "buy btc"
        await fmo.search(msg_order)
        await fmo.identify_order(msg_order)

        msg_order = "SELL BTC 1%"
        await fmo.get_order(msg_order)
        msg_order = "SELL BTCUSDT 1%"
        await fmo.get_order(msg_order)

        msg_order = "buy EURUSD sl=1000 tp=1000 q=1 comment=FOMC"
        await fmo.get_order(msg_order)

        msg_order = "sell EURGBP sl=200 tp=400 q=2%"
        await fmo.get_order(msg_order)

        await asyncio.sleep(7200)


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
