from models.process import SchedulingResult
from collections import deque

def round_robin(processes, quantum=2):
    processes = sorted(processes, key=lambda x: x.arrival_time)

    queue = deque()
    time = 0
    i = 0
    n = len(processes)

    remaining = {p.pid: p.burst_time for p in processes}
    start_times = {}
    results = {}

    while len(results) < n:
        while i < n and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time = processes[i].arrival_time
            continue

        current = queue.popleft()

        # First time execution
        if current.pid not in start_times:
            start_times[current.pid] = time

        exec_time = min(quantum, remaining[current.pid])
        remaining[current.pid] -= exec_time
        time += exec_time

        while i < n and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if remaining[current.pid] > 0:
            queue.append(current)
        else:
            finish_time = time
            result = SchedulingResult(
                current.pid,
                current.arrival_time,
                current.burst_time,
                start_times[current.pid],
                finish_time
            )
            results[current.pid] = result

    return list(results.values())