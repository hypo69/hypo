# Модуль `executor`

## Обзор

Модуль `executor` содержит класс `ExecuteLocator`, предназначенный для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver.  Класс обрабатывает различные типы локаторов, позволяя настраивать поведение и управлять ошибками.

## Оглавление

* [Общая Структура и Назначение](#общая-структура-и-назначение)
* [Классы](#классы)
    * [ExecuteLocator](#executelocator)
* [Примеры Локаторов](#примеры-локаторов)

## Классы

### `ExecuteLocator`

**Описание**: Основной класс для выполнения действий с веб-элементами.

**Атрибуты**:

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами.
- `by_mapping`: Словарь для преобразования строковых локаторов в объекты `By`.

**Методы**:

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса, инициализирующий `driver` и `actions`.

**Параметры**:
- `driver`: Экземпляр `webdriver`.

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**:  Основной метод для выполнения действий по локатору.

**Параметры**:
- `locator` (dict): Словарь с параметрами для выполнения действий (см. примеры локаторов).
- `message` (str, optional): Сообщение для отправки элементу (если необходимо). По умолчанию `None`.
- `typing_speed` (float, optional): Скорость набора текста при отправке сообщений. По умолчанию `0`.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при возникновении ошибки. По умолчанию `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия. Может быть строкой, списком, словарем, объектом `WebElement` или булевым значением в зависимости от действия.

**Вызывает исключения**:
- `NoSuchElementException`: Если элемент не найден.
- `TimeoutException`: Если ожидание элемента превысило установленное время.
- `ExecuteLocatorException`:  Если возникла ошибка при выполнении действия.

#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**:  Получает элемент(ы) на основе локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с параметрами локатора.
- `message` (str, optional): Сообщение. По умолчанию `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Возвращает найденный элемент или список элементов, или `False`, если элемент не найден.

**Вызывает исключения**:
- Аналогично `execute_locator`.

#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Получает атрибут элемента по заданному локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с параметрами локатора.
- `message` (str, optional): Сообщение. По умолчанию `None`.

**Возвращает**:
- `str | list | dict | bool`: Значение атрибута или `False`, если элемент или атрибут не найдены.

**Вызывает исключения**:
- Аналогично `execute_locator`.


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`
#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`
#### `evaluate_locator(self, attribute: str | list | dict) -> str`
#### `_evaluate(self, attribute: str) -> str | None`
#### `get_locator_keys() -> list`

(Подробные описания этих методов следует добавить аналогично предыдущим.)

## Примеры Локаторов

(Пример JSON локаторов приведен в запросе, но здесь следует добавить более развернутые пояснения к использованию разных типов локаторов и их значениям в `locator`.)

```