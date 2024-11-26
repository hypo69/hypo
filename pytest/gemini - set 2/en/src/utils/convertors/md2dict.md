```python
import pytest
import re
from markdown2 import markdown
from hypotez.src.utils.convertors.md2dict import md2dict, extract_json_from_string
from hypotez.src.logger import logger


# Mock logger for testing
logger.error = lambda msg, exc_info=None: print(f"Error: {msg}")


def test_md2dict_valid_input():
    """Checks correct behavior with valid Markdown input."""
    md_string = "# Title\nThis is the content.\n## Subheading\nMore content."
    expected_output = {
        "Title": ["This is the content."],
        "Subheading": ["More content."],
    }
    actual_output = md2dict(md_string)
    assert actual_output == expected_output


def test_md2dict_nested_headings():
    md_string = "# Title\nThis is the content.\n## Subheading 1\nMore content.\n### Sub-subheading\nEven more content."
    expected_output = {
        "Title": ["This is the content."],
        "Subheading 1": ["More content.", "Even more content."],
    }
    actual_output = md2dict(md_string)
    assert actual_output == expected_output

def test_md2dict_json_in_markdown():
    """Test case for extracting JSON from Markdown."""
    md_string = "# Title\nThis is the content.\n```json\n{\n \"key\": \"value\"\n}\n```"
    expected_output = {"json": {"key": "value"}}
    actual_output = md2dict(md_string)
    assert actual_output == expected_output


def test_md2dict_invalid_json():
    """Tests the handling of invalid JSON within the Markdown."""
    md_string = "# Title\n```json\n{\n \"key\": \"value\"\n```"
    expected_output = {}  # Should return an empty dict in case of invalid JSON.
    actual_output = md2dict(md_string)
    assert actual_output == expected_output


def test_extract_json_from_string_valid_json():
    """Tests the extraction of valid JSON from a string."""
    text = "{ \"name\": \"John Doe\" }"
    expected_output = {"name": "John Doe"}
    actual_output = extract_json_from_string(text)
    assert actual_output == expected_output


def test_extract_json_from_string_no_json():
    """Tests the handling of a string without JSON."""
    text = "This is not JSON."
    actual_output = extract_json_from_string(text)
    assert actual_output is None


def test_extract_json_from_string_invalid_json():
    """Tests the handling of invalid JSON in a string."""
    text = "{ \"name\": \"John Doe"
    actual_output = extract_json_from_string(text)
    assert actual_output is None


def test_md2dict_empty_string():
    """Tests the handling of an empty input string."""
    md_string = ""
    expected_output = {}
    actual_output = md2dict(md_string)
    assert actual_output == expected_output

def test_md2dict_error_handling():
    """Tests error handling during markdown conversion."""
    md_string = "This is invalid Markdown!"  # Example invalid markdown
    expected_output = {}
    actual_output = md2dict(md_string)
    assert actual_output == expected_output


def test_md2dict_malformed_json():
  """Test case for extracting malformed JSON."""
  md_string = "# Title\n```json\n{ \n```"
  expected_output = {}
  actual_output = md2dict(md_string)
  assert actual_output == expected_output

# Add more test cases as needed (e.g., for different heading levels, more complex Markdown, edge cases)
```