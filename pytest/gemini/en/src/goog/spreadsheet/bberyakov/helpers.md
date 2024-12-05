```python
import pytest

from hypotez.src.goog.spreadsheet.bberyakov.helpers import (
    hex_color_to_decimal,
    decimal_color_to_hex,
    hex_to_rgb,
)


def test_hex_color_to_decimal_single_letter():
    """Tests hex_color_to_decimal with a single-letter input."""
    assert hex_color_to_decimal('A') == 10
    assert hex_color_to_decimal('Z') == 26
    assert hex_color_to_decimal('a') == 1  # test lowercase input
    assert hex_color_to_decimal('z') == 26  # test lowercase input


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double-letter input."""
    assert hex_color_to_decimal('AA') == 270
    assert hex_color_to_decimal('ZZ') == 676
    assert hex_color_to_decimal('aA') == 286
    assert hex_color_to_decimal('Bb') == 302
    assert hex_color_to_decimal("ab") == 28


def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with invalid input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal("ABC")  # raises error for input with more than 2 characters
    with pytest.raises(ValueError):
        hex_color_to_decimal("1")  # raises error for non-alphanumeric input


def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'
    assert decimal_color_to_hex(27) == 'AA'
    assert decimal_color_to_hex(52) == 'BA'


def test_decimal_color_to_hex_edge_case():
    """Tests decimal_color_to_hex with edge cases."""
    assert decimal_color_to_hex(0) == ''  # Handles zero input
    assert decimal_color_to_hex(52) == 'BA'
    assert decimal_color_to_hex(702) == 'AAA'  # Handles larger numbers


def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with invalid input."""
    with pytest.raises(ValueError):
        decimal_color_to_hex(-1)  # Raises error for negative input


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FF0000") == (255, 0, 0)
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("#FFAA00") == (255, 170, 0)
    assert hex_to_rgb("FF00FF") == (255, 0, 255)


def test_hex_to_rgb_no_hash():
    """Tests hex_to_rgb without '#' prefix."""
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("FF0000") == (255, 0, 0)


def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input."""
    with pytest.raises(ValueError):
        hex_to_rgb("invalidhex")  # Raises error for invalid hex strings
    with pytest.raises(ValueError):
        hex_to_rgb("#")  # Raises error for invalid hex string


```