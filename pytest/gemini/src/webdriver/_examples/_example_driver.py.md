```python
import pytest
from unittest.mock import MagicMock, patch
from src.webdriver.driver import Driver, Chrome, Firefox, Edge

# Mock the webdriver classes for testing purposes
class MockWebDriver:
    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.get_url_called = False
        self.scroll_called = False
        self.quit_called = False
        self.domain = None
    
    def get(self, url):
        self.get_url_called = True
        return True
    
    def execute_script(self, script):
      self.scroll_called = True
      return True

    def quit(self):
        self.quit_called = True
    
    def get_cookies(self):
        return [{'domain':'test.com', 'name':'test_cookie', 'value':'test_value'}]
    
    def current_url(self):
        return 'https://test.com'

class MockChrome(MockWebDriver):
    def __init__(self):
        super().__init__("Chrome")
    
class MockFirefox(MockWebDriver):
    def __init__(self):
        super().__init__("Firefox")

class MockEdge(MockWebDriver):
    def __init__(self):
        super().__init__("Edge")


# Fixture for creating a Driver instance with a mock webdriver
@pytest.fixture(params=[MockChrome, MockFirefox, MockEdge])
def mock_driver(request):
    """Creates a Driver instance with a mock webdriver."""
    mock_browser_class = request.param
    mock_browser = mock_browser_class()
    with patch('src.webdriver.driver.webdriver', create=True) as mock_webdriver:
        if mock_browser.browser_type == "Chrome":
            mock_webdriver.Chrome.return_value = mock_browser
        elif mock_browser.browser_type == "Firefox":
            mock_webdriver.Firefox.return_value = mock_browser
        elif mock_browser.browser_type == "Edge":
            mock_webdriver.Edge.return_value = mock_browser

        driver = Driver(mock_browser_class)
        yield driver, mock_browser
        driver.quit()

# Test cases for Driver.get_url
def test_get_url_valid(mock_driver):
    """Checks correct navigation with a valid URL."""
    driver, mock_browser = mock_driver
    url = "https://www.example.com"
    assert driver.get_url(url) is True
    assert mock_browser.get_url_called is True

def test_get_url_invalid(mock_driver):
    """Checks correct handling of an invalid URL."""
    driver, mock_browser = mock_driver
    url = "invalid-url"
    with patch.object(driver.driver, 'get', side_effect=Exception("Invalid URL")):
       assert driver.get_url(url) is False
    assert mock_browser.get_url_called is False

# Test cases for Driver.extract_domain
def test_extract_domain_valid_url(mock_driver):
    """Checks correct domain extraction from a valid URL."""
    driver, mock_browser = mock_driver
    url = "https://www.example.com/path"
    domain = driver.extract_domain(url)
    assert domain == "www.example.com"

def test_extract_domain_invalid_url(mock_driver):
    """Checks handling of an invalid URL for domain extraction."""
    driver, mock_browser = mock_driver
    url = "invalid-url"
    domain = driver.extract_domain(url)
    assert domain is None

def test_extract_domain_without_protocol(mock_driver):
  """Check the extraction of a valid domain with no protocol given"""
  driver, mock_browser = mock_driver
  url = "www.example.com/path"
  domain = driver.extract_domain(url)
  assert domain == "www.example.com"

# Test cases for Driver.scroll
def test_scroll_forward_valid(mock_driver):
    """Checks correct scrolling forward."""
    driver, mock_browser = mock_driver
    assert driver.scroll(scrolls=2, direction='forward') is True
    assert mock_browser.scroll_called is True

def test_scroll_backward_valid(mock_driver):
    """Checks correct scrolling backward."""
    driver, mock_browser = mock_driver
    assert driver.scroll(scrolls=1, direction='backward') is True
    assert mock_browser.scroll_called is True

def test_scroll_both_valid(mock_driver):
    """Checks correct scrolling in both directions."""
    driver, mock_browser = mock_driver
    assert driver.scroll(scrolls=1, direction='both') is True
    assert mock_browser.scroll_called is True

def test_scroll_invalid_direction(mock_driver):
    """Checks handling of an invalid scroll direction."""
    driver, mock_browser = mock_driver
    assert driver.scroll(scrolls=1, direction='invalid') is False
    assert mock_browser.scroll_called is False

# Test cases for Driver._save_cookies_localy
def test_save_cookies_localy_valid(mock_driver):
    """Checks that cookies are saved locally with valid parameters."""
    driver, mock_browser = mock_driver
    with patch('src.webdriver.driver.pickle.dump') as mock_pickle_dump:
        assert driver._save_cookies_localy(to_file='cookies.pkl') is True
        mock_pickle_dump.assert_called()

def test_save_cookies_localy_no_cookies(mock_driver):
    """Checks that cookies are not saved if driver returns empty cookies"""
    driver, mock_browser = mock_driver
    mock_browser.get_cookies = MagicMock(return_value=[])
    with patch('src.webdriver.driver.pickle.dump') as mock_pickle_dump:
      assert driver._save_cookies_localy(to_file='cookies.pkl') is False
      mock_pickle_dump.assert_not_called()

def test_save_cookies_localy_no_file(mock_driver):
   """Checks that cookies are not saved if file is not specified"""
   driver, mock_browser = mock_driver
   with patch('src.webdriver.driver.pickle.dump') as mock_pickle_dump:
     assert driver._save_cookies_localy(to_file='') is False
     mock_pickle_dump.assert_not_called()

# Test cases for Driver.quit
def test_quit(mock_driver):
    """Checks that the driver is closed."""
    driver, mock_browser = mock_driver
    driver.quit()
    assert mock_browser.quit_called is True
```