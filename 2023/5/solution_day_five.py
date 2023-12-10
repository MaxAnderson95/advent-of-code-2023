import sys
import pathlib
import re


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


class MappingTable():
    def __init__(self, inputs: list[str]) -> None:
        self.mapping: dict[int, tuple[int, int, int]] = {}
        for input in inputs:
            dst = int(input.split()[0])
            src = int(input.split()[1])
            length = int(input.split()[2])
            self.mapping[src] = (dst, src, length)

    def get(self, input: int) -> int:
        keys = sorted(self.mapping.keys())

        # Check if it falls between all of the source ranges
        for i in range(len(keys) - 1):
            dst, _, length = self.mapping[keys[i]]
            if keys[i] <= input < keys[i] + length:
                difference = input - keys[i]
                return dst + difference

        # Final try, check if falls within the last source's range
        dst, _, length = self.mapping[keys[-1]]
        if keys[-1] <= input < keys[-1] + length:
            difference = input - keys[-1]
            return dst + difference

        return input  # Out of range, return back same number


def parse_file(input: list[str]) -> tuple[list[int], dict[str, MappingTable]]:
    mapping_of_mappings: dict[str, MappingTable] = {}
    i = 0
    current_section: str = ''
    current_num_list: list[str] = []
    seeds: list[int] = []
    while i <= len(input) - 1:
        if i == 0:  # If we're on the first line
            seeds = [int(n) for n in input[0].split(": ")[1].split()]
            i += 2  # Skip line 2 of file
            continue

        if re.match(r'[a-z]', input[i]):  # If we have a line with words (a section header)
            current_section = input[i].split()[0].replace("-", "_")

        if re.match(r'\d', input[i]):  # If we have a line with numbers
            current_num_list.append(input[i])

        # If we have a blank line or end of file (we've hit the end of a section)
        if input[i] == '' or i == len(input) - 1:
            mapping_of_mappings[current_section] = MappingTable(current_num_list)
            current_section = ''
            current_num_list = []
        i += 1

    return seeds, mapping_of_mappings


def walk_seed(seed: int, mapping_tables: dict[str, MappingTable]) -> int:
    soil = mapping_tables["seed_to_soil"].get(seed)
    fertilizer = mapping_tables["soil_to_fertilizer"].get(soil)
    water = mapping_tables["fertilizer_to_water"].get(fertilizer)
    light = mapping_tables["water_to_light"].get(water)
    temp = mapping_tables["light_to_temperature"].get(light)
    humidity = mapping_tables["temperature_to_humidity"].get(temp)
    location = mapping_tables["humidity_to_location"].get(humidity)

    return location


def solution_part_one(input: list[str]) -> int:
    seeds, mapping_tables = parse_file(input)
    seed_to_location: dict[int, int] = {}
    for seed in seeds:
        location = walk_seed(seed, mapping_tables)
        seed_to_location[seed] = location

    return min(seed_to_location.values())


if __name__ == "__main__":
    input = get_input()
    print(f"Solution for part 1: {solution_part_one(input)}")
