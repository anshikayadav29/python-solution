import asyncio

async def worker(queue):
    while True:
        priority, task_name = await queue.get()
        print(f"Processing {task_name} (Priority: {priority})")
        queue.task_done()

async def main():
    queue = asyncio.PriorityQueue()
    await queue.put((1, "Critical Update"))
    await queue.put((3, "Background Sync"))
    await worker(queue)
