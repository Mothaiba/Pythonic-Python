import time
from concurrent import futures


def foo(num):
    print(f"Start doing with {num}")
    time.sleep(num)
    print(f"Done with {num}")
    return num * 10


# multi-threading
# # use executor.map
with futures.ThreadPoolExecutor(max_workers=2) as executor:
    threads_results = executor.map(foo, [3, 1, 2])

print(list(threads_results))  # output: [30, 10, 20]
print("\n")

# # use executor.submit and futures.as_completed
waiting_jobs = []
with futures.ThreadPoolExecutor(max_workers=2) as executor:
    for inp in range(5, 0, -1):
        future = executor.submit(foo, inp)
        waiting_jobs.append(future)

results = []
for result in futures.as_completed(waiting_jobs):
    results.append(result.result())

print(results)  # output: [40, 20, 50, 10, 30]
print("\n")


# multi-processing
# # use executor.map
with futures.ProcessPoolExecutor(max_workers=2) as executor:
    processes_results = executor.map(foo, [3, 1, 2])

print(list(processes_results))  # output: [30, 10, 20]
print("\n")

# # use executor.submit and futures.as_completed
waiting_jobs = []
with futures.ProcessPoolExecutor(max_workers=2) as executor:
    for inp in range(5, 0, -1):
        future = executor.submit(foo, inp)
        waiting_jobs.append(future)

results = []
for result in futures.as_completed(waiting_jobs):
    results.append(result.result())

print(results)  # output: [20, 40, 10, 30, 50]
print("\n")
