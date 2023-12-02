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


if __name__ == "__main__":
    input = get_input("input.txt")
    print(f"Solution for part 1: {solution_part_one(input)}")
