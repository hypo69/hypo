# Модуль executor

## Обзор

Модуль `executor` содержит класс `ExecuteLocator`, предназначенный для выполнения действий с веб-элементами на основе конфигурационных данных (локаторов) с использованием Selenium WebDriver.  Класс предоставляет методы для поиска элементов, отправки сообщений, получения атрибутов и обработки различных сценариев взаимодействия с веб-страницей.

## Оглавление

* [Общая Структура и Назначение](#общая-структура-и-назначение)
* [Импорты и Зависимости](#импорты-и-зависимости)
* [Класс ExecuteLocator](#класс-executelocator)
    * [Атрибуты](#атрибуты-класса)
    * [Методы](#методы-класса)
        * [`__init__(self, driver, *args, **kwargs)`](#init-self-driver-args-kwargs)
        * [`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`](#execute-locator-self-locator-message-typing-speed-continue-on-error)
        * [`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None)`](#get-webelement-by-locator-self-locator-message)
        * [`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None)`](#get-attribute-by-locator-self-locator-message)
        * [`_get_element_attribute(self, element: WebElement, attribute: str)`](#get-element-attribute-self-element-attribute)
        * [`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool)`](#send-message-self-locator-message-typing-speed-continue-on-error)
        * [`evaluate_locator(self, attribute: str | list | dict)`](#evaluate-locator-self-attribute)
        * [`_evaluate(self, attribute: str)`](#evaluate-self-attribute)
        * [`get_locator_keys() -> list`](#get-locator-keys-staticmethod)
* [Примеры Локаторов](#примеры-локаторов)


## Импорты и Зависимости

Этот раздел содержит список импортируемых библиотек и модулей, необходимых для работы класса `ExecuteLocator`.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src import gs
from src.utils import pprint, j_loads, j_loads_ns, j_dumps, save_png
from src.utils.string import StringFormatter
from src.logger import logger
from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
```

## Класс ExecuteLocator

### Атрибуты класса

- `driver`: Экземпляр `webdriver`, используемый для взаимодействия с браузером.
- `actions`: Экземпляр `ActionChains`, для выполнения сложных действий с элементами.
- `by_mapping`: Словарь для преобразования строковых представлений локаторов в объекты `By`.


### Методы класса

#### `__init__(self, driver, *args, **kwargs)`

Инициализирует экземпляр класса `ExecuteLocator`.

```python
def __init__(self, driver, *args, **kwargs):
    self.driver = driver
    self.actions = ActionChains(driver)
```

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

Выполняет действие, заданное локатором.

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    # ... реализация метода ...
```

**Описание**: Выполняет действие, заданное локатором `locator`, обрабатывая различные типы локаторов.

**Параметры**:
- `locator` (dict): Словарь с параметрами локатора.
- `message` (str, optional): Сообщение для отправки, если требуется.
- `typing_speed` (float, optional): Скорость набора текста при отправке сообщения.
- `continue_on_error` (bool, optional): Флаг для продолжения выполнения при ошибках.

**Возвращает**:
- `Union[str, list, dict, WebElement, bool]`: Результат выполнения действия или `bool` в случае ошибки.

**Вызывает исключения**:
- `ExecuteLocatorException`: При ошибках, связанных с выполнением действия по локатору.


(Аналогичные описания для остальных методов: `get_webelement_by_locator`, `get_attribute_by_locator`, `_get_element_attribute`, `send_message`, `evaluate_locator`, `_evaluate`, `get_locator_keys`)


## Примеры Локаторов

Примеры локаторов, используемых для взаимодействия с элементами веб-страницы.

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

```