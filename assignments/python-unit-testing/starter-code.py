"""Starter code for the Unit Testing with unittest assignment.

Your goal is to write tests in a separate file named test_starter.py.
Run tests with:
    python -m unittest -v
"""


def calculate_average(numbers):
    """Return the arithmetic mean for a non-empty list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


def normalize_username(username):
    """Normalize usernames by trimming spaces and converting to lowercase."""
    return username.strip().lower()


def apply_discount(price, percent):
    """Apply a percentage discount and return the final price."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def is_strong_password(password):
    """Return True if password seems strong.

    Expected rule set for this assignment:
    - At least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one digit

    NOTE: This function currently contains incomplete logic on purpose.
    """
    return len(password) >= 8
