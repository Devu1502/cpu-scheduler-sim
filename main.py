from models.process import Process
from scheduler.fcfs import fcfs

processes = [
    Process("P1", 0, 4),
    Process("P2", 1, 3),
    Process("P3", 2, 2)
]

results = fcfs(processes)

for r in results:
    print(r.pid, r.start_time, r.finish_time, r.waiting_time, r.turnaround_time)