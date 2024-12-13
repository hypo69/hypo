```python
import pytest
from datetime import datetime
from decimal import Decimal
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

# Fixture definitions, if needed (none needed for this case)

# Tests for normalize_boolean
def test_normalize_boolean_true_values():
    """Checks correct behavior with various true values."""
    assert normalize_boolean('yes') == True
    assert normalize_boolean('true') == True
    assert normalize_boolean('1') == True
    assert normalize_boolean(1) == True
    assert normalize_boolean(True) == True
    assert normalize_boolean('Yes') == True
    assert normalize_boolean('TRUE') == True
    assert normalize_boolean('On') == True
    assert normalize_boolean('on') == True


def test_normalize_boolean_false_values():
    """Checks correct behavior with various false values."""
    assert normalize_boolean('no') == False
    assert normalize_boolean('false') == False
    assert normalize_boolean('0') == False
    assert normalize_boolean(0) == False
    assert normalize_boolean(False) == False
    assert normalize_boolean('No') == False
    assert normalize_boolean('FALSE') == False
    assert normalize_boolean('Off') == False
    assert normalize_boolean('off') == False


def test_normalize_boolean_invalid_input():
    """Checks correct handling of invalid input."""
    assert normalize_boolean('invalid') == False
    assert normalize_boolean(None) == False
    assert normalize_boolean(3.14) == False
    assert normalize_boolean([1,2,3]) == False
    assert normalize_boolean({'a': 1}) == False


# Tests for normalize_string
def test_normalize_string_valid_string():
    """Checks correct behavior with a valid string."""
    assert normalize_string("  test string  ") == "test string"


def test_normalize_string_list_of_strings():
    """Checks correct behavior with a list of strings."""
    assert normalize_string(["  test  ", "string  "]) == "test string"


def test_normalize_string_with_html():
    """Checks correct behavior when removing HTML tags."""
    assert normalize_string("  <p>test</p> string  ") == "test string"

def test_normalize_string_with_special_characters():
    """Checks correct behavior when removing special characters."""
    assert normalize_string("  test!@#$%^  string   ") == "test string"


def test_normalize_string_empty_input():
     """Checks behavior with empty string or list"""
     assert normalize_string("") == ""
     assert normalize_string([]) == ""

def test_normalize_string_none_input():
     """Checks behavior with None as input"""
     assert normalize_string(None) == ""



# Tests for normalize_int
def test_normalize_int_valid_integer():
    """Checks correct behavior with a valid integer."""
    assert normalize_int("42") == 42
    assert normalize_int(42) == 42
    assert normalize_int(42.0) == 42
    assert normalize_int(Decimal(42)) == 42


def test_normalize_int_valid_float():
    """Checks correct behavior with a float input."""
    assert normalize_int(3.14) == 3


def test_normalize_int_string_float():
    """Checks correct behavior with a string float input."""
    assert normalize_int("3.14") == 3

def test_normalize_int_invalid_input():
    """Checks correct handling of invalid input."""
    with pytest.raises(ValueError):
        normalize_int("invalid")
    with pytest.raises(TypeError):
        normalize_int(None)
    with pytest.raises(ValueError):
        normalize_int("123a")



# Tests for normalize_float
def test_normalize_float_valid_float():
    """Checks correct behavior with a valid float."""
    assert normalize_float("3.14") == 3.14
    assert normalize_float(3.14) == 3.14
    assert normalize_float(3) == 3.0
    assert normalize_float(Decimal("3.14")) == 3.14


def test_normalize_float_list_of_numbers():
    """Checks correct behavior with a list of numbers."""
    assert normalize_float([1, "2.5", 3]) == [1.0, 2.5, 3.0]
    assert normalize_float([1, 2, 3]) == [1.0, 2.0, 3.0]
    assert normalize_float([1.1, 2.2, 3.3]) == [1.1, 2.2, 3.3]
    assert normalize_float([Decimal("1.1"), Decimal("2.2"), Decimal("3.3")]) == [1.1, 2.2, 3.3]


def test_normalize_float_invalid_input():
    """Checks correct handling of invalid input."""
    assert normalize_float("invalid") is None
    assert normalize_float(None) is None
    assert normalize_float([1, "invalid", 3]) == [1.0, None, 3.0]


# Tests for remove_line_breaks
def test_remove_line_breaks_with_breaks():
    """Checks correct behavior when removing line breaks."""
    assert remove_line_breaks("String\nwith\nline\rbreaks") == "Stringwithlinebreaks"


def test_remove_line_breaks_without_breaks():
    """Checks behavior when there are no line breaks."""
    assert remove_line_breaks("String without line breaks") == "String without line breaks"


def test_remove_line_breaks_empty_string():
    """Checks behavior with empty string"""
    assert remove_line_breaks("") == ""


# Tests for remove_html_tags
def test_remove_html_tags_with_tags():
    """Checks correct behavior when removing HTML tags."""
    assert remove_html_tags("<p>Example</p><b>text</b>") == "Exampletext"
    assert remove_html_tags("<p>Example</p>text") == "Exampletext"
    assert remove_html_tags("Example<p>text</p>") == "Exampletext"


def test_remove_html_tags_without_tags():
    """Checks behavior when there are no HTML tags."""
    assert remove_html_tags("Example text") == "Example text"


def test_remove_html_tags_empty_string():
    """Checks behavior with empty string"""
    assert remove_html_tags("") == ""


# Tests for remove_special_characters
def test_remove_special_characters_with_chars():
    """Checks correct behavior when removing special characters."""
    assert remove_special_characters("Hello!@#$%^World") == "HelloWorld"
    assert remove_special_characters("!@#$%^Hello World!@#$%^") == "HelloWorld"
    assert remove_special_characters("Hello@#$World%^") == "HelloWorld"


def test_remove_special_characters_without_chars():
    """Checks behavior when there are no special characters."""
    assert remove_special_characters("Hello World") == "Hello World"


def test_remove_special_characters_list_of_strings():
    """Checks behavior with a list of strings"""
    assert remove_special_characters(["Hello!@#$", "World%^"]) == ["Hello", "World"]


def test_remove_special_characters_empty_string():
    """Checks behavior with empty string"""
    assert remove_special_characters("") == ""


# Tests for normalize_sql_date
def test_normalize_sql_date_valid_date_string():
    """Checks correct behavior with a valid date string."""
    assert normalize_sql_date("2024-12-06") == "2024-12-06"
    assert normalize_sql_date("2024/12/06") == "2024-12-06"
    assert normalize_sql_date("06/12/2024") == "2024-12-06"
    assert normalize_sql_date("12/06/2024") == "2024-06-12"

def test_normalize_sql_date_datetime_object():
    """Checks correct behavior with a datetime object."""
    date_obj = datetime(2024, 12, 6)
    assert normalize_sql_date(date_obj) == "2024-12-06"


def test_normalize_sql_date_invalid_input():
    """Checks correct handling of invalid input."""
    with pytest.raises(ValueError):
        normalize_sql_date("invalid")
    with pytest.raises(TypeError):
        normalize_sql_date(None)
    with pytest.raises(ValueError):
         normalize_sql_date("2024-12-32")

```