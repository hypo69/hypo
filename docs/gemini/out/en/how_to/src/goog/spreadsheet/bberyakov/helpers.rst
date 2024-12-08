rst
How to use the color conversion functions
=========================================================================================

Description
-------------------------
This Python code provides functions for converting colors between different formats. It includes functions for converting hexadecimal color codes to decimal representations, decimal representations to hexadecimal, and hexadecimal color codes to RGB tuples.

Execution steps
-------------------------
1. **Import the module:** Ensure the `helpers.py` file is in your Python project's directory or accessible through the import path.

2. **`hex_color_to_decimal(letters)` function:**
   - Takes a hexadecimal color code (e.g., "FF") as input.
   - Converts each letter in the hex code to its decimal equivalent (e.g., 'A' to 10).
   - Calculates the decimal value based on the position of the letters in the hexadecimal code (e.g., "FF" to 255).
   - Returns the calculated decimal value.

3. **`decimal_color_to_hex(number)` function:**
   - Takes a decimal color value (e.g., 255) as input.
   - Converts the decimal value to its hexadecimal equivalent by handling single and double-letter hexadecimal codes (e.g., 10 to "A", 26 to "Z", 27 to "AA", and so on.).
   - Returns the resulting hexadecimal color code.


4. **`hex_to_rgb(hex)` function:**
   - Takes a hexadecimal color code (e.g., "#FF0000" or "FF0000") as input.
   - Extracts the RGB values from the hexadecimal code.
   - Converts each pair of hexadecimal characters to its corresponding decimal RGB value (e.g., "FF" to 255).
   - Returns a tuple containing the red, green, and blue values (e.g., (255, 0, 0)).

Usage example
-------------------------
.. code-block:: python

    from goog.spreadsheet.bberyakov.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

    # Example 1: Convert hexadecimal to decimal
    hex_color = "FF"
    decimal_value = hex_color_to_decimal(hex_color)
    print(f"Decimal value of {hex_color}: {decimal_value}")  # Output: Decimal value of FF: 255


    # Example 2: Convert decimal to hexadecimal
    decimal_number = 255
    hex_representation = decimal_color_to_hex(decimal_number)
    print(f"Hexadecimal representation of {decimal_number}: {hex_representation}") # Output: Hexadecimal representation of 255: FF


    # Example 3: Convert hexadecimal to RGB
    hex_color_with_hash = "#FF0000"
    rgb_tuple = hex_to_rgb(hex_color_with_hash)
    print(f"RGB tuple of {hex_color_with_hash}: {rgb_tuple}")  # Output: RGB tuple of #FF0000: (255, 0, 0)


    hex_color_without_hash = "00FF00"
    rgb_tuple = hex_to_rgb(hex_color_without_hash)
    print(f"RGB tuple of {hex_color_without_hash}: {rgb_tuple}") # Output: RGB tuple of 00FF00: (0, 255, 0)