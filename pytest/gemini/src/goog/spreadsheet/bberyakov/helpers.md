```python
import pytest

from hypotez.src.goog.spreadsheet.bberyakov.helpers import (
    hex_color_to_decimal,
    decimal_color_to_hex,
    hex_to_rgb,
)


def test_hex_color_to_decimal_single_letter():
    """Tests hex_color_to_decimal with a single letter input."""
    assert hex_color_to_decimal("A") == 10
    assert hex_color_to_decimal("Z") == 26
    assert hex_color_to_decimal("a") == 1 #case insensitivity
    assert hex_color_to_decimal("z") == 26
    
    #testing error handling for case where input is not alpha
    with pytest.raises(ValueError):
        hex_color_to_decimal("1")


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double letter input."""
    assert hex_color_to_decimal("AA") == 270
    assert hex_color_to_decimal("AZ") == 280
    assert hex_color_to_decimal("ZZ") == 702
    assert hex_color_to_decimal("aA") == 28


def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with invalid input."""
    with pytest.raises(TypeError):
        hex_color_to_decimal(123) #checking for non-string input
    with pytest.raises(ValueError):
        hex_color_to_decimal("ABC")  # Handling input longer than 2 letters



def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == "A"
    assert decimal_color_to_hex(26) == "Z"
    assert decimal_color_to_hex(27) == "AA"
    assert decimal_color_to_hex(52) == "BA"
    assert decimal_color_to_hex(702) == "ZZZ"
   


def test_decimal_color_to_hex_invalid_input():
    """Tests decimal_color_to_hex with invalid input."""
    with pytest.raises(TypeError):
        decimal_color_to_hex("abc")  # checking for non-numeric input


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("#00FF00") == (0, 255, 0)
    assert hex_to_rgb("FF0000") == (255, 0, 0) #Testing without #


def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input."""
    with pytest.raises(ValueError):
        hex_to_rgb("InvalidHex")  # Invalid hex format
    with pytest.raises(ValueError):
        hex_to_rgb("#FFFF") #Incorrect length
    with pytest.raises(ValueError):
        hex_to_rgb("123456789") #Testing for non-hex values

```