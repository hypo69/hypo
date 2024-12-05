```python
import pytest
import datetime

# Example Python code (replace with the actual code)
def calculate_age(birthdate):
    """
    Calculates the age of a person given their birthdate.

    Args:
        birthdate (datetime.date): The birthdate of the person.

    Returns:
        int: The age of the person in years.
        
    Raises:
        TypeError: If birthdate is not a datetime.date object.
        ValueError: If birthdate is in the future.
    """
    today = datetime.date.today()
    if not isinstance(birthdate, datetime.date):
        raise TypeError("Birthdate must be a datetime.date object")
    if birthdate > today:
        raise ValueError("Birthdate cannot be in the future")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Tests for calculate_age function
def test_calculate_age_valid_input():
    """Checks correct age calculation with valid input."""
    birthdate = datetime.date(1990, 10, 26)
    age = calculate_age(birthdate)
    assert age == 33  # Assuming today's date is October 26, 2023


def test_calculate_age_leap_year():
  """Checks age calculation for birthdates in leap years."""
  birthdate = datetime.date(1996, 2, 29)
  age = calculate_age(birthdate)
  assert age == 27


def test_calculate_age_invalid_input_type():
    """Checks exception handling for invalid input type."""
    with pytest.raises(TypeError):
        calculate_age("invalid_birthdate")


def test_calculate_age_invalid_input_future_date():
    """Checks exception handling for invalid input (future date)."""
    birthdate = datetime.date(2024, 10, 26)
    with pytest.raises(ValueError):
        calculate_age(birthdate)


def test_calculate_age_boundary_case_recent_birthdate():
    """Checks edge case for birthdate within the current year."""
    birthdate = datetime.date(2023, 10, 27)
    age = calculate_age(birthdate)
    assert age == 0


```
```
This solution includes comprehensive test cases for the `calculate_age` function, covering valid inputs, invalid input types, future dates, and boundary cases like recent birthdates.  It uses `pytest.raises` for exception handling and clear, descriptive test function names.  The example Python code is also included for clarity.  Remember to replace this example with the actual Python code you want to test.