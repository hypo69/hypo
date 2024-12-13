```python
import pytest
from unittest.mock import patch, MagicMock
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By


@pytest.fixture
def mock_chrome_driver():
    """Provides a mocked Chrome driver instance."""
    mock_driver = MagicMock()
    mock_driver.get.return_value = None
    mock_driver.execute_script.return_value = None
    mock_driver.get_cookies.return_value = []
    mock_driver.current_url = "https://www.example.com"
    mock_driver.find_element.return_value = MagicMock(text="Example Heading")
    mock_driver.title = "Example Domain"
    mock_driver.page_source = "<html><body><h1>Example Heading</h1></body></html>"

    return mock_driver

@pytest.fixture
def driver_instance(mock_chrome_driver):
    """Provides a Driver instance using the mocked Chrome driver."""
    with patch("src.webdriver.driver.Chrome", return_value=mock_chrome_driver):
        driver = Driver(Chrome)
    return driver

def test_driver_get_url_valid(driver_instance, mock_chrome_driver):
    """Checks correct behavior of get_url with a valid URL."""
    mock_chrome_driver.get.return_value = None  # Simulate successful navigation
    assert driver_instance.get_url("https://www.example.com") is True
    mock_chrome_driver.get.assert_called_once_with("https://www.example.com")

def test_driver_get_url_invalid(driver_instance, mock_chrome_driver):
    """Checks correct behavior of get_url with an invalid URL."""
    mock_chrome_driver.get.side_effect = Exception("Navigation error")
    assert driver_instance.get_url("invalid_url") is False
    mock_chrome_driver.get.assert_called_once_with("invalid_url")


def test_driver_extract_domain_valid_url(driver_instance):
    """Checks correct extraction of domain from a valid URL."""
    url = "https://www.example.com/path/to/page"
    expected_domain = "www.example.com"
    assert driver_instance.extract_domain(url) == expected_domain

def test_driver_extract_domain_invalid_url(driver_instance):
    """Checks correct handling of an invalid URL during domain extraction."""
    url = "invalid-url"
    with pytest.raises(ValueError):
         driver_instance.extract_domain(url)


def test_driver_save_cookies_localy_success(driver_instance, mock_chrome_driver):
    """Checks that cookies are saved locally successfully."""
    mock_chrome_driver.get_cookies.return_value = [{"name": "test_cookie", "value": "test_value"}]
    with patch("src.webdriver.driver.os.path.exists", return_value=True), \
         patch("src.webdriver.driver.json.dump", return_value=None):
        assert driver_instance._save_cookies_localy() is True
    
def test_driver_save_cookies_localy_no_cookies(driver_instance, mock_chrome_driver):
    """Checks that returns False if no cookies are found."""
    mock_chrome_driver.get_cookies.return_value = []
    assert driver_instance._save_cookies_localy() is False

def test_driver_save_cookies_localy_exception(driver_instance, mock_chrome_driver):
     """Checks that the exception is handled gracefully."""
     mock_chrome_driver.get_cookies.return_value = [{"name": "test_cookie", "value": "test_value"}]
     with patch("src.webdriver.driver.os.path.exists", return_value=True), \
        patch("src.webdriver.driver.json.dump", side_effect=Exception("Failed to save cookies")):
            assert driver_instance._save_cookies_localy() is False
    
def test_driver_page_refresh_success(driver_instance, mock_chrome_driver):
    """Checks that page refresh executes without errors."""
    assert driver_instance.page_refresh() is True
    mock_chrome_driver.refresh.assert_called_once()

def test_driver_page_refresh_exception(driver_instance, mock_chrome_driver):
    """Checks that an exception during page refresh is handled."""
    mock_chrome_driver.refresh.side_effect = Exception("Refresh failed")
    assert driver_instance.page_refresh() is False
    mock_chrome_driver.refresh.assert_called_once()


def test_driver_scroll_forward_success(driver_instance, mock_chrome_driver):
    """Checks that scrolling forward executes without errors."""
    assert driver_instance.scroll(scrolls=2, direction="forward", frame_size=500, delay=0.1) is True
    assert mock_chrome_driver.execute_script.call_count == 2

def test_driver_scroll_backward_success(driver_instance, mock_chrome_driver):
    """Checks that scrolling backward executes without errors."""
    assert driver_instance.scroll(scrolls=2, direction="backward", frame_size=500, delay=0.1) is True
    assert mock_chrome_driver.execute_script.call_count == 2

def test_driver_scroll_invalid_direction(driver_instance):
    """Checks that an exception is raised for an invalid scroll direction."""
    with pytest.raises(ValueError):
        driver_instance.scroll(scrolls=1, direction="invalid", frame_size=100, delay=0.1)

def test_driver_scroll_exception(driver_instance, mock_chrome_driver):
    """Checks that exception is handled during scrolling."""
    mock_chrome_driver.execute_script.side_effect = Exception("Scroll failed")
    assert driver_instance.scroll(scrolls=1, direction="forward", frame_size=100, delay=0.1) is False

def test_driver_locale(driver_instance, mock_chrome_driver):
    """Checks that the locale property returns the correct language."""
    mock_chrome_driver.execute_script.return_value = "en-US"
    assert driver_instance.locale == "en-US"

def test_driver_locale_exception(driver_instance, mock_chrome_driver):
    """Checks that exception is handled during getting the page locale."""
    mock_chrome_driver.execute_script.side_effect = Exception("Failed to get locale")
    assert driver_instance.locale is None
    
def test_driver_find_element_success(driver_instance, mock_chrome_driver):
    """Checks find_element with valid selector."""
    element = driver_instance.find_element(By.CSS_SELECTOR, "h1")
    assert element.text == "Example Heading"
    mock_chrome_driver.find_element.assert_called_once_with(By.CSS_SELECTOR, "h1")
    
def test_driver_find_element_not_found(driver_instance, mock_chrome_driver):
    """Checks find_element returns None if element not found."""
    mock_chrome_driver.find_element.return_value = None
    element = driver_instance.find_element(By.CSS_SELECTOR, "nonexistent")
    assert element is None
    mock_chrome_driver.find_element.assert_called_once_with(By.CSS_SELECTOR, "nonexistent")

def test_driver_find_element_exception(driver_instance, mock_chrome_driver):
    """Checks that the exception is handled when finding element."""
    mock_chrome_driver.find_element.side_effect = Exception("Find element failed")
    element = driver_instance.find_element(By.CSS_SELECTOR, "h1")
    assert element is None

def test_driver_current_url(driver_instance, mock_chrome_driver):
     """Checks that current_url property retrieves the current url."""
     assert driver_instance.current_url == "https://www.example.com"
     
def test_driver_window_focus(driver_instance, mock_chrome_driver):
    """Checks that window focus executes without error."""
    driver_instance.window_focus()
    mock_chrome_driver.switch_to.window.assert_called_once()

def test_driver_window_focus_exception(driver_instance, mock_chrome_driver):
    """Checks that an exception is handled during window focus."""
    mock_chrome_driver.switch_to.window.side_effect = Exception("Focus failed")
    driver_instance.window_focus()
```