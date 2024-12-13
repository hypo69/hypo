```python
import pytest
from src.utils.convertors.md2dict import md2dict, extract_json_from_string
import json

# Fixture definitions, if needed
@pytest.fixture
def sample_md_string_with_json():
    """Provides a sample Markdown string with embedded JSON."""
    return """
    # Section 1
    {
      "key": "value",
      "items": [1, 2, 3]
    }
    Some text in section 1.
    ## Subsection 1.1
    More text.
    """

@pytest.fixture
def sample_md_string_no_json():
    """Provides a sample Markdown string without JSON."""
    return """
    # Section 1
    Some text in section 1.
    ## Subsection 1.1
    More text.
    # Section 2
    Another text.
    """
@pytest.fixture
def sample_md_string_with_empty_lines():
    """Provides a sample Markdown string with empty lines."""
    return """
    # Section 1
    
    Some text in section 1.
    
    ## Subsection 1.1
    
    More text.
    """

@pytest.fixture
def sample_md_string_with_html():
    """Provides a sample Markdown string with HTML tags."""
    return """
    # Section 1
    <p>Some text with HTML.</p>
    ## Subsection 1.1
    <a href="#">Link</a>
    """

@pytest.fixture
def sample_md_string_with_invalid_json():
        """Provides a sample Markdown string with invalid json"""
        return """
            # Section 1
            {"key": "value"
            Some text
        """

# Tests for md2dict function
def test_md2dict_valid_input_with_json(sample_md_string_with_json):
    """Checks correct behavior when Markdown contains JSON."""
    expected_json = {
        "json": {
            "key": "value",
            "items": [1, 2, 3]
        }
    }
    assert md2dict(sample_md_string_with_json) == expected_json

def test_md2dict_valid_input_no_json(sample_md_string_no_json):
    """Checks correct behavior when Markdown does not contain JSON."""
    expected_output = {
        "Section 1": ["Some text in section 1.", "Subsection 1.1", "More text."],
        "Section 2": ["Another text."]
    }
    assert md2dict(sample_md_string_no_json) == expected_output

def test_md2dict_empty_input():
    """Checks behavior with empty input."""
    assert md2dict("") == {}

def test_md2dict_input_with_empty_lines(sample_md_string_with_empty_lines):
     """Checks correct behavior with empty lines in input."""
     expected_output = {
        "Section 1": ["Some text in section 1.", "Subsection 1.1", "More text."],
    }
     assert md2dict(sample_md_string_with_empty_lines) == expected_output

def test_md2dict_input_with_html(sample_md_string_with_html):
    """Checks correct handling of HTML tags in input"""
    expected_output = {
        "Section 1": ["Some text with HTML.", "Subsection 1.1", "Link"]
    }
    assert md2dict(sample_md_string_with_html) == expected_output


def test_md2dict_invalid_input(sample_md_string_with_invalid_json):
    """Checks behavior with an invalid input that causes exceptions"""
    assert md2dict(sample_md_string_with_invalid_json) == {}

# Tests for extract_json_from_string function
def test_extract_json_from_string_valid():
    """Checks correct extraction of JSON from a string."""
    text = 'Some text {"key": "value"} more text'
    expected_output = {"key": "value"}
    assert extract_json_from_string(text) == expected_output


def test_extract_json_from_string_no_json():
    """Checks behavior when no JSON is present."""
    text = "Some text without JSON"
    assert extract_json_from_string(text) is None

def test_extract_json_from_string_invalid_json():
    """Checks behavior with invalid JSON input."""
    text = 'Some text {"key": "value" invalid json}'
    assert extract_json_from_string(text) is None

def test_extract_json_from_string_empty_input():
    """Checks behavior with empty input."""
    assert extract_json_from_string("") is None

def test_extract_json_from_string_with_nested_json():
     """Checks correct extraction of nested JSON from a string."""
     text = 'Some text {"key": {"nested_key": "nested_value"}} more text'
     expected_output = {"key": {"nested_key": "nested_value"}}
     assert extract_json_from_string(text) == expected_output
```