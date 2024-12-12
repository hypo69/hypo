# Модуль `executor.py` (src.webdriver)

## Обзор

Модуль `executor.py` содержит класс `ExecuteLocator`, предназначенный для выполнения действий с элементами веб-страницы, используя Selenium WebDriver.  Класс обрабатывает различные типы локаторов, позволяя гибко взаимодействовать с веб-страницей на основе конфигурации.

## Оглавление

- [Модуль `executor.py`](#модуль-executorpy-srcwebdriver)
    - [Обзор](#обзор)
    - [Класс `ExecuteLocator`](#класс-executelocator)
        - [Атрибуты](#атрибуты)
        - [Методы](#методы)
            - [`__init__`](#init)
            - [`execute_locator`](#execute-locator)
            - [`get_webelement_by_locator`](#get-webelement-by-locator)
            - [`get_attribute_by_locator`](#get-attribute-by-locator)
            - [`_get_element_attribute`](#_get-element-attribute)
            - [`send_message`](#send-message)
            - [`evaluate_locator`](#evaluate-locator)
            - [`_evaluate`](#_evaluate)
            - [`get_locator_keys`](#get-locator-keys)
    - [Примеры локаторов](#примеры-локаторов)

## Класс `ExecuteLocator`

### Атрибуты

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains`, предназначенный для сложных действий с элементами.
- `by_mapping`: Словарь, сопоставляющий строковые представления локаторов (`'id'`, `'name'`, `'xpath'`) с соответствующими объектами `By` из Selenium.

### Методы

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса. Инициализирует `driver` и `actions` для взаимодействия с браузером.

**Параметры**:
- `driver`: Экземпляр `webdriver`.

**Возвращает**:
-  Ничего.


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**: Основной метод для выполнения действия по локатору.  Выбирает подходящий метод в зависимости от типа локатора.

**Параметры**:
- `locator (dict)`: Словарь с параметрами для выполнения действия.
- `message (str, optional)`: Сообщение для отправки (например, в текстовое поле). По умолчанию `None`.
- `typing_speed (float, optional)`: Скорость набора текста. По умолчанию 0 (стандартная скорость).
- `continue_on_error (bool, optional)`: Флаг, определяющий, продолжать ли выполнение при возникновении ошибки. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия (например, текст элемента, список элементов, атрибут элемента, True/False). Возвращает `None` в случае ошибки, если `continue_on_error=False`.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка при взаимодействии с WebDriver.
- `ExecuteLocatorException`: При специфических ошибках работы с локаторами.



#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Получает элемент(ы) на основе локатора.

**Параметры**:
- `locator (dict | SimpleNamespace)`: Словарь или объект `SimpleNamespace` с параметрами локатора.
- `message (str, optional)`: Сообщение для отладки. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Найденный элемент (или список элементов), или `False` при неудачном поиске.

**Вызывает исключения**:
- `NoSuchElementException`: Если элемент не найден.
- `TimeoutException`: Если поиск превысил заданное время ожидания.



#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Получает атрибут элемента по локатору.

#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для получения атрибута элемента.

#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

**Описание**: Отправляет сообщение элементу.


#### `evaluate_locator(self, attribute: str | list | dict) -> str`

**Описание**: Оценивает атрибут локатора.


#### `_evaluate(self, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для оценки одного атрибута.


#### `get_locator_keys() -> list`

**Описание**: Возвращает список доступных ключей локатора.


## Примеры локаторов

(Здесь описываются примеры JSON-локаторов, как они представлены в коде.)


```
```