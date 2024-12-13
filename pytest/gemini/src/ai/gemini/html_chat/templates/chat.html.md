```python
import pytest
from bs4 import BeautifulSoup

# Fixture to load the HTML content from the file
@pytest.fixture
def html_content():
    """Loads the HTML content from the specified file."""
    with open("hypotez/src/ai/gemini/html_chat/templates/chat.html", "r", encoding="utf-8") as f:
        return f.read()

def test_html_structure_contains_doctype(html_content):
    """Checks if the HTML document starts with a doctype declaration."""
    assert html_content.strip().startswith("<!DOCTYPE html>")

def test_html_has_lang_attribute(html_content):
    """Checks if the <html> tag has a 'lang' attribute with value 'en'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    html_tag = soup.find('html')
    assert html_tag is not None
    assert html_tag.get('lang') == 'en'

def test_html_has_title(html_content):
    """Checks if the <head> tag contains a <title> tag with specific content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    assert title_tag is not None
    assert title_tag.text == 'Kazarinov Chat'

def test_html_includes_bootstrap_css(html_content):
    """Checks if the <head> tag includes Bootstrap CSS link."""
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tags = soup.find_all('link')
    bootstrap_css_found = any(
        "bootstrap" in link.get('href', '') and "min.css" in link.get('href', '')
        for link in link_tags
    )
    assert bootstrap_css_found

def test_html_includes_jquery(html_content):
    """Checks if the <head> tag includes jQuery script."""
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tags = soup.find_all('script')
    jquery_found = any("jquery-3.5.1.min.js" in script.get('src', '') for script in script_tags)
    assert jquery_found

def test_html_includes_custom_css(html_content):
    """Checks if the <head> tag includes custom CSS link."""
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tags = soup.find_all('link')
    custom_css_found = any(
        link.get('href', '') == '{{ url_for(\'static\', path=\'css/styles.css\') }}'
        for link in link_tags
    )
    assert custom_css_found

def test_html_contains_chat_box(html_content):
    """Checks if the HTML body contains a div with class 'chat-box'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    chat_box = soup.find('div', class_='chat-box')
    assert chat_box is not None

def test_chat_box_has_scrollable_content(html_content):
    """Checks if the chat box div has overflow-y style set to 'scroll'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    chat_box = soup.find('div', class_='chat-box')
    assert chat_box is not None
    assert "overflow-y: scroll;" in chat_box.get('style', '')

def test_html_contains_chat_log_div(html_content):
    """Checks if the chat box contains a div with id 'chat-log'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    chat_log = soup.find('div', id='chat-log')
    assert chat_log is not None

def test_html_contains_chat_form(html_content):
    """Checks if the HTML body contains a form with id 'chat-form'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    chat_form = soup.find('form', id='chat-form')
    assert chat_form is not None

def test_chat_form_contains_input(html_content):
    """Checks if the chat form contains an input element with id 'user-input'."""
    soup = BeautifulSoup(html_content, 'html.parser')
    input_element = soup.find('input', id='user-input')
    assert input_element is not None
    assert input_element.get('type') == 'text'

def test_chat_form_contains_submit_button(html_content):
    """Checks if the chat form contains a submit button."""
    soup = BeautifulSoup(html_content, 'html.parser')
    submit_button = soup.find('button', type='submit')
    assert submit_button is not None

def test_javascript_code_exists(html_content):
    """Checks if the HTML document contains a <script> tag with Javascript code"""
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tags = soup.find_all('script')
    assert len(script_tags) > 1
    script_content = script_tags[-1].text
    assert "$(document).ready(function() {" in script_content
    assert "$('#chat-form').submit(function(event) {" in script_content
    assert "$.ajax({" in script_content
    assert "$('#chat-log').append('<p><strong>AI:</strong> ' + response.response + '</p>');" in script_content
    assert "$('#user-input').val('');" in script_content
    
def test_js_code_contains_ajax_call(html_content):
    """Verifies if the Javascript code includes an AJAX call to /ask"""
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tags = soup.find_all('script')
    assert len(script_tags) > 1
    script_content = script_tags[-1].text
    assert "url: '/ask'," in script_content

def test_js_code_sends_user_input_data(html_content):
    """Verifies if the Javascript code sends 'user_input' data in AJAX call."""
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tags = soup.find_all('script')
    assert len(script_tags) > 1
    script_content = script_tags[-1].text
    assert "data: { user_input: userInput }," in script_content
```