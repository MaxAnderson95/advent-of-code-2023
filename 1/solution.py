import sys
import pathlib
import string

DIGITS: set[str] = set(string.digits)


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


def solution_part_one(input: list[str]) -> int:
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


def solution_part_two(input: list[str]) -> int:
    numbers: list[int] = []

    digit_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for line in input:
        first = None
        last = None

        word = ''
        count = 0
        while count < len(line):  # AKA: for char in line -- Using a while loop so I can backtrack in cases where two spelled out characters share a joining letter (ex. oneight needs to be extracted as 1 and then 8)
            char = line[count]
            # Check if current char is a digit itself
            if char in DIGITS:
                if first is None:
                    first = char
                else:
                    last = char

                word = ''
                count += 1
                continue

            # Check for a spelled out digit
            word += char
            try:
                for digit in digit_mapping.keys():
                    if digit in word:
                        if first is None:
                            first = str(digit_mapping[digit])
                        else:
                            last = str(digit_mapping[digit])
                        word = ''
                        count - 1  # Backtrack in the list of characters
                        # Python doesn't support labeled loops, so we can't use continue here, so we raise an exception and catch it in the outer loop, then continue from there.
                        raise StopIteration  # AKA continue
            except StopIteration:  # Catch the inner "continue" and then continue in the outer loop
                continue

            count += 1

        if not first:  # Handles a line that doesn't have any digits
            continue

        if not last:  # Handles a line with only one digit
            last = first

        numbers.append(int(first + last))

    return sum(numbers)


if __name__ == "__main__":
    data = get_input("input.txt")
    data2 = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(data)}")
    print(f"Solution for part 2: {solution_part_two(data2)}")
