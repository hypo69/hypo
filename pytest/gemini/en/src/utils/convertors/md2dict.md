```python
import pytest
import re
from markdown2 import markdown
from hypotez.src.utils.convertors.md2dict import md2dict, extract_json_from_string
from typing import Dict


def test_md2dict_valid_input_json():
    """Tests the function with a valid Markdown string containing JSON."""
    markdown_string = """
    ```json
    {"key": "value"}
    ```
    Some text after JSON.
    """
    expected_output = {"json": {"key": "value"}}
    assert md2dict(markdown_string) == expected_output


def test_md2dict_valid_input_markdown():
    """Tests the function with a valid Markdown string without JSON."""
    markdown_string = """
    # Heading 1
    This is the content of the first heading.

    ## Heading 2
    This is the content of the second heading.
    """
    expected_output = {
        "# Heading 1": ["This is the content of the first heading."],
        "## Heading 2": ["This is the content of the second heading."],
    }
    assert md2dict(markdown_string) == expected_output


def test_md2dict_multiple_headings():
    """Tests the function with multiple headings of different levels."""
    markdown_string = """
    # Heading 1
    Content 1

    ## Heading 2
    Content 2

    ### Heading 3
    Content 3

    # Another Heading 1
    Content 4
    """
    expected_output = {
        "# Heading 1": ["Content 1"],
        "## Heading 2": ["Content 2"],
        "### Heading 3": ["Content 3"],
        "# Another Heading 1": ["Content 4"],
    }
    assert md2dict(markdown_string) == expected_output



def test_md2dict_empty_input():
    """Tests the function with an empty Markdown string."""
    markdown_string = ""
    assert md2dict(markdown_string) == {}

def test_md2dict_no_headings():
    """Tests the function with Markdown without any headings."""
    markdown_string = "This is some text without headings."
    assert md2dict(markdown_string) == {}

def test_md2dict_invalid_json():
    """Tests the function with a Markdown string containing invalid JSON."""
    markdown_string = """
    ```json
    {key: "value"}
    ```
    """
    result = md2dict(markdown_string)
    assert result == {}  # Or check for specific error handling


def test_md2dict_json_in_paragraph():
  """Tests the function with JSON inside a paragraph."""
  markdown_string = "Some text.  `{\"key\": \"value\"}` More text."
  expected_output = {}
  assert md2dict(markdown_string) == expected_output



def test_extract_json_from_string_valid_json():
    """Tests extract_json_from_string with valid JSON."""
    text = '{"name": "John Doe", "age": 30}'
    expected_output = {"name": "John Doe", "age": 30}
    assert extract_json_from_string(text) == expected_output

def test_extract_json_from_string_invalid_json():
    """Tests extract_json_from_string with invalid JSON."""
    text = '{"name": "John Doe',  # Missing closing bracket
    assert extract_json_from_string(text) is None


def test_extract_json_from_string_no_json():
    """Tests extract_json_from_string with no JSON."""
    text = "This is some text with no JSON."
    assert extract_json_from_string(text) is None


def test_md2dict_error_handling():
    """Tests error handling in md2dict."""
    markdown_string = "This contains an error that causes an exception."
    expected_output = {}
    assert md2dict(markdown_string) == expected_output
```