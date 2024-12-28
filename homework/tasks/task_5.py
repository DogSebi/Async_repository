import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float)\
      -> None:
    """
    Execute one coroutine with time limit

    :param coro: coroutine to execute
    :param max_execution_time: time limit
    """

    async with asyncio.timeout(max_execution_time):
        await coro


async def limit_execution_time_many(
        *coros: Coroutine, max_execution_time: float
        ) -> None:
    """
    Execute several coroutines with time limit

    :param max_execution_time: time limit
    """

    tasks = [asyncio.create_task(coro) for coro in coros]
    _, pending = await asyncio.wait(tasks, timeout=max_execution_time)
    for task in pending:
        task.cancel()
