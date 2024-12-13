```python
import pytest
from unittest.mock import patch
import os


# Fixture definitions, if needed
@pytest.fixture
def mock_chrome_storage():
    """Mocks chrome.storage for testing."""
    class MockStorage:
        def __init__(self):
            self.data = {}

        def get(self, keys, callback):
           callback(self.data.get(keys, {}))
        
        def set(self, items, callback = None):
            self.data.update(items)
            if callback:
                callback()
    
    with patch('chrome.storage.local', MockStorage()):
        yield MockStorage

# Test for the html structure 
def test_popup_html_structure():
    """Verify the basic structure of the popup.html file."""
    
    file_path = 'hypotez/src/webdriver/chrome/extentions/catch_page/popup.html'
    assert os.path.exists(file_path)

    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    assert "<!DOCTYPE html>" in content
    assert "<html" in content
    assert "<head>" in content
    assert "<title>URL Sender</title>" in content
    assert '<script src="popup.js"></script>' in content
    assert "<body>" in content
    assert '<button id="sendUrlButton">Send URL</button>' in content
    assert "</body>" in content
    assert "</html>" in content

def test_popup_html_contains_send_url_button():
    """Verify the popup.html contains send url button."""
    file_path = 'hypotez/src/webdriver/chrome/extentions/catch_page/popup.html'
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    assert '<button id="sendUrlButton">Send URL</button>' in content
    
def test_popup_html_references_popup_js():
    """Verify the popup.html references popup.js."""
    file_path = 'hypotez/src/webdriver/chrome/extentions/catch_page/popup.html'
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    assert '<script src="popup.js"></script>' in content
    
def test_popup_html_has_title():
    """Verify the popup.html has a title."""
    file_path = 'hypotez/src/webdriver/chrome/extentions/catch_page/popup.html'
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()

    assert "<title>URL Sender</title>" in content
```