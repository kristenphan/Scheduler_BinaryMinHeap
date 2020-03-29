# python3

from collections import namedtuple
import heapq

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

# this function returns a list of tuples that states the index of the worker
# who was assigned a particular job (sorted in the same order as jobs in list jobs)
# and the time the worker started working on the job
def assign_jobs(n_workers, jobs):
    # create a list of pairs that contains the next free time and the index of a particular worker
    # initialize the next free time of all workers to 0 as initially they have not started working on any job yet
    workers_heap = []
    for idx in range(n_workers):
        workers_heap.append([0,idx])
    # heapify the list of workers so that they are arranged into min-binary heap
    # with the worker who will be available the earliest and has the smallest index sorted first
    heapq.heapify(workers_heap)
    # create a list to store the results
    results = []
    for idx, job in enumerate(jobs):
        # find the next worker by popping the smallest item from the workers_heap priority queue
        next_worker = heapq.heappop(workers_heap)
        # record the index of the worker who was assigned the job and the starting time
        results.append((next_worker[1], next_worker[0]))
        # increase the next free time value of said worker by the duration of the job
        next_worker[0] += job
        # push the worker back on the queue
        heapq.heappush(workers_heap,next_worker)

    return results



if __name__ == "__main__":
    main()
