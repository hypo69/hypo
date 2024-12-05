```python
import pytest
from hypotez.src.utils.string import normalize_string, normalize_int, normalize_float, normalize_boolean

# Tests for normalize_string
def test_normalize_string_valid_input():
    """Checks correct behavior with valid input (string)."""
    input_string = "  This is a test string.  "
    expected_output = "This is a test string."
    assert normalize_string(input_string) == expected_output

def test_normalize_string_empty_string():
    """Checks behavior with empty input string."""
    input_string = ""
    expected_output = ""
    assert normalize_string(input_string) == expected_output
    
def test_normalize_string_none_input():
    """Checks behavior with None input."""
    input_string = None
    expected_output = ""  # or raise exception
    assert normalize_string(input_string) == expected_output

def test_normalize_string_invalid_input():
    """Checks correct handling of invalid input (non-string)."""
    input_value = 123  # Integer
    with pytest.raises(TypeError):
        normalize_string(input_value)

# Tests for normalize_int
def test_normalize_int_valid_input():
    """Checks correct behavior with valid input (integer)."""
    input_int = "123"
    expected_output = 123
    assert normalize_int(input_int) == expected_output

def test_normalize_int_invalid_input():
    """Checks correct handling of invalid input (non-integer)."""
    input_value = "abc"
    with pytest.raises(ValueError):
        normalize_int(input_value)
        
def test_normalize_int_empty_string():
    """Checks behavior with empty input string."""
    input_int = ""
    with pytest.raises(ValueError):
        normalize_int(input_int)

def test_normalize_int_none_input():
    """Checks behavior with None input."""
    input_int = None
    with pytest.raises(TypeError):
        normalize_int(input_int)

# Tests for normalize_float
def test_normalize_float_valid_input():
    """Checks correct behavior with valid input (float)."""
    input_float = "3.14"
    expected_output = 3.14
    assert normalize_float(input_float) == expected_output

def test_normalize_float_invalid_input():
    """Checks correct handling of invalid input (non-float)."""
    input_value = "abc"
    with pytest.raises(ValueError):
        normalize_float(input_value)

def test_normalize_float_none_input():
    """Checks behavior with None input."""
    input_float = None
    with pytest.raises(TypeError):
        normalize_float(input_float)


# Tests for normalize_boolean
def test_normalize_boolean_valid_input_true():
    """Checks correct behavior with valid input (true)."""
    input_bool = "True"
    expected_output = True
    assert normalize_boolean(input_bool) == expected_output

def test_normalize_boolean_valid_input_false():
    """Checks correct behavior with valid input (false)."""
    input_bool = "False"
    expected_output = False
    assert normalize_boolean(input_bool) == expected_output

def test_normalize_boolean_invalid_input():
    """Checks correct handling of invalid input (non-boolean)."""
    input_value = "abc"
    with pytest.raises(ValueError):
        normalize_boolean(input_value)
        
def test_normalize_boolean_none_input():
    """Checks behavior with None input."""
    input_bool = None
    with pytest.raises(TypeError):
        normalize_boolean(input_bool)

```