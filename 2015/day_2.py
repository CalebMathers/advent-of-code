"""Advent of code 2015 day 2"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def calculate_paper(gift_dimensions: str) -> int:
    """Takes the dimensions of a gift and returns the square feet
    of wrapping paper required"""
    dimensions = gift_dimensions.strip().split("x")
    dimensions = [int(num) for num in dimensions]
    if len(dimensions) != 3:
        raise ValueError("The dimensions string must contain 3 measurements.")

    length_width = dimensions[0] * dimensions[1]
    width_height = dimensions[1] * dimensions[2]
    height_length = dimensions[0] * dimensions[2]

    paper_needed = (2 * length_width) + \
        (2 * width_height) + (2 * height_length)
    paper_needed += min([length_width, width_height, height_length])

    return paper_needed


def calculate_total_paper(all_gift_dimensions: list[str]) -> int:
    """Calculates the total paper required"""
    total = 0

    for gift in all_gift_dimensions:
        total += calculate_paper(gift)

    return total


def calculate_ribbon(gift_dimensions: str) -> int:
    """Takes the dimensions of a gift and returns the total
    feet of ribbon required"""
    dimensions = gift_dimensions.strip().split("x")
    dimensions = [int(num) for num in dimensions]
    if len(dimensions) != 3:
        raise ValueError("The dimensions string must contain 3 measurements.")

    ribbon_needed = dimensions[0] * dimensions[1] * dimensions[2]
    dimensions.sort()
    ribbon_needed += (dimensions[0] * 2) + (dimensions[1] * 2)

    return ribbon_needed


def calculate_total_ribbon(all_gift_dimensions: list[str]) -> int:
    """Calculates the total ribbon required"""
    total = 0

    for gift in all_gift_dimensions:
        total += calculate_ribbon(gift)

    return total


if __name__ == "__main__":
    data = read_input("day_2_data.txt")
    total_paper = calculate_total_paper(data)
    total_ribbon = calculate_total_ribbon(data)

    print(f"The total paper needed is: {total_paper}")
    print(f"The total ribbon needed is {total_ribbon}")
