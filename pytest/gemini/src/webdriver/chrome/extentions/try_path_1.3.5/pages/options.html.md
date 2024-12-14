```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup

# Fixture definitions
@pytest.fixture
def html_content():
    """Provides the HTML content for testing."""
    file_path = Path(__file__).parent / "hypotez/src/webdriver/chrome/extentions/try_path_1.3.5/pages/options.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

@pytest.fixture
def parsed_html(html_content):
    """Provides a parsed BeautifulSoup object of the HTML content."""
    return BeautifulSoup(html_content, 'html.parser')


# Tests for HTML structure
def test_html_has_doctype(html_content):
    """Checks if the HTML document has a DOCTYPE declaration."""
    assert html_content.strip().startswith("<!DOCTYPE html>")

def test_html_has_head_and_body(parsed_html):
    """Checks if the HTML document has both <head> and <body> tags."""
    assert parsed_html.head is not None
    assert parsed_html.body is not None

def test_html_charset_is_utf8(parsed_html):
    """Checks if the HTML document has a UTF-8 charset declaration."""
    assert parsed_html.find('meta', {'charset': 'utf-8'}) is not None

def test_html_includes_scripts(parsed_html):
    """Checks if the HTML document includes the necessary scripts."""
    scripts = parsed_html.find_all('script')
    assert any("try_xpath_functions.js" in script.get('src', '') for script in scripts)
    assert any("options.js" in script.get('src', '') for script in scripts)

def test_html_contains_attribute_inputs(parsed_html):
    """Checks if the HTML document contains input fields for attributes."""
    input_ids = [
        "element-attribute",
        "context-attribute",
        "focused-attribute",
        "ancestor-attribute",
        "frame-attribute",
        "frame-ancestor-attribute"
    ]
    for input_id in input_ids:
      assert parsed_html.find('input', {'id': input_id}) is not None

def test_html_contains_style_textarea(parsed_html):
    """Checks if the HTML document contains a textarea for style input."""
    assert parsed_html.find('textarea', {'id': 'style'}) is not None

def test_html_contains_popup_style_inputs(parsed_html):
    """Checks if the HTML document contains input fields for popup styles."""
    assert parsed_html.find('input', {'id': 'popup-body-width'}) is not None
    assert parsed_html.find('input', {'id': 'popup-body-height'}) is not None

def test_html_contains_save_and_default_buttons(parsed_html):
    """Checks if the HTML document contains the save and default buttons."""
    assert parsed_html.find('button', {'id': 'save'}) is not None
    assert parsed_html.find('button', {'id': 'show-default'}) is not None

def test_html_contains_message_div(parsed_html):
    """Checks if the HTML document contains the message div."""
    assert parsed_html.find('div', {'id': 'message'}) is not None

def test_html_attribute_labels(parsed_html):
    """Checks if the labels for attribute fields are present."""
    labels = [
        "Resulted elements",
        "Context element",
        "Focused element",
        "Ancestors of the focused element",
        "Frame elements",
        "Ancestors of the frames"
    ]
    for label_text in labels:
        assert parsed_html.find('label', string=label_text) is not None

def test_html_style_label(parsed_html):
    """Checks if the label for the style textarea is present."""
    assert parsed_html.find('label', string="Style") is not None

def test_html_popup_labels(parsed_html):
    """Checks if the labels for popup style fields are present."""
    assert parsed_html.find('label', string="Body width(auto or px)") is not None
    assert parsed_html.find('label', string="Body height(auto or px)") is not None
```