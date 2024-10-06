## \file ../src/goog/spreadsheet/bberyakov/helpers.py
## \file src/utils/interface/goog/helpers.py
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
        


