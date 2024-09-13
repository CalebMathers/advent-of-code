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

    return delivered


def dual_move_and_deliver(movements: str) -> int:
    """Returns the number of unique houses that have been delivered
    to after santa and robo-santa have finished their movements."""
    santa_movements = movements[::2]
    robo_movements = movements[1::2]

    santa_delivery_coords = list(move_and_deliver(santa_movements).keys())
    robo_delivery_coords = list(move_and_deliver(robo_movements).keys())

    all_delivered_coords = set(santa_delivery_coords + robo_delivery_coords)
    return len(all_delivered_coords)


if __name__ == "__main__":
    data = read_input("./data/day_3_data.txt")
    part_one_deliveries = move_and_deliver(data)
    print(len(part_one_deliveries.keys()))

    print(dual_move_and_deliver(data))
