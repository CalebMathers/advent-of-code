"""Day 3 of advent of code 2024."""

import re


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def find_uncorrupted_instructions(corrupted_data: str) -> list[str]:
    """Returns a list of all the uncorrupted multiplication instructions
    from a string containing corrupted data."""
    uncorrupted_pattern = r'mul\(\d{1,3},\d{1,3}\)'

    multiply_calls = re.findall(uncorrupted_pattern, corrupted_data)

    return multiply_calls


if __name__ == "__main__":
    raw_data = read_input("data/day_3_data.txt")

    print(find_uncorrupted_instructions(raw_data))
