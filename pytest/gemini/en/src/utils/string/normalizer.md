```python
import pytest
from decimal import Decimal
from hypotez.src.utils.string.normalizer import normalize_boolean, normalize_string, normalize_int, normalize_float
from src.logger import logger

# Mock logger for testing
logger.debug = lambda x: None
logger.error = lambda x, y: None
logger.warning = lambda x, y: print(f"Warning: {x} {y}")


def test_normalize_boolean_valid_true():
    """Test normalize_boolean with valid True inputs."""
    assert normalize_boolean(True) is True
    assert normalize_boolean('true') is True
    assert normalize_boolean('1') is True
    assert normalize_boolean('yes') is True
    assert normalize_boolean('y') is True
    assert normalize_boolean('on') is True


def test_normalize_boolean_valid_false():
    """Test normalize_boolean with valid False inputs."""
    assert normalize_boolean(False) is False
    assert normalize_boolean('false') is False
    assert normalize_boolean('0') is False
    assert normalize_boolean('no') is False
    assert normalize_boolean('n') is False
    assert normalize_boolean('off') is False


def test_normalize_boolean_invalid_input():
    """Test normalize_boolean with invalid input (not boolean)."""
    assert normalize_boolean('abc') is 'abc'
    assert normalize_boolean(123) is 123
    assert normalize_boolean([1, 2, 3]) is [1, 2, 3]


def test_normalize_string_valid_input():
    """Test normalize_string with valid string input."""
    input_str = "  Hello, world!  "
    expected_output = "Hello, world!".encode('utf-8').decode('utf-8')
    assert normalize_string(input_str) == expected_output


def test_normalize_string_with_list():
    """Test normalize_string with a list of strings."""
    input_list = ["Hello", " World!"]
    expected_output = "Hello World!".encode('utf-8').decode('utf-8')
    assert normalize_string(input_list) == expected_output


def test_normalize_string_with_html_and_linebreaks():
    """Test normalize_string handling HTML tags and linebreaks."""
    input_str = "<h1>Hello</h1><br>World!<br>  "
    expected_output = "Hello World!".encode('utf-8').decode('utf-8')
    assert normalize_string(input_str) == expected_output


def test_normalize_string_error_handling():
    """Test normalize_string error handling with invalid input."""
    input_str = None
    expected_output = None
    assert normalize_string(input_str) == str(input_str).encode('utf-8').decode('utf-8')


def test_normalize_int_valid_input():
    """Test normalize_int with valid integer input."""
    assert normalize_int(42) == 42
    assert normalize_int("42") == 42
    assert normalize_int(Decimal("42.0")) == 42


def test_normalize_int_with_float():
    """Test normalize_int with float input."""
    assert normalize_int(42.5) == 42


def test_normalize_int_invalid_input():
    """Test normalize_int with invalid input."""
    assert normalize_int("abc") == "abc"
    assert normalize_int(None) is None


def test_normalize_float_valid_input():
    assert normalize_float(3.14) == 3.14
    assert normalize_float("3.14") == 3.14
    assert normalize_float(Decimal("3.14")) == 3.14
    

def test_normalize_float_list_input():
    input_list = [1, "2.5", 3]
    assert normalize_float(input_list) == [1.0, 2.5, 3.0]


def test_normalize_float_empty_list():
    assert normalize_float([]) == []


def test_normalize_float_invalid_input():
    assert normalize_float("abc") is "abc"
    assert normalize_float(None) is None

def test_normalize_float_empty_input():
  assert normalize_float(None) is 0
```