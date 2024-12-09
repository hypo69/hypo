```python
import pytest

def hex_color_to_decimal(letters: str) -> int:
    """ Перевод HEX->DECIMAL
    
    @param letters `str` : [description]
    Returns : 
         int : [description]
    """
    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        return int(ord(letter.lower()) - 96)

    return letter_to_number(letters) if len(letters) == 1 else (letter_to_number(letters[0]) * 26) + letter_to_number(letters[1])

def decimal_color_to_hex(number: int) -> str:
    """
     [Function's description]

    Parameters : 
         number : int : [description]
    Returns : 
         str : [description]
    """
    if number <= 26:
        return chr(number + 96).upper()
    else:
        quotient, remainder = divmod(number - 1, 26)
        return decimal_color_to_hex(quotient) + chr(remainder + 97).upper()

def hex_to_rgb (hex: str) -> tuple:
    """
     [Function's description]

    Parameters : 
         hex : str : [description]
    Returns : 
         tuple : [description]
    """
    hex = hex[1:] if '#' in hex else hex
    try:
        return (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16))
    except ValueError as e:
        raise ValueError("Invalid hexadecimal color code") from e

def test_hex_color_to_decimal_single_letter():
    """Tests hex_color_to_decimal with a single-letter input."""
    assert hex_color_to_decimal("A") == 10
    assert hex_color_to_decimal("Z") == 26


def test_hex_color_to_decimal_double_letter():
    """Tests hex_color_to_decimal with a double-letter input."""
    assert hex_color_to_decimal("AA") == 27
    assert hex_color_to_decimal("ZZ") == 702


def test_hex_color_to_decimal_invalid_input():
    """Tests hex_color_to_decimal with invalid input (non-letters)."""
    with pytest.raises(ValueError):
        hex_color_to_decimal("1A")  # Tests case with a number
    with pytest.raises(ValueError):
        hex_color_to_decimal("AB1")  #Tests case with more than 2 letters



def test_decimal_color_to_hex_valid_input():
    """Tests decimal_color_to_hex with valid input."""
    assert decimal_color_to_hex(1) == "A"
    assert decimal_color_to_hex(26) == "Z"
    assert decimal_color_to_hex(27) == "AA"
    assert decimal_color_to_hex(702) == "ZZ"


def test_decimal_color_to_hex_zero():
    """Tests decimal_color_to_hex with input 0."""
    with pytest.raises(ValueError):
        decimal_color_to_hex(0)


def test_hex_to_rgb_valid_input():
    """Tests hex_to_rgb with valid input."""
    assert hex_to_rgb("#FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("00FF00") == (0, 255, 0)
    assert hex_to_rgb("FF0000") == (255, 0, 0)

def test_hex_to_rgb_invalid_input():
    """Tests hex_to_rgb with invalid input (non-hex characters)."""
    with pytest.raises(ValueError) as excinfo:
        hex_to_rgb("InvalidHex")
    assert "Invalid hexadecimal color code" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        hex_to_rgb("#InvalidHex")
    assert "Invalid hexadecimal color code" in str(excinfo.value)

def test_hex_to_rgb_no_hash():
    """Tests hex_to_rgb with input without '#'."""
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)
```