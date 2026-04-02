def calculate_metrics(results):
    n = len(results)

    total_waiting = sum(r.waiting_time for r in results)
    total_turnaround = sum(r.turnaround_time for r in results)
    total_burst = sum(r.burst_time for r in results)
    total_time = max(r.finish_time for r in results)

    avg_waiting_time = total_waiting / n
    avg_turnaround_time = total_turnaround / n
    cpu_utilization = (total_burst / total_time) * 100
    throughput = n / total_time

    return {
        "AWT": avg_waiting_time,
        "ATT": avg_turnaround_time,
        "CPU Utilization": cpu_utilization,
        "Throughput": throughput
    }