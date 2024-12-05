```python
import pytest
import re
from hypotez.src.utils.string.formatter import StringFormatter

# Tests for remove_line_breaks
def test_remove_line_breaks_valid_input():
    input_str = "This is a\nmultiline\nstring."
    expected_output = "This is a multiline string."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_empty_input():
    input_str = ""
    expected_output = ""
    assert StringFormatter.remove_line_breaks(input_str) == expected_output
    
def test_remove_line_breaks_single_line():
    input_str = "This is a single line."
    expected_output = "This is a single line."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_multiple_types_of_breaks():
    input_str = "This is a\r\nmultiline\nstring.\r"
    expected_output = "This is a multiline string."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output
    

# Tests for remove_htmls
def test_remove_htmls_valid_input():
    input_html = "<p>This is a paragraph.</p>"
    expected_output = "This is a paragraph."
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_remove_htmls_empty_input():
    input_html = ""
    expected_output = ""
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_remove_htmls_multiple_tags():
    input_html = "<p>This <span>is</span> a paragraph.</p>"
    expected_output = "This is a paragraph."
    assert StringFormatter.remove_htmls(input_html) == expected_output
    
def test_remove_htmls_no_tags():
    input_html = "This is a paragraph."
    expected_output = "This is a paragraph."
    assert StringFormatter.remove_htmls(input_html) == expected_output

# Tests for escape_html_tags
def test_escape_html_tags_valid_input():
    input_html = "<p>This is &lt;important&gt;!</p>"
    expected_output = "&lt;p&gt;This is &amp;lt;important&amp;gt;!&lt;/p&gt;"
    assert StringFormatter.escape_html_tags(input_html) == expected_output


def test_escape_html_tags_no_tags():
    input_html = "This is a paragraph."
    expected_output = "This is a paragraph."
    assert StringFormatter.escape_html_tags(input_html) == expected_output



# Tests for clear_numbers
def test_clear_numbers_valid_input():
    input_str = "aaa123.456 cde"
    expected_output = "123.456"
    assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_empty_input():
    input_str = ""
    expected_output = ""
    assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_no_numbers():
    input_str = "abc def"
    expected_output = ""
    assert StringFormatter.clear_numbers(input_str) == expected_output
    
def test_clear_numbers_with_decimal_and_other_characters():
    input_str = "abc12.34xyz"
    expected_output = "12.34"
    assert StringFormatter.clear_numbers(input_str) == expected_output



# Add more test cases for other functions as needed.
```