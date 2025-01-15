"""Day 4 of advent of code 2024."""


def read_input(filename: str) -> list[str]:
    """Reads the data from the file given."""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def find_word(word_search: list[str]) -> int:
    """Return the total count of the word in the grid of characters."""
    total_count = 0

    for row_num in range(len(word_search)):
        for char_num in range(len(word_search[row_num])):
            if word_search[row_num][char_num] == "X":
                results = get_words(word_search, row_num, char_num)
                total_count += len(results)

    return total_count


def get_words(word_search: list[str], row_index: int, char_index: int) -> list[str]:
    """Returns a list of strings that match the word XMAS."""
    results = []
    space_up = False
    space_down = False
    space_left = False
    space_right = False

    if row_index <= (len(word_search) - 4):
        space_down = True
        # check for down
        results.append("X" + word_search[row_index + 1][char_index] +
                       word_search[row_index + 2][char_index] +
                       word_search[row_index + 3][char_index])

    if char_index >= 3:
        space_left = True
        # check for backwards
        results.append("X" + word_search[row_index][char_index - 1] +
                       word_search[row_index][char_index - 2] +
                       word_search[row_index][char_index - 3])

    if char_index <= len(word_search[row_index]) - 4:
        space_right = True
        # check for forwards
        results.append("X" + word_search[row_index][char_index + 1] +
                       word_search[row_index][char_index + 2] +
                       word_search[row_index][char_index + 3])

    if row_index >= 3:
        # check for up
        space_up = True
        results.append("X" + word_search[row_index - 1][char_index] +
                       word_search[row_index - 2][char_index] +
                       word_search[row_index - 3][char_index])

    if space_right and space_up:
        # check for up right diagonal
        results.append("X" + word_search[row_index - 1][char_index + 1] +
                       word_search[row_index - 2][char_index + 2] +
                       word_search[row_index - 3][char_index + 3])

    if space_left and space_up:
        # check for up left diagonal
        results.append("X" + word_search[row_index - 1][char_index - 1] +
                       word_search[row_index - 2][char_index - 2] +
                       word_search[row_index - 3][char_index - 3])

    if space_right and space_down:
        # check for down right diagonal
        results.append("X" + word_search[row_index + 1][char_index + 1] +
                       word_search[row_index + 2][char_index + 2] +
                       word_search[row_index + 3][char_index + 3])

    if space_left and space_down:
        # check for down left diagonal
        results.append("X" + word_search[row_index + 1][char_index - 1] +
                       word_search[row_index + 2][char_index - 2] +
                       word_search[row_index + 3][char_index - 3])

    return [word for word in results if word == 'XMAS']


if __name__ == "__main__":
    word_search_data = read_input("data/day_4_data.txt")
    word_count = find_word(word_search_data)

    print(f"There are {word_count} occurrences of the word XMAS for part one.")
