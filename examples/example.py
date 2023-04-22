

import sys, os, asyncio, requests, logging

from web3 import Web3

from fastapi import FastAPI
import uvicorn


from findmyorder import findmyorder
#DEBUG LEVEL for DXSP package
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('findmyorder.__main__').setLevel(logging.DEBUG)


async def main():
	while True:

  fmo = findmyorder()
  
  msg_test = "this is a test"
  
  order = fmo.search(msg_test)
  print(order)
  
  msg_order = "buy btc"
  order = fmo.search(msg_order)
  print(order)

		await asyncio.sleep(3600)


app = FastAPI()

@app.on_event('startup')
async def start():
    asyncio.create_task(main())

@app.get("/")
def read_root():
    return {"FMY is online"}

@app.get("/health")
def health_check():
    return {"FMO is online"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

