# Документация модуля `executor.py`

## Обзор

Модуль `executor.py` является частью пакета `src.webdriver` и предназначен для автоматизации взаимодействия с веб-элементами с использованием Selenium. Этот модуль предоставляет гибкий и универсальный фреймворк для определения местоположения, взаимодействия и извлечения информации из веб-элементов на основе предоставленных конфигураций, известных как "локаторы".

## Подробнее

Модуль `executor.py` предоставляет инструменты для работы с веб-элементами на странице, используя Selenium WebDriver. Он позволяет выполнять различные действия, такие как клики, отправка сообщений, выполнение событий и получение атрибутов. Модуль особенно полезен для автоматизации задач, связанных с тестированием веб-приложений, сбором данных и взаимодействием с динамическими веб-страницами.

## Классы

### `ExecuteLocator`

**Описание**:
Этот класс является ядром модуля и отвечает за обработку взаимодействий с веб-элементами на основе предоставленных локаторов.

**Как работает класс**:
Класс `ExecuteLocator` инициализируется с экземпляром Selenium WebDriver. Он использует этот драйвер для поиска веб-элементов на странице на основе предоставленных локаторов. Локаторы могут быть представлены в виде словарей или объектов `SimpleNamespace`, что обеспечивает гибкость в определении критериев поиска элементов.

При вызове метода `execute_locator` класс определяет тип локатора и преобразует его в `SimpleNamespace`, если это необходимо. Затем он проверяет наличие атрибутов события, атрибута или обязательного флага. Если локатор соответствует этим критериям, класс пытается сопоставить локатор и извлечь атрибуты элемента.

В случае возникновения исключений в процессе выполнения, класс перехватывает их и регистрирует с помощью модуля `logger`. Если локатор содержит событие, класс выполняет его. Если локатор содержит атрибут, класс извлекает его значение. Если ни событие, ни атрибут не указаны, класс возвращает веб-элемент, соответствующий локатору.

**Атрибуты**:
- `driver`: Экземпляр Selenium WebDriver.
- `actions`: Объект `ActionChains` для выполнения сложных действий.
- `by_mapping`: Словарь, сопоставляющий типы локаторов с методами `By` Selenium.
- `mode`: Режим выполнения (`debug`, `dev` и т. д.).

**Методы**:
- `__post_init__`: Инициализирует объект `ActionChains`, если предоставлен драйвер.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.
- `get_webelement_by_locator`: Извлекает веб-элементы на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет события, связанные с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

## Функции

### `ExecuteLocator.execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace) -> Any:
    """Executes actions on a web element based on the provided locator."""
```

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Как работает функция**:
Метод `execute_locator` принимает локатор в виде словаря или объекта `SimpleNamespace`. Он определяет тип локатора и преобразует его в `SimpleNamespace`, если это необходимо. Затем он проверяет наличие атрибутов события, атрибута или обязательного флага. Если локатор соответствует этим критериям, метод пытается сопоставить локатор и извлечь атрибуты элемента.

В случае возникновения исключений в процессе выполнения, метод перехватывает их и регистрирует с помощью модуля `logger`. Если локатор содержит событие, метод выполняет его. Если локатор содержит атрибут, метод извлекает его значение. Если ни событие, ни атрибут не указаны, метод возвращает веб-элемент, соответствующий локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Локатор для веб-элемента.

**Возвращает**:
- `Any`: Результат выполнения действия над веб-элементом.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при выполнении действия над веб-элементом.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде словаря
locator_dict = {
    "by": "ID",
    "selector": "some_element_id",
    "event": "click()"
}

# Выполнение локатора
result = await executor.execute_locator(locator_dict)
print(result)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id", event="click()")

# Выполнение локатора
result = await executor.execute_locator(locator_sns)
print(result)
```

### `ExecuteLocator.evaluate_locator`

```python
async def evaluate_locator(self, locator: SimpleNamespace) -> list[Any] | Any | None:
    """Evaluates and processes locator attributes."""
```

**Описание**: Оценивает и обрабатывает атрибуты локатора.

**Как работает функция**:
Метод `evaluate_locator` принимает локатор в виде объекта `SimpleNamespace`. Он проверяет, является ли атрибут локатора списком. Если да, то метод итерируется по каждому атрибуту в списке и вызывает функцию `_evaluate` для каждого атрибута. Результаты собираются с помощью `asyncio.gather`. Если атрибут не является списком, метод вызывает `_evaluate` для одного атрибута.

**Параметры**:
- `locator` (SimpleNamespace): Локатор для веб-элемента.

**Возвращает**:
- `list[Any] | Any | None`: Результат оценки и обработки атрибутов локатора.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при оценке и обработке атрибутов локатора.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде SimpleNamespace с атрибутом в виде списка
locator_sns_list = SimpleNamespace(by="ID", selector="some_element_id", attribute=["value", "text"])

# Выполнение локатора
result = await executor.evaluate_locator(locator_sns_list)
print(result)

# Определение локатора в виде SimpleNamespace с одиночным атрибутом
locator_sns_single = SimpleNamespace(by="ID", selector="some_element_id", attribute="value")

# Выполнение локатора
result = await executor.evaluate_locator(locator_sns_single)
print(result)
```

### `ExecuteLocator.get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> list[Any] | Any | None:
    """Retrieves attributes from an element or list of elements found by the given locator."""
```

**Описание**: Извлекает атрибуты из элемента или списка элементов, найденных по заданному локатору.

**Как работает функция**:
Метод `get_attribute_by_locator` принимает локатор в виде словаря или объекта `SimpleNamespace`. Он преобразует локатор в `SimpleNamespace`, если это необходимо. Затем он вызывает метод `get_webelement_by_locator` для получения веб-элемента. Если веб-элемент не найден, метод регистрирует отладочное сообщение и возвращает `None`.

Если веб-элемент найден, метод проверяет, является ли атрибут локатора строкой, подобной словарю. Если да, то метод анализирует строку атрибута в словарь. Затем он проверяет, является ли веб-элемент списком. Если да, то метод извлекает атрибуты для каждого элемента в списке. Если веб-элемент не является списком, метод извлекает атрибуты для одного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Локатор для веб-элемента.

**Возвращает**:
- `list[Any] | Any | None`: Список атрибутов или один атрибут, извлеченный из веб-элемента.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при извлечении атрибутов из веб-элемента.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде словаря
locator_dict = {
    "by": "ID",
    "selector": "some_element_id",
    "attribute": "value"
}

# Получение атрибута по локатору
result = await executor.get_attribute_by_locator(locator_dict)
print(result)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id", attribute="value")

# Получение атрибута по локатору
result = await executor.get_attribute_by_locator(locator_sns)
print(result)
```

### `ExecuteLocator.get_webelement_by_locator`

```python
def get_webelement_by_locator(self, locator: SimpleNamespace) -> WebElement | list[WebElement] | None:
    """Extracts web elements based on the provided locator."""
```

**Описание**: Извлекает веб-элементы на основе предоставленного локатора.

**Как работает функция**:
Метод `get_webelement_by_locator` принимает локатор в виде объекта `SimpleNamespace`. Он использует атрибуты `by` и `selector` локатора для поиска веб-элементов на странице. Если атрибут `many` установлен в `True`, метод пытается найти несколько веб-элементов. В противном случае метод пытается найти только один веб-элемент.

**Параметры**:
- `locator` (SimpleNamespace): Локатор для веб-элемента.

**Возвращает**:
- `WebElement | list[WebElement] | None`: Найденный веб-элемент, список веб-элементов или `None`, если веб-элемент не найден.

**Вызывает исключения**:
- `NoSuchElementException`: Если веб-элемент не найден.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace
from selenium.webdriver.remote.webdriver import WebElement

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id")

# Получение веб-элемента по локатору
element = executor.get_webelement_by_locator(locator_sns)

if isinstance(element, WebElement):
    print("Web element found")
else:
    print("Web element not found")
```

### `ExecuteLocator.get_webelement_as_screenshot`

```python
def get_webelement_as_screenshot(self, locator: SimpleNamespace, filename: str = 'element_screenshot.png') -> str | None:
    """Takes a screenshot of the located web element."""
```

**Описание**: Делает скриншот найденного веб-элемента.

**Как работает функция**:
Метод `get_webelement_as_screenshot` принимает локатор в виде объекта `SimpleNamespace` и имя файла для сохранения скриншота. Он вызывает метод `get_webelement_by_locator` для получения веб-элемента. Если веб-элемент найден, метод делает скриншот веб-элемента и сохраняет его в файл.

**Параметры**:
- `locator` (SimpleNamespace): Локатор для веб-элемента.
- `filename` (str, optional): Имя файла для сохранения скриншота. По умолчанию 'element_screenshot.png'.

**Возвращает**:
- `str | None`: Путь к сохраненному скриншоту или `None`, если веб-элемент не найден.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при создании скриншота веб-элемента.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id")

# Получение скриншота веб-элемента
screenshot_path = executor.get_webelement_as_screenshot(locator_sns)

if screenshot_path:
    print(f"Screenshot saved to {screenshot_path}")
else:
    print("Web element not found")
```

### `ExecuteLocator.execute_event`

```python
def execute_event(self, web_element: WebElement, locator: SimpleNamespace) -> Any:
    """Executes the events associated with a locator."""
```

**Описание**: Выполняет события, связанные с локатором.

**Как работает функция**:
Метод `execute_event` принимает веб-элемент и локатор в виде объекта `SimpleNamespace`. Он извлекает тип события из локатора и выполняет соответствующее действие над веб-элементом. Поддерживаемые типы событий включают `click()`, `hover()`, `send_keys()`, `submit()` и другие.

**Параметры**:
- `web_element` (WebElement): Веб-элемент, над которым выполняется событие.
- `locator` (SimpleNamespace): Локатор для веб-элемента.

**Возвращает**:
- `Any`: Результат выполнения события.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при выполнении события.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from types import SimpleNamespace
from selenium.webdriver.remote.webdriver import WebElement

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id", event="click()")

# Получение веб-элемента по локатору
element = executor.get_webelement_by_locator(locator_sns)

if isinstance(element, WebElement):
    # Выполнение события
    result = executor.execute_event(element, locator_sns)
    print("Event executed")
else:
    print("Web element not found")
```

### `ExecuteLocator.send_message`

```python
def send_message(self, web_element: WebElement, message: str) -> None:
    """Sends a message to a web element."""
```

**Описание**: Отправляет сообщение веб-элементу.

**Как работает функция**:
Метод `send_message` принимает веб-элемент и сообщение в виде строки. Он отправляет сообщение веб-элементу с помощью метода `send_keys`.

**Параметры**:
- `web_element` (WebElement): Веб-элемент, которому отправляется сообщение.
- `message` (str): Отправляемое сообщение.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при отправке сообщения веб-элементу.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from selenium.webdriver.remote.webdriver import WebElement
from types import SimpleNamespace

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Определение локатора в виде SimpleNamespace
locator_sns = SimpleNamespace(by="ID", selector="some_element_id")

# Получение веб-элемента по локатору
element = executor.get_webelement_by_locator(locator_sns)

if isinstance(element, WebElement):
    # Отправка сообщения веб-элементу
    executor.send_message(element, "Hello, world!")
    print("Message sent")
else:
    print("Web element not found")
```

## Зависимости

- `selenium`: Для веб-автоматизации.
- `asyncio`: Для асинхронных операций.
- `re`: Для регулярных выражений.
- `dataclasses`: Для создания классов данных.
- `enum`: Для создания перечислений.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.

## Обработка ошибок

Модуль включает надежную обработку ошибок, чтобы гарантировать, что выполнение продолжается, даже если определенные элементы не найдены или если есть проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Вклад

Вклад в этот модуль приветствуется. Убедитесь, что любые изменения хорошо задокументированы и включают соответствующие тесты.

## Лицензия

Этот модуль лицензирован в соответствии с лицензией MIT. Подробности см. в файле `LICENSE`.