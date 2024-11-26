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
    assert hex_color_to_decimal('B') == 11
    assert hex_color_to_decimal('Z') == 26


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double-letter input."""
    assert hex_color_to_decimal('AA') == 27


def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with an invalid input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal('Invalid')


def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'
    assert decimal_color_to_hex(27) == 'AA'
    assert decimal_color_to_hex(52) == 'BA'


def test_decimal_color_to_hex_edge_case():
    """Tests decimal_color_to_hex with edge cases."""
    assert decimal_color_to_hex(0) == ''  # Handle edge case with 0


def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with negative input."""
    with pytest.raises(ValueError):
        decimal_color_to_hex(-1)


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("FF0000") == (255, 0, 0)


def test_hex_to_rgb_no_hash_prefix():
    """Tests hex_to_rgb without '#' prefix."""
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)


def test_hex_to_rgb_invalid_input_length():
    """Tests hex_to_rgb with invalid input length."""
    with pytest.raises(ValueError):
        hex_to_rgb("Invalid")


def test_hex_to_rgb_invalid_input_format():
    """Tests hex_to_rgb with invalid input format."""
    with pytest.raises(ValueError):
        hex_to_rgb("FF00")


```