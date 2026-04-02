from models.process import Process
from scheduler.sjf import sjf
from metrics.metrics import calculate_metrics
from scheduler.rr import round_robin


processes = [
    Process("P1", 0, 5),
    Process("P2", 1, 4),
    Process("P3", 2, 2)
]

# THEN call algorithm
results = round_robin(processes, quantum=2)
metrics = calculate_metrics(results)

print("\nRound Robin Results:")
for r in results:
    print(r.pid, r.start_time, r.finish_time, r.waiting_time, r.turnaround_time)

print("\nMetrics:")
for k, v in metrics.items():
    print(f"{k}: {v:.2f}")