```python
import pytest
from pathlib import Path

# Define the path to the HTML file for testing
HTML_FILE_PATH = Path("hypotez/src/webdriver/firefox/extentions/test_extention/html/popup.html")

# Fixture to read the content of the HTML file
@pytest.fixture
def html_content():
    """Reads and returns the content of the HTML file for testing."""
    if not HTML_FILE_PATH.exists():
        raise FileNotFoundError(f"HTML file not found at: {HTML_FILE_PATH}")
    
    with open(HTML_FILE_PATH, 'r', encoding='utf-8') as file:
        return file.read()

def test_html_file_exists():
    """Checks if the HTML file exists."""
    assert HTML_FILE_PATH.exists(), f"HTML file does not exist at {HTML_FILE_PATH}"

def test_html_contains_title(html_content):
    """Checks if the HTML contains the <title> tag with the correct content."""
    assert "<title>Hypotez</title>" in html_content, "The HTML does not contain the correct <title> tag."

def test_html_contains_h1(html_content):
    """Checks if the HTML contains the <h1> tag with the correct content."""
    assert "<h1>Hypotez</h1>" in html_content, "The HTML does not contain the correct <h1> tag."

def test_html_contains_p_tag(html_content):
    """Checks if the HTML contains the <p> tag with the correct content."""
    assert "<p>Привет, Это Давидка. Я обучаю модель</p>" in html_content, "The HTML does not contain the correct <p> tag."

def test_html_contains_doctype_declaration(html_content):
    """Checks if the HTML starts with the correct DOCTYPE declaration."""
    assert "<!DOCTYPE html>" in html_content, "The HTML does not have the correct DOCTYPE declaration."

def test_html_contains_html_tag(html_content):
    """Checks if the HTML contains the <html> tag with language attribute set to "en"."""
    assert '<html lang="en">' in html_content, "The HTML does not have the correct <html> tag with lang attribute set to 'en'."

def test_html_contains_head_tag(html_content):
    """Checks if the HTML contains the <head> tag."""
    assert "<head>" in html_content, "The HTML does not contain the <head> tag."
    assert "</head>" in html_content, "The HTML does not contain the closing </head> tag."

def test_html_contains_body_tag(html_content):
    """Checks if the HTML contains the <body> tag."""
    assert "<body>" in html_content, "The HTML does not contain the <body> tag."
    assert "</body>" in html_content, "The HTML does not contain the closing </body> tag."
    
def test_html_has_utf8_charset(html_content):
    """Checks if the HTML meta tag specifies the UTF-8 charset."""
    assert '<meta charset="UTF-8">' in html_content, "The HTML does not have the correct meta charset tag."
    
def test_html_has_viewport_meta_tag(html_content):
     """Checks if the HTML contains viewport meta tag."""
     assert '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in html_content, "The HTML does not have the correct viewport meta tag."
     
def test_html_has_no_script_tag(html_content):
     """Check if HTML contains script tags, it should not have any."""
     assert "<script>" not in html_content, "The HTML has the script tag, it should not be present in html file."

def test_html_is_not_empty(html_content):
    """Checks if the HTML content is not empty."""
    assert html_content.strip(), "The HTML file is empty or contains only whitespace."

def test_html_is_valid(html_content):
    """
    A basic check to see if the html content is not completely broken.
    Note: this test does not fully validate the html content structure.
    """
    assert "<html" in html_content, "Invalid HTML: does not contain html tag"
    assert "<head" in html_content, "Invalid HTML: does not contain head tag"
    assert "<body" in html_content, "Invalid HTML: does not contain body tag"
    assert "</html" in html_content, "Invalid HTML: does not contain closing html tag"
    assert "</head" in html_content, "Invalid HTML: does not contain closing head tag"
    assert "</body" in html_content, "Invalid HTML: does not contain closing body tag"
```