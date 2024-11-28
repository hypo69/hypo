```python
import pytest
from decimal import Decimal
from hypotez.src.utils.string.normalizer import StringNormalizer
from hypotez.src.logger import logger


# Mock logger for testing
def mock_logger(*args, **kwargs):
    pass

logger.debug = mock_logger
logger.error = mock_logger
logger.warning = mock_logger

# Fixture for creating test data
@pytest.fixture
def test_data():
    return {
        "boolean_true": "yes",
        "boolean_false": "no",
        "boolean_mixed": [True, "0"],
        "string_valid": "Hello World!",
        "string_multiple": ["Hello", "World", "!"],
        "string_invalid": "<>;!@#$%^&*()_+=-`~[]\\{}|;':\",./?",
        "string_with_html": "<p>Hello</p> World!",
        "string_with_linebreaks": "Hello\nWorld!",
        "int_valid": "42",
        "int_decimal": Decimal("42.0"),
        "int_invalid": "abc",
        "float_valid": "3.14",
        "float_list": [1, "2.5", 3],
        "float_invalid": "xyz",
        "empty_float": "",
        "empty_list": []
    }


# Tests for normalize_boolean
def test_normalize_boolean_true(test_data):
    assert StringNormalizer.normalize_boolean(test_data["boolean_true"]) is True

def test_normalize_boolean_false(test_data):
    assert StringNormalizer.normalize_boolean(test_data["boolean_false"]) is False

def test_normalize_boolean_mixed(test_data):
    assert StringNormalizer.normalize_boolean(test_data["boolean_mixed"]) == [True, False]

def test_normalize_boolean_already_boolean(test_data):
    assert StringNormalizer.normalize_boolean(True) is True


# Tests for normalize_string
def test_normalize_string_valid(test_data):
    assert StringNormalizer.normalize_string(test_data["string_valid"]) == "Hello World!"
def test_normalize_string_multiple(test_data):
    assert StringNormalizer.normalize_string(test_data["string_multiple"]) == "Hello World !"

def test_normalize_string_invalid(test_data):
    assert StringNormalizer.normalize_string(test_data["string_invalid"]) == ""


def test_normalize_string_html(test_data):
    assert StringNormalizer.normalize_string(test_data["string_with_html"]) == "Hello World!"

def test_normalize_string_linebreaks(test_data):
    assert StringNormalizer.normalize_string(test_data["string_with_linebreaks"]) == "Hello World!"

# Tests for normalize_int
def test_normalize_int_valid(test_data):
    assert StringNormalizer.normalize_int(test_data["int_valid"]) == 42

def test_normalize_int_decimal(test_data):
    assert StringNormalizer.normalize_int(test_data["int_decimal"]) == 42

def test_normalize_int_invalid(test_data):
    assert StringNormalizer.normalize_int(test_data["int_invalid"]) is None  # Correctly handles None

# Tests for normalize_float
def test_normalize_float_valid(test_data):
    assert StringNormalizer.normalize_float(test_data["float_valid"]) == 3.14

def test_normalize_float_list(test_data):
    assert StringNormalizer.normalize_float(test_data["float_list"]) == [1.0, 2.5, 3.0]

def test_normalize_float_invalid(test_data):
    assert StringNormalizer.normalize_float(test_data["float_invalid"]) is None

def test_normalize_float_empty(test_data):
    assert StringNormalizer.normalize_float(test_data["empty_float"]) == 0

def test_normalize_float_empty_list(test_data):
    assert StringNormalizer.normalize_float(test_data["empty_list"]) == []
```