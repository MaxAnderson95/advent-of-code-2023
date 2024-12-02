from solution_day_one_2024 import get_input, solution_part_one, solution_part_two

input = get_input()


def test_solution_part_one() -> None:
    assert solution_part_one(input) == 2000468


def test_solution_part_two() -> None:
    assert solution_part_two(input) == 18567089


if __name__ == "__main__":
    test_solution_part_one()
    test_solution_part_two()
