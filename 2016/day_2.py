"""Day 2 of the advent of code 2016."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def move_up(current_num: int) -> int:
    """Returns the new num selected on the keypad after up movement."""
    if current_num in [1, 2, 3]:
        return current_num

    return current_num - 3


def move_down(current_num: int) -> int:
    """Returns the new num selected on the keypad after down movement."""
    if current_num in [7, 8, 9]:
        return current_num

    return current_num + 3


def move_left(current_num: int) -> int:
    """Returns the new num selected on the keypad after left movement."""
    if current_num in [1, 4, 7]:
        return current_num

    return current_num - 1


def move_right(current_num: int) -> int:
    """Returns the new num selected on the keypad after right movement."""
    if current_num in [3, 6, 9]:
        return current_num

    return current_num + 1


def find_code(instructions: list[str]) -> str:
    """Conducts the movements for each instruction line and returns
    the keypad code."""
    code = ""
    current_num = 5

    for instruction in instructions:
        for movement in instruction:
            if movement == "U":
                current_num = move_up(current_num)
            elif movement == "D":
                current_num = move_down(current_num)
            elif movement == "L":
                current_num = move_left(current_num)
            else:
                current_num = move_right(current_num)

        code += str(current_num)

    return code


def new_move_up(current_num: str) -> str:
    """Returns the new num selected on the keypad after up movement."""
    up_movements = {'1': '1', '2': '2', '3': '1', '4': '4',
                    '5': '5', '6': '2', '7': '3', '8': '4', '9': '9',
                    'A': '6', 'B': '7', 'C': '8', 'D': 'B'}

    return up_movements[current_num]


def new_move_down(current_num: str) -> str:
    """Returns the new num selected on the keypad after down movement."""
    down_movements = {'1': '3', '2': '6', '3': '7', '4': '8',
                      '5': '5', '6': 'A', '7': 'B', '8': 'C', '9': '9',
                      'A': 'A', 'B': 'D', 'C': 'C', 'D': 'D'}

    return down_movements[current_num]


def new_move_left(current_num: str) -> str:
    """Returns the new num selected on the keypad after left movement."""
    left_movements = {'1': '1', '2': '2', '3': '2', '4': '3',
                      '5': '5', '6': '5', '7': '6', '8': '7', '9': '8',
                      'A': 'A', 'B': 'A', 'C': 'B', 'D': 'D'}

    return left_movements[current_num]


def new_move_right(current_num: str) -> str:
    """Returns the new num selected on the keypad after right movement."""
    left_movements = {'1': '1', '2': '3', '3': '4', '4': '4',
                      '5': '6', '6': '7', '7': '8', '8': '9', '9': '9',
                      'A': 'B', 'B': 'C', 'C': 'C', 'D': 'D'}

    return left_movements[current_num]


def new_find_code(instructions: list[str]) -> str:
    """Conducts the movements for each instruction line and returns
    the keypad code."""
    code = ""
    current_num = '5'

    for instruction in instructions:
        for movement in instruction:
            if movement == "U":
                current_num = new_move_up(current_num)
            elif movement == "D":
                current_num = new_move_down(current_num)
            elif movement == "L":
                current_num = new_move_left(current_num)
            else:
                current_num = new_move_right(current_num)

        code += current_num

    return code


if __name__ == "__main__":
    movements_data = read_input("data/day_2_data.txt")

    part_one_code = find_code(movements_data)
    print(f"The code for the first keypad is {part_one_code}")

    part_two_code = new_find_code(movements_data)
    print(f"The code for the first keypad is {part_two_code}")
