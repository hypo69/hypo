```python
import pytest
import datetime


# Assuming the code to be tested is as follows (replace with the actual code)
class DateCalculator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def calculate_days(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        else:
            return 0

    def is_valid_date(self, date_str):
      try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
      except ValueError:
        return False


# Fixture definitions
@pytest.fixture
def valid_dates():
    return {
        "start_date": datetime.date(2024, 1, 1),
        "end_date": datetime.date(2024, 1, 10)
    }


@pytest.fixture
def invalid_start_date():
    return {"start_date": "invalid_date", "end_date": datetime.date(2024, 1, 10)}

@pytest.fixture
def invalid_end_date():
    return {"start_date": datetime.date(2024, 1, 1), "end_date": "invalid_date"}



# Tests for DateCalculator class
def test_calculate_days_valid_input(valid_dates):
    """Tests calculate_days with valid dates."""
    calculator = DateCalculator(valid_dates["start_date"], valid_dates["end_date"])
    assert calculator.calculate_days() == 9

def test_calculate_days_no_dates(valid_dates):
    """Tests calculate_days with no dates."""
    calculator = DateCalculator(None, None)
    assert calculator.calculate_days() == 0


def test_calculate_days_invalid_start_date(invalid_start_date):
  """Tests calculate_days with invalid start date."""
  calculator = DateCalculator(invalid_start_date["start_date"], invalid_start_date["end_date"])
  assert calculator.calculate_days() == 0

def test_calculate_days_invalid_end_date(invalid_end_date):
  """Tests calculate_days with invalid end date."""
  calculator = DateCalculator(invalid_end_date["start_date"], invalid_end_date["end_date"])
  assert calculator.calculate_days() == 0



def test_is_valid_date_valid_input():
    """Tests is_valid_date with a valid date string."""
    assert DateCalculator.is_valid_date("2024-01-15") is True

def test_is_valid_date_invalid_input():
    """Tests is_valid_date with an invalid date string."""
    assert DateCalculator.is_valid_date("invalid_date") is False

def test_is_valid_date_empty_string():
    """Tests is_valid_date with an empty string."""
    assert DateCalculator.is_valid_date("") is False

```