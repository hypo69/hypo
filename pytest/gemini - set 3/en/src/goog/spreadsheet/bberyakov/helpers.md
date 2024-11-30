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
    assert hex_color_to_decimal('F') == 15
    assert hex_color_to_decimal('z') == 0  # Handling lower-case input


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double-letter input."""
    assert hex_color_to_decimal('AA') == 2700 + 10


def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with invalid input."""
    with pytest.raises(ValueError):
        hex_color_to_decimal("invalid")  # Non-hex characters
    with pytest.raises(ValueError):
        hex_color_to_decimal("")  # Empty string

    with pytest.raises(ValueError):
         hex_color_to_decimal("ABCDEF")  # Invalid input


def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == "A"
    assert decimal_color_to_hex(26) == "Z"
    assert decimal_color_to_hex(27) == "AA"
    assert decimal_color_to_hex(52) == "BA"


def test_decimal_color_to_hex_edge_case():
    """Tests decimal_color_to_hex with edge cases."""
    assert decimal_color_to_hex(0) == "" #edge case handling
    assert decimal_color_to_hex(27) == "AA"


def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with invalid input."""
    with pytest.raises(TypeError):
        decimal_color_to_hex("invalid")  # Non-integer input


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FF0000") == (255, 0, 0)
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("00FF00") == (0, 255, 0)
    assert hex_to_rgb("#008000") == (0, 128, 0)


def test_hex_to_rgb_no_hash():
    """Tests hex_to_rgb without the '#' symbol."""
    assert hex_to_rgb("FF0000") == (255, 0, 0)


def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input."""
    with pytest.raises(ValueError):
        hex_to_rgb("InvalidHex")
    with pytest.raises(ValueError):
        hex_to_rgb("")


def test_hex_to_rgb_short_input():
    """Tests hex_to_rgb with short input."""
    with pytest.raises(ValueError):
        hex_to_rgb("FF")

```