# Модуль `executor.py`

## Обзор

Модуль `executor.py` предоставляет класс `PlaywrightExecutor`, который используется для выполнения команд на веб-страницах с использованием библиотеки Playwright. Он поддерживает запуск, остановку браузера, поиск элементов, выполнение событий и получение атрибутов.

## Оглавление

- [Классы](#классы)
    - [`PlaywrightExecutor`](#playwrightexecutor)
- [Функции](#функции)
    - [`_parse_locator`](#_parse_locator)
    - [`evaluate_locator`](#evaluate_locator)
    - [`_evaluate`](#_evaluate)
    - [`get_attribute_by_locator`](#get_attribute_by_locator)
    - [`_parse_dict_string`](#_parse_dict_string)
    - [`_get_attribute`](#_get_attribute)
    - [`_get_attributes_from_dict`](#_get_attributes_from_dict)
    - [`get_webelement_by_locator`](#get_webelement_by_locator)
    - [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
    - [`execute_event`](#execute_event)
    - [`send_message`](#send_message)
    - [`goto`](#goto)

## Классы

### `PlaywrightExecutor`

**Описание**: Класс для выполнения команд с использованием Playwright.

**Методы**:

- `__init__`: Инициализирует экземпляр `PlaywrightExecutor`.
- `start`: Запускает браузер Playwright.
- `stop`: Останавливает браузер Playwright.
- `execute_locator`: Выполняет действие на основе локатора и события.
- `evaluate_locator`: Обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает атрибут из веб-элемента.
- `get_webelement_by_locator`: Получает веб-элемент по локатору.
- `get_webelement_as_screenshot`: Делает скриншот веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение в веб-элемент.
- `goto`: Переходит по указанному URL.

#### `__init__`

```python
def __init__(self, browser_type: str = 'chromium', **kwargs) -> None:
    """
    Args:
        browser_type (str, optional): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
        **kwargs: Дополнительные аргументы.
    
    Returns:
        None
    """
```

**Описание**: Инициализирует `PlaywrightExecutor` с заданным типом браузера.

**Параметры**:

- `browser_type` (str, optional): Тип браузера для запуска. По умолчанию `'chromium'`.
- `**kwargs`: Дополнительные аргументы.

#### `start`

```python
async def start(self) -> None:
    """
    Args:
        None

    Returns:
         None
    
    Raises:
        Exception: В случае ошибки запуска браузера.
    """
```

**Описание**: Запускает браузер Playwright.

**Параметры**:

- Нет.

**Возвращает**:

- Нет.

**Вызывает исключения**:

- `Exception`: В случае ошибки запуска браузера.

#### `stop`

```python
async def stop(self) -> None:
    """
    Args:
       None
    
    Returns:
        None
    
    Raises:
        Exception: В случае ошибки остановки браузера.
    """
```

**Описание**: Останавливает браузер Playwright.

**Параметры**:

- Нет.

**Возвращает**:

- Нет.

**Вызывает исключения**:

- `Exception`: В случае ошибки остановки браузера.

#### `execute_locator`

```python
async def execute_locator(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | dict | bytes | bool:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        message (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
        typing_speed (float, optional): Скорость печати для событий. По умолчанию `0`.

    Returns:
        str | List[str] | dict | bytes | bool: Результат операции.
    """
```

**Описание**: Выполняет действия на основе локатора и события.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:

- `str | List[str] | dict | bytes | bool`: Результат операции.

#### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Args:
       attribute (str | List[str] | dict): Атрибуты для обработки.
    
    Returns:
       Optional[str | List[str] | dict]: Обработанные атрибуты.
    """
```

**Описание**: Обрабатывает атрибуты локатора.

**Параметры**:

- `attribute` (str | List[str] | dict): Атрибуты для обработки.

**Возвращает**:

- `Optional[str | List[str] | dict]`: Обработанные атрибуты.

#### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.

    Returns:
        Optional[str | List[str] | dict]: Атрибут или `None`.
    """
```

**Описание**: Получает атрибут из веб-элемента.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:

- `Optional[str | List[str] | dict]`: Атрибут или `None`.

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
    
    Returns:
        Optional[Locator | List[Locator]]: Playwright Locator или `None`.
    
    Raises:
        ValueError: В случае некорректного локатора.
    """
```

**Описание**: Получает веб-элемент по локатору.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:

- `Optional[Locator | List[Locator]]`: Playwright Locator или `None`.

**Вызывает исключения**:

- `ValueError`: В случае некорректного локатора.

#### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        webelement (Optional[Locator], optional): Веб-элемент Locator. По умолчанию `None`.

    Returns:
        Optional[bytes]: Скриншот в байтах или `None`.
    """
```

**Описание**: Делает скриншот веб-элемента.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `webelement` (Optional[Locator], optional): Веб-элемент Locator. По умолчанию `None`.

**Возвращает**:

- `Optional[bytes]`: Скриншот в байтах или `None`.

#### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> str | List[str] | bytes | List[bytes] | bool:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        message (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
        typing_speed (float, optional): Скорость печати для событий. По умолчанию `0`.

    Returns:
        str | List[str] | bytes | List[bytes] | bool: Статус выполнения.
    """
```

**Описание**: Выполняет событие, связанное с локатором.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий. По умолчанию `0`.

**Возвращает**:

- `str | List[str] | bytes | List[bytes] | bool`: Статус выполнения.

#### `send_message`

```python
async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        message (str, optional): Сообщение для отправки. По умолчанию `None`.
        typing_speed (float, optional): Скорость печати сообщения в секундах. По умолчанию `0`.

    Returns:
        bool: `True`, если сообщение отправлено успешно, `False` в противном случае.
    """
```

**Описание**: Отправляет сообщение в веб-элемент.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (str, optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати сообщения в секундах. По умолчанию `0`.

**Возвращает**:

- `bool`: `True`, если сообщение отправлено успешно, `False` в противном случае.

#### `goto`

```python
async def goto(self, url: str) -> None:
    """
    Args:
        url (str): URL для перехода.
    
    Returns:
        None

    Raises:
        Exception: При ошибке навигации.
    """
```

**Описание**: Переходит по указанному URL.

**Параметры**:

- `url` (str): URL для перехода.

**Возвращает**:

- Нет.

**Вызывает исключения**:

- `Exception`: При ошибке навигации.

## Функции

### `_parse_locator`

```python
async def _parse_locator(locator: dict | SimpleNamespace, message: Optional[str]) -> str | List[str] | dict | bytes | bool:
    """
    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        message (Optional[str], optional): Сообщение для отправки. По умолчанию `None`.

    Returns:
        str | List[str] | dict | bytes | bool: Результат выполнения.
    """
```

**Описание**: Разбирает и выполняет инструкции локатора.

**Параметры**:

- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для отправки. По умолчанию `None`.

**Возвращает**:

- `str | List[str] | dict | bytes | bool`: Результат выполнения.

### `_evaluate`

```python
async def _evaluate(attr: str) -> Optional[str]:
    """
    Args:
        attr (str): Атрибут для обработки.
    
    Returns:
        Optional[str]: Обработанный атрибут.
    """
```

**Описание**:  Обрабатывает атрибуты.

**Параметры**:

- `attr` (str): Атрибут для обработки.

**Возвращает**:

- `Optional[str]`: Обработанный атрибут.

### `_parse_dict_string`

```python
def _parse_dict_string(attr_string: str) -> dict | None:
    """
    Args:
        attr_string (str): Строка, представляющая структуру, похожую на словарь.

    Returns:
        dict | None: Разобранный словарь или `None`, если разбор не удался.
    """
```

**Описание**: Разбирает строку вида `'{attr1:attr2}'` в словарь.

**Параметры**:

- `attr_string` (str): Строка, представляющая структуру, похожую на словарь.

**Возвращает**:

- `dict | None`: Разобранный словарь или `None`, если разбор не удался.

### `_get_attribute`

```python
async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
    """
    Args:
        el (Locator): Веб-элемент.
        attr (str): Имя атрибута.

    Returns:
        Optional[str]: Значение атрибута или `None`.
    """
```

**Описание**: Получает атрибут из `Locator`.

**Параметры**:

- `el` (Locator): Веб-элемент.
- `attr` (str): Имя атрибута.

**Возвращает**:

- `Optional[str]`: Значение атрибута или `None`.

### `_get_attributes_from_dict`

```python
async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
    """
    Args:
        element (Locator): Веб-элемент для получения атрибутов.
        attr_dict (dict): Словарь, ключи/значения которого представляют имена атрибутов.

    Returns:
        dict: Словарь с атрибутами и их значениями.
    """
```

**Описание**: Получает несколько атрибутов на основе словаря.

**Параметры**:

- `element` (Locator): Веб-элемент для получения атрибутов.
- `attr_dict` (dict): Словарь, ключи/значения которого представляют имена атрибутов.

**Возвращает**:

- `dict`: Словарь с атрибутами и их значениями.