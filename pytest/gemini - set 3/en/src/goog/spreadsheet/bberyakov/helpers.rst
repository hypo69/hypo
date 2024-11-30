```python
import pytest

from hypotez.src.goog.spreadsheet.bberyakov.helpers import (
    hex_color_to_decimal,
    decimal_color_to_hex,
    hex_to_rgb,
)


def test_hex_color_to_decimal_single_letter():
    """Tests hex_color_to_decimal with a single-letter input."""
    assert hex_color_to_decimal('a') == 1
    assert hex_color_to_decimal('B') == 11
    assert hex_color_to_decimal('Z') == 26


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double-letter input."""
    assert hex_color_to_decimal('AA') == 27 * 26 + 1
    assert hex_color_to_decimal('AZ') == 27 * 26 + 26
    assert hex_color_to_decimal('ZZ') == 26 * 26 + 26

def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with an invalid input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal("invalid")
    with pytest.raises(ValueError):
        hex_color_to_decimal("ABC")


def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid inputs."""
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'
    assert decimal_color_to_hex(27) == 'AA'
    assert decimal_color_to_hex(52) == 'BA'



def test_decimal_color_to_hex_boundary_cases():
    """Tests decimal_color_to_hex with boundary cases."""
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'

def test_decimal_color_to_hex_large_number():
    assert decimal_color_to_hex(701) == 'ZZ'



def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with invalid input."""
    with pytest.raises(ValueError):
        decimal_color_to_hex(-1)
    with pytest.raises(TypeError):
        decimal_color_to_hex("invalid")


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("000000") == (0, 0, 0)
    assert hex_to_rgb("FF0000") == (255, 0, 0)
    assert hex_to_rgb("#FF00FF") == (255, 0, 255)
    assert hex_to_rgb("FF00") == (255,0,0)


def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input."""
    with pytest.raises(ValueError):
        hex_to_rgb("InvalidHex")
    with pytest.raises(ValueError):
        hex_to_rgb("#InvalidHex")
    with pytest.raises(ValueError):
        hex_to_rgb("ABC")
```