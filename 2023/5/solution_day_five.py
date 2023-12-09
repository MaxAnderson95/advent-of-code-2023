import sys
import pathlib
import re


def get_input(file_name: str = "input.txt") -> list[str]:
    with open(pathlib.Path(sys.path[0], file_name)) as f:
        data = f.readlines()
    return [line.rstrip() for line in data]  # Strips the newline characters


class MappingTable():
    def __init__(self, inputs: list[str]) -> None:
        self.mapping: dict[int, int] = {}
        for input in inputs:
            dst = int(input.split()[0])
            src = int(input.split()[1])
            len = int(input.split()[2])

            src_nums = list(range(src, src + len))
            dst_nums = list(range(dst, dst + len))
            map = dict(zip(src_nums, dst_nums))
            self.mapping.update(map)

    def get(self, input: int) -> int:
        return self.mapping.get(input, input)


def parse_file(input: list[str]) -> tuple[list[int], dict[str, MappingTable]]:
    mapping_of_mappings: dict[str, MappingTable] = {}
    i = 0
    current_section: str = ''
    current_num_list: list[str] = []
    seeds: list[int] = []
    while i <= len(input) - 1:
        if i == 0:  # If we're on the first line
            seeds = [int(n) for n in input[0].split(": ")[1].split()]
            i += 1  # Skip line 2 of file
        elif re.match(r'[a-z]', input[i]):  # If we have a line with words (a section header)
            current_section = input[i].split()[0].replace("-", "_")
        elif re.match(r'\d', input[i]):  # If we have a line with numbers
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
    print("Parsing file...")
    seeds, mapping_tables = parse_file(input)

    seed_to_location: dict[int, int] = {}

    print("Processing seeds...")
    for seed in seeds:
        print(f"Seed {seed}")
        location = walk_seed(seed, mapping_tables)
        seed_to_location[seed] = location

    return min(seed_to_location.values())


if __name__ == "__main__":
    input = get_input()
    print(f"Solution for part 1: {solution_part_one(input)}")
