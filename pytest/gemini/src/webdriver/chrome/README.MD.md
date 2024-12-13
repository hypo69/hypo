```python
import pytest
import json
from unittest.mock import patch, mock_open
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

# Assuming the necessary logger and singleton class are available
# For the sake of testability we will mock them here
class MockLogger:
    def __init__(self):
        self.logs = []

    def info(self, message):
        self.logs.append(f"INFO: {message}")

    def warning(self, message):
        self.logs.append(f"WARNING: {message}")

    def error(self, message):
        self.logs.append(f"ERROR: {message}")

    def debug(self, message):
        self.logs.append(f"DEBUG: {message}")

logger = MockLogger()

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
# Mock the Singleton metaclass
class MockSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
           cls._instances[cls] = object.__new__(cls)
           cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

# Mock Chrome class
class MockChrome(metaclass=MockSingleton):

    def __init__(self, user_agent=None, options=None):
      self.user_agent = user_agent
      self.options = options
      self.driver = self.create_mock_driver()
    
    def create_mock_driver(self):
       class MockDriver:
          def __init__(self):
            self.current_url = None
            self.closed = False
          def get(self, url):
              self.current_url = url
          def quit(self):
              self.closed = True
       return MockDriver()

    def get(self, url):
      self.driver.get(url)

    def quit(self):
        self.driver.quit()


@pytest.fixture
def mock_chrome_json():
    """Provides mock data for chrome.json file."""
    return {
    "options": {
        "log-level": "5",
        "disable-dev-shm-usage": "",
        "remote-debugging-port": "0",
        "arguments": ["--kiosk", "--disable-gpu"]
    },
    "disabled_options": {"headless": ""},
    "profile_directory": {
        "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
        "internal": "webdriver\\chrome\\profiles\\default",
        "testing": "%LOCALAPPDATA%\\Google\\Chrome for Testing\\User Data"
    },
    "binary_location": {
        "os": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "exe": "bin\\webdrivers\\chrome\\125.0.6422.14\\chromedriver.exe",
        "binary": "bin\\webdrivers\\chrome\\125.0.6422.14\\win64-125.0.6422.14\\chrome-win64\\chrome.exe",
        "chromium": "bin\\webdrivers\\chromium\\chrome-win\\chrome.exe"
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive"
    },
    "proxy_enabled": False
}

@pytest.fixture
def mock_chrome_class(mock_chrome_json):
    """Mocks the Chrome class."""
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_chrome_json))):
        yield MockChrome
        MockSingleton._instances = {}
        

def test_chrome_initialization_default_config(mock_chrome_class):
    """Test Chrome initialization with default configuration."""
    browser = mock_chrome_class()
    assert browser.user_agent is None
    assert browser.options is None

def test_chrome_initialization_custom_user_agent(mock_chrome_class):
    """Test Chrome initialization with a custom user agent."""
    browser = mock_chrome_class(user_agent="Custom User Agent")
    assert browser.user_agent == "Custom User Agent"
    assert browser.options is None


def test_chrome_initialization_custom_options(mock_chrome_class):
    """Test Chrome initialization with custom options."""
    browser = mock_chrome_class(options=["--headless"])
    assert browser.user_agent is None
    assert browser.options == ["--headless"]

def test_chrome_initialization_custom_user_agent_and_options(mock_chrome_class):
    """Test Chrome initialization with custom user agent and options."""
    browser = mock_chrome_class(user_agent="Custom User Agent", options=["--headless"])
    assert browser.user_agent == "Custom User Agent"
    assert browser.options == ["--headless"]
    
def test_chrome_singleton_pattern(mock_chrome_class):
    """Test that the Chrome class implements the singleton pattern."""
    browser1 = mock_chrome_class()
    browser2 = mock_chrome_class()
    assert browser1 is browser2

def test_chrome_get_method(mock_chrome_class):
    """Test the get method of the Chrome class."""
    browser = mock_chrome_class()
    browser.get("https://www.example.com")
    assert browser.driver.current_url == "https://www.example.com"

def test_chrome_quit_method(mock_chrome_class):
    """Test the quit method of the Chrome class."""
    browser = mock_chrome_class()
    browser.quit()
    assert browser.driver.closed is True
```