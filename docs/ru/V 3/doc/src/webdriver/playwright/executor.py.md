# src.webdriver.playwright.executor

## Обзор

Модуль `src.webdriver.playwright.executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами через Playwright. Он позволяет выполнять различные действия, такие как клики, ввод текста, загрузка файлов и получение скриншотов элементов. Модуль использует асинхронный подход для обеспечения высокой производительности и эффективного управления ресурсами.

## Классы

### `PlaywrightExecutor`

**Описание**:
Класс `PlaywrightExecutor` выполняет команды на основе локаторов в стиле executor, используя Playwright.

**Методы**:
- `__init__`: Инициализирует экземпляр `PlaywrightExecutor`.
- `start`: Запускает Playwright и инициализирует браузер.
- `stop`: Закрывает браузер Playwright и останавливает его экземпляр.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Вычисляет и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает указанный атрибут из веб-элемента.
- `get_webelement_by_locator`: Получает веб-элемент, используя локатор.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.
- `goto`: Переходит по указанному URL.

**Параметры**:
- `browser_type` (str): Тип запускаемого браузера (например, 'chromium', 'firefox', 'webkit').

**Примеры**:

```python
executor = PlaywrightExecutor(browser_type='chromium')
await executor.start()
# ... выполнение действий ...
await executor.stop()
```

## Функции

### `__init__`

```python
def __init__(self, browser_type: str = 'chromium', **kwargs):
    """
    Args:
        browser_type (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit').
    """
```

**Описание**:
Инициализирует экземпляр `PlaywrightExecutor`.

**Параметры**:
- `browser_type` (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`: Дополнительные параметры.

**Примеры**:

```python
executor = PlaywrightExecutor(browser_type='firefox')
```

### `start`

```python
async def start(self) -> None:
    """
    """
```

**Описание**:
Инициализирует Playwright и запускает экземпляр браузера.

**Вызывает исключения**:
- `Exception`: Если не удается запустить браузер Playwright.

**Примеры**:

```python
await executor.start()
```

### `stop`

```python
async def stop(self) -> None:
    """
    """
```

**Описание**:
Закрывает браузер Playwright и останавливает его экземпляр.

**Вызывает исключения**:
- `Exception`: Если не удается закрыть браузер Playwright.

**Примеры**:

```python
await executor.stop()
```

### `execute_locator`

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
    Args:
        locator: Данные локатора (dict или SimpleNamespace).
        message: Дополнительное сообщение для событий.
        typing_speed: Дополнительная скорость ввода для событий.
        timeout: Тайм-аут для поиска элемента (в секундах).
        timeout_for_event: Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located').

    Returns:
         Результат операции, который может быть строкой, списком, словарем, Locator, bool или None.
    """
```

**Описание**:
Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора (словарь или `SimpleNamespace`).
- `message` (Optional[str], optional): Дополнительное сообщение для событий. По умолчанию `None`.
- `typing_speed` (float): Дополнительная скорость ввода для событий. По умолчанию 0.
- `timeout` (Optional[float], optional): Тайм-аут для поиска элемента (в секундах). По умолчанию 0.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию 'presence_of_element_located'.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, `Locator`, `bool` или `None`.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//button', 'event': 'click()'}
result = await executor.execute_locator(locator_data)
```

### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Args:
        attribute: Атрибут для вычисления (может быть строкой, списком строк или словарем).

    Returns:
        Вычисленный атрибут, который может быть строкой, списком строк или словарем.
    """
```

**Описание**:
Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Примеры**:

```python
attribute = await executor.evaluate_locator('some_attribute')
```

### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Args:
        locator: Данные локатора (dict или SimpleNamespace).

    Returns:
        Атрибут или None.
    """
```

**Описание**:
Получает указанный атрибут из веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или `SimpleNamespace`).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Атрибут или `None`.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//input', 'attribute': 'value'}
attribute = await executor.get_attribute_by_locator(locator_data)
```

### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Args:
        locator: Данные локатора (dict или SimpleNamespace).

    Returns:
        Playwright Locator
    """
```

**Описание**:
Получает веб-элемент, используя локатор.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или `SimpleNamespace`).

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright `Locator`.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//div'}
element = await executor.get_webelement_by_locator(locator_data)
```

### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Args:
        locator: Данные локатора (dict или SimpleNamespace).
        webelement: Веб-элемент Locator.

    Returns:
         Скриншот в байтах или None.
    """
```

**Описание**:
Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или `SimpleNamespace`).
- `webelement` (Optional[Locator], optional): Веб-элемент `Locator`. По умолчанию `None`.

**Возвращает**:
- `Optional[bytes]`: Скриншот в байтах или `None`.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//img'}
screenshot = await executor.get_webelement_as_screenshot(locator_data)
if screenshot:
    with open('screenshot.png', 'wb') as f:
        f.write(screenshot)
```

### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]:
    """
     Args:
        locator: Данные локатора (dict или SimpleNamespace).
        message: Дополнительное сообщение для событий.
        typing_speed: Дополнительная скорость ввода для событий.

    Returns:
       Execution status.
    """
```

**Описание**:
Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или `SimpleNamespace`).
- `message` (Optional[str], optional): Дополнительное сообщение для событий. По умолчанию `None`.
- `typing_speed` (float): Дополнительная скорость ввода для событий. По умолчанию 0.

**Возвращает**:
- `Union[str, List[str], bytes, List[bytes], bool]`: Статус выполнения.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//button', 'event': 'click()'}
status = await executor.execute_event(locator_data)
```

### `send_message`

```python
async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
    """
    Args:
         locator: Информация о местоположении элемента на странице.
         message: Сообщение для отправки веб-элементу.
         typing_speed: Скорость ввода сообщения в секундах.

    Returns:
        Возвращает `True`, если сообщение было отправлено успешно, `False` в противном случае.
    """
```

**Описание**:
Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
- `typing_speed` (float): Скорость ввода сообщения в секундах. По умолчанию 0.

**Возвращает**:
- `bool`: Возвращает `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Примеры**:

```python
locator_data = {'by': 'XPATH', 'selector': '//input'}
status = await executor.send_message(locator_data, 'Hello, World!')
```

### `goto`

```python
async def goto(self, url: str) -> None:
    """
    Args:
        url: URL для перехода.
    """
```

**Описание**:
Переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Вызывает исключения**:
- `Exception`: Если не удается перейти по указанному URL.

**Примеры**:

```python
await executor.goto('https://www.example.com')