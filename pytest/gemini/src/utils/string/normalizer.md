```python
import pytest
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from hypotez.src.utils.string.normalizer import (
    normalize_boolean,
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_sql_date,
    simplify_string,
    remove_line_breaks,
    remove_html_tags,
    remove_special_characters
)


def test_normalize_boolean_valid_true():
    """Test normalize_boolean with valid true inputs."""
    assert normalize_boolean("true") is True
    assert normalize_boolean("1") is True
    assert normalize_boolean("yes") is True
    assert normalize_boolean("y") is True
    assert normalize_boolean("on") is True
    assert normalize_boolean(True) is True
    assert normalize_boolean(1) is True


def test_normalize_boolean_valid_false():
    """Test normalize_boolean with valid false inputs."""
    assert normalize_boolean("false") is False
    assert normalize_boolean("0") is False
    assert normalize_boolean("no") is False
    assert normalize_boolean("n") is False
    assert normalize_boolean("off") is False
    assert normalize_boolean(False) is False
    assert normalize_boolean(0) is False


def test_normalize_boolean_invalid_input():
    """Test normalize_boolean with invalid inputs."""
    assert normalize_boolean("invalid") == "invalid"
    assert normalize_boolean(123) == 123
    assert normalize_boolean([1, 2, 3]) == [1, 2, 3]  # Test list input


def test_normalize_string_valid_input():
    """Test normalize_string with valid string input."""
    input_str = " Пример строки <b>с HTML</b> "
    expected_output = "Пример строки с HTML"
    assert normalize_string(input_str) == expected_output


def test_normalize_string_list_input():
    """Test normalize_string with list input."""
    input_list = ["Hello", "  World!  "]
    expected_output = "Hello World!"
    assert normalize_string(input_list) == expected_output


def test_normalize_string_invalid_input():
    """Test normalize_string with invalid input (not a string or list)."""
    with pytest.raises(TypeError):
        normalize_string(123)


def test_normalize_int_valid_input():
    """Test normalize_int with valid input."""
    assert normalize_int("42") == 42
    assert normalize_int(42.5) == 42
    assert normalize_int(Decimal("42.5")) == 42


def test_normalize_int_invalid_input():
    """Test normalize_int with invalid input."""
    assert normalize_int("abc") == "abc"
    assert normalize_int("42.5") == 42  # Check handling of floats in string
    assert normalize_int("not a number") == "not a number"


def test_normalize_float_valid_input():
    assert normalize_float("3.14") == 3.14
    assert normalize_float(3.14) == 3.14
    assert normalize_float([1, "2.5", 3]) == [1.0, 2.5, 3.0]


def test_normalize_float_invalid_input():
    assert normalize_float("xyz") == "xyz"
    assert normalize_float([1, "abc", 3]) == [1.0, "abc", 3.0]


def test_normalize_sql_date_valid_input():
  assert normalize_sql_date("2024-12-06") == "2024-12-06"
  assert normalize_sql_date("12/06/2024") == "2024-12-06"


def test_normalize_sql_date_invalid_input():
  assert normalize_sql_date("invalid date") == "invalid date"


def test_simplify_string_valid_input():
    input_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
    expected_output = "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
    assert simplify_string(input_str) == expected_output

def test_remove_line_breaks():
    input_str = "This is\na test\nstring."
    expected_output = "This is a test string."
    assert remove_line_breaks(input_str) == expected_output

def test_remove_html_tags():
    input_str = "<p>This is a paragraph.</p>"
    expected_output = "This is a paragraph."
    assert remove_html_tags(input_str) == expected_output

def test_remove_special_characters():
    input_str = "This#is#a#string."
    expected_output = "Thisisastring."
    assert remove_special_characters(input_str) == expected_output

    input_list = ["This#is#a#list", "of#strings."]
    expected_output = ["Thisisalist", "ofstrings."]
    assert remove_special_characters(input_list) == expected_output

```