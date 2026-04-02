from models.process import SchedulingResult

def fcfs(processes):
    # Sort by arrival time
    processes = sorted(processes, key=lambda x: x.arrival_time)

    current_time = 0
    results = []

    for p in processes:
        # If CPU is idle, jump to arrival time
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        start_time = current_time
        finish_time = start_time + p.burst_time

        result = SchedulingResult(
            p.pid,
            p.arrival_time,
            p.burst_time,
            start_time,
            finish_time
        )

        results.append(result)

        current_time = finish_time

    return results