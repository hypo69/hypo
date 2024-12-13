```python
import pytest
from src.utils.string.normalizer import (
    normalize_boolean,
    normalize_string,
    normalize_int,
    normalize_float,
    remove_line_breaks,
    remove_html_tags,
    remove_special_characters,
    normalize_sql_date,
)
from datetime import datetime
from decimal import Decimal

# Fixture definitions, if needed
@pytest.fixture
def example_html():
    """Provides a sample HTML string for testing."""
    return "<p>This is <b>bold</b> text with <span>span</span>.</p>"


@pytest.fixture
def example_string_with_breaks():
    """Provides a sample string with line breaks."""
    return "String\nwith\nline\nbreaks\r"


@pytest.fixture
def example_string_with_special_chars():
    """Provides a sample string with special characters."""
    return "Hello@W#o$r%l^d!"


@pytest.fixture
def example_list_of_strings():
    """Provides a sample list of strings."""
    return ["  string 1  ", "string2", "   string3  "]


# Tests for normalize_boolean
def test_normalize_boolean_true_values():
    """Checks correct behavior with various true-like inputs."""
    assert normalize_boolean("yes") is True
    assert normalize_boolean("true") is True
    assert normalize_boolean("1") is True
    assert normalize_boolean(1) is True
    assert normalize_boolean(True) is True
    assert normalize_boolean("y") is True
    assert normalize_boolean("on") is True


def test_normalize_boolean_false_values():
    """Checks correct behavior with various false-like inputs."""
    assert normalize_boolean("no") is False
    assert normalize_boolean("false") is False
    assert normalize_boolean("0") is False
    assert normalize_boolean(0) is False
    assert normalize_boolean(False) is False
    assert normalize_boolean("n") is False
    assert normalize_boolean("off") is False


def test_normalize_boolean_invalid_input():
    """Checks handling of invalid input."""
    assert normalize_boolean("invalid") is False
    assert normalize_boolean(None) is False


# Tests for normalize_string
def test_normalize_string_valid_string_input():
    """Checks correct behavior with a valid string input."""
    assert normalize_string("  test  string  ") == "test string"


def test_normalize_string_valid_list_input(example_list_of_strings):
    """Checks correct behavior with a valid list of strings."""
    assert normalize_string(example_list_of_strings) == "string 1 string2 string3"


def test_normalize_string_html_tags_removal(example_html):
    """Checks correct removal of HTML tags."""
    assert normalize_string(example_html) == "This is bold text with span."


def test_normalize_string_empty_input():
    """Checks correct behavior with empty string or list."""
    assert normalize_string("") == ""
    assert normalize_string([]) == ""
    
def test_normalize_string_none_input():
    """Checks correct behavior when input is none"""
    assert normalize_string(None) == ""

# Tests for normalize_int
def test_normalize_int_valid_integer_string():
    """Checks correct behavior with a valid integer string."""
    assert normalize_int("42") == 42


def test_normalize_int_valid_float():
    """Checks correct behavior with a valid float."""
    assert normalize_int(3.14) == 3


def test_normalize_int_valid_int():
    """Checks correct behavior with a valid integer."""
    assert normalize_int(123) == 123


def test_normalize_int_valid_decimal():
    """Checks correct behavior with a valid decimal."""
    assert normalize_int(Decimal('42.5')) == 42

def test_normalize_int_invalid_input():
    """Checks handling of invalid input."""
    with pytest.raises(ValueError):
        normalize_int("invalid")
    
def test_normalize_int_none_input():
    """Checks correct behavior when input is none"""
    with pytest.raises(TypeError):
        normalize_int(None)


# Tests for normalize_float
def test_normalize_float_valid_float_string():
    """Checks correct behavior with a valid float string."""
    assert normalize_float("3.14") == 3.14


def test_normalize_float_valid_list_of_numbers():
    """Checks correct behavior with a valid list of numbers."""
    assert normalize_float([1, "2.5", 3]) == [1.0, 2.5, 3.0]


def test_normalize_float_valid_float():
    """Checks correct behavior with a valid float."""
    assert normalize_float(3.14) == 3.14
    
def test_normalize_float_valid_integer():
    """Checks correct behavior with a valid integer."""
    assert normalize_float(5) == 5.0


def test_normalize_float_invalid_input():
    """Checks handling of invalid input."""
    assert normalize_float("invalid") is None
    assert normalize_float([1, "invalid", 3]) == [1.0, None, 3.0]


def test_normalize_float_empty_list():
    """Checks behavior with empty list"""
    assert normalize_float([]) == []
    
def test_normalize_float_none_input():
    """Checks correct behavior when input is none"""
    assert normalize_float(None) is None


# Tests for remove_line_breaks
def test_remove_line_breaks_valid_string(example_string_with_breaks):
    """Checks correct removal of line breaks."""
    assert remove_line_breaks(example_string_with_breaks) == "Stringwithlinebreaks"


def test_remove_line_breaks_no_breaks():
    """Checks correct behavior when no line breaks exist."""
    assert remove_line_breaks("String without breaks") == "String without breaks"


def test_remove_line_breaks_empty_string():
    """Checks correct behavior with an empty string."""
    assert remove_line_breaks("") == ""

def test_remove_line_breaks_none_input():
    """Checks correct behavior when input is none"""
    assert remove_line_breaks(None) is None

# Tests for remove_html_tags
def test_remove_html_tags_valid_html(example_html):
    """Checks correct removal of HTML tags."""
    assert remove_html_tags(example_html) == "This is bold text with span."


def test_remove_html_tags_no_html():
    """Checks correct behavior when no HTML tags exist."""
    assert remove_html_tags("String without HTML") == "String without HTML"


def test_remove_html_tags_empty_string():
    """Checks correct behavior with an empty string."""
    assert remove_html_tags("") == ""
    
def test_remove_html_tags_none_input():
    """Checks correct behavior when input is none"""
    assert remove_html_tags(None) == ""


# Tests for remove_special_characters
def test_remove_special_characters_valid_string(example_string_with_special_chars):
    """Checks correct removal of special characters."""
    assert remove_special_characters(example_string_with_special_chars) == "HelloWorld"


def test_remove_special_characters_valid_list(example_list_of_strings):
    """Checks correct removal of special characters from list"""
    
    assert remove_special_characters(["te@st!", "an#other!", "l$ist"]) == ["test", "another", "list"]
    
def test_remove_special_characters_no_special_chars():
    """Checks correct behavior when no special characters exist."""
    assert remove_special_characters("String without special chars") == "String without special chars"


def test_remove_special_characters_empty_string():
    """Checks correct behavior with an empty string."""
    assert remove_special_characters("") == ""


def test_remove_special_characters_empty_list():
    """Checks correct behavior with an empty list."""
    assert remove_special_characters([]) == []
    
def test_remove_special_characters_none_input():
    """Checks correct behavior when input is none"""
    assert remove_special_characters(None) == ""
    
def test_remove_special_characters_list_none_input():
    """Checks correct behavior when input list contains none"""
    assert remove_special_characters([None, "test"]) == ["", "test"]


# Tests for normalize_sql_date
def test_normalize_sql_date_valid_string():
    """Checks correct behavior with a valid date string."""
    assert normalize_sql_date("2024-12-06") == "2024-12-06"


def test_normalize_sql_date_valid_datetime():
    """Checks correct behavior with a valid datetime object."""
    date_obj = datetime(2024, 12, 6)
    assert normalize_sql_date(date_obj) == "2024-12-06"
    
def test_normalize_sql_date_valid_datetime_with_time():
    """Checks correct behavior with a valid datetime object containing time."""
    date_obj = datetime(2024, 12, 6, 10, 30, 0)
    assert normalize_sql_date(date_obj) == "2024-12-06"
    


def test_normalize_sql_date_invalid_format():
    """Checks handling of invalid date format string."""
    assert normalize_sql_date("06-12-2024") is None


def test_normalize_sql_date_empty_string():
    """Checks correct behavior with an empty string."""
    assert normalize_sql_date("") is None
    
def test_normalize_sql_date_none_input():
    """Checks correct behavior when input is none"""
    assert normalize_sql_date(None) is None
```