```python
import pytest
from unittest.mock import patch, mock_open
from pathlib import Path
from types import SimpleNamespace
import json
import logging

# Assuming the BS class is in src/webdriver/bs.py
# and the j_loads_ns function is in src/utils/jjson.py
from src.webdriver.bs import BS
from src.utils.jjson import j_loads_ns

# --- Fixtures ---
@pytest.fixture
def default_config_path(tmp_path):
    """Provides a path to a temporary config file."""
    config_data = {
        "default_url": "https://example.com",
        "default_file_path": "file://path/to/your/file.html",
        "default_locator": {
            "by": "ID",
            "attribute": "element_id",
            "selector": "//*[@id='element_id']"
        },
        "logging": {
            "level": "INFO",
            "file": "logs/bs.log"
        },
        "proxy": {
            "enabled": False,
            "server": "http://proxy.example.com:8080",
            "username": "user",
            "password": "password"
        },
        "timeout": 10,
        "encoding": "utf-8"
    }
    config_file = tmp_path / "bs.json"
    with open(config_file, "w") as f:
        json.dump(config_data, f)
    return config_file

@pytest.fixture
def mock_requests_get():
    """Mocks the requests.get function."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html><body><div id='element_id'>Test</div></body></html>"
        yield mock_get

@pytest.fixture
def mock_file_open():
     """Mocks the open function for file reading."""
     with patch("builtins.open", mock_open(read_data="<html><body><div id='element_id'>Test</div></body></html>")) as mock_file:
         yield mock_file


# --- Tests for BS Class ---

def test_bs_initialization_with_config(default_config_path):
    """Checks if BS initializes correctly with a config file."""
    settings = j_loads_ns(default_config_path)
    bs = BS(url=settings.default_url)
    assert bs.url == settings.default_url
    assert bs.timeout == settings.timeout
    assert bs.encoding == settings.encoding
    assert bs.logger is not None

def test_bs_initialization_without_config():
    """Checks if BS initializes correctly without config file."""
    bs = BS()
    assert bs.url is None
    assert bs.timeout == 10 # default timeout
    assert bs.encoding == "utf-8" # default encoding
    assert bs.logger is not None

def test_get_url_from_url(mock_requests_get):
    """Checks fetching HTML content from a URL."""
    bs = BS()
    url = "https://example.com"
    bs.get_url(url)
    mock_requests_get.assert_called_once_with(url, timeout=10, proxies=None)
    assert bs.html is not None
    
def test_get_url_from_file(mock_file_open):
    """Checks fetching HTML content from a file."""
    bs = BS()
    file_path = "file://path/to/your/file.html"
    bs.get_url(file_path)
    mock_file_open.assert_called_once_with("path/to/your/file.html", 'r', encoding='utf-8')
    assert bs.html is not None

def test_get_url_invalid_url():
    """Checks how it handles invalid URL."""
    bs = BS()
    with pytest.raises(ValueError, match="Invalid URL"):
        bs.get_url("invalid_url")

def test_execute_locator_valid_locator(mock_file_open):
    """Checks element extraction with valid locator."""
    bs = BS()
    file_path = "file://path/to/your/file.html"
    bs.get_url(file_path)
    locator = SimpleNamespace(by="ID", attribute="element_id", selector='//*[@id="element_id"]')
    elements = bs.execute_locator(locator)
    assert len(elements) == 1
    assert elements[0].text == "Test"

def test_execute_locator_invalid_locator_type():
    """Checks how it handles invalid locator type."""
    bs = BS()
    bs.html = "<html><body><div id='element_id'>Test</div></body></html>"
    locator = SimpleNamespace(by="INVALID", attribute="element_id", selector='//*[@id="element_id"]')
    with pytest.raises(ValueError, match="Unsupported locator type"):
        bs.execute_locator(locator)

def test_execute_locator_no_elements_found(mock_file_open):
    """Checks element extraction when no element is found."""
    bs = BS()
    file_path = "file://path/to/your/file.html"
    bs.get_url(file_path)
    locator = SimpleNamespace(by="ID", attribute="nonexistent_id", selector='//*[@id="nonexistent_id"]')
    elements = bs.execute_locator(locator)
    assert len(elements) == 0

def test_execute_locator_no_html_set():
     """Checks execute_locator when html is not set."""
     bs = BS()
     locator = SimpleNamespace(by="ID", attribute="element_id", selector='//*[@id="element_id"]')
     with pytest.raises(AttributeError, match="HTML content not loaded. Use get_url first."):
         bs.execute_locator(locator)
         
def test_execute_locator_css_selector(mock_file_open):
    """Checks element extraction with CSS selector."""
    bs = BS()
    file_path = "file://path/to/your/file.html"
    bs.get_url(file_path)
    locator = SimpleNamespace(by="CSS", attribute="element_id", selector='#element_id')
    elements = bs.execute_locator(locator)
    assert len(elements) == 1
    assert elements[0].text == "Test"
    
def test_execute_locator_text_selector(mock_file_open):
    """Checks element extraction with text selector."""
    bs = BS()
    file_path = "file://path/to/your/file.html"
    bs.get_url(file_path)
    locator = SimpleNamespace(by="TEXT", attribute="text", selector='Test')
    elements = bs.execute_locator(locator)
    assert len(elements) == 1
    assert elements[0].text == "Test"
        
def test_proxy_settings_from_config(default_config_path, mock_requests_get):
    """Checks if proxy settings are applied when enabled in the config."""
    config_data = {
        "default_url": "https://example.com",
        "default_file_path": "file://path/to/your/file.html",
        "default_locator": {
            "by": "ID",
            "attribute": "element_id",
            "selector": "//*[@id='element_id']"
        },
        "logging": {
            "level": "INFO",
            "file": "logs/bs.log"
        },
        "proxy": {
            "enabled": True,
            "server": "http://proxy.example.com:8080",
            "username": "proxyuser",
            "password": "proxypassword"
        },
        "timeout": 10,
        "encoding": "utf-8"
    }
    
    config_file = default_config_path
    with open(config_file, "w") as f:
      json.dump(config_data, f)
    settings = j_loads_ns(config_file)
    bs = BS(url=settings.default_url)
    bs.get_url(settings.default_url)
    expected_proxies = {
        "http": "http://proxyuser:proxypassword@proxy.example.com:8080",
        "https": "http://proxyuser:proxypassword@proxy.example.com:8080",
    }
    mock_requests_get.assert_called_once_with(
        settings.default_url, timeout=10, proxies=expected_proxies
    )

def test_no_proxy_settings_from_config(default_config_path, mock_requests_get):
    """Checks if no proxy settings are applied when disabled in the config."""
    settings = j_loads_ns(default_config_path)
    bs = BS(url=settings.default_url)
    bs.get_url(settings.default_url)
    mock_requests_get.assert_called_once_with(settings.default_url, timeout=10, proxies=None)
```