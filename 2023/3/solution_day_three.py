import sys
import pathlib
import itertools


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


# A list of tuples with each being coordinates to every spot in a 9x9 grid from the perspective of the center
# For a given digit in the center of the grid, we search around it. If a symbol is found within one of these positions,
# that entire multi-digit number is considered "adjacent" to the symbol and counts as a valid part number.
# OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
OFFSETS = list(itertools.product([-1, 0, 1], [-1, 0, 1]))


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def solution_part_one(input: list[str]) -> int:
    valid_numbers: list[int] = []
    for i, line in enumerate(input):  # Loop through each line
        is_valid = False  # So far we've not found a valid number
        num = ''  # Create a number builder string
        for j, char in enumerate(line):  # Loop through each chracter on the line
            if char.isdigit():  # If it's a digit
                num += char  # Start building the number string
                # Now we check the coordinates in the 8 spots around it for a symbol
                for i_offset, j_offset in OFFSETS:
                    try:
                        position_to_check = input[i + i_offset][j + j_offset]
                        if is_symbol(position_to_check):  # If it's a symbol
                            # We've hit a symbol in the 9x9 grid around the char
                            # We mark the entire number as being valid.
                            is_valid = True
                    except IndexError:
                        continue  # Ignore when we're on the edge or corner of the grid when we check out of bounds

            # If we spot a non-digit or hit the end of the row, we've found all the digits in that whole number
            if not char.isdigit() or j == len(line) - 1:
                # If that whole number we found is valid (adjacent to a symbol)
                if is_valid:
                    # Add it to the final list
                    valid_numbers.append(int(num))
                    is_valid = False  # Reset back to false
                num = ''  # Reset number builder string back to empty

    return sum(valid_numbers)


def solution_part_two(input: list[str]) -> int:
    gears: dict[tuple[int, int], list[int]] = {}
    for i, line in enumerate(input):  # Loop through each line
        is_valid = False  # So far we've not found a valid number
        num = ''  # Create a number builder string
        for j, char in enumerate(line):  # Loop through each chracter on the line
            if char.isdigit():  # If it's a digit
                num += char  # Start building the number string
                # Now we check the coordinates in the 8 spots around it for a gear
                for i_offset, j_offset in OFFSETS:
                    try:
                        position_to_check = input[i + i_offset][j + j_offset]
                        if position_to_check == '*':  # If it's a gear
                            # We've hit a gear in the 9x9 grid around the char
                            # We mark the entire number as being valid.
                            is_valid = True
                            gear_location = (i + i_offset, j + j_offset)
                    except IndexError:
                        continue  # Ignore when we're on the edge or corner of the grid when we check out of bounds

            # If we spot a non-digit or hit the end of the row, we've found all the digits in that whole number
            if not char.isdigit() or j == len(line) - 1:
                # If that whole number we found is valid (adjacent to a gear)
                if is_valid:
                    # Add it to the final list
                    if gear_location not in gears:
                        gears[gear_location] = []
                    gears[gear_location].append(int(num))
                    is_valid = False  # Reset back to false
                num = ''  # Reset number builder string back to empty

    # Filter for the gears that have exactly two adjacent part numbers
    # Multiply the two part numbers for that gear to produce the gear ratio
    # Sum all of the gear ratios
    return sum([parts[0] * parts[1]
                for parts in gears.values()
                if len(parts) == 2])


if __name__ == "__main__":
    input = get_input()
    print(f"Solution for part 1: {solution_part_one(input)}")
    print(f"Solution for part 2: {solution_part_two(input)}")
