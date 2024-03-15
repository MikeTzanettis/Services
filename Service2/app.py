from fastapi import FastAPI,Request
import aiohttp
import time
import itertools
import random
import requests

app = FastAPI()
service_3_url = "http://192.168.49.2:30005/find_divisible_by_7"
metrics_exporter_url = "http://service-metrics-exporter:7001/monitor-metrics"

@app.post("/calculate-distance")
async def calculate_distance(request: Request):
    json_data = await request.json()
    start_time = json_data["start-time"]
    divisible_by_5 = []

    for i in range(20):
        if i % 5 == 0:
            divisible_by_5.append(i)
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://service-service-3:6689/find_divisible_by_7',json=json_data) as response:
            data = await response.json()
            
    #_ = requests.post(f"http://service-service-3:6689/find_divisible_by_7",json=json_data)
    # end = time.time()
    # latency = end - start_time
    # json_data["latency"] = latency
    # _ = requests.post(metrics_exporter_url,json=json_data)
    
    return "Ok",202