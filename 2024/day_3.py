"""Day 3 of advent of code 2024."""

import re


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    raw_data = read_input("data/day_3_data.txt")
    print(raw_data)
