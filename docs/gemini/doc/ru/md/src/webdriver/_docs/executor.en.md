# WebDriver Executor

## Обзор

Модуль `executor.py` в пакете `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий с элементами веб-страницы с помощью Selenium WebDriver.  Он обрабатывает навигацию и взаимодействие с веб-страницей, основываясь на данных, предоставленных в виде словарей локейтеров.

## Оглавление

* [Обзор](#обзор)
* [Класс `ExecuteLocator`](#класс-executelocator)
    * [Атрибуты класса](#атрибуты-класса)
    * [Методы класса](#методы-класса)
        * [`__init__(self, driver, *args, **kwargs)`](#init-self-driver-args-kwargs)
        * [`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`](#execute-locator-self-locator-message-typing-speed-continue-on-error)
        * [`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None)`](#get-webelement-by-locator-self-locator-message)
        * [`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None)`](#get-attribute-by-locator-self-locator-message)
        * [`_get_element_attribute(self, element: WebElement, attribute: str)`](#_get-element-attribute-self-element-attribute)
        * [`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool)`](#send-message-self-locator-message-typing-speed-continue-on-error)
        * [`evaluate_locator(self, attribute: str | list | dict)`](#evaluate-locator-self-attribute)
        * [`_evaluate(self, attribute: str)`](#_evaluate-self-attribute)
        * [`get_locator_keys() -> list`](#get-locator-keys-static)
* [Примеры локейтеров](#примеры-локейтеров)
* [Обработка ошибок](#обработка-ошибок)
* [Использование](#использование)
* [Зависимости](#зависимости)
* [Пример использования](#пример-использования)


## Класс `ExecuteLocator`

### Атрибуты класса

* `driver`: Экземпляр WebDriver для взаимодействия с браузером.
* `actions`: Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
* `by_mapping`: Словарь, сопоставляющий строковые представления локейтеров с объектами `By` Selenium.

### Методы класса

#### `__init__(self, driver, *args, **kwargs)`

Инициализирует WebDriver и `ActionChains`:

```python
def __init__(self, driver, *args, **kwargs):
    self.driver = driver
    self.actions = ActionChains(driver)
```

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

Основной метод для выполнения действий на основе локейтера:

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    ...
```

* `locator` (dict): Словарь с параметрами для выполнения действий.
* `message` (str, optional): Сообщение, которое необходимо отправить (если требуется).
* `typing_speed` (float, optional): Скорость набора текста при отправке сообщений.
* `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение, если произошла ошибка.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

Возвращает элементы, найденные на странице по локейтору:

```python
def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
    ...
```


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

Возвращает атрибут элемента, найденного по локейтору:

```python
def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
    ...
```


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

Вспомогательный метод для получения атрибута веб-элемента.

#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

Отправляет сообщение веб-элементу.

#### `evaluate_locator(self, attribute: str | list | dict) -> str`

Оценивает атрибут локейтера.

#### `_evaluate(self, attribute: str) -> str | None`

Вспомогательный метод для оценки отдельного атрибута.

#### `get_locator_keys() -> list`

Возвращает список доступных ключей локейтера.


## Примеры локейтеров

Примеры различных локейтеров, которые могут быть использованы для тестирования, приведены в коде.


## Обработка ошибок

Модуль использует блоки `try-except` для перехвата и логирования ошибок во время различных операций.  Определенные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекло время ожидания.


## Использование

Инициализация экземпляра `ExecuteLocator` с экземпляром WebDriver.
Вызов метода `execute_locator` со словарем локейтера для выполнения действий или получения данных с веб-элементов.

## Зависимости

Модуль использует Selenium для операций с WebDriver, включая поиск элементов, отправку нажатий клавиш и взаимодействие с веб-страницами.


## Пример использования

Пример использования класса `ExecuteLocator`  приведен в коде.  Он демонстрирует инициализацию драйвера, навигацию, поиск элементов и другие важные операции.

```python
# Пример кода (см. предоставленный код)
```
```