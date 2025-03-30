# Модуль `executor`

## Обзор

Модуль `executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль предназначен для выполнения действий над веб-элементами с использованием библиотеки Playwright. Он включает в себя класс `PlaywrightExecutor`, который инициализирует браузер, выполняет поиск элементов на странице и выполняет различные действия, такие как клики, ввод текста и получение атрибутов. Модуль также обеспечивает обработку ошибок и логирование.

## Классы

### `PlaywrightExecutor`

**Описание**: Класс `PlaywrightExecutor` выполняет команды на основе команд локаторов в стиле исполнителя, используя Playwright.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PlaywrightExecutor`.
- `start`: Запускает Playwright и инициализирует экземпляр браузера.
- `stop`: Закрывает браузер Playwright и останавливает его экземпляр.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Вычисляет и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает указанный атрибут из веб-элемента.
- `get_webelement_by_locator`: Получает веб-элемент с использованием локатора.
- `get_webelement_as_screenshot`: Делает снимок экрана расположенного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.
- `goto`: Переходит по указанному URL.

**Параметры**:
- `browser_type` (str): Тип запускаемого браузера (например, "chromium", "firefox", "webkit"). По умолчанию: "chromium".
- `**kwargs`: Дополнительные параметры конфигурации.

**Примеры**
```python
    executor = PlaywrightExecutor(browser_type='chromium')
    await executor.start()
    # ... выполнение действий ...
    await executor.stop()
```

## Функции

### `start`

```python
async def start(self) -> None:
    """
    Initializes Playwright and launches a browser instance.
    """
```

**Описание**: Инициализирует Playwright и запускает экземпляр браузера.

**Вызывает исключения**:
- `Exception`: Если не удается запустить браузер Playwright.

**Примеры**:
```python
    executor = PlaywrightExecutor(browser_type='chromium')
    await executor.start()
```

### `stop`

```python
async def stop(self) -> None:
    """
    Closes Playwright browser and stops its instance.
    """
```

**Описание**: Закрывает браузер Playwright и останавливает его экземпляр.

**Вызывает исключения**:
- `Exception`: Если не удается закрыть браузер Playwright.

**Примеры**:
```python
    executor = PlaywrightExecutor(browser_type='chromium')
    await executor.start()
    # ... выполнение действий ...
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
    Executes actions on a web element based on the provided locator.
    """
```

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора.
- `message` (Optional[str], optional): Необязательное сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Необязательная скорость ввода для событий. По умолчанию `0`.
- `timeout` (Optional[float], optional): Время ожидания для определения местоположения элемента (в секундах). По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания ("presence_of_element_located", "visibility_of_all_elements_located"). По умолчанию `'presence_of_element_located'`.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, булевым значением или `None`.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//input[@id="username"]', 'attribute': 'value'}
    result = await executor.execute_locator(locator_data)
    print(result)
```

### `evaluate_locator`

```python
async def evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    """
    Evaluates and processes locator attributes.
    """
```

**Описание**: Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Примеры**:
```python
    attribute = '//input[@id="username"]/@value'
    result = await executor.evaluate_locator(attribute)
    print(result)
```

### `get_attribute_by_locator`

```python
async def get_attribute_by_locator(self, locator: dict | SimpleNamespace) -> Optional[str | List[str] | dict]:
    """
    Gets the specified attribute from the web element.
    """
```

**Описание**: Получает указанный атрибут из веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Атрибут или `None`.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//input[@id="username"]', 'attribute': 'value'}
    result = await executor.get_attribute_by_locator(locator_data)
    print(result)
```

### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(self, locator: dict | SimpleNamespace) -> Optional[Locator | List[Locator]]:
    """
    Gets a web element using the locator.
    """
```

**Описание**: Получает веб-элемент с использованием локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright Locator.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//input[@id="username"]'}
    element = await executor.get_webelement_by_locator(locator_data)
    if element:
        print("Element found")
```

### `get_webelement_as_screenshot`

```python
async def get_webelement_as_screenshot(self, locator: dict | SimpleNamespace, webelement: Optional[Locator] = None) -> Optional[bytes]:
    """
    Takes a screenshot of the located web element.
    """
```

**Описание**: Делает снимок экрана расположенного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `webelement` (Optional[Locator], optional): Веб-элемент Locator. По умолчанию `None`.

**Возвращает**:
- `Optional[bytes]`: Снимок экрана в байтах или `None`.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//input[@id="username"]'}
    screenshot = await executor.get_webelement_as_screenshot(locator_data)
    if screenshot:
        with open('screenshot.png', 'wb') as f:
            f.write(screenshot)
```

### `execute_event`

```python
async def execute_event(self, locator: dict | SimpleNamespace, message: Optional[str] = None, typing_speed: float = 0) -> Union[str, List[str], bytes, List[bytes], bool]:
    """
    Executes the event associated with the locator.
    """
```

**Описание**: Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Необязательное сообщение для событий. По умолчанию `None`.
- `typing_speed` (float, optional): Необязательная скорость ввода для событий. По умолчанию `0`.

**Возвращает**:
- `Union[str, List[str], bytes, List[bytes], bool]`: Статус выполнения.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//button[@id="submit"]', 'event': 'click()'}
    result = await executor.execute_event(locator_data)
    print(result)
```

### `send_message`

```python
async def send_message(self, locator: dict | SimpleNamespace, message: str = None, typing_speed: float = 0) -> bool:
    """Sends a message to a web element.
    """
```

**Описание**: Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str, optional): Сообщение, которое нужно отправить веб-элементу. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость ввода сообщения в секундах. По умолчанию `0`.

**Возвращает**:
- `bool`: Возвращает `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Примеры**:
```python
    locator_data = {'by': 'XPATH', 'selector': '//input[@id="username"]'}
    result = await executor.send_message(locator_data, "test_username")
    print(result)
```

### `goto`

```python
async def goto(self, url: str) -> None:
    """
    Navigates to a specified URL.
    """
```

**Описание**: Переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Вызывает исключения**:
- `Exception`: Если во время навигации возникает ошибка.

**Примеры**:
```python
    await executor.goto("https://www.example.com")