[Русский](https://github.com/hypo69/hypo/blob/master/README.RU.MD)
### Module Overview: Executor via WebDriver

**Description:**
The module provides an execution framework for navigating and interacting with web pages using a WebDriver. It processes scripts and locators to perform automated actions on web elements.

**Main Features:**
- Executes navigation algorithms specified in script files.
- Executes interaction algorithms with the page specified in locator files.

**Functionality:**

1. **Locator Handling:**
   - **Initialization:** The `ExecuteLocator` class is initialized with a WebDriver instance and an optional list of arguments and keyword arguments. It sets up the WebDriver and the action chains for interacting with web elements.
   - **Locator Execution:** The `execute_locator` method processes the locator dictionary, which contains information about how to find and interact with web elements. It handles different types of locators and actions based on the configuration provided.
   - **Element Retrieval:** The `get_webelement_by_locator` method retrieves web elements based on the locator information, such as XPATH, ID, or CSS selectors. It waits for elements to be present and can return a single element, a list of elements, or `False` if none are found.
   - **Attribute Retrieval:** The `get_attribute_by_locator` method retrieves attributes from elements found using the locator. It supports both single and multiple elements.
   - **Message Sending:** The `send_message` method sends text input to web elements. It supports typing simulation with configurable typing speed and optional mouse interaction.

2. **Screenshots:**
   - **Element Screenshot:** The `get_webelement_as_screenshot` method takes a screenshot of a web element and returns it as a PNG image. It supports capturing screenshots of multiple elements and handles errors if elements are no longer present in the DOM.

3. **Click Action:**
   - **Element Click:** The `click` method performs a click action on a web element identified by the locator. It handles cases where the click results in navigation to a new page or opens a new window, and it logs errors if the click fails.

4. **Locator Evaluation:**
   - **Attribute Evaluation:** The `evaluate_locator` method evaluates locator attributes, including handling special cases where attributes are represented as placeholders (e.g., `%EXTERNAL_MESSAGE%`).

**Error Handling:**
- The module uses try-except blocks to catch and log errors during various operations, such as finding elements, sending messages, and taking screenshots. Specific exceptions like `NoSuchElementException` and `TimeoutException` are caught to handle cases where elements are not found or time out.

**Usage:**
- **Initialization:** Create an instance of `ExecuteLocator` with a WebDriver instance.
- **Execute Locator:** Call the `execute_locator` method with a locator dictionary to perform actions or retrieve data from web elements.
- **Handle Results:** Use methods like `get_webelement_by_locator`, `send_message`, and `get_webelement_as_screenshot` to interact with web elements and process results.

**Dependencies:**
- The module relies on Selenium for WebDriver operations, including finding elements, sending keys, and interacting with web pages. It also uses Python's built-in libraries for exception handling and time management.

---

Feel free to adjust any specifics or add more details based on the actual implementation and requirements.
```python
# -*- coding: utf-8 -*-

""" Examples for using `Driver` and `Chrome` classes """

from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    """ Main function to demonstrate usage examples for Driver and Chrome """

    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

### Module Overview: `Driver`

**Description:**
The `Driver` module provides a dynamic WebDriver implementation that integrates common WebDriver functionalities with additional methods for interacting with web pages, handling JavaScript, and managing cookies. It leverages Selenium's WebDriver capabilities and custom extensions to support various web automation tasks.

**Main Features:**
- Inherits from a specified WebDriver class (e.g., Chrome, Firefox, Edge) and adds additional functionality.
- Includes methods for scrolling, handling cookies, interacting with web elements, and executing JavaScript.
- Provides utilities for managing browser windows and page interactions.

**Components:**

1. **DriverBase Class:**
   - **Attributes:**
     - `previous_url`: Stores the previous URL.
     - `referrer`: Stores the referrer URL.
     - `page_lang`: Stores the language of the page.
     - Various attributes related to interacting with web elements and executing JavaScript.

   - **Methods:**
     - `scroll`: Scrolls the web page in the specified direction. Supports scrolling forward, backward, or both.
     - `locale`: Attempts to determine the language of the page by checking meta tags or using JavaScript.
     - `get_url`: Loads the specified URL.
     - `extract_domain`: Extracts the domain from a URL.
     - `_save_cookies_localy`: Saves cookies to a local file.
     - `page_refresh`: Refreshes the current page.
     - `window_focus`: Focuses the browser window using JavaScript.
     - `wait`: Waits for a specified interval.

2. **DriverMeta Class:**
   - **Methods:**
     - `__call__`: Creates a new `Driver` class that combines the specified WebDriver class (e.g., Chrome, Firefox, Edge) with `DriverBase`. Initializes JavaScript methods and locator execution functionalities.

3. **Driver Class:**
   - **Description:**
     - A dynamically created WebDriver class that inherits from both `DriverBase` and the specified WebDriver class.
   - **Usage Example:**
     - ```python
       from src.webdriver.driver import Driver, Chrome, Firefox, Edge
       d = Driver(Chrome)
       ```

**Usage:**
- **Initialization:** Create an instance of `Driver` with a specific WebDriver class.
- **Functionality:** Use methods such as `scroll`, `get_url`, `extract_domain`, and `page_refresh` to interact with web pages. The class also provides methods for JavaScript execution and cookie management.

**Dependencies:**
- **Selenium:** Used for WebDriver operations including finding elements, scrolling, and interacting with web pages.
- **Python Libraries:** Includes `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse`, and others for various functionalities.

---

Feel free to customize or expand this overview based on any additional specifics or details about your module's functionality.
### Примеры использования классов и методов

- **Создание экземпляра Chrome драйвера и навигация по URL:**

  ```python
  chrome_driver = Driver(Chrome)
  if chrome_driver.get_url("https://www.example.com"):
      print("Successfully navigated to the URL")
  ```

- **Извлечение домена из URL:**

  ```python
  domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
  print(f"Extracted domain: {domain}")
  ```

- **Сохранение cookies в локальный файл:**

  ```python
  success = chrome_driver._save_cookies_localy()
  if success:
      print("Cookies were saved successfully")
  ```

- **Обновление текущей страницы:**

  ```python
  if chrome_driver.page_refresh():
      print("Page was refreshed successfully")
  ```

- **Прокрутка страницы вниз:**

  ```python
  if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
      print("Successfully scrolled the page down")
  ```

- **Получение языка текущей страницы:**

  ```python
  page_language = chrome_driver.locale
  print(f"Page language: {page_language}")
  ```

- **Установка кастомного User-Agent для Chrome драйвера:**

  ```python
  user_agent = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }
  custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
  if custom_chrome_driver.get_url("https://www.example.com"):
      print("Successfully navigated to the URL with custom user agent")
  ```

- **Поиск элемента по CSS селектору:**

  ```python
  element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
  if element:
      print(f"Found element with text: {element.text}")
  ```

- **Получение текущего URL:**

  ```python
  current_url = chrome_driver.current_url
  print(f"Current URL: {current_url}")
  ```

- **Фокусировка окна, чтобы убрать фокус с элемента:**

  ```python
  chrome_driver.window_focus()
  print("Focused the window")
  ```

### Примечания

- Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.


The `executor.py` file in the `src.webdriver` module contains the `ExecuteLocator` class, which is designed for performing various actions on web page elements using Selenium WebDriver. Let’s break down the main components and functions of this class:

## General Structure and Purpose

### Main Purpose

The `ExecuteLocator` class is designed to execute navigation algorithms and interactions with a web page based on configuration data provided in the form of locator dictionaries.

### Main Components

1. **Imports and Dependencies**

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.keys import Keys
   from selenium.webdriver.common.by import By
   from selenium.webdriver.remote.webelement import WebElement
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.common.action_chains import ActionChains
   from selenium.common.exceptions import NoSuchElementException, TimeoutException

   from src import gs 
   from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
   
   from src.logger.logger import logger
   from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
   ```

   Here, essential libraries and modules are imported, including Selenium WebDriver for interacting with web pages, and internal modules for settings, logging, and exception handling.

2. **Class `ExecuteLocator`**

   The `ExecuteLocator` class is the core component of this file and contains methods for performing actions on web elements and handling locators. Let’s look at its methods and attributes in more detail.

### Class Attributes

- **`driver`**: A reference to the WebDriver instance used for browser interactions.
- **`actions`**: An `ActionChains` instance for performing complex actions on web page elements.
- **`by_mapping`**: A dictionary that maps string representations of locators to Selenium `By` objects.

### Class Methods

1. **`__init__(self, driver, *args, **kwargs)`**

   The class constructor initializes the WebDriver and `ActionChains`:

   ```python
   def __init__(self, driver, *args, **kwargs):
       self.driver = driver
       self.actions = ActionChains(driver)
   ```

2. **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

   The main method for performing actions based on the locator:

   ```python
   def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
       ...
   ```

   - **`locator`**: A dictionary with parameters for performing actions.
   - **`message`**: A message to send if needed.
   - **`typing_speed`**: Typing speed for sending messages.
   - **`continue_on_error`**: A flag indicating whether to continue execution if an error occurs.

   This method selects which actions to perform based on the locator configuration.

3. **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

   Retrieves elements found on the page based on the locator:

   ```python
   def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
       ...
   ```

4. **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

   Retrieves an attribute from an element based on the locator:

   ```python
   def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
       ...
   ```

5. **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

   Helper method to get the attribute from a web element:

   ```python
   def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
       ...
   ```

6. **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

   Sends a message to a web element:

   ```python
   def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
       ...
   ```

7. **`evaluate_locator(self, attribute: str | list | dict) -> str`**

   Evaluates the locator’s attribute:

   ```python
   def evaluate_locator(self, attribute: str | list | dict) -> str:
       ...
   ```

8. **`_evaluate(self, attribute: str) -> str | None`**

   Helper method to evaluate a single attribute:

   ```python
   def _evaluate(self, attribute: str) -> str | None:
       ...
   ```

9. **`get_locator_keys() -> list`**

   Returns a list of available locator keys:

   ```python
   @staticmethod
   def get_locator_keys() -> list:
       ...
   ```

### Locator Examples

The file also includes examples of various locators that can be used for testing:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },
  ...
}
```


### Locator Examples
<pre>
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },

  "pagination": {
    "ul": {
      "attribute": null,
      "by": "xpath",
      "selector": "//ul[@class='pagination']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
    },
    "->": {
      "attribute": null,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
      "if_list":"first","use_mouse": false
    }
  }

}
"description": {
  "attribute": [
    null,
    null
  ],
  "by": [
    "xpath",
    "xpath"
  ],
  "selector": [
    "//a[contains(@href, '#tab-description')]",
    "//div[@id = 'tab-description']//p"
  ],
  "timeout":0,"timeout_for_event":"presence_of_element_located","event": [
    "click()",
    null
  ],
  "if_list":"first","use_mouse": [
    false,
    false
  ],
  "mandatory": [
    true,
    true
  ],
  "locator_description": [
    "Clicking on the tab to open the description field",
    "Reading data from div"
  ]
}
</pre>

1. KEY.NULL: Represents the null key.
2. KEY.CANCEL: Represents the cancel key.
3. KEY.HELP: Represents the help key.
4. KEY.BACKSPACE: Represents the backspace key.
5. KEY.TAB: Represents the tab key.
6. KEY.CLEAR: Represents the clear key.
7. KEY.RETURN: Represents the return key.
8. KEY.ENTER: Represents the enter key.
9. KEY.SHIFT: Represents the shift key.
10. KEY.CONTROL: Represents the control key.
11. KEY.ALT: Represents the alt key.
12. KEY.PAUSE: Represents the pause key.
13. KEY.ESCAPE: Represents the escape key.
14. KEY.SPACE: Represents the space key.
15. KEY.PAGE_UP: Represents the page up key.
16. KEY.PAGE_DOWN: Represents the page down key.
17. KEY.END: Represents the end key.
18. KEY.HOME: Represents the home key.
19. KEY.LEFT: Represents the left arrow key.
20. KEY.UP: Represents the up arrow key.
21. KEY.RIGHT: Represents the right arrow key.
22. KEY.DOWN: Represents the down arrow key.
23. KEY.INSERT: Represents the insert key.
24. KEY.DELETE: Represents the delete key.
25. KEY.SEMICOLON: Represents the semicolon key.
26. KEY.EQUALS: Represents the equals key.
27. KEY.NUMPAD0 through KEY.NUMPAD9: Represents the numpad keys from 0 to 9.
28. KEY.MULTIPLY: Represents the multiply key.
29. KEY.ADD: Represents the add key.
30. KEY.SEPARATOR: Represents the separator key.
31. KEY.SUBTRACT: Represents the subtract key.
32. KEY.DECIMAL: Represents the decimal key.
33. KEY.DIVIDE: Represents the divide key.
34. KEY.F1 through KEY.F12: Represents the function keys from F1 to F12.
35. KEY.META: Represents the meta key.
---
# WebDriver Executor

## Overview

The WebDriver Executor module provides an execution framework for navigating and interacting with web pages using a WebDriver. It processes scripts and locators to perform automated actions on web elements.

## Main Features

- **Locator Handling**
  - **Initialization:** The `ExecuteLocator` class is initialized with a WebDriver instance and an optional list of arguments and keyword arguments. It sets up the WebDriver and the action chains for interacting with web elements.
  - **Locator Execution:** The `execute_locator` method processes the locator dictionary, which contains information about how to find and interact with web elements. It handles different types of locators and actions based on the configuration provided.
  - **Element Retrieval:** The `get_webelement_by_locator` method retrieves web elements based on the locator information, such as XPATH, ID, or CSS selectors. It waits for elements to be present and can return a single element, a list of elements, or `False` if none are found.
  - **Attribute Retrieval:** The `get_attribute_by_locator` method retrieves attributes from elements found using the locator. It supports both single and multiple elements.
  - **Message Sending:** The `send_message` method sends text input to web elements. It supports typing simulation with configurable typing speed and optional mouse interaction.

- **Screenshots**
  - **Element Screenshot:** The `get_webelement_as_screenshot` method takes a screenshot of a web element and returns it as a PNG image. It supports capturing screenshots of multiple elements and handles errors if elements are no longer present in the DOM.

- **Click Action**
  - **Element Click:** The `click` method performs a click action on a web element identified by the locator. It handles cases where the click results in navigation to a new page or opens a new window, and it logs errors if the click fails.

- **Locator Evaluation**
  - **Attribute Evaluation:** The `evaluate_locator` method evaluates locator attributes, including handling special cases where attributes are represented as placeholders (e.g., `%EXTERNAL_MESSAGE%`).

## Error Handling

The module uses try-except blocks to catch and log errors during various operations, such as finding elements, sending messages, and taking screenshots. Specific exceptions like `NoSuchElementException` and `TimeoutException` are caught to handle cases where elements are not found or time out.

## Usage

### Initialization

Create an instance of `ExecuteLocator` with a WebDriver instance.

### Execute Locator

Call the `execute_locator` method with a locator dictionary to perform actions or retrieve data from web elements.

### Handle Results

Use methods like `get_webelement_by_locator`, `send_message`, and `get_webelement_as_screenshot` to interact with web elements and process results.

## Dependencies

The module relies on Selenium for WebDriver operations, including finding elements, sending keys, and interacting with web pages. It also uses Python's built-in libraries for exception handling and time management.

## Example Usage

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Main function to demonstrate usage examples for Driver and Chrome 

    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```
[Объяснение Driver](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение Executor](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение локатора](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.ru.md)

