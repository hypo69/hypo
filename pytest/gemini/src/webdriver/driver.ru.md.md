```python
import pytest
from unittest.mock import MagicMock
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from selenium.webdriver.common.by import By
from pathlib import Path
import logging
import copy
import time
import pickle
import re
from typing import Optional

# Mocking necessary external dependencies
logger = MagicMock()
gs = MagicMock()
gs.cookies_filepath = "test_cookies.pkl"


class MockWebElement:
    def __init__(self, tag_name, attributes=None, text=''):
      self.tag_name = tag_name
      self.attributes = attributes if attributes else {}
      self.text = text

    def get_attribute(self, item):
        return self.attributes.get(item)
    
    def get_property(self, item):
      return self.attributes.get(item)
    
    def is_enabled(self):
      return True

    def click(self):
        return True

class MockWebDriver(WebDriver):
    def __init__(self, *args, **kwargs):
        self.current_url = "initial_url"
        self.page_source = "<html><head></head><body>Test Page</body></html>"
        self.window_handles = ['window1']
        self.ready_state = "complete"
        self.mock_cookies = {}
        self.attributes = {}

    def get(self, url):
        self.current_url = url
        self.page_source = f"<html><head></head><body>Content for {url}</body></html>"
    
    def execute_script(self, script):
        if "window.scrollBy" in script:
            pass
        if "window.open" in script:
          self.window_handles.append('window2')

    def find_element(self, by, value):
        if by == By.CSS_SELECTOR and value == "meta[http-equiv='Content-Language']":
            return MockWebElement(tag_name="meta", attributes={'content': 'en'})
        return MockWebElement(tag_name='div')
    
    def find_elements(self, by, value):
      return [MockWebElement(tag_name='div')]
    
    def get_cookies(self):
      return self.mock_cookies

    def add_cookie(self, cookie):
        self.mock_cookies[cookie['name']] = cookie
        
    def delete_all_cookies(self):
      self.mock_cookies = {}

    @property
    def title(self):
      return 'Test Page'
    
    @property
    def text(self):
      return 'Test Text'
    
    def switch_to_window(self, window_handle):
      pass
    
    def quit(self):
        pass
    
    def start_client(self):
      pass
    
    def stop_client(self):
      pass

    
class Driver:
    def __init__(self, webdriver_cls, *args, **kwargs):
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` должен быть допустимым классом WebDriver.')
        self.driver = webdriver_cls(*args, **kwargs)
        self.previous_url = None
        self.html_content = None
    
    def __init_subclass__(cls, *, browser_name=None, **kwargs):
      super().__init_subclass__(**kwargs)
      if browser_name is None:
        raise ValueError(f'Класс {cls.__name__} должен указать аргумент `browser_name`.')
      cls.browser_name = browser_name

    def __getattr__(self, item):
        return getattr(self.driver, item)

    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            try:
                for _ in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error('Ошибка при прокрутке', exc_info=ex)
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
        except Exception as ex:
            logger.error('Ошибка в функции прокрутки', ex)
            return False
    
    @property
    def locale(self) -> Optional[str]:
      try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
      except Exception as ex:
        logger.debug('Не удалось определить язык сайта из META', ex)
        try:
          return self.get_page_lang()
        except Exception as ex:
          logger.debug('Не удалось определить язык сайта из JavaScript', ex)
          return

    def get_url(self, url: str) -> bool:
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Ошибка при получении текущего URL", ex)
            return False
        
        try:
            self.driver.get(url)
            
            while self.ready_state != 'complete':
                """ Ожидаем завершения загрузки страницы """

            if url != _previous_url:
                self.previous_url = _previous_url

            self._save_cookies_localy()
            return True
            
        except WebDriverException as ex:
            logger.error('WebDriverException', ex)
            return False

        except InvalidArgumentException as ex:
            logger.error(f"InvalidArgumentException {url}", ex)
            return False
        except Exception as ex:
            logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
            return False

    def window_open(self, url: Optional[str] = None) -> None:
        self.execute_script('window.open();')
        self.switch_to.window(self.window_handles[-1])
        if url:
            self.get(url)

    def wait(self, delay: float = .3) -> None:
      time.sleep(delay)

    def _save_cookies_localy(self) -> None:
      return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
      try:
          with open(gs.cookies_filepath, 'wb') as cookiesfile:
              pickle.dump(self.driver.get_cookies(), cookiesfile)
      except Exception as ex:
          logger.error('Ошибка при сохранении куки:', ex)

    def fetch_html(self, url: str) -> Optional[bool]:
        if url.startswith('file://'):
            cleaned_url = url.replace('file://', '')
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Ошибка при чтении файла:', ex)
                        return False
                else:
                    logger.error('Локальный файл не найден:', file_path)
                    return False
            else:
                logger.error('Некорректный путь к файлу:', cleaned_url)
                return False
        elif url.startswith('http://') or url.startswith('https://'):
            try:
                if self.get_url(url):
                    self.html_content = self.page_source
                    return True
            except Exception as ex:
                logger.error(f"Ошибка при получении {url}:", ex)
                return False
        else:
            logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
            return False

# Fixture for Driver class
@pytest.fixture
def mock_driver():
    return Driver(MockWebDriver)

# Tests for Driver.__init__
def test_driver_init_valid_webdriver():
    """Checks if the driver initializes correctly with a valid webdriver class."""
    driver = Driver(MockWebDriver)
    assert isinstance(driver.driver, MockWebDriver)

def test_driver_init_invalid_webdriver():
    """Checks if TypeError is raised when webdriver_cls is not valid."""
    with pytest.raises(TypeError, match='`webdriver_cls` должен быть допустимым классом WebDriver.'):
        Driver(object)

# Tests for Driver.__init_subclass__
def test_driver_init_subclass_valid():
    """Checks if the subclass initializes correctly with a browser_name."""
    class SubDriver(Driver, browser_name="chrome"):
        pass
    assert SubDriver.browser_name == "chrome"

def test_driver_init_subclass_invalid():
    """Checks if ValueError is raised when browser_name is not provided."""
    with pytest.raises(ValueError, match='Класс SubDriver должен указать аргумент `browser_name`.') :
        class SubDriver(Driver):
            pass

# Tests for Driver.__getattr__
def test_driver_getattr(mock_driver):
    """Checks if attributes are correctly proxied to the webdriver instance."""
    mock_driver.start_client()
    assert hasattr(mock_driver, 'start_client')
    assert mock_driver.title == 'Test Page'
    assert mock_driver.text == 'Test Text'

# Tests for Driver.scroll
def test_driver_scroll_forward(mock_driver):
    """Checks if forward scroll works correctly."""
    assert mock_driver.scroll(direction='forward') is True

def test_driver_scroll_backward(mock_driver):
    """Checks if backward scroll works correctly."""
    assert mock_driver.scroll(direction='backward') is True

def test_driver_scroll_both(mock_driver):
    """Checks if both directions scroll works correctly."""
    assert mock_driver.scroll(direction='both') is True

def test_driver_scroll_invalid_direction(mock_driver):
  """Checks if an invalid direction does not cause errors, returning False due to exception"""
  assert mock_driver.scroll(direction='invalid') is False

# Tests for Driver.locale
def test_driver_locale_meta(mock_driver):
  """Checks if locale is extracted correctly from meta tag."""
  assert mock_driver.locale == "en"

def test_driver_locale_no_meta(mock_driver):
  """Checks if locale extraction returns None when no meta and js return no result."""
  mock_driver.find_element = MagicMock(side_effect=Exception('No meta'))
  mock_driver.get_page_lang = MagicMock(side_effect=Exception('No js'))
  assert mock_driver.locale is None

# Tests for Driver.get_url
def test_driver_get_url_valid(mock_driver):
    """Checks if get_url navigates successfully and saves previous url."""
    url = "https://example.com"
    assert mock_driver.get_url(url) is True
    assert mock_driver.current_url == url
    assert mock_driver.previous_url == "initial_url"

def test_driver_get_url_webdriver_exception(mock_driver):
    """Checks if get_url handles WebDriverException correctly."""
    mock_driver.driver.get = MagicMock(side_effect=WebDriverException("Webdriver error"))
    url = "https://example.com"
    assert mock_driver.get_url(url) is False
    assert mock_driver.previous_url is None

def test_driver_get_url_invalid_argument_exception(mock_driver):
    """Checks if get_url handles InvalidArgumentException correctly."""
    mock_driver.driver.get = MagicMock(side_effect=InvalidArgumentException("Invalid argument"))
    url = "invalid_url"
    assert mock_driver.get_url(url) is False
    assert mock_driver.previous_url is None

def test_driver_get_url_generic_exception(mock_driver):
    """Checks if get_url handles a generic exception correctly."""
    mock_driver.driver.get = MagicMock(side_effect=Exception("Generic error"))
    url = "https://example.com"
    assert mock_driver.get_url(url) is False
    assert mock_driver.previous_url is None
    
def test_driver_get_url_current_url_exception(mock_driver):
    """Checks if get_url handles an exception when getting the current url"""
    mock_driver.current_url = MagicMock(side_effect=Exception("Generic error"))
    url = "https://example.com"
    assert mock_driver.get_url(url) is False
    assert mock_driver.previous_url is None

def test_driver_get_url_same_url(mock_driver):
    """Checks if previous url is not overwritten if current url is the same"""
    url = "https://example.com"
    mock_driver.get_url(url)
    mock_driver.previous_url = 'previous_url' # simulate setting previous url before
    mock_driver.get_url(url) # navigate to same url
    assert mock_driver.previous_url == 'previous_url'

# Tests for Driver.window_open
def test_driver_window_open_no_url(mock_driver):
    """Checks if window_open opens a new tab without a URL."""
    mock_driver.window_open()
    assert len(mock_driver.window_handles) == 2

def test_driver_window_open_with_url(mock_driver):
    """Checks if window_open opens a new tab with a URL."""
    url = "https://example.com"
    mock_driver.window_open(url)
    assert len(mock_driver.window_handles) == 2
    assert mock_driver.current_url == url

# Tests for Driver.wait
def test_driver_wait(mock_driver):
    """Checks if wait pauses execution for the specified time."""
    start_time = time.time()
    mock_driver.wait(delay=0.1)
    end_time = time.time()
    assert end_time - start_time >= 0.1

# Tests for Driver._save_cookies_localy
def test_driver_save_cookies_localy(mock_driver):
    """Checks if _save_cookies_localy does not raise exception."""
    assert mock_driver._save_cookies_localy() is True

# Tests for Driver.fetch_html
def test_driver_fetch_html_file_valid(mock_driver, tmp_path):
  """Checks if fetch_html can read from a local file."""
  test_file = tmp_path / "test.html"
  test_file.write_text("<html><body>Test Content</body></html>", encoding='utf-8')
  url = f"file://{str(test_file)}"
  assert mock_driver.fetch_html(url) is True
  assert mock_driver.html_content == "<html><body>Test Content</body></html>"

def test_driver_fetch_html_file_not_found(mock_driver, tmp_path):
  """Checks if fetch_html handles a non-existent local file."""
  file_path = tmp_path / "non_existent.html"
  url = f"file://{str(file_path)}"
  assert mock_driver.fetch_html(url) is False
  assert mock_driver.html_content is None

def test_driver_fetch_html_file_invalid_path(mock_driver):
  """Checks if fetch_html handles invalid file paths."""
  url = "file://invalid_file_path"
  assert mock_driver.fetch_html(url) is False
  assert mock_driver.html_content is None

def test_driver_fetch_html_file_exception(mock_driver, tmp_path):
  """Checks if fetch_html handles exceptions during file reading."""
  test_file = tmp_path / "test.html"
  test_file.write_text("<html><body>Test Content</body></html>", encoding='utf-8')
  url = f"file://{str(test_file)}"
  mock_open = MagicMock(side_effect=Exception('Test exception'))
  with  pytest.MonkeyPatch().context() as mp:
    mp.setattr("builtins.open", mock_open)
    assert mock_driver.fetch_html(url) is False
    assert mock_driver.html_content is None

def test_driver_fetch_html_http_valid(mock_driver):
    """Checks if fetch_html can retrieve HTML from an HTTP URL."""
    url = "http://example.com"
    assert mock_driver.fetch_html(url) is True
    assert mock_driver.html_content == f"<html><head></head><body>Content for {url}</body></html>"

def test_driver_fetch_html_https_valid(mock_driver):
    """Checks if fetch_html can retrieve HTML from an HTTPS URL."""
    url = "https://example.com"
    assert mock_driver.fetch_html(url) is True
    assert mock_driver.html_content == f"<html><head></head><body>Content for {url}</body></html>"

def test_driver_fetch_html_http_exception(mock_driver):
  """Checks if fetch_html handles an exception during http request."""
  mock_driver.get_url = MagicMock(side_effect=Exception('Test exception'))
  url = "http://example.com"
  assert mock_driver.fetch_html(url) is False
  assert mock_driver.html_content is None

def test_driver_fetch_html_unsupported_protocol(mock_driver):
    """Checks if fetch_html handles an unsupported URL protocol."""
    url = "ftp://example.com"
    assert mock_driver.fetch_html(url) is False
    assert mock_driver.html_content is None
```