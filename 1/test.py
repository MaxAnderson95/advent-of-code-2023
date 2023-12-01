from solution import get_input, solution_part_one

input = get_input()

try:
    assert solution_part_one(input) == 56465
except AssertionError:
    print("Tests did NOT pass")
else:
    print("Tests passed successfully!")
