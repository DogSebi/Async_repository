from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    """
    Get the result of coroutine's execution

    :param f: coroutine's life cycle stage
    :raises ValueError: if wrong instance is passed
    :return: the result of coroutine's execution
    """

    if isinstance(f, Callable):
        return await f()
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        return await f
    else:
        raise ValueError('invalid argument')

if __name__ == '__main__':
    pass
