# Модуль `executor`

## Обзор

Модуль `executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок. Модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами, позволяя находить элементы на странице по различным локаторам, выполнять с ними различные действия и получать значения их атрибутов.

## Подробней

Этот модуль предназначен для выполнения действий над веб-элементами, используя Selenium. Он включает в себя класс `ExecuteLocator`, который предоставляет методы для поиска элементов, выполнения различных действий (например, клик, ввод текста) и получения значений их атрибутов. Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.
В проекте `hypotez` данный модуль используется для автоматизации взаимодействия с веб-интерфейсом, позволяя выполнять задачи, такие как заполнение форм, навигация по сайту и сбор данных.

## Классы

### `ExecuteLocator`

**Описание**: Класс для обработки взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Методы**:
- `__post_init__`: Инициализирует объект `ActionChains` после создания экземпляра класса.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `_evaluate_locator`: Вычисляет и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Извлекает атрибуты из веб-элемента или списка веб-элементов.
- `get_webelement_by_locator`: Извлекает веб-элемент или список элементов на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

**Параметры**:
- `driver` (Optional[object], optional): Экземпляр веб-драйвера Selenium. По умолчанию `None`.
- `actions` (ActionChains): Объект `ActionChains` для выполнения цепочки действий. Инициализируется автоматически.
- `mode` (str, optional): Режим работы (например, `debug`). По умолчанию `"debug"`.

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

# Инициализация веб-драйвера
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Пример использования execute_locator
locator = {"by": "id", "selector": "myElement", "attribute": "value"}
result = await executor.execute_locator(locator)

print(result)

# Закрытие веб-драйвера
driver.quit()
```

## Функции

### `execute_locator`

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
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').
        message: Optional message for actions like send_keys or type.
        typing_speed: Typing speed for send_keys events (seconds).

    Returns:
        The result of the operation, which can be a string, list, dict, WebElement, bool, or None.
    """
```

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Сообщение для таких действий, как `send_keys` или `type`. По умолчанию `None`.
- `typing_speed` (Optional[float], optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, логическим значением или `None`.

**Примеры**:

```python
locator = {"by": "id", "selector": "myElement", "attribute": "value"}
result = await executor.execute_locator(locator)
print(result)
```

### `_evaluate_locator`

```python
def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Args:
        attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

    Returns:
        The evaluated attribute, which can be a string, list of strings, or dictionary.
    """
```

**Описание**: Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Примеры**:

```python
attribute = "%TAB%"
evaluated_attribute = executor._evaluate_locator(attribute)
print(evaluated_attribute)
```

### `get_attribute_by_locator`

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
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').
        message: Not used in this function.
        typing_speed: Not used in this function.

    Returns:
        The attribute value(s) as a WebElement, list of WebElements, or None if not found.
    """
```

**Описание**: Извлекает атрибуты из веб-элемента или списка веб-элементов.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (str, optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.

**Возвращает**:
- `Optional[WebElement | list[WebElement]]`: Значение(я) атрибута в виде веб-элемента, списка веб-элементов или `None`, если не найдено.

**Примеры**:

```python
locator = {"by": "id", "selector": "myElement", "attribute": "value"}
attribute_value = await executor.get_attribute_by_locator(locator)
print(attribute_value)
```

### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
) -> Optional[WebElement | List[WebElement]]:
    """
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').

    Returns:
       WebElement, list of WebElements, or None if not found.
    """
```

**Описание**: Извлекает веб-элемент или список элементов на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для поиска элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: Веб-элемент, список веб-элементов или `None`, если не найдено.

**Примеры**:

```python
locator = {"by": "id", "selector": "myElement"}
web_element = await executor.get_webelement_by_locator(locator)
print(web_element)
```

### `get_webelement_as_screenshot`

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
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').
        message: Not used in this function.
        typing_speed: Not used in this function.
        webelement: Optional pre-fetched web element.

    Returns:
       BinaryIO stream of the screenshot or None if failed.
    """
```

**Описание**: Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.
- `webelement` (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

**Возвращает**:
- `Optional[BinaryIO]`: Двоичный поток скриншота или `None`, если не удалось.

**Примеры**:

```python
locator = {"by": "id", "selector": "myElement"}
screenshot = await executor.get_webelement_as_screenshot(locator)
if screenshot:
    with open("screenshot.png", "wb") as f:
        f.write(screenshot)
```

### `execute_event`

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
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').
        message: Optional message to send with the event.
        typing_speed: Typing speed for send_keys events (seconds).

    Returns:
        The result of the event execution (str, list of str, bytes, list of bytes, or bool).
    """
```

**Описание**: Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки с событием. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события (строка, список строк, байты, список байтов или логическое значение).

**Примеры**:

```python
locator = {"by": "id", "selector": "myButton", "event": "click()"}
result = await executor.execute_event(locator)
print(result)
```

### `send_message`

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
    Args:
        locator: Locator data (dict or SimpleNamespace).
        timeout: Timeout for locating the element (seconds).
        timeout_for_event: Wait condition ('presence_of_element_located', 'visibility_of_all_elements_located').
        message: Message to send to the web element.
        typing_speed: Typing speed for send_keys events (seconds).

    Returns:
        True if the message was sent successfully, False otherwise.
    """
```

**Описание**: Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Время ожидания для поиска элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `bool`: `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Примеры**:

```python
locator = {"by": "id", "selector": "myTextField"}
message = "Hello, world!"
result = await executor.send_message(locator, message=message)
print(result)