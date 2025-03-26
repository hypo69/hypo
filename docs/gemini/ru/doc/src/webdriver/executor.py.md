# src.webdriver.executor

## Обзор

Модуль `src.webdriver.executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Классы

### `ExecuteLocator`

**Описание**:
Класс `ExecuteLocator` обрабатывает взаимодействие с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Методы**:
- `__post_init__`: Инициализирует экземпляр класса `ExecuteLocator` и создает экземпляр `ActionChains`.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `_evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Извлекает атрибуты из веб-элемента или списка веб-элементов.
- `get_webelement_by_locator`: Извлекает веб-элемент или список элементов на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот расположенного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

#### `__post_init__`

```python
def __post_init__(self) -> None:
    """
    Инициализирует экземпляр класса `ExecuteLocator` и создает экземпляр `ActionChains`.

    Args:
        None

    Returns:
        None
    """
```

#### `execute_locator`

```python
async def execute_locator(
    self,
    locator:  dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
    message: Optional[str] = None,
    typing_speed: Optional[float] = 0,
) ->  Optional[str | list | dict | WebElement | bool]:
    """
    Выполняет действия над веб-элементом на основе предоставленного локатора.

    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
        timeout_for_event (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
        message (Optional[str], optional): Сообщение для таких действий, как `send_keys` или `type`. По умолчанию `None`.
        typing_speed (Optional[float], optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

    Returns:
        Optional[str | list | dict | WebElement | bool]: Результат операции, который может быть строкой, списком, словарем, WebElement, булевым значением или `None`.
    """
```

#### `_evaluate_locator`

```python
def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Оценивает и обрабатывает атрибуты локатора.

    Args:
        attribute (str | List[str] | dict): Атрибут для оценки (может быть строкой, списком строк или словарем).

    Returns:
        Optional[str | List[str] | dict]: Оцененный атрибут, который может быть строкой, списком строк или словарем.
    """
```

#### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(
    self,
    locator: SimpleNamespace | dict,
    timeout: Optional[float] = 0,
    timeout_for_event: str = "presence_of_element_located",
    message: Optional[str] = None,
    typing_speed: float = 0,
) -> Optional[WebElement | list[WebElement]]:
    """
    Извлекает атрибуты из веб-элемента или списка веб-элементов.

    Args:
        locator (SimpleNamespace | dict): Данные локатора.
        timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
        timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
        message (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
        typing_speed (float, optional): Не используется в этой функции. По умолчанию `0`.

    Returns:
        Optional[WebElement | list[WebElement]]: Значение(я) атрибута в виде WebElement, списка WebElements или `None`, если не найдено.
    """
```

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
) -> Optional[WebElement | List[WebElement]]:
    """
    Извлекает веб-элемент или список элементов на основе предоставленного локатора.

    Args:
        locator (dict | SimpleNamespace): Данные локатора.
        timeout (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
        timeout_for_event (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.

    Returns:
        Optional[WebElement | List[WebElement]]: WebElement, список WebElements или `None`, если не найдено.
    """
```

#### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = "presence_of_element_located",
    message: Optional[str] = None,
    typing_speed: float = 0,
    webelement: Optional[WebElement] = None,
) -> Optional[BinaryIO]:
    """
    Делает скриншот расположенного веб-элемента.

    Args:
        locator (SimpleNamespace | dict): Данные локатора.
        timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
        timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
        message (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
        typing_speed (float, optional): Не используется в этой функции. По умолчанию `0`.
        webelement (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

    Returns:
        Optional[BinaryIO]: BinaryIO поток скриншота или `None`, если не удалось.
    """
```

#### `execute_event`

```python
async def execute_event(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = "presence_of_element_located",
    message: str = None,
    typing_speed: float = 0,
) -> Optional[str | list[str] | bytes | list[bytes] | bool]:
    """
    Выполняет событие, связанное с локатором.

    Args:
        locator (SimpleNamespace | dict): Данные локатора.
        timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
        timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
        message (str, optional): Сообщение для отправки с событием. По умолчанию `None`.
        typing_speed (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

    Returns:
        Optional[str | list[str] | bytes | list[bytes] | bool]: Результат выполнения события (str, список str, bytes, список bytes или bool).
    """
```

#### `send_message`

```python
async def send_message(
    self,
    locator: SimpleNamespace | dict,
    timeout: float = 5,
    timeout_for_event: str = "presence_of_element_located",
    message: str = None,
    typing_speed: float = 0,
) -> bool:
    """
    Отправляет сообщение веб-элементу.

    Args:
        locator (SimpleNamespace | dict): Данные локатора.
        timeout (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
        timeout_for_event (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
        message (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
        typing_speed (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

    Returns:
        bool: `True`, если сообщение отправлено успешно, `False` в противном случае.
    """
```