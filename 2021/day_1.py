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


def create_windows(data: list[str]) -> list[str]:
    """Creates measurement windows"""
    windows = []
    for i, num in enumerate(data):
        if not i >= (len(data) - 2):
            current_sum = int(num.strip())
            current_sum += int(data[i+1].strip())
            current_sum += int(data[i+2].strip())
            windows.append(str(current_sum))

    return windows


if __name__ == "__main__":
    num_list = read_input("day_1_data.txt")
    print(f"There are {count_increases(num_list)} increases")
    windowed_data = create_windows(num_list)
    print(f"There are {count_increases(windowed_data)}" +
          " increases when working with three measurement windows")
