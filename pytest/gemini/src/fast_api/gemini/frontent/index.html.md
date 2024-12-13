```python
import pytest
from bs4 import BeautifulSoup

# Fixture to load the HTML content
@pytest.fixture
def html_content():
    """Provides the HTML content for testing."""
    with open('hypotez/src/fast_api/gemini/frontent/index.html', 'r', encoding='utf-8') as f:
        return f.read()

def test_html_contains_doctype(html_content):
    """Checks if the HTML document starts with a DOCTYPE declaration."""
    soup = BeautifulSoup(html_content, 'html.parser')
    assert soup.doctype is not None, "The document does not have a DOCTYPE declaration."

def test_html_language_is_english(html_content):
    """Checks if the HTML document has the language attribute set to English."""
    soup = BeautifulSoup(html_content, 'html.parser')
    html_tag = soup.find('html')
    assert html_tag, "HTML tag not found"
    assert html_tag.get('lang') == 'en', "HTML language is not set to 'en'"

def test_html_title_is_present(html_content):
    """Checks if the title tag is present and contains the expected text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    assert title_tag is not None, "Title tag not found."
    assert title_tag.text == "Chat with Generative AI", "Title text does not match expected text."

def test_html_includes_viewport_meta(html_content):
    """Checks if the meta tag for viewport settings is included."""
    soup = BeautifulSoup(html_content, 'html.parser')
    meta_tag = soup.find('meta', {'name': 'viewport'})
    assert meta_tag is not None, "Meta tag for viewport settings not found."
    assert meta_tag.get('content') == "width=device-width, initial-scale=1.0", "Viewport content does not match expected content."


def test_html_includes_bootstrap_css(html_content):
    """Checks if the link to bootstrap CSS file is included."""
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tag = soup.find('link', {'rel': 'stylesheet', 'href': '/static/bootstrap.min.css'})
    assert link_tag is not None, "Link to Bootstrap CSS not found."

def test_html_includes_app_js_script(html_content):
        """Checks if the script tag for app.js is included and has type text/babel."""
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tag = soup.find('script', {'src': '/static/app.js','type':'text/babel'})
        assert script_tag is not None, "Script tag for app.js not found."
        assert script_tag.get('type') == 'text/babel', "Script tag for app.js has incorrect type."


def test_html_contains_chat_app_div(html_content):
    """Checks if the chat app div is included."""
    soup = BeautifulSoup(html_content, 'html.parser')
    chat_app_div = soup.find('div', {'id': 'chat-app'})
    assert chat_app_div is not None, "Div with id 'chat-app' not found."


def test_html_h1_tag_is_present(html_content):
    """Checks if the h1 tag is present and contains the expected text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    h1_tag = soup.find('h1')
    assert h1_tag is not None, "h1 tag not found."
    assert h1_tag.text == "AI Chat Interface", "h1 text does not match expected text."

def test_html_container_div_is_present(html_content):
    """Checks if the container div is present and has class container."""
    soup = BeautifulSoup(html_content, 'html.parser')
    container_div = soup.find('div', class_='container')
    assert container_div is not None, "Div with class 'container' not found."
    
def test_html_body_has_padding(html_content):
    """Checks if the body tag has padding defined in styles."""
    soup = BeautifulSoup(html_content, 'html.parser')
    body_tag = soup.find('body')
    assert body_tag, "body tag is not found"
    style_tag = soup.find('style')
    assert style_tag, "style tag is not found"
    assert 'padding: 2rem;' in style_tag.text, "body style doesn't contain padding 2rem"
```