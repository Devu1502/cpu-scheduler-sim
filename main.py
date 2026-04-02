from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from models.process import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.rr import round_robin
from scheduler.srtf import srtf
from scheduler.hrrn import hrrn
from metrics.metrics import calculate_metrics

app = FastAPI()

# Request schema
class ProcessInput(BaseModel):
    pid: str
    arrival_time: int
    burst_time: int
    priority: int = 0

class ScheduleRequest(BaseModel):
    algorithm: str
    processes: List[ProcessInput]

# Algorithm map
algorithms = {
    "FCFS": fcfs,
    "SJF": sjf,
    "RR": lambda p: round_robin(p, quantum=2),
    "SRTF": srtf,
    "HRRN": hrrn
}

@app.post("/schedule")
def schedule(req: ScheduleRequest):
    processes = [
        Process(p.pid, p.arrival_time, p.burst_time, p.priority)
        for p in req.processes
    ]

    algo = algorithms.get(req.algorithm)
    if not algo:
        return {"error": "Invalid algorithm"}

    results = algo(processes)
    metrics = calculate_metrics(results)

    return {
        "results": [r.__dict__ for r in results],
        "metrics": metrics
    }