from fastapi import FastAPI,Request
import time
import requests
import aiohttp
app = FastAPI()

metrics_exporter_url = "http://192.168.49.2:30007/monitor-metrics"
service_2_url = "http://192.168.49.2:30004/calculate-distance?sum="


@app.post("/fibonacci")
async def get_fibonacci(request: Request):
    json_data = await request.json()
    #start_time = json_data["start-time"]
    number = json_data["number"]
    fib_sequence = [0, 1]
    for _ in range(2, number):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://service-service-2:6779/calculate-distance',json=json_data) as response:
            data = await response.json()
            
    #_ = requests.post(f"http://service-service-2:6779/calculate-distance",json=json_data)

    # end = time.time()
    # latency = end - start_time
    # json_data["latency"] = latency
    # _ = requests.post(metrics_exporter_url,json = json_data)

    return "Request Received",202



# Override the default warning method with the custom handler

# To run this app   
# uvicorn api:app --reload --port 8000