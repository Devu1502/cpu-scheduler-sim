from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.rr import round_robin
from scheduler.srtf import srtf
from scheduler.hrrn import hrrn
from metrics.metrics import calculate_metrics
from models.process import Process

processes = [
    Process("P1", 0, 5),
    Process("P2", 1, 4),
    Process("P3", 2, 2)
]

algorithms = {
    "FCFS": fcfs,
    "SJF": sjf,
    "RR": lambda p: round_robin(p, quantum=2),
    "SRTF": srtf,
    "HRRN": hrrn
}

print("\n=== Algorithm Comparison ===\n")

for name, algo in algorithms.items():
    results = algo(processes)
    metrics = calculate_metrics(results)

    print(f"{name}:")
    for k, v in metrics.items():
        print(f"  {k}: {v:.2f}")
    print()