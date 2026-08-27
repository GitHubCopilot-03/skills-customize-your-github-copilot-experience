# 📘 Assignment: Unit Testing with unittest

## 🎯 Objective

Learn how to write automated unit tests in Python using the built-in `unittest` module. By the end of this assignment, you will design test cases, validate edge cases, and use failing tests to improve code quality.

## 📝 Tasks

### 🛠️ Write Your First Test Cases

#### Description
Use `starter-code.py` and create a new file named `test_starter.py`. Write tests for the provided utility functions to verify expected behavior for normal inputs.

#### Requirements
Completed program should:

- Import functions from `starter-code.py` into `test_starter.py`.
- Create a `unittest.TestCase` class with at least 3 test methods.
- Test `calculate_average()` with valid numeric lists.
- Test `normalize_username()` with mixed-case text and extra spaces.
- Run tests with `python -m unittest -v`.

### 🛠️ Add Edge Case and Error Tests

#### Description
Expand your test suite to include edge cases and invalid inputs so your tests can catch hidden bugs.

#### Requirements
Completed program should:

- Add tests for empty input in `calculate_average()`.
- Add tests that verify `ValueError` is raised for invalid discounts in `apply_discount()`.
- Add at least 2 additional edge-case tests of your choice.
- Keep test names clear and descriptive.

### 🛠️ Use Tests to Find and Fix a Bug

#### Description
One function in `starter-code.py` has behavior that does not fully match the expected password rules. Write tests first, then fix the implementation.

#### Requirements
Completed program should:

- Write tests for `is_strong_password()` that cover uppercase letters, digits, and minimum length.
- Demonstrate at least one failing test before the fix.
- Update `is_strong_password()` so all tests pass.
- Confirm final output shows all tests passing.
