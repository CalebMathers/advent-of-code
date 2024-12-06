"""Day 1 of advent of code 2024."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def separate_lists(locations_list: list[str]) -> tuple[list[int]]:
    """Separates the lists of location into two separate lists of ints,
    sorted ascending."""
    left_list = []
    right_list = []

    for locations in locations_list:
        left_list.append(int(locations.split()[0]))
        right_list.append(int(locations.split()[1]))

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    return left_list, right_list


def calculate_total_difference(left_locations: list[int], right_locations: list[int]) -> int:
    """Returns the total difference for every number pair in the two lists given."""
    total_difference = 0

    for left_num, right_num in zip(left_locations, right_locations):
        total_difference += abs(left_num - right_num)

    return total_difference


if __name__ == "__main__":
    location_data = read_input("data/day_1_data.txt")
    left_data, right_data = separate_lists(location_data)
    total_distance = calculate_total_difference(left_data, right_data)

    print(f"The total distance for part one is: {total_distance}")
