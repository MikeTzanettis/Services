from fastapi import FastAPI
import time
import aiohttp

app = FastAPI()

async def fetch_data():
    start = time.time()
    json_data = {"start-time": start, "number":5}
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://192.168.49.2:30001/fibonacci',json=json_data) as response:
            data = await response.json()
            return data

@app.get("/gateway-service")
async def gateway_service():
    data = await fetch_data()
    return {"message": "Service started successfully", "data": data}