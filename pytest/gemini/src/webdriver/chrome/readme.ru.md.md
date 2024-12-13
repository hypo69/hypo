```python
import pytest
import json
from unittest.mock import patch, mock_open
from src.webdriver.chrome import Chrome  # Assuming the class is in this location
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


@pytest.fixture
def mock_chrome_json():
    """Provides a mock chrome.json configuration for testing."""
    return {
        "options": {
            "log-level": "5",
            "disable-dev-shm-usage": "",
            "remote-debugging-port": "0",
            "arguments": ["--kiosk", "--disable-gpu"],
        },
        "disabled_options": {"headless": ""},
        "profile_directory": {
            "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
            "internal": "webdriver\\chrome\\profiles\\default",
            "testing": "%LOCALAPPDATA%\\Google\\Chrome for Testing\\User Data",
        },
        "binary_location": {
            "os": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "exe": "bin\\webdrivers\\chrome\\125.0.6422.14\\chromedriver.exe",
            "binary": "bin\\webdrivers\\chrome\\125.0.6422.14\\win64-125.0.6422.14\\chrome-win64\\chrome.exe",
            "chromium": "bin\\webdrivers\\chromium\\chrome-win\\chrome.exe",
        },
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
        },
        "proxy_enabled": False,
    }


@patch("builtins.open", new_callable=mock_open)
def test_chrome_init_with_default_config(mock_file, mock_chrome_json):
    """
    Tests if Chrome initializes correctly with default configurations from json file.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    
    browser = Chrome()

    assert browser.options is not None
    assert browser.user_agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    assert "--kiosk" in browser.options.arguments
    assert "--disable-gpu" in browser.options.arguments
    assert not browser.options.headless

    # Check that a new browser instance was created
    assert browser._driver is not None
    browser.quit() # Ensure the browser is closed


@patch("builtins.open", new_callable=mock_open)
def test_chrome_init_with_custom_user_agent(mock_file, mock_chrome_json):
    """
    Tests if Chrome initializes with a custom user agent.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    custom_user_agent = "Test User Agent"
    browser = Chrome(user_agent=custom_user_agent)
    assert browser.user_agent == custom_user_agent
    browser.quit()


@patch("builtins.open", new_callable=mock_open)
def test_chrome_init_with_custom_options(mock_file, mock_chrome_json):
    """
    Tests if Chrome initializes with additional options passed at initialization.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    custom_options = ["--headless", "--window-size=1920,1080"]
    browser = Chrome(options=custom_options)
    
    for opt in custom_options:
         assert opt in browser.options.arguments
    
    browser.quit()
    

@patch("builtins.open", new_callable=mock_open)
def test_chrome_singleton_pattern(mock_file, mock_chrome_json):
    """
    Tests if the singleton pattern ensures only one instance of WebDriver is created.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    browser1 = Chrome()
    browser2 = Chrome()
    assert browser1 is browser2
    browser1.quit()


@patch("builtins.open", new_callable=mock_open)
def test_chrome_get_method(mock_file, mock_chrome_json):
    """
    Tests if the get method successfully opens a URL.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    browser = Chrome()
    test_url = "https://www.example.com"
    browser.get(test_url)
    assert browser._driver.current_url == test_url
    browser.quit()


@patch("builtins.open", new_callable=mock_open)
def test_chrome_quit_method(mock_file, mock_chrome_json):
    """
    Tests if the quit method closes the browser.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    browser = Chrome()
    browser.quit()
    with pytest.raises(Exception):
        browser._driver.current_url  # Raises an exception if the driver is closed


@patch("builtins.open", new_callable=mock_open)
def test_chrome_invalid_json(mock_file):
    """
    Tests how Chrome handles invalid json file format.
    """
    mock_file.return_value.read.return_value = 'invalid json'
    with pytest.raises(json.JSONDecodeError):
         Chrome()
         
         
@patch("builtins.open", new_callable=mock_open)
def test_chrome_missing_config_file(mock_file):
    """
    Tests how Chrome handles a missing configuration file.
    """
    mock_file.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        Chrome()


def test_chrome_default_user_agent_generation():
    """
    Test user agent generation with default value
    """
    user_agent = Chrome().user_agent
    assert user_agent != ""


def test_chrome_user_agent_generation_fake():
    """
    Test user agent generation with fake UserAgent
    """
    ua = UserAgent()
    user_agent = Chrome(user_agent=ua.random).user_agent
    assert user_agent != ""


def test_chrome_default_options():
   """Test default options setting."""
   chrome = Chrome()
   assert isinstance(chrome.options, Options)
   chrome.quit()

@patch("builtins.open", new_callable=mock_open)
def test_chrome_custom_headers(mock_file, mock_chrome_json):
    """
    Tests if Chrome initializes with headers from json configuration.
    """
    mock_file.return_value.read.return_value = json.dumps(mock_chrome_json)
    browser = Chrome()
    
    # Check if headers are set
    assert browser.headers["User-Agent"] == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    assert browser.headers["Accept"] == "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8"
    assert browser.headers["Accept-Charset"] == "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
    assert browser.headers["Accept-Encoding"] == "none"
    assert browser.headers["Accept-Language"] == "en-US,en;q=0.8"
    assert browser.headers["Connection"] == "keep-alive"
    
    browser.quit()

```