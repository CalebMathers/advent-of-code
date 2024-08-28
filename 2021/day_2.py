"""Day 2 of the advent of code 2021"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def plot_course(data: list[str]) -> dict:
    """Runs the course given from the data and returns the final
    horizontal position and depth"""
    positions = {"hor": 0, "depth": 0}

    for move in data:
        if "forward" in move:
            positions["hor"] += int(move.strip()[-1])
        elif "up" in move:
            positions["depth"] -= int(move.strip()[-1])
        else:
            positions["depth"] += int(move.strip()[-1])

    return positions


if __name__ == "__main__":
    course = read_input("day_2_data.txt")
    final_positions = plot_course(course)
    print("The product of the final positions is " +
          f"{final_positions["hor"] * final_positions["depth"]}")
