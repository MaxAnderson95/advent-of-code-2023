from solution_day_three import get_input, solution_part_one

input = get_input()


def test_solution_part_one() -> None:
    print(input)
    assert solution_part_one(input) == 539713


if __name__ == "__main__":
    test_solution_part_one()
