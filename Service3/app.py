from fastapi import FastAPI,Request
import requests
import time

app = FastAPI(timeout = 60)
metrics_exporter_url = "http://service-metrics-exporter:7001/monitor-metrics"
@app.post("/find_divisible_by_7")
async def find_numbers_divisible_by_7(request: Request):
    divisible_by_7 = []
    json_data = await request.json()
    start_time = json_data["start-time"]
    for i in range(20):
        if i % 7 == 0:
            divisible_by_7.append(i)
    end = time.time()
    latency = end - start_time
    json_data["latency"] = latency
    _ = requests.post(metrics_exporter_url,json=json_data)
    return "Ok",202