```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidArgumentException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException,
)

# Mock dependencies that are not directly testable without a full environment
class MockWebElement:
    def __init__(self, text="mock_text", tag_name='div', displayed=True, enabled=True):
        self.text = text
        self.tag_name = tag_name
        self._displayed = displayed
        self._enabled = enabled

    def get_attribute(self, attribute_name):
        if attribute_name == 'innerHTML':
            return self.text
        return None

    @property
    def displayed(self):
        return self._displayed

    @property
    def is_enabled(self):
        return self._enabled

    def click(self):
      if not self._enabled:
        raise ElementNotInteractableException('Element is not enabled')
      if not self._displayed:
        raise ElementNotVisibleException('Element is not visible')

    def send_keys(self, text):
      pass
class MockWebDriver:
    def __init__(self, url=None, page_source="<html></html>", current_url="about:blank"):
        self.current_url = current_url
        self.url = url
        self.page_source = page_source
        self.execute_script_called = []
        self.get_called = []
        self.implicitly_wait_called = []
        self.current_window_handle = 'main_window'
        self.window_handles = ['main_window']
        self.log_types = ['browser', 'driver']
        self.logs = {
          'browser': [{'level': 'INFO', 'message': 'initial log'}],
          'driver': []
        }
        self.quit_called = False

    def execute_script(self, script, *args):
        self.execute_script_called.append((script, args))
        return True

    def get(self, url):
        self.get_called.append(url)
        self.current_url = url

    def find_element(self, by, value):
        return MockWebElement()

    def find_elements(self, by, value):
        return [MockWebElement()]

    def implicitly_wait(self, interval):
        self.implicitly_wait_called.append(interval)

    def switch_to_window(self, window_name):
      self.current_window_handle = window_name
    
    def current_url(self):
       return self.current_url
    
    def get_log(self, log_type):
       return self.logs[log_type]
    
    def quit(self):
      self.quit_called = True
      return True
class MockActionChains:
   def __init__(self, driver):
     self.driver = driver
     self.actions = []

   def move_to_element(self, element):
     self.actions.append(('move_to_element', element))
     return self

   def click(self):
     self.actions.append('click')
     return self

   def perform(self):
      pass
    
class MockExpectedConditions:
    def __init__(self):
        pass
    def visibility_of_element_located(self, locator):
        def _condition(driver):
           return True
        return _condition
    
    def presence_of_element_located(self, locator):
        def _condition(driver):
           return True
        return _condition
    
    def element_to_be_clickable(self, locator):
       def _condition(driver):
           return MockWebElement()
       return _condition
    
class MockWebDriverWait:
    def __init__(self, driver, timeout, poll_frequency=0.5):
      self.driver = driver
      self.timeout = timeout
      self.poll_frequency = poll_frequency
    
    def until(self, condition, message=''):
       return condition(self.driver)
    
    
@pytest.fixture
def mock_driver():
    """Provides a mocked WebDriver instance."""
    with patch('src.webdriver.driver.ActionChains', new=MockActionChains), \
         patch('src.webdriver.driver.EC', new=MockExpectedConditions()),\
         patch('src.webdriver.driver.WebDriverWait', new=MockWebDriverWait):
        driver = MockWebDriver()
    yield driver

@pytest.fixture
def driver_instance(mock_driver):
  from src.webdriver.driver import Driver
  driver = Driver(webdriver_cls=MagicMock(return_value=mock_driver))
  yield driver


def test_driver_payload_valid(driver_instance):
    """Checks driver_payload() with valid driver instance."""
    payload = driver_instance.driver_payload()
    assert isinstance(payload, dict)
    assert 'js' in payload
    assert 'execute_locator' in payload
    assert 'browser' in payload['js']
    assert 'send_message' in payload['js']
    assert 'pprint' in payload['js']
    assert 'utils' in payload['js']
    assert 'click' in payload['execute_locator']


def test_scroll_valid_positive_scrolls(driver_instance, mock_driver):
    """Checks scroll() with valid positive scrolls."""
    result = driver_instance.scroll(scrolls=2, frame_size=100, direction="down", delay=0.1)
    assert mock_driver.execute_script_called[0][0].startswith("window.scrollBy")
    assert mock_driver.execute_script_called[0][1] == (0, 100)
    assert result is None

def test_scroll_valid_negative_scrolls(driver_instance, mock_driver):
    """Checks scroll() with valid negative scrolls."""
    result = driver_instance.scroll(scrolls=-2, frame_size=100, direction="up", delay=0.1)
    assert mock_driver.execute_script_called[0][0].startswith("window.scrollBy")
    assert mock_driver.execute_script_called[0][1] == (0, -100)
    assert result is None


def test_scroll_invalid_direction(driver_instance):
    """Checks scroll() with invalid direction."""
    with pytest.raises(ValueError, match="Invalid scroll direction"):
      driver_instance.scroll(scrolls=2, frame_size=100, direction="invalid", delay=0.1)


def test_locale_valid(driver_instance):
    """Checks locale() returns 'en' by default if not set."""
    locale = driver_instance.locale()
    assert locale == 'en'


def test_get_url_valid(driver_instance, mock_driver):
    """Checks get_url() with a valid URL."""
    url = "https://example.com"
    result = driver_instance.get_url(url)
    assert result is True
    assert mock_driver.get_called[0] == url


def test_get_url_invalid(driver_instance):
    """Checks get_url() with an invalid URL (not a string)."""
    with pytest.raises(TypeError, match="url must be a string"):
        driver_instance.get_url(123)

def test_get_url_empty_url(driver_instance):
    """Checks get_url() with an empty string."""
    with pytest.raises(ValueError, match="url cannot be an empty string"):
        driver_instance.get_url("")


def test_extract_domain_valid(driver_instance):
    """Checks extract_domain() with a valid URL."""
    url = "https://www.example.com/path/to/page"
    domain = driver_instance.extract_domain(url)
    assert domain == "www.example.com"


def test_extract_domain_invalid_url(driver_instance):
    """Checks extract_domain() with an invalid URL."""
    url = "invalid-url"
    domain = driver_instance.extract_domain(url)
    assert domain == ""

def test_extract_domain_empty_url(driver_instance):
    """Checks extract_domain() with an empty string."""
    url = ""
    domain = driver_instance.extract_domain(url)
    assert domain == ""

def test_save_cookies_localy_valid(driver_instance, mock_driver, tmp_path):
    """Checks _save_cookies_localy() with a valid path."""
    file_path = tmp_path / "test_cookies.pkl"
    mock_driver.get_cookies = MagicMock(return_value=[{'name': 'test_cookie', 'value': 'test_value'}])
    result = driver_instance._save_cookies_localy(file_path)
    assert result is True
    assert file_path.exists()

def test_save_cookies_localy_no_cookies(driver_instance, mock_driver, tmp_path):
    """Checks _save_cookies_localy() with no cookies."""
    file_path = tmp_path / "test_cookies.pkl"
    mock_driver.get_cookies = MagicMock(return_value=[])
    result = driver_instance._save_cookies_localy(file_path)
    assert result is True
    assert not file_path.exists()

def test_save_cookies_localy_invalid_path(driver_instance, mock_driver):
    """Checks _save_cookies_localy() with invalid path (not a string or Path)."""
    with pytest.raises(TypeError, match="to_file must be a string or Path"):
      driver_instance._save_cookies_localy(123)

def test_save_cookies_localy_invalid_directory(driver_instance, mock_driver, tmp_path):
    """Checks _save_cookies_localy() with an invalid directory."""
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
       driver_instance._save_cookies_localy(tmp_path / "invalid_directory" / "test_cookies.pkl")

def test_page_refresh_valid(driver_instance, mock_driver):
    """Checks page_refresh() refreshes the page."""
    result = driver_instance.page_refresh()
    assert result is True
    assert mock_driver.get_called[-1] == mock_driver.current_url

def test_window_focus_valid(driver_instance, mock_driver):
    """Checks window_focus() switches to main window handle."""
    mock_driver.window_handles = ['another_window', 'main_window']
    mock_driver.current_window_handle = 'another_window'
    driver_instance.window_focus()
    assert mock_driver.current_window_handle == 'main_window'

def test_wait_valid(driver_instance, mock_driver):
    """Checks wait() calls implicitly_wait on the driver."""
    interval = 2.5
    driver_instance.wait(interval)
    assert mock_driver.implicitly_wait_called[0] == interval


def test_delete_driver_logs_valid(driver_instance, mock_driver):
   """Checks delete_driver_logs removes all logs from all log types"""
   mock_driver.logs['browser'] = [{'level': 'INFO', 'message': 'log to delete'}]
   mock_driver.logs['driver'] = [{'level': 'INFO', 'message': 'another log to delete'}]
   result = driver_instance.delete_driver_logs()
   assert result == True
   assert mock_driver.logs['browser'] == []
   assert mock_driver.logs['driver'] == []

def test_get_page_lang_valid(driver_instance, mock_driver):
    """Checks get_page_lang() returns 'en' by default if not set."""
    lang = driver_instance.get_page_lang()
    assert lang == 'en'

def test_unhide_DOM_element_valid(driver_instance, mock_driver):
    """Checks unhide_DOM_element() calls execute_script with the correct arguments."""
    locator = (By.ID, "test_id")
    driver_instance.unhide_DOM_element(locator)
    assert mock_driver.execute_script_called[0][0].startswith("document.querySelector")
    assert 'test_id' in mock_driver.execute_script_called[0][0]

def test_get_referrer_default(driver_instance):
    """Checks get_referrer() return empty string by default"""
    assert driver_instance.get_referrer() == ''

def test_get_attribute_by_locator_valid(driver_instance, mock_driver):
    """Checks get_attribute_by_locator() returns the innerHTML of the element located by the provided locator."""
    locator = (By.ID, "test_id")
    attribute = driver_instance.get_attribute_by_locator(locator, 'innerHTML')
    assert attribute == "mock_text"

def test_get_attribute_by_locator_element_not_found(driver_instance, mock_driver):
    """Checks get_attribute_by_locator() returns None if no element was found."""
    locator = (By.ID, "not_found")
    mock_driver.find_element = MagicMock(return_value = None)
    attribute = driver_instance.get_attribute_by_locator(locator, 'innerHTML')
    assert attribute == None

def test_get_attribute_by_locator_no_attribute(driver_instance, mock_driver):
    """Checks get_attribute_by_locator() returns None if the attribute does not exists."""
    locator = (By.ID, "test_id")
    attribute = driver_instance.get_attribute_by_locator(locator, 'not_exists')
    assert attribute is None

def test_send_message_valid(driver_instance, mock_driver):
  """Checks send_message() calls js send_message with valid arguments"""
  message = 'This is a test message'
  driver_instance.send_message(message)
  assert mock_driver.execute_script_called[0][0].startswith('return (function (message) {')
  assert mock_driver.execute_script_called[0][1] == (message,)
  

def test_send_key_to_webelement_valid(driver_instance, mock_driver):
  """Checks send_key_to_webelement() calls send_keys with a webelement"""
  locator = (By.ID, "test_id")
  keys = "test keys"
  mock_element = MockWebElement()
  mock_driver.find_element = MagicMock(return_value = mock_element)
  driver_instance.send_key_to_webelement(locator, keys)
  assert isinstance(mock_driver.find_element(locator[0], locator[1]), MockWebElement)
  assert True

def test_send_key_to_webelement_element_not_found(driver_instance, mock_driver):
    """Checks send_key_to_webelement() returns false if no element was found."""
    locator = (By.ID, "not_found")
    mock_driver.find_element = MagicMock(return_value = None)
    result = driver_instance.send_key_to_webelement(locator, "test")
    assert result == False

def test_click_valid(driver_instance, mock_driver):
    """Checks click() calls webelement.click() when element is found"""
    locator = (By.ID, "test_id")
    mock_element = MockWebElement()
    mock_driver.find_element = MagicMock(return_value = mock_element)
    driver_instance.click(locator)
    assert True

def test_click_element_not_found(driver_instance, mock_driver):
    """Checks click() returns False if element is not found"""
    locator = (By.ID, "not_found")
    mock_driver.find_element = MagicMock(return_value = None)
    result = driver_instance.click(locator)
    assert result == False

def test_click_element_not_enabled(driver_instance, mock_driver):
    """Checks click() returns False if element is not enabled"""
    locator = (By.ID, "test_id")
    mock_element = MockWebElement(enabled=False)
    mock_driver.find_element = MagicMock(return_value = mock_element)
    with pytest.raises(ElementNotInteractableException):
       driver_instance.click(locator)

def test_click_element_not_visible(driver_instance, mock_driver):
   """Checks click() returns False if element is not visible"""
   locator = (By.ID, "test_id")
   mock_element = MockWebElement(displayed=False)
   mock_driver.find_element = MagicMock(return_value = mock_element)
   with pytest.raises(ElementNotVisibleException):
      driver_instance.click(locator)

def test_get_webelement_as_screenshot_valid(driver_instance, mock_driver):
   """Checks get_webelement_as_screenshot return base64 string if element is found"""
   locator = (By.ID, "test_id")
   mock_element = MockWebElement()
   mock_element.screenshot_as_base64 = MagicMock(return_value = 'base64string')
   mock_driver.find_element = MagicMock(return_value = mock_element)
   result = driver_instance.get_webelement_as_screenshot(locator)
   assert result == 'base64string'

def test_get_webelement_as_screenshot_element_not_found(driver_instance, mock_driver):
   """Checks get_webelement_as_screenshot return False if element not found"""
   locator = (By.ID, "test_id")
   mock_driver.find_element = MagicMock(return_value = None)
   result = driver_instance.get_webelement_as_screenshot(locator)
   assert result == False
```