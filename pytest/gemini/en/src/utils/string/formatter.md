```python
import pytest
import re
from hypotez.src.utils.string.formatter import StringFormatter

def test_remove_line_breaks_valid_input():
    """Tests remove_line_breaks with valid input."""
    input_str = "This is a string\nwith line breaks.\rAnd more."
    expected_output = "This is a string with line breaks. And more."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_empty_input():
    """Tests remove_line_breaks with empty input."""
    input_str = ""
    expected_output = ""
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_single_line_input():
    """Tests remove_line_breaks with a single line input."""
    input_str = "This is a single line."
    expected_output = "This is a single line."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_htmls_valid_input():
    """Tests remove_htmls with valid HTML input."""
    input_html = "<p>This is a paragraph.</p> <span>with tags.</span>"
    expected_output = "This is a paragraph. with tags."
    assert StringFormatter.remove_htmls(input_html) == expected_output
    
def test_remove_htmls_empty_input():
    """Tests remove_htmls with empty input."""
    input_html = ""
    expected_output = ""
    assert StringFormatter.remove_htmls(input_html) == expected_output
    
def test_remove_htmls_no_tags():
    """Tests remove_htmls with no tags."""
    input_html = "This is plain text."
    expected_output = "This is plain text."
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_escape_html_tags_valid_input():
    """Tests escape_html_tags with valid input."""
    input_html = "<p>This & <p>"
    expected_output = "&lt;p&gt;This & &lt;p&gt;"
    assert StringFormatter.escape_html_tags(input_html) == expected_output

def test_escape_html_tags_empty_input():
    """Tests escape_html_tags with empty input."""
    input_html = ""
    expected_output = ""
    assert StringFormatter.escape_html_tags(input_html) == expected_output

def test_escape_to_html_valid_input():
    """Tests escape_to_html with valid input."""
    text = "<>&\"'"
    expected_output = "&lt;&gt;&amp;&quot;&apos;"
    assert StringFormatter.escape_to_html(text) == expected_output

def test_remove_non_latin_characters_valid_input():
    """Tests remove_non_latin_characters with valid input."""
    input_str = "Hello, world!  你好世界"
    expected_output = "Hello, world!  "
    assert StringFormatter.remove_non_latin_characters(input_str) == expected_output


def test_remove_special_characters_valid_input_string():
  input_str = "Hello!@#$%^&*()_+=-`~[]\\{}|;':\",./<>?"
  expected_output = "Hello"
  assert StringFormatter.remove_special_characters(input_str) == expected_output

def test_remove_special_characters_valid_input_list():
  input_list = ["Hello!", "World?", "123."]
  expected_output = ["Hello", "World", "123"]
  assert StringFormatter.remove_special_characters(input_list) == expected_output

def test_clear_numbers_valid_input():
    """Tests clear_numbers with a valid input string."""
    input_str = "aaa123.456 cde"
    expected_output = "123.456"
    assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_empty_input():
    """Tests clear_numbers with an empty input string."""
    input_str = ""
    expected_output = ""
    assert StringFormatter.clear_numbers(input_str) == expected_output


```