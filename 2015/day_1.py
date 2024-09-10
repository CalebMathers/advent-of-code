"""Day 1 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def get_final_destination(movements: str) -> int:
    """Returns the final floor after a serious of movements given."""
    return movements.count("(") - movements.count(")")


def get_basement_index(movements: str) -> int:
    """Returns the index in which the basement is entered."""
    for i in range(len(movements)):
        if movements[:i].count(")") > movements[:i].count("("):
            return i

    return None


if __name__ == "__main__":
    floor_movements = read_input("./data/day_1_data.txt")
    print(get_final_destination(floor_movements))
    print(get_basement_index(floor_movements))
