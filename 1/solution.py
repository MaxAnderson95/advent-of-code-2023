import sys
import pathlib
import string


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


def solution_part_one(input: list[str]) -> int:
    DIGITS: set[str] = set(string.digits)
    numbers: list[int] = []

    for line in input:
        first = None
        last = None

        for char in line:
            if char in DIGITS:
                if first is None:
                    first = char
                else:
                    last = char

        if not first:  # Handles a line that doesn't have any digits
            continue

        if not last:  # Handles a line with only one digit
            last = first

        numbers.append(int(first + last))

    return sum(numbers)


if __name__ == "__main__":
    data = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(data)}")
