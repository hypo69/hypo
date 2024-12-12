# Модуль `executor`

## Обзор

Модуль `executor` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий над элементами веб-страницы с помощью Selenium WebDriver. Он обрабатывает локаторы, позволяя навигацию и взаимодействие со страницей на основе предоставленных данных.

## Оглавление

* [Модуль `executor`](#модуль-executor)
* [Обзор](#обзор)
* [Класс `ExecuteLocator`](#класс-executelocator)
    * [Атрибуты](#атрибуты)
    * [Методы](#методы)
    * [Примеры локаторов](#примеры-локаторов)
* [Обработка ошибок](#обработка-ошибок)
* [Использование](#использование)
* [Зависимости](#зависимости)
* [Пример использования](#пример-использования)


## Класс `ExecuteLocator`

### Атрибуты

* **`driver`**: Экземпляр WebDriver для взаимодействия с браузером.
* **`actions`**: Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
* **`by_mapping`**: Словарь, сопоставляющий строковые представления локаторов с объектами `By` Selenium.


### Методы

#### `__init__(self, driver, *args, **kwargs)`

Конструктор класса. Инициализирует экземпляр WebDriver и `ActionChains`.

```python
def __init__(self, driver, *args, **kwargs):
    """
    Инициализирует экземпляр ExecuteLocator.

    Args:
        driver: Экземпляр WebDriver.
        *args: Дополнительные аргументы.
        **kwargs: Дополнительные ключевые аргументы.
    """
    self.driver = driver
    self.actions = ActionChains(driver)
```

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

Основной метод для выполнения действий на основе локатора.

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    """
    Выполняет действие на основе локатора.

    Args:
        locator (dict): Словарь с параметрами для выполнения действия.
        message (str, optional): Сообщение для отправки. По умолчанию None.
        typing_speed (float, optional): Скорость набора текста. По умолчанию 0.
        continue_on_error (bool, optional): Флаг, указывающий на продолжение выполнения при ошибке. По умолчанию True.

    Returns:
        Union[str, list, dict, WebElement, bool]: Результат выполнения действия. Возвращает строку, список, словарь, WebElement или bool.

    Raises:
        ExecuteLocatorException: Если возникла ошибка при выполнении действия.
    """
    # ... (реализация метода)
```

(Аналогичные описания для остальных методов: `get_webelement_by_locator`, `get_attribute_by_locator`, `_get_element_attribute`, `send_message`, `evaluate_locator`, `_evaluate`, `get_locator_keys`)


### Примеры локаторов

Примеры JSON-представлений локаторов, используемые для тестирования.


## Обработка ошибок

Модуль использует блоки `try...except` для обработки потенциальных ошибок, таких как `NoSuchElementException`, `TimeoutException`, `WebDriverException`.

## Использование

Для использования модуля необходимо создать экземпляр класса `ExecuteLocator` и вызвать метод `execute_locator` с соответствующим локатором.

## Зависимости

Модуль `executor` использует Selenium WebDriver для взаимодействия с браузером.

## Пример использования

(Здесь приводится пример использования, взятый из входного кода.)


```python
# ... (пример использования)
```


```markdown