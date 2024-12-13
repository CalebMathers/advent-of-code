"""Day 2 of advent of code 2024."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def convert_list(reports: list[str]) -> list[list[int]]:
    """Converts the given list of reports to a list
    of lists of ints."""
    return [[int(num) for num in level.split(" ")] for level in reports]


def determine_line_safety(levels: list[int]) -> bool:
    """Returns true if the line is safe, else false."""
    pass


def find_total_safe(reports: list[list[int]]) -> int:
    """Returns the total number of safe reports."""
    pass


if __name__ == "__main__":
    reports_input = (read_input("data/day_2_data.txt"))
    converted_reports = convert_list(reports_input)

    print(converted_reports)
