from fastapi import FastAPI,Request
from prometheus_fastapi_instrumentator import Instrumentator
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary,Counter,Histogram,Gauge
import time
import logging

class CustomHandler(logging.Logger):
    def __init__(self, name):

        return super(CustomHandler, self).__init__(name)      

    def warning(self, msg, level = "INFO"):
        msg = f"[{level}]:{msg}"
        return super(CustomHandler, self).warning(msg)

app = FastAPI(timeout = 60)
logging.basicConfig(level=logging.WARNING)
logger = CustomHandler(__name__)
graphs = {}
graphs['c'] = Counter('python_requests_operations_total','The total number of processed requests')
graphs['h'] = Histogram('python_requests_duration_seconds','Histogram for the duration in seconds')
# Initialize the Instrumentator
#  "/metrics" endpoint is exposed by default
Instrumentator().instrument(app).expose(app)

@app.post("/monitor-metrics")
async def monitor_metrics(request: Request):
    json_data = await request.json()
    latency = json_data["latency"]
    graphs['c'].inc()
    logger.warning(latency)
    graphs['h'].observe(latency)

    return 'Ok', 200