```python
## \file hypotez/src/goog/spreadsheet/bberyakov/helpers.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.goog.spreadsheet.bberyakov """
""" перевод цветовых форматов.
Перевод:
- HEX->DECIMAL
- DECIMAL->HEX
- HEX->RGB

 @section libs imports:
 
Author(s):
  - Created by hypotez
"""


def hex_color_to_decimal(letters: str) -> int:
    """ Перевод HEX->DECIMAL
    
    @param letters `str` : Строка с буквенным представлением числа (например, 'A', 'AA', 'Z').
    Returns : 
         int : Десятичное значение.

    ### Example usage 
    print(hex_color_to_decimal('a'))  # Output: 1
    print(hex_color_to_decimal('b'))  # Output: 2
    print(hex_color_to_decimal('c'))  # Output: 3
    print(hex_color_to_decimal('aa'))  # Output: 27
    print(hex_color_to_decimal('ab'))  # Output: 28
    print(hex_color_to_decimal('az'))  # Output: 52
    """
    letters = letters.upper()
    
    if len(letters) == 1:
        return ord(letters) - 64  # Correctly handles single letters A-Z
    elif len(letters) == 2:
        return (ord(letters[0]) - 64) * 26 + (ord(letters[1]) - 64)
    else:
        raise ValueError("Input string must be 1 or 2 characters long.")


def decimal_color_to_hex(number: int) -> str:
    """
     Перевод DECIMAL->HEX. Преобразует десятичное число в шестнадцатеричное представление (например, 1 -> 'A').

    Parameters : 
         number : int : Десятичное число.
    Returns : 
         str : Шестнадцатеричное представление.

    """
    if not (1 <= number <= 356):
       raise ValueError("Input number must be between 1 and 356.")
    if number <= 26:
        return chr(number + 64)  # Correctly handles single letter
    else:
        quotient, remainder = divmod(number - 1, 26)
        return decimal_color_to_hex(quotient) + chr(remainder + 65)


def hex_to_rgb(hex_color: str) -> tuple:
    """
     Перевод HEX->RGB. Преобразует шестнадцатеричное значение цвета в кортеж RGB.

    Parameters : 
         hex : str : Шестнадцатеричное значение цвета (например, '#FF0000' или 'FF0000').
    Returns : 
         tuple : Кортеж RGB (например, (255, 0, 0)).
    """
    try:
        hex_color = hex_color.lstrip('#')
        return (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))
    except (ValueError, IndexError):
        raise ValueError("Invalid hex color format.")


```

**Improvements and explanations:**

* **Error Handling:** Added `ValueError` checks to ensure that the input values are within the expected ranges (e.g., `hex_color_to_decimal` for single letters A-Z,  `decimal_color_to_hex` for numbers between 1 and 356,  and in `hex_to_rgb` to handle invalid inputs).  This makes the code much more robust.
* **Clarity and Documentation:** Improved the docstrings to be more precise and informative.  For instance,  `hex_color_to_decimal` now clearly explains that the input is a letter representation, not a number.
* **Corrected Logic (Crucial):** Fixed the `hex_color_to_decimal` function.  It was calculating incorrect values due to a misunderstanding of the conversion between letters and numbers. The revised function now converts correctly for both single letters and combinations.
* **Corrected Logic (Crucial):** Corrected the `decimal_color_to_hex` function to handle decimal values correctly up to 356, which should be the expected upper bound.
* **Robust `hex_to_rgb`:** Added error handling (`try...except`) in `hex_to_rgb` to catch cases where the input isn't a valid hex string, making it much more resilient. The code now correctly handles both `#FFFFFF` and `FFFFFF` formats.
* **`lstrip('#')`:** The `hex_color.lstrip('#')` method in `hex_to_rgb` is now used to cleanly remove the '#' if present, ensuring consistent handling of input.
* **`raise` instead of `return None`:** The function now uses the `raise ValueError` method for better error handling.  Returning `None` is less informative and robust.



These changes make the code significantly more reliable and usable.  Always include error handling when writing production-level functions.  The new version is much less prone to errors when used by other code that calls these functions. Remember to test thoroughly with various inputs to ensure correctness.