## File hypotez/src/webdriver/bs/bs.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.webdriver.bs 
	:platform: Windows, Unix
	:synopsis: parse pages with `BeautifulSoup` and XPath 
```python
if __name__ == "__main__":
    driver = Driver()
    # For file
    driver.get_url('path/to/your/file.html')
    # For URL
    driver.get_url('https://example.com')
    driver.execute_locator(locator)
```

"""
MODE = 'dev'


import re
from math import log
from bs4 import BeautifulSoup
from types import SimpleNamespace
from lxml import etree
import requests
from pathlib import Path
from src import gs
from src.webdriver import Driver
from src.logger import logger

class BS:
    
    html_content:str
    def __init__(self, url:str|None=None):
        """"""
        self.html_content = url


    def get_url(self, url: str):
        """ Fetch HTML content from a file or URL and parse it with BeautifulSoup and XPath

        @param url: The file path or URL to fetch HTML content from
        """

        if url.startswith('file://'):
            # Remove 'file://' prefix and clean up the path
            cleaned_url = url.replace(r'file:///', '')
            
            # Extract the Windows path if it's in the form of 'c:/... or 'C:/...'
            match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
            if match:
                file_path = Path(match.group(0))
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            self.html_content = file.read()
                        return True
                    except Exception as ex:
                        logger.error('Exception while reading the file:', ex)
                        ...
                else:
                    logger.error('Local file not found:', file_path)
                    ...
            else:
                logger.error('Invalid file path:', cleaned_url)
                ...
        elif url.startswith('https://'):
            # Handle web URLs
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check for HTTP request errors
                self.html_content = response.text
                return True
            except requests.RequestException as ex:
                logger.error(f"Error fetching {url}:", ex)
                ...
        else:
            logger.error('Invalid URL or file path:', url)
            ...
        


    def execute_locator(self,locator:SimpleNamespace|dict, url: str = None):
        """ мини версия экзкьютора вебдрайвера `Driver` (`src.webdriver.executor`)"""
        ...
        if url:
            self.get_url(url)
            
        soup = BeautifulSoup(self.html_content, 'lxml')
        tree = etree.HTML(str(soup))  # Convert BeautifulSoup object to lxml tree
        attribute = locator.attribute
        by = locator.by
        selector = locator.selector
        elements = None
        
        if by.upper() == 'ID':
            elements = tree.xpath(f'//*[@id="{attribute}"]')
        elif by.upper() == 'CSS':
            elements = tree.xpath(f'//*[contains(@class, "{attribute}")]')
        elif by.upper() == 'TEXT':
            elements = tree.xpath(f'//input[@type="{attribute}"]')
         ## @todo: - это костыль, а не логика"""
        else:
            ...
            elements = tree.xpath(selector)
            
        return elements
    
if __name__ == "__main__":
    driver = Driver()
    # For file
    driver.get_url('path/to/your/file.html')
    # For URL
    driver.get_url('https://example.com')
    locator:SimpleNamespace
    driver.execute_locator(locator)
```

```
<algorithm>
**Step 1:**  Initialization (Class BS)
    * Input: Optional `url` (file path or URL).
    * Output: `BS` object with `html_content` initialized (if `url` is provided).
    * Example: `bs_object = BS('https://example.com')` (populates `html_content`)


**Step 2:** `get_url` Method
    * Input: `url` (string).
    * Output: Boolean (True on success, False/Errors logged otherwise).
    * Logical Blocks:
        * **File Path Check (file://):**
            * Extracts Windows path from `url`.
            * Checks if file exists using `Path.exists()`.
            * Reads file content and updates `html_content`.
            * Logs errors (file not found, invalid path) to `logger`.
        * **HTTP URL Check (https://):**
            * Fetches `url` content using `requests.get()`.
            * Checks for errors in the HTTP request using `response.raise_for_status()`.
            * Updates `html_content` with response text.
            * Logs error if request fails.
        * **Error handling:**
            * Logs errors for unsupported protocols.

**Step 3:** `execute_locator` Method
    * Input: `locator` (SimpleNamespace or dict, containing attributes like 'attribute', 'by', 'selector') and `url` (optional).
    * Output: List of elements (`elements`) found by the locator (XPath results), or None if no elements match.
    * Logical Blocks:
        * **Handle optional `url`:** if url is provided, calls the get_url function to update html_content.
        * **Parsing with BeautifulSoup:** Converts `html_content` to a BeautifulSoup object for easy HTML parsing.
        * **Conversion to lxml Tree:** Creates an lxml ElementTree from BeautifulSoup object.
        * **Locator Matching:** Determines locator type (`ID`, `CSS`, `TEXT`) and constructs the appropriate XPath query to find the elements.
        * **XPath Query:** Uses `tree.xpath` to search the lxml tree based on the locator's attributes.
        * **Return Result:** Returns `elements` (list of found elements) or logs errors and returns `None`.
        * **Error Handling:** Error handling for incorrect locator type.



```

```
<explanation>

**Imports:**

* `re`: Regular expressions for parsing file paths.
* `math`: Used (log)  but not directly applied in this file.
* `bs4`: Beautiful Soup for parsing HTML/XML content.
* `types`:  `SimpleNamespace` for creating objects with attributes (e.g., locators).
* `lxml`: lxml library (etree) for XPath querying.
* `requests`: For fetching HTML content from URLs.
* `pathlib`: For working with file paths (using Path objects).
* `src.gs`: Likely another module (hypothesized package) for general-purpose functions (not used directly here).
* `src.webdriver.Driver`: Probably a class that represents a web driver object, to work with the browser.
* `src.logger`:  For logging messages (error and info). This module likely defines a custom logging setup.

**Classes:**

* `BS`: This class provides methods to fetch and parse HTML content from files or URLs, and locate elements using XPath.
    * `html_content`: The attribute to hold the parsed HTML content.
    * `__init__`: Initializes the `html_content` attribute (optional parameter `url`).
    * `get_url`: Fetches HTML content from a given URL or file path.
    * `execute_locator`: Executes a locator to locate elements, using the stored html content.

**Functions:**

* `get_url`:
    * Arguments: `url` (string, the file or URL).
    * Returns: `True` on success, potentially logs errors and returns nothing.
    *  Purpose: Reads HTML content from either a file or a URL.
* `execute_locator`:
    * Arguments: `locator` (a SimpleNamespace/dict object defining the locator's attributes) and `url` (optional).
    * Returns: `elements` (list of found elements) or `None`.
    * Purpose: Locates elements in the HTML content using XPath.

**Variables:**

* `MODE`:  A constant defining the operating mode, likely 'dev' or 'prod'.
* `locator`: Variable used in `if __name__ == "__main__":`. This is declared in the main block but not assigned. (Should be initialized.)


**Potential Errors and Improvements:**

* The `@todo` comment indicates that the `execute_locator` method's handling of different locator types is incomplete.  This function should include a more comprehensive selection of locator types beyond `ID`, `CSS`, and `TEXT`.
*  Error handling in `get_url` is somewhat basic. Improve logging and error messages.
* The `if __name__ == "__main__"` block is used to run test cases, which is correct. However, the `locator` variable is used without being assigned. This block should be updated to correctly initialize a valid locator object before passing to `execute_locator`.
* The `...` placeholders throughout the code require more concrete implementation. They need to be replaced with the actual logic for handling different cases.


**Relationships:**

The `bs.py` script relies on classes and functions from other modules, indicated by the imports: `gs` (likely for general-purpose functions), `Driver` (for web driver interactions), and `logger` (for logging). The relationships indicate that this module acts as a bridge for interacting with HTML content and with a wider system by working with `Driver`.