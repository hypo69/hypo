

Файл `executor.py` модуля `src.webdriver` содержит класс `ExecuteLocator`, который предназначен для выполнения различных действий с элементами веб-страницы с использованием Selenium WebDriver. Давайте разберем основные компоненты и функции этого класса:

## Общая Структура и Назначение

### Основная Цель

Класс `ExecuteLocator` предназначен для выполнения навигационных алгоритмов и взаимодействий с веб-страницей на основе конфигурационных данных, которые предоставлены в виде словарей локаторов.

### Основные Компоненты

1. **Импорты и Зависимости**

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
   from src.utils.printer import pprint, j_loads, j_loads_ns, j_dumps, save_png
   from src.utils.string import StringFormatter
   from src.logger import logger
   from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
   ```

   Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами и внутренние модули для настроек, логирования и обработки исключений.

2. **Класс `ExecuteLocator`**

   Класс `ExecuteLocator` является основным элементом этого файла и содержит методы для выполнения действий с веб-элементами и обработки локаторов. Рассмотрим его методы и атрибуты более детально.

### Атрибуты Класса

- **`driver`**: Ссылка на экземпляр WebDriver, который используется для взаимодействия с браузером.
- **`actions`**: Экземпляр `ActionChains` для выполнения сложных действий с элементами веб-страницы.
- **`by_mapping`**: Словарь для преобразования строковых представлений локаторов в объекты Selenium `By`.

### Методы Класса

1. **`__init__(self, driver, *args, **kwargs)`**

   Конструктор класса, который инициализирует WebDriver и `ActionChains`:

   ```python
   def __init__(self, driver, *args, **kwargs):
       self.driver = driver
       self.actions = ActionChains(driver)
   ```

2. **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

   Основной метод для выполнения действий по локатору:

   ```python
   def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
       ...
   ```

   - **`locator`**: Словарь с параметрами для выполнения действий.
   - **`message`**: Сообщение для отправки, если это необходимо.
   - **`typing_speed`**: Скорость набора текста при отправке сообщений.
   - **`continue_on_error`**: Флаг для продолжения выполнения при возникновении ошибки.

   Этот метод выбирает, какой метод использовать в зависимости от конфигурации локатора.

3. **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

   Получение элемента(ов) на основе локатора:

   ```python
   def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
       ...
   ```

4. **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

   Получение атрибута элемента:

   ```python
   def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
       ...
   ```

5. **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

   Вспомогательный метод для получения атрибута элемента:

   ```python
   def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
       ...
   ```

6. **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

   Отправка сообщения элементу:

   ```python
   def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
       ...
   ```

7. **`evaluate_locator(self, attribute: str | list | dict) -> str`**

   Оценка атрибута локатора:

   ```python
   def evaluate_locator(self, attribute: str | list | dict) -> str:
       ...
   ```

8. **`_evaluate(self, attribute: str) -> str | None`**

   Вспомогательный метод для оценки одного атрибута:

   ```python
   def _evaluate(self, attribute: str) -> str | None:
       ...
   ```

9. **`get_locator_keys() -> list`**

   Возвращает список доступных ключей локатора:

   ```python
   @staticmethod
   def get_locator_keys() -> list:
       ...
   ```

### Примеры Локаторов

В файле также приводятся примеры различных локаторов, которые могут быть использованы для выполнения тестов:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false, 
    "mandatory": true,
    "event": null
  },
  ...
}
```

---
