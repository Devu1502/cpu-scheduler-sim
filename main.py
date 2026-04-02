from models.process import Process
from scheduler.sjf import sjf
from metrics.metrics import calculate_metrics

processes = [
    Process("P1", 0, 4),
    Process("P2", 1, 3),
    Process("P3", 2, 2)
]

# THEN call algorithm
results = sjf(processes)
metrics = calculate_metrics(results)

print("\nSJF Results:")
for r in results:
    print(r.pid, r.start_time, r.finish_time, r.waiting_time, r.turnaround_time)

print("\nMetrics:")
for k, v in metrics.items():
    print(f"{k}: {v:.2f}")