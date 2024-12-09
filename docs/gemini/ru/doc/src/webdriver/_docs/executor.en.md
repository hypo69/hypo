# Модуль `executor`

## Обзор

Модуль `executor` предоставляет класс `ExecuteLocator` для выполнения действий на веб-страницах с помощью Selenium WebDriver. Он обрабатывает различные локаторы и действия, базируясь на предоставленных данных конфигурации.

## Оглавление

- [Модуль `executor`](#модуль-executor)
- [Обзор](#обзор)
- [Класс `ExecuteLocator`](#класс-executelocator)
    - [Атрибуты](#атрибуты)
    - [Методы](#методы)
        - [`__init__`](#init)
        - [`execute_locator`](#execute_locator)
        - [`get_webelement_by_locator`](#get_webelement_by_locator)
        - [`get_attribute_by_locator`](#get_attribute_by_locator)
        - [`_get_element_attribute`](#_get_element_attribute)
        - [`send_message`](#send_message)
        - [`evaluate_locator`](#evaluate_locator)
        - [`_evaluate`](#_evaluate)
        - [`get_locator_keys`](#get_locator_keys)
- [Примеры локаторов](#примеры-локаторов)
- [Обработка ошибок](#обработка-ошибок)
- [Использование](#использование)
- [Зависимости](#зависимости)
- [Пример использования](#пример-использования)


## Класс `ExecuteLocator`

### Атрибуты

- `driver`: Экземпляр WebDriver для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий на элементах страницы.
- `by_mapping`: Словарь, сопоставляющий строковые представления локаторов с объектами `By` Selenium.

### Методы

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса, инициализирующий WebDriver и `ActionChains`.

**Аргументы**:

- `driver`: Экземпляр WebDriver.

**Возвращает**:
- Нет


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

**Описание**: Главный метод для выполнения действий, заданных в `locator`.

**Аргументы**:

- `locator` (dict): Словарь с параметрами для действий.
- `message` (str, опционально): Сообщение для отправки, если нужно. По умолчанию `None`.
- `typing_speed` (float, опционально): Скорость ввода текста. По умолчанию `0`.
- `continue_on_error` (bool, опционально): Флаг, указывающий на продолжение выполнения при ошибке. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия. Возвращаемый тип зависит от типа действия, например, текст, список элементов, словарь или сам элемент. Возвращает `False` при ошибке, если `continue_on_error` = `False`.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Возвращает элемент или список элементов, найденных по локатору.

**Аргументы**:

- `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с локатором.
- `message` (str, опционально): Сообщение. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Найденный элемент(ы) или `False`, если элементы не найдены.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Возвращает атрибут элемента по локатору.

**Аргументы**:

- `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с локатором.
- `message` (str, опционально): Сообщение. По умолчанию `None`.

**Возвращает**:
- `str | list | dict | bool`: Атрибут элемента или `False` при ошибке.


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для получения атрибута элемента.

**Аргументы**:

- `element` (WebElement): Элемент, из которого нужно получить атрибут.
- `attribute` (str): Название атрибута.

**Возвращает**:
- `str | None`: Значение атрибута или `None`, если атрибут не найден.


#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

**Описание**: Отправляет сообщение элементу.

**Аргументы**:

- `locator`: Локатор.
- `message`: Текст сообщения.
- `typing_speed`: Скорость набора.
- `continue_on_error`: Флаг продолжения.

**Возвращает**:
- `bool`: Успешность выполнения.


#### `evaluate_locator(self, attribute: str | list | dict) -> str`

**Описание**: Оценивает атрибут локатора.

**Аргументы**:

- `attribute`: Атрибут для оценки.

**Возвращает**:
- `str`: Результат оценки.


#### `_evaluate(self, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для оценки атрибута.

**Аргументы**:

- `attribute`: Атрибут.

**Возвращает**:
- `str | None`: Значение атрибута или `None`.


#### `get_locator_keys() -> list`

**Описание**: Возвращает список доступных ключей локаторов.

**Возвращает**:
- `list`: Список ключей.


## Примеры локаторов

... (Примеры в формате JSON)


## Обработка ошибок

Модуль использует блоки `try-except` для обработки и логирования ошибок.


## Использование

... (Описание использования)


## Зависимости

Модуль использует Selenium WebDriver для работы с браузером.


## Пример использования

```python
# (Пример кода)
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```