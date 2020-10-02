from queue import Queue
from Jobs import Jobs


def print_header(jobs):
    print('%5s'%('Time'), end='')
    for i in jobs:
        print('%5s'%(i.tag), end='')
    print()

def build_job_queue(jobs_list):
    jobs = []
    counter = 0
    for i in jobs_list:
        tag = 'J' + str(counter)
        job = Jobs(tag, i)
        jobs.append(job)
        counter += 1
    return jobs

def round_robin(time_slice, jobs_queue):
    jobs_initial_state = [i for i in jobs_queue]
    runtime = 0
    while True:
        available_jobs = False
        for i in jobs_queue:
            if i.time_requested > 0:
                available_jobs = True
                break
        if not available_jobs or len(jobs_queue) == 0:
            break
        if runtime % time_slice == 0 and runtime != 0:
            temp = jobs_queue.pop(0)
            jobs_queue.append(temp)
        print('%5s'%(runtime), end='')
        for i in jobs_initial_state:
            if i.tag == job_queue[0].tag:
                print('%5s'%('X'), end='')
                job_queue[0].time_requested -= 1
                if job_queue[0].time_requested == 0:
                    jobs_queue.pop(0)
            else:
                print('%5s'%('_'), end='')
        print()
        runtime += 1        

#jobs listed in order of arrival
jobs_list = [2, 3, 2]
time_slice = 1

job_queue = build_job_queue(jobs_list)
print_header(job_queue)
round_robin(time_slice, job_queue)