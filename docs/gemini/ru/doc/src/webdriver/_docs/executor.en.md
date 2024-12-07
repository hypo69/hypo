# WebDriver Executor

## Обзор

Модуль `webdriver/executor.py` предоставляет класс `ExecuteLocator` для выполнения различных действий над элементами веб-страницы с помощью Selenium WebDriver.  Он обрабатывает локейторы, определяющие элементы, и выполняет с ними заданные операции.

## Оглавление

- [WebDriver Executor](#webdriver-executor)
- [Обзор](#обзор)
- [Класс `ExecuteLocator`](#класс-executelocator)
    - [Атрибуты](#атрибуты)
    - [Методы](#методы)
        - [`__init__`](#init)
        - [`execute_locator`](#execute_locator)
        - [`get_webelement_by_locator`](#get_webelement_by_locator)
        - [`get_attribute_by_locator`](#get_attribute_by_locator)
        - [\_`get_element_attribute`](#_get_element_attribute)
        - [`send_message`](#send_message)
        - [`evaluate_locator`](#evaluate_locator)
        - [\_`evaluate`](#_evaluate)
        - [`get_locator_keys`](#get_locator_keys)
- [Примеры локейторов](#примеры-локейторов)
- [Обработка ошибок](#обработка-ошибок)
- [Использование](#использование)
- [Зависимости](#зависимости)
- [Пример использования](#пример-использования)


## Класс `ExecuteLocator`

### Атрибуты

- `driver`: Экземпляр WebDriver для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами.
- `by_mapping`: Словарь, сопоставляющий строковые представления локейторов с объектами Selenium `By`.

### Методы

#### `__init__(self, driver, *args, **kwargs)`

Инициализирует экземпляр класса.

```python
def __init__(self, driver, *args, **kwargs):
    """
    Инициализирует экземпляр класса.

    Args:
        driver: Экземпляр WebDriver.
        *args: Дополнительные аргументы.
        **kwargs: Дополнительные ключевые аргументы.
    """
    self.driver = driver
    self.actions = ActionChains(driver)
```

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

Выполняет действия, заданные в локейторе.

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    """
    Выполняет действия, заданные в локейторе.

    Args:
        locator (dict): Словарь с параметрами для действий.
        message (str, optional): Сообщение для отправки (если необходимо). По умолчанию None.
        typing_speed (float, optional): Скорость ввода. По умолчанию 0.
        continue_on_error (bool, optional): Флаг, указывающий на продолжение выполнения при ошибке. По умолчанию True.

    Returns:
        Union[str, list, dict, WebElement, bool]: Результат выполнения (строка, список, словарь, элемент WebElement или bool).

    Raises:
        ExecuteLocatorException:  При возникновении ошибки при выполнении действий.
    """
    # ... (реализация метода) ...
```

(Другие методы аналогичным образом описываются с указанием аргументов, возвращаемых значений и возможных исключений)

#### `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message`, `evaluate_locator`, `_evaluate`, `get_locator_keys`


## Примеры локейторов

Примеры локейторов показаны в коде.

```json
{
  // ... (примеры)
}
```

## Обработка ошибок

Модуль использует блоки `try-except` для обработки исключений, таких как `NoSuchElementException` и `TimeoutException`.


## Использование

Для использования модуля необходимо создать экземпляр `ExecuteLocator` с объектом WebDriver.  Затем вызвать `execute_locator` с соответствующим локейтором.


## Зависимости

Модуль использует Selenium WebDriver для взаимодействия с браузером.


## Пример использования

```python
# ... (Пример использования из документации) ...
```


```
```