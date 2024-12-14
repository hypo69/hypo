```python
import pytest
from pathlib import Path

# Assuming the html file is in the same directory as the test file or a known location
HTML_FILE_PATH = Path(__file__).parent / "popup.html" # Replace with the actual path if needed

def read_html_file(file_path):
    """Helper function to read the HTML file content."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None  # or raise an exception, depending on requirements

# Test for valid HTML file path
def test_read_html_file_valid_path():
    """Checks if a valid HTML file path reads the file content."""
    html_content = read_html_file(HTML_FILE_PATH)
    assert html_content is not None
    assert "<!DOCTYPE html>" in html_content
    assert "<title>hypotez</title>" in html_content
    assert "<h1>hypotez</h1>" in html_content
    assert "<p>Click the extension icon to collect data from the current webpage.</p>" in html_content

# Test for invalid HTML file path
def test_read_html_file_invalid_path():
    """Checks if returns None when provided an invalid HTML file path."""
    html_content = read_html_file("non_existent_file.html")
    assert html_content is None

# Test for correct body width
def test_html_body_width():
    """Checks if body width is set to 200px"""
    html_content = read_html_file(HTML_FILE_PATH)
    assert "width: 200px;" in html_content, "Body width should be 200px"

# Test if title is hypotez
def test_html_title():
    """Checks if the title of the html is hypotez"""
    html_content = read_html_file(HTML_FILE_PATH)
    assert "<title>hypotez</title>" in html_content, "Title should be hypotez"

# Test if h1 is hypotez
def test_html_h1():
    """Checks if the h1 title of the html is hypotez"""
    html_content = read_html_file(HTML_FILE_PATH)
    assert "<h1>hypotez</h1>" in html_content, "h1 should be hypotez"


# Test for paragraph element content
def test_html_paragraph():
    """Checks if the paragraph has the correct content"""
    html_content = read_html_file(HTML_FILE_PATH)
    assert "<p>Click the extension icon to collect data from the current webpage.</p>" in html_content, "Paragraph content is not correct"
```