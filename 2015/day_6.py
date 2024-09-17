"""Day 6 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def initialise_light_grid() -> list[list]:
    """Returns a 1000x1000 grid of lights turned off (0)"""
    light_grid = [[0] * 1000 for i in range(1001)]
    return light_grid


def toggle_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled on/off depending on previous state."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            if light_grid[row][light] == 0:
                light_grid[row][light] = 1
            else:
                light_grid[row][light] = 0

    return light_grid


def turn_off_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled off."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            light_grid[row][light] = 0

    return light_grid


def turn_on_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end toggled on."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            light_grid[row][light] = 1

    return light_grid


def follow_instructions(instructions: list[str]) -> list[list]:
    """Returns the final result of the light grid given a set of instructions."""
    lights = initialise_light_grid()

    for instruction in instructions:
        if "toggle" in instruction:
            instruction = instruction.replace(
                "toggle ", "").replace("through ", "").split()
            lights = toggle_lights(lights, instruction[0], instruction[1])
        elif "off" in instruction:
            instruction = instruction.replace(
                "turn off ", "").replace("through ", "").split()
            lights = turn_off_lights(lights, instruction[0], instruction[1])
        elif "on" in instruction:
            instruction = instruction.replace(
                "turn on ", "").replace("through ", "").split()
            lights = turn_on_lights(lights, instruction[0], instruction[1])

    return lights


def follow_brightness_instructions(instructions: list[str]) -> list[list]:
    """Returns the final result of the light grid given a set of instructions."""
    lights = initialise_light_grid()

    for instruction in instructions:
        if "toggle" in instruction:
            instruction = instruction.replace(
                "toggle ", "").replace("through ", "").split()
            lights = toggle_lights_brightness(
                lights, instruction[0], instruction[1])
        elif "off" in instruction:
            instruction = instruction.replace(
                "turn off ", "").replace("through ", "").split()
            lights = turn_down_lights(lights, instruction[0], instruction[1])
        elif "on" in instruction:
            instruction = instruction.replace(
                "turn on ", "").replace("through ", "").split()
            lights = turn_up_lights(lights, instruction[0], instruction[1])

    return lights


def turn_up_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end increased in 1 brightness."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            light_grid[row][light] += 1

    return light_grid


def turn_down_lights(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end turned down by 1 brightness."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            if light_grid[row][light] > 0:
                light_grid[row][light] -= 1

    return light_grid


def toggle_lights_brightness(light_grid: list[list], start: str, end: str) -> list[list]:
    """Returns the light grid with the lights in the range of the start and
    end increased by 2 brightness."""
    start_grids = [int(grid_ref) for grid_ref in start.split(",")]
    end_grids = [int(grid_ref) for grid_ref in end.split(",")]

    for row in range(start_grids[0], end_grids[0] + 1):
        for light in range(start_grids[1], end_grids[1] + 1):
            light_grid[row][light] += 2

    return light_grid


def count_lights_on(light_grid: list[list]) -> int:
    """Returns the number of lights on in a grid."""
    on_count = 0

    for row in light_grid:
        for light in row:
            if light == 1:
                on_count += 1

    return on_count


def count_lights_brightness(light_grid: list[list]) -> int:
    """Returns the total brightness of all lights in a grid."""
    total_brightness = 0

    for row in light_grid:
        for light in row:
            total_brightness += light

    return total_brightness


if __name__ == "__main__":
    instruction_set = read_input("./data/day_6_data.txt")
    end_grid = follow_instructions(instruction_set)
    print(count_lights_on(end_grid))

    end_brightness_grid = follow_brightness_instructions(instruction_set)
    print(count_lights_brightness(end_brightness_grid))
