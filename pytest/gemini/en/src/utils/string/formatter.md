```python
import pytest
import re
from hypotez.src.utils.string.formatter import StringFormatter

def test_remove_line_breaks_valid_input():
    """Checks correct behavior with valid input (newline characters)."""
    input_str = "This is a string\nwith multiple\nlines."
    expected_output = "This is a string with multiple lines."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_empty_input():
    """Checks behavior with empty input."""
    input_str = ""
    expected_output = ""
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_line_breaks_single_line_input():
    """Checks behavior with a single-line input."""
    input_str = "This is a single line."
    expected_output = "This is a single line."
    assert StringFormatter.remove_line_breaks(input_str) == expected_output

def test_remove_htmls_valid_input():
    """Checks correct behavior with valid input (HTML tags)."""
    input_html = "<p>This is a paragraph.</p> <span>with some tags</span>"
    expected_output = "This is a paragraph. with some tags"
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_remove_htmls_empty_input():
    """Checks behavior with empty input."""
    input_html = ""
    expected_output = ""
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_remove_htmls_no_tags_input():
    """Checks behavior with input containing no HTML tags."""
    input_html = "This is plain text."
    expected_output = "This is plain text."
    assert StringFormatter.remove_htmls(input_html) == expected_output

def test_escape_html_tags_valid_input():
    """Checks correct behavior with valid HTML input."""
    input_html = "<p>This is &lt;strong&gt;important&lt;/strong&gt;.</p>"
    expected_output = "&lt;p&gt;This is &amp;lt;strong&amp;gt;important&amp;lt;/strong&amp;gt;.&lt;/p&gt;"
    assert StringFormatter.escape_html_tags(input_html) == expected_output

def test_escape_html_tags_no_tags_input():
    """Checks behavior with no HTML tags in the input."""
    input_html = "This is plain text."
    expected_output = "This is plain text."
    assert StringFormatter.escape_html_tags(input_html) == expected_output

def test_escape_to_html_valid_input():
    """Checks correct behavior with valid input."""
    text = "<>&'\"\\n"
    expected_output = "&lt;&gt;&amp;&apos;&quot;\\\\n"
    assert StringFormatter.escape_to_html(text) == expected_output

def test_remove_non_latin_characters_valid_input():
    """Checks correct behavior with valid input containing non-Latin characters."""
    input_str = "Hello, world! こんにちは"
    expected_output = "Hello, world! "
    assert StringFormatter.remove_non_latin_characters(input_str) == expected_output

def test_remove_non_latin_characters_no_non_latin_input():
    """Checks behavior with input containing no non-Latin characters."""
    input_str = "This is all Latin characters."
    expected_output = "This is all Latin characters."
    assert StringFormatter.remove_non_latin_characters(input_str) == expected_output


def test_remove_special_characters_string_input():
    """Checks behavior with a string input."""
    input_str = "Hello!@#$%^&*()"
    expected_output = "Hello"
    assert StringFormatter.remove_special_characters(input_str) == expected_output

def test_remove_special_characters_list_input():
    """Checks behavior with a list input."""
    input_str = ["Hello!@#$%^&*", "World!@#$%^&*"]
    expected_output = ["Hello", "World"]
    assert StringFormatter.remove_special_characters(input_str) == expected_output

def test_clear_numbers_valid_input():
  input_str = "aaa123.456 cde"
  expected_output = "123.456"
  assert StringFormatter.clear_numbers(input_str) == expected_output

def test_clear_numbers_no_numbers_input():
  input_str = "abc def"
  expected_output = ""
  assert StringFormatter.clear_numbers(input_str) == expected_output

```