```python
import pytest
import re
from hypotez.src.utils.string.formatter import StringFormatter

# Test cases for StringFormatter class methods


def test_remove_line_breaks_valid_input():
    input_str = "Line 1\nLine 2\rLine 3"
    expected_output = "Line 1 Line 2 Line 3"
    actual_output = StringFormatter.remove_line_breaks(input_str)
    assert actual_output == expected_output

def test_remove_line_breaks_empty_input():
    input_str = ""
    expected_output = ""
    actual_output = StringFormatter.remove_line_breaks(input_str)
    assert actual_output == expected_output


def test_remove_htmls_valid_input():
    input_html = "<p>This is a paragraph.</p> <span>with a span.</span>"
    expected_output = "This is a paragraph. with a span."
    actual_output = StringFormatter.remove_htmls(input_html)
    assert actual_output == expected_output


def test_remove_htmls_no_tags():
    input_html = "This is a text without tags."
    expected_output = "This is a text without tags."
    actual_output = StringFormatter.remove_htmls(input_html)
    assert actual_output == expected_output


def test_escape_html_tags_valid_input():
    input_html = "<p>&lt;hello&gt;</p>"
    expected_output = "&lt;p&gt;&amp;lt;hello&amp;gt;&amp;lt;/p&gt;"
    actual_output = StringFormatter.escape_html_tags(input_html)
    assert actual_output == expected_output


def test_escape_html_tags_no_tags():
    input_html = "This is a text without tags."
    expected_output = "This is a text without tags."
    actual_output = StringFormatter.escape_html_tags(input_html)
    assert actual_output == expected_output


def test_escape_to_html_valid_input():
    input_text = "This string has & and <"
    expected_output = "This string has &amp; and &lt;"
    actual_output = StringFormatter.escape_to_html(input_text)
    assert actual_output == expected_output


def test_remove_non_latin_characters_valid_input():
    input_str = "Hello, world! 123 €"
    expected_output = "Hello, world! 123"
    actual_output = StringFormatter.remove_non_latin_characters(input_str)
    assert actual_output == expected_output


def test_remove_non_latin_characters_empty_input():
    input_str = ""
    expected_output = ""
    actual_output = StringFormatter.remove_non_latin_characters(input_str)
    assert actual_output == expected_output


def test_remove_special_characters_valid_input():
    input_str = "Hello, world! 123 €"
    expected_output = "Hello world 123"
    actual_output = StringFormatter.remove_special_characters(input_str)
    assert actual_output == expected_output


def test_remove_special_characters_list_input():
    input_list = ["Hello, world!", "123 €"]
    expected_output = ["Hello world", "123"]
    actual_output = StringFormatter.remove_special_characters(input_list)
    assert actual_output == expected_output

def test_clear_numbers_valid_input():
    input_str = "aaa123.456 cde"
    expected_output = "123.456"
    actual_output = StringFormatter.clear_numbers(input_str)
    assert actual_output == expected_output

def test_clear_numbers_no_numbers():
    input_str = "abc def"
    expected_output = ""
    actual_output = StringFormatter.clear_numbers(input_str)
    assert actual_output == expected_output
```