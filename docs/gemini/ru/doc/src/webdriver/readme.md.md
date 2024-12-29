# Модуль `webdriver`

## Обзор
Этот модуль содержит классы и функции, необходимые для автоматизации веб-браузеров с использованием Selenium WebDriver. Он включает в себя настройку драйвера, выполнение различных действий на веб-странице, таких как навигация, взаимодействие с элементами и многое другое.

## Оглавление
1. [Классы](#классы)
    - [`Driver`](#класс-driver)
    - [`Chrome`](#класс-chrome)
2. [Функции](#функции)
    - [`main`](#функция-main)
3. [Дополнительная информация](#дополнительная-информация)
    - [Обзор модуля `Driver`](#обзор-модуля-driver)
    - [Примеры использования классов и методов](#примеры-использования-классов-и-методов)
    - [Обзор модуля `Executor`](#обзор-модуля-executor)
    - [Примеры локаторов](#примеры-локаторов)
    - [WebDriver Executor](#webdriver-executor)
    - [Пример использования](#пример-использования)

## Классы

### `Driver`
**Описание**:
Класс `Driver` предоставляет динамическую реализацию WebDriver, которая объединяет общие функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления файлами cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-сайтов.

**Методы:**
- `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
- `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
- `get_url`: Загружает указанный URL-адрес.
- `extract_domain`: Извлекает домен из URL-адреса.
- `_save_cookies_localy`: Сохраняет файлы cookie в локальный файл.
- `page_refresh`: Обновляет текущую страницу.
- `window_focus`: Фокусирует окно браузера с помощью JavaScript.
- `wait`: Ожидает указанный интервал времени.

**Параметры:**
- `driver_class` (class): Класс драйвера WebDriver для создания экземпляра.
- `user_agent` (dict, optional): Пользовательский user-agent для настройки драйвера. По умолчанию `None`.

### `Chrome`
**Описание**:
Класс `Chrome` используется для создания экземпляра Chrome WebDriver.

**Методы:**
-   `__call__`: Создает и возвращает экземпляр Chrome WebDriver.

**Параметры:**
- `user_agent` (dict, optional): Пользовательский user-agent для настройки драйвера. По умолчанию `None`.

## Функции

### `main`
**Описание**:
Главная функция для демонстрации примеров использования классов `Driver` и `Chrome`.

**Параметры**:
- Нет

**Возвращает**:
- None

## Дополнительная информация

### Обзор модуля `Driver`

**Описание:**
Модуль `Driver` предоставляет динамическую реализацию WebDriver, объединяющую общие функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления файлами cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-сайтов.

**Основные функции:**
- Наследует от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
- Включает методы для прокрутки, обработки файлов cookie, взаимодействия с веб-элементами и выполнения JavaScript.
- Предоставляет утилиты для управления окнами браузера и взаимодействием со страницами.

**Компоненты:**
1.  **Класс `DriverBase`:**
    -   **Атрибуты:**
        -   `previous_url`: Сохраняет предыдущий URL.
        -   `referrer`: Сохраняет URL-адрес реферера.
        -   `page_lang`: Сохраняет язык страницы.
        -   Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.
    -   **Методы:**
        -   `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
        -   `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
        -   `get_url`: Загружает указанный URL-адрес.
        -   `extract_domain`: Извлекает домен из URL-адреса.
        -   `_save_cookies_localy`: Сохраняет файлы cookie в локальный файл.
        -   `page_refresh`: Обновляет текущую страницу.
        -   `window_focus`: Фокусирует окно браузера с помощью JavaScript.
        -   `wait`: Ожидает указанный интервал времени.
2.  **Класс `DriverMeta`:**
    -   **Методы:**
        -   `__call__`: Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональные возможности выполнения локаторов.
3.  **Класс `Driver`:**
    -   **Описание:**
        -   Динамически созданный класс WebDriver, который наследует от `DriverBase` и указанного класса WebDriver.
    -   **Пример использования:**
        ```python
        from src.webdriver.driver import Driver, Chrome, Firefox, Edge
        d = Driver(Chrome)
        ```

**Использование:**
-   **Инициализация:** Создайте экземпляр `Driver` с конкретным классом WebDriver.
-   **Функциональность:** Используйте методы, такие как `scroll`, `get_url`, `extract_domain` и `page_refresh` для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления файлами cookie.

**Зависимости:**
-   **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
-   **Python Libraries:** Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функциональных возможностей.

### Примеры использования классов и методов

-   **Создание экземпляра Chrome драйвера и навигация по URL:**

    ```python
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")
    ```
-   **Извлечение домена из URL:**

    ```python
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")
    ```
-   **Сохранение cookies в локальный файл:**

    ```python
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")
    ```
-   **Обновление текущей страницы:**

    ```python
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")
    ```
-   **Прокрутка страницы вниз:**

    ```python
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")
    ```
-   **Получение языка текущей страницы:**

    ```python
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")
    ```
-   **Установка кастомного User-Agent для Chrome драйвера:**

    ```python
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")
    ```
-   **Поиск элемента по CSS селектору:**

    ```python
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    ```
-   **Получение текущего URL:**

    ```python
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")
    ```
-   **Фокусировка окна, чтобы убрать фокус с элемента:**

    ```python
    chrome_driver.window_focus()
    print("Focused the window")
    ```

**Примечания:**
- Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

### Обзор модуля `Executor`

Файл `executor.py` в модуле `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий над элементами веб-страницы с использованием Selenium WebDriver.

**Основное назначение:**
Класс `ExecuteLocator` предназначен для выполнения алгоритмов навигации и взаимодействия с веб-страницей на основе данных конфигурации, предоставляемых в виде словарей локаторов.

**Основные компоненты:**
1.  **Импорты и зависимости**

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
    Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, а также внутренние модули для настроек, ведения журнала и обработки исключений.

2.  **Класс `ExecuteLocator`**
    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов.

    -   **Атрибуты класса:**
        -   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
        -   `actions`: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
        -   `by_mapping`: Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

    -   **Методы класса:**
        1.  **`__init__(self, driver, *args, **kwargs)`**
            Конструктор класса инициализирует WebDriver и `ActionChains`:
            ```python
            def __init__(self, driver, *args, **kwargs):
                self.driver = driver
                self.actions = ActionChains(driver)
            ```
        2.  **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**
            Основной метод для выполнения действий на основе локатора:

            ```python
            def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
                ...
            ```
            - `locator`: Словарь с параметрами для выполнения действий.
            - `message`: Сообщение для отправки, если необходимо.
            - `typing_speed`: Скорость набора сообщений.
            - `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.
            Этот метод выбирает, какие действия выполнять на основе конфигурации локатора.
        3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**
            Извлекает элементы, найденные на странице на основе локатора:
            ```python
            def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
                ...
            ```
        4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**
            Извлекает атрибут из элемента на основе локатора:
            ```python
            def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
                ...
            ```
        5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**
            Вспомогательный метод для получения атрибута из веб-элемента:
            ```python
            def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
                ...
            ```
        6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**
            Отправляет сообщение веб-элементу:
            ```python
            def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
                ...
            ```
        7.  **`evaluate_locator(self, attribute: str | list | dict) -> str`**
            Оценивает атрибут локатора:
            ```python
            def evaluate_locator(self, attribute: str | list | dict) -> str:
                ...
            ```
        8.  **`_evaluate(self, attribute: str) -> str | None`**
            Вспомогательный метод для оценки одного атрибута:
            ```python
            def _evaluate(self, attribute: str) -> str | None:
                ...
            ```
        9.  **`get_locator_keys() -> list`**
            Возвращает список доступных ключей локатора:
            ```python
            @staticmethod
            def get_locator_keys() -> list:
                ...
            ```

### Примеры локаторов

Файл также включает примеры различных локаторов, которые можно использовать для тестирования:

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

1. KEY.NULL: Представляет нулевой ключ.
2. KEY.CANCEL: Представляет ключ отмены.
3. KEY.HELP: Представляет ключ справки.
4. KEY.BACKSPACE: Представляет ключ backspace.
5. KEY.TAB: Представляет ключ табуляции.
6. KEY.CLEAR: Представляет ключ очистки.
7. KEY.RETURN: Представляет ключ return.
8. KEY.ENTER: Представляет ключ enter.
9. KEY.SHIFT: Представляет ключ shift.
10. KEY.CONTROL: Представляет ключ control.
11. KEY.ALT: Представляет ключ alt.
12. KEY.PAUSE: Представляет ключ pause.
13. KEY.ESCAPE: Представляет ключ escape.
14. KEY.SPACE: Представляет ключ пробела.
15. KEY.PAGE_UP: Представляет ключ page up.
16. KEY.PAGE_DOWN: Представляет ключ page down.
17. KEY.END: Представляет ключ end.
18. KEY.HOME: Представляет ключ home.
19. KEY.LEFT: Представляет ключ левой стрелки.
20. KEY.UP: Представляет ключ верхней стрелки.
21. KEY.RIGHT: Представляет ключ правой стрелки.
22. KEY.DOWN: Представляет ключ нижней стрелки.
23. KEY.INSERT: Представляет ключ insert.
24. KEY.DELETE: Представляет ключ delete.
25. KEY.SEMICOLON: Представляет ключ точки с запятой.
26. KEY.EQUALS: Представляет ключ равно.
27. KEY.NUMPAD0 through KEY.NUMPAD9: Представляет клавиши цифровой клавиатуры от 0 до 9.
28. KEY.MULTIPLY: Представляет ключ умножения.
29. KEY.ADD: Представляет ключ сложения.
30. KEY.SEPARATOR: Представляет ключ разделителя.
31. KEY.SUBTRACT: Представляет ключ вычитания.
32. KEY.DECIMAL: Представляет ключ десятичной дроби.
33. KEY.DIVIDE: Представляет ключ деления.
34. KEY.F1 through KEY.F12: Представляет функциональные клавиши от F1 до F12.
35. KEY.META: Представляет мета-ключ.

### WebDriver Executor
**Описание:**
Модуль WebDriver Executor предоставляет фреймворк для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий на веб-элементах.

**Основные функции:**

- **Обработка локаторов:**
  - **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и ключевых слов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
  - **Выполнение локаторов:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
  - **Получение элементов:** Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может возвращать один элемент, список элементов или `False`, если ни один не найден.
  - **Получение атрибутов:** Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
  - **Отправка сообщений:** Метод `send_message` отправляет текстовые данные в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью набора и дополнительным взаимодействием мыши.

- **Скриншоты:**
  - **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

- **Действие клика:**
  - **Клик по элементу:** Метод `click` выполняет действие клика на веб-элементе, идентифицированном локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удался.

- **Оценка локатора:**
  - **Оценка атрибутов:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

**Обработка ошибок:**
Модуль использует блоки try-except для перехвата и записи ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекает время ожидания.

**Использование:**
1.  **Инициализация:** Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.
2.  **Выполнение локатора:** Вызовите метод `execute_locator` со словарем локаторов, чтобы выполнить действия или получить данные из веб-элементов.
3.  **Обработка результатов:** Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

**Зависимости:**
Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

### Пример использования

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
[Driver explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Executor explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Locator explanantion](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.md)