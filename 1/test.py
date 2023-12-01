from solution import main

try:
    assert main() == 56465
except AssertionError:
    print("Test did NOT pass")
else:
    print("Test passed successfully!")
