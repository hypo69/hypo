# Модуль `src.webdriver.executor`

## Обзор

Модуль `src.webdriver.executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами. Он позволяет находить элементы на странице по различным локаторам (например, `id`, `class`, `xpath`), выполнять с ними различные действия (например, клик, ввод текста) и получать значения их атрибутов. Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для обработки взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Методы**:
- `__post_init__`: Инициализирует объект `ActionChains` после создания экземпляра класса, если драйвер передан.
- `execute_locator`: Выполняет действия с веб-элементом на основе предоставленного локатора.
- `_evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Извлекает атрибуты из веб-элемента или списка веб-элементов.
- `get_webelement_by_locator`: Извлекает веб-элемент или список элементов на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

**Параметры**:
- `driver` (Optional[object]): Экземпляр веб-драйвера Selenium.
- `actions` (ActionChains): Объект ActionChains для выполнения сложных действий с веб-элементами.
- `mode` (str): Режим работы (по умолчанию "debug").

**Примеры**

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from selenium.webdriver.common.by import By

# Инициализация драйвера (пример для Chrome)
driver = webdriver.Chrome()

# Создание экземпляра ExecuteLocator
executor = ExecuteLocator(driver=driver)

# Пример локатора
locator = {
    'by': By.ID,
    'selector': 'my_element_id',
    'attribute': 'value'
}

# Пример выполнения локатора
async def main():
    result = await executor.execute_locator(locator=locator)
    print(result)

# Запуск асинхронной функции (пример)
# asyncio.run(main())
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Optional message for actions like send_keys or type.
            typing_speed: Typing speed for send_keys events (seconds).

        Returns:
            The result of the operation, which can be a string, list, dict, WebElement, bool, or None.
        """
```

**Описание**: Выполняет действия с веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Необязательное сообщение для таких действий, как `send_keys` или `type`. По умолчанию `None`.
- `typing_speed` (Optional[float], optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, логическим значением или `None`.

**Примеры**:

```python
# Пример вызова функции execute_locator
locator = {
    'by': By.ID,
    'selector': 'my_element_id',
    'attribute': 'value'
}
# asyncio.run(executor.execute_locator(locator=locator, timeout=10))
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

**Описание**: Оценивает и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Оцененный атрибут, который может быть строкой, списком строк или словарем.

**Примеры**:

```python
# Пример вызова функции _evaluate_locator
# executor._evaluate_locator(attribute='%ENTER%')
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Not used in this function.
            typing_speed: Not used in this function.

        Returns:
            The attribute value(s) as a WebElement, list of WebElements, or None if not found.
        """
```

**Описание**: Извлекает атрибуты из веб-элемента или списка веб-элементов.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.

**Возвращает**:
- `Optional[WebElement | list[WebElement]]`: Значение атрибута (или значения) в виде веб-элемента, списка веб-элементов или `None`, если не найдено.

**Примеры**:

```python
# Пример вызова функции get_attribute_by_locator
locator = {
    'by': By.ID,
    'selector': 'my_element_id',
    'attribute': 'value'
}
# asyncio.run(executor.get_attribute_by_locator(locator=locator, timeout=10))
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').

        Returns:
           WebElement, list of WebElements, or None if not found.
        """
```

**Описание**: Извлекает веб-элемент или список элементов на основе предоставленного локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: Веб-элемент, список веб-элементов или `None`, если не найдено.

**Примеры**:

```python
# Пример вызова функции get_webelement_by_locator
locator = {
    'by': By.ID,
    'selector': 'my_element_id'
}
# asyncio.run(executor.get_webelement_by_locator(locator=locator, timeout=10))
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
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
- `timeout` (float, optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.
- `webelement` (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

**Возвращает**:
- `Optional[BinaryIO]`: Бинарный поток скриншота или `None`, если не удалось.

**Примеры**:

```python
# Пример вызова функции get_webelement_as_screenshot
locator = {
    'by': By.ID,
    'selector': 'my_element_id'
}
# asyncio.run(executor.get_webelement_as_screenshot(locator=locator, timeout=10))
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Optional message to send with the event.
            typing_speed: Typing speed for send_keys events (seconds).

        Returns:
            The result of the event execution (str, list of str, bytes, list of bytes, or bool).
        """
```

**Описание**: Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Необязательное сообщение для отправки с событием. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события (строка, список строк, байты, список байтов или логическое значение).

**Примеры**:

```python
# Пример вызова функции execute_event
locator = {
    'by': By.ID,
    'selector': 'my_element_id',
    'event': 'click()'
}
# asyncio.run(executor.execute_event(locator=locator, timeout=10))
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
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').
            message: Message to send to the web element.
            typing_speed: Typing speed for send_keys events (seconds).

        Returns:
            True if the message was sent successfully, False otherwise.
        """
```

**Описание**: Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати для событий `send_keys` (в секундах). По умолчанию `0`.

**Возвращает**:
- `bool`: `True`, если сообщение отправлено успешно, `False` в противном случае.

**Примеры**:

```python
# Пример вызова функции send_message
locator = {
    'by': By.ID,
    'selector': 'my_element_id'
}
# asyncio.run(executor.send_message(locator=locator, timeout=10, message='Hello, world!'))