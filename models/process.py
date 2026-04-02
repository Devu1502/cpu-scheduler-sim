class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority


class SchedulingResult:
    def __init__(self, pid, arrival_time, burst_time, start_time, finish_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = start_time
        self.finish_time = finish_time

        self.turnaround_time = self.finish_time - self.arrival_time
        self.waiting_time = self.turnaround_time - self.burst_time
        self.response_time = self.start_time - self.arrival_time