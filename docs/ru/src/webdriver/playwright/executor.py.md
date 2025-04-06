# Модуль `executor.py`

## Обзор

Модуль `executor.py` предоставляет функциональность для взаимодействия с веб-элементами с использованием Playwright на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации взаимодействия с веб-страницами с использованием библиотеки Playwright. Он предоставляет класс `PlaywrightExecutor`, который инициализирует Playwright, запускает браузер, выполняет действия с веб-элементами на основе локаторов и обрабатывает ошибки. Модуль использует асинхронный подход для обеспечения высокой производительности и эффективного использования ресурсов.

## Классы

### `PlaywrightExecutor`

**Описание**: Класс `PlaywrightExecutor` предназначен для выполнения команд на основе локаторов в стиле executor с использованием Playwright.

**Принцип работы**:
Класс инициализируется с указанием типа браузера (например, 'chromium', 'firefox', 'webkit'). Он предоставляет методы для запуска и остановки Playwright, выполнения действий с веб-элементами на основе предоставленных локаторов, получения атрибутов элементов, выполнения событий (например, кликов, ввода текста) и навигации по URL.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `PlaywrightExecutor`.
- `start`: Запускает Playwright и браузер.
- `stop`: Закрывает браузер и останавливает Playwright.
- `execute_locator`: Выполняет действия с веб-элементом на основе предоставленного локатора.
- `evaluate_locator`: Оценивает и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает указанный атрибут веб-элемента.
- `get_webelement_by_locator`: Получает веб-элемент, используя локатор.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.
- `goto`: Переходит по указанному URL.

### `__init__`

```python
    def __init__(self, browser_type: str = 'chromium', **kwargs):
        """
        Initializes the Playwright executor.

        Args:
            browser_type: Type of browser to launch (e.g., 'chromium', 'firefox', 'webkit').
        """
```

**Назначение**: Инициализирует экземпляр класса `PlaywrightExecutor`.

**Параметры**:
- `browser_type` (str): Тип браузера для запуска (например, 'chromium', 'firefox', 'webkit'). По умолчанию 'chromium'.
- `**kwargs`: Дополнительные именованные аргументы.

**Как работает функция**:
1. Инициализирует драйвер в `None`.
2. Устанавливает тип браузера `browser_type`.
3. Инициализирует страницу в `None`.
4. Загружает конфигурацию из файла `playwrid.json` и сохраняет ее в атрибуте `config`.

**Примеры**:
```python
executor = PlaywrightExecutor(browser_type='firefox')
```

### `start`

```python
    async def start(self) -> None:
        """
        Initializes Playwright and launches a browser instance.
        """
```

**Назначение**: Инициализирует Playwright и запускает экземпляр браузера.

**Как работает функция**:
1. Запускает Playwright с использованием `async_playwright().start()`.
2. Запускает браузер указанного типа (например, chromium, firefox) в режиме headless.
3. Создает новую страницу в браузере.
4. Обрабатывает исключения, возникающие при запуске Playwright и браузера, и логирует их с использованием `logger.critical`.

```
A: Запуск Playwright
|
-- B: Запуск браузера
|
C: Создание страницы
```

Где:
- `A`: Инициализация Playwright с использованием `async_playwright().start()`.
- `B`: Запуск браузера указанного типа (например, chromium, firefox) в режиме headless.
- `C`: Создание новой страницы в браузере.

**Примеры**:
```python
await executor.start()
```

### `stop`

```python
    async def stop(self) -> None:
        """
        Closes Playwright browser and stops its instance.
        """
```

**Назначение**: Закрывает браузер Playwright и останавливает его экземпляр.

**Как работает функция**:
1. Закрывает текущую страницу, если она существует.
2. Останавливает драйвер Playwright, если он существует.
3. Устанавливает драйвер в `None`.
4. Логирует информацию об остановке Playwright с использованием `logger.info`.
5. Обрабатывает исключения, возникающие при закрытии браузера, и логирует их с использованием `logger.error`.

```
A: Проверка наличия страницы
|
-- B: Закрытие страницы
|
C: Проверка наличия драйвера
|
-- D: Остановка драйвера
|
E: Установка драйвера в None
```

Где:
- `A`: Проверяет, существует ли текущая страница (`self.page`).
- `B`: Закрывает страницу, если она существует (`await self.page.close()`).
- `C`: Проверяет, существует ли драйвер (`self.driver`).
- `D`: Останавливает драйвер, если он существует (`await self.driver.stop()`).
- `E`: Устанавливает драйвер в `None`.

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

**Назначение**: Выполняет действия с веб-элементом на основе предоставленного локатора.

**Параметры**:
- `locator` (Union[dict, SimpleNamespace]): Данные локатора (словарь или SimpleNamespace).
- `message` (Optional[str]): Необязательное сообщение для событий.
- `typing_speed` (float): Необязательная скорость ввода текста для событий.
- `timeout` (float): Время ожидания для поиска элемента (в секундах).
- `timeout_for_event` (str): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located').

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, булевым значением или None.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Проверяет, что локатор не пустой, и содержит атрибут и селектор.
3. Определяет внутреннюю асинхронную функцию `_parse_locator`, которая выполняет разбор и выполнение инструкций локатора.
4. Если `locator.event` и `locator.attribute` определены, но отсутствует флаг `locator.mandatory`, пропускает локатор.
5. В зависимости от типов `locator.attribute`, `locator.by` и значения `locator.sorted` вызывает соответствующие методы для выполнения действий с элементом.
6. Возвращает результат выполнения.

**Внутренние функции**:

#### `_parse_locator`

```python
        async def _parse_locator(
                locator: SimpleNamespace, message: Optional[str]
        ) -> Union[str, list, dict, Locator, bool, None]:
            """Parses and executes locator instructions."""
```

**Назначение**: Разбирает и выполняет инструкции локатора.

**Параметры**:
- `locator` (SimpleNamespace): Данные локатора.
- `message` (Optional[str]): Необязательное сообщение для событий.

**Возвращает**:
- `Union[str, list, dict, Locator, bool, None]`: Результат операции, который может быть строкой, списком, словарем, локатором, булевым значением или None.

**Как работает функция**:
1. Проверяет наличие атрибутов `event`, `attribute` и `mandatory` в локаторе.
2. Если `locator.attribute` и `locator.by` являются строками, пытается получить атрибут элемента с помощью `evaluate_locator`.
3. В зависимости от наличия `locator.event` выполняет событие или получает атрибут элемента.
4. Если `locator.selector` и `locator.by` являются списками, обрабатывает их как пары элементов и выполняет действия для каждой пары.
5. Возвращает результат выполнения.

```
A: Проверка наличия атрибутов event, attribute и mandatory
|
-- B: Проверка типов locator.attribute и locator.by
|
-- C: Получение атрибута элемента с помощью evaluate_locator
|
-- D: Выполнение события или получение атрибута элемента
|
-- E: Обработка списков locator.selector и locator.by как пар элементов
```

Где:
- `A`: Проверяет наличие атрибутов `event`, `attribute` и `mandatory` в локаторе.
- `B`: Проверяет, являются ли `locator.attribute` и `locator.by` строками.
- `C`: Получает атрибут элемента с помощью `evaluate_locator`.
- `D`: В зависимости от наличия `locator.event` выполняет событие или получает атрибут элемента.
- `E`: Если `locator.selector` и `locator.by` являются списками, обрабатывает их как пары элементов и выполняет действия для каждой пары.

**Примеры**:
```python
result = await executor.execute_locator(locator_data, message="Some message")
```

### `evaluate_locator`

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

**Назначение**: Оценивает и обрабатывает атрибуты локатора.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки (может быть строкой, списком строк или словарем).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Оцененный атрибут, который может быть строкой, списком строк или словарем.

**Как работает функция**:
1. Определяет внутреннюю асинхронную функцию `_evaluate`, которая возвращает атрибут без изменений.
2. Если атрибут является списком, вызывает `_evaluate` для каждого элемента списка и возвращает результаты в виде списка.
3. Если атрибут является строкой, вызывает `_evaluate` для атрибута и возвращает результат.

**Внутренние функции**:

#### `_evaluate`

```python
        async def _evaluate(attr: str) -> Optional[str]:
            return attr
```

**Назначение**: Возвращает атрибут без изменений.

**Параметры**:
- `attr` (str): Атрибут для возврата.

**Возвращает**:
- `Optional[str]`: Атрибут.

**Как работает функция**:
1. Возвращает переданный атрибут.

**Примеры**:
```python
evaluated_attribute = await executor.evaluate_locator("some_attribute")
```

### `get_attribute_by_locator`

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

**Назначение**: Получает указанный атрибут веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[str | List[str] | dict]`: Атрибут или None.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Получает веб-элемент с помощью `get_webelement_by_locator`.
3. Если элемент не найден, возвращает None.
4. Определяет внутреннюю функцию `_parse_dict_string` для разбора строки в формате словаря.
5. Определяет внутреннюю асинхронную функцию `_get_attribute` для получения одного атрибута из элемента.
6. Определяет внутреннюю асинхронную функцию `_get_attributes_from_dict` для получения нескольких атрибутов на основе словаря.
7. Если `locator.attribute` является строкой и начинается с '{', пытается разобрать ее как словарь и получить соответствующие атрибуты.
8. Если элемент является списком, получает атрибуты для каждого элемента списка.
9. Возвращает атрибут или None.

**Внутренние функции**:

#### `_parse_dict_string`

```python
        def _parse_dict_string(attr_string: str) -> dict | None:
            """Parses a string like '{attr1:attr2}' into a dictionary."""
```

**Назначение**: Разбирает строку типа '{attr1:attr2}' в словарь.

**Параметры**:
- `attr_string` (str): Строка для разбора.

**Возвращает**:
- `dict | None`: Словарь или None в случае ошибки.

**Как работает функция**:
1. Пытается разобрать строку в формат словаря, разделяя пары ключ-значение по ':' и элементы по ','.
2. Возвращает словарь, если разбор успешен, или None в случае ошибки.

#### `_get_attribute`

```python
        async def _get_attribute(el: Locator, attr: str) -> Optional[str]:
            """Retrieves a single attribute from a Locator."""
```

**Назначение**: Получает один атрибут из Locator.

**Параметры**:
- `el` (Locator): Locator элемента.
- `attr` (str): Имя атрибута для получения.

**Возвращает**:
- `Optional[str]`: Значение атрибута или None в случае ошибки.

**Как работает функция**:
1. Пытается получить атрибут элемента с использованием `el.get_attribute(attr)`.
2. Возвращает значение атрибута, если получение успешно, или None в случае ошибки.

#### `_get_attributes_from_dict`

```python
        async def _get_attributes_from_dict(element: Locator, attr_dict: dict) -> dict:
            """Retrieves multiple attributes based on a dictionary."""
```

**Назначение**: Получает несколько атрибутов на основе словаря.

**Параметры**:
- `element` (Locator): Locator элемента.
- `attr_dict` (dict): Словарь атрибутов для получения.

**Возвращает**:
- `dict`: Словарь с полученными атрибутами.

**Как работает функция**:
1. Итерируется по словарю атрибутов.
2. Для каждого ключа и значения в словаре пытается получить атрибут элемента с использованием `_get_attribute`.
3. Сохраняет полученные атрибуты в результирующем словаре.
4. Возвращает результирующий словарь.

```
A: Преобразование локатора в SimpleNamespace
|
-- B: Получение веб-элемента с помощью get_webelement_by_locator
|
-- C: Проверка наличия элемента
|
-- D: Разбор строки в формате словаря (если необходимо)
|
-- E: Получение атрибутов элемента
```

Где:
- `A`: Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
- `B`: Получает веб-элемент с помощью `get_webelement_by_locator`.
- `C`: Проверяет, найден ли элемент.
- `D`: Если `locator.attribute` является строкой и начинается с '{', пытается разобрать ее как словарь.
- `E`: Получает атрибуты элемента с использованием `_get_attribute` или `_get_attributes_from_dict`.

**Примеры**:
```python
attribute = await executor.get_attribute_by_locator(locator_data)
```

### `get_webelement_by_locator`

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

**Назначение**: Получает веб-элемент, используя локатор.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).

**Возвращает**:
- `Optional[Locator | List[Locator]]`: Playwright Locator.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Проверяет, что локатор не пустой.
3. В зависимости от значения `locator.by` создает локатор с использованием `self.page.locator`.
4. В зависимости от значения `locator.if_list` возвращает один элемент или список элементов.
5. Обрабатывает исключения, возникающие при поиске элемента, и логирует их с использованием `logger.error`.

```
A: Преобразование локатора в SimpleNamespace
|
-- B: Проверка наличия локатора
|
-- C: Создание локатора с использованием self.page.locator
|
-- D: Возврат элемента или списка элементов в зависимости от locator.if_list
```

Где:
- `A`: Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
- `B`: Проверяет, что локатор не пустой.
- `C`: Создает локатор с использованием `self.page.locator`.
- `D`: В зависимости от значения `locator.if_list` возвращает один элемент или список элементов.

**Примеры**:
```python
element = await executor.get_webelement_by_locator(locator_data)
```

### `get_webelement_as_screenshot`

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

**Назначение**: Делает скриншот найденного веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `webelement` (Optional[Locator]): Веб-элемент Locator.

**Возвращает**:
- `Optional[bytes]`: Скриншот в байтах или None.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Если `webelement` не передан, получает веб-элемент с помощью `get_webelement_by_locator`.
3. Если элемент не найден, возвращает None.
4. Делает скриншот элемента с использованием `webelement.screenshot()`.
5. Обрабатывает исключения, возникающие при создании скриншота, и логирует их с использованием `logger.error`.

```
A: Преобразование локатора в SimpleNamespace
|
-- B: Получение веб-элемента с помощью get_webelement_by_locator (если webelement не передан)
|
-- C: Проверка наличия элемента
|
-- D: Создание скриншота элемента
```

Где:
- `A`: Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
- `B`: Если `webelement` не передан, получает веб-элемент с помощью `get_webelement_by_locator`.
- `C`: Проверяет, найден ли элемент.
- `D`: Делает скриншот элемента с использованием `webelement.screenshot()`.

**Примеры**:
```python
screenshot = await executor.get_webelement_as_screenshot(locator_data)
```

### `execute_event`

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

**Назначение**: Выполняет событие, связанное с локатором.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора (словарь или SimpleNamespace).
- `message` (Optional[str]): Необязательное сообщение для событий.
- `typing_speed` (float): Необязательная скорость ввода текста для событий.

**Возвращает**:
- `Union[str, List[str], bytes, List[bytes], bool]`: Статус выполнения.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Получает список событий из `locator.event`, разделяя строку по ';'.
3. Получает веб-элемент с помощью `get_webelement_by_locator`.
4. Если элемент не найден, возвращает False.
5. Итерируется по списку событий и выполняет соответствующие действия.
6. Поддерживаемые события: "click()", "pause(duration)", "upload_media()", "screenshot()", "clear()", "send_keys(keys)", "type(message)".
7. Обрабатывает исключения, возникающие при выполнении событий, и логирует их с использованием `logger.error`.

```
A: Преобразование локатора в SimpleNamespace
|
-- B: Получение списка событий из locator.event
|
-- C: Получение веб-элемента с помощью get_webelement_by_locator
|
-- D: Итерация по списку событий и выполнение соответствующих действий
```

Где:
- `A`: Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
- `B`: Получает список событий из `locator.event`, разделяя строку по ';'.
- `C`: Получает веб-элемент с помощью `get_webelement_by_locator`.
- `D`: Итерируется по списку событий и выполняет соответствующие действия.

**Примеры**:
```python
status = await executor.execute_event(locator_data, message="file_path", typing_speed=0.1)
```

### `send_message`

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

**Назначение**: Отправляет сообщение веб-элементу.

**Параметры**:
- `locator` (dict | SimpleNamespace): Информация о местоположении элемента на странице.
- `message` (str): Сообщение для отправки веб-элементу.
- `typing_speed` (float): Скорость ввода сообщения в секундах.

**Возвращает**:
- `bool`: Возвращает `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Как работает функция**:
1. Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
2. Получает веб-элемент с помощью `get_webelement_by_locator`.
3. Если элемент не найден, возвращает False.
4. Если `typing_speed` указана, вводит сообщение посимвольно с указанной скоростью.
5. В противном случае вводит сообщение целиком.
6. Возвращает True, если сообщение было отправлено успешно.

```
A: Преобразование локатора в SimpleNamespace
|
-- B: Получение веб-элемента с помощью get_webelement_by_locator
|
-- C: Проверка наличия элемента
|
-- D: Ввод сообщения посимвольно или целиком в зависимости от typing_speed
```

Где:
- `A`: Преобразует локатор из словаря в SimpleNamespace, если это необходимо.
- `B`: Получает веб-элемент с помощью `get_webelement_by_locator`.
- `C`: Проверяет, найден ли элемент.
- `D`: Вводит сообщение посимвольно или целиком в зависимости от `typing_speed`.

**Примеры**:
```python
success = await executor.send_message(locator_data, message="Hello, world!", typing_speed=0.1)
```

### `goto`

```python
    async def goto(self, url: str) -> None:
        """
        Navigates to a specified URL.

        Args:
            url: URL to navigate to.
        """
```

**Назначение**: Переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Как работает функция**:
1. Проверяет, что страница существует.
2. Переходит по указанному URL с помощью `self.page.goto(url)`.
3. Обрабатывает исключения, возникающие при переходе по URL, и логирует их с использованием `logger.error`.

```
A: Проверка наличия страницы
|
-- B: Переход по указанному URL
```

Где:
- `A`: Проверяет, что страница существует (`self.page`).
- `B`: Переходит по указанному URL с помощью `self.page.goto(url)`.

**Примеры**:
```python
await executor.goto("https://example.com")
```