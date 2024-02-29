from fastapi import FastAPI,Request
import time
import itertools
import random
import requests

app = FastAPI()
service_3_url = "http://192.168.49.2:30005/find_divisible_by_7"
metrics_exporter_url = "http://192.168.49.2:30007/monitor-metrics?latency="

@app.post("/calculate-distance")
async def calculate_distance(request: Request):
    json_data = await request.json()
    divisible_by_5 = []

    for i in range(50):
        if i % 5 == 0:
            divisible_by_5.append(i)
    total_sum = sum(divisible_by_5)
    json_data["div5"] = total_sum
    _ = requests.post(f"http://192.168.49.2:30005/find_divisible_by_7",json=json_data)
    # end = time.time()
    # latency = end - start_time
    # metrics_url = metrics_exporter_url+str(latency)
    # _ = requests.get(metrics_url)
    
    return "Ok",202