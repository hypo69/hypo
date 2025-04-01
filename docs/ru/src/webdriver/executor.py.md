# Модуль `executor.py`

## Обзор

Модуль `executor.py` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами. Он позволяет находить элементы на странице по различным локаторам (например, id, class, xpath), выполнять с ними различные действия (например, клик, ввод текста) и получать значения их атрибутов. Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для обработки взаимодействия с веб-элементами, используя Selenium, на основе предоставленных локаторов.

**Принцип работы**:
1.  Инициализируется с драйвером WebDriver.
2.  Предоставляет методы для поиска веб-элементов на основе локаторов, получения атрибутов и выполнения различных действий (например, кликов, ввода текста).
3.  Обрабатывает возможные исключения, такие как `TimeoutException` и `ElementClickInterceptedException`.

**Атрибуты**:

*   `driver` (Optional[object]): Экземпляр драйвера WebDriver для управления браузером.
*   `actions` (ActionChains): Объект ActionChains для выполнения сложных последовательностей действий с веб-элементами. Инициализируется в методе `__post_init__`.
*   `mode` (str): Режим работы, по умолчанию `"debug"`.

**Методы**:

*   `__post_init__()`: Инициализирует объект `ActionChains` после создания экземпляра класса, если передан драйвер.
*   `execute_locator(locator:  dict | SimpleNamespace, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = "presence_of_element_located", message: Optional[str] = None, typing_speed: Optional[float] = 0) ->  Optional[str | list | dict | WebElement | bool]`: Выполняет действия над веб-элементом на основе предоставленного локатора.
*   `_evaluate_locator(attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]`: Вычисляет и обрабатывает атрибуты локатора.
*   `get_attribute_by_locator(locator: SimpleNamespace | dict, timeout: Optional[float] = 0, timeout_for_event: str = "presence_of_element_located", message: Optional[str] = None, typing_speed: float = 0) -> Optional[WebElement | list[WebElement]]`: Получает атрибуты из веб-элемента или списка веб-элементов.
*   `get_webelement_by_locator(locator: dict | SimpleNamespace, timeout: Optional[float] = 0, timeout_for_event: Optional[str] = "presence_of_element_located") -> Optional[WebElement | List[WebElement]]`: Извлекает веб-элемент или список элементов на основе предоставленного локатора.
*   `get_webelement_as_screenshot(locator: SimpleNamespace | dict, timeout: float = 5, timeout_for_event: str = "presence_of_element_located", message: Optional[str] = None, typing_speed: float = 0, webelement: Optional[WebElement] = None) -> Optional[BinaryIO]`: Делает снимок экрана найденного веб-элемента.
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
    ...
```

**Назначение**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Параметры**:

*   `locator` (dict | SimpleNamespace): Данные локатора. Может быть словарем или объектом `SimpleNamespace`.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента в секундах. По умолчанию `0`.
*   `timeout_for_event` (Optional[str]): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.
*   `message` (Optional[str]): Сообщение для действий, таких как `send_keys` или `type`.
*   `typing_speed` (Optional[float]): Скорость печати для событий `send_keys` в секундах.

**Возвращает**:

*   `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или `None`.

**Как работает функция**:

1.  Проверяет, является ли `locator` словарем, и преобразует его в `SimpleNamespace`, если это необходимо.
2.  Проверяет наличие атрибутов `attribute` и `selector` в `locator`. Если их нет, возвращает `None`.
3.  Определяет внутреннюю функцию `_parse_locator`, которая обрабатывает инструкции локатора.

**Внутренние функции**:

*   `_parse_locator`:
    *   Анализирует и выполняет инструкции локатора.
    *   Определяет, какой тип локатора используется (например, по атрибуту, по URL).
    *   Вызывает соответствующие методы для выполнения действий (например, `execute_event`, `get_attribute_by_locator`, `get_webelement_by_locator`).

**ASCII flowchart**:

```
    Начало
    │
    ├── Проверка типа locator (dict -> SimpleNamespace)
    │
    ├── Проверка наличия attribute и selector
    │   └── Нет -> Возврат None
    │   └── Да -> _parse_locator
    │
    │   _parse_locator:
    │   │
    │   ├── Проверка флагов locator
    │   │   └── Возврат None, если неверно
    │   │   └── Продолжение, если верно
    │   │
    │   ├── Проверка типа locator.by (str или list)
    │   │   └── str -> Вычисление атрибута, если есть
    │   │   │       ├── Проверка locator.by
    │   │   │       │   ├── value -> Возврат атрибута
    │   │   │       │   ├── url   -> Разбор URL и возврат параметра
    │   │   │       │   └── Другое -> Вызов execute_event или get_attribute_by_locator или get_webelement_by_locator
    │   │   └── list -> Проверка locator.sorted
    │   │       ├── pairs -> Итерация по парам элементов и рекурсивный вызов _parse_locator
    │   │       └── Другое -> Логирование предупреждения
    │   │
    │   └── Возврат результата
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Использование execute_locator с минимальными параметрами
locator_data = {'by': 'id', 'selector': 'myElement'}
result = ExecuteLocator().execute_locator(locator_data)

# Пример 2: Использование execute_locator с указанием времени ожидания
locator_data = {'by': 'xpath', 'selector': '//button[@id="submit"]'}
result = ExecuteLocator().execute_locator(locator_data, timeout=10)

# Пример 3: Использование execute_locator с сообщением
locator_data = {'by': 'name', 'selector': 'myTextField'}
result = ExecuteLocator().execute_locator(locator_data, message='Hello, World!')
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
    ...
```

**Назначение**: Вычисляет и обрабатывает атрибуты локатора.

**Параметры**:

*   `attribute` (str | List[str] | dict): Атрибут для вычисления (может быть строкой, списком строк или словарем).

**Возвращает**:

*   `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

**Как работает функция**:

1.  Определяет внутреннюю функцию `_evaluate`, которая обрабатывает отдельные строковые атрибуты.
2.  Если `attribute` является списком, применяет `_evaluate` к каждому элементу списка.
3.  Если `attribute` является строкой, применяет `_evaluate` к строке.

**Внутренние функции**:

*   `_evaluate`:
    *   Проверяет, соответствует ли атрибут паттерну `%\\w+%`.
    *   Если соответствует, пытается получить значение атрибута из `Keys`.
    *   В противном случае возвращает атрибут без изменений.

**ASCII flowchart**:

```
    Начало
    │
    ├── Проверка типа attribute (str, list, dict)
    │   ├── list -> Итерация по списку и вызов _evaluate для каждого элемента
    │   ├── str  -> Вызов _evaluate для строки
    │   └── dict -> Возврат без изменений
    │
    │   _evaluate:
    │   │
    │   ├── Проверка соответствия паттерну "%\\w+%"
    │   │   ├── Да -> Получение значения из Keys
    │   │   └── Нет -> Возврат атрибута без изменений
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Вычисление строкового атрибута
attribute = "%TAB%"
result = ExecuteLocator()._evaluate_locator(attribute)

# Пример 2: Вычисление списка атрибутов
attributes = ["%SHIFT%", "%ENTER%"]
result = ExecuteLocator()._evaluate_locator(attributes)

# Пример 3: Вычисление атрибута, который не требует вычисления
attribute = "some_attribute"
result = ExecuteLocator()._evaluate_locator(attribute)
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
    ...
```

**Назначение**: Получает атрибуты из веб-элемента или списка веб-элементов.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора. Может быть `SimpleNamespace` или словарем.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента в секундах. По умолчанию `0`.
*   `timeout_for_event` (str): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.
*   `message` (Optional[str]): Не используется в этой функции.
*   `typing_speed` (float): Не используется в этой функции.

**Возвращает**:

*   `Optional[WebElement | list[WebElement]]`: Значение атрибута(ов) в виде `WebElement`, списка `WebElement` или `None`, если не найдено.

**Как работает функция**:

1.  Преобразует `locator` в `SimpleNamespace`, если это необходимо.
2.  Получает веб-элемент с помощью `get_webelement_by_locator`.
3.  Если веб-элемент не найден и `locator.mandatory` истинно, записывает отладочное сообщение и возвращает `None`.
4.  Определяет внутренние функции `_parse_dict_string` и `_get_attributes_from_dict`.

**Внутренние функции**:

*   `_parse_dict_string`:
    *   Разбирает строку типа `'{attr1:attr2}'` в словарь.
    *   Обрабатывает исключение `ValueError`, если строка имеет неверный формат.
*   `_get_attributes_from_dict`:
    *   Получает значения атрибутов из `WebElement` на основе словаря.
    *   Возвращает словарь с полученными значениями атрибутов.

**ASCII flowchart**:

```
    Начало
    │
    ├── Преобразование locator в SimpleNamespace
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │   └── Элемент не найден и locator.mandatory -> Логирование и возврат None
    │
    ├── Определение внутренних функций _parse_dict_string и _get_attributes_from_dict
    │
    ├── Проверка типа атрибута locator.attribute
    │   ├── str и начинается с "{" -> _parse_dict_string -> _get_attributes_from_dict
    │   ├── list -> Итерация по списку и получение атрибутов
    │   └── Другое -> Получение атрибута из веб-элемента
    │
    └── Возврат значения атрибута или None
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Получение атрибута 'src' из веб-элемента
locator_data = {'by': 'tag_name', 'selector': 'img', 'attribute': 'src'}
result = ExecuteLocator().get_attribute_by_locator(locator_data)

# Пример 2: Получение атрибутов из списка веб-элементов
locator_data = {'by': 'class_name', 'selector': 'item', 'attribute': 'text'}
result = ExecuteLocator().get_attribute_by_locator(locator_data)

# Пример 3: Получение атрибутов с использованием формата словаря
locator_data = {'by': 'id', 'selector': 'myElement', 'attribute': '{attr1:attr2}'}
result = ExecuteLocator().get_attribute_by_locator(locator_data)
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
    ...
```

**Назначение**: Извлекает веб-элемент или список элементов на основе предоставленного локатора.

**Параметры**:

*   `locator` (dict | SimpleNamespace): Данные локатора. Может быть словарем или объектом `SimpleNamespace`.
*   `timeout` (Optional[float]): Время ожидания для обнаружения элемента в секундах. По умолчанию `0`.
*   `timeout_for_event` (Optional[str]): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.

**Возвращает**:

*   `Optional[WebElement | List[WebElement]]`: `WebElement`, список `WebElement` или `None`, если не найдено.

**Как работает функция**:

1.  Преобразует `locator` в `SimpleNamespace`, если это необходимо.
2.  Определяет внутреннюю функцию `_parse_elements_list`, которая фильтрует список веб-элементов на основе атрибута `if_list`.
3.  Ищет веб-элементы с использованием `driver.find_elements` или `WebDriverWait`, в зависимости от значения `timeout`.
4.  Вызывает `_parse_elements_list` для фильтрации списка веб-элементов, если они найдены.

**Внутренние функции**:

*   `_parse_elements_list`:
    *   Фильтрует список веб-элементов на основе значения `locator.if_list`.
    *   Поддерживает различные варианты фильтрации, такие как `'all'`, `'first'`, `'last'`, `'even'`, `'odd'`, список индексов или один индекс.

**ASCII flowchart**:

```
    Начало
    │
    ├── Преобразование locator в SimpleNamespace
    │
    ├── Определение внутренней функции _parse_elements_list
    │
    ├── Проверка значения timeout
    │   ├── timeout == 0 -> Поиск элементов с помощью driver.find_elements
    │   └── timeout > 0  -> Поиск элементов с помощью WebDriverWait
    │
    ├── Вызов _parse_elements_list для фильтрации списка веб-элементов
    │
    └── Возврат веб-элемента или списка веб-элементов или None
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Получение одного веб-элемента по id
locator_data = {'by': 'id', 'selector': 'myElement'}
result = ExecuteLocator().get_webelement_by_locator(locator_data)

# Пример 2: Получение списка веб-элементов по class_name
locator_data = {'by': 'class_name', 'selector': 'item'}
result = ExecuteLocator().get_webelement_by_locator(locator_data)

# Пример 3: Получение первого элемента из списка веб-элементов
locator_data = {'by': 'tag_name', 'selector': 'div', 'if_list': 'first'}
result = ExecuteLocator().get_webelement_by_locator(locator_data)
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
    ...
```

**Назначение**: Делает снимок экрана найденного веб-элемента.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора. Может быть `SimpleNamespace` или словарем.
*   `timeout` (float): Время ожидания для обнаружения элемента в секундах. По умолчанию `5`.
*   `timeout_for_event` (str): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.
*   `message` (Optional[str]): Не используется в этой функции.
*   `typing_speed` (float): Не используется в этой функции.
*   `webelement` (Optional[WebElement]): Предварительно полученный веб-элемент.

**Возвращает**:

*   `Optional[BinaryIO]`: Двоичный поток данных снимка экрана или `None`, если не удалось.

**Как работает функция**:

1.  Преобразует `locator` в `SimpleNamespace`, если это необходимо.
2.  Если `webelement` не предоставлен, получает его с помощью `get_webelement_by_locator`.
3.  Делает снимок экрана веб-элемента с помощью `webelement.screenshot_as_png`.

**ASCII flowchart**:

```
    Начало
    │
    ├── Преобразование locator в SimpleNamespace
    │
    ├── Проверка наличия webelement
    │   └── Нет -> Получение веб-элемента с помощью get_webelement_by_locator
    │
    ├── Проверка, найден ли веб-элемент
    │   └── Нет -> Возврат None
    │
    ├── Создание скриншота элемента
    │
    └── Возврат BinaryIO stream скриншота или None, если не удалось
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Получение скриншота веб-элемента по id
locator_data = {'by': 'id', 'selector': 'myElement'}
result = ExecuteLocator().get_webelement_as_screenshot(locator_data)

# Пример 2: Получение скриншота предварительно полученного веб-элемента
webelement = ExecuteLocator().get_webelement_by_locator({'by': 'id', 'selector': 'myElement'})
result = ExecuteLocator().get_webelement_as_screenshot(locator=None, webelement=webelement)
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
    ...
```

**Назначение**: Выполняет событие, связанное с локатором.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора. Может быть `SimpleNamespace` или словарем.
*   `timeout` (float): Время ожидания для обнаружения элемента в секундах. По умолчанию `5`.
*   `timeout_for_event` (str): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.
*   `message` (str): Дополнительное сообщение для отправки с событием.
*   `typing_speed` (float): Скорость печати для событий `send_keys` в секундах.

**Возвращает**:

*   `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события (строка, список строк, байты, список байтов или булево значение).

**Как работает функция**:

1.  Преобразует `locator` в `SimpleNamespace`, если это необходимо.
2.  Разбивает строку `locator.event` на список событий.
3.  Получает веб-элемент с помощью `get_webelement_by_locator`.
4.  Выполняет итерацию по списку событий и выполняет соответствующие действия (например, `click()`, `pause()`, `upload_media()`, `screenshot()`, `clear()`, `send_keys()`, `type()`).

**ASCII flowchart**:

```
    Начало
    │
    ├── Преобразование locator в SimpleNamespace
    │
    ├── Разделение locator.event на список событий
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │
    ├── Итерация по списку событий
    │   ├── click()            -> Клик на элемент
    │   ├── pause(duration)    -> Пауза на указанное время
    │   ├── upload_media()     -> Загрузка медиафайла
    │   ├── screenshot()       -> Создание скриншота элемента
    │   ├── clear()            -> Очистка элемента
    │   ├── send_keys(keys)    -> Отправка клавиш
    │   └── type(message)      -> Ввод сообщения
    │
    └── Возврат результата или True
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Выполнение события click()
locator_data = {'by': 'id', 'selector': 'myButton', 'event': 'click()'}
result = ExecuteLocator().execute_event(locator_data)

# Пример 2: Выполнение события pause() и click()
locator_data = {'by': 'id', 'selector': 'myElement', 'event': 'pause(2);click()'}
result = ExecuteLocator().execute_event(locator_data)

# Пример 3: Выполнение события upload_media()
locator_data = {'by': 'id', 'selector': 'myFileInput', 'event': 'upload_media()', 'message': '/path/to/file.txt'}
result = ExecuteLocator().execute_event(locator_data, message='/path/to/file.txt')
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
    ...
```

**Назначение**: Отправляет сообщение веб-элементу.

**Параметры**:

*   `locator` (SimpleNamespace | dict): Данные локатора. Может быть `SimpleNamespace` или словарем.
*   `timeout` (float): Время ожидания для обнаружения элемента в секундах. По умолчанию `5`.
*   `timeout_for_event` (str): Условие ожидания (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `'presence_of_element_located'`.
*   `message` (str): Сообщение для отправки веб-элементу.
*   `typing_speed` (float): Скорость печати для событий `send_keys` в секундах.

**Возвращает**:

*   `bool`: `True`, если сообщение было успешно отправлено, `False` в противном случае.

**Как работает функция**:

1.  Преобразует `locator` в `SimpleNamespace`, если это необходимо.
2.  Определяет внутреннюю функцию `type_message`, которая вводит сообщение в веб-элемент с указанной скоростью печати.
3.  Получает веб-элемент с помощью `get_webelement_by_locator`.
4.  Перемещает фокус на веб-элемент и вызывает `type_message` для ввода сообщения.

**Внутренние функции**:

*   `type_message`:
    *   Вводит сообщение в веб-элемент с указанной скоростью печати.
    *   Заменяет определенные символы (например, `;`) на соответствующие комбинации клавиш (например, `SHIFT+ENTER`).

**ASCII flowchart**:

```
    Начало
    │
    ├── Преобразование locator в SimpleNamespace
    │
    ├── Определение внутренней функции type_message
    │
    ├── Получение веб-элемента с помощью get_webelement_by_locator
    │
    ├── Перемещение фокуса на веб-элемент
    │
    ├── Вызов type_message для ввода сообщения
    │
    └── Возврат True или False в зависимости от успеха
    │
    Конец
```

**Примеры**:

```python
# Пример 1: Отправка сообщения веб-элементу по id
locator_data = {'by': 'id', 'selector': 'myTextField'}
result = ExecuteLocator().send_message(locator_data, message='Hello, World!')

# Пример 2: Отправка сообщения с указанием скорости печати
locator_data = {'by': 'name', 'selector': 'myTextField'}
result = ExecuteLocator().send_message(locator_data, message='Hello, World!', typing_speed=0.1)

# Пример 3: Отправка сообщения с заменой символа ";"
locator_data = {'by': 'id', 'selector': 'myTextArea'}
result = ExecuteLocator().send_message(locator_data, message='Line 1; Line 2')