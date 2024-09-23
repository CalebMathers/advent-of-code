"""Day 8 for the advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip()for line in f.readlines()]


def count_all_strings(strings: list[str]) -> tuple[int, int]:
    """Counts every string given and returns the total number of
    characters, and the total of each literal string."""
    total_code = 0
    total_memory = 0

    for string in strings:
        counts = count_string(string)
        total_code += counts[0]
        total_memory += counts[1]

    return (total_code, total_memory)


def count_string(string: str) -> tuple[int, int]:
    """Returns the count of the total number of characters, and the
    number of characters in the literal string represented."""
    code_count = len(string)

    evaluated_string = string.encode().decode("unicode-escape")[1:-1]
    memory_count = len(evaluated_string)

    test = len(fr'"{string.replace('"', 'bb')}"') + 2

    return (code_count, memory_count, test)


if __name__ == "__main__":
    # data = read_input("./data/day_8_test_data.txt")
    # code_total, memory_total = (count_all_strings(data))
    # print(f"Answer to part one: {code_total - memory_total}")
    print(count_string('"\x27"'))
