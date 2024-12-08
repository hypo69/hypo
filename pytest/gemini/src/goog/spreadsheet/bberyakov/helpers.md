```python
import pytest

# Tests for hex_color_to_decimal
def test_hex_color_to_decimal_single_letter():
    """Tests hex_color_to_decimal with a single letter input."""
    assert hex_color_to_decimal('a') == 1
    assert hex_color_to_decimal('Z') == 26

def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double letter input."""
    assert hex_color_to_decimal('AA') == 27 * 26 + 1
    assert hex_color_to_decimal('ZZ') == 26 * 26 + 26

def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with an invalid input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal('Invalid')

def test_hex_color_to_decimal_empty_input():
    """Tests hex_color_to_decimal with an empty input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal('')



# Tests for decimal_color_to_hex
def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'
    assert decimal_color_to_hex(27) == 'AA'
    assert decimal_color_to_hex(702) == 'ZZ' # Example boundary case

def test_decimal_color_to_hex_edge_case_large_number():
    """Tests decimal_color_to_hex with a large input number."""
    assert decimal_color_to_hex(702) == 'ZZ'

def test_decimal_color_to_hex_zero():
    """Tests decimal_color_to_hex with zero input."""
    assert decimal_color_to_hex(0) == '' # Should raise exception if it tries to convert -1 to char

def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with an invalid input (non-positive integer)."""
    with pytest.raises(ValueError):
        decimal_color_to_hex(-1)

# Tests for hex_to_rgb
def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input (including #)."""
    assert hex_to_rgb('#FFFFFF') == (255, 255, 255)
    assert hex_to_rgb('FFFFFF') == (255, 255, 255)
    assert hex_to_rgb('#000000') == (0, 0, 0)
    assert hex_to_rgb('00FF00') == (0, 255, 0)

def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input (incorrect format)."""
    with pytest.raises(ValueError):
        hex_to_rgb('InvalidHex')


def test_hex_to_rgb_input_with_no_hash():
    """Tests hex_to_rgb with input string without #"""
    assert hex_to_rgb("00FF00") == (0, 255, 0)

def test_hex_to_rgb_input_with_missing_value():
    """Tests hex_to_rgb with input that missing part of value."""
    with pytest.raises(ValueError):
        hex_to_rgb("00FF")




```