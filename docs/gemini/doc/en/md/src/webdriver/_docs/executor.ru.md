# webdriver/executor.ru.md

## Обзор

Модуль `executor.py` предоставляет класс `ExecuteLocator` для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver.  Класс обрабатывает различные типы локаторов, позволяя настраиваемо взаимодействовать с веб-страницей.

## Содержание

### Таблица содержания

[Обзор](#обзор)
[Классы](#классы)
[Функции](#функции)
[Примеры локаторов](#примеры-локаторов)


## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предназначен для выполнения действий с веб-элементами, используя локаторы в виде словарей. Он обеспечивает абстракцию для различных типов взаимодействий (нажатия, ввод текста, получение атрибутов) и обработки потенциальных ошибок.

**Атрибуты**:

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами.
- `by_mapping`: Словарь для отображения строк локаторов в объекты `By` из Selenium.

**Методы**:

#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Конструктор класса, инициализирующий `webdriver` и `ActionChains`.

**Параметры**:
- `driver`: Экземпляр `webdriver`.


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**: Основной метод для выполнения действий по заданному локатору.

**Параметры**:
- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, optional): Сообщение для отправки, если необходимо. Defaults to `None`.
- `typing_speed` (float, optional): Скорость ввода текста. Defaults to `0`.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при ошибке. Defaults to `True`.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия или `False` при ошибке, если `continue_on_error` равен `False`.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Получение элемента(ов) на основе локатора.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с данными локатора.
- `message` (str, optional): Сообщение для логирования. Defaults to `None`.

**Возвращает**:
- `WebElement | List[WebElement] | bool`: Найденный элемент или список элементов, или `False` при ошибке.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Описание**: Получение атрибута элемента по локатору.

**Параметры**:
- `locator` (dict | SimpleNamespace): Словарь или `SimpleNamespace` с локатором.
- `message` (str, optional): Сообщение для логирования. Defaults to `None`.

**Возвращает**:
- `str | list | dict | bool`: Значение атрибута или `False` при ошибке.


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для получения атрибута веб-элемента.

**Параметры**:
- `element` (WebElement): Веб-элемент.
- `attribute` (str): Имя атрибута.

**Возвращает**:
- `str | None`: Значение атрибута или `None` при ошибке.


#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

**Описание**: Отправка сообщения элементу.

**Параметры**:
- `locator`: Локатор элемента.
- `message`: Сообщение для отправки.
- `typing_speed`: Скорость набора текста.
- `continue_on_error`: Флаг для обработки ошибок.

**Возвращает**:
- `bool`: `True` при успехе, `False` при ошибке.


#### `evaluate_locator(self, attribute: str | list | dict) -> str`

**Описание**: Оценивает атрибут локатора.

**Параметры**:
- `attribute`: Атрибут локатора.


#### `_evaluate(self, attribute: str) -> str | None`

**Описание**: Вспомогательный метод для оценки атрибута.


#### `get_locator_keys() -> list`

**Описание**: Возвращает список доступных ключей локатора.


## Функции

(Список функций, если они есть, будет здесь)


## Примеры локаторов

(Примеры локаторов, как показано в коде, будут здесь, форматированные как JSON)

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,\'node-galery\')]//li[contains(@class,\'item\')]//a",
    "selector 2": "//span[@data-component-type=\'s-product-image\']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "event": null
  },
  ...
}
```