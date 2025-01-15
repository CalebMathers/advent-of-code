"""Day 4 of advent of code 2024."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    word_search = read_input("data/day_4_data.txt")
