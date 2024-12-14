# Анализ кода модуля `readme.ru.md`

**Качество кода**
7
-   Плюсы
    -   Документ содержит подробное описание функциональности модулей `Driver` и `Executor`.
    -   Приведены примеры использования основных методов и классов.
    -   Есть разделы с описанием обработки ошибок и зависимостей.
-   Минусы
    -   Документ содержит смешанный формат (текст и примеры кода), что усложняет восприятие.
    -   Некоторые части документа дублируются.
    -   Отсутствует последовательное оформление в RST формате.

**Рекомендации по улучшению**

1.  **Форматирование**: Привести весь текст к единому формату reStructuredText (RST) для корректного отображения в Sphinx или других инструментах документации.
2.  **Структура**: Улучшить структуру документа, разделив на логические блоки с использованием заголовков и подзаголовков.
3.  **Устранение дублирования**: Избежать дублирования информации, особенно в описаниях классов и примерах кода.
4.  **Консистентность примеров**: Привести примеры кода к единому стилю и убедиться в их работоспособности.
5. **Использовать docstring**:  Добавить  docstring к модулям, классам, методам и переменным в формает RST.

**Оптимизированный код**

```markdown
# Анализ модуля src.webdriver

## Обзор модуля

Модуль предоставляет фреймворк для управления веб-драйвером, позволяя автоматизировать навигацию и взаимодействие с веб-страницами. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий над веб-элементами.

## Основные функции

-   **Обработка локаторов**
    -   **Инициализация**: Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора**: Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Извлечение элементов**: Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может возвращать один элемент, список элементов или `False`, если ни один не найден.
    -   **Извлечение атрибутов**: Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
    -   **Отправка сообщений**: Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию набора текста с настраиваемой скоростью набора и необязательным взаимодействием с мышью.
-   **Скриншоты**
    -   **Скриншот элемента**: Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
-   **Действие клика**
    -   **Клик по элементу**: Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удался.
-   **Оценка локатора**
    -   **Оценка атрибута**: Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

## Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекает время ожидания.

## Использование

### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

### Выполнение локатора

Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или извлечения данных из веб-элементов.

### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot` для взаимодействия с веб-элементами и обработки результатов.

## Зависимости

Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Примеры использования

### Примеры для `Driver` и `Chrome`

```python
# -*- coding: utf-8 -*-

"""
Примеры использования классов `Driver` и `Chrome`.
=========================================================================================

Этот модуль демонстрирует основные методы для навигации и взаимодействия с веб-страницами с помощью классов `Driver` и `Chrome`.

Пример использования
--------------------

Пример использования классов `Driver` и `Chrome`:

.. code-block:: python

    from src.webdriver.driver import Driver, Chrome
    from selenium.webdriver.common.by import By

    def main():
        # Пример 1: Создание экземпляра Chrome и навигация по URL
        chrome_driver = Driver(Chrome)
        if chrome_driver.get_url("https://www.example.com"):
            print("Успешно перешли по URL")

        # Пример 2: Извлечение домена из URL
        domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
        print(f"Извлеченный домен: {domain}")

        # Пример 3: Сохранение cookies в локальный файл
        success = chrome_driver._save_cookies_localy()
        if success:
            print("Cookies успешно сохранены")

        # Пример 4: Обновление текущей страницы
        if chrome_driver.page_refresh():
            print("Страница успешно обновлена")

        # Пример 5: Прокрутка страницы вниз
        if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
            print("Страница успешно прокручена вниз")

        # Пример 6: Получение языка текущей страницы
        page_language = chrome_driver.locale
        print(f"Язык страницы: {page_language}")

        # Пример 7: Установка кастомного user-agent
        user_agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
        if custom_chrome_driver.get_url("https://www.example.com"):
            print("Успешно перешли по URL с кастомным user-agent")

        # Пример 8: Поиск элемента по CSS-селектору
        element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
            print(f"Найден элемент с текстом: {element.text}")

        # Пример 9: Получение текущего URL
        current_url = chrome_driver.current_url
        print(f"Текущий URL: {current_url}")

        # Пример 10: Фокусировка окна
        chrome_driver.window_focus()
        print("Окно сфокусировано")

    if __name__ == "__main__":
        main()
"""
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    """
    Главная функция для демонстрации примеров использования классов `Driver` и `Chrome`.
    """
    # Пример 1: Создание экземпляра Chrome и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Успешно перешли по URL")

    # Пример 2: Извлечение домена из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Извлеченный домен: {domain}")

    # Пример 3: Сохранение cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies успешно сохранены")

    # Пример 4: Обновление текущей страницы
    if chrome_driver.page_refresh():
        print("Страница успешно обновлена")

    # Пример 5: Прокрутка страницы вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Страница успешно прокручена вниз")

    # Пример 6: Получение языка текущей страницы
    page_language = chrome_driver.locale
    print(f"Язык страницы: {page_language}")

    # Пример 7: Установка кастомного user-agent
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Успешно перешли по URL с кастомным user-agent")

    # Пример 8: Поиск элемента по CSS-селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Найден элемент с текстом: {element.text}")

    # Пример 9: Получение текущего URL
    current_url = chrome_driver.current_url
    print(f"Текущий URL: {current_url}")

    # Пример 10: Фокусировка окна
    chrome_driver.window_focus()
    print("Окно сфокусировано")

if __name__ == "__main__":
    main()
```

### Обзор модуля `Driver`

```rst
Модуль `Driver`
===============

Описание
--------
Модуль `Driver` предоставляет динамическую реализацию WebDriver, которая интегрирует общие функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач веб-автоматизации.

Основные функции
----------------

-   Наследует от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительные функции.
-   Включает методы для прокрутки, обработки cookie, взаимодействия с веб-элементами и выполнения JavaScript.
-   Предоставляет утилиты для управления окнами браузера и взаимодействиями со страницей.

Компоненты
----------

1.  **Класс `DriverBase`**

    -   **Атрибуты**:
        -   `previous_url`: Хранит предыдущий URL.
        -   `referrer`: Хранит URL-адрес источника перехода.
        -   `page_lang`: Хранит язык страницы.
        -   Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.

    -   **Методы**:
        -   `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
        -   `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
        -   `get_url`: Загружает указанный URL.
        -   `extract_domain`: Извлекает домен из URL.
        -   `_save_cookies_localy`: Сохраняет cookie в локальный файл.
        -   `page_refresh`: Обновляет текущую страницу.
        -   `window_focus`: Фокусирует окно браузера с помощью JavaScript.
        -   `wait`: Ожидает в течение указанного интервала времени.

2.  **Класс `DriverMeta`**

    -   **Методы**:
        -   `__call__`: Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональные возможности выполнения локаторов.

3.  **Класс `Driver`**

    -   **Описание**:
        -   Динамически созданный класс WebDriver, который наследует как от `DriverBase`, так и от указанного класса WebDriver.
    -   **Пример использования**:

        .. code-block:: python

            from src.webdriver.driver import Driver, Chrome, Firefox, Edge
            d = Driver(Chrome)

Использование
-------------

-   **Инициализация**: Создайте экземпляр `Driver` с конкретным классом WebDriver.
-   **Функциональность**: Используйте такие методы, как `scroll`, `get_url`, `extract_domain` и `page_refresh`, для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления cookie.

Зависимости
-----------

-   **Selenium**: Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
-   **Python Libraries**: Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функций.

```

### Описание класса `ExecuteLocator`

```rst
Класс `ExecuteLocator`
=====================

Описание
--------

Класс `ExecuteLocator` предназначен для выполнения различных действий над элементами веб-страницы с использованием Selenium WebDriver.

Основные компоненты
-------------------

1.  **Импорты и зависимости**

    .. code-block:: python

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

    Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, а также внутренние модули для настроек, логирования и обработки исключений.

2.  **Класс `ExecuteLocator`**

    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов.

    ### Атрибуты класса

    -   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
    -   `actions`: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
    -   `by_mapping`: Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

    ### Методы класса

    1.  **`__init__(self, driver, *args, **kwargs)`**

        Конструктор класса инициализирует WebDriver и `ActionChains`:

        .. code-block:: python

           def __init__(self, driver, *args, **kwargs):
               self.driver = driver
               self.actions = ActionChains(driver)

    2.  **`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`**

        Основной метод для выполнения действий на основе локатора:

        .. code-block:: python

           def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
               ...

        -   `locator`: Словарь с параметрами для выполнения действий.
        -   `message`: Сообщение для отправки, если необходимо.
        -   `typing_speed`: Скорость набора текста при отправке сообщений.
        -   `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение в случае ошибки.

        Этот метод выбирает, какие действия выполнять, на основе конфигурации локатора.

    3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

        Извлекает элементы, найденные на странице на основе локатора:

        .. code-block:: python

           def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
               ...

    4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

        Извлекает атрибут из элемента на основе локатора:

        .. code-block:: python

           def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
               ...

    5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

        Вспомогательный метод для получения атрибута из веб-элемента:

        .. code-block:: python

           def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
               ...

    6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

        Отправляет сообщение в веб-элемент:

        .. code-block:: python

           def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
               ...

    7.  **`evaluate_locator(self, attribute: str | list | dict) -> str`**

        Оценивает атрибут локатора:

        .. code-block:: python

           def evaluate_locator(self, attribute: str | list | dict) -> str:
               ...

    8.  **`_evaluate(self, attribute: str) -> str | None`**

        Вспомогательный метод для оценки отдельного атрибута:

        .. code-block:: python

           def _evaluate(self, attribute: str) -> str | None:
               ...

    9.  **`get_locator_keys() -> list`**

        Возвращает список доступных ключей локатора:

        .. code-block:: python

           @staticmethod
           def get_locator_keys() -> list:
               ...

### Примеры локаторов

Файл также содержит примеры различных локаторов, которые можно использовать для тестирования:

.. code-block:: json

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
    },
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
}

```

## WebDriver Executor

### Обзор

Модуль WebDriver Executor предоставляет фреймворк для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматизированных действий над веб-элементами.

### Основные функции

-   **Обработка локаторов**
    -   **Инициализация**: Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора**: Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как найти и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Извлечение элементов**: Метод `get_webelement_by_locator` извлекает веб-элементы на основе информации о локаторе, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может возвращать один элемент, список элементов или `False`, если ни один не найден.
    -   **Извлечение атрибутов**: Метод `get_attribute_by_locator` извлекает атрибуты из элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
    -   **Отправка сообщений**: Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию набора текста с настраиваемой скоростью набора и необязательным взаимодействием с мышью.
-   **Скриншоты**
    -   **Скриншот элемента**: Метод `get_webelement_as_screenshot` делает скриншот веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват скриншотов нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
-   **Действие клика**
    -   **Клик по элементу**: Метод `click` выполняет действие клика по веб-элементу, идентифицированному локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открытию нового окна, и регистрирует ошибки, если клик не удался.
-   **Оценка локатора**
    -   **Оценка атрибута**: Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

### Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание скриншотов. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекает время ожидания.

### Использование

#### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

#### Выполнение локатора

Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или извлечения данных из веб-элементов.

#### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot` для взаимодействия с веб-элементами и обработки результатов.

### Зависимости

Модуль полагается на Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

### Примеры использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Main function to demonstrate usage examples for Driver and Chrome

    # Example 1: Create a Chrome driver instance and navigate to a URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Example 2: Extract the domain from a URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
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
    if custom_chrome_driver.get_url("https://www.example.com"):
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