"""Day 5 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def check_nice_string(string_to_check: str) -> bool:
    """Returns true if the string is 'nice', else returns false."""


def find_nice_strings(all_strings: list[str]) -> list[str]:
    """Returns every string that is deemed nice as per
    Santa's odd standards."""


if __name__ == "__main__":
    print(read_input("./data/day_5_data.txt"))
