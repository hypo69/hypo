# Модуль executor

## Обзор

Модуль `executor` предоставляет класс `ExecuteLocator` для выполнения действий с веб-элементами на основе локаторов.  Класс использует Selenium WebDriver для взаимодействия с веб-страницей и предоставляет методы для поиска, навигации, взаимодействия и получения атрибутов элементов.

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` отвечает за выполнение действий с веб-элементами, используя предопределенные локаторы.

**Атрибуты**:

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий.
- `by_mapping`: Словарь для преобразования строковых представлений локаторов в объекты `By` (Selenium).


**Методы**:

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса. Инициализирует `driver` и `actions`.

**Параметры**:
- `driver`: Экземпляр `webdriver`.


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**: Основной метод для выполнения действий с элементом, указанным в `locator`.

**Параметры**:
- `locator` (dict): Словарь, содержащий информацию о локаторе.
- `message` (str, optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора текста (если требуется). По умолчанию `0`.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при ошибке. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия или `bool` (успех/неудача).


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Возвращает веб-элемент(ы) по указанному локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с данными локатора.
- `message` (str, optional): Сообщение.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Веб-элемент(ы) или `bool` (успех/неудача).


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Возвращает атрибут веб-элемента по локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с данными локатора.
- `message` (str, optional): Сообщение.

**Возвращает**:
- `str | list | dict | bool`: Атрибут веб-элемента или `bool` (успех/неудача).



#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для получения атрибута элемента.

**Параметры**:
- `element` (WebElement): Веб-элемент.
- `attribute` (str): Название атрибута.

**Возвращает**:
- `str | None`: Значение атрибута или `None`.



#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

**Описание**: Отправляет сообщение в текстовое поле.

**Параметры**:
- `locator`: Словарь с локатором элемента.
- `message`: Сообщение.
- `typing_speed`: Скорость набора текста.
- `continue_on_error`: Флаг продолжения при ошибке.

**Возвращает**:
- `bool`: Успех/неудача.



#### `evaluate_locator(self, attribute: str | list | dict) -> str`

**Описание**: Оценивает локатор.

**Параметры**:
- `attribute`: Атрибут для оценки.


#### `_evaluate(self, attribute: str) -> str | None`

**Описание**: Вспомогательный метод оценки атрибута.


#### `get_locator_keys() -> list`

**Описание**: Возвращает список доступных ключей для локаторов.


## Примеры Локаторов

Примеры локаторов показаны в коде.


```