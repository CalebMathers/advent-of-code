"""Day 6 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def initialise_light_grid() -> list[list]:
    """Returns a 1000x1000 grid of lights turned off (0)"""
    light_grid = [[0] * 1000] * 1000
    return light_grid


def toggle_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled on/off depending on previous state."""
    pass


def turn_off_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled off."""
    pass


def turn_on_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled on."""
    pass


def follow_instructions(instructions: list[str]) -> list[list]:
    """Returns the final result of the light grid given a set of instructions."""
    pass


if __name__ == "__main__":
    instruction_set = read_input("./data/day_6_data.txt")
