# Анализ кода модуля `readme.ru.md`

**Качество кода**

-   **Соответствие требованиям**: 8/10
    -   **Плюсы**:
        -   Хорошее описание функциональности модуля.
        -   Приведены примеры использования.
        -   Детальное описание классов и методов.
        -   Логическая структура документации.
    -   **Минусы**:
        -   Не все примеры кода следуют стандарту с одинарными кавычками.
        -   Некоторые блоки кода не имеют комментариев.
        -   Встречается избыточное описание.

**Рекомендации по улучшению**

1.  **Привести примеры кода к единому стандарту**: Необходимо использовать одинарные кавычки в коде Python, как указано в инструкции.
2.  **Добавить комментарии к коду**: Код в примерах должен быть прокомментирован, чтобы объяснить его работу.
3.  **Уточнить описание**: Некоторые части описания можно сделать более конкретными.
4.  **Улучшить структуру**: Разделить большие текстовые блоки на более мелкие, добавив подзаголовки.
5.  **Добавить RST docstring**: Добавить документацию в формате RST для всех функций, методов и классов в коде.
6.  **Использовать `logger.error`**: Заменить стандартные `try-except` блоки на использование `logger.error` для обработки ошибок.
7.  **Добавить описание для модуля**: В начале файла должно быть описание модуля в формате RST docstring.
8.  **Улучшить форматирование примеров**: Добавить подсветку синтаксиса для примеров кода.

**Оптимизированный код**

```markdown
[Русский](https://github.com/hypo69/hypo/blob/master/README.RU.MD)
### Обзор модуля: Исполнитель через WebDriver

**Описание:**
Модуль предоставляет фреймворк для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматических действий над веб-элементами.

**Основные возможности:**
- Выполнение алгоритмов навигации, указанных в файлах скриптов.
- Выполнение алгоритмов взаимодействия со страницей, указанных в файлах локаторов.

**Функциональность:**

1.  **Обработка локаторов:**
    -   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и ключевых слов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Получение элемента:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    -   **Получение атрибута:** Метод `get_attribute_by_locator` получает атрибуты элементов, найденных с помощью локатора. Он поддерживает как отдельные, так и множественные элементы.
    -   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью ввода и необязательным взаимодействием с мышью.

2.  **Скриншоты:**
    -   **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

3.  **Действие клика:**
    -   **Клик по элементу:** Метод `click` выполняет действие клика на веб-элементе, идентифицированном локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открывает новое окно, и регистрирует ошибки, если клик не удался.

4.  **Оценка локатора:**
    -   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены как заполнители (например, `%EXTERNAL_MESSAGE%`).

**Обработка ошибок:**
- Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или время ожидания истекло.

**Использование:**
- **Инициализация:** Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.
- **Выполнение локатора:** Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или получения данных из веб-элементов.
- **Обработка результатов:** Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

**Зависимости:**
- Модуль использует Selenium для операций WebDriver, включая поиск элементов, отправку ключей и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

---

Feel free to adjust any specifics or add more details based on the actual implementation and requirements.
```python
# -*- coding: utf-8 -*-

"""
Модуль для демонстрации использования классов `Driver` и `Chrome`
=================================================================

Этот модуль содержит примеры использования классов `Driver` и `Chrome` из модуля `src.webdriver.driver`.
Примеры демонстрируют создание экземпляров драйвера, навигацию по URL, извлечение домена, работу с cookies,
обновление страницы, прокрутку, получение языка страницы, установку пользовательского агента и поиск элементов.

Пример использования:
---------------------

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome
    
    def main():
        # Код, демонстрирующий использование классов Driver и Chrome
        ...

"""
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By
# from src.logger import logger # TODO remove unuse import

def main():
    """
    Основная функция для демонстрации примеров использования классов Driver и Chrome.
    
    
    """
    # Пример 1: Создание экземпляра Chrome драйвера и навигация по URL
    # Код создает экземпляр класса `Driver` с `Chrome` в качестве аргумента и выполняет навигацию на заданный URL.
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL")

    # Пример 2: Извлечение домена из URL
    # Код извлекает домен из заданного URL.
    domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
    print(f"Extracted domain: {domain}")

    # Пример 3: Сохранение cookies в локальный файл
    # Код сохраняет cookies текущего сеанса в локальный файл.
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Пример 4: Обновление текущей страницы
    # Код обновляет текущую страницу.
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Пример 5: Прокрутка страницы вниз
    # Код прокручивает страницу вниз на заданное количество раз с заданной высотой кадра и задержкой.
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Пример 6: Получение языка текущей страницы
    # Код получает язык текущей страницы.
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Пример 7: Установка пользовательского агента для Chrome драйвера
    # Код создает экземпляр класса `Driver` с пользовательским агентом и выполняет навигацию на заданный URL.
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL with custom user agent")

    # Пример 8: Поиск элемента по CSS селектору
    # Код находит элемент на странице по CSS селектору и выводит его текст.
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Пример 9: Получение текущего URL
    # Код получает текущий URL страницы.
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Пример 10: Фокусировка окна для удаления фокуса с элемента
    # Код фокусирует окно браузера.
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

### Обзор модуля: `Driver`

**Описание:**
Модуль `Driver` предоставляет динамическую реализацию WebDriver, которая объединяет общие функциональные возможности WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookies. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-приложений.

**Основные возможности:**
- Наследует от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
- Включает методы для прокрутки, обработки cookies, взаимодействия с веб-элементами и выполнения JavaScript.
- Предоставляет утилиты для управления окнами браузера и взаимодействия со страницей.

**Компоненты:**

1.  **Класс `DriverBase`:**
    -   **Атрибуты:**
        -   `previous_url`: Сохраняет предыдущий URL.
        -   `referrer`: Сохраняет URL-адрес перехода.
        -   `page_lang`: Сохраняет язык страницы.
        -   Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.

    -   **Методы:**
        -   `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
        -   `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
        -   `get_url`: Загружает указанный URL.
        -   `extract_domain`: Извлекает домен из URL.
        -   `_save_cookies_localy`: Сохраняет cookies в локальный файл.
        -   `page_refresh`: Обновляет текущую страницу.
        -   `window_focus`: Фокусирует окно браузера с помощью JavaScript.
        -   `wait`: Ожидает указанный интервал.

2.  **Класс `DriverMeta`:**
    -   **Методы:**
        -   `__call__`: Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональность выполнения локаторов.

3.  **Класс `Driver`:**
    -   **Описание:**
        -   Динамически созданный класс WebDriver, который наследует от `DriverBase` и указанного класса WebDriver.
    -   **Пример использования:**
        ```python
        from src.webdriver.driver import Driver, Chrome, Firefox, Edge
        d = Driver(Chrome)
        ```

**Использование:**
- **Инициализация:** Создайте экземпляр `Driver` с конкретным классом WebDriver.
- **Функциональность:** Используйте методы, такие как `scroll`, `get_url`, `extract_domain` и `page_refresh`, для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления cookies.

**Зависимости:**
- **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
- **Python Libraries:** Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функциональных возможностей.

---

Feel free to customize or expand this overview based on any additional specifics or details about your module's functionality.
### Примеры использования классов и методов

-   **Создание экземпляра Chrome драйвера и навигация по URL:**

    ```python
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL")
    ```

-   **Извлечение домена из URL:**

    ```python
    domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
    print(f"Extracted domain: {domain}")
    ```

-   **Сохранение cookies в локальный файл:**

    ```python
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")
    ```

-   **Обновление текущей страницы:**

    ```python
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")
    ```

-   **Прокрутка страницы вниз:**

    ```python
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")
    ```

-   **Получение языка текущей страницы:**

    ```python
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")
    ```

-   **Установка кастомного User-Agent для Chrome драйвера:**

    ```python
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL with custom user agent")
    ```

-   **Поиск элемента по CSS селектору:**

    ```python
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")
    ```

-   **Получение текущего URL:**

    ```python
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")
    ```

-   **Фокусировка окна, чтобы убрать фокус с элемента:**

    ```python
    chrome_driver.window_focus()
    print("Focused the window")
    ```

### Примечания

-   Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent`, и `src` модули, указанные в импортах.
-   Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

The `executor.py` file in the `src.webdriver` module contains the `ExecuteLocator` class, which is designed for performing various actions on web page elements using Selenium WebDriver. Let’s break down the main components and functions of this class:

## Общая структура и назначение

### Основная цель

Класс `ExecuteLocator` предназначен для выполнения алгоритмов навигации и взаимодействия с веб-страницей на основе данных конфигурации, предоставленных в виде словарей локаторов.

### Основные компоненты

1.  **Импорты и зависимости**

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
    
    from src.logger.logger import logger
    from src.logger.exceptions import DefaultSettingsException, WebDriverException, ExecuteLocatorException
    ```

    Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, и внутренние модули для настроек, логирования и обработки исключений.

2.  **Класс `ExecuteLocator`**

    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов. Давайте подробнее рассмотрим его методы и атрибуты.

### Атрибуты класса

-   **`driver`**: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
-   **`actions`**: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
-   **`by_mapping`**: Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

### Методы класса

1.  **`__init__(self, driver, *args, **kwargs)`**

    Конструктор класса инициализирует WebDriver и `ActionChains`:

    ```python
    def __init__(self, driver, *args, **kwargs):
        self.driver = driver
        self.actions = ActionChains(driver)
    ```

2.  **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

    Основной метод для выполнения действий на основе локатора:

    ```python
    def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
        ...
    ```

    -   **`locator`**: Словарь с параметрами для выполнения действий.
    -   **`message`**: Сообщение для отправки, если необходимо.
    -   **`typing_speed`**: Скорость ввода для отправки сообщений.
    -   **`continue_on_error`**: Флаг, указывающий, следует ли продолжать выполнение в случае ошибки.

    Этот метод выбирает, какие действия следует выполнить на основе конфигурации локатора.

3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

    Возвращает элементы, найденные на странице, на основе локатора:

    ```python
    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
        ...
    ```

4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

    Возвращает атрибут элемента на основе локатора:

    ```python
    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
        ...
    ```

5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

    Вспомогательный метод для получения атрибута из веб-элемента:

    ```python
    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
        ...
    ```

6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

    Отправляет сообщение в веб-элемент:

    ```python
    def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
        ...
    ```

7.  **`evaluate_locator(self, attribute: str | list | dict) -> str`**

    Оценивает атрибут локатора:

    ```python
    def evaluate_locator(self, attribute: str | list | dict) -> str:
        ...
    ```

8.  **`_evaluate(self, attribute: str) -> str | None`**

    Вспомогательный метод для оценки одного атрибута:

    ```python
    def _evaluate(self, attribute: str) -> str | None:
        ...
    ```

9.  **`get_locator_keys() -> list`**

    Возвращает список доступных ключей локатора:

    ```python
    @staticmethod
    def get_locator_keys() -> list:
        ...
    ```

### Примеры локаторов

Файл также включает примеры различных локаторов, которые можно использовать для тестирования:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false,
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },
  ...
}
```

### Примеры локаторов
<pre>
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
    "selector 2": "//span[@data-component-type='s-product-image']//a",
    "if_list":"first","use_mouse": false,
    "mandatory": true,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": null
  },

  "pagination": {
    "ul": {
      "attribute": null,
      "by": "xpath",
      "selector": "//ul[@class='pagination']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
    },
    "->": {
      "attribute": null,
      "by": "xpath",
      "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
      "if_list":"first","use_mouse": false
    }
  }

}
"description": {
  "attribute": [
    null,
    null
  ],
  "by": [
    "xpath",
    "xpath"
  ],
  "selector": [
    "//a[contains(@href, '#tab-description')]",
    "//div[@id = 'tab-description']//p"
  ],
  "timeout":0,"timeout_for_event":"presence_of_element_located","event": [
    "click()",
    null
  ],
  "if_list":"first","use_mouse": [
    false,
    false
  ],
  "mandatory": [
    true,
    true
  ],
  "locator_description": [
    "Clicking on the tab to open the description field",
    "Reading data from div"
  ]
}
</pre>

1. KEY.NULL: Представляет нулевой ключ.
2. KEY.CANCEL: Представляет ключ отмены.
3. KEY.HELP: Представляет ключ помощи.
4. KEY.BACKSPACE: Представляет ключ backspace.
5. KEY.TAB: Представляет ключ tab.
6. KEY.CLEAR: Представляет ключ clear.
7. KEY.RETURN: Представляет ключ return.
8. KEY.ENTER: Представляет ключ enter.
9. KEY.SHIFT: Представляет ключ shift.
10. KEY.CONTROL: Представляет ключ control.
11. KEY.ALT: Представляет ключ alt.
12. KEY.PAUSE: Представляет ключ pause.
13. KEY.ESCAPE: Представляет ключ escape.
14. KEY.SPACE: Представляет ключ space.
15. KEY.PAGE_UP: Представляет ключ page up.
16. KEY.PAGE_DOWN: Представляет ключ page down.
17. KEY.END: Представляет ключ end.
18. KEY.HOME: Представляет ключ home.
19. KEY.LEFT: Представляет ключ стрелка влево.
20. KEY.UP: Представляет ключ стрелка вверх.
21. KEY.RIGHT: Представляет ключ стрелка вправо.
22. KEY.DOWN: Представляет ключ стрелка вниз.
23. KEY.INSERT: Представляет ключ insert.
24. KEY.DELETE: Представляет ключ delete.
25. KEY.SEMICOLON: Представляет ключ semicolon.
26. KEY.EQUALS: Представляет ключ equals.
27. KEY.NUMPAD0 through KEY.NUMPAD9: Представляют цифровые клавиши от 0 до 9 на цифровой клавиатуре.
28. KEY.MULTIPLY: Представляет ключ multiply.
29. KEY.ADD: Представляет ключ add.
30. KEY.SEPARATOR: Представляет ключ separator.
31. KEY.SUBTRACT: Представляет ключ subtract.
32. KEY.DECIMAL: Представляет ключ decimal.
33. KEY.DIVIDE: Представляет ключ divide.
34. KEY.F1 through KEY.F12: Представляют функциональные клавиши от F1 до F12.
35. KEY.META: Представляет ключ meta.
---
# WebDriver Executor

## Обзор

Модуль WebDriver Executor предоставляет фреймворк для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий над веб-элементами.

## Основные возможности

- **Обработка локаторов**
  - **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и ключевых слов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
  - **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
  - **Получение элемента:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
  - **Получение атрибута:** Метод `get_attribute_by_locator` получает атрибуты элементов, найденных с помощью локатора. Он поддерживает как отдельные, так и множественные элементы.
  - **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью ввода и необязательным взаимодействием с мышью.

- **Скриншоты**
  - **Скриншот элемента:** Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

- **Действие клика**
  - **Клик по элементу:** Метод `click` выполняет действие клика на веб-элементе, идентифицированном локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открывает новое окно, и регистрирует ошибки, если клик не удался.

- **Оценка локатора**
  - **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены как заполнители (например, `%EXTERNAL_MESSAGE%`).

## Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или время ожидания истекло.

## Использование

### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

### Выполнение локатора

Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или получения данных из веб-элементов.

### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

## Зависимости

Модуль использует Selenium для операций WebDriver, включая поиск элементов, отправку ключей и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Пример использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Main function to demonstrate usage examples for Driver and Chrome

    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain('https://www.example.com/path/to/page')
    print(f"Extracted domain: {domain}")

    # Example 3: Save cookies to a local file
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Example 4: Refresh the current page
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Example 5: Scroll the page down
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Example 6: Get the language of the current page
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Example 7: Set a custom user agent for the Chrome driver
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url('https://www.example.com'):
        print("Successfully navigated to the URL with custom user agent")

    # Example 8: Find an element by its CSS selector
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Example 9: Get the current URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Example 10: Focus the window to remove focus from the element
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```
[Объяснение Driver](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение Executor](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.ru.md)
[Объяснение локатора](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.ru.md)
```