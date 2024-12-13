```python
import pytest
from datetime import datetime
from decimal import Decimal
from hypotez.src.utils.string.normalizer import (
    normalize_boolean,
    normalize_string,
    normalize_int,
    normalize_float,
    normalize_sql_date,
    simplify_string,
    remove_line_breaks,
    remove_html_tags,
    remove_special_characters,
    normalize_sku,
)


# Fixture definitions, if needed
@pytest.fixture
def example_list():
    """Provides a list of strings for testing."""
    return ["  Hello  ", "World!", "  Test  "]


@pytest.fixture
def example_html():
    """Provides an HTML string for testing."""
    return "  <p>Hello</p> <b>World</b>  "


# Tests for normalize_boolean
def test_normalize_boolean_valid_true_values():
    """Checks correct conversion of various true-like values."""
    assert normalize_boolean(True) is True
    assert normalize_boolean("true") is True
    assert normalize_boolean("1") is True
    assert normalize_boolean("yes") is True
    assert normalize_boolean("y") is True
    assert normalize_boolean("on") is True
    assert normalize_boolean(1) is True


def test_normalize_boolean_valid_false_values():
    """Checks correct conversion of various false-like values."""
    assert normalize_boolean(False) is False
    assert normalize_boolean("false") is False
    assert normalize_boolean("0") is False
    assert normalize_boolean("no") is False
    assert normalize_boolean("n") is False
    assert normalize_boolean("off") is False
    assert normalize_boolean(0) is False


def test_normalize_boolean_invalid_input():
    """Checks that invalid input returns the original input."""
    assert normalize_boolean("invalid") == "invalid"
    assert normalize_boolean(None) is None
    assert normalize_boolean(123) == 123
    assert normalize_boolean(3.14) == 3.14


# Tests for normalize_string
def test_normalize_string_valid_string():
    """Checks correct normalization of a valid string with HTML and special chars."""
    test_str = "  <p> Hello </p>  World! # "
    expected_str = "Hello World!"
    assert normalize_string(test_str) == expected_str


def test_normalize_string_valid_list(example_list):
    """Checks correct normalization of a list of strings."""
    expected_str = "Hello World! Test"
    assert normalize_string(example_list) == expected_str


def test_normalize_string_empty_input():
    """Checks that empty input returns an empty string."""
    assert normalize_string("") == ""
    assert normalize_string([]) == ""


def test_normalize_string_type_error():
    """Checks that non-string or list inputs raise TypeError."""
    with pytest.raises(TypeError):
        normalize_string(123)
    with pytest.raises(TypeError):
        normalize_string(None)
    with pytest.raises(TypeError):
        normalize_string(True)


def test_normalize_string_returns_original_value_on_error():
    """Checks that original value is returned in case of error."""
    input_value = 123
    assert normalize_string(input_value) == str(input_value).encode('utf-8').decode('utf-8')


# Tests for normalize_int
def test_normalize_int_valid_input():
    """Checks correct conversion of valid integer-like values."""
    assert normalize_int("42") == 42
    assert normalize_int(42) == 42
    assert normalize_int(42.5) == 42
    assert normalize_int(Decimal("42.7")) == 42


def test_normalize_int_invalid_input():
    """Checks that invalid input returns the original input."""
    assert normalize_int("abc") == "abc"
    assert normalize_int(None) is None
    assert normalize_int(True) == True
    assert normalize_int(float("inf")) == float("inf")


# Tests for normalize_float
def test_normalize_float_valid_input():
    """Checks correct conversion of valid float-like values."""
    assert normalize_float("3.14") == 3.14
    assert normalize_float(3.14) == 3.14
    assert normalize_float(3) == 3.0


def test_normalize_float_valid_list():
    """Checks correct conversion of a list of float-like values."""
    assert normalize_float(["1", 2, "3.5"]) == [1.0, 2.0, 3.5]


def test_normalize_float_empty_input():
    """Checks that empty input returns 0."""
    assert normalize_float("") == 0
    assert normalize_float([]) == []


def test_normalize_float_invalid_input():
    """Checks that invalid input returns the original input."""
    assert normalize_float("abc") == "abc"
    assert normalize_float(None) == None
    assert normalize_float(True) == True


def test_normalize_float_list_with_invalid():
    """Checks correct handling of list with invalid float values."""
    test_list = ["1", "invalid", 2.5, None]
    expected_list = [1.0, 2.5]
    assert normalize_float(test_list) == expected_list


# Tests for normalize_sql_date
def test_normalize_sql_date_valid_iso_format():
    """Checks correct normalization of ISO format date."""
    assert normalize_sql_date("2024-01-20") == "2024-01-20"


def test_normalize_sql_date_valid_non_iso_format():
    """Checks correct normalization of non-ISO format dates."""
    assert normalize_sql_date("01/20/2024") == "2024-01-20"
    assert normalize_sql_date("20/01/2024") == "2024-01-20"


def test_normalize_sql_date_with_datetime_object():
    """Checks correct handling of datetime object."""
    date_obj = datetime(2024, 1, 20)
    assert normalize_sql_date(date_obj) == "2024-01-20"


def test_normalize_sql_date_invalid_input():
    """Checks that invalid input returns the original input."""
    assert normalize_sql_date("invalid date") == "invalid date"
    assert normalize_sql_date(123) == 123
    assert normalize_sql_date(None) is None


# Tests for simplify_string
def test_simplify_string_valid_input():
    """Checks correct simplification of a string."""
    test_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
    expected_str = "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
    assert simplify_string(test_str) == expected_str


def test_simplify_string_empty_input():
    """Checks that empty input returns an empty string."""
    assert simplify_string("") == ""


def test_simplify_string_with_special_chars():
    """Checks correct handling of special characters."""
    test_str = "!@#$%^&*()_+=-`~[]\{}|;':\",./<>?"
    expected_str = ""
    assert simplify_string(test_str) == expected_str


def test_simplify_string_with_consecutive_spaces():
    """Checks that consecutive spaces are converted to single underscores."""
    test_str = "  multiple   spaces  "
    expected_str = "_multiple_spaces_"
    assert simplify_string(test_str) == expected_str


def test_simplify_string_returns_original_value_on_error():
    """Checks that original value is returned in case of error."""
    input_value = None
    assert simplify_string(input_value) == input_value


# Tests for remove_line_breaks
def test_remove_line_breaks_valid_input():
    """Checks correct removal of line breaks."""
    test_str = "Hello\nWorld\rTest\n"
    expected_str = "Hello World Test"
    assert remove_line_breaks(test_str) == expected_str


def test_remove_line_breaks_empty_input():
    """Checks that empty input returns an empty string."""
    assert remove_line_breaks("") == ""


def test_remove_line_breaks_no_line_breaks():
    """Checks that string without line breaks is unchanged."""
    test_str = "Hello World Test"
    assert remove_line_breaks(test_str) == test_str


# Tests for remove_html_tags
def test_remove_html_tags_valid_input(example_html):
    """Checks correct removal of HTML tags."""
    expected_str = "Hello World"
    assert remove_html_tags(example_html) == expected_str


def test_remove_html_tags_empty_input():
    """Checks that empty input returns an empty string."""
    assert remove_html_tags("") == ""


def test_remove_html_tags_no_tags():
    """Checks that string without tags is unchanged."""
    test_str = "Hello World"
    assert remove_html_tags(test_str) == test_str


# Tests for remove_special_characters
def test_remove_special_characters_default():
    """Checks correct removal of default special character '#'."
    """
    test_str = "Test#string#with#hashes"
    expected_str = "Teststringwithhashes"
    assert remove_special_characters(test_str) == expected_str


def test_remove_special_characters_custom_chars():
    """Checks correct removal of custom special characters."""
    test_str = "Test!string@with$custom%chars^"
    chars_to_remove = ["!", "@", "$", "%", "^"]
    expected_str = "Teststringwithcustomchars"
    assert remove_special_characters(test_str, chars_to_remove) == expected_str


def test_remove_special_characters_list_default():
    """Checks correct removal of default special characters from a list of strings."""
    test_list = ["Test#1", "Test#2", "Test#3"]
    expected_list = ["Test1", "Test2", "Test3"]
    assert remove_special_characters(test_list) == expected_list


def test_remove_special_characters_list_custom_chars():
    """Checks correct removal of custom special characters from a list of strings."""
    test_list = ["Test!1", "Test@2", "Test$3"]
    chars_to_remove = ["!", "@", "$"]
    expected_list = ["Test1", "Test2", "Test3"]
    assert remove_special_characters(test_list, chars_to_remove) == expected_list


def test_remove_special_characters_empty_input():
    """Checks that empty input returns an empty string or list."""
    assert remove_special_characters("") == ""
    assert remove_special_characters([]) == []


def test_remove_special_characters_no_chars():
    """Checks that strings without special chars are unchanged."""
    test_str = "Test string"
    assert remove_special_characters(test_str) == test_str


# Tests for normalize_sku
def test_normalize_sku_valid_input():
    """Checks correct normalization of SKU with Hebrew keywords."""
    assert normalize_sku("מקט: 303235") == "303235"
    assert normalize_sku("מק''ט: 12345") == "12345"
    assert normalize_sku("  303235  ") == "303235"
    assert normalize_sku("303235") == "303235"


def test_normalize_sku_no_hebrew_keywords():
    """Checks correct behavior with no Hebrew keywords."""
    test_str = "SKU12345"
    assert normalize_sku(test_str) == "SKU12345"


def test_normalize_sku_with_special_characters():
    """Checks correct removal of non-alphanumeric characters."""
    test_str = "SKU-123*45$"
    assert normalize_sku(test_str) == "SKU12345"


def test_normalize_sku_empty_input():
    """Checks that empty input returns an empty string."""
    assert normalize_sku("") == ""


def test_normalize_sku_returns_original_value_on_error():
    """Checks that original value is returned in case of error."""
    input_value = None
    assert normalize_sku(input_value) == input_value
```