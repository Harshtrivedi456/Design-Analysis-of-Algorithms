# Job Scheduling with Deadlines and Profits (Greedy Optimal)

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    scheduled_jobs = []
    for job_id, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job_id
                scheduled_jobs.append(job_id)
                total_profit += profit
                break
    return scheduled_jobs, total_profit


jobs = [('A', 2, 100), ('B', 1, 19), ('C', 2, 27), ('D', 1, 25), ('E', 3, 15)]
scheduled, profit = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled)
print("Total Profit:", profit)
