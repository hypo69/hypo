# <input code>

```python
## \file hypotez/src/goog/spreadsheet/bberyakov/helpers.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet.bberyakov 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
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
    
    @param letters `str` : [description]
    Returns : 
         int : [description]

    ### Example usage 
    print(number_to_letter(1))  # Output: 'a' \n
    print(number_to_letter(2))  # Output: 'b' \n
    print(number_to_letter(3))  # Output: 'c' \n
    print(number_to_letter(27))  # Output: 'aa' \n
    print(number_to_letter(28))  # Output: 'ab' \n
    print(number_to_letter(29))  # Output: 'ac' \n
    """
    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        """
         [Function's description]

        Parameters : 
             letter : str : [description]
        Returns : 
             int : [description]

        """
        """
        ord() function returns the Unicode code from a given character. \n
        print(ord('a'))  # Output: 97 \n
        """
        return str (ord (letter.lower()) - 96).upper()
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
        return str (chr (number + 96)).upper()
    else:
        quotient, remainder = divmod (number - 1, 26)
        return str ( decimal_color_to_hex (quotient) + chr (remainder + 97) ).upper()


def hex_to_rgb (hex: str) -> tuple:
    """
     [Function's description]

    Parameters : 
         hex : str : [description]
    Returns : 
         tuple : [description]

    """
        """
        #FFFFFF -> (255, 255, 255) \n

        `hex`: color in hexadecimal
        """
        hex = hex[1:] if '#' in hex else hex           
        return (int (hex[:2], 16), int (hex[2:4], 16), int (hex[4:], 16) )
        

```

# <algorithm>

The code defines functions for converting colors between hexadecimal (HEX), decimal, and RGB formats.

**hex_color_to_decimal(letters: str) -> int:**

1. Converts the input `letters` (hexadecimal color code) to uppercase.
2. Defines an inner function `letter_to_number` that converts a single letter to its corresponding decimal value (A=10, B=11, etc.).
3. If `letters` is a single letter, it returns the corresponding decimal value; otherwise, it calculates the decimal value by combining the decimal values of the two letters (e.g., "AA" = A*26 + A).

**decimal_color_to_hex(number: int) -> str:**

1. If the input `number` is less than or equal to 26, it converts it directly to a single-letter hexadecimal character.
2. Otherwise, it calculates the quotient and remainder when dividing the number by 26.
3. Recursively calls itself with the quotient and appends the corresponding letter for the remainder to generate the full hexadecimal string.

**hex_to_rgb(hex: str) -> tuple:**

1. Extracts the hexadecimal color code (removing the '#' if present).
2. Converts the first two characters, the next two, and the last two characters to integer values in base 16 (hexadecimal).
3. Returns a tuple containing the red, green, and blue values (RGB).


# <mermaid>

```mermaid
graph TD
    A[Input HEX Color] --> B{hex_color_to_decimal};
    B -- Single letter --> C[Letter to Decimal];
    B -- Double letter --> D[Combine Letters];
    C --> E[Return Decimal Value];
    D --> F[Return Combined Decimal Value];
    
    G[Input Decimal Color] --> H{decimal_color_to_hex};
    H -- Number <= 26 --> I[Convert to Letter];
    H -- Number > 26 --> J[Divide by 26, Recurse];
    I --> K[Return Letter];
    J --> L[Recurse, Combine Result];
    
    M[Input HEX Color (RGB)] --> N{hex_to_rgb};
    N -- Extract components --> O[Convert to Integer (base 16)];
    O --> P[Return RGB Tuple];
```

This mermaid diagram shows the functions and their relationships, with arrows representing data flow between them.  The functions are independent but work together to perform color conversions.


# <explanation>

**Imports:**

There are no imports in this code, so the analysis does not relate to any other package/module.


**Classes:**

There are no classes defined.


**Functions:**

*   **`hex_color_to_decimal(letters: str) -> int`**: This function takes a hexadecimal color code (e.g., "FF" or "AA") as input and returns its decimal equivalent (e.g., 255 or 170).  It handles both single-letter and double-letter hexadecimal codes. The `letter_to_number` helper function converts individual hexadecimal characters to their decimal values.

*   **`decimal_color_to_hex(number: int) -> str`**: This function performs the reverse operation: converting a decimal color value to its hexadecimal equivalent (e.g., 255 to "FF"). It's a recursive function, efficiently handling numbers greater than 26.

*   **`hex_to_rgb(hex: str) -> tuple`**: This function converts a hexadecimal color code to its RGB representation (a tuple of three integers). It extracts the red, green, and blue components from the input hexadecimal string and returns them as an integer tuple.  It correctly handles both '#' prefixed and plain hexadecimal codes.



**Variables:**

*   **`MODE`**: A constant string, likely used for controlling different modes of operation (e.g., 'dev' for development mode). This variable is not used within the functions, so its role is outside the context of these color conversion functions.


**Possible Errors/Improvements:**

*   **Error Handling:** The code lacks robust error handling.  If the input to `hex_color_to_decimal` is not a valid hexadecimal string (e.g., "XYZ"), an `IndexError` might occur. Similarly, `hex_to_rgb` could fail if the input string isn't of the correct format. Adding checks for valid input would enhance the code's reliability.
*   **Input Validation:** The code could be improved by validating the input values to ensure they are within the expected ranges for hexadecimal and decimal color components.
*   **Docstrings:** While the docstrings are present, they could be more comprehensive to include edge cases and potential use scenarios. Examples should include more elaborate cases for `hex_color_to_decimal` (like "ABC" "XYZ").


**Relationship to other parts of the project:**

Without knowing the larger context of the `hypotez` project, it's hard to determine how these helper functions integrate.  They likely serve as utility functions to be used by other parts of the codebase, e.g., for processing spreadsheet data that includes color information.