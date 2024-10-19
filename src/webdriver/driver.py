## \file ../src/webdriver/driver.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" `WebDriver` 
@code
# Пример использования
from selenium.webdriver import Chrome
d = Driver(Chrome)
d.get_url('https://hypotez.com')-
@ebdcode
@html webdriver\\driver.md

@dotfile webdriver\\driver.dot
@image html webdriver.png
@include  webdriver\\_example_driver.py
"""


import copy
import pickle
import time
import re
from pathlib import Path
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (InvalidArgumentException, 
                                        ElementClickInterceptedException, 
                                        ElementNotInteractableException, 
                                        ElementNotVisibleException )
from src import gs
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException, WebDriverException

class Driver:
    """
    `Driver` Class for interacting with web browsers using Selenium WebDriver.

    This class provides a unified interface for different web drivers such as Chrome, Firefox, and Edge. 
    It includes methods for navigating to URLs, scrolling pages, extracting content, and handling cookies.

    Attributes:
        driver (selenium.webdriver): An instance of the WebDriver to control the browser.
    """

    def __init__(self, webdriver_cls, *args, **kwargs):
        """ Initializes the Driver class with the specified web driver.

        Args:
            webdriver_cls (type): A WebDriver class from `selenium.webdriver` such as `Chrome`, `Firefox`, or `Edge`.
            *args: Additional positional arguments passed to the WebDriver constructor.
            **kwargs: Additional keyword arguments passed to the WebDriver constructor.

        Returns:
            None: This method does not return any value.

        Raises:
            TypeError: If `webdriver_cls` is not a valid WebDriver class.
        """
        if not hasattr(webdriver_cls, 'get'):
            raise TypeError("`webdriver_cls` must be a valid WebDriver class.")
        self.driver = webdriver_cls(*args, **kwargs)

    def __getattr__(self, item):
        """ Proxy for accessing WebDriver attributes.

        Args:
            item (str): The attribute name to access.

        Returns:
            Any: The value of the attribute from the WebDriver instance.
        """
        return getattr(self.driver, item)



    def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
        """ Scrolls the web page.

        Args:
            scrolls (int, optional): Number of times to scroll. Defaults to 1.
            frame_size (int, optional): The scroll frame size in pixels. Defaults to 1800.
            direction (str, optional): Direction of scrolling. Possible values are 'both', 'down', 'up'. Defaults to 'both'.
            delay (float, optional): Delay in seconds between each scroll. Defaults to 0.3.

        Returns:
            bool: `True` if scrolling is successful, `False` otherwise.

        Raises:
            Exception: If an error occurs during scrolling.
        """
        def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
            """ Scrolls the screen up or down.

            Args:
                direction (str, optional): 'down', 'up', 'both'. Defaults to 'both'.
                scrolls (int, optional): Number of scroll frames. Defaults to 5.
                frame_size (int, optional): Frame size in pixels. Defaults to 1800.
                delay (float, optional): Delay in seconds between each scroll. Defaults to 1.

            Returns:
                bool: `True` if successful, `False` otherwise.

            Raises:
                Exception: If an error occurs during scrolling.
            """
            try:
                for i in range(scrolls):
                    self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                    self.wait(delay)
                return True
            except Exception as ex:
                logger.error("Error during scrolling", exc_info=ex)
                return False

        try:
            if direction == 'forward' or direction == 'down':
                return carousel('', scrolls, frame_size, delay)
            elif direction == 'backward' or direction == 'up':
                return carousel('-', scrolls, frame_size, delay)
            elif direction == 'both':
                if not carousel('', scrolls, frame_size, delay) or not carousel('-', scrolls, frame_size, delay):
                    return False
                return True


        except Exception as ex:
            logger.error("Error in scroll function", ex)
            return False

    @property
    def locale(self) -> Optional[str]:
        """ Attempts to determine the language of the page.

        Returns:
            Optional[str]: The language code if found, `None` otherwise.

        Raises:
            Exception: If an error occurs while determining the language.
        """
        try:
            meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
            return meta_language.get_attribute("content")
        except Exception as ex:
            logger.debug("Could not determine site language from META", ex)
            try:
                return self.get_page_lang()
            except Exception as ex:
                logger.debug("Could not determine site language from JavaScript", ex)
                return None

    def get_url(self, url: str) -> bool:
        """ Navigates to the specified URL and saves the current URL, previous URL, and cookies.

        Args:
            url (str): The URL to navigate to.

        Returns:
            bool: `True` if the transition is successful and the current URL matches the expected one, `False` otherwise.

        Raises:
            WebDriverException: If an error occurs with WebDriver operations.
            InvalidArgumentException: If the URL is invalid.
            Exception: For any other errors during navigation.
        """
        try:
            _previous_url = copy.copy(self.current_url)
        except Exception as ex:
            logger.error("Driver exception:", ex)
            return False
        
        try:
            self.driver.get(url)
            
            while self.get_ready_state() != 'complete':
                """ Wait until the whole page loads """

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
            logger.error(f'Error on url: {url}\n', ex)
            return False

    def fetch_html(self, url: str) -> Optional[bool]:
        """ Fetches HTML content from a file or URL and parses it with BeautifulSoup and XPath.

        Args:
            url (str): The file path or URL to fetch HTML content from.

        Returns:
            Optional[bool]: `True` on successful content retrieval, `None` otherwise.

        Raises:
            Exception: If an error occurs during content retrieval.
        """
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
                        logger.error('Exception while reading the file:', ex)
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
            logger.error('Invalid URL or file path:', url)
            return False
    
        return None

    def extract_body_text(self, url: str = '') -> str:
        """ Extracts and returns the text from the body of the HTML page using JavaScript executed via Selenium.

        Args:
            url (str, optional): The URL of the webpage to extract text from. If not provided, extracts from the current page.

        Returns:
            str: The extracted plain text from the body of the HTML page.

        Examples:
            >>> import header
            >>> d = Driver()
            >>>
            >>> # 1. Extract from a specific URL
            >>> text = d.extract_body_text('https://example.com')
            >>> print(text)
            >>> 
            >>> # 2. Extract from the current page
            >>> url = 'https://example2.com'
            >>> d.get(url)
            >>> text = d.extract_body_text()
            >>> print(text)
        """
        try:
            if url:
                self.get(url)

            script = """
            return document.body.innerText;
            """
            text = self.execute_script(script)
        except Exception as ex:
            logger.error(f"Error processing page text extraction: {ex}")
            text = ''
        return text

    def extract_domain(self, url: str) -> str:
        """ Extracts the domain name from the URL, removing the 'www' prefix if present.

        Args:
            url (str): The URL to extract the domain from.

        Returns:
            str: Domain name without 'www' prefix.

        Raises:
            ValueError: If the URL is malformed.
        """
        if "://" in url:
            url = url.split("://")[1]

        domain = url.split('/')[0]

        if domain.startswith('www.'):
            domain = domain[4:]

        return domain  

    def _save_cookies_localy(self, to_file: Optional[str | Path] = None) -> bool:
        """ Saves cookies to a local file.

        Args:
            to_file (Optional[str | Path], optional): Path to the file where cookies will be saved. Defaults to None.

        Returns:
            bool: `True` if cookies are successfully saved, `False` otherwise.

        Raises:
            Exception: If an error occurs while saving cookies.
        """
        return True # <- debug без куки
        if not to_file:
            to_file = Path(gs.path.google_drive / 'cookies' / self.driver_name / self.extract_domain(self.current_url) / 'cookie')
        
        directory = to_file.parent
        if not directory.exists():
            directory.mkdir(parents=True)

        try:
            cookies = self.get_cookies()
        except Exception as ex:
            logger.debug("Error getting cookies", ex, True)
            return False
            
        try:
            with open(to_file, 'wb') as file:
                pickle.dump(cookies, file)
        except Exception as ex:
            logger.debug("Cookie local file was not saved", ex)
            return False
    
        return True

    def page_refresh(self) -> bool:
        """ Refreshes the page and waits for it to fully reload.

        Returns:
            bool: `True` if the page refresh is successful, `False` otherwise.

        Raises:
            Exception: If an error occurs during page refresh.
        """
        return self.get_url(self.current_url)

    def window_focus(self) -> None:
        """ Returns focus to the page (removes focus from the element).

        Returns:
            None: This method does not return any value.

        Raises:
            Exception: If an error occurs while returning focus.
        """
        self.get_ready_state()

    def wait(self, interval: float = 0) -> None:
        """ Waits for a specified time interval.

        Args:
            interval (float, optional): The time interval to wait in seconds. Defaults to 0.

        Returns:
            None: This method does not return any value.
        """
        time.sleep(interval)
