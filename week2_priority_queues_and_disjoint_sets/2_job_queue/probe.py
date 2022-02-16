# python3


def assign_jobs(n_workers, jobs):
    threads_time = [0] * n_workers
    assigned_jobs = []
    for i in range(0, len(jobs)):
        thread_start = min(threads_time)
        thread_index = threads_time.index(thread_start)
        threads_time[thread_index] += jobs[i]
        assigned_jobs.append([thread_index, thread_start])
    return assigned_jobs


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for thread, time in assigned_jobs:
        print(thread, time)


if __name__ == "__main__":
    main()