```python
import pytest
from decimal import Decimal
from hypotez.src.utils.string.normalizer import StringNormalizer
from hypotez.src.logger import logger
import logging


# Mock logger for testing
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Only log errors during testing


@pytest.fixture
def string_formatter_mock():
    """Mocks the StringFormatter class."""
    class MockFormatter:
        @staticmethod
        def remove_htmls(text):
            return text
        @staticmethod
        def remove_line_breaks(text):
            return text
        @staticmethod
        def remove_special_characters(text):
            return text

    return MockFormatter()

def test_normalize_boolean_valid_input():
    """Test normalize_boolean with valid boolean inputs."""
    assert StringNormalizer.normalize_boolean(True) is True
    assert StringNormalizer.normalize_boolean(False) is False
    assert StringNormalizer.normalize_boolean("true") is True
    assert StringNormalizer.normalize_boolean("1") is True
    assert StringNormalizer.normalize_boolean("yes") is True
    assert StringNormalizer.normalize_boolean("y") is True
    assert StringNormalizer.normalize_boolean("on") is True
    assert StringNormalizer.normalize_boolean("false") is False
    assert StringNormalizer.normalize_boolean("0") is False
    assert StringNormalizer.normalize_boolean("no") is False
    assert StringNormalizer.normalize_boolean("n") is False
    assert StringNormalizer.normalize_boolean("off") is False

def test_normalize_boolean_invalid_input():
    """Test normalize_boolean with invalid input."""
    assert StringNormalizer.normalize_boolean("invalid") is False
    assert StringNormalizer.normalize_boolean(123) is False
    assert StringNormalizer.normalize_boolean([1,2]) is False


def test_normalize_string_valid_input(string_formatter_mock):
    """Test normalize_string with valid input."""
    assert StringNormalizer.normalize_string("Hello World!") == "Hello World!"
    assert StringNormalizer.normalize_string(["Hello", "World!"]) == "Hello World!"
    assert StringNormalizer.normalize_string(["Hello", "  World!  "]) == "Hello World!"

def test_normalize_string_empty_input(string_formatter_mock):
    """Test normalize_string with empty input."""
    assert StringNormalizer.normalize_string("") == ""
    assert StringNormalizer.normalize_string([""]) == ""

def test_normalize_string_with_html_and_breaks(string_formatter_mock):
    input_data = "<h1>Hello</h1><br>World!<br><br>"
    expected_output = "Hello World"
    assert StringNormalizer.normalize_string(input_data) == expected_output


def test_normalize_string_list_input(string_formatter_mock):
    input_data = ["Hello", "World!", "   ", "Test"]
    expected_output = "Hello World! Test"
    assert StringNormalizer.normalize_string(input_data) == expected_output



def test_normalize_int_valid_input():
    assert StringNormalizer.normalize_int("42") == 42
    assert StringNormalizer.normalize_int(42) == 42
    assert StringNormalizer.normalize_int(42.5) == 42
    assert StringNormalizer.normalize_int(Decimal("42.5")) == 42



def test_normalize_int_invalid_input():
    with pytest.raises(ValueError):  # Expect a ValueError if conversion fails
        StringNormalizer.normalize_int("abc")
    assert StringNormalizer.normalize_int("abc") is None  # Or None if you prefer
    assert StringNormalizer.normalize_int(None) is None #handle none

def test_normalize_float_valid_input():
    assert StringNormalizer.normalize_float("3.14") == 3.14
    assert StringNormalizer.normalize_float(3.14) == 3.14
    assert StringNormalizer.normalize_float(Decimal("3.14")) == 3.14
    assert StringNormalizer.normalize_float([1, '2.5', 3]) == [1.0, 2.5, 3.0]
    assert StringNormalizer.normalize_float((1, '2.5', 3)) == [1.0, 2.5, 3.0]


def test_normalize_float_empty_input():
  assert StringNormalizer.normalize_float(None) == 0
  assert StringNormalizer.normalize_float([]) is None


def test_normalize_float_invalid_input():
    assert StringNormalizer.normalize_float("abc") is None
    assert StringNormalizer.normalize_float([1, 'abc', 3]) == [1.0, None, 3.0]
```