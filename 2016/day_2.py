"""Day 2 of the advent of code 2016."""


def move_up(current_num: int) -> int:
    """"""
    if current_num in [1, 2, 3]:
        return current_num

    return current_num - 3


def move_down(current_num: int) -> int:
    """"""
    if current_num in [7, 8, 9]:
        return current_num

    return current_num + 3


def move_left(current_num: int) -> int:
    """"""
    if current_num in [1, 4, 7]:
        return current_num

    return current_num - 1


def move_right(current_num: int) -> int:
    """"""
    if current_num in [3, 6, 9]:
        return current_num

    return current_num + 1


if __name__ == "__main__":
    pass
