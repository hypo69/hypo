# Модуль `executor`

## Обзор

Модуль `executor.py` в `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий с веб-элементами на веб-странице с использованием Selenium WebDriver. Этот класс обрабатывает навигационные алгоритмы и взаимодействие с веб-страницей на основе конфигурационных данных, представленных в виде словарей локаторов.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
  - [`ExecuteLocator`](#ExecuteLocator)
    - [`__init__`](#__init__)
    - [`execute_locator`](#execute_locator)
    - [`get_webelement_by_locator`](#get_webelement_by_locator)
    - [`get_attribute_by_locator`](#get_attribute_by_locator)
    - [`_get_element_attribute`](#_get_element_attribute)
    - [`send_message`](#send_message)
    - [`evaluate_locator`](#evaluate_locator)
    - [`_evaluate`](#_evaluate)
    - [`get_locator_keys`](#get_locator_keys)
- [Примеры Локаторов](#примеры-локаторов)
- [Описание Ключей](#описание-ключей)
- [Основное Назначение](#основное-назначение)
- [Основные Компоненты](#основные-компоненты)
- [Обработка Ошибок](#обработка-ошибок)
- [Использование](#использование)
- [Зависимости](#зависимости)
- [Пример Использования](#пример-использования)

## Классы

### `ExecuteLocator`

**Описание**:
Класс `ExecuteLocator` предназначен для выполнения различных действий с веб-элементами на веб-странице с использованием Selenium WebDriver.

#### `__init__`

```python
def __init__(self, driver, *args, **kwargs)
```

**Описание**:
Конструктор класса `ExecuteLocator`.

**Параметры**:
- `driver` (selenium.webdriver): Экземпляр WebDriver для взаимодействия с браузером.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `None`: Метод ничего не возвращает.

**Вызывает исключения**:
- `WebDriverException`: Возникает, если `driver` не является экземпляром `webdriver`.

#### `execute_locator`

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]
```

**Описание**:
Основной метод для выполнения действий на основе переданного локатора.

**Параметры**:
- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, optional): Сообщение для отправки, если требуется. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора сообщения. По умолчанию `0`.
- `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Возвращает результат выполнения действия, в зависимости от типа действия.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает при ошибке выполнения локатора.
- `WebDriverException`: Возникает при проблемах с WebDriver.

#### `get_webelement_by_locator`

```python
def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool
```

**Описание**:
Получает веб-элементы на основе переданного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с параметрами локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Возвращает веб-элемент, список веб-элементов или `False`, если элементы не найдены.

**Вызывает исключения**:
- `WebDriverException`: Возникает при ошибках работы с WebDriver.
- `NoSuchElementException`: Возникает, если элемент не найден.

#### `get_attribute_by_locator`

```python
def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool
```

**Описание**:
Получает атрибут элемента на основе переданного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с параметрами локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `str | list | dict | bool`: Возвращает атрибут элемента, список атрибутов, словарь атрибутов или `False`, если атрибут не найден.

**Вызывает исключения**:
- `WebDriverException`: Возникает при ошибках работы с WebDriver.
- `NoSuchElementException`: Возникает, если элемент не найден.

#### `_get_element_attribute`

```python
def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None
```

**Описание**:
Вспомогательный метод для получения атрибута веб-элемента.

**Параметры**:
- `element` (WebElement): Веб-элемент, атрибут которого необходимо получить.
- `attribute` (str): Имя атрибута, который нужно получить.

**Возвращает**:
- `str | None`: Возвращает значение атрибута или `None`, если атрибут не найден.

**Вызывает исключения**:
- `WebDriverException`: Возникает при ошибках работы с WebDriver.

#### `send_message`

```python
def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool
```

**Описание**:
Отправляет сообщение в веб-элемент.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с параметрами локатора.
- `message` (str): Сообщение для отправки.
- `typing_speed` (float): Скорость набора сообщения.
- `continue_on_error` (bool): Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.

**Возвращает**:
- `bool`: Возвращает `True` при успешной отправке сообщения, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Возникает при ошибках работы с WebDriver.
- `NoSuchElementException`: Возникает, если элемент не найден.

#### `evaluate_locator`

```python
def evaluate_locator(self, attribute: str | list | dict) -> str
```

**Описание**:
Оценивает атрибут локатора, обрабатывая специальные случаи, такие как `%EXTERNAL_MESSAGE%`.

**Параметры**:
- `attribute` (str | list | dict): Атрибут для оценки.

**Возвращает**:
- `str`: Возвращает оцененный атрибут.

**Вызывает исключения**:
- `AttributeError`: Возникает при неверном формате атрибута.

#### `_evaluate`

```python
def _evaluate(self, attribute: str) -> str | None
```

**Описание**:
Вспомогательный метод для оценки единичного атрибута.

**Параметры**:
- `attribute` (str): Атрибут для оценки.

**Возвращает**:
- `str | None`: Возвращает оцененный атрибут или `None`, если атрибут не найден.

**Вызывает исключения**:
- `AttributeError`: Возникает при неверном формате атрибута.

#### `get_locator_keys`

```python
@staticmethod
def get_locator_keys() -> list
```

**Описание**:
Статический метод для получения списка доступных ключей локаторов.

**Параметры**:
- `None`: Метод не принимает параметры.

**Возвращает**:
- `list`: Возвращает список ключей локаторов.

## Примеры Локаторов

Примеры различных локаторов, используемых для тестирования:

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

## Описание Ключей

Описание ключей, которые могут быть использованы для эмуляции нажатий клавиш:

1.  `KEY.NULL`: Представляет нулевую клавишу.
2.  `KEY.CANCEL`: Представляет клавишу отмены.
3.  `KEY.HELP`: Представляет клавишу справки.
4.  `KEY.BACKSPACE`: Представляет клавишу Backspace.
5.  `KEY.TAB`: Представляет клавишу Tab.
6.  `KEY.CLEAR`: Представляет клавишу Clear.
7.  `KEY.RETURN`: Представляет клавишу Return.
8.  `KEY.ENTER`: Представляет клавишу Enter.
9.  `KEY.SHIFT`: Представляет клавишу Shift.
10. `KEY.CONTROL`: Представляет клавишу Control.
11. `KEY.ALT`: Представляет клавишу Alt.
12. `KEY.PAUSE`: Представляет клавишу Pause.
13. `KEY.ESCAPE`: Представляет клавишу Escape.
14. `KEY.SPACE`: Представляет клавишу Space.
15. `KEY.PAGE_UP`: Представляет клавишу Page Up.
16. `KEY.PAGE_DOWN`: Представляет клавишу Page Down.
17. `KEY.END`: Представляет клавишу End.
18. `KEY.HOME`: Представляет клавишу Home.
19. `KEY.LEFT`: Представляет клавишу Left Arrow.
20. `KEY.UP`: Представляет клавишу Up Arrow.
21. `KEY.RIGHT`: Представляет клавишу Right Arrow.
22. `KEY.DOWN`: Представляет клавишу Down Arrow.
23. `KEY.INSERT`: Представляет клавишу Insert.
24. `KEY.DELETE`: Представляет клавишу Delete.
25. `KEY.SEMICOLON`: Представляет клавишу Semicolon.
26. `KEY.EQUALS`: Представляет клавишу Equals.
27. `KEY.NUMPAD0` - `KEY.NUMPAD9`: Представляют клавиши NumPad от 0 до 9.
28. `KEY.MULTIPLY`: Представляет клавишу Multiply.
29. `KEY.ADD`: Представляет клавишу Add.
30. `KEY.SEPARATOR`: Представляет клавишу Separator.
31. `KEY.SUBTRACT`: Представляет клавишу Subtract.
32. `KEY.DECIMAL`: Представляет клавишу Decimal.
33. `KEY.DIVIDE`: Представляет клавишу Divide.
34. `KEY.F1` - `KEY.F12`: Представляют функциональные клавиши от F1 до F12.
35. `KEY.META`: Представляет клавишу Meta.

## Основное Назначение

Класс `ExecuteLocator` предназначен для выполнения навигации и взаимодействия с веб-страницами, используя Selenium WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматических действий с веб-элементами.

## Основные Компоненты

- **Обработка Локаторов**:
    - **Инициализация**: Класс `ExecuteLocator` инициализируется экземпляром `WebDriver` и набором аргументов. Он устанавливает `WebDriver` и цепочки действий для взаимодействия с веб-элементами.
    - **Выполнение Локаторов**: Метод `execute_locator` обрабатывает словарь локаторов, содержащий информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    - **Получение Элементов**: Метод `get_webelement_by_locator` получает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может возвращать один элемент, список элементов или `False`, если ни один не найден.
    - **Получение Атрибутов**: Метод `get_attribute_by_locator` получает атрибуты элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
    - **Отправка Сообщений**: Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью набора и дополнительным взаимодействием с мышью.

- **Скриншоты**:
    - **Скриншот Элемента**: Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

- **Действия Кликом**:
    - **Клик по Элементу**: Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открывает новое окно, и регистрирует ошибки, если клик не удался.

- **Оценка Локаторов**:
    - **Оценка Атрибутов**: Метод `evaluate_locator` оценивает атрибуты локаторов, включая обработку специальных случаев, когда атрибуты представлены как заполнители (например, `%EXTERNAL_MESSAGE%`).

## Обработка Ошибок

Модуль использует блоки try-except для перехвата и логирования ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или время ожидания истекло.

## Использование

### Инициализация
Создайте экземпляр `ExecuteLocator` с экземпляром `WebDriver`.

### Выполнение Локатора
Вызовите метод `execute_locator` со словарем локатора для выполнения действий или получения данных из веб-элементов.

### Обработка Результатов
Используйте методы `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot` для взаимодействия с веб-элементами и обработки результатов.

## Зависимости

Модуль зависит от Selenium для операций `WebDriver`, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Пример Использования

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