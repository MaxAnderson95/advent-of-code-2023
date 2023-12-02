from solution import get_input, solution_part_one

input = get_input()

try:
    assert solution_part_one(input) == 2551
except AssertionError:
    print("Tests did NOT pass")
    raise
else:
    print("Tests passed successfully!")
