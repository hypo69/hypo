```python
import pytest
import re
from markdown2 import markdown
from hypotez.src.utils.convertors.md2dict import md2dict, extract_json_from_string
from unittest.mock import patch

# Fixtures
@pytest.fixture
def valid_markdown():
    return """# Heading 1
This is the content of the first heading.

## Heading 2
This is the content of the second heading.
"""

@pytest.fixture
def markdown_with_json():
    return """# Heading 1
This is the content of the first heading.
```json
{"key": "value"}
```
"""

@pytest.fixture
def invalid_markdown():
    return """# Heading 1
This is the content of the first heading.
```invalid_json
"""

@pytest.fixture
def empty_markdown():
    return ""

# Tests for md2dict function
def test_md2dict_valid_input(valid_markdown):
    """Tests md2dict with valid Markdown."""
    result = md2dict(valid_markdown)
    expected = {
        "Heading 1": [
            "This is the content of the first heading."
        ],
        "Heading 2": [
            "This is the content of the second heading."
        ]
    }
    assert result == expected

def test_md2dict_markdown_with_json(markdown_with_json):
    """Tests md2dict with Markdown containing JSON."""
    result = md2dict(markdown_with_json)
    expected = {"json": {"key": "value"}}
    assert result == expected

def test_md2dict_invalid_markdown(invalid_markdown):
    """Tests md2dict with invalid Markdown (no JSON)."""
    result = md2dict(invalid_markdown)
    assert result == {}

def test_md2dict_empty_markdown(empty_markdown):
    """Tests md2dict with empty Markdown."""
    result = md2dict(empty_markdown)
    assert result == {}

def test_md2dict_exception_handling(invalid_markdown):
    """Tests exception handling in md2dict."""
    #This needs to be mocked so that the logger.error isn't actually called
    with patch('hypotez.src.logger.logger.error') as mock_error:
      md2dict(invalid_markdown)
      mock_error.assert_called()


def test_extract_json_from_string_valid_json():
    """Tests extract_json_from_string with valid JSON."""
    json_string = '```json\n{"key": "value"}\n```'
    result = extract_json_from_string(json_string)
    expected = {"key": "value"}
    assert result == expected

def test_extract_json_from_string_no_json():
    """Tests extract_json_from_string with no JSON."""
    text = "This is some text with no JSON."
    result = extract_json_from_string(text)
    assert result is None

def test_extract_json_from_string_invalid_json():
    """Tests extract_json_from_string with invalid JSON."""
    invalid_json = '```json\n{"key': "value"}\n```'
    result = extract_json_from_string(invalid_json)
    assert result is None

def test_extract_json_from_string_exception_handling():
    """Tests exception handling in extract_json_from_string"""
    with patch('hypotez.src.logger.logger.error') as mock_error:
        extract_json_from_string("some invalid json")
        mock_error.assert_called()
```

**Explanation and Improvements:**

* **Clearer Test Names:** Test names now explicitly describe the input and expected outcome.
* **Comprehensive Coverage:** Added tests for valid and invalid Markdown, empty input, and cases with JSON.
* **Edge Case Testing:** Included an empty Markdown string and invalid JSON as tests.
* **Exception Handling:** Added a test (`test_md2dict_exception_handling`) to ensure that `md2dict` catches and logs exceptions appropriately. Similar tests for `extract_json_from_string` were added.
* **Mocking `logger`:** The `logger` is patched in `test_md2dict_exception_handling` and `test_extract_json_from_string_exception_handling` to prevent actual logging calls, making the tests more isolated.
* **Fixtures for Data:** Used fixtures (`valid_markdown`, `markdown_with_json`, etc.) to improve code organization and readability.
* **Explicit Assertions:**  All tests now use `assert` to check for equality against expected outputs.
* **`pytest.raises` is NOT needed:** Exception handling is now properly tested using patching (mocking).

This revised test suite provides more thorough and robust coverage of the `md2dict` and `extract_json_from_string` functions, addressing the requirements of the prompt.  Remember to install `pytest` and `markdown2` if you haven't already.  Also, ensure the `src.logger` module is correctly imported/configured in your test environment for the mocking to work. Remember to replace `"hypotez.src.logger"` with the correct path if your logger is not in the `hypotez.src` directory.


```bash
pip install pytest markdown2
```