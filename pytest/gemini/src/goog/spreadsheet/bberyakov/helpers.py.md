```python
import pytest
from hypotez.src.goog.spreadsheet.bberyakov.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

# Test cases for hex_color_to_decimal
def test_hex_color_to_decimal_single_letter():
    """Checks conversion of single letter hex to decimal."""
    assert hex_color_to_decimal("a") == "1"
    assert hex_color_to_decimal("b") == "2"
    assert hex_color_to_decimal("z") == "26"
    assert hex_color_to_decimal("A") == "1"
    assert hex_color_to_decimal("Z") == "26"
    
def test_hex_color_to_decimal_double_letters():
    """Checks conversion of double letter hex to decimal."""
    assert hex_color_to_decimal("aa") == 27
    assert hex_color_to_decimal("ab") == 28
    assert hex_color_to_decimal("az") == 52
    assert hex_color_to_decimal("ba") == 53
    assert hex_color_to_decimal("bz") == 78
    assert hex_color_to_decimal("AA") == 27
    assert hex_color_to_decimal("AZ") == 52

def test_hex_color_to_decimal_invalid_input():
    """Checks how function handles invalid inputs like empty string, special chars, numbers"""
    with pytest.raises(AttributeError): # ord() cant convert digits or special symbols
      hex_color_to_decimal("")
    with pytest.raises(AttributeError): 
       hex_color_to_decimal("#")
    with pytest.raises(AttributeError):
       hex_color_to_decimal("1")
    with pytest.raises(AttributeError):
        hex_color_to_decimal("1a")
    with pytest.raises(AttributeError):
        hex_color_to_decimal("a1")
    with pytest.raises(AttributeError):
        hex_color_to_decimal("a#")

def test_hex_color_to_decimal_long_string():
    """Checks the behavior when a string longer than 2 chars is passed"""
    with pytest.raises(IndexError):
       hex_color_to_decimal("abc")
    with pytest.raises(IndexError):
       hex_color_to_decimal("abcd")

# Test cases for decimal_color_to_hex
def test_decimal_color_to_hex_single_digit():
    """Checks conversion of single digit decimal to hex."""
    assert decimal_color_to_hex(1) == "A"
    assert decimal_color_to_hex(2) == "B"
    assert decimal_color_to_hex(26) == "Z"

def test_decimal_color_to_hex_double_digit():
    """Checks conversion of double digit decimal to hex."""
    assert decimal_color_to_hex(27) == "AA"
    assert decimal_color_to_hex(28) == "AB"
    assert decimal_color_to_hex(52) == "AZ"
    assert decimal_color_to_hex(53) == "BA"
    assert decimal_color_to_hex(78) == "BZ"
    

def test_decimal_color_to_hex_edge_cases():
    """Checks behavior with edge cases."""
    assert decimal_color_to_hex(0) == "A"
    assert decimal_color_to_hex(26 * 26) == "ZZ" # Test max valid value

def test_decimal_color_to_hex_invalid_input():
    """Checks the behavior when invalid input are passed"""
    with pytest.raises(TypeError):
        decimal_color_to_hex("a")  
    with pytest.raises(RecursionError):
        decimal_color_to_hex(26*26+1) # invalid input
    with pytest.raises(RecursionError):
       decimal_color_to_hex(-1) 
       

# Test cases for hex_to_rgb
def test_hex_to_rgb_valid_hex():
    """Checks conversion of valid hex to RGB."""
    assert hex_to_rgb("#FFFFFF") == (255, 255, 255)
    assert hex_to_rgb("000000") == (0, 0, 0)
    assert hex_to_rgb("#FF0000") == (255, 0, 0)
    assert hex_to_rgb("00FF00") == (0, 255, 0)
    assert hex_to_rgb("#0000FF") == (0, 0, 255)
    assert hex_to_rgb("ffffff") == (255, 255, 255)
    assert hex_to_rgb("fFfFfF") == (255, 255, 255)
    assert hex_to_rgb("#fFfFfF") == (255, 255, 255)

def test_hex_to_rgb_short_hex():
    """Checks conversion of 3 letter hex to RGB"""
    assert hex_to_rgb("#FFF") == (255, 255, 255)
    assert hex_to_rgb("000") == (0, 0, 0)
    assert hex_to_rgb("#F00") == (255, 0, 0)
    assert hex_to_rgb("0F0") == (0, 255, 0)
    assert hex_to_rgb("#00F") == (0, 0, 255)
    assert hex_to_rgb("fff") == (255, 255, 255)
    assert hex_to_rgb("f0f") == (255,0,255)
    assert hex_to_rgb("#f0f") == (255,0,255)

def test_hex_to_rgb_invalid_hex():
    """Checks how function handles invalid hex formats."""
    with pytest.raises(ValueError):
        hex_to_rgb("invalid")
    with pytest.raises(ValueError):
       hex_to_rgb("#invalid")
    with pytest.raises(ValueError):
        hex_to_rgb("#12345")
    with pytest.raises(ValueError):
       hex_to_rgb("#1234567")
    with pytest.raises(ValueError):
       hex_to_rgb("#1234")
    with pytest.raises(ValueError):
        hex_to_rgb("#")
    with pytest.raises(ValueError):
        hex_to_rgb("")

def test_hex_to_rgb_empty():
    """Checks behavior when empty string is passed"""
    with pytest.raises(ValueError):
        hex_to_rgb("")
```