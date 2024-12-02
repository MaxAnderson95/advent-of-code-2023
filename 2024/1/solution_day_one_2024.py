import sys
import pathlib


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


def solution_part_one(input: list[str]) -> int:
    column_one: list[int] = []
    column_two: list[int] = []
    distance: int = 0

    for line in input:
        column_one.append(int(line.split("   ")[0]))
        column_two.append(int(line.split("   ")[1]))

    column_one = sorted(column_one)
    column_two = sorted(column_two)
    zipped_tuples = list(zip(column_one, column_two))

    for tup in zipped_tuples:
        distance += abs(tup[0] - tup[1])

    return distance


def solution_part_two(input: list[str]) -> int:
    column_one: list[int] = []
    column_two: list[int] = []
    similarity_score: int = 0

    for line in input:
        column_one.append(int(line.split("   ")[0]))
        column_two.append(int(line.split("   ")[1]))

    # Construct a count of reoccuring nums in column 2
    counts: dict[int, int] = {}
    for num in column_two:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in column_one:
        try:
            count = counts[num]
        except KeyError:  # Account for numbers which only appear in column one
            count = 0
        similarity_score += (num * count)

    return similarity_score


if __name__ == "__main__":
    input = get_input("input.txt")
    print(solution_part_one(input))
    print(solution_part_two(input))
