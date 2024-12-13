```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
import requests
from requests.exceptions import RequestException, ProxyError

from src.webdriver.proxy import download_proxies_list, get_proxies_dict, check_proxy, proxies_list_path

# Fixture for a mock logger
@pytest.fixture
def mock_logger():
    class MockLogger:
        def info(self, message):
            print(f"INFO: {message}")
        def error(self, message, *args):
             print(f"ERROR: {message} {args}")
        def warning(self, message, *args, **kwargs):
            print(f"WARNING: {message} {args} {kwargs}")

    with patch('src.webdriver.proxy.logger', new=MockLogger()) as mock:
        yield mock

# Fixture for a mock requests
@pytest.fixture
def mock_requests():
    with patch('src.webdriver.proxy.requests') as mock_requests:
        yield mock_requests

# Fixture for a temporary test file
@pytest.fixture
def temp_test_file(tmp_path):
    test_file = tmp_path / "test_proxies.txt"
    return test_file

# --- Tests for download_proxies_list ---
def test_download_proxies_list_success(mock_requests, mock_logger, temp_test_file):
    """Checks successful download of proxies list."""
    mock_response = mock_requests.get.return_value
    mock_response.status_code = 200
    mock_response.iter_content.return_value = [b'test data']
    
    assert download_proxies_list(save_path=temp_test_file) == True
    mock_requests.get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()
    
    # Check if the file was actually written
    with open(temp_test_file, 'r') as f:
        content = f.read()
    assert content == 'test data'

def test_download_proxies_list_http_error(mock_requests, mock_logger, temp_test_file):
    """Checks handling of HTTP error during download."""
    mock_response = mock_requests.get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP Error")
    
    assert download_proxies_list(save_path=temp_test_file) == False
    mock_requests.get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()

def test_download_proxies_list_request_exception(mock_requests, mock_logger, temp_test_file):
    """Checks handling of other request exceptions during download."""
    mock_requests.get.side_effect = RequestException("Request error")
    
    assert download_proxies_list(save_path=temp_test_file) == False
    mock_requests.get.assert_called_once()

# --- Tests for get_proxies_dict ---
def test_get_proxies_dict_valid_file(mock_logger, temp_test_file):
    """Checks parsing of a file with valid proxies."""
    with open(temp_test_file, 'w', encoding='utf-8') as f:
        f.write("http://1.1.1.1:8080\n")
        f.write("socks4://2.2.2.2:1080\n")
        f.write("socks5://3.3.3.3:1081\n")

    proxies = get_proxies_dict(file_path=temp_test_file)

    assert proxies == {
        'http': [{'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}],
        'socks4': [{'protocol': 'socks4', 'host': '2.2.2.2', 'port': '1080'}],
        'socks5': [{'protocol': 'socks5', 'host': '3.3.3.3', 'port': '1081'}]
    }

def test_get_proxies_dict_file_not_found(mock_logger):
    """Checks handling of FileNotFoundError."""
    non_existent_file = Path("non_existent_file.txt")
    proxies = get_proxies_dict(file_path=non_existent_file)
    assert proxies == {
        'http': [],
        'socks4': [],
        'socks5': []
    }
    
    
def test_get_proxies_dict_invalid_format(mock_logger, temp_test_file):
     """Checks handling of invalid proxy format."""
     with open(temp_test_file, 'w', encoding='utf-8') as f:
         f.write("invalid_proxy_format\n")
         f.write("http://1.1.1.1:8080\n")
         f.write("invalid_proxy_format2\n")

     proxies = get_proxies_dict(file_path=temp_test_file)
     assert proxies == {
        'http': [{'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}],
        'socks4': [],
        'socks5': []
    }

def test_get_proxies_dict_empty_file(mock_logger, temp_test_file):
    """Checks parsing of an empty file."""
    with open(temp_test_file, 'w', encoding='utf-8') as f:
        pass

    proxies = get_proxies_dict(file_path=temp_test_file)
    assert proxies == {
        'http': [],
        'socks4': [],
        'socks5': []
    }


# --- Tests for check_proxy ---
def test_check_proxy_valid(mock_requests, mock_logger):
    """Checks a working proxy."""
    mock_response = mock_requests.get.return_value
    mock_response.status_code = 200
    
    proxy = {'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}
    
    assert check_proxy(proxy) == True
    mock_requests.get.assert_called_once()

def test_check_proxy_not_working(mock_requests, mock_logger):
    """Checks a not working proxy."""
    mock_response = mock_requests.get.return_value
    mock_response.status_code = 404
    
    proxy = {'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}
    
    assert check_proxy(proxy) == False
    mock_requests.get.assert_called_once()


def test_check_proxy_proxy_error(mock_requests, mock_logger):
    """Checks handling of ProxyError during proxy check."""
    mock_requests.get.side_effect = ProxyError("Proxy error")
    proxy = {'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}
    assert check_proxy(proxy) == False
    mock_requests.get.assert_called_once()

def test_check_proxy_request_exception(mock_requests, mock_logger):
    """Checks handling of other request exceptions during proxy check."""
    mock_requests.get.side_effect = RequestException("Request error")
    proxy = {'protocol': 'http', 'host': '1.1.1.1', 'port': '8080'}
    assert check_proxy(proxy) == False
    mock_requests.get.assert_called_once()
```