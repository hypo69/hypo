```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidArgumentException, WebDriverException

from src.webdriver.driver import Driver
from src.logger.exceptions import ExecuteLocatorException, WebDriverException

class MockWebDriver:
    """
    Mock class for simulating Selenium WebDriver behavior.
    """
    def __init__(self, *args, **kwargs):
        self.current_url = 'https://example.com'
        self.page_source = '<html><body><h1>Test Page</h1></body></html>'
        self.window_handles = ['handle1', 'handle2']
        self.ready_state = 'complete'
        self._cookies = [{"name": "test_cookie", "value": "test_value"}]

    def get(self, url):
        self.current_url = url

    def execute_script(self, script):
        pass

    def switch_to_window(self, handle):
        pass

    def find_element(self, by, value):
       if value == 'meta[http-equiv=\'Content-Language\']':
           mock_element = MagicMock()
           mock_element.get_attribute.return_value = 'en'
           return mock_element
       else:
            raise Exception('Element not found')
    
    def get_cookies(self):
        return self._cookies

    @property
    def current_url(self):
        return self._current_url
    
    @current_url.setter
    def current_url(self, value):
        self._current_url = value
        
    @property
    def ready_state(self):
        return self._ready_state
    
    @ready_state.setter
    def ready_state(self, value):
        self._ready_state = value
        
    @property
    def window_handles(self):
        return self._window_handles
    
    @window_handles.setter
    def window_handles(self, value):
        self._window_handles = value
    
    @property
    def page_source(self):
        return self._page_source
    
    @page_source.setter
    def page_source(self, value):
        self._page_source = value

@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance."""
    return Driver(MockWebDriver)

@pytest.fixture
def mock_webdriver_cls():
    """Provides a mock WebDriver class."""
    return MockWebDriver

def test_driver_init_valid_webdriver(mock_webdriver_cls):
    """Checks successful initialization with a valid WebDriver class."""
    driver = Driver(mock_webdriver_cls)
    assert isinstance(driver.driver, mock_webdriver_cls)

def test_driver_init_invalid_webdriver():
    """Checks that initialization fails with an invalid WebDriver class."""
    with pytest.raises(TypeError, match='`webdriver_cls` должен быть допустимым классом WebDriver.'):
        Driver(object)

def test_driver_init_subclass_no_browser_name():
    """Checks that a subclass without browser_name raises a ValueError."""
    with pytest.raises(ValueError, match='Класс TestDriver должен указать аргумент `browser_name`.'):
        class TestDriver(Driver):
            pass
        
def test_driver_init_subclass_with_browser_name():
    """Checks successful subclass initialization with a browser_name."""
    class TestDriver(Driver, browser_name='test_browser'):
        pass
    assert TestDriver.browser_name == 'test_browser'
    
def test_driver_getattr_proxy(mock_driver):
    """Checks that attribute access is correctly proxied to the underlying driver."""
    assert mock_driver.current_url == "https://example.com"

def test_driver_scroll_down(mock_driver):
    """Checks correct scroll behavior downwards."""
    with patch.object(mock_driver, 'execute_script') as mock_execute, \
         patch.object(mock_driver, 'wait') as mock_wait:
        mock_driver.scroll(scrolls=2, direction='down', frame_size=300, delay=0.1)
        mock_execute.assert_called_with('window.scrollBy(0,300)')
        assert mock_execute.call_count == 2
        assert mock_wait.call_count == 2

def test_driver_scroll_up(mock_driver):
    """Checks correct scroll behavior upwards."""
    with patch.object(mock_driver, 'execute_script') as mock_execute, \
         patch.object(mock_driver, 'wait') as mock_wait:
        mock_driver.scroll(scrolls=2, direction='up', frame_size=300, delay=0.1)
        mock_execute.assert_called_with('window.scrollBy(0,-300)')
        assert mock_execute.call_count == 2
        assert mock_wait.call_count == 2

def test_driver_scroll_both(mock_driver):
    """Checks correct scroll behavior both directions."""
    with patch.object(mock_driver, 'execute_script') as mock_execute, \
         patch.object(mock_driver, 'wait') as mock_wait:
        mock_driver.scroll(scrolls=1, direction='both', frame_size=300, delay=0.1)
        assert mock_execute.call_count == 2
        assert mock_wait.call_count == 2

def test_driver_scroll_error_handling(mock_driver):
    """Checks error handling during scrolling."""
    with patch.object(mock_driver, 'execute_script', side_effect=Exception('Test Exception')):
        assert mock_driver.scroll(direction='down') == False

def test_driver_locale_from_meta(mock_driver):
    """Checks correct retrieval of locale from meta tags."""
    assert mock_driver.locale == 'en'

def test_driver_locale_from_js(mock_driver):
     """Checks correct retrieval of locale from JS when meta tag is missing."""
     with patch.object(mock_driver, 'find_element', side_effect=Exception('Test Exception Meta')):
        with patch.object(mock_driver, 'get_page_lang', return_value="js_lang"):
            assert mock_driver.locale == 'js_lang'

def test_driver_locale_not_found(mock_driver):
    """Checks return None when locale not found in META and Javascript"""
    with patch.object(mock_driver, 'find_element', side_effect=Exception('Test Exception Meta')):
       with patch.object(mock_driver, 'get_page_lang', side_effect=Exception('Test Exception JS')):
        assert mock_driver.locale is None

def test_driver_get_url_success(mock_driver):
    """Checks successful navigation to URL."""
    assert mock_driver.get_url('https://newexample.com') == True
    assert mock_driver.driver.current_url == 'https://newexample.com'

def test_driver_get_url_webdriver_exception(mock_driver):
    """Checks handling of WebDriverException during get_url."""
    mock_driver.driver.get = MagicMock(side_effect=WebDriverException('Test WebDriver Error'))
    assert mock_driver.get_url('https://test.com') is False
    
def test_driver_get_url_invalid_argument_exception(mock_driver):
    """Checks handling of InvalidArgumentException during get_url."""
    mock_driver.driver.get = MagicMock(side_effect=InvalidArgumentException('Test Invalid Argument'))
    assert mock_driver.get_url('invalid_url') is False

def test_driver_get_url_other_exception(mock_driver):
    """Checks handling of other exceptions during get_url."""
    mock_driver.driver.get = MagicMock(side_effect=Exception('Test General Error'))
    assert mock_driver.get_url('https://test.com') is False
    
def test_driver_get_url_wait_ready_state(mock_driver):
     """Checks correct waiting of ready state during get_url."""
     mock_driver.driver.ready_state = 'loading'
     with patch.object(mock_driver, 'wait') as mock_wait:
          mock_driver.get_url('https://test.com')
          assert mock_wait.call_count > 0
          
def test_driver_get_url_same_url(mock_driver):
    """Checks that `previous_url` is not changed when navigating to the same URL."""
    current_url = mock_driver.current_url
    mock_driver.get_url(current_url)
    assert not hasattr(mock_driver, 'previous_url')

def test_driver_window_open_no_url(mock_driver):
    """Checks opening a new tab without URL."""
    with patch.object(mock_driver, 'execute_script') as mock_execute, \
         patch.object(mock_driver.driver.switch_to, 'window') as mock_switch_to:
        mock_driver.window_open()
        mock_execute.assert_called_with('window.open();')
        mock_switch_to.assert_called_with('handle2')

def test_driver_window_open_with_url(mock_driver):
    """Checks opening a new tab with URL."""
    with patch.object(mock_driver, 'execute_script') as mock_execute, \
         patch.object(mock_driver.driver.switch_to, 'window') as mock_switch_to, \
         patch.object(mock_driver, 'get_url') as mock_get_url:
        mock_driver.window_open('https://newtab.com')
        mock_execute.assert_called_with('window.open();')
        mock_switch_to.assert_called_with('handle2')
        mock_get_url.assert_called_with('https://newtab.com')
        
def test_driver_wait(mock_driver):
    """Checks the wait function."""
    with patch('time.sleep') as mock_sleep:
        mock_driver.wait(delay=0.5)
        mock_sleep.assert_called_with(0.5)

def test_driver_save_cookies_localy(mock_driver):
    """Checks that cookies are saved."""
    with patch('pickle.dump') as mock_dump:
        assert mock_driver._save_cookies_localy() == True # Debug condition

def test_driver_fetch_html_from_file(mock_driver):
    """Checks successful fetching of HTML from a local file."""
    with patch('builtins.open', mock_open_html('<html><body><h1>Test</h1></body></html>')) as mock_file:
        assert mock_driver.fetch_html('file://C:\\test.html') == True
        assert mock_driver.html_content == '<html><body><h1>Test</h1></body></html>'
        
def test_driver_fetch_html_file_not_found(mock_driver):
        """Checks handling of non-existent local files."""
        with patch('pathlib.Path.exists', return_value=False):
             assert mock_driver.fetch_html('file://C:\\notfound.html') is False
        
def test_driver_fetch_html_invalid_file_path(mock_driver):
    """Checks handling of invalid local file paths."""
    assert mock_driver.fetch_html('file://invalid_path') is False

def test_driver_fetch_html_file_read_error(mock_driver):
    """Checks handling of errors while reading a local file."""
    with patch('builtins.open', side_effect=Exception('Test File Read Error')):
         assert mock_driver.fetch_html('file://C:\\test.html') is False
    
def test_driver_fetch_html_from_url(mock_driver):
    """Checks successful fetching of HTML from a URL."""
    with patch.object(mock_driver, 'get_url', return_value=True):
        assert mock_driver.fetch_html('https://test.com') == True
        assert mock_driver.html_content == '<html><body><h1>Test Page</h1></body></html>'

def test_driver_fetch_html_from_url_error(mock_driver):
    """Checks handling of errors while fetching HTML from a URL."""
    with patch.object(mock_driver, 'get_url', return_value=False):
         assert mock_driver.fetch_html('https://test.com') is False

def test_driver_fetch_html_unsupported_protocol(mock_driver):
    """Checks handling of unsupported protocols."""
    assert mock_driver.fetch_html('ftp://test.com') is False
    
def mock_open_html(html_content):
    """
    Helper function to create a mock `open` object.
    """
    mock_file = MagicMock()
    mock_file.read.return_value = html_content
    mock_file.return_value.__enter__.return_value = mock_file
    return mock_file
```