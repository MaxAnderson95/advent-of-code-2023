from solution import get_input, solution_part_one, solution_part_two

input = get_input()

try:
    assert solution_part_one(input) == 56465
    assert solution_part_two(input) == 55902
except AssertionError:
    print("Tests did NOT pass")
    raise
else:
    print("Tests passed successfully!")
