import sys
import os
from queue import Queue
from Jobs import Jobs

def get_parameters(raw_parameters):
    time_slice = int(raw_parameters[1])
    jobs_list = raw_parameters[2].split(',')
    jobs_list = [int(i) for i in jobs_list]
    return [time_slice, jobs_list]

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
    jobs_record = [i for i in jobs_queue]
    runtime = 0
    runtime_time_slice = 0
    job_finished = False
    while True:
        if len(jobs_queue) == 0:
            break
        if jobs_queue[0].time_requested <= 0:
            finished = jobs_queue.pop(0)
            for i in jobs_record:
                if i.tag == finished.tag:
                    i.finished = True
            job_finished = True
            runtime_time_slice = 0
            continue
        if runtime_time_slice == time_slice and runtime != 0 and not job_finished:
            temp = jobs_queue.pop(0)
            job_queue.append(temp)
            runtime_time_slice = 0
        current_job = jobs_queue[0]
        jobs_queue[0].time_requested -= 1
        job_finished = False
        print('%5s'%(runtime), end='')
        for i in jobs_record:
            if i.tag == current_job.tag:
                print('%5s'%('X'), end='')
            elif i.finished:
                print('%5s'%('F'), end='')
            else:
                print('%5s'%(' '), end='')
        print()
        runtime += 1
        runtime_time_slice += 1

#index      data
#    0      time slice
#    1      jobs          
if len(sys.argv) != 3:
    print('usage: python RoundRobin.py <TimeSlice> <Job1, Job2, ...>')
    print('Example: python RoundRobin.py 2 20,30,20')
    sys.exit(1)
user_input = get_parameters(list(sys.argv))
job_queue = build_job_queue(user_input[1])
print_header(job_queue)
round_robin(user_input[0], job_queue)
