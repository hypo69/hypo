# Модуль `executor` для Selenium WebDriver

## Обзор

Этот модуль предоставляет класс `ExecuteLocator`, предназначенный для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver. Класс использует конфигурацию в виде словарей для определения действий и локаторов элементов.

## Оглавление

* [Общая Структура и Назначение](#общая-структура-и-назначение)
* [Классы](#классы)
    * [ExecuteLocator](#executelocator)
* [Методы класса ExecuteLocator](#методы-класса-executelocator)
    * [`__init__`](#init)
    * [`execute_locator`](#executelocator)
    * [`get_webelement_by_locator`](#getwebelementbylocator)
    * [`get_attribute_by_locator`](#getattributebylocator)
    * [`_get_element_attribute`](#_getelementattribute)
    * [`send_message`](#sendmessage)
    * [`evaluate_locator`](#evaluatelocator)
    * [`_evaluate`](#_evaluate)
    * [`get_locator_keys`](#getlocatorkeys)
* [Примеры Локаторов](#примеры-локаторов)


## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` отвечает за выполнение действий с элементами веб-страницы на основе конфигураций локаторов.

**Атрибуты**:

* `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
* `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами.
* `by_mapping`: Словарь для преобразования строковых представлений локаторов в объекты `By`.

**Методы**:


#### `__init__(self, driver, *args, **kwargs)`

**Описание**: Инициализирует экземпляр класса `ExecuteLocator`.

**Параметры**:

* `driver`: Экземпляр `webdriver`.

**Возвращает**:
    Возвращает `None`.

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Описание**: Выполняет действие, указанное в `locator`.

**Параметры**:

* `locator` (dict): Словарь с описанием действия. Ожидается, что словарь будет содержать ключи, определяющие тип действия (например, `'click'`, `'send_message'`, `'get_attribute'`).
* `message` (str, optional): Текст для отправки в текстовое поле, если требуется. По умолчанию `None`.
* `typing_speed` (float, optional): Скорость набора текста при отправке сообщения. По умолчанию `0`.
* `continue_on_error` (bool, optional): Флаг, определяющий, нужно ли продолжать выполнение при ошибке. По умолчанию `True`.

**Возвращает**:

* `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия. Возвращаемый тип зависит от выполняемого действия.

**Возможные исключения**:

* `NoSuchElementException`: Если элемент не найден.
* `TimeoutException`: Если действие не выполнено в течение заданного времени ожидания.
* `WebDriverException`: Общие ошибки WebDriver.
* `ExecuteLocatorException`: Ошибки, специфичные для этого класса.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Описание**: Получает элемент(ы) на основе локатора.


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


## Примеры Локаторов

Здесь представлены примеры словарей локаторов, которые могут быть использованы для выполнения тестов.  Они иллюстрируют различные способы определения элементов на веб-странице.  Обратите внимание на ключи, указывающие тип локации (например, `'xpath'`, `'id'`), аттрибут (`attribute`) и селектор (`selector`).


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


**Важно:**  Для полноценного понимания, необходимо ознакомиться с реализацией методов в файле `executor.py`.  Этот документ предоставляет структурированное описание API.