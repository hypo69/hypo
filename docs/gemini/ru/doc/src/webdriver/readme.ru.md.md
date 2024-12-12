# Модуль `driver.py`

## Обзор

Модуль `driver.py` предоставляет динамическую реализацию WebDriver, которая интегрирует стандартные функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-страниц.

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [`DriverBase`](#driverbase)
    - [`DriverMeta`](#drivermeta)
    - [`Driver`](#driver)
- [Примеры использования классов и методов](#примеры-использования-классов-и-методов)
- [Примечания](#примечания)

## Классы

### `DriverBase`

**Описание**: Базовый класс для WebDriver, предоставляющий основные методы для взаимодействия с браузером.

**Атрибуты**:

- `previous_url` (str): Сохраняет предыдущий URL.
- `referrer` (str): Сохраняет URL-адрес реферера.
- `page_lang` (str): Сохраняет язык страницы.
- Различные атрибуты для взаимодействия с веб-элементами и выполнения JavaScript.

**Методы**:

#### `scroll`

**Описание**: Прокручивает веб-страницу в указанном направлении.

**Параметры**:
- `scrolls` (int): Количество прокруток.
- `direction` (str): Направление прокрутки (`forward`, `backward`, `both`).
- `frame_size` (int): Размер фрейма прокрутки.
- `delay` (int): Задержка между прокрутками.

**Возвращает**:
- `bool`: `True`, если прокрутка прошла успешно, иначе `False`.

#### `locale`

**Описание**: Пытается определить язык страницы, проверяя мета-теги или используя JavaScript.

**Возвращает**:
- `str`: Язык страницы или `None`, если не удалось определить.

#### `get_url`

**Описание**: Загружает указанный URL.

**Параметры**:
- `url` (str): URL для загрузки.

**Возвращает**:
- `bool`: `True`, если URL загружен успешно, иначе `False`.

#### `extract_domain`

**Описание**: Извлекает домен из URL.

**Параметры**:
- `url` (str): URL для анализа.

**Возвращает**:
- `str`: Домен из URL.

#### `_save_cookies_localy`

**Описание**: Сохраняет cookies в локальный файл.

**Возвращает**:
- `bool`: `True`, если cookies были сохранены успешно, иначе `False`.

#### `page_refresh`

**Описание**: Обновляет текущую страницу.

**Возвращает**:
- `bool`: `True`, если страница была обновлена успешно, иначе `False`.

#### `window_focus`

**Описание**: Фокусирует окно браузера с помощью JavaScript.

**Возвращает**:
- `None`

#### `wait`

**Описание**: Ожидает указанный интервал.

**Параметры**:
- `interval` (int): Интервал ожидания в секундах.

**Возвращает**:
- `None`

### `DriverMeta`

**Описание**: Метакласс для создания класса `Driver`.

**Методы**:

#### `__call__`

**Описание**: Создает новый класс `Driver`, который сочетает указанный класс WebDriver (например, `Chrome`, `Firefox`, `Edge`) с `DriverBase`. Инициализирует методы JavaScript и функциональность выполнения локаторов.

**Параметры**:
- `cls` (type): Класс WebDriver.
- `*args`: Позиционные аргументы.
- `**kwargs`: Именованные аргументы.

**Возвращает**:
- `type`: Новый класс `Driver`.

### `Driver`

**Описание**: Динамически созданный класс WebDriver, который наследует от `DriverBase` и указанного класса WebDriver.

**Пример использования**:

```python
from src.webdriver.driver import Driver, Chrome, Firefox, Edge
d = Driver(Chrome)
```

## Примеры использования классов и методов

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

## Примечания

- Убедитесь, что у вас установлены все зависимости, например, `selenium`, `fake_useragent` и `src` модули, указанные в импортах.
- Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.
```
```markdown
# Модуль `executor.py`

## Обзор
Модуль `executor.py` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий с элементами веб-страницы с использованием Selenium WebDriver. Класс обрабатывает локаторы и выполняет такие действия, как поиск элементов, отправка сообщений, получение атрибутов и т.д.

## Оглавление

- [Обзор](#обзор)
- [Основные компоненты](#основные-компоненты)
    - [Импорты и зависимости](#импорты-и-зависимости)
    - [Класс `ExecuteLocator`](#класс-executelocator)
        - [Атрибуты класса](#атрибуты-класса)
        - [Методы класса](#методы-класса)
- [Примеры локаторов](#примеры-локаторов)
- [Примеры клавиш Selenium](#примеры-клавиш-selenium)
- [WebDriver Executor](#webdriver-executor)
    - [Обзор](#обзор-1)
    - [Основные функции](#основные-функции)
    - [Обработка ошибок](#обработка-ошибок)
    - [Использование](#использование)
    - [Зависимости](#зависимости)
- [Примеры использования](#примеры-использования)
- [Ссылки](#ссылки)

## Основные компоненты

### Импорты и зависимости

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

Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, а также внутренние модули для настроек, логирования и обработки исключений.

### Класс `ExecuteLocator`

Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий с веб-элементами и обработки локаторов.

#### Атрибуты класса

-   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
-   `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
-   `by_mapping`: Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

#### Методы класса

1.  `__init__(self, driver, *args, **kwargs)`

    Конструктор класса инициализирует WebDriver и `ActionChains`:

    ```python
    def __init__(self, driver, *args, **kwargs):
        self.driver = driver
        self.actions = ActionChains(driver)
    ```

2.  `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

    Основной метод для выполнения действий на основе локатора:

    ```python
    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        ...
    ```

    -   `locator`: Словарь с параметрами для выполнения действий.
    -   `message`: Сообщение для отправки, если необходимо.
    -   `typing_speed`: Скорость набора сообщения.
    -   `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение, если произошла ошибка.

    Этот метод выбирает, какие действия выполнять на основе конфигурации локатора.

3.  `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

    Извлекает элементы, найденные на странице, на основе локатора:

    ```python
    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
        ...
    ```

4.  `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

    Извлекает атрибут из элемента на основе локатора:

    ```python
    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
        ...
    ```

5.  `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

    Вспомогательный метод для получения атрибута из веб-элемента:

    ```python
    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
        ...
    ```

6.  `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool`

    Отправляет сообщение в веб-элемент:

    ```python
    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool:
        ...
    ```

7.  `evaluate_locator(self, attribute: str | list | dict) -> str`

    Вычисляет атрибут локатора:

    ```python
    def evaluate_locator(self, attribute: str | list | dict) -> str:
        ...
    ```

8.  `_evaluate(self, attribute: str) -> str | None`

    Вспомогательный метод для вычисления отдельного атрибута:

    ```python
    def _evaluate(self, attribute: str) -> str | None:
        ...
    ```

9.  `get_locator_keys() -> list`

    Возвращает список доступных ключей локатора:

    ```python
    @staticmethod
    def get_locator_keys() -> list:
        ...
    ```

## Примеры локаторов

Файл также включает примеры различных локаторов, которые можно использовать для тестирования:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first",
	"use_mouse": false,
    "mandatory": true,
    "timeout":0,
	"timeout_for_event":"presence_of_element_located",
	"event": null
  },
  "pagination": {
    "ul": {
      "attribute": null,
      "by": "xpath",
      "selector": "//ul[@class='pagination']",
      "timeout":0,
	  "timeout_for_event":"presence_of_element_located",
	  "event": "click()"
    },
    "->": {
      "attribute": null,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "timeout":0,
	  "timeout_for_event":"presence_of_element_located",
	  "event": "click()",
      "if_list":"first",
	  "use_mouse": false
    }
  },
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
    "timeout":0,
	"timeout_for_event":"presence_of_element_located",
	"event": [
      "click()",
      null
    ],
    "if_list":"first",
	"use_mouse": [
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
}
```
## Примеры клавиш Selenium
1.  `KEY.NULL`: Представляет клавишу null.
2.  `KEY.CANCEL`: Представляет клавишу cancel.
3.  `KEY.HELP`: Представляет клавишу help.
4.  `KEY.BACKSPACE`: Представляет клавишу backspace.
5.  `KEY.TAB`: Представляет клавишу tab.
6.  `KEY.CLEAR`: Представляет клавишу clear.
7.  `KEY.RETURN`: Представляет клавишу return.
8.  `KEY.ENTER`: Представляет клавишу enter.
9.  `KEY.SHIFT`: Представляет клавишу shift.
10. `KEY.CONTROL`: Представляет клавишу control.
11. `KEY.ALT`: Представляет клавишу alt.
12. `KEY.PAUSE`: Представляет клавишу pause.
13. `KEY.ESCAPE`: Представляет клавишу escape.
14. `KEY.SPACE`: Представляет клавишу space.
15. `KEY.PAGE_UP`: Представляет клавишу page up.
16. `KEY.PAGE_DOWN`: Представляет клавишу page down.
17. `KEY.END`: Представляет клавишу end.
18. `KEY.HOME`: Представляет клавишу home.
19. `KEY.LEFT`: Представляет клавишу left arrow.
20. `KEY.UP`: Представляет клавишу up arrow.
21. `KEY.RIGHT`: Представляет клавишу right arrow.
22. `KEY.DOWN`: Представляет клавишу down arrow.
23. `KEY.INSERT`: Представляет клавишу insert.
24. `KEY.DELETE`: Представляет клавишу delete.
25. `KEY.SEMICOLON`: Представляет клавишу semicolon.
26. `KEY.EQUALS`: Представляет клавишу equals.
27. `KEY.NUMPAD0` through `KEY.NUMPAD9`: Представляет клавиши цифровой клавиатуры от 0 до 9.
28. `KEY.MULTIPLY`: Представляет клавишу multiply.
29. `KEY.ADD`: Представляет клавишу add.
30. `KEY.SEPARATOR`: Представляет клавишу separator.
31. `KEY.SUBTRACT`: Представляет клавишу subtract.
32. `KEY.DECIMAL`: Представляет клавишу decimal.
33. `KEY.DIVIDE`: Представляет клавишу divide.
34. `KEY.F1` through `KEY.F12`: Представляет функциональные клавиши от F1 до F12.
35. `KEY.META`: Представляет клавишу meta.

## WebDriver Executor

### Обзор

Модуль WebDriver Executor предоставляет фреймворк для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий с веб-элементами.

### Основные функции

-   **Обработка локаторов**
    -   **Инициализация**: Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и ключевых слов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора**: Метод `execute_locator` обрабатывает словарь локатора, который содержит информацию о том, как найти веб-элементы и взаимодействовать с ними. Он обрабатывает различные типы локаторов и действия на основе предоставленной конфигурации.
    -   **Получение элементов**: Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации локатора, такой как XPATH, ID или CSS-селекторы. Он ждет, пока элементы появятся, и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    -   **Получение атрибутов**: Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с помощью локатора. Он поддерживает как единичные, так и множественные элементы.
    -   **Отправка сообщений**: Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию набора текста с настраиваемой скоростью набора и возможностью взаимодействия с мышью.

-   **Скриншоты**
    -   **Скриншот элемента**: Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

-   **Действие "Клик"**
    -   **Клик по элементу**: Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удается.

-   **Вычисление локатора**
    -   **Вычисление атрибута**: Метод `evaluate_locator` вычисляет атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

### Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Определенные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекло время ожидания.

### Использование

#### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

#### Выполнение локатора

Вызовите метод `execute_locator` со словарем локатора для выполнения действий или извлечения данных из веб-элементов.

#### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

### Зависимости

Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Примеры использования
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
## Ссылки
[Объяснение Driver](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение Executor](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение локатора](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.ru.md)