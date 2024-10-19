## \file src/utils/string/formatter.py
## \file ../src/string/formatter.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" 
String formatting functions.

Functions:
    - remove_line_breaks(input_str: str) -> str
    - remove_htmls(input_html: str) -> str
    - html_escape(input_html: str) -> str
    - remove_non_latin_characters(input_str: str) -> str
    - remove_special_characters(input_str: str | list) -> str
    - escapes_to_html(text: str) -> str
    - symbols2UTF(text: str) -> str
    - clear_numbers(input_str: str) -> str

Data transformation:
    - convert_to_list(input: str | list[str, dict, list[dict]], delimiter: str = ',') -> list | bool
    - extract_value_from_parentheses_with_lead_dollar(input_str: str) -> str | list | bool
    - clean_url_from_protocols(url: str) -> str
"""
import re
import html
from typing import List, Dict
from urllib.parse import urlparse, parse_qs
from src.logger import logger
from .html_escapes import html_escapes

class StringFormatter:
    """  
    StringFormatter (String Formatting):
    
    @details 
    This module provides functions for formatting strings, such as removing line breaks, HTML tags, non-Latin characters, and special characters.
    """

    @staticmethod
    def remove_line_breaks(input_str: str) -> str:
        """
        Removes line breaks from the input string.
        
        Args:
            input_str (str): Input string.
        
        Returns:
            str: A string with line breaks removed.
        """
        return input_str.replace("\n", " ").replace("\r", " ").strip()

    @staticmethod
    def remove_htmls(input_html: str) -> str:
        """
        Removes HTML tags from the input string.
        
        Args:
            input_html (str): Input HTML string.
        
        Returns:
            str: A string with HTML tags removed.
        """
        return re.sub(r'<.*?>', '', input_html).strip()

    @staticmethod
    def escape_html_tags(input_html: str) -> str:
        """
        Replaces `<` and `>` with `&lt;` and `&gt;` in the input HTML string.
        
        Args:
            input_html (str): Input HTML string.
        
        Returns:
            str: An escaped HTML string.
        """
        return html.escape(input_html)
    
    @staticmethod
    def escape_to_html(text: str) -> str:
        """
        Replaces non-Latin characters and digits with HTML entities.
        
        Args:
            text (str): Input text.
        
        Returns:
            str: Output text with non-Latin characters replaced by HTML entities.
        """
        return ''.join(html_escapes.get(char, char) for char in text)
    
    @staticmethod
    def remove_non_latin_characters(input_str: str) -> str:
        """
        Removes non-Latin characters from the input string.
        
        Args:
            input_str (str): Input string.
        
        Returns:
            str: A string with non-Latin characters removed.
        """
        return re.sub(r'[^a-zA-Z\s]', '', input_str).strip()
    
    @staticmethod
    def remove_special_characters(input_str: str | list) -> str:
        """  
        Removes special characters not allowed in the 'name' field in Prestashop, e.g., `#`, `<`, `>`.
        
        Args:
            input_str (str | list): Input string or list of strings.
        
        Returns:
            str: Processed string with special characters removed.
        """
        if isinstance(input_str, list):
            return [re.sub(r'[^a-zA-Z0-9\s]', '', s) for s in input_str]
        return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

    @staticmethod
    def clear_numbers(input_str: str) -> str:
        """
        Clears a string from non-decimal numbers or points.
        
        Args:
            input_str (str): Input string.
        
        Returns:
            str: Cleared string containing only decimal numbers and points.

        Example:
            @code
            > input_str = 'aaa123.456 cde'
            > output_str = StringFormatter.clear_numbers(input_str)
            > print(output_str)
            > 123.456
        """
        return re.sub(r'[^\d\.]', '', input_str)
