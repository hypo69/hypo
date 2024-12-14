```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup

# Fixture to load the HTML file content
@pytest.fixture
def html_content():
    """Provides the HTML content for testing."""
    file_path = Path(__file__).parent / "popup.html"  # Assuming the test file is in the same directory as popup.html
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def test_html_structure(html_content):
    """
    Checks the basic structure of the HTML content.
    Ensures that the document is valid HTML, contains a head and body,
    and checks that the title is present with expected value.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    assert soup.html is not None, "The HTML document should have an <html> tag"
    assert soup.head is not None, "The HTML document should have a <head> tag"
    assert soup.body is not None, "The HTML document should have a <body> tag"
    
    title_tag = soup.find('title')
    assert title_tag is not None, "The HTML document should have a <title> tag"
    assert title_tag.string == 'Hypotez', "The <title> should be 'Hypotez'"


def test_html_h1_exists(html_content):
    """
    Tests if the <h1> tag with the heading is present in the HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    h1_tag = soup.find('h1')
    assert h1_tag is not None, "The HTML document should have an <h1> tag"
    assert h1_tag.string == 'Hypotez', "The <h1> tag should have content 'Hypotez'"


def test_html_paragraph_exists(html_content):
    """
    Tests if the <p> tag with a specific text is present in the HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    p_tag = soup.find('p')
    assert p_tag is not None, "The HTML document should have a <p> tag"
    assert p_tag.string == 'Привет, Это Давидка. Я обучаю модель', "The <p> tag should have a specific content"

def test_html_charset_meta(html_content):
    """
    Test if the meta tag defining the charset is present and has the correct value.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    meta_charset = soup.find('meta', {'charset': True})
    assert meta_charset is not None, "The HTML document should have a meta tag defining charset"
    assert meta_charset['charset'] == 'UTF-8', "The meta charset should be 'UTF-8'"
    
def test_html_viewport_meta(html_content):
    """
    Test if the viewport meta tag exists and has the correct content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    meta_viewport = soup.find('meta', {'name': 'viewport'})
    assert meta_viewport is not None, "The HTML document should have a meta tag defining viewport"
    expected_content = "width=device-width, initial-scale=1.0"
    assert meta_viewport['content'] == expected_content, f"The meta viewport content should be '{expected_content}'"

def test_html_lang_attribute(html_content):
    """
    Test if the <html> tag has the correct language attribute.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    html_tag = soup.find('html')
    assert html_tag is not None, "The HTML document should have an <html> tag"
    assert html_tag['lang'] == 'en', "The <html> tag should have lang attribute equal to 'en'"

def test_html_contains_doctype(html_content):
  """
  Checks if the HTML content starts with the DOCTYPE declaration.
  """
  assert html_content.strip().startswith('<!DOCTYPE html>'), "The HTML should start with a DOCTYPE declaration"
```