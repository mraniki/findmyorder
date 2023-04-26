import asyncio, logging
from fastapi import FastAPI
import uvicorn

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level='DEBUG')
logger =  logging.getLogger(__name__)

from findmyorder import findmyorder

async def main():
    while True:
        try:
            fmo = findmyorder()
            print(fmo)
            
            msg_order = "this is a test"

            order = fmo.search(msg_order)
            logger.debug(f"Order identified: {order}")
            order = fmo.get_order(msg_order)
            logger.debug(f"Order identified: {order}")

            msg_order = "buy btc"

            order = fmo.search(msg_order)
            logger.debug(f"Order identified: {order}")
            order = fmo.get_order(msg_order)
            logger.debug(msg=f"Order identified: {order}")

            msg_order = "SELL BTC 1%"

            order = fmo.search(msg_order)
            logger.debug(f"Order identified: {order}")
            order = fmo.get_order(msg_order)
            logger.debug(f"Order identified: {order}")


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

