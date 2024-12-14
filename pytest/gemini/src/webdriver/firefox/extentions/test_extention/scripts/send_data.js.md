```python
import pytest
from unittest.mock import patch, Mock
import json

# Fixture definitions, if needed
@pytest.fixture
def mock_fetch():
    """Mocks the fetch function for testing."""
    with patch('builtins.fetch') as mock_fetch:
        yield mock_fetch

@pytest.fixture
def mock_document():
     """Mocks document object for testing."""
     mock_doc = Mock()
     mock_doc.title = "Test Title"
     mock_doc.body = Mock()
     mock_doc.body.innerHTML = "<p>Test Body Content</p>"
     with patch('hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data.document', new=mock_doc):
        yield mock_doc

@pytest.fixture
def mock_window():
    """Mocks window object for testing"""
    mock_win = Mock()
    mock_win.location = Mock()
    mock_win.location.href = "http://example.com/test"
    with patch('hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data.window', new = mock_win) as mock_window:
        yield mock_window



# Tests for onPageLoad function
def test_onPageLoad_successful_fetch(mock_fetch, mock_document, mock_window):
    """Checks correct behavior with a successful fetch request."""
    mock_response = Mock()
    mock_response.ok = True
    mock_response.json.return_value = {"status": "success"}
    mock_fetch.return_value = Promise(resolve=mock_response)
    
    
    from hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data import onPageLoad
    onPageLoad()
    
    mock_fetch.assert_called_once()
    args, kwargs = mock_fetch.call_args
    assert args[0] == 'http://127.0.0.1/hypotez.online/api/'
    assert kwargs['method'] == 'POST'
    assert kwargs['headers'] == {'Content-Type': 'application/json'}
    
    
    expected_data = {
        'title': "Test Title",
        'url': "http://example.com/test",
        'body': "<p>Test Body Content</p>"
    }
    assert json.loads(kwargs['body']) == expected_data

def test_onPageLoad_failed_fetch(mock_fetch, mock_document, mock_window):
    """Checks correct behavior with a failed fetch request."""
    mock_response = Mock()
    mock_response.ok = False
    mock_fetch.return_value = Promise(resolve=mock_response)
    
    from hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data import onPageLoad
    
    with pytest.raises(Exception, match="Network response was not ok"):
        onPageLoad()

def test_onPageLoad_fetch_error(mock_fetch, mock_document, mock_window):
    """Checks error handling when fetch throws an error."""
    mock_fetch.return_value = Promise(reject=Exception("Fetch error"))
    from hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data import onPageLoad
    
    with patch('hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data.console.error') as mock_error:
        onPageLoad()
        mock_error.assert_called_once()
        assert "Fetch error" in str(mock_error.call_args.args[0])

def test_onPageLoad_empty_body(mock_fetch, mock_window):
    """Checks behavior when the body is empty"""
    mock_document = Mock()
    mock_document.title = "Empty body"
    mock_document.body = Mock()
    mock_document.body.innerHTML = ""
    
    mock_response = Mock()
    mock_response.ok = True
    mock_response.json.return_value = {"status": "success"}
    mock_fetch.return_value = Promise(resolve=mock_response)

    with patch('hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data.document', new=mock_document):
        from hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data import onPageLoad
        onPageLoad()
        mock_fetch.assert_called_once()
        args, kwargs = mock_fetch.call_args
        expected_data = {
        'title': "Empty body",
        'url': "http://example.com/test",
        'body': ""
    }
        assert json.loads(kwargs['body']) == expected_data

def test_onPageLoad_no_title(mock_fetch, mock_window):
    """Checks behaviour when the title is missing"""
    mock_document = Mock()
    mock_document.title = ""
    mock_document.body = Mock()
    mock_document.body.innerHTML = "Some Content"
    
    mock_response = Mock()
    mock_response.ok = True
    mock_response.json.return_value = {"status": "success"}
    mock_fetch.return_value = Promise(resolve=mock_response)

    with patch('hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data.document', new=mock_document):
        from hypotez.src.webdriver.firefox.extentions.test_extention.scripts.send_data import onPageLoad
        onPageLoad()
        mock_fetch.assert_called_once()
        args, kwargs = mock_fetch.call_args
        expected_data = {
            'title': "",
            'url': "http://example.com/test",
            'body': "Some Content"
        }
        assert json.loads(kwargs['body']) == expected_data
        
        
class Promise:
    def __init__(self, resolve=None, reject=None):
        self.resolve_callback = resolve
        self.reject_callback = reject
    def then(self, callback):
        if self.resolve_callback:
            callback(self.resolve_callback)
        return self
    def catch(self, callback):
        if self.reject_callback:
            callback(self.reject_callback)
        return self
```