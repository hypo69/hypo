```rst
.. module:: src.webdriver.driver
```
[Русский](https://github.com/hypo69/hypo/blob/master/src/webdriver/driver.ru.md)

## Explanation of the `driver.py` Module Code

### Overview

The `driver.py` module is designed to work with Selenium web drivers. The primary purpose of the `Driver` class is to provide a unified interface for interacting with Selenium web drivers. The class offers methods for driver initialization, navigation, cookie management, exception handling, and other operations.

### Key Functions

1. **Driver Initialization**: Creating an instance of the Selenium WebDriver.
2. **Navigation**: Navigating to URLs, scrolling, and extracting content.
3. **Cookie Management**: Saving and managing cookies.
4. **Exception Handling**: Logging errors.

### `Driver` Class

#### Initialization

```python
class Driver:
    def __init__(self, webdriver_cls, *args, **kwargs):
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError('`webdriver_cls` must be a valid WebDriver class.')
        self.driver = webdriver_cls(*args, **kwargs)
```

- **Arguments**:
  - `webdriver_cls`: WebDriver class (e.g., Chrome, Firefox).
  - `*args`, `**kwargs`: Positional and keyword arguments for driver initialization.

- **Validation**: Checks if `webdriver_cls` is a valid WebDriver class.

#### Subclasses

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    super().__init_subclass__(**kwargs)
    if browser_name is None:
        raise ValueError(f'Class {cls.__name__} must specify the `browser_name` argument.')
    cls.browser_name = browser_name
```

- **Purpose**: Automatically called when creating a subclass of `Driver`.
- **Arguments**:
  - `browser_name`: Browser name.
  - `**kwargs`: Additional arguments.

#### Accessing Driver Attributes

```python
def __getattr__(self, item):
    return getattr(self.driver, item)
```

- **Purpose**: Proxy for accessing driver attributes.
- **Arguments**:
  - `item`: Attribute name.

#### Scrolling the Page

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
        try:
            for _ in range(scrolls):
                self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                self.wait(delay)
            return True
        except Exception as ex:
            logger.error('Error while scrolling', exc_info=ex)
            return False

    try:
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
    except Exception as ex:
        logger.error('Error in scroll function', ex)
        return False
```

- **Purpose**: Scrolls the page in the specified direction.
- **Arguments**:
  - `scrolls`: Number of scrolls.
  - `frame_size`: Scroll size in pixels.
  - `direction`: Direction ('both', 'down', 'up').
  - `delay`: Delay between scrolls.

#### Determining Page Language

```python
@property
def locale(self) -> Optional[str]:
    try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
    except Exception as ex:
        logger.debug('Failed to determine site language from META', ex)
        try:
            return self.get_page_lang()
        except Exception as ex:
            logger.debug('Failed to determine site language from JavaScript', ex)
            return
```

- **Purpose**: Determines the page language based on meta tags or JavaScript.
- **Returns**: Language code if found, otherwise `None`.

#### Navigating to a URL

```python
def get_url(self, url: str) -> bool:
    try:
        _previous_url = copy.copy(self.current_url)
    except Exception as ex:
        logger.error("Error getting current URL", ex)
        return False
    
    try:
        self.driver.get(url)
        
        while self.ready_state != 'complete':
            """ Wait for the page to finish loading """

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
        logger.error(f'Error navigating to URL: {url}\n', ex)
        return False
```

- **Purpose**: Navigates to the specified URL and saves the current URL, previous URL, and cookies.
- **Arguments**:
  - `url`: URL to navigate to.
- **Returns**: `True` if the navigation is successful and the current URL matches the expected URL, `False` otherwise.

#### Opening a New Tab

```python
def window_open(self, url: Optional[str] = None) -> None:
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

- **Purpose**: Opens a new tab in the current browser window and switches to it.
- **Arguments**:
  - `url`: URL to open in the new tab.

#### Waiting

```python
def wait(self, delay: float = .3) -> None:
    time.sleep(delay)
```

- **Purpose**: Waits for the specified amount of time.
- **Arguments**:
  - `delay`: Delay time in seconds.

#### Saving Cookies Locally

```python
def _save_cookies_localy(self) -> None:
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Error saving cookies:', ex)
```

- **Purpose**: Saves the current web driver cookies to a local file.

#### Fetching HTML Content

```python
def fetch_html(self, url: str) -> Optional[bool]:
    if url.startswith('file://'):
        cleaned_url = url.replace('file://', '')
        match = re.search(r'[a-zA-Z]:[\/].*', cleaned_url)
        if match:
            file_path = Path(match.group(0))
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.html_content = file.read()
                    return True
                except Exception as ex:
                    logger.error('Error reading file:', ex)
                    return False
            else:
                logger.error('Local file not found:', file_path)
                return False
        else:
            logger.error('Invalid file path:', cleaned_url)
            return False
    elif url.startswith('http://') or url.startswith('https://'):
        try:
            if self.get_url(url):
                self.html_content = self.page_source
                return True
        except Exception as ex:
            logger.error(f"Error fetching {url}:", ex)
            return False
    else:
        logger.error("Error: Unsupported protocol for URL:", url)
        return False
```

- **Purpose**: Fetches HTML content from a file or web page.
- **Arguments**:
  - `url`: File path or URL to fetch HTML content from.
- **Returns**: `True` if the content is successfully fetched, otherwise `None`.

### Example Usage

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
driver.get_url('https://example.com')
```

### Conclusion

The `Driver` class provides a unified interface for working with Selenium web drivers, simplifying navigation, cookie management, exception handling, and other operations. This class is useful for web scraping and testing automation.