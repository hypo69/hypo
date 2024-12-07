# Модуль executor

## Обзор

Модуль `executor` содержит класс `ExecuteLocator`, предназначенный для выполнения действий с элементами веб-страницы с использованием Selenium WebDriver на основе конфигурационных данных (локаторов).

## Оглавление

* [Общая Структура и Назначение](#общая-структура-и-назначение)
* [Классы](#классы)
    * [ExecuteLocator](#executelocator)
* [Методы](#методы)
    * [`__init__`](#init)
    * [`execute_locator`](#execute-locator)
    * [`get_webelement_by_locator`](#get-webelement-by-locator)
    * [`get_attribute_by_locator`](#get-attribute-by-locator)
    * [`_get_element_attribute`](#_get-element-attribute)
    * [`send_message`](#send-message)
    * [`evaluate_locator`](#evaluate-locator)
    * [`_evaluate`](#_evaluate)
    * [`get_locator_keys`](#get-locator-keys)
* [Примеры Локаторов](#примеры-локаторов)


## Классы

### `ExecuteLocator`

**Описание**: Класс `ExecuteLocator` предоставляет методы для взаимодействия с веб-элементами на основе локаторов, заданных в виде словарей.

**Атрибуты**:

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами.
- `by_mapping`: Словарь для преобразования строковых представлений локаторов в объекты `By`.


## Методы

### `__init__`

**Описание**: Конструктор класса `ExecuteLocator`.

**Параметры**:

- `driver`: Экземпляр `webdriver`.

**Возвращает**:
-  Не имеет возвращаемого значения.

```python
def __init__(self, driver, *args, **kwargs):
    """
    Инициализирует экземпляр класса ExecuteLocator.

    Args:
        driver: Экземпляр класса webdriver.
    """
    self.driver = driver
    self.actions = ActionChains(driver)
```

### `execute_locator`

**Описание**: Основной метод для выполнения действий по локатору.

**Параметры**:

- `locator` (dict): Словарь с параметрами для выполнения действий.
- `message` (str, optional): Сообщение для отправки. По умолчанию None.
- `typing_speed` (float, optional): Скорость набора текста при отправке сообщений. По умолчанию 0.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при ошибке. По умолчанию True.

**Возвращает**:
- Union[str, list, dict, WebElement, bool]: Результат выполнения действий по локатору.

**Вызывает исключения**:
- `NoSuchElementException`: Если элемент не найден.
- `TimeoutException`: Если ожидание элемента превысило установленный таймаут.
- `ExecuteLocatorException`: Общие ошибки при выполнении локатора.


```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    """
    Выполняет действие по локатору.

    Args:
        locator (dict): Словарь с параметрами для выполнения действий.
        message (str, optional): Сообщение для отправки. По умолчанию None.
        typing_speed (float, optional): Скорость набора текста при отправке сообщений. По умолчанию 0.
        continue_on_error (bool, optional): Флаг для продолжения выполнения при ошибке. По умолчанию True.

    Returns:
        Union[str, list, dict, WebElement, bool]: Результат выполнения действий по локатору.

    Raises:
        NoSuchElementException: Если элемент не найден.
        TimeoutException: Если ожидание элемента превысило установленный таймаут.
        ExecuteLocatorException: Общие ошибки при выполнении локатора.
    """
    # ... (Тело метода)
```

(Аналогично, опишите остальные методы с подробными комментариями, включая типы возвращаемых значений, возможные исключения и описание параметров)


## Примеры Локаторов

Примеры локаторов приведены в коде.


```
```