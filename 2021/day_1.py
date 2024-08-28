"""Day 1 of the advent of code 2021"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def count_increases(data: list[str]) -> int:
    """Counts the number of time a num in the list is larger than
    that before it"""
    count = 0
    for i, num in enumerate(data):
        if not i == 0:
            if int(num.strip()) > int(data[i-1].strip()):
                count += 1

    return count


if __name__ == "__main__":
    data = read_input("day_1_data.txt")
    print(f"There are {count_increases(data)} increases")
