from solution_day_two import get_input, solution_part_one, solution_part_two

input = get_input()


def test_solution_part_one() -> None:
    print(input)
    assert solution_part_one(input) == 2551


def test_solution_part_two() -> None:
    print(input)
    assert solution_part_two(input) == 62811


if __name__ == "__main__":
    test_solution_part_one()
    test_solution_part_two()
