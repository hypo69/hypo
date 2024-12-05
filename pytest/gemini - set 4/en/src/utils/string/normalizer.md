```python
import pytest
from decimal import Decimal
from hypotez.src.utils.string.normalizer import normalize_boolean, normalize_string, normalize_int, normalize_float

# Fixture definitions for test data
@pytest.fixture
def boolean_data():
    return [
        ("true", True),
        ("1", True),
        ("yes", True),
        ("y", True),
        ("on", True),
        ("false", False),
        ("0", False),
        ("no", False),
        ("n", False),
        ("off", False),
        (True, True),
        (False, False),
        (1, True),
        (0, False),
        ("abc", "abc"),  # Invalid boolean input
        (None, None),
        (123, 123) #Integer
    ]


@pytest.fixture
def string_data():
    return [
        ("Hello World!", "Hello World!"),
        (["Hello", " World!"], "Hello World!"),
        ("  Hello  World!  ", "Hello World!"),
        ("<h1>Hello</h1>", "Hello"), # Test HTML removal
        ("<p>World!</p>", "World!"), # Test HTML removal
        ("\n\nHello World!\n", "Hello World!"), # Test line break removal
        ("Hello<br/>World!", "HelloWorld!"), # Test line break removal
        ("Hello world!", "Hello world!"), # Test with no transformations needed
        (None, None),  # None should return None
        (["hello", " world"], "hello world"),
    ]


@pytest.fixture
def int_data():
    return [
        ("42", 42),
        (42, 42),
        ("123.45", 123),
        (123.45, 123),
        (Decimal("10.5"), 10),  # Test Decimal input
        ("abc", "abc"),  # Test invalid input string
        (None, None),
    ]


@pytest.fixture
def float_data():
    return [
        ("3.14", 3.14),
        (3.14, 3.14),
        ("123.456", 123.456),
        (123.456, 123.456),
        ("abc", "abc"),
        ([1, "2.5", 3], [1.0, 2.5, 3.0]),  # test list of floats
        (None, None),
        ([], [])
    ]
    


# Tests for normalize_boolean
def test_normalize_boolean_valid(boolean_data):
    for input_value, expected_output in boolean_data:
        result = normalize_boolean(input_value)
        assert result == expected_output


# Tests for normalize_string
def test_normalize_string_valid(string_data):
    for input_value, expected_output in string_data:
        result = normalize_string(input_value)
        assert result == expected_output.encode('utf-8').decode('utf-8')


# Tests for normalize_int
def test_normalize_int_valid(int_data):
    for input_value, expected_output in int_data:
        result = normalize_int(input_value)
        assert result == expected_output



# Tests for normalize_float
def test_normalize_float_valid(float_data):
    for input_value, expected_output in float_data:
        result = normalize_float(input_value)
        if isinstance(result, list):
            assert result == expected_output
        else:
            assert result == expected_output

# Test for edge cases and exception handling (general)
def test_normalize_boolean_invalid():
  assert normalize_boolean("invalid") == "invalid"

def test_normalize_string_invalid_input_type():
  with pytest.raises(TypeError):
      normalize_string(123)

def test_normalize_int_invalid_input_type():
  with pytest.raises(TypeError):
      normalize_int("abc")

def test_normalize_float_invalid_input_type():
  with pytest.raises(ValueError):
      normalize_float("xyz")


```