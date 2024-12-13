```python
import pytest
from hypotez.src.utils.convertors.unicode import decode_unicode_escape

# Fixture definitions, if needed
@pytest.fixture
def example_dict():
    """Provides a dictionary with unicode escape sequences for testing."""
    return {
        'product_name': r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2',
        'category': r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd',
        'price': 123.45
    }

@pytest.fixture
def example_list():
    """Provides a list with unicode escape sequences for testing."""
    return [r'\u05e2\u05e8\u05db\u05ea \u05e9\u05d1\u05d1\u05d9\u05dd', r'H510M K V2']

@pytest.fixture
def example_string():
    """Provides a string with unicode escape sequences for testing."""
    return r'\u05de\u05e7"\u05d8 \u05d9\u05e6\u05e8\u05df\nH510M K V2'

# Tests for decode_unicode_escape
def test_decode_unicode_escape_valid_dict(example_dict):
    """Checks correct behavior with a dictionary containing unicode escape sequences."""
    decoded_dict = decode_unicode_escape(example_dict)
    assert isinstance(decoded_dict, dict)
    assert decoded_dict['product_name'] == 'מקט" יצרן\nH510M K V2'
    assert decoded_dict['category'] == 'ערכת שבבים'
    assert decoded_dict['price'] == 123.45

def test_decode_unicode_escape_valid_list(example_list):
    """Checks correct behavior with a list containing unicode escape sequences."""
    decoded_list = decode_unicode_escape(example_list)
    assert isinstance(decoded_list, list)
    assert decoded_list[0] == 'ערכת שבבים'
    assert decoded_list[1] == 'H510M K V2'

def test_decode_unicode_escape_valid_string(example_string):
    """Checks correct behavior with a string containing unicode escape sequences."""
    decoded_string = decode_unicode_escape(example_string)
    assert isinstance(decoded_string, str)
    assert decoded_string == 'מקט" יצרן\nH510M K V2'

def test_decode_unicode_escape_empty_dict():
    """Checks correct behavior with an empty dictionary."""
    empty_dict = {}
    decoded_empty_dict = decode_unicode_escape(empty_dict)
    assert decoded_empty_dict == {}

def test_decode_unicode_escape_empty_list():
    """Checks correct behavior with an empty list."""
    empty_list = []
    decoded_empty_list = decode_unicode_escape(empty_list)
    assert decoded_empty_list == []

def test_decode_unicode_escape_empty_string():
    """Checks correct behavior with an empty string."""
    empty_string = ""
    decoded_empty_string = decode_unicode_escape(empty_string)
    assert decoded_empty_string == ""

def test_decode_unicode_escape_string_no_escape():
    """Checks correct behavior with a string not containing unicode escape sequences."""
    no_escape_string = "Regular string without escapes"
    decoded_no_escape_string = decode_unicode_escape(no_escape_string)
    assert decoded_no_escape_string == no_escape_string

def test_decode_unicode_escape_nested_dict():
    """Checks correct behavior with nested dictionaries containing unicode escapes."""
    nested_dict = {
        "level1": {
            "level2": r"\u0048\u0065\u006c\u006c\u006f"
        }
    }
    decoded_nested_dict = decode_unicode_escape(nested_dict)
    assert decoded_nested_dict["level1"]["level2"] == "Hello"

def test_decode_unicode_escape_nested_list():
    """Checks correct behavior with nested lists containing unicode escapes."""
    nested_list = [
        [r"\u0048\u0065\u006c\u006c\u006f"],
        [r"\u0057\u006f\u0072\u006c\u0064"]
    ]
    decoded_nested_list = decode_unicode_escape(nested_list)
    assert decoded_nested_list[0][0] == "Hello"
    assert decoded_nested_list[1][0] == "World"


def test_decode_unicode_escape_dict_with_mixed_values():
    """Checks correct behavior with a dictionary containing mixed types including strings and numbers."""
    mixed_dict = {
        "key1": r"\u0041\u0062\u0063",
        "key2": 123,
        "key3": r"\u0044\u0065\u0066"
    }
    decoded_mixed_dict = decode_unicode_escape(mixed_dict)
    assert decoded_mixed_dict["key1"] == "Abc"
    assert decoded_mixed_dict["key2"] == 123
    assert decoded_mixed_dict["key3"] == "Def"

def test_decode_unicode_escape_list_with_mixed_values():
    """Checks correct behavior with a list containing mixed types including strings and numbers."""
    mixed_list = [r"\u0041\u0062\u0063", 123, r"\u0044\u0065\u0066"]
    decoded_mixed_list = decode_unicode_escape(mixed_list)
    assert decoded_mixed_list[0] == "Abc"
    assert decoded_mixed_list[1] == 123
    assert decoded_mixed_list[2] == "Def"

def test_decode_unicode_escape_invalid_unicode():
    """Checks that invalid unicode sequences are not decoded."""
    invalid_unicode_string = r'\u0041\u0062\u0063\uinvalid'
    decoded_invalid_unicode_string = decode_unicode_escape(invalid_unicode_string)
    assert decoded_invalid_unicode_string == 'Abc\\uinvalid'

def test_decode_unicode_escape_non_string_input():
    """Checks behavior with non-string, non-list, and non-dict inputs (int, float, None)."""
    assert decode_unicode_escape(123) == 123
    assert decode_unicode_escape(123.45) == 123.45
    assert decode_unicode_escape(None) is None

def test_decode_unicode_escape_double_escaped_unicode():
    """Checks behavior with double escaped unicode sequences like \\\\u0041."""
    double_escaped_string = r'\\\\u0041\\\\u0062'
    decoded_double_escaped_string = decode_unicode_escape(double_escaped_string)
    assert decoded_double_escaped_string == 'Ab'
```