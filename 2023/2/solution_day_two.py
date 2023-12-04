import sys
import pathlib
import re


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


MAX_COUNTS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def solution_part_one(input: list[str]) -> int:
    possible_games: list[int] = []
    for game in input:
        search = re.search("^Game (\\d+): (.*)$", game)
        game_number = search.group(1)
        gameplay = search.group(2)
        rounds = gameplay.split("; ")
        try:
            for round in rounds:
                color_pairs = re.findall("(\\d+) (blue|red|green)", round)
                for color_pair in color_pairs:
                    color_name = color_pair[1]
                    color_quantity = int(color_pair[0])
                    if color_quantity > MAX_COUNTS[color_name]:
                        raise StopIteration
        except StopIteration:
            continue

        possible_games.append(int(game_number))

    return sum(possible_games)


def solution_part_two(input: list[str]) -> int:
    powers: list[int] = []
    for game in input:
        search = re.search("^Game (\\d+): (.*)$", game)
        gameplay = search.group(2)
        rounds = gameplay.split("; ")

        min_required: dict[str, int] = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for round in rounds:
            color_pairs = re.findall("(\\d+) (blue|red|green)", round)
            for color_pair in color_pairs:
                color_name = color_pair[1]
                color_quantity = int(color_pair[0])
                if color_quantity > min_required[color_name]:
                    min_required[color_name] = color_quantity

        power = min_required["blue"] * \
            min_required["green"] * \
            min_required["red"]

        powers.append(power)

    return sum(powers)


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(input)}")
    print(f"Solution for part 2: {solution_part_two(input)}")
