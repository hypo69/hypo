## \file ../src/utils/string/normalizer.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Модуль нормализации строк  """
import header
import regex as re
from src.logger import logger
from src.utils.string.formatter import StringFormatter

class StringNormalizer:
    """ Class for normalizing strings."""

    @staticmethod
    def simplify_string(input_str: str) -> str:
        """Simplifies the input string by keeping only letters, digits, and replacing spaces with underscores.

        Args:
            input_str (str): The string to be simplified.
        
        Returns:
            str: The simplified string.
        
        Examples:
            >>> example_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
            >>> simplified_str = StringNormalizer.simplify_string(example_str)
            >>> print(simplified_str)
            'Its_a_test_string_with_single_quotes_numbers_123_and_symbols'
        """
        try:
            # Remove all characters except letters, digits, and spaces using Unicode property for letters (\p{L})
            cleaned_str = re.sub(r'[^\p{L}\p{N}\s]', '', input_str, flags=re.UNICODE)
            # Replace spaces with underscores
            cleaned_str = cleaned_str.replace(' ', '_')
            # Remove consecutive underscores
            cleaned_str = re.sub(r'_+', '_', cleaned_str)
            return cleaned_str
        except Exception as ex:
            logger.error("Error simplifying the string", exc_info=True)
            return input_str

# Example usage
if __name__ == "__main__":
    example_str = "It's a test שלום with 'single qu#otes', пр::ивет 1%3$ and symbols!"
    simplified_str = StringNormalizer.simplify_string(example_str)
    print(simplified_str)  # Output: Its_a_test_string_with_single_quotes_numbers_123_and_symbols
