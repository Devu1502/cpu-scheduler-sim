from models.process import SchedulingResult

def sjf(processes):
    processes = sorted(processes, key=lambda x: x.arrival_time)

    completed = []
    ready_queue = []
    current_time = 0
    i = 0
    n = len(processes)

    while len(completed) < n:
        # Add arrived processes to ready queue
        while i < n and processes[i].arrival_time <= current_time:
            ready_queue.append(processes[i])
            i += 1

        if not ready_queue:
            current_time = processes[i].arrival_time
            continue

        # Pick process with shortest burst time
        ready_queue.sort(key=lambda x: x.burst_time)
        p = ready_queue.pop(0)

        start_time = current_time
        finish_time = start_time + p.burst_time

        result = SchedulingResult(
            p.pid,
            p.arrival_time,
            p.burst_time,
            start_time,
            finish_time
        )

        completed.append(result)
        current_time = finish_time

    return completed