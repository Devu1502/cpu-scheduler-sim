from models.process import SchedulingResult

def hrrn(processes):
    processes = sorted(processes, key=lambda x: x.arrival_time)

    completed = []
    current_time = 0
    n = len(processes)
    done = set()

    while len(completed) < n:
        # Get available processes
        available = [p for p in processes if p.arrival_time <= current_time and p.pid not in done]

        if not available:
            current_time += 1
            continue

        # Calculate response ratio
        def response_ratio(p):
            waiting = current_time - p.arrival_time
            return (waiting + p.burst_time) / p.burst_time

        # Pick highest ratio
        current = max(available, key=response_ratio)

        start_time = current_time
        finish_time = start_time + current.burst_time

        result = SchedulingResult(
            current.pid,
            current.arrival_time,
            current.burst_time,
            start_time,
            finish_time
        )

        completed.append(result)
        done.add(current.pid)
        current_time = finish_time

    return completed