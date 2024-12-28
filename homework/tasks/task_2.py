async def magic_func() -> int:
    """
    Get number 42

    :return: number 42
    """

    return 42


async def fix_this_code() -> int:
    """
    Call function magic_func

    :return: magic_func result
    """

    return await magic_func()


if __name__ == '__main__':
    pass
