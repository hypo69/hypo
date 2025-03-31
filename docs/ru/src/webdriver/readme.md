# Документация модуля `webdriver`

## Обзор

Этот модуль содержит классы для управления веб-браузером с использованием WebDriver. Он предоставляет инструменты для автоматизации взаимодействия с веб-страницами, включая навигацию, ввод данных, выполнение JavaScript и управление cookies.

## Содержание

- [Классы](#классы)
  - [Driver](#driver)
  - [Chrome](#chrome)
- [Функции](#функции)
  - [main](#main)

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет динамическую реализацию WebDriver, объединяющую общие функциональности WebDriver с дополнительными методами для взаимодействия с веб-страницами, обработки JavaScript и управления файлами cookie. Он использует возможности Selenium WebDriver и пользовательские расширения для поддержки различных задач веб-автоматизации.

**Как работает класс**:
- Класс `Driver` наследуется от указанного класса WebDriver (например, Chrome, Firefox, Edge) и добавляет дополнительную функциональность.
- Включает методы для прокрутки, обработки файлов cookie, взаимодействия с веб-элементами и выполнения JavaScript.
- Предоставляет утилиты для управления окнами браузера и взаимодействием со страницей.

#### Атрибуты класса:

- `previous_url`: Сохраняет предыдущий URL.
- `referrer`: Сохраняет URL реферера.
- `page_lang`: Сохраняет язык страницы.
- Различные атрибуты, связанные с взаимодействием с веб-элементами и выполнением JavaScript.

#### Методы класса:

- `scroll(scrolls: int, direction: str = 'forward', frame_size: int = 1000, delay: int = 1) -> bool`: Прокручивает веб-страницу в указанном направлении. Поддерживает прокрутку вперед, назад или в обоих направлениях.
- `locale() -> str | None`: Пытается определить язык страницы, проверяя метатеги или используя JavaScript.
- `get_url(url: str) -> bool`: Загружает указанный URL.
- `extract_domain(url: str) -> str`: Извлекает домен из URL.
- `_save_cookies_localy() -> bool`: Сохраняет файлы cookie в локальный файл.
- `page_refresh() -> bool`: Обновляет текущую страницу.
- `window_focus() -> None`: Фокусирует окно браузера с использованием JavaScript.
- `wait(interval: int) -> None`: Ожидает указанный интервал.

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome, Firefox, Edge
d = Driver(Chrome)
```

---

### `Chrome`

**Описание**:
Класс `Chrome` является частью модуля `webdriver` и предназначен для создания экземпляров драйвера Chrome с определенными параметрами. Он предоставляет удобный способ настройки и запуска браузера Chrome для автоматизированного тестирования или сбора данных.

**Как работает класс**:
- Класс `Chrome` является подклассом `DriverBase` и используется для инициализации драйвера Chrome с заданными опциями.
- Он позволяет настраивать различные параметры Chrome, такие как user-agent, аргументы командной строки и другие параметры.
- После инициализации драйвер Chrome готов к использованию для управления браузером и взаимодействия с веб-страницами.

#### Методы:

- `__init__(self, *args, **kwargs)`: Инициализирует новый экземпляр драйвера Chrome.

#### Параметры:

- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы, которые могут включать:
    - `user_agent` (str, optional): User-agent для установки. По умолчанию `None`.
    - Другие параметры, поддерживаемые драйвером Chrome.

**Пример**:

```python
from src.webdriver.driver import Driver, Chrome
driver = Driver(Chrome, user_agent={'user-agent': 'Custom User Agent'})
```

## Функции

### `main`

```python
def main():
    """
    Основная функция для демонстрации примеров использования классов Driver и Chrome.

    Функция создает экземпляры драйвера Chrome, выполняет различные действия на веб-страницах,
    такие как навигация по URL, извлечение домена, сохранение cookies, обновление страницы,
    прокрутка страницы, получение языка страницы, установка пользовательского user-agent,
    поиск элемента по CSS-селектору и фокусировка окна.

    Example:
        Чтобы запустить функцию main, выполните этот скрипт.
    """
    # Пример 1: Создать экземпляр драйвера Chrome и перейти по URL
    chrome_driver = Driver(Chrome)
    if chrome_driver.get_url("https://www.example.com"):
        print("Успешно перешли по URL")

    # Пример 2: Извлечь домен из URL
    domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
    print(f"Извлеченный домен: {domain}")

    # Пример 3: Сохранить cookies в локальный файл
    success = chrome_driver._save_cookies_localy()
    if success:
        print("Cookies были успешно сохранены")

    # Пример 4: Обновить текущую страницу
    if chrome_driver.page_refresh():
        print("Страница была успешно обновлена")

    # Пример 5: Прокрутить страницу вниз
    if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
        print("Страница была успешно прокручена вниз")

    # Пример 6: Получить язык текущей страницы
    page_language = chrome_driver.locale
    print(f"Язык страницы: {page_language}")

    # Пример 7: Установить пользовательский user agent для драйвера Chrome
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
    if custom_chrome_driver.get_url("https://www.example.com"):
        print("Успешно перешли по URL с пользовательским user agent")

    # Пример 8: Найти элемент по его CSS-селектору
    element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
    if element:
        print(f"Найден элемент с текстом: {element.text}")

    # Пример 9: Получить текущий URL
    current_url = chrome_driver.current_url
    print(f"Текущий URL: {current_url}")

    # Пример 10: Сфокусировать окно, чтобы убрать фокус с элемента
    chrome_driver.window_focus()
    print("Окно сфокусировано")
```

**Назначение**:
Функция `main` демонстрирует примеры использования классов `Driver` и `Chrome`. Она создает экземпляры драйвера Chrome, выполняет различные действия на веб-страницах, такие как навигация по URL, извлечение домена, сохранение cookies, обновление страницы, прокрутка страницы, получение языка страницы, установка пользовательского user-agent, поиск элемента по CSS-селектору и фокусировка окна.

**Как работает функция**:
1. Создается экземпляр драйвера Chrome с использованием класса `Driver` и `Chrome`.
2. Выполняются различные действия на веб-странице с использованием методов класса `Driver`, такие как `get_url`, `extract_domain`, `_save_cookies_localy`, `page_refresh`, `scroll`, `locale`, `find_element` и `window_focus`.
3. Результаты выполнения действий выводятся в консоль.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:

```python
if __name__ == "__main__":
    main()
```
---
```markdown
# Документация модуля `executor.py`

## Обзор

Файл `executor.py` в модуле `src.webdriver` содержит класс `ExecuteLocator`, предназначенный для выполнения различных действий над элементами веб-страницы с использованием Selenium WebDriver.

## Содержание

- [Класс `ExecuteLocator`](#класс-executelocator)
    - [Описание](#описание)
    - [Атрибуты класса](#атрибуты-класса)
    - [Методы класса](#методы-класса)
        - [`__init__`](#__init__)
        - [`execute_locator`](#execute_locator)
        - [`get_webelement_by_locator`](#get_webelement_by_locator)
        - [`get_attribute_by_locator`](#get_attribute_by_locator)
        - [`_get_element_attribute`](#_get_element_attribute)
        - [`send_message`](#send_message)
        - [`evaluate_locator`](#evaluate_locator)
        - [`_evaluate`](#_evaluate)
        - [`get_locator_keys`](#get_locator_keys)
- [Примеры локаторов](#примеры-локаторов)

## Класс `ExecuteLocator`

### Описание

Класс `ExecuteLocator` предназначен для выполнения алгоритмов навигации и взаимодействия с веб-страницей на основе данных конфигурации, представленных в виде словарей локаторов.

### Атрибуты класса

-   `driver`: Ссылка на экземпляр WebDriver, используемый для взаимодействия с браузером.
-   `actions`: Экземпляр `ActionChains` для выполнения сложных действий над элементами веб-страницы.
-   `by_mapping`: Словарь, который сопоставляет строковые представления локаторов с объектами `By` Selenium.

### Методы класса

#### `__init__(self, driver, *args, **kwargs)`

```python
def __init__(self, driver, *args, **kwargs):
    self.driver = driver
    self.actions = ActionChains(driver)
```

**Описание**:
Конструктор класса инициализирует WebDriver и `ActionChains`.

**Как работает метод**:
1.  Принимает экземпляр WebDriver в качестве аргумента.
2.  Инициализирует атрибут `driver` переданным экземпляром WebDriver.
3.  Создает экземпляр `ActionChains` с использованием WebDriver и присваивает его атрибуту `actions`.

**Параметры**:

-   `driver`: Экземпляр WebDriver для управления браузером.
-   `*args`: Произвольные позиционные аргументы.
-   `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
-   None

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

driver = webdriver.Chrome()
executor = ExecuteLocator(driver)
```

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> str | list | dict | WebElement | bool`

```python
def execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]:
    ...
```

**Описание**:
Основной метод для выполнения действий на основе локатора.

**Как работает метод**:
Метод `execute_locator` выполняет действия на веб-странице на основе предоставленного словаря `locator`. Он определяет, какое действие следует выполнить, на основе конфигурации локатора и вызывает соответствующие методы для выполнения этих действий.

Основные этапы работы метода:

1. **Проверка наличия локатора**:
   - Проверяет, предоставлен ли локатор. Если локатор отсутствует, метод возвращает `False` и регистрирует ошибку.

2. **Извлечение параметров локатора**:
   - Извлекает различные параметры из словаря локатора, такие как тип локатора (`by`), селектор (`selector`), атрибут (`attribute`), событие (`event`) и другие.

3. **Выполнение действий на основе локатора**:
   - В зависимости от конфигурации локатора, метод выполняет различные действия:
     - **Получение веб-элемента**:
       - Если указан селектор, метод пытается получить веб-элемент с использованием `get_webelement_by_locator`.
       - Если элемент не найден и указано, что он обязателен (`mandatory`), метод регистрирует ошибку и, если `continue_on_error` имеет значение `False`, вызывает исключение `ExecuteLocatorException`.
     - **Отправка сообщения**:
       - Если указано сообщение (`message`), метод отправляет сообщение в веб-элемент с использованием `send_message`.
     - **Получение атрибута**:
       - Если указан атрибут, метод получает значение атрибута веб-элемента с использованием `get_attribute_by_locator`.
     - **Выполнение события**:
       - Если указано событие (`event`), метод выполняет JavaScript-событие на веб-элементе.
     - **Клик на элемент**:
       - Если указано событие `click()`, метод выполняет клик на веб-элемент.

4. **Обработка результатов**:
   - Метод возвращает результат выполненного действия, например, веб-элемент, значение атрибута или `True`/`False` в зависимости от успеха операции.

**Параметры**:

-   `locator` (dict): Словарь с параметрами для выполнения действий.
-   `message` (str, optional): Сообщение для отправки, если необходимо. По умолчанию `None`.
-   `typing_speed` (float, optional): Скорость ввода сообщения. По умолчанию `0`.
-   `continue_on_error` (bool, optional): Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки. По умолчанию `True`.

**Возвращает**:

-   str | list | dict | WebElement | bool: Результат выполненного действия, например, веб-элемент, значение атрибута или `True`/`False` в зависимости от успеха операции.

**Вызывает исключения**:

-   `ExecuteLocatorException`: Если не удается выполнить действие и `continue_on_error` имеет значение `False`.

**Пример**:

```python
locator = {
    "by": "id",
    "selector": "myElement",
    "attribute": "value"
}
result = executor.execute_locator(locator)
```

#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

```python
def get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool:
    ...
```

**Описание**:
Извлекает элементы, найденные на странице, на основе локатора.

**Как работает метод**:
Метод `get_webelement_by_locator` извлекает веб-элементы из текущей веб-страницы на основе предоставленного словаря `locator`. Он использует различные стратегии поиска элементов, такие как XPath, CSS-селекторы, ID и другие, чтобы найти один или несколько элементов, соответствующих критериям локатора.

Основные этапы работы метода:

1. **Проверка наличия локатора**:
   - Проверяет, предоставлен ли локатор. Если локатор отсутствует, метод возвращает `False` и регистрирует ошибку.

2. **Извлечение параметров локатора**:
   - Извлекает тип локатора (`by`) и селектор (`selector`) из словаря локатора.
   - Определяет, следует ли возвращать один элемент или список элементов на основе параметра `if_list` (если указан).

3. **Поиск элементов**:
   - Использует `WebDriverWait` для ожидания появления элемента на странице в течение заданного времени ожидания (`timeout`).
   - В зависимости от типа локатора (`by`), метод использует соответствующий метод поиска элементов (`find_element` или `find_elements`) из WebDriver.
   - Если указано несколько селекторов (например, `selector` и `selector 2`), метод пытается найти элемент с использованием каждого селектора по очереди.

4. **Обработка результатов**:
   - Если найден один элемент, метод возвращает его.
   - Если найдено несколько элементов и `if_list` имеет значение `first`, метод возвращает первый элемент из списка.
   - Если найдено несколько элементов и `if_list` не указан, метод возвращает список элементов.
   - Если элементы не найдены, метод возвращает `False`.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с параметрами локатора.
-   `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:

-   WebElement | List[WebElement] | bool: Веб-элемент, список веб-элементов или `False`, если элемент не найден.

**Вызывает исключения**:

-   `WebDriverException`: Если не удается найти элемент в течение заданного времени ожидания.

**Пример**:

```python
locator = {
    "by": "id",
    "selector": "myElement"
}
element = executor.get_webelement_by_locator(locator)
```

#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

```python
def get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool:
    ...
```

**Описание**:
Извлекает атрибут из элемента на основе локатора.

**Как работает метод**:
Метод `get_attribute_by_locator` извлекает значение атрибута из веб-элемента на основе предоставленного словаря `locator`. Он сначала находит веб-элемент с использованием `get_webelement_by_locator`, а затем извлекает значение указанного атрибута из этого элемента.

Основные этапы работы метода:

1. **Получение веб-элемента**:
   - Использует `get_webelement_by_locator` для поиска веб-элемента на странице на основе предоставленного локатора.
   - Если элемент не найден, метод возвращает `False`.

2. **Извлечение атрибута**:
   - Извлекает имя атрибута (`attribute`) из словаря локатора.
   - Если указан атрибут, метод использует метод `_get_element_attribute` для получения значения атрибута из веб-элемента.
   - Если атрибут не указан, метод возвращает весь веб-элемент.

3. **Обработка результатов**:
   - Если атрибут успешно извлечен, метод возвращает его значение.
   - Если атрибут не найден или элемент не найден, метод возвращает `False`.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с параметрами локатора.
-   `message` (str, optional): Сообщение для логирования. По умолчанию `None`.

**Возвращает**:

-   str | list | dict | bool: Значение атрибута, список значений атрибутов или `False`, если элемент или атрибут не найден.

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
locator = {
    "by": "id",
    "selector": "myElement",
    "attribute": "value"
}
attribute_value = executor.get_attribute_by_locator(locator)
```

#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

```python
def _get_element_attribute(self, element: WebElement, attribute: str) -> str | None:
    ...
```

**Описание**:
Вспомогательный метод для получения атрибута из веб-элемента.

**Как работает метод**:
Метод `_get_element_attribute` является вспомогательным методом, который извлекает значение указанного атрибута из предоставленного веб-элемента.

Основные этапы работы метода:

1. **Извлечение атрибута**:
   - Использует метод `get_attribute` веб-элемента для получения значения атрибута.
   - Если атрибут не найден, метод возвращает `None`.

2. **Обработка результатов**:
   - Если атрибут успешно извлечен, метод возвращает его значение.
   - Если атрибут не найден, метод возвращает `None`.

**Параметры**:

-   `element` (WebElement): Веб-элемент, из которого нужно извлечь атрибут.
-   `attribute` (str): Имя атрибута, который нужно извлечь.

**Возвращает**:

-   str | None: Значение атрибута или `None`, если атрибут не найден.

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator

driver = webdriver.Chrome()
driver.get("https://www.example.com")
element = driver.find_element("id", "myElement")
executor = ExecuteLocator(driver)
attribute_value = executor._get_element_attribute(element, "value")
```

#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

```python
def send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool:
    ...
```

**Описание**:
Отправляет сообщение в веб-элемент.

**Как работает метод**:
Метод `send_message` отправляет указанное сообщение в веб-элемент, найденный на странице на основе предоставленного словаря `locator`. Он поддерживает симуляцию ввода текста с заданной скоростью печати и обработку ошибок.

Основные этапы работы метода:

1. **Получение веб-элемента**:
   - Использует `get_webelement_by_locator` для поиска веб-элемента на странице на основе предоставленного локатора.
   - Если элемент не найден, метод регистрирует ошибку и возвращает `False`.

2. **Очистка элемента**:
   - Очищает содержимое веб-элемента с помощью метода `clear`.

3. **Отправка сообщения**:
   - Если указана скорость печати (`typing_speed` больше `0`), метод отправляет сообщение посимвольно с задержкой между символами.
   - Если скорость печати не указана, метод отправляет сообщение целиком с помощью метода `send_keys`.

4. **Обработка ошибок**:
   - Если во время отправки сообщения возникает исключение, метод регистрирует ошибку и, если `continue_on_error` имеет значение `False`, вызывает исключение `ExecuteLocatorException`.

**Параметры**:

-   `locator` (dict | SimpleNamespace): Словарь или объект `SimpleNamespace` с параметрами локатора.
-   `message` (str): Сообщение для отправки.
-   `typing_speed` (float): Скорость печати (задержка в секундах между символами).
-   `continue_on_error` (bool): Флаг, указывающий, следует ли продолжать выполнение при возникновении ошибки.

**Возвращает**:

-   bool: `True`, если сообщение успешно отправлено, `False` в противном случае.

**Вызывает исключения**:

-   `ExecuteLocatorException`: Если не удается отправить сообщение и `continue_on_error` имеет значение `False`.

**Пример**:

```python
locator = {
    "by": "id",
    "selector": "myElement"
}
message = "Hello, world!"
success = executor.send_message(locator, message, 0.1, True)
```

#### `evaluate_locator(self, attribute: str | list | dict) -> str`

```python
def evaluate_locator(self, attribute: str | list | dict) -> str:
    ...
```

**Описание**:
Оценивает атрибут локатора.

**Как работает метод**:
Метод `evaluate_locator` оценивает значение атрибута локатора, обрабатывая специальные случаи, когда атрибуты представлены в виде заполнителей (например, `%EXTERNAL_MESSAGE%`).

Основные этапы работы метода:

1. **Проверка типа атрибута**:
   - Проверяет тип атрибута:
     - Если атрибут является строкой, метод вызывает `_evaluate` для оценки значения атрибута.
     - Если атрибут является списком или словарем, метод рекурсивно вызывает `evaluate_locator` для каждого элемента списка или значения словаря.

2. **Оценка атрибута**:
   - Если атрибут является строкой, метод `_evaluate` заменяет заполнители в строке фактическими значениями.

**Параметры**:

-   `attribute` (str | list | dict): Атрибут для оценки.

**Возвращает**:

-   str: Оцененное значение атрибута.

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
attribute = "%EXTERNAL_MESSAGE%"
evaluated_attribute = executor.evaluate_locator(attribute)
```

#### `_evaluate(self, attribute: str) -> str | None`

```python
def _evaluate(self, attribute: str) -> str | None:
    ...
```

**Описание**:
Вспомогательный метод для оценки одного атрибута.

**Как работает метод**:
Метод `_evaluate` является вспомогательным методом, который оценивает значение одного атрибута, заменяя заполнители в строке фактическими значениями.

Основные этапы работы метода:

1. **Проверка наличия атрибута**:
   - Проверяет, является ли атрибут строкой. Если атрибут не является строкой, метод возвращает `None`.

2. **Замена заполнителей**:
   - Заменяет заполнители в строке фактическими значениями. В текущей реализации заполнители не заменяются.

**Параметры**:

-   `attribute` (str): Атрибут для оценки.

**Возвращает**:

-   str | None: Оцененное значение атрибута или `None`, если атрибут не является строкой.

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
attribute = "%EXTERNAL_MESSAGE%"
evaluated_attribute = executor._evaluate(attribute)
```

#### `get_locator_keys() -> list`

```python
@staticmethod
def get_locator_keys() -> list:
    ...
```

**Описание**:
Возвращает список доступных ключей локатора.

**Как работает метод**:
Метод `get_locator_keys` является статическим методом, который возвращает список доступных ключей локатора.

Основные этапы работы метода:

1. **Возврат списка ключей**:
   - Возвращает список ключей, которые могут быть использованы в словаре локатора.

**Параметры**:
-   Отсутствуют

**Возвращает**:

-   list: Список доступных ключей локатора.

**Вызывает исключения**:
-   Отсутствуют

**Пример**:

```python
locator_keys = ExecuteLocator.get_locator_keys()
```

## Примеры локаторов

Файл содержит примеры различных локаторов, которые могут быть использованы для тестирования:

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

## Описание ключей

1. KEY.NULL: Представляет нулевой ключ.
2. KEY.CANCEL: Представляет ключ отмены.
3. KEY.HELP: Представляет ключ справки.
4. KEY.BACKSPACE: Представляет клавишу backspace.
5. KEY.TAB: Представляет клавишу tab.
6. KEY.CLEAR: Представляет ключ clear.
7. KEY.RETURN: Представляет ключ возврата.
8. KEY.ENTER: Представляет клавишу enter.
9. KEY.SHIFT: Представляет клавишу shift.
10. KEY.CONTROL: Представляет клавишу control.
11. KEY.ALT: Представляет клавишу alt.
12. KEY.PAUSE: Представляет клавишу паузы.
13. KEY.ESCAPE: Представляет клавишу escape.
14. KEY.SPACE: Представляет клавишу space.
15. KEY.PAGE_UP: Представляет клавишу page up.
16. KEY.PAGE_DOWN: Представляет клавишу page down.
17. KEY.END: Представляет клавишу end.
18. KEY.HOME: Представляет клавишу home.
19. KEY.LEFT: Представляет клавишу стрелки влево.
20. KEY.UP: Представляет клавишу стрелки вверх.
21. KEY.RIGHT: Представляет клавишу стрелки вправо.
22. KEY.DOWN: Представляет клавишу стрелки вниз.
23. KEY.INSERT: Представляет клавишу insert.
24. KEY.DELETE: Представляет клавишу delete.
25. KEY.SEMICOLON: Представляет клавишу semicolon.
26. KEY.EQUALS: Представляет клавишу equals.
27. KEY.NUMPAD0 through KEY.NUMPAD9: Представляет клавиши numpad от 0 до 9.
28. KEY.MULTIPLY: Представляет клавишу multiply.
29. KEY.ADD: Представляет клавишу add.
30. KEY.SEPARATOR: Представляет клавишу separator.
31. KEY.SUBTRACT: Представляет клавишу subtract.
32. KEY.DECIMAL: Представляет клавишу decimal.
33. KEY.DIVIDE: Представляет клавишу divide.
34. KEY.F1 through KEY.F12: Представляет функциональные клавиши от F1 до F12.
35. KEY.META: Представляет мета-клавишу.