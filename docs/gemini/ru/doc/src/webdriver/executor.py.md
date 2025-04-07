# Модуль `executor.py`

## Обзор

Модуль `executor.py` предоставляет функциональность для взаимодействия с веб-элементами, используя Selenium, на основе предоставленных локаторов. Он обрабатывает парсинг локаторов, взаимодействие с элементами и обработку ошибок.

Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами. Он позволяет находить элементы на странице по различным локаторам (например, id, class, xpath), выполнять с ними различные действия (например, клик, ввод текста) и получать значения их атрибутов. Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.

## Подробней

Модуль содержит класс `ExecuteLocator`, который используется для выполнения действий над веб-элементами на основе предоставленных локаторов. Класс включает методы для получения веб-элементов, выполнения событий (например, кликов, ввода текста) и получения атрибутов элементов. Модуль также содержит функции для обработки ошибок и ведения журнала.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Принцип работы**:
1.  При инициализации класса создается экземпляр `ActionChains` для выполнения сложных действий с веб-элементами.
2.  Метод `execute_locator` является основным методом класса, который принимает локатор и выполняет действия на основе его атрибутов.
3.  Вспомогательные методы, такие как `get_webelement_by_locator`, `get_attribute_by_locator` и `execute_event`, используются для получения веб-элементов, извлечения атрибутов и выполнения событий соответственно.
4.  Для обработки ошибок используются блоки `try...except`, которые позволяют перехватывать исключения и регистрировать их в журнале.

**Атрибуты**:

*   `driver` (Optional[object]): Экземпляр веб-драйвера Selenium.
*   `actions` (ActionChains): Объект для выполнения цепочки действий с веб-элементами.
*   `mode` (str): Режим работы (по умолчанию "debug").

**Методы**:

*   `__post_init__()`: Инициализирует объект `ActionChains` после создания экземпляра класса.
*   `execute_locator(locator: dict | SimpleNamespace, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = "presence_of_element_located", message: Optional[str] = None, typing_speed: Optional[float] = 0) -> Optional[str | list | dict | WebElement | bool]`: Выполняет действия над веб-элементом на основе предоставленного локатора.
*   `_evaluate_locator(attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`: Вычисляет и обрабатывает атрибуты локатора.
*   `get_attribute_by_locator(locator: SimpleNamespace | dict, timeout: Optional[float] = 0, timeout_for_event: str = "presence_of_element_located", message: Optional[str] = None, typing_speed: float = 0) -> Optional[WebElement | list[WebElement]]`: Получает атрибуты веб-элемента или списка веб-элементов.
*   `get_webelement_by_locator(locator: dict | SimpleNamespace, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = "presence_of_element_located") -> Optional[WebElement | List[WebElement]]`: Получает веб-элемент или список элементов на основе предоставленного локатора.
*   `get_webelement_as_screenshot(locator: SimpleNamespace | dict, timeout: float = 5, timeout_for_event: str = "presence_of_element_located", message: Optional[str] = None, typing_speed: float = 0, webelement: Optional[WebElement] = None) -> Optional[BinaryIO]`: Делает скриншот найденного веб-элемента.
*   `execute_event(locator: SimpleNamespace | dict, timeout: float = 5, timeout_for_event: str = "presence_of_element_located", message: str = None, typing_speed: float = 0) -> Optional[str | list[str] | bytes | list[bytes] | bool]`: Выполняет событие, связанное с локатором.
*   `send_message(locator: SimpleNamespace | dict, timeout: float = 5, timeout_for_event: str = "presence_of_element_located", message: str = None, typing_speed: float = 0) -> bool`: Отправляет сообщение веб-элементу.

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
        Executes actions on a web element based on the provided locator.

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

**Назначение**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:

*   `locator` (dict | SimpleNamespace): Данные локатора.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента (в секундах). По умолчанию 0.
*   `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
*   `message` (Optional[str]): Необязательное сообщение для действий, таких как `send_keys` или `type`.
*   `typing_speed` (Optional[float]): Скорость ввода для событий `send_keys` (в секундах). По умолчанию 0.

**Возвращает**:

*   `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или None.

**Вызывает исключения**:

*   `TimeoutException`: Если элемент не найден в течение указанного времени ожидания.
*   `Exception`: При возникновении ошибки во время выполнения действий с элементом.

**Внутренние функции**:

*   `_parse_locator(locator: SimpleNamespace, message: Optional[str] = None, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = "presence_of_element_located", typing_speed: Optional[float] = 0) -> Optional[str | list | dict | WebElement | bool]`:
    Разбирает и выполняет инструкции локатора.

    *   **Параметры**:
        *   `locator` (SimpleNamespace): Данные локатора.
        *   `message` (Optional[str]): Необязательное сообщение для действий, таких как `send_keys` или `type`.
        *   `timeout` (Optional[float]): Время ожидания для обнаружения элемента (в секундах). По умолчанию 0.
        *   `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
        *   `typing_speed` (Optional[float]): Скорость ввода для событий `send_keys` (в секундах). По умолчанию 0.
    *   **Возвращает**:
        *   `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или None.

**Как работает функция**:

1.  Функция `execute_locator` принимает данные локатора, время ожидания, условие ожидания, сообщение и скорость ввода в качестве параметров.
2.  Если локатор является словарем, он преобразуется в объект `SimpleNamespace` для упрощения доступа к атрибутам.
3.  Если атрибут `selector` или `attribute` локатора отсутствует, функция регистрирует отладочное сообщение и возвращает `None`.
4.  Вызывается внутренняя функция `_parse_locator` для разбора инструкций локатора и выполнения действий с веб-элементом.

```
    execute_locator
    │
    ├── Проверка локатора (locator.attribute и locator.selector)
    │   └── Если локатор пустой, вернуть None
    │
    └── _parse_locator(locator, message, timeout, timeout_for_event, typing_speed)
        │
        ├── Проверка флагов (locator.event, locator.attribute, locator.mandatory)
        │   └── Если флаги неверные, вернуть None
        │
        ├── Проверка типа locator.by (str или list)
        │   ├── Если str
        │   │   ├── Обработка атрибута locator.attribute
        │   │   ├── Проверка locator.by == "value" или "url"
        │   │   ├── Вызов execute_event, get_attribute_by_locator, get_webelement_by_locator
        │   │   └── Вернуть результат
        │   │
        │   └── Если list
        │       ├── Проверка locator.sorted == "pairs"
        │       │   ├── Итерация по спискам локаторов
        │       │   ├── Вызов _parse_locator для каждого элемента
        │       │   ├── Объединение результатов в пары
        │       │   └── Вернуть пары
        │       │
        │       └── Иначе, логгирование предупреждения
        │
        └── Вернуть результат _parse_locator
```

**Примеры**:

```python
# Пример 1: Выполнение клика на элементе
locator = {"by": "id", "selector": "myButton", "event": "click()"}
result = await execute_locator(locator)
print(result)  # True или False

# Пример 2: Получение значения атрибута элемента
locator = {"by": "id", "selector": "myInput", "attribute": "value"}
result = await execute_locator(locator)
print(result)  # Значение атрибута 'value' элемента 'myInput'

# Пример 3: Отправка сообщения элементу
locator = {"by": "id", "selector": "myTextarea"}
message = "Hello, world!"
result = await execute_locator(locator, message=message)
print(result)  # True
```

### `_evaluate_locator`

```python
    def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
        """
        Evaluates and processes locator attributes.

        Args:
            attribute: Attribute to evaluate (can be a string, list of strings, or a dictionary).

        Returns:
            The evaluated attribute, which can be a string, list of strings, or dictionary.
        """
```

**Назначение**: Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:

*   `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:

*   `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Внутренние функции**:

*   `_evaluate(attr: str) -> Optional[str]`: Вычисляет отдельную строку атрибута.

    *   **Параметры**:
        *   `attr` (str): Строка атрибута для вычисления.
    *   **Возвращает**:
        *   `Optional[str]`: Вычисленная строка атрибута.

**Как работает функция**:

1.  Функция `_evaluate_locator` принимает атрибут, который может быть строкой, списком строк или словарем.
2.  Если атрибут является списком, функция применяет функцию `_evaluate` к каждому элементу списка.
3.  Функция `_evaluate` проверяет, начинается ли атрибут с символа `%`. Если да, она пытается получить соответствующий атрибут из класса `Keys` и возвращает его. В противном случае она возвращает исходный атрибут.

```
    _evaluate_locator
    │
    ├── Проверка типа attribute (str, list, dict)
    │   ├── Если list
    │   │   ├── Применить _evaluate к каждому элементу
    │   │   └── Вернуть список вычисленных атрибутов
    │   │
    │   └── Иначе, применить _evaluate к атрибуту
    │
    └── Вернуть вычисленный атрибут
```

**Примеры**:

```python
# Пример 1: Вычисление атрибута строки
attribute = "%TAB%"
result = _evaluate_locator(attribute)
print(result)  # Keys.TAB

# Пример 2: Вычисление списка атрибутов
attribute = ["%TAB%", "value"]
result = _evaluate_locator(attribute)
print(result)  # [Keys.TAB, "value"]
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
        Retrieves attributes from a web element or a list of web elements.

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

**Назначение**: Получает атрибуты веб-элемента или списка веб-элементов.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента (в секундах). По умолчанию 0.
*   `timeout_for_event` (str): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
*   `message` (Optional[str]): Не используется в этой функции.
*   `typing_speed` (float): Не используется в этой функции.

**Возвращает**:

*   `Optional[WebElement | list[WebElement]]`: Значение атрибута (или атрибутов) в виде веб-элемента, списка веб-элементов или `None`, если не найдено.

**Внутренние функции**:

*   `_parse_dict_string(attr_string: str) -> dict | None`: Разбирает строку вроде '{attr1:attr2}' в словарь.

    *   **Параметры**:
        *   `attr_string` (str): Строка для разбора.
    *   **Возвращает**:
        *   `dict | None`: Словарь атрибутов или `None`, если разбор не удался.
*   `_get_attributes_from_dict(web_element: WebElement, attr_dict: dict) -> dict`: Получает значения атрибутов из веб-элемента на основе словаря.

    *   **Параметры**:
        *   `web_element` (WebElement): Веб-элемент для получения атрибутов.
        *   `attr_dict` (dict): Словарь атрибутов.
    *   **Возвращает**:
        *   `dict`: Словарь значений атрибутов.

**Как работает функция**:

1.  Функция `get_attribute_by_locator` принимает данные локатора, время ожидания и условие ожидания в качестве параметров.
2.  Она получает веб-элемент с помощью функции `get_webelement_by_locator`.
3.  Если веб-элемент не найден, функция регистрирует отладочное сообщение и возвращает `None`.
4.  Если атрибут локатора является строкой, начинающейся с символа `{`, функция вызывает функцию `_parse_dict_string` для преобразования строки в словарь. Затем она вызывает функцию `_get_attributes_from_dict` для получения значений атрибутов на основе словаря.
5.  Если веб-элемент является списком, функция итерируется по списку и получает значение атрибута для каждого элемента.

```
    get_attribute_by_locator
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │   └── Если веб-элемент не найден, вернуть None
    │
    ├── Проверка типа locator.attribute (str)
    │   ├── Если строка начинается с "{", вызвать _parse_dict_string
    │   │   ├── Вызвать _get_attributes_from_dict для получения атрибутов
    │   │   └── Вернуть словарь атрибутов
    │   │
    │   └── Иначе, получить значение атрибута из веб-элемента
    │
    └── Вернуть значение атрибута
```

**Примеры**:

```python
# Пример 1: Получение значения атрибута 'value' элемента 'myInput'
locator = {"by": "id", "selector": "myInput", "attribute": "value"}
result = await get_attribute_by_locator(locator)
print(result)  # Значение атрибута 'value' элемента 'myInput'

# Пример 2: Получение словаря атрибутов из элемента
locator = {"by": "id", "selector": "myElement", "attribute": "{attr1:attr2}"}
result = await get_attribute_by_locator(locator)
print(result)  # {"value1": "value2"}
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
        Retrieves a web element or list of elements based on the provided locator.

        Args:
            locator: Locator data (dict or SimpleNamespace).
            timeout: Timeout for locating the element (seconds).
            timeout_for_event: Wait condition (\'presence_of_element_located\', \'visibility_of_all_elements_located\').

        Returns:
           WebElement, list of WebElements, or None if not found.
        """
```

**Назначение**: Получает веб-элемент или список элементов на основе предоставленного локатора.

**Параметры**:

*   `locator` (dict | SimpleNamespace): Данные локатора.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента (в секундах). По умолчанию 0.
*   `timeout_for_event` (Optional[str]): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".

**Возвращает**:

*   `Optional[WebElement | List[WebElement]]`: Веб-элемент, список веб-элементов или `None`, если не найдено.

**Внутренние функции**:

*   `_parse_elements_list(web_elements: WebElement | List[WebElement], locator: SimpleNamespace) -> Optional[WebElement | List[WebElement]]`: Фильтрует список веб-элементов на основе атрибута `if_list`.

    *   **Параметры**:
        *   `web_elements` (WebElement | List[WebElement]): Веб-элемент или список веб-элементов для фильтрации.
        *   `locator` (SimpleNamespace): Данные локатора.
    *   **Возвращает**:
        *   `Optional[WebElement | List[WebElement]]`: Отфильтрованный веб-элемент или список веб-элементов.

**Как работает функция**:

1.  Функция `get_webelement_by_locator` принимает данные локатора, время ожидания и условие ожидания в качестве параметров.
2.  Она использует веб-драйвер для поиска веб-элементов на основе предоставленного локатора.
3.  Если веб-элементы найдены, функция вызывает функцию `_parse_elements_list` для фильтрации списка веб-элементов на основе атрибута `if_list`.
4.  Если веб-элементы не найдены в течение указанного времени ожидания, функция регистрирует ошибку и возвращает `None`.

```
    get_webelement_by_locator
    │
    ├── Определение времени ожидания (timeout)
    │
    ├── Проверка locator
    │   └── Если locator не валидный, вернуть None
    │
    ├── Поиск веб-элементов
    │   ├── Если timeout == 0, использовать driver.find_elements
    │   └── Иначе, использовать WebDriverWait
    │
    ├── Фильтрация списка элементов с помощью _parse_elements_list
    │   └── Вернуть отфильтрованный список или None
    │
    └── Обработка исключений (TimeoutException, Exception)
```

**Примеры**:

```python
# Пример 1: Получение веб-элемента по ID
locator = {"by": "id", "selector": "myElement"}
result = await get_webelement_by_locator(locator)
print(result)  # WebElement

# Пример 2: Получение списка веб-элементов по классу
locator = {"by": "class name", "selector": "myClass", "if_list": "all"}
result = await get_webelement_by_locator(locator)
print(result)  # List[WebElement]

# Пример 3: Получение первого элемента из списка
locator = {"by": "class name", "selector": "myClass", "if_list": "first"}
result = await get_webelement_by_locator(locator)
print(result)  # WebElement
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
        Takes a screenshot of the located web element.

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

**Назначение**: Делает скриншот найденного веб-элемента.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора.
*   `timeout` (float): Время ожидания для обнаружения элемента (в секундах). По умолчанию 5.
*   `timeout_for_event` (str): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
*   `message` (Optional[str]): Не используется в этой функции.
*   `typing_speed` (float): Не используется в этой функции.
*   `webelement` (Optional[WebElement]): Предварительно полученный веб-элемент.

**Возвращает**:

*   `Optional[BinaryIO]`: Двоичный поток скриншота или `None`, если не удалось.

**Как работает функция**:

1.  Функция `get_webelement_as_screenshot` принимает данные локатора, время ожидания, условие ожидания и предварительно полученный веб-элемент в качестве параметров.
2.  Если веб-элемент не предоставлен, функция пытается получить его с помощью функции `get_webelement_by_locator`.
3.  Если веб-элемент не найден, функция возвращает `None`.
4.  Если веб-элемент найден, функция делает скриншот элемента и возвращает его в виде двоичного потока.

```
    get_webelement_as_screenshot
    │
    ├── Проверка наличия webelement
    │   └── Если webelement отсутствует, получить его с помощью get_webelement_by_locator
    │
    ├── Если webelement не найден, вернуть None
    │
    ├── Сделать скриншот webelement
    │   └── Вернуть скриншот в виде BinaryIO или None в случае ошибки
    │
    └── Обработка исключений
```

**Примеры**:

```python
# Пример 1: Получение скриншота веб-элемента по ID
locator = {"by": "id", "selector": "myElement"}
result = await get_webelement_as_screenshot(locator)
print(result)  # BinaryIO

# Пример 2: Получение скриншота предварительно полученного веб-элемента
webelement = await get_webelement_by_locator({"by": "id", "selector": "myElement"})
result = await get_webelement_as_screenshot(locator, webelement=webelement)
print(result)  # BinaryIO
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
        Executes an event associated with a locator.

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

**Назначение**: Выполняет событие, связанное с локатором.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора.
*   `timeout` (float): Время ожидания для обнаружения элемента (в секундах). По умолчанию 5.
*   `timeout_for_event` (str): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
*   `message` (str): Необязательное сообщение для отправки с событием.
*   `typing_speed` (float): Скорость ввода для событий `send_keys` (в секундах).

**Возвращает**:

*   `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события (строка, список строк, байты, список байтов или булево значение).

**Как работает функция**:

1.  Функция `execute_event` принимает данные локатора, время ожидания, условие ожидания, сообщение и скорость ввода в качестве параметров.
2.  Она получает веб-элемент с помощью функции `get_webelement_by_locator`.
3.  Если веб-элемент не найден, функция возвращает `False`.
4.  Функция разбивает строку события на отдельные события и выполняет их последовательно.
5.  Поддерживаемые события включают `click()`, `pause()`, `upload_media()`, `screenshot()`, `clear()`, `send_keys()` и `type()`.
6.  Функция обрабатывает исключения, которые могут возникнуть во время выполнения событий, и регистрирует ошибки в журнале.

```
    execute_event
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │   └── Если веб-элемент не найден, вернуть False
    │
    ├── Разделение строки события на отдельные события
    │
    ├── Итерация по событиям
    │   ├── Обработка различных событий (click(), pause(), upload_media(), screenshot(), clear(), send_keys(), type())
    │   └── Выполнение соответствующих действий для каждого события
    │
    └── Вернуть результат выполнения событий
```

**Примеры**:

```python
# Пример 1: Выполнение клика на элементе
locator = {"by": "id", "selector": "myButton", "event": "click()"}
result = await execute_event(locator)
print(result)  # True или False

# Пример 2: Отправка сообщения в элемент и выполнение клика
locator = {"by": "id", "selector": "myInput", "event": "type(Hello, world!);click()"}
result = await execute_event(locator)
print(result)  # True
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
        Sends a message to a web element.

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

**Назначение**: Отправляет сообщение веб-элементу.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора.
*   `timeout` (float): Время ожидания для обнаружения элемента (в секундах). По умолчанию 5.
*   `timeout_for_event` (str): Условие ожидания ('presence_of_element_located', 'visibility_of_all_elements_located'). По умолчанию "presence_of_element_located".
*   `message` (str): Сообщение для отправки веб-элементу.
*   `typing_speed` (float): Скорость ввода для событий `send_keys` (в секундах).

**Возвращает**:

*   `bool`: `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Внутренние функции**:

*   `type_message(el: WebElement, message: str, replace_dict: dict = {";": "SHIFT+ENTER"}, typing_speed: float = typing_speed) -> bool`: Вводит сообщение в веб-элемент с заданной скоростью ввода.

    *   **Параметры**:
        *   `el` (WebElement): Веб-элемент для ввода сообщения.
        *   `message` (str): Сообщение для ввода.
        *   `replace_dict` (dict): Словарь замен символов. По умолчанию `{";": "SHIFT+ENTER"}`.
        *   `typing_speed` (float): Скорость ввода для событий `send_keys` (в секундах).
    *   **Возвращает**:
        *   `bool`: `True`, если сообщение было введено успешно, `False` в противном случае.

**Как работает функция**:

1.  Функция `send_message` принимает данные локатора, время ожидания, условие ожидания, сообщение и скорость ввода в качестве параметров.
2.  Она получает веб-элемент с помощью функции `get_webelement_by_locator`.
3.  Если веб-элемент не найден, функция регистрирует отладочное сообщение и возвращает `False`.
4.  Функция вызывает функцию `type_message` для ввода сообщения в веб-элемент с заданной скоростью ввода.

```
    send_message
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │   └── Если веб-элемент не найден, вернуть False
    │
    ├── Перемещение к веб-элементу
    │
    ├── Ввод сообщения с помощью type_message
    │
    └── Вернуть True
```

**Примеры**:

```python
# Пример 1: Отправка сообщения в текстовое поле
locator = {"by": "id", "selector": "myInput"}
message = "Hello, world!"
result = await send_message(locator, message=message)
print(result)  # True

# Пример 2: Отправка сообщения с заменой символов
locator = {"by": "id", "selector": "myTextarea"}
message = "Line 1;Line 2"
result = await send_message(locator, message=message)
print(result)  # True