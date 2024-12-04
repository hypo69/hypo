```python
import pytest

def hex_color_to_decimal(letters: str) -> int:
    """ Перевод HEX->DECIMAL """
    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        """ Перевод буквы в число """
        return int(ord(letter.lower()) - 96)
    
    if len(letters) == 1:
        return letter_to_number(letters)
    elif len(letters) == 2:
        return (letter_to_number(letters[0]) * 26) + letter_to_number(letters[1])
    else:
        return 0


def decimal_color_to_hex(number: int) -> str:
    """ Перевод DECIMAL->HEX """
    if not isinstance(number, int) or number < 1 or number > 676:
        return ""

    if number <= 26:
        return chr(number + 96).upper()
    else:
        quotient, remainder = divmod(number - 1, 26)
        return decimal_color_to_hex(quotient) + chr(remainder + 97).upper()


def hex_to_rgb(hex: str) -> tuple:
    """ Перевод HEX->RGB """
    hex = hex[1:] if '#' in hex else hex
    if len(hex) != 6:
      return (0,0,0)
    try:
        return (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16))
    except ValueError:
        return (0,0,0)


# Tests for hex_color_to_decimal
def test_hex_color_to_decimal_single_letter():
    assert hex_color_to_decimal('A') == 10
    assert hex_color_to_decimal('Z') == 26

def test_hex_color_to_decimal_double_letter():
    assert hex_color_to_decimal('AA') == 27 * 26 + 1
    assert hex_color_to_decimal('AZ') == 27 * 26 + 26


def test_hex_color_to_decimal_invalid_input():
    assert hex_color_to_decimal('ABC') == 0
    assert hex_color_to_decimal('') == 0
    assert hex_color_to_decimal('A B') == 0


# Tests for decimal_color_to_hex
def test_decimal_color_to_hex_valid_input():
    assert decimal_color_to_hex(1) == 'A'
    assert decimal_color_to_hex(26) == 'Z'
    assert decimal_color_to_hex(27) == 'AA'
    assert decimal_color_to_hex(52) == 'BA'
    assert decimal_color_to_hex(676) == 'ZZ'

def test_decimal_color_to_hex_invalid_input():
    assert decimal_color_to_hex(0) == ""
    assert decimal_color_to_hex(270) == 'AJ'
    assert decimal_color_to_hex(-1) == ""


# Tests for hex_to_rgb
def test_hex_to_rgb_valid_input():
    assert hex_to_rgb("#FF0000") == (255, 0, 0)
    assert hex_to_rgb("FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("00FF00") == (0, 255, 0)


def test_hex_to_rgb_invalid_input():
  assert hex_to_rgb("#InvalidHex") == (0,0,0)
  assert hex_to_rgb("") == (0,0,0)
  assert hex_to_rgb("12345") == (0,0,0)
  assert hex_to_rgb("1") == (0,0,0)
```