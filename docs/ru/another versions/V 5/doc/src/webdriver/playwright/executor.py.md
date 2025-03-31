# Модуль `executor.py`

## Обзор

Модуль `executor.py` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации взаимодействия с веб-страницами через Playwright. Он предоставляет класс `PlaywrightExecutor`, который позволяет выполнять различные действия с веб-элементами, такие как клики, ввод текста, загрузка файлов и получение скриншотов. Модуль использует конфигурационный файл `playwrid.json` для настройки параметров запуска браузера.

## Классы

### `PlaywrightExecutor`

**Описание**: Класс `PlaywrightExecutor` выполняет команды на основе локаторов, используя Playwright.

**Как работает класс**:
Класс инициализируется с типом браузера и дополнительными аргументами. Он предоставляет методы для запуска и остановки Playwright, выполнения действий с веб-элементами на основе локаторов, получения атрибутов элементов, создания скриншотов и выполнения событий.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PlaywrightExecutor`.
- `start`: Запускает Playwright и открывает браузер.
- `stop`: Закрывает браузер и останавливает Playwright.
- `execute_locator`: Выполняет действия с веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает указанный атрибут из веб-элемента.
- `get_webelement_by_locator`: Получает веб-элемент, используя локатор.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.
- `goto`: Переходит по указанному URL.

#### `__init__`

```python
def __init__(self, browser_type: str = 'chromium', **kwargs) -> None:
    """
    Initializes the Playwright executor.

    Args:
        browser_type: Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit').
    """
```

**Описание**: Инициализирует экземпляр класса `PlaywrightExecutor`.

**Как работает функция**:
Конструктор класса `PlaywrightExecutor` инициализирует драйвер, тип браузера и загружает конфигурацию из файла `playwrid.json`.

**Параметры**:
- `browser_type` (str, optional): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`: Дополнительные аргументы.

#### `start`

```python
async def start(self) -> None:
    """
    Initializes Playwright and launches a browser instance.
    """
```

**Описание**: Инициализирует Playwright и запускает экземпляр браузера.

**Как работает функция**:
Метод `start` запускает Playwright, открывает браузер указанного типа и создает новую страницу.

**Вызывает исключения**:
- `Exception`: Если не удается запустить браузер.

#### `stop`

```python
async def stop(self) -> None:
    """
    Closes Playwright browser and stops its instance.
    """
```

**Описание**: Закрывает браузер Playwright и останавливает его экземпляр.

**Как работает функция**:
Метод `stop` закрывает текущую страницу, останавливает драйвер Playwright и устанавливает драйвер в `None`.

**Вызывает исключения**:
- `Exception`: Если не удается закрыть браузер.

#### `execute_locator`

```python
async def execute_locator(
        self,
        locator: Union[dict, SimpleNamespace],
        message: Optional[str] = None,
        typing_speed: float = 0,
        timeout: Optional[float] = 0,
        timeout_for_event: Optional[str] = 'presence_of_element_located',
) -> Union[str, list, dict, Locator, bool, None]:
    """
    Executes actions on a web element based on the provided locator.

    Args:
        locator: Locator data (dict or SimpleNamespace).
        message: Optional message for events.
        typing_speed: Optional typing speed for events.
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').

    Returns:
         The result of the operation, which can be a string, list, dict, Locator, bool, or None.
    """
```

**Описание**: Выполняет действия с веб-элементом на основе предоставленного локатора.

**Как работает функция**:
Метод `execute_locator` принимает локатор в виде словаря или `SimpleNamespace`, сообщение, скорость печати, таймаут и условие ожидания. Он вызывает внутреннюю функцию `_parse_locator` для разбора инструкций локатора и выполнения соответствующих действий.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию 0.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента (в секундах). По умолчанию 0.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, булевым значением или `None`.

#### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Evaluates and processes locator attributes.

    Args:
        attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

    Returns:
        The evaluated attribute, which can be a string, list of strings, or dictionary.
    """
```

**Описание**: Оценивает и обрабатывает атрибуты локатора.

**Как работает функция**:
Метод `evaluate_locator` принимает атрибут, который может быть строкой, списком строк или словарем. Он вызывает внутреннюю функцию `_evaluate` для обработки каждого атрибута.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Оцененный атрибут, который может быть строкой, списком строк или словарем.

#### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Gets the specified attribute from the web element.

    Args:
        locator: Locator data (dict or SimpleNamespace).

    Returns:
        Attribute or None.
    """
```

**Описание**: Получает указанный атрибут из веб-элемента.

**Как работает функция**:
Метод `get_attribute_by_locator` принимает локатор в виде словаря или `SimpleNamespace`. Он получает веб-элемент с помощью `get_webelement_by_locator` и извлекает значение атрибута.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Значение атрибута или `None`, если элемент не найден.

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Gets a web element using the locator.

    Args:
        locator: Locator data (dict or SimpleNamespace).

    Returns:
        Playwright Locator
    """
```

**Описание**: Получает веб-элемент, используя локатор.

**Как работает функция**:
Метод `get_webelement_by_locator` принимает локатор в виде словаря или `SimpleNamespace`. Он использует `locator.selector` и `locator.by` для поиска элемента на странице.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright `Locator` или `None`, если элемент не найден.

#### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Takes a screenshot of the located web element.

    Args:
        locator: Locator data (dict or SimpleNamespace).
        webelement: The web element Locator.

    Returns:
         Screenshot in bytes or None.
    """
```

**Описание**: Делает скриншот найденного веб-элемента.

**Как работает функция**:
Метод `get_webelement_as_screenshot` принимает локатор и необязательный веб-элемент. Если веб-элемент не предоставлен, он получает его с помощью `get_webelement_by_locator`. Затем он делает скриншот элемента и возвращает его в виде байтов.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `webelement` (Optional[Locator], optional): Веб-элемент `Locator`. По умолчанию `None`.

**Возвращает**:
- `Optional[bytes]`: Скриншот в виде байтов или `None`, если элемент не найден.

#### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]:
    """
    Executes the event associated with the locator.

     Args:
        locator: Locator data (dict or SimpleNamespace).
        message: Optional message for events.
        typing_speed: Optional typing speed for events.

    Returns:
       Execution status.
    """
```

**Описание**: Выполняет событие, связанное с локатором.

**Как работает функция**:
Метод `execute_event` принимает локатор, сообщение и скорость печати. Он разделяет строку событий на отдельные события и выполняет их одно за другим. Поддерживаемые события: `click()`, `pause()`, `upload_media()`, `screenshot()`, `clear()`, `send_keys()`, `type()`.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию 0.

**Возвращает**:
- `Union[str, List[str], bytes, List[bytes], bool]`: Статус выполнения.

#### `send_message`

```python
async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
    """Sends a message to a web element.

    Args:
         locator: Information about the element's location on the page.
         message: The message to be sent to the web element.
         typing_speed: Speed of typing the message in seconds.

    Returns:
        Returns `True` if the message was sent successfully, `False` otherwise.
    """
```

**Описание**: Отправляет сообщение веб-элементу.

**Как работает функция**:
Метод `send_message` принимает локатор, сообщение и скорость печати. Он получает веб-элемент с помощью `get_webelement_by_locator` и отправляет сообщение, используя `element.type()`.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати сообщения в секундах. По умолчанию 0.

**Возвращает**:
- `bool`: `True`, если сообщение было отправлено успешно, `False` в противном случае.

#### `goto`

```python
async def goto(self, url: str) -> None:
    """
    Navigates to a specified URL.

    Args:
        url: URL to navigate to.
    """
```

**Описание**: Переходит по указанному URL.

**Как работает функция**:
Метод `goto` принимает URL и переходит по нему, используя `self.page.goto()`.

**Параметры**:
- `url` (str): URL для перехода.

**Вызывает исключения**:
- `Exception`: Если не удается перейти по URL.