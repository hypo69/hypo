```python
import pytest
import datetime

from hypotez.src.utils.string import (
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_boolean,
    normalize_sql_date,
)


# Fixtures (if needed, but none are apparent from the provided code)

# Tests for normalize_string
def test_normalize_string_valid_input():
    """Checks correct behavior with valid input (string)."""
    input_string = "  This is a test string.  "
    expected_output = "This is a test string."
    assert normalize_string(input_string) == expected_output

def test_normalize_string_empty_string():
  """Checks handling of empty string."""
  input_string = ""
  expected_output = ""
  assert normalize_string(input_string) == expected_output

def test_normalize_string_none_input():
  """Checks handling of None input."""
  input_string = None
  with pytest.raises(TypeError):
      normalize_string(input_string)


# Tests for normalize_int
def test_normalize_int_valid_input():
    """Checks correct behavior with valid integer input."""
    input_int = "123"
    expected_output = 123
    assert normalize_int(input_int) == expected_output

def test_normalize_int_invalid_input():
    """Checks handling of invalid integer input (non-integer)."""
    input_int = "abc"
    with pytest.raises(ValueError):
        normalize_int(input_int)

def test_normalize_int_empty_string():
  """Checks handling of empty string."""
  input_int = ""
  with pytest.raises(ValueError):
      normalize_int(input_int)

def test_normalize_int_none_input():
  """Checks handling of None input."""
  input_int = None
  with pytest.raises(TypeError):
      normalize_int(input_int)

# Tests for normalize_float
def test_normalize_float_valid_input():
    """Checks correct behavior with valid float input."""
    input_float = "3.14"
    expected_output = 3.14
    assert normalize_float(input_float) == expected_output

def test_normalize_float_invalid_input():
    """Checks handling of invalid float input (non-float)."""
    input_float = "abc"
    with pytest.raises(ValueError):
        normalize_float(input_float)

def test_normalize_float_empty_string():
  """Checks handling of empty string."""
  input_float = ""
  with pytest.raises(ValueError):
      normalize_float(input_float)

def test_normalize_float_none_input():
  """Checks handling of None input."""
  input_float = None
  with pytest.raises(TypeError):
      normalize_float(input_float)


# Tests for normalize_boolean
def test_normalize_boolean_true():
  """Checks handling of 'true'."""
  input_bool = "true"
  expected_output = True
  assert normalize_boolean(input_bool) == expected_output

def test_normalize_boolean_false():
  """Checks handling of 'false'."""
  input_bool = "false"
  expected_output = False
  assert normalize_boolean(input_bool) == expected_output

def test_normalize_boolean_invalid_input():
    """Checks handling of invalid boolean input."""
    input_bool = "TRUE"  # Case sensitivity check
    with pytest.raises(ValueError):
        normalize_boolean(input_bool)
def test_normalize_boolean_none_input():
  """Checks handling of None input."""
  input_bool = None
  with pytest.raises(TypeError):
      normalize_boolean(input_bool)



# Tests for normalize_sql_date
def test_normalize_sql_date_valid_input():
    """Checks correct behavior with valid date string input."""
    date_string = "2024-10-27"
    expected_date = datetime.date(2024, 10, 27)
    assert normalize_sql_date(date_string) == expected_date

def test_normalize_sql_date_invalid_input():
    """Checks handling of invalid date string input."""
    date_string = "2024-13-27"  # Invalid month
    with pytest.raises(ValueError):
        normalize_sql_date(date_string)

def test_normalize_sql_date_none_input():
    """Checks handling of None input."""
    date_string = None
    with pytest.raises(TypeError):
        normalize_sql_date(date_string)


```