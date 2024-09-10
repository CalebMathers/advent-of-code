"""Day 3 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def move_and_deliver(movements: str) -> dict:
    """Returns the number of house locations with at least one present"""
    x_loc = 0
    y_loc = 0

    # Deliver to the first house
    delivered = {}
    delivered[f"{x_loc}:{y_loc}"] = 1

    # Go through every movement and change x or y location
    for movement in movements:
        if movement == "^":
            y_loc += 1
        elif movement == "v":
            y_loc -= 1
        elif movement == ">":
            x_loc += 1
        else:
            x_loc -= 1

        # Deliver to the house at the location
        if delivered.get(f"{x_loc}:{y_loc}"):
            delivered[f"{x_loc}:{y_loc}"] += 1
        else:
            delivered[f"{x_loc}:{y_loc}"] = 1

    return len(delivered.keys())


if __name__ == "__main__":
    data = read_input("./data/day_3_data.txt")
    print(move_and_deliver(data))
