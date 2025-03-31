# Модуль `executor`

## Обзор

Модуль `executor` предоставляет функциональность для взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов. Он обрабатывает разбор локаторов, взаимодействие с элементами и обработку ошибок. Этот модуль является ключевым компонентом для автоматизированного взаимодействия с веб-страницами, позволяя находить элементы на странице по различным локаторам, выполнять с ними различные действия и получать значения их атрибутов. Модуль также включает механизмы ожидания появления элементов и обработки возможных ошибок, таких как таймауты и перехваты кликов.

## Подробней

Модуль `executor` предназначен для упрощения и стандартизации работы с веб-элементами через Selenium. Он предоставляет класс `ExecuteLocator`, который инкапсулирует логику поиска элементов, выполнения действий над ними и обработки возникающих исключений. Модуль использует асинхронный подход, что позволяет эффективно выполнять параллельные операции и уменьшает время ожидания.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для обработки взаимодействия с веб-элементами с использованием Selenium на основе предоставленных локаторов.

**Как работает класс**:
Класс `ExecuteLocator` инициализируется с драйвером Selenium и использует `ActionChains` для выполнения сложных действий, таких как ввод текста с заданной скоростью. Основной метод `execute_locator` принимает локатор элемента и выполняет соответствующие действия, такие как клик, ввод текста или получение атрибутов. Класс также обрабатывает различные исключения, которые могут возникнуть в процессе выполнения действий.

**Методы**:
- `__post_init__`: Инициализирует экземпляр `ActionChains` после создания экземпляра класса, если предоставлен драйвер.
- `execute_locator`: Выполняет действия над веб-элементом на основе предоставленного локатора.
- `_parse_locator`: Разбирает инструкции локатора и выполняет соответствующие действия.
- `_evaluate_locator`: Вычисляет и обрабатывает атрибуты локатора.
- `get_attribute_by_locator`: Получает атрибуты веб-элемента или списка веб-элементов.
- `get_webelement_by_locator`: Получает веб-элемент или список элементов на основе предоставленного локатора.
- `get_webelement_as_screenshot`: Делает скриншот найденного веб-элемента.
- `execute_event`: Выполняет событие, связанное с локатором.
- `send_message`: Отправляет сообщение веб-элементу.

#### `__post_init__`

```python
def __post_init__(self):
    ...
```

**Описание**: Инициализирует экземпляр `ActionChains` после создания экземпляра класса, если предоставлен драйвер.

**Как работает функция**:
Если при создании экземпляра класса `ExecuteLocator` был передан драйвер, этот метод инициализирует атрибут `actions` экземпляром класса `ActionChains`, который используется для выполнения сложных действий с веб-элементами, таких как последовательный ввод текста или перемещение мыши.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

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
    ...
```

**Описание**: Выполняет действия над веб-элементом на основе предоставленного локатора.

**Как работает функция**:
Метод `execute_locator` является основным методом класса `ExecuteLocator`. Он принимает локатор элемента, таймаут для поиска элемента, условие ожидания, сообщение (для отправки текста) и скорость печати. В зависимости от типа локатора и указанных атрибутов, метод выполняет различные действия, такие как получение атрибута элемента, выполнение события (например, клик) или получение самого веб-элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Сообщение для отправки элементу. По умолчанию `None`.
- `typing_speed` (Optional[float], optional): Скорость печати текста в секундах. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или `None`.

#### `_parse_locator`

```python
async def _parse_locator(
    locator: SimpleNamespace,
    message: Optional[str] = None,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
    typing_speed: Optional[float] = 0,
) -> Optional[str | list | dict | WebElement | bool]:
    ...
```

**Описание**: Разбирает инструкции локатора и выполняет соответствующие действия.

**Как работает функция**:
Метод `_parse_locator` принимает объект `SimpleNamespace` с данными локатора и выполняет действия в зависимости от атрибутов локатора, таких как `by`, `attribute` и `event`. Если указан атрибут `attribute`, метод пытается получить значение этого атрибута из веб-элемента. Если указано событие `event`, метод выполняет это событие (например, клик или ввод текста).

**Параметры**:
- `locator` (SimpleNamespace): Данные локатора.
- `message` (Optional[str], optional): Сообщение для отправки элементу. По умолчанию `None`.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `typing_speed` (Optional[float], optional): Скорость печати текста в секундах. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list | dict | WebElement | bool]`: Результат операции, который может быть строкой, списком, словарем, веб-элементом, булевым значением или `None`.

#### `_evaluate_locator`

```python
def _evaluate_locator(self, attribute: str | List[str] | dict) -> Optional[str | List[str] | dict]:
    ...
```

**Описание**: Вычисляет и обрабатывает атрибуты локатора.

**Как работает функция**:
Метод `_evaluate_locator` принимает атрибут локатора (строку, список строк или словарь) и обрабатывает его. Если атрибут является строкой и соответствует определенному шаблону (например, `%KEY_NAME%`), метод пытается заменить его значением из атрибутов класса `Keys` в Selenium.

**Параметры**:
- `attribute` (str | List[str] | dict): Атрибут для вычисления.

**Возвращает**:
- `Optional[str | List[str] | dict]`: Вычисленный атрибут, который может быть строкой, списком строк или словарем.

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
    ...
```

**Описание**: Получает атрибуты веб-элемента или списка веб-элементов.

**Как работает функция**:
Метод `get_attribute_by_locator` принимает локатор элемента, таймаут и условие ожидания. Сначала он получает веб-элемент с помощью метода `get_webelement_by_locator`. Затем, в зависимости от типа атрибута (строка или словарь), метод получает значение атрибута из веб-элемента и возвращает его.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (str, optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.

**Возвращает**:
- `Optional[WebElement | list[WebElement]]`: Значение атрибута, которое может быть веб-элементом, списком веб-элементов или `None`, если элемент не найден.

#### `get_webelement_by_locator`

```python
async def get_webelement_by_locator(
    self,
    locator: dict | SimpleNamespace,
    timeout: Optional[float] = 0,
    timeout_for_event: Optional[str] = "presence_of_element_located",
) -> Optional[WebElement | List[WebElement]]:
    ...
```

**Описание**: Получает веб-элемент или список элементов на основе предоставленного локатора.

**Как работает функция**:
Метод `get_webelement_by_locator` принимает локатор элемента, таймаут и условие ожидания. Он использует Selenium для поиска элемента на странице. Если указан таймаут, метод ожидает появления элемента в течение заданного времени. Если элемент найден, метод возвращает его; в противном случае возвращается `None`.

**Параметры**:
- `locator` (dict | SimpleNamespace): Данные локатора.
- `timeout` (Optional[float], optional): Таймаут для поиска элемента в секундах. По умолчанию `0`.
- `timeout_for_event` (Optional[str], optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.

**Возвращает**:
- `Optional[WebElement | List[WebElement]]`: Веб-элемент, список веб-элементов или `None`, если элемент не найден.

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
    ...
```

**Описание**: Делает скриншот найденного веб-элемента.

**Как работает функция**:
Метод `get_webelement_as_screenshot` принимает локатор элемента, таймаут и условие ожидания. Сначала он получает веб-элемент с помощью метода `get_webelement_by_locator` или использует уже переданный `webelement`. Затем метод делает скриншот элемента и возвращает его в виде бинарного потока.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `message` (Optional[str], optional): Не используется в этой функции. По умолчанию `None`.
- `typing_speed` (float, optional): Не используется в этой функции. По умолчанию `0`.
- `webelement` (Optional[WebElement], optional): Предварительно полученный веб-элемент. По умолчанию `None`.

**Возвращает**:
- `Optional[BinaryIO]`: Бинарный поток скриншота или `None`, если не удалось сделать скриншот.

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
    ...
```

**Описание**: Выполняет событие, связанное с локатором.

**Как работает функция**:
Метод `execute_event` принимает локатор элемента, таймаут, условие ожидания, сообщение и скорость печати. Он получает веб-элемент с помощью метода `get_webelement_by_locator` и выполняет событие, указанное в локаторе. Поддерживаются различные события, такие как клик, пауза, загрузка медиа, создание скриншота, очистка поля и отправка клавиш.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки с событием. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати текста в секундах. По умолчанию `0`.

**Возвращает**:
- `Optional[str | list[str] | bytes | list[bytes] | bool]`: Результат выполнения события.

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
    ...
```

**Описание**: Отправляет сообщение веб-элементу.

**Как работает функция**:
Метод `send_message` принимает локатор элемента, таймаут, условие ожидания, сообщение и скорость печати. Он получает веб-элемент с помощью метода `get_webelement_by_locator` и отправляет сообщение в элемент, используя `ActionChains` для эмуляции ввода текста с заданной скоростью.

**Параметры**:
- `locator` (SimpleNamespace | dict): Данные локатора.
- `timeout` (float, optional): Таймаут для поиска элемента в секундах. По умолчанию `5`.
- `timeout_for_event` (str, optional): Условие ожидания. По умолчанию `"presence_of_element_located"`.
- `message` (str, optional): Сообщение для отправки в веб-элемент. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость печати текста в секундах. По умолчанию `0`.

**Возвращает**:
- `bool`: `True`, если сообщение было успешно отправлено, `False` в противном случае.