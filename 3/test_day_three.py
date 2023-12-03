from solution_day_three import get_input, solution_part_one, solution_part_two

input = get_input()


def test_solution_part_one() -> None:
    print(input)
    assert solution_part_one(input) == 539713


def test_solution_part_two() -> None:
    assert solution_part_two(input) == 84159075


if __name__ == "__main__":
    test_solution_part_one()
