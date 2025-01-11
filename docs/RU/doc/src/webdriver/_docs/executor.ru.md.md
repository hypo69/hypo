# Модуль `src.webdriver.executor`

## Обзор

Модуль `executor.py` содержит класс `ExecuteLocator`, который предназначен для выполнения различных действий с элементами веб-страницы с использованием Selenium WebDriver. Класс позволяет выполнять навигационные алгоритмы и взаимодействия с веб-страницей на основе конфигурационных данных, представленных в виде словарей локаторов.

## Оглавление

- [Обзор](#обзор)
- [Классы](#классы)
    - [`ExecuteLocator`](#ExecuteLocator)
- [Функции](#функции)
    - [`get_locator_keys`](#get_locator_keys)

## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для выполнения действий с веб-элементами и обработки локаторов.

**Методы**:
- [`__init__`](#__init__)
- [`execute_locator`](#execute_locator)
- [`get_webelement_by_locator`](#get_webelement_by_locator)
- [`get_attribute_by_locator`](#get_attribute_by_locator)
- [`_get_element_attribute`](#_get_element_attribute)
- [`send_message`](#send_message)
- [`evaluate_locator`](#evaluate_locator)
- [`_evaluate`](#_evaluate)

#### `__init__`
```python
def __init__(self, driver, *args, **kwargs)
```
**Описание**: Конструктор класса, который инициализирует WebDriver и `ActionChains`.

**Параметры**:
- `driver` (webdriver): Экземпляр WebDriver.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

#### `execute_locator`
```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]
```
**Описание**: Основной метод для выполнения действий по локатору.

**Параметры**:
- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, optional): Сообщение для отправки. По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора текста при отправке сообщений. По умолчанию `0`.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при возникновении ошибки. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия, может быть строкой, списком, словарем, элементом WebElement или булевым значением.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает при ошибках во время выполнения локатора.

#### `get_webelement_by_locator`
```python
def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool
```
**Описание**: Получение элемента(ов) на основе локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Возвращает веб-элемент, список веб-элементов или `False`, если элемент не найден.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает при ошибках во время поиска элемента.

#### `get_attribute_by_locator`
```python
def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool
```
**Описание**: Получение атрибута элемента.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:
- `str | list | dict | bool`: Возвращает значение атрибута, список атрибутов, словарь или `False`, если элемент не найден.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает при ошибках во время получения атрибута.

#### `_get_element_attribute`
```python
def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None
```
**Описание**: Вспомогательный метод для получения атрибута элемента.

**Параметры**:
- `element` (WebElement): Веб-элемент.
- `attribute` (str): Название атрибута.

**Возвращает**:
- `str | None`: Значение атрибута или `None`, если атрибут не найден.

#### `send_message`
```python
def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool
```
**Описание**: Отправка сообщения элементу.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или SimpleNamespace с параметрами локатора.
- `message` (str): Сообщение для отправки.
- `typing_speed` (float): Скорость набора текста.
- `continue_on_error` (bool): Флаг для продолжения выполнения при ошибке.

**Возвращает**:
- `bool`: `True` при успешной отправке, иначе `False`.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает при ошибках во время отправки сообщения.

#### `evaluate_locator`
```python
def evaluate_locator(self, attribute: str | list | dict) -> str
```
**Описание**: Оценка атрибута локатора.

**Параметры**:
- `attribute` (str | list | dict): Атрибут для оценки.

**Возвращает**:
- `str`: Оцененное значение атрибута.

#### `_evaluate`
```python
def _evaluate(self, attribute: str) -> str | None
```
**Описание**: Вспомогательный метод для оценки одного атрибута.

**Параметры**:
- `attribute` (str): Атрибут для оценки.

**Возвращает**:
- `str | None`: Оцененное значение атрибута или `None`, если атрибут не найден.

## Функции

### `get_locator_keys`
```python
@staticmethod
def get_locator_keys() -> list
```
**Описание**: Возвращает список доступных ключей локатора.

**Возвращает**:
- `list`: Список строк, представляющих ключи локатора.