```python
import pytest
import re
from markdown2 import markdown
from hypotez.src.utils.convertors.md2dict import md2dict, extract_json_from_string
from typing import Dict

# Fixture definitions
def valid_md_string():
    return """# Header 1
This is the content of the first header.

## Header 2
Some text here.

### Header 3
More text.

```json
{"key": "value"}
```
"""


def invalid_md_string():
    return "This is not valid markdown."


def md_string_with_json():
    return """# Header 1
This is the content of the first header.
```json
{"name": "John Doe"}
```
"""

def md_string_no_json():
    return """# Header 1
This is the content of the first header.

## Header 2
Some text here.
"""


def test_md2dict_valid_input(valid_md_string):
    """Checks correct behavior with valid markdown containing a JSON object."""
    expected_output = {"json": {"key": "value"}}
    actual_output = md2dict(valid_md_string)
    assert actual_output == expected_output


def test_md2dict_invalid_input(invalid_md_string):
    """Checks correct handling of invalid markdown."""
    actual_output = md2dict(invalid_md_string)
    assert actual_output == {}


def test_md2dict_json_extraction(md_string_with_json):
    """Checks json extraction from valid markdown."""
    expected_output = {"json": {"name": "John Doe"}}
    actual_output = md2dict(md_string_with_json)
    assert actual_output == expected_output

def test_md2dict_no_json(md_string_no_json):
    """Checks behavior with valid markdown without JSON."""
    expected_output = {"Header 1": ["This is the content of the first header.", ""], "Header 2": ["Some text here."]}
    actual_output = md2dict(md_string_no_json)
    assert actual_output == expected_output


def test_extract_json_from_string_valid_json():
    """Checks correct JSON extraction from a string."""
    input_string = "```json\n{\"name\": \"John Doe\"}\n```"
    expected_output = {"name": "John Doe"}
    actual_output = extract_json_from_string(input_string)
    assert actual_output == expected_output


def test_extract_json_from_string_no_json():
    """Checks handling when no JSON is present."""
    input_string = "This is some text."
    expected_output = None
    actual_output = extract_json_from_string(input_string)
    assert actual_output is None



def test_extract_json_from_string_invalid_json():
    """Checks handling of invalid JSON format."""
    input_string = "```json\n{\"name\": \"John Doe\"}\n```"
    with pytest.raises(Exception) as e:
        extract_json_from_string(input_string)  # Expecting eval() to raise an exception
    assert 'invalid syntax' in str(e.value)


def test_md2dict_empty_string():
    """Checks behavior with an empty string."""
    actual_output = md2dict("")
    assert actual_output == {}

def test_md2dict_only_header():
  """Checks behavior with a markdown string containing only a header."""
  input_string = "# Header 1"
  expected_output = {"Header 1": []}
  actual_output = md2dict(input_string)
  assert actual_output == expected_output

```