"""Day 3 for for advent of code 2015"""

import hashlib


def find_smallest_hash_number_five(secret_key: str) -> int:
    """Returns the smallest positive integer that could make
    a hash that begins with 5 zeroes in hexadecimal when
    combined with the secret key."""
    i = 0
    while True:
        string_to_hash = f"{secret_key}{i}"

        m = hashlib.md5()
        m.update(string_to_hash.encode('utf-8'))
        digested_hex = m.hexdigest()

        if str(digested_hex)[:5] == "00000":
            return i

        i += 1


def find_smallest_hash_number_six(secret_key: str) -> int:
    """Returns the smallest positive integer that could make
    a hash that begins with 6 zeroes in hexadecimal when
    combined with the secret key."""
    i = 0
    while True:
        string_to_hash = f"{secret_key}{i}"

        m = hashlib.md5()
        m.update(string_to_hash.encode('utf-8'))
        digested_hex = m.hexdigest()

        if str(digested_hex)[:6] == "000000":
            return i

        i += 1


if __name__ == "__main__":
    print(find_smallest_hash_number_five("yzbqklnj"))

    print(find_smallest_hash_number_six("yzbqklnj"))
