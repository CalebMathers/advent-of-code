"""Day 5 for for advent of code 2015"""

VOWELS = ["a", "e", "i", "o", "u"]
FORBIDDEN_STRINGS = ["ab", "cd", "pq", "xy"]


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def check_nice_string(string_to_check: str) -> bool:
    """Returns true if the string is 'nice', else returns false."""
    vowel_count = 0
    double_count = 0

    for i, char in enumerate(string_to_check):
        if char in VOWELS:
            vowel_count += 1

        if i != len(string_to_check) - 1:
            if char == string_to_check[i + 1]:
                double_count += 1

            if (char + string_to_check[i + 1]) in FORBIDDEN_STRINGS:
                return False

    if vowel_count >= 3 and double_count >= 1:
        return True

    return False


def find_nice_strings(all_strings: list[str]) -> list[str]:
    """Returns every string that is deemed nice as per
    Santa's odd standards."""
    nice_strings = []
    for string in all_strings:
        if check_nice_string(string):
            nice_strings.append(string)

    return nice_strings


def find_new_nice_strings(all_strings: list[str]) -> list[str]:
    """Returns every string that is deemed nice as per
    Santa's odd but new standards."""
    nice_strings = []
    for string in all_strings:
        if check_new_nice_string(string):
            nice_strings.append(string)

    return nice_strings


def check_new_nice_string(string_to_check: str) -> bool:
    """Returns true if the string is 'nice' according to
    new standards, else returns false."""
    repeat_gap_count = 0
    pairs = []

    for i, char in enumerate(string_to_check):
        if i != len(string_to_check) - 1:
            pairs.append(char + string_to_check[i+1])

            if i != len(string_to_check) - 2:
                if char == string_to_check[i+2]:
                    repeat_gap_count += 1

    repeating_pair_count = 0

    for pair in pairs:
        if string_to_check.count(pair) > 1:
            repeating_pair_count += 1

    if repeat_gap_count >= 1 and repeating_pair_count >= 1:
        return True

    return False


if __name__ == "__main__":
    list_of_strings = read_input("./data/day_5_data.txt")

    nice = find_nice_strings(list_of_strings)
    print(len(nice))

    new_nice = find_new_nice_strings(list_of_strings)
    print(len(new_nice))
