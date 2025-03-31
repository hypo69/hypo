# Модуль `src.webdriver.executor`

## Обзор

Модуль `src.webdriver.executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок.

Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами.
Он позволяет находить элементы на странице по различным локаторам (например, id, class, xpath),
выполнять с ними различные действия (например, клик, ввод текста) и получать значения их атрибутов.
Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.

## Содержание

- [ExecuteLocator](#ExecuteLocator)
    - [__post_init__](#__post_init__)
    - [execute_locator](#execute_locator)
    - [_evaluate_locator](#_evaluate_locator)
    - [get_attribute_by_locator](#get_attribute_by_locator)
    - [get_webelement_by_locator](#get_webelement_by_locator)
    - [get_webelement_as_screenshot](#get_webelement_as_screenshot)
    - [execute_event](#execute_event)
    - [send_message](#send_message)

## Классы

### `ExecuteLocator`

**Описание**:
Класс `ExecuteLocator` предназначен для обработки взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Как работает класс**:
- Инициализируется с драйвером Selenium и создает объект `ActionChains` для выполнения сложных действий, таких как перемещение мыши и ввод текста.
- Методы класса позволяют выполнять различные действия с веб-элементами, такие как получение атрибутов, отправка сообщений, выполнение событий (например, клики) и получение скриншотов.
- Класс обрабатывает различные типы локаторов и обеспечивает гибкий способ взаимодействия с веб-страницами.

**Методы**:
- [`__post_init__`](#__post_init__)
- [`execute_locator`](#execute_locator)
- [`_evaluate_locator`](#_evaluate_locator)
- [`get_attribute_by_locator`](#get_attribute_by_locator)
- [`get_webelement_by_locator`](#get_webelement_by_locator)
- [`get_webelement_as_screenshot`](#get_webelement_as_screenshot)
- [`execute_event`](#execute_event)
- [`send_message`](#send_message)

#### `__post_init__`

```python
def __post_init__(self):
    if self.driver:
        self.actions = ActionChains(self.driver)
```

**Назначение**:
Инициализирует объект `ActionChains` после создания экземпляра класса, если предоставлен драйвер Selenium.

**Как работает функция**:
Если драйвер Selenium (`self.driver`) предоставлен при создании экземпляра класса `ExecuteLocator`, этот метод создает объект `ActionChains`, связанный с этим драйвером. `ActionChains` используется для выполнения сложных последовательностей действий, таких как перемещение мыши, нажатие клавиш и т.д.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Нет

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
```

**Назначение**:
Выполняет действия над веб-элементом на основе предоставленного локатора.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания, условие ожидания события, сообщение для отправки (например, для ввода текста) и скорость ввода текста.
- Если локатор представлен в виде словаря, он преобразуется в объект `SimpleNamespace` для удобства доступа к атрибутам.
- Вызывает внутреннюю асинхронную функцию `_parse_locator` для разбора и выполнения инструкций локатора.
- Возвращает результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или `None`.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Сообщение для действий, таких как `send_keys` или `type`. По умолчанию `None`.
- `typing_speed` (Optional[float], optional): Скорость ввода текста для событий `send_keys` в секундах. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или `None`.

**Вызывает исключения**:
- Нет

#### `_evaluate_locator`

```python
def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
```

**Назначение**:
Оценивает и обрабатывает атрибуты локатора.

**Как работает функция**:
- Принимает атрибут для оценки, который может быть строкой, списком строк или словарем.
- Если атрибут является строкой и соответствует шаблону `%\\w+%`, он пытается получить соответствующее значение из атрибутов класса `Keys` (например, `%ENTER%` будет заменен на `Keys.ENTER`).
- Если атрибут является списком, он применяет эту операцию к каждому элементу списка.
- Возвращает оцененный атрибут.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для оценки.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Оцененный атрибут, который может быть строкой, списком строк или словарем.

**Вызывает исключения**:
- Нет

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
```

**Назначение**:
Извлекает атрибуты из веб-элемента или списка веб-элементов.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания и условие ожидания события.
- Получает веб-элемент с помощью метода `get_webelement_by_locator`.
- Если веб-элемент найден, извлекает значение атрибута из элемента и возвращает его.
- Если атрибут имеет формат словаря, он разбирает строку словаря и извлекает соответствующие атрибуты из веб-элемента.
- Возвращает значение атрибута, список значений атрибутов или `None`, если элемент не найден.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (str, optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.

**Возвращает**:
- `Optional[WebElement | list[WebElement]]`: Значение атрибута(ов) в виде `WebElement`, списка `WebElement` или `None`, если не найдено.

**Вызывает исключения**:
- Нет

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
) -> Optional[WebElement | List[WebElement]]:
```

**Назначение**:
Извлекает веб-элемент или список элементов на основе предоставленного локатора.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания и условие ожидания события.
- Использует `driver.find_elements` для поиска элементов на странице.
- Если указан таймаут, использует `WebDriverWait` для ожидания появления элементов.
- Вызывает внутреннюю асинхронную функцию `_parse_elements_list` для фильтрации списка веб-элементов на основе атрибута `if_list` локатора.
- Возвращает веб-элемент, список веб-элементов или `None`, если элементы не найдены.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: `WebElement`, список `WebElement` или `None`, если не найдено.

**Вызывает исключения**:
- Нет

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
```

**Назначение**:
Делает скриншот найденного веб-элемента.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания и условие ожидания события.
- Если `webelement` не предоставлен, пытается получить его с помощью `get_webelement_by_locator`.
- Если веб-элемент найден, делает его скриншот и возвращает в виде потока `BinaryIO`.
- Возвращает `None`, если веб-элемент не найден или не удалось сделать скриншот.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.
- `webelement` (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

**Возвращает**:
- `Optional[BinaryIO]`: Поток `BinaryIO` скриншота или `None`, если не удалось.

**Вызывает исключения**:
- Нет

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
```

**Назначение**:
Выполняет событие, связанное с локатором.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания, условие ожидания события, сообщение для отправки и скорость ввода текста.
- Получает веб-элемент с помощью метода `get_webelement_by_locator`.
- Разделяет строку события на отдельные события, разделенные символом `;`.
- Выполняет каждое событие в цикле. Поддерживаются события, такие как `click()`, `pause()`, `upload_media()`, `screenshot()`, `clear()` и `send_keys()`.
- Возвращает результат выполнения события.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки с событием. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость ввода текста для событий `send_keys` в секундах. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события (str, список str, bytes, список bytes или bool).

**Вызывает исключения**:
- Нет

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
```

**Назначение**:
Отправляет сообщение веб-элементу.

**Как работает функция**:
- Принимает локатор элемента, таймаут ожидания, условие ожидания события, сообщение для отправки и скорость ввода текста.
- Получает веб-элемент с помощью метода `get_webelement_by_locator`.
- Использует `ActionChains` для ввода текста в элемент с заданной скоростью.
- Поддерживает замену символов, таких как `;`, на `SHIFT+ENTER`.
- Возвращает `True`, если сообщение было успешно отправлено, и `False` в противном случае.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания события (`'presence_of_element_located'`, `'visibility_of_all_elements_located'`). По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки веб-элементу. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость ввода текста для событий `send_keys` в секундах. По умолчанию `0`.

**Возвращает**:
- `bool`: `True`, если сообщение было отправлено успешно, `False` в противном случае.

**Вызывает исключения**:
- Нет