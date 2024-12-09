```python
import pytest
import re
from datetime import datetime
from decimal import Decimal
from src.utils.string.normalizer import (
    normalize_boolean,
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_sql_date,
    simplify_string,
    remove_line_breaks,
    remove_html_tags,
    remove_special_characters,
)
from src.logger import logger


# Mock the logger for testing (important for pytest)
def fake_logger(message: str):
    print(message)
    return None

logger.debug = fake_logger
logger.error = fake_logger


# Test cases for normalize_boolean
def test_normalize_boolean_true():
    assert normalize_boolean("yes") is True
    assert normalize_boolean("true") is True
    assert normalize_boolean("1") is True


def test_normalize_boolean_false():
    assert normalize_boolean("no") is False
    assert normalize_boolean("false") is False
    assert normalize_boolean("0") is False


def test_normalize_boolean_invalid():
    assert normalize_boolean("abc") == "abc"  # Returns original value
    assert normalize_boolean(42) == 42


def test_normalize_boolean_boolean_input():
  assert normalize_boolean(True) is True
  assert normalize_boolean(False) is False


# Test cases for normalize_string
def test_normalize_string_valid_string():
    assert normalize_string(" Hello World! ") == "Hello World!"


def test_normalize_string_valid_list():
    assert normalize_string(["Hello", " World! "]) == "Hello World!"


def test_normalize_string_empty_string():
    assert normalize_string("") == ""


def test_normalize_string_empty_list():
    assert normalize_string([]) == ""


def test_normalize_string_invalid_input():
    with pytest.raises(TypeError):
        normalize_string(123)


def test_normalize_string_html_tags():
  input_str = "<b>Hello</b> <i>World</i>"
  expected_output = "Hello World"
  assert normalize_string(input_str) == expected_output


# Test cases for normalize_int
def test_normalize_int_valid_input():
    assert normalize_int("42") == 42
    assert normalize_int(42.0) == 42
    assert normalize_int(Decimal("42.0")) == 42


def test_normalize_int_invalid_input():
    assert normalize_int("abc") == "abc"  # Returns original value
    assert normalize_int(None) == None  # Check for None


# Test cases for normalize_float
def test_normalize_float_valid_input():
  assert normalize_float("3.14") == 3.14
  assert normalize_float(3) == 3.0
  assert normalize_float([1, '2.5', 3]) == [1.0, 2.5, 3.0]


def test_normalize_float_invalid_input():
  assert normalize_float("abc") == "abc"
  assert normalize_float(None) == None


# Test cases for normalize_sql_date
def test_normalize_sql_date_valid_input():
  assert normalize_sql_date("2024-12-06") == "2024-12-06"
  assert normalize_sql_date("12/06/2024") == "2024-12-06"


def test_normalize_sql_date_invalid_input():
  assert normalize_sql_date("invalid date") == "invalid date"  # returns original value

# Test cases for simplify_string
def test_simplify_string():
  input_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
  expected_output = "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
  assert simplify_string(input_str) == expected_output


# Test cases for remove_line_breaks
def test_remove_line_breaks():
  input_str = "This is\n a test\r string."
  expected_output = "This is a test string."
  assert remove_line_breaks(input_str) == expected_output


# Test cases for remove_html_tags
def test_remove_html_tags():
  input_str = "<b>Hello</b> World!"
  expected_output = "Hello World!"
  assert remove_html_tags(input_str) == expected_output


# Test cases for remove_special_characters
def test_remove_special_characters():
  input_str = "Hello#World!"
  expected_output = "HelloWorld!"
  assert remove_special_characters(input_str) == expected_output


def test_remove_special_characters_list():
  input_list = ["Hello#World!", "Test#String!"]
  expected_output = ["HelloWorld!", "TestString!"]
  assert remove_special_characters(input_list) == expected_output
```