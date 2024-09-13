"""Day 5 for for advent of code 2015"""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(read_input("./data/day_5_data.txt"))
