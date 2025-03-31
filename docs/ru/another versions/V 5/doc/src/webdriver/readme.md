# Модуль webdriver

## Обзор

Модуль `webdriver` предоставляет инструменты для автоматизированного управления веб-браузерами. Он включает классы и функции для создания драйверов браузеров, навигации по веб-страницам, взаимодействия с элементами и выполнения JavaScript-кода.

## Подробнее

Модуль `webdriver` является частью проекта `hypotez` и предназначен для автоматизации тестирования и сбора данных с веб-сайтов. Он предоставляет удобный интерфейс для управления браузером, позволяя выполнять различные действия, такие как ввод текста, нажатие кнопок, прокрутка страниц и получение информации об элементах.

## Содержание

- [Классы](#классы)
    - [Driver](#driver)
    - [Chrome](#chrome)
- [Функции](#функции)
    - [main](#main)

## Классы

### `Driver`

**Описание**: Базовый класс для управления веб-драйвером. Предоставляет методы для навигации, управления cookies, выполнения JavaScript и взаимодействия с элементами страницы.

**Как работает класс**:
Класс `Driver` динамически создается с использованием метакласса `DriverMeta`, который объединяет базовый класс `DriverBase` с указанным классом веб-драйвера (например, `Chrome`, `Firefox`, `Edge`). Это позволяет добавлять общую функциональность к различным типам драйверов.

**Методы**:
- `__init__(self, webdriver_class, *args, **kwargs)`: Инициализирует экземпляр класса `Driver`.
- `get_url(self, url: str) -> bool`: Открывает указанный URL в браузере.
- `extract_domain(self, url: str) -> str`: Извлекает доменное имя из URL.
- `_save_cookies_localy(self) -> bool`: Сохраняет cookies в локальный файл.
- `page_refresh(self) -> bool`: Обновляет текущую страницу.
- `scroll(self, scrolls: int = 1, direction: str = 'forward', frame_size: int = 1000, delay: float = 1) -> bool`: Прокручивает страницу вниз или вверх.
- `window_focus(self) -> None`: Фокусирует окно браузера.
- `find_element(self, by, value)`: Находит элемент на странице по указанному локатору.

**Параметры**:
- `webdriver_class`: Класс веб-драйвера, который будет использоваться (например, `Chrome`).
- `url` (str): URL для открытия в браузере.
- `scrolls` (int, optional): Количество прокруток. По умолчанию 1.
- `direction` (str, optional): Направление прокрутки ('forward' или 'backward'). По умолчанию 'forward'.
- `frame_size` (int, optional): Размер фрейма прокрутки. По умолчанию 1000.
- `delay` (float, optional): Задержка между прокрутками. По умолчанию 1.
- `by`: Метод поиска элемента (например, `By.CSS_SELECTOR`).
- `value`: Значение локатора элемента.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера
chrome_driver = Driver(Chrome)

# Открытие URL
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")

# Извлечение домена из URL
domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
print(f"Extracted domain: {domain}")
```

### `Chrome`

**Описание**: Класс для создания экземпляра веб-драйвера Chrome.

**Как работает класс**:
Класс `Chrome` наследуется от `selenium.webdriver.chrome.webdriver.WebDriver` и предоставляет стандартный интерфейс для управления браузером Chrome. Он может быть использован для создания экземпляра `Driver` с поддержкой Chrome.

**Методы**:
- `__init__(self, *args, **kwargs)`: Инициализирует экземпляр класса `Chrome`.

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome

# Создание экземпляра Chrome драйвера с использованием класса Driver
chrome_driver = Driver(Chrome)

# Дальнейшее использование chrome_driver для выполнения различных действий
```

## Функции

### `main`

```python
def main():
    """ Main function to demonstrate usage examples for Driver and Chrome """
```

**Описание**: Главная функция для демонстрации примеров использования классов `Driver` и `Chrome`.

**Как работает функция**:
Функция `main` создает экземпляры классов `Driver` и `Chrome`, выполняет различные операции, такие как навигация по URL, извлечение домена, сохранение cookies, обновление страницы, прокрутка страницы, получение языка страницы, установка пользовательского агента, поиск элемента по CSS-селектору и фокусировка окна.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Ничего (None).

**Примеры**:
```python
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
```markdown
# Модуль `executor`

## Обзор

Модуль `executor` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий с элементами веб-страницы с использованием Selenium WebDriver.

## Подробнее

Модуль `executor` является частью проекта `hypotez` и используется для автоматизации взаимодействия с веб-страницами на основе конфигурационных данных, представленных в виде словарей локаторов.

## Содержание

- [Классы](#классы)
    - [ExecuteLocator](#executelocator)

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для выполнения различных действий с элементами веб-страницы с использованием Selenium WebDriver. Он обрабатывает словари локаторов, извлекает элементы и выполняет действия, такие как ввод текста, клики и получение атрибутов.

**Как работает класс**:
Класс инициализируется экземпляром WebDriver и использует `ActionChains` для выполнения сложных действий. Он содержит методы для получения веб-элементов на основе локаторов, отправки сообщений, оценки атрибутов и обработки ошибок.

**Методы**:
- `__init__(self, driver, *args, **kwargs)`: Инициализирует экземпляр класса `ExecuteLocator`.
- `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> str | list | dict | WebElement | bool`: Выполняет действия на основе словаря локаторов.
- `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | list[WebElement] | bool`: Получает веб-элемент на основе локатора.
- `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`: Получает атрибут элемента на основе локатора.
- `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`: Получает атрибут веб-элемента.
- `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool`: Отправляет сообщение веб-элементу.
- `evaluate_locator(self, attribute: str | list | dict) -> str`: Оценивает атрибут локатора.
- `_evaluate(self, attribute: str) -> str | None`: Оценивает атрибут.
- `get_locator_keys() -> list`: Возвращает список доступных ключей локаторов.

**Параметры**:
- `driver`: Экземпляр WebDriver.
- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати сообщения. По умолчанию 0.
- `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при ошибке. По умолчанию `True`.
- `attribute` (str): Атрибут для оценки.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

# Инициализация драйвера Chrome
driver = webdriver.Chrome()
executor = ExecuteLocator(driver)

# Пример словаря локатора
locator = {
    "by": "xpath",
    "selector": "//input[@id='search']",
    "action": "send_keys",
    "message": "example"
}

# Выполнение действия на основе локатора
executor.execute_locator(locator, message="example")
```
```markdown
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