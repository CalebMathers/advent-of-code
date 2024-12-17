"""Day 3 of advent of code 2024."""

import re


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def find_uncorrupted_instructions(corrupted_data: str) -> list[str]:
    """Returns a list of all the uncorrupted multiplication instructions
    from a string containing corrupted data."""
    uncorrupted_pattern = r"mul\(\d{1,3},\d{1,3}\)"

    multiply_calls = re.findall(uncorrupted_pattern, corrupted_data)

    return multiply_calls


def carry_out_multiplications(uncorrupted_calls: list[str]) -> int:
    """Returns the total sum of all the products of each
    uncorrupted multiplication call."""
    total = 0

    for mul_call in uncorrupted_calls:
        nums = mul_call.removeprefix("mul(").removesuffix(")").split(",")
        total += int(nums[0]) * int(nums[1])

    return total


if __name__ == "__main__":
    raw_data = read_input("data/day_3_data.txt")

    uncorrupted_data = find_uncorrupted_instructions(raw_data)
    total_result = carry_out_multiplications(uncorrupted_data)
    print(f"The total of all part one multiplications is: {total_result}")
