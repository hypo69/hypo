```python
import pytest
import re
from markdown2 import markdown
from hypotez.src.utils.convertors.md2dict import md2dict, extract_json_from_string
from typing import Dict


def test_md2dict_valid_json():
    """Checks correct conversion of a Markdown string containing JSON."""
    md_string = """
    ```json
    {"key": "value"}
    ```
    """
    expected_output = {"json": {"key": "value"}}
    assert md2dict(md_string) == expected_output


def test_md2dict_valid_markdown():
    """Checks conversion of a valid Markdown string."""
    md_string = "# Title\nThis is a test.\n\n## Subheading\nMore text."
    expected_output = {
        "Title": ["This is a test."],
        "Subheading": ["More text."]
    }
    assert md2dict(md_string) == expected_output


def test_md2dict_markdown_with_multiple_sections():
    """Checks conversion of a Markdown string with multiple sections."""
    md_string = "# Introduction\nHello.\n\n## Section 1\nMore text.\n\n# Conclusion\nGoodbye."
    expected_output = {
        "Introduction": ["Hello."],
        "Section 1": ["More text."],
        "Conclusion": ["Goodbye."]
    }
    assert md2dict(md_string) == expected_output

def test_md2dict_empty_string():
    """Checks handling of an empty Markdown string."""
    md_string = ""
    assert md2dict(md_string) == {}


def test_md2dict_no_json_no_sections():
    """Checks handling of a Markdown string without JSON and no sections."""
    md_string = "This is a paragraph of text.  No JSON or headings."
    expected_output = {}
    assert md2dict(md_string) == expected_output



def test_md2dict_invalid_json():
    """Checks handling of a Markdown string with invalid JSON."""
    md_string = "```json\n{key: value}\n```"  # Incorrect JSON
    assert md2dict(md_string) == {}


def test_md2dict_exception_handling():
    """Checks exception handling for malformed markdown."""
    md_string = "This is invalid Markdown\n{{this is not JSON}}"

    assert md2dict(md_string) == {}


def test_extract_json_from_string_valid_json():
    """Tests extraction of valid JSON from a string."""
    text = '{"name": "John Doe", "age": 30}'
    expected_output = {"name": "John Doe", "age": 30}
    assert extract_json_from_string(text) == expected_output


def test_extract_json_from_string_no_json():
    """Tests extraction when no JSON is present."""
    text = "This is not JSON."
    assert extract_json_from_string(text) is None


def test_extract_json_from_string_malformed_json():
    """Tests extraction when the JSON is malformed."""
    text = "{This is not valid JSON"
    assert extract_json_from_string(text) is None


```