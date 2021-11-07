from fastapi import APIRouter, Body , Depends, FastAPI
import requests
import json
from blocks import Block
from blockchain import *
import uvicorn

blockchain = Blockchain()

app = FastAPI()

@app.get("/chain", response_description="All blocks Retrieved")
async def get_outputs():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
    # chain_data = blockchain.chain
    # return chain_data

@app.post("/chain", response_description="Block Requested to be Added to Chain")
async def get_outputs(transaction):
    blockchain.add_new_transaction(transaction)

    result = blockchain.mine()

    return result

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "This is the Blockchains Backend"}