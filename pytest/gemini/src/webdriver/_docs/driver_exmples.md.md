```python
import pytest
from unittest.mock import patch, MagicMock
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import os
import json

# Mock the global settings object
class MockGlobalSettings:
    def __init__(self):
        self.settings_file_path = "mock_settings.json"
        # Create a mock settings file
        with open(self.settings_file_path, "w") as f:
            json.dump({"cookies": {"save_location": "mock_cookies.json"}}, f)

gs = MockGlobalSettings()

# Fixtures
@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance with a mock Chrome driver."""
    mock_chrome_driver = MagicMock()
    mock_chrome_driver.current_url = "https://www.example.com"
    mock_chrome_driver.page_source = "<html><body><h1>Test</h1></body></html>"
    mock_chrome_driver.get_cookies.return_value = [{"name": "test_cookie", "value": "test_value"}]
    mock_chrome_driver.execute_script.return_value = None
    mock_chrome_driver.find_element.return_value = MagicMock(text="Test Element")
    mock_chrome_driver.window_handles = ["test_window"]
    mock_chrome_driver.switch_to.window = MagicMock()

    with patch("src.webdriver.driver.Chrome", return_value=mock_chrome_driver):
        driver = Driver(Chrome)
        driver.driver = mock_chrome_driver
        yield driver

    # Clean up the mock settings file
    os.remove(gs.settings_file_path)
    os.remove("mock_cookies.json")

def test_driver_init(mock_driver):
    """Test the Driver class initialization."""
    assert isinstance(mock_driver, Driver)
    assert isinstance(mock_driver.driver, MagicMock)


def test_get_url_valid(mock_driver):
    """Test navigation to a valid URL."""
    mock_driver.driver.get.return_value = None  # Mock successful navigation
    assert mock_driver.get_url("https://www.example.com") is True
    mock_driver.driver.get.assert_called_once_with("https://www.example.com")


def test_get_url_invalid(mock_driver):
    """Test navigation to an invalid URL, checking for exception handling."""
    mock_driver.driver.get.side_effect = WebDriverException("Navigation failed")
    assert mock_driver.get_url("invalid_url") is False
    mock_driver.driver.get.assert_called_once_with("invalid_url")


def test_extract_domain_valid(mock_driver):
    """Test extracting a domain from a valid URL."""
    url = "https://www.example.com/path/to/page"
    domain = mock_driver.extract_domain(url)
    assert domain == "www.example.com"


def test_extract_domain_invalid_url(mock_driver):
    """Test extracting a domain from an invalid URL."""
    url = "invalid-url"
    domain = mock_driver.extract_domain(url)
    assert domain is None


def test_save_cookies_localy(mock_driver):
    """Test saving cookies to a local file."""
    mock_driver.driver.get_cookies.return_value = [{"name": "test_cookie", "value": "test_value"}]
    success = mock_driver._save_cookies_localy()
    assert success is True
    # Check if cookies.json file was created with correct data
    with open("mock_cookies.json", "r") as f:
        cookies_data = json.load(f)
    assert cookies_data == [{"name": "test_cookie", "value": "test_value"}]


def test_save_cookies_localy_no_cookies(mock_driver):
    """Test saving cookies to a local file when there are no cookies."""
    mock_driver.driver.get_cookies.return_value = []
    success = mock_driver._save_cookies_localy()
    assert success is True
    with open("mock_cookies.json", "r") as f:
        cookies_data = json.load(f)
    assert cookies_data == []


def test_page_refresh_success(mock_driver):
    """Test page refresh successfully."""
    mock_driver.driver.refresh.return_value = None
    assert mock_driver.page_refresh() is True
    mock_driver.driver.refresh.assert_called_once()

def test_page_refresh_fail(mock_driver):
    """Test page refresh failure."""
    mock_driver.driver.refresh.side_effect = WebDriverException("Refresh failed")
    assert mock_driver.page_refresh() is False
    mock_driver.driver.refresh.assert_called_once()


def test_scroll_valid(mock_driver):
    """Test successful page scrolling."""
    assert mock_driver.scroll(scrolls=1, direction='forward', frame_size=100, delay=0.1) is True
    mock_driver.driver.execute_script.assert_called()

def test_scroll_invalid_direction(mock_driver):
    """Test scrolling with an invalid direction."""
    assert mock_driver.scroll(scrolls=1, direction='invalid', frame_size=100, delay=0.1) is False

def test_scroll_exception(mock_driver):
     """Test page scrolling throws exception."""
     mock_driver.driver.execute_script.side_effect = WebDriverException("Scroll failed")
     assert mock_driver.scroll(scrolls=1, direction='forward', frame_size=100, delay=0.1) is False

def test_locale(mock_driver):
    """Test getting the page language."""
    mock_driver.driver.execute_script.return_value = "en-US"
    assert mock_driver.locale == "en-US"
    mock_driver.driver.execute_script.assert_called_with("return navigator.language;")


def test_locale_no_language(mock_driver):
    """Test getting page language when not available"""
    mock_driver.driver.execute_script.return_value = None
    assert mock_driver.locale == None
    mock_driver.driver.execute_script.assert_called_with("return navigator.language;")


def test_find_element_valid(mock_driver):
    """Test finding a single element by CSS selector."""
    element = mock_driver.find_element(By.CSS_SELECTOR, 'h1')
    assert element is not None
    assert element.text == "Test Element"
    mock_driver.driver.find_element.assert_called_once_with(By.CSS_SELECTOR, 'h1')


def test_find_element_not_found(mock_driver):
    """Test finding element that does not exist"""
    mock_driver.driver.find_element.return_value = None
    element = mock_driver.find_element(By.CSS_SELECTOR, 'div')
    assert element is None
    mock_driver.driver.find_element.assert_called_once_with(By.CSS_SELECTOR, 'div')


def test_find_element_exception(mock_driver):
    """Test exception handling when element is not found"""
    mock_driver.driver.find_element.side_effect = WebDriverException("Element not found")
    element = mock_driver.find_element(By.CSS_SELECTOR, 'div')
    assert element is None
    mock_driver.driver.find_element.assert_called_once_with(By.CSS_SELECTOR, 'div')

def test_current_url(mock_driver):
    """Test getting the current URL."""
    assert mock_driver.current_url == "https://www.example.com"

def test_window_focus(mock_driver):
    """Test focusing on the window"""
    mock_driver.window_focus()
    mock_driver.driver.switch_to.window.assert_called_once_with("test_window")
```