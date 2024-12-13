"""Day 2 of advent of code 2024."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def convert_list(reports: list[str]) -> list[list[int]]:
    """Converts the given list of reports to a list
    of lists of ints."""
    return [[int(num) for num in level.split(" ")] for level in reports]


def determine_report_safety(levels: list[int]) -> bool:
    """Returns true if the line is safe, else false."""

    # check for all increasing by 1 to 3
    if (all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
            and all(abs(levels[i] - levels[i + 1]) in [1, 2, 3] for i in range(len(levels) - 1))):
        return True

    # check for all decreasing by 1 to 3
    if (all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
            and all(abs(levels[i] - levels[i + 1]) in [1, 2, 3] for i in range(len(levels) - 1))):
        return True

    return False


def find_total_safe(reports: list[list[int]]) -> int:
    """Returns the total number of safe reports."""
    safe_count = 0

    for report in reports:
        if determine_report_safety(report):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    reports_input = (read_input("data/day_2_data.txt"))
    converted_reports = convert_list(reports_input)

    print(find_total_safe(converted_reports))
