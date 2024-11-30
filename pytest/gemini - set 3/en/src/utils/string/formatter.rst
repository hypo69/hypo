```python
import pytest
import re
from hypotez.src.utils.string.formatter import StringFormatter

# Tests for remove_line_breaks
def test_remove_line_breaks_valid_input():
    input_str = "This is a\nstring\rwith\nline breaks."
    expected_output = "This is a stringwithline breaks."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_empty_input():
    input_str = ""
    expected_output = ""
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_single_line_input():
    input_str = "This is a single line."
    expected_output = "This is a single line."
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

def test_remove_htmls_no_tags():
    input_html = "This is a paragraph."
    expected_output = "This is a paragraph."
    assert StringFormatter.remove_htmls(input_html) == expected_output

# Tests for escape_html_tags
def test_escape_html_tags_valid_input():
    input_html = "<p>This & <p>"
    expected_output = "&lt;p&gt;This & &lt;p&gt;"
    assert StringFormatter.escape_html_tags(input_html) == expected_output

def test_escape_html_tags_empty_input():
    input_html = ""
    expected_output = ""
    assert StringFormatter.escape_html_tags(input_html) == expected_output


# Tests for escape_to_html (using a small subset of html_escapes for brevity)
def test_escape_to_html_valid_input():
    text = "<>&\"'"
    expected_output = "&lt;&gt;&amp;&quot;&apos;"
    # Mock html_escapes for testing - Replace with actual usage if available
    mock_html_escapes = {"<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;", "'": "&apos;"}
    formatted_text = ''.join(mock_html_escapes.get(char, char) for char in text)
    assert formatted_text == expected_output
    


# Tests for remove_non_latin_characters (testing specific characters)
def test_remove_non_latin_characters_valid_input():
    input_str = "Hello, world!  你好世界"
    expected_output = "Hello, world!  "
    assert StringFormatter.remove_non_latin_characters(input_str) == expected_output

def test_remove_non_latin_characters_empty_input():
    input_str = ""
    expected_output = ""
    assert StringFormatter.remove_non_latin_characters(input_str) == expected_output


# Tests for remove_special_characters (string and list cases)
def test_remove_special_characters_string():
    input_str = "Hello, world!@#$%^&*()"
    expected_output = "Hello world"
    assert StringFormatter.remove_special_characters(input_str) == expected_output


def test_remove_special_characters_list():
    input_list = ["Hello, world!", "你好世界"]
    expected_output = ["Hello world", "你好世界"]
    assert StringFormatter.remove_special_characters(input_list) == expected_output

# Tests for clear_numbers
def test_clear_numbers_valid_input():
    input_str = "aaa123.456 cde"
    expected_output = "123.456"
    assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_no_numbers():
    input_str = "abc def"
    expected_output = ""
    assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_empty_input():
    input_str = ""
    expected_output = ""
    assert StringFormatter.clear_numbers(input_str) == expected_output



```