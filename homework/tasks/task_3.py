import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    """
    Call all coroutines and sort results by numbers

    :param coros: coroutines to call
    :return: string of connected keys
    """

    result = await asyncio.gather(*coros)
    result.sort(key=lambda t: t.number)
    return ''.join([t.key for t in result])

if __name__ == '__main__':
    pass
