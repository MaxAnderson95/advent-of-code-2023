import sys
import pathlib
import re
import math


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


def extract_nums(input: str) -> list[int]:
    pattern = re.compile(r"((?P<number>[\s\d][\s\d])\s?)")
    return [int(m.groupdict()["number"]) for m in pattern.finditer(input)]


def solution_part_one(input: list[str]) -> int:
    total_points = 0
    for card in input:
        winning_nums_str = card.split("|")[0].split(":")[1].strip()
        my_nums_str = card.split("|")[1].strip()

        winning_nums = extract_nums(winning_nums_str)
        my_nums = extract_nums(my_nums_str)

        winners_found: int = 0
        for num in my_nums:
            if num in winning_nums:
                winners_found += 1

        if winners_found == 0:
            points = 0
        elif winners_found == 1:
            points = 1
        else:
            points = int(math.pow(2, winners_found - 1))

        total_points += points

    return total_points


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(input)}")
    # print(f"Solution for part 2: {solution_part_two(input)}")
