from models.process import SchedulingResult

def srtf(processes):
    processes = sorted(processes, key=lambda x: x.arrival_time)

    n = len(processes)
    remaining = {p.pid: p.burst_time for p in processes}
    start_times = {}
    finish_times = {}

    time = 0
    completed = 0

    while completed < n:
        # Get available processes
        available = [p for p in processes if p.arrival_time <= time and remaining[p.pid] > 0]

        if not available:
            time += 1
            continue

        # Picking process with shortest remaining time
        current = min(available, key=lambda x: remaining[x.pid])

        # Record first start time
        if current.pid not in start_times:
            start_times[current.pid] = time

        remaining[current.pid] -= 1
        time += 1

        # If finished
        if remaining[current.pid] == 0:
            finish_times[current.pid] = time
            completed += 1

    # Build results
    results = []
    for p in processes:
        result = SchedulingResult(
            p.pid,
            p.arrival_time,
            p.burst_time,
            start_times[p.pid],
            finish_times[p.pid]
        )
        results.append(result)

    return results