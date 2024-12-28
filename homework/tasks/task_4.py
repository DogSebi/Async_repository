result = ''


async def task_1(i: int) -> None:
    """
    Add '1' to result and call task_2 if i != 0

    :param i: counter
    """

    global result

    result += '1'

    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int) -> None:
    """
    Add '2' to result and call task_1 or task_2 if i != 0

    :param i: counter
    """

    global result

    result += '2'

    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    """
    Run the coroutines in order

    :param i: counter, defaults to 42
    :return: sequence of 1 and 2 concatenated to string
    """

    global result

    await task_1(i)
    return int(result)

if __name__ == '__main__':
    pass
