"""Day 1 of the advent of code 2016."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [movement.strip() for movement in f.read().split(",")]


def move_once(direction: str, distance: int, current_loc: tuple) -> tuple:
    """Makes a movement based on the given inputs and returns the new location."""
    current_x, current_y = current_loc

    if direction == "N":
        current_y += distance
    elif direction == "E":
        current_x += distance
    elif direction == "S":
        current_y -= distance
    else:
        current_x -= distance

    return current_x, current_y


def change_direction(current_direction: str, turn_direction: str) -> str:
    """Changes the direction the elf is facing."""
    if current_direction == "N":
        return "E" if turn_direction == "R" else "W"

    if current_direction == "E":
        return "S" if turn_direction == "R" else "N"

    if current_direction == "S":
        return "W" if turn_direction == "R" else "E"

    if current_direction == "W":
        return "N" if turn_direction == "R" else "S"

    return current_direction


def move_all(movements: list[str]) -> tuple:
    """Initializes location then moves as per the given list of movements
    and returns the final x and y coords as a tuple."""
    current_direction = "N"
    current_x = 0
    current_y = 0

    for movement in movements:
        turn_direction = movement[0]
        current_direction = change_direction(current_direction, turn_direction)

        moving_distance = int(movement[1:])

        current_x, current_y = move_once(
            current_direction, moving_distance, (current_x, current_y))

    return current_x, current_y


def find_repeat_location(movements: list[str]) -> tuple:
    """Returns the x and y coordinates of the first location that is visited twice
    while following the movements given."""
    current_direction = "N"
    current_x = 0
    current_y = 0
    visited_locations = []
    visited_locations.append((current_x, current_y))

    for movement in movements:
        turn_direction = movement[0]
        current_direction = change_direction(current_direction, turn_direction)

        moving_distance = int(movement[1:])

        for _ in range(1, moving_distance+1):
            current_x, current_y = move_once(
                current_direction, 1, (current_x, current_y))

            if (current_x, current_y) in visited_locations:
                return (current_x, current_y)
            visited_locations.append((current_x, current_y))

    return current_x, current_y


if __name__ == "__main__":
    movements_data = read_input("data/day_1_data.txt")

    final_x, final_y = move_all(movements_data)
    blocks_away = abs(final_x) + abs(final_y)
    print(f"Part 1: Easter Bunny HQ is {blocks_away} blocks away.")

    repeat_x, repeat_y = find_repeat_location(movements_data)
    repeated_blocks_away = abs(repeat_x) + abs(repeat_y)
    print(f"""Part 2: The first revisited location is {
          repeated_blocks_away} blocks away.""")
