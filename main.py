from models.process import Process, SchedulingResult

p = Process("P1", 0, 5)
r = SchedulingResult("P1", 0, 5, 0, 5)

print(r.waiting_time, r.turnaround_time, r.response_time)