import time
import asyncio

results = []


async def do_some_work(num):
    await asyncio.sleep(0.1)
    results.append(num)
    return num * 100


async def worker_function(name, work_list):
    print(f"Execute task {name}")
    for i, work in enumerate(work_list):
        await do_some_work(work)
        print(f"Time: {time.time() - start_time:.4f} Task {name}: done {i+1} jobs")


task_descriptions = [
    ("work_1", range(0, 3)),
    ("work_2", range(6, 10)),
]

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(worker_function(task_name, work_list))
    for task_name, work_list in task_descriptions
]

start_time = time.time()

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print(results)  # output: [0, 6, 1, 7, 2, 8, 9]


async def manager_function(task_descriptions):
    outputs = await asyncio.gather(
        *[
            do_some_work(work)
            for task_name, work_list in task_descriptions
            for work in work_list
        ]
    )

    print(f"Outputs: {outputs}")  # output: [0, 100, 200, 600, 700, 800, 900]


asyncio.run(manager_function(task_descriptions))
