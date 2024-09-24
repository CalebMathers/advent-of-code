"""Day 3 for advent of code 2023"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [f.strip() for f in f.readlines()]


def count_bits(bit_strings: list[str]) -> tuple[int, int]:
    """Returns the decimal of a bit string for the gamma rate
    and epsilon rate."""
    gamma = ""
    epsilon = ""

    for i in range(len(bit_strings[0])):
        one_count = 0
        zero_count = 0
        for bit_string in bit_strings:
            if bit_string[i] == "1":
                one_count += 1
            else:
                zero_count += 1

        if one_count > zero_count:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return (int(gamma, base=2), int(epsilon, base=2))


def calculate_power_consumption(gamma: int, epsilon: int) -> int:
    """Returns the power consumption which is the product
    of the gamma and epsilon rates."""
    return gamma * epsilon


if __name__ == "__main__":
    data = read_input("day_3_data.txt")
    gamma_rate, epsilon_rate = count_bits(data)
    print(calculate_power_consumption(gamma_rate, epsilon_rate))
