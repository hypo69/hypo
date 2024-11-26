```python
import pytest
from decimal import Decimal
from hypotez.src.utils.string.normalizer import StringNormalizer
from hypotez.src.logger import logger  # Import the logger for testing

# Mock the logger for testing
logger.error = lambda msg: print(f"Error: {msg}")
logger.warning = lambda msg: print(f"Warning: {msg}")
logger.debug = lambda msg: print(f"Debug: {msg}")

# Fixtures (if needed, but not in this case)
# @pytest.fixture
# def example_data():
#     return ...


# Tests for StringNormalizer.normalize_boolean
def test_normalize_boolean_true():
    assert StringNormalizer.normalize_boolean(True) is True
    assert StringNormalizer.normalize_boolean("true") is True
    assert StringNormalizer.normalize_boolean("1") is True
    assert StringNormalizer.normalize_boolean("yes") is True
    assert StringNormalizer.normalize_boolean("y") is True
    assert StringNormalizer.normalize_boolean("on") is True

def test_normalize_boolean_false():
    assert StringNormalizer.normalize_boolean(False) is False
    assert StringNormalizer.normalize_boolean("false") is False
    assert StringNormalizer.normalize_boolean("0") is False
    assert StringNormalizer.normalize_boolean("no") is False
    assert StringNormalizer.normalize_boolean("n") is False
    assert StringNormalizer.normalize_boolean("off") is False

def test_normalize_boolean_invalid():
    assert StringNormalizer.normalize_boolean("abc") is False
    assert StringNormalizer.normalize_boolean(10) is False
    assert StringNormalizer.normalize_boolean(None) is False # Added for None


# Tests for StringNormalizer.normalize_string
def test_normalize_string_valid():
    assert StringNormalizer.normalize_string("Hello World!") == "Hello World!"
    assert StringNormalizer.normalize_string(["Hello", "World!"]) == "Hello World!"
    assert StringNormalizer.normalize_string(["Hello", "  World!  "]) == "Hello World!"
    assert StringNormalizer.normalize_string("  Hello <p>World!</p> ") == "Hello World!"
    assert StringNormalizer.normalize_string(["<p>Hello</p>", "World!"]) == "Hello World!"



def test_normalize_string_empty():
    assert StringNormalizer.normalize_string("") == ""
    assert StringNormalizer.normalize_string([]) == ""


def test_normalize_string_with_html():
    assert StringNormalizer.normalize_string("<p>Hello</p> <b>World!</b>") == "Hello World!"

def test_normalize_string_list_of_strings():
    assert StringNormalizer.normalize_string(["  Hello", "World!  "]) == "Hello World!"


# Tests for StringNormalizer.normalize_int
def test_normalize_int_valid():
    assert StringNormalizer.normalize_int("42") == 42
    assert StringNormalizer.normalize_int(42) == 42
    assert StringNormalizer.normalize_int(42.5) == 42


def test_normalize_int_invalid():
    assert StringNormalizer.normalize_int("abc") is None
    assert StringNormalizer.normalize_int(None) is None


def test_normalize_int_decimal():
    decimal_value = Decimal("10.5")
    assert StringNormalizer.normalize_int(decimal_value) == 10

# Tests for StringNormalizer.normalize_float

def test_normalize_float_valid():
    assert StringNormalizer.normalize_float("3.14") == 3.14
    assert StringNormalizer.normalize_float(3.14) == 3.14
    assert StringNormalizer.normalize_float("10") == 10.0


def test_normalize_float_list():
    assert StringNormalizer.normalize_float([1, '2.5', 3]) == [1.0, 2.5, 3.0]
    assert StringNormalizer.normalize_float(['1', '2.5', '3']) == [1.0, 2.5, 3.0]

def test_normalize_float_invalid():
    assert StringNormalizer.normalize_float("abc") is None
    assert StringNormalizer.normalize_float(None) is None

def test_normalize_float_empty():
    assert StringNormalizer.normalize_float("") == 0


def test_normalize_float_list_invalid():
  assert StringNormalizer.normalize_float(["abc", "1"]) == [1.0]


# Add more tests as needed.  Remember to test edge cases and error handling.
```