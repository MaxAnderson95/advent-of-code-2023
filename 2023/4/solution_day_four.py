from copy import deepcopy
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


def get_winner_count_per_game(input: list[str]) -> list[int]:
    winners: list[int] = []
    for card in input:
        winning_nums_str = card.split("|")[0].split(":")[1].strip()
        my_nums_str = card.split("|")[1].strip()

        winning_nums = extract_nums(winning_nums_str)
        my_nums = extract_nums(my_nums_str)

        winners_found: int = 0
        for num in my_nums:
            if num in winning_nums:
                winners_found += 1

        winners.append(winners_found)

    return winners


def solution_part_one(input: list[str]) -> int:
    games = get_winner_count_per_game(input)

    total_points = 0
    for game in games:
        if game == 0:
            points = 0
        elif game == 1:
            points = 1
        else:
            points = int(math.pow(2, game - 1))

        total_points += points

    return total_points


def solution_part_two(input: list[str]) -> int:
    # Create a list representing how many copies of a card you have for each game. We start off with 1 each. Index 0 is game 1, index 1 is game 2, etc.
    cards = [1 for _ in input]
    games = get_winner_count_per_game(input)  # Use part 1 to get the number of winners per game in a list
    for gi, n in enumerate(games):  # Loop through each game, grabbing game index (gi), and number of winners (n)
        for i in range(n):  # Itterate over number of winners
            cards[gi + i + 1] += cards[gi]  # Increment the next n games by the amount of winners in game gi
    return sum(cards)


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(input)}")
    print(f"Solution for part 2: {solution_part_two(input)}")
