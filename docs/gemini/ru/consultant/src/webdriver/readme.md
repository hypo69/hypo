# Анализ кода модуля `readme.md`

**Качество кода**
    **7/10**
  -  Плюсы
        - Документ содержит подробное описание функциональности модулей `driver`, `executor` и `locator`.
        - Приведены примеры использования основных методов и классов, что облегчает понимание.
        - Описаны основные концепции и структуры данных (например, структура локаторов).
  -  Минусы
    -  Форматирование markdown не всегда последовательное (например, в примерах кода).
    -  Некоторые части документации можно было бы сделать более структурированными (например, описание методов класса `ExecuteLocator`).
    -  Некоторые описания повторяются, что может запутать читателя.
    -  Отсутствует явное разделение на части "Описание модуля", "Использование", "Примеры", "Зависимости" и т.д.

**Рекомендации по улучшению**

1.  **Форматирование**:
    -   Использовать единообразное форматирование для примеров кода, включая отступы и использование ` ` для выделения кода.
    -   Структурировать описания классов и их методов с помощью заголовков и списков.
2.  **Содержание**:
    -   Устранить дублирование описаний, переформулировав и объединив похожие части.
    -   Добавить больше конкретики в описаниях, например, указать, какие именно ошибки может выдавать каждый метод.
    -   Разделить документацию на логические блоки: "Описание модуля", "Использование", "Примеры", "Зависимости", "Обработка ошибок".
3.  **Примеры**:
    -   Добавить примеры использования `ExecuteLocator`, чтобы показать, как он работает с реальными локаторами.
    -   Расширить примеры использования `Driver` и `Chrome` классов, добавив больше вариантов действий с элементами.
4.  **Структура**
    -   Использовать заголовки разных уровней для разделения документации на разделы и подразделы.
    -   Добавить оглавление в начале документа для удобства навигации.
5. **Документация**
    - Привести примеры  структуры RST документации для класса `ExecuteLocator`, функций  и методов.

**Оптимизированный код**

```markdown
# Анализ кода модуля `readme.md`

## Обзор модуля: Исполнитель через WebDriver

**Описание:**
Модуль предоставляет среду выполнения для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматических действий над веб-элементами.

**Основные возможности:**

- Выполняет алгоритмы навигации, заданные в файлах скриптов.
- Выполняет алгоритмы взаимодействия со страницей, заданные в файлах локаторов.

**Функциональность:**

### 1. Обработка локаторов

-   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
-   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
-   **Получение элемента:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации локатора, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
-   **Получение атрибута:** Метод `get_attribute_by_locator` получает атрибуты элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
-   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью печати и дополнительным взаимодействием с мышью.

### 2. Скриншоты

-   **Снимок экрана элемента:** Метод `get_webelement_as_screenshot` делает снимок экрана веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват снимков экрана нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.

### 3. Действие клика

-   **Клик элемента:** Метод `click` выполняет действие клика на веб-элементе, определенном локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открывает новое окно, и регистрирует ошибки в случае сбоя клика.

### 4. Оценка локатора

-   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

**Обработка ошибок:**

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание снимков экрана. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекает время ожидания.

**Использование:**

-   **Инициализация:** Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.
-   **Выполнение локатора:** Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или получения данных из веб-элементов.
-   **Обработка результатов:** Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

**Зависимости:**

Модуль зависит от Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

---

[Русский](https://github.com/hypo69/hypo/blob/master/README.RU.MD)

### Обзор модуля: `Driver`

**Описание:**

Модуль `Driver` предоставляет динамическую реализацию WebDriver, которая объединяет общие функции WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач автоматизации веб-приложений.

**Основные возможности:**

-   Наследуется от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительные функции.
-   Включает методы для прокрутки, обработки cookie, взаимодействия с веб-элементами и выполнения JavaScript.
-   Предоставляет утилиты для управления окнами браузера и взаимодействием со страницей.

**Компоненты:**

#### 1. Класс `DriverBase`

-   **Атрибуты:**
    -   `previous_url`: Хранит предыдущий URL.
    -   `referrer`: Хранит URL-адрес реферера.
    -   `page_lang`: Хранит язык страницы.
    -   Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.
-   **Методы:**
    -   `scroll`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
    -   `locale`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
    -   `get_url`: Загружает указанный URL-адрес.
    -   `extract_domain`: Извлекает домен из URL-адреса.
    -   `_save_cookies_localy`: Сохраняет cookie в локальный файл.
    -   `page_refresh`: Обновляет текущую страницу.
    -   `window_focus`: Фокусирует окно браузера с помощью JavaScript.
    -   `wait`: Ожидает указанный интервал.

#### 2. Класс `DriverMeta`

-   **Методы:**
    -   `__call__`: Создает новый класс `Driver`, который объединяет указанный класс WebDriver (например, Chrome, Firefox, Edge) с `DriverBase`. Инициализирует методы JavaScript и функциональные возможности выполнения локаторов.

#### 3. Класс `Driver`

-   **Описание:**
    -   Динамически созданный класс WebDriver, который наследуется как от `DriverBase`, так и от указанного класса WebDriver.
-   **Пример использования:**
    -   ```python
        from src.webdriver.driver import Driver, Chrome, Firefox, Edge
        d = Driver(Chrome)
        ```

**Использование:**

-   **Инициализация:** Создайте экземпляр `Driver` с определенным классом WebDriver.
-   **Функциональность:** Используйте такие методы, как `scroll`, `get_url`, `extract_domain` и `page_refresh`, для взаимодействия с веб-страницами. Класс также предоставляет методы для выполнения JavaScript и управления cookie.

**Зависимости:**

-   **Selenium:** Используется для операций WebDriver, включая поиск элементов, прокрутку и взаимодействие с веб-страницами.
-   **Библиотеки Python:** Включает `sys`, `pickle`, `time`, `copy`, `pathlib`, `urllib.parse` и другие для различных функций.

---

### Примеры использования классов и методов

-   **Создание экземпляра Chrome драйвера и навигация по URL:**

    ```python
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")
    ```

-   **Извлечение домена из URL:**

    ```python
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
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
    if custom_chrome_driver.get_url("https://www.example.com"):
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

-   Убедитесь, что у вас установлены все зависимости, например `selenium`, `fake_useragent` и `src` модули, указанные в импортах.
-   Путь к файлу настроек и другим ресурсам должен быть настроен в `gs` (global settings).

Этот файл примеров демонстрирует, как использовать различные методы и функции из `driver.py` и `chrome.py`. Вы можете запускать эти примеры для тестирования работы вашего драйвера и других утилит.

### Модуль `executor.py`: `ExecuteLocator`

Файл `executor.py` в модуле `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий над элементами веб-страницы с помощью Selenium WebDriver.

#### Общая структура и назначение

##### Основное назначение

Класс `ExecuteLocator` предназначен для выполнения алгоритмов навигации и взаимодействия с веб-страницей на основе данных конфигурации, предоставляемых в виде словарей локаторов.

##### Основные компоненты

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

    Здесь импортируются необходимые библиотеки и модули, включая Selenium WebDriver для взаимодействия с веб-страницами, а также внутренние модули для настроек, логирования и обработки исключений.

2.  **Класс `ExecuteLocator`**

    Класс `ExecuteLocator` является основным компонентом этого файла и содержит методы для выполнения действий над веб-элементами и обработки локаторов.

##### Атрибуты класса

-   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
-   `actions`: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
-   `by_mapping`: Словарь, который сопоставляет строковые представления локаторов с объектами Selenium `By`.

##### Методы класса

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

    -   `locator`: Словарь с параметрами для выполнения действий.
    -   `message`: Сообщение для отправки, если необходимо.
    -   `typing_speed`: Скорость ввода для отправки сообщений.
    -   `continue_on_error`: Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.

    Метод выбирает, какие действия выполнять, на основе конфигурации локатора.

3.  **`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`**

    Получает элементы, найденные на странице на основе локатора:

    ```python
    def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
        ...
    ```

4.  **`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`**

    Получает атрибут элемента на основе локатора:

    ```python
    def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
       ...
    ```

5.  **`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`**

    Вспомогательный метод для получения атрибута веб-элемента:

    ```python
    def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
       ...
    ```

6.  **`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`**

    Отправляет сообщение веб-элементу:

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

В файле также приведены примеры различных локаторов, которые можно использовать для тестирования:

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

,"description": {
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

#### Ключи Selenium

1.  KEY.NULL: Представляет нулевой ключ.
2.  KEY.CANCEL: Представляет ключ отмены.
3.  KEY.HELP: Представляет ключ справки.
4.  KEY.BACKSPACE: Представляет клавишу backspace.
5.  KEY.TAB: Представляет клавишу tab.
6.  KEY.CLEAR: Представляет клавишу clear.
7.  KEY.RETURN: Представляет клавишу return.
8.  KEY.ENTER: Представляет клавишу enter.
9.  KEY.SHIFT: Представляет клавишу shift.
10. KEY.CONTROL: Представляет клавишу control.
11. KEY.ALT: Представляет клавишу alt.
12. KEY.PAUSE: Представляет клавишу паузы.
13. KEY.ESCAPE: Представляет клавишу escape.
14. KEY.SPACE: Представляет клавишу пробел.
15. KEY.PAGE_UP: Представляет клавишу page up.
16. KEY.PAGE_DOWN: Представляет клавишу page down.
17. KEY.END: Представляет клавишу end.
18. KEY.HOME: Представляет клавишу home.
19. KEY.LEFT: Представляет клавишу со стрелкой влево.
20. KEY.UP: Представляет клавишу со стрелкой вверх.
21. KEY.RIGHT: Представляет клавишу со стрелкой вправо.
22. KEY.DOWN: Представляет клавишу со стрелкой вниз.
23. KEY.INSERT: Представляет клавишу insert.
24. KEY.DELETE: Представляет клавишу delete.
25. KEY.SEMICOLON: Представляет клавишу semicolon.
26. KEY.EQUALS: Представляет клавишу equals.
27. KEY.NUMPAD0 через KEY.NUMPAD9: Представляют клавиши цифровой клавиатуры от 0 до 9.
28. KEY.MULTIPLY: Представляет клавишу умножения.
29. KEY.ADD: Представляет клавишу сложения.
30. KEY.SEPARATOR: Представляет клавишу разделителя.
31. KEY.SUBTRACT: Представляет клавишу вычитания.
32. KEY.DECIMAL: Представляет клавишу decimal.
33. KEY.DIVIDE: Представляет клавишу деления.
34. KEY.F1 через KEY.F12: Представляют функциональные клавиши от F1 до F12.
35. KEY.META: Представляет клавишу meta.

---

# WebDriver Executor

## Обзор

Модуль WebDriver Executor предоставляет среду выполнения для навигации и взаимодействия с веб-страницами с использованием WebDriver. Он обрабатывает скрипты и локаторы для выполнения автоматических действий над веб-элементами.

## Основные возможности

-   **Обработка локаторов**
    -   **Инициализация:** Класс `ExecuteLocator` инициализируется экземпляром WebDriver и необязательным списком аргументов и именованных аргументов. Он настраивает WebDriver и цепочки действий для взаимодействия с веб-элементами.
    -   **Выполнение локатора:** Метод `execute_locator` обрабатывает словарь локаторов, который содержит информацию о том, как находить и взаимодействовать с веб-элементами. Он обрабатывает различные типы локаторов и действий на основе предоставленной конфигурации.
    -   **Получение элемента:** Метод `get_webelement_by_locator` получает веб-элементы на основе информации локатора, такой как XPATH, ID или CSS-селекторы. Он ожидает появления элементов и может вернуть один элемент, список элементов или `False`, если ничего не найдено.
    -   **Получение атрибута:** Метод `get_attribute_by_locator` получает атрибуты элементов, найденных с помощью локатора. Он поддерживает как одиночные, так и множественные элементы.
    -   **Отправка сообщения:** Метод `send_message` отправляет текстовый ввод в веб-элементы. Он поддерживает имитацию ввода с настраиваемой скоростью печати и дополнительным взаимодействием с мышью.
-   **Скриншоты**
    -   **Снимок экрана элемента:** Метод `get_webelement_as_screenshot` делает снимок экрана веб-элемента и возвращает его в виде изображения PNG. Он поддерживает захват снимков экрана нескольких элементов и обрабатывает ошибки, если элементы больше не присутствуют в DOM.
-   **Действие клика**
    -   **Клик элемента:** Метод `click` выполняет действие клика на веб-элементе, определенном локатором. Он обрабатывает случаи, когда клик приводит к переходу на новую страницу или открывает новое окно, и регистрирует ошибки в случае сбоя клика.
-   **Оценка локатора**
    -   **Оценка атрибута:** Метод `evaluate_locator` оценивает атрибуты локатора, включая обработку особых случаев, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

## Обработка ошибок

Модуль использует блоки try-except для перехвата и регистрации ошибок во время различных операций, таких как поиск элементов, отправка сообщений и создание снимков экрана. Конкретные исключения, такие как `NoSuchElementException` и `TimeoutException`, перехватываются для обработки случаев, когда элементы не найдены или истекает время ожидания.

## Использование

### Инициализация

Создайте экземпляр `ExecuteLocator` с экземпляром WebDriver.

### Выполнение локатора

Вызовите метод `execute_locator` со словарем локаторов для выполнения действий или получения данных из веб-элементов.

### Обработка результатов

Используйте методы, такие как `get_webelement_by_locator`, `send_message` и `get_webelement_as_screenshot`, для взаимодействия с веб-элементами и обработки результатов.

## Зависимости

Модуль зависит от Selenium для операций WebDriver, включая поиск элементов, отправку клавиш и взаимодействие с веб-страницами. Он также использует встроенные библиотеки Python для обработки исключений и управления временем.

## Пример использования

```python
from src.webdriver.driver import Driver, Chrome
from selenium.webdriver.common.by import By

def main():
    # Основная функция для демонстрации примеров использования Driver и Chrome

    # Пример 1: Создание экземпляра Chrome драйвера и навигация по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL")

    # Пример 2: Извлечение домена из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Extracted domain: {domain}")

    # Пример 3: Сохранение cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies were saved successfully")

    # Пример 4: Обновление текущей страницы
    if chrome_driver.page_refresh():
        print("Page was refreshed successfully")

    # Пример 5: Прокрутка страницы вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Successfully scrolled the page down")

    # Пример 6: Получение языка текущей страницы
    page_language = chrome_driver.locale
    print(f"Page language: {page_language}")

    # Пример 7: Установка кастомного User-Agent для Chrome драйвера
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Successfully navigated to the URL with custom user agent")

    # Пример 8: Поиск элемента по CSS селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Found element with text: {element.text}")

    # Пример 9: Получение текущего URL
    current_url = chrome_driver.current_url
    print(f"Current URL: {current_url}")

    # Пример 10: Фокусировка окна, чтобы убрать фокус с элемента
    chrome_driver.window_focus()
    print("Focused the window")

if __name__ == "__main__":
    main()
```

[Driver explanation](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Executor explanation](https://github.com/hypo69/hypo/tree/master/src/webdriver/executor.md)
[Locator explanation](https://github.com/hypo69/hypo/tree/master/src/webdriver/locator.md)
```