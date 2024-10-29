"""Day 1 of the advent of code 2016."""

def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [movement.strip() for movement in f.read().split(",")]
    
def move_once(direction: str, distance: int, current_loc: tuple) -> tuple:
    """"""
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
    """"""
    if current_direction == "N":
        if turn_direction == "R":
            return "E"
        else:
            return "W"
        
    if current_direction == "E":
        if turn_direction == "R":
            return "S"
        else:
            return "N"
        
    if current_direction == "S":
        if turn_direction == "R":
            return "W"
        else:
            return "E"
        
    if current_direction == "W":
        if turn_direction == "R":
            return "N"
        else:
            return "S"


def move_all(movements: list[str]) -> tuple:
    """"""
    current_direction = "N"
    current_x = 0
    current_y = 0

    for movement in movements:
        turn_direction = movement[0]
        current_direction = change_direction(current_direction, turn_direction)

        moving_distance = int(movement[1:])

        current_x, current_y = move_once(current_direction, moving_distance, (current_x, current_y))

    return current_x, current_y





if __name__ == "__main__":
    movements = read_input("data/day_1_data.txt")
    final_x, final_y = move_all(movements)
    
    print(abs(final_x) + abs(final_y))