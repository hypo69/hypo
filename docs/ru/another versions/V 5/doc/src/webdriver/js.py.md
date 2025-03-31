# Модуль `src.webdriver.js`

## Обзор

Модуль `src.webdriver.js` предоставляет JavaScript-утилиты для взаимодействия с веб-страницей через Selenium WebDriver. Он расширяет возможности WebDriver, добавляя функции для манипуляции видимостью элементов DOM, получения информации о странице и управления фокусом браузера.

## Подробней

Этот модуль предназначен для упрощения автоматизированного тестирования и взаимодействия с веб-страницами, особенно в случаях, когда требуется выполнение JavaScript-кода для достижения определенной функциональности. Модуль содержит класс `JavaScript`, который инкапсулирует методы для выполнения JavaScript-кода в контексте текущей веб-страницы.

## Классы

### `JavaScript`

**Описание**: Класс `JavaScript` предоставляет методы для выполнения JavaScript-кода в браузере, управляемом Selenium WebDriver.

**Как работает класс**:
- Класс инициализируется экземпляром `WebDriver`.
- Методы класса позволяют выполнять JavaScript-код для манипуляции DOM-элементами, получения информации о странице и управления фокусом браузера.

**Методы**:
- `__init__`: Инициализирует класс `JavaScript` с экземпляром `WebDriver`.
- `unhide_DOM_element`: Делает невидимый DOM-элемент видимым.
- `ready_state`: Возвращает статус загрузки документа.
- `window_focus`: Устанавливает фокус на окно браузера.
- `get_referrer`: Возвращает URL-адрес реферера текущего документа.
- `get_page_lang`: Возвращает язык текущей страницы.

#### `__init__`

```python
def __init__(self, driver: WebDriver):
    """Initializes the JavaScript helper with a Selenium WebDriver instance.

    Args:
        driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
    """
    self.driver = driver
```

**Описание**: Инициализирует экземпляр класса `JavaScript` с переданным экземпляром `WebDriver`.

**Как работает функция**:
- Принимает экземпляр `WebDriver` в качестве аргумента.
- Сохраняет переданный экземпляр `WebDriver` в атрибуте `self.driver` для последующего использования в других методах класса.

**Параметры**:
- `driver` (WebDriver): Экземпляр `WebDriver`, используемый для выполнения JavaScript-кода.

#### `unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Makes an invisible DOM element visible by modifying its style properties.

    Args:
        element (WebElement): The WebElement object to make visible.

    Returns:
        bool: True if the script executes successfully, False otherwise.
    """
    script = """
    arguments[0].style.opacity = 1;
    arguments[0].style.transform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.MozTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.WebkitTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.msTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.OTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].scrollIntoView(true);
    return true;
    """
    try:
        self.driver.execute_script(script, element)
        return True
    except Exception as ex:
        logger.error('Error in unhide_DOM_element: %s', ex)
        return False
```

**Описание**: Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

**Как работает функция**:
- Принимает объект `WebElement` в качестве аргумента.
- Выполняет JavaScript-код, который изменяет свойства стиля элемента, делая его видимым.
- Использует `try-except` блок для обработки возможных исключений.
- Логирует ошибку, если выполнение JavaScript-кода завершается неудачно.

**Параметры**:
- `element` (WebElement): DOM-элемент, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если выполнение скрипта прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка при выполнении JavaScript-кода.

**Примеры**:

```python
# Пример использования функции unhide_DOM_element
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")
element = driver.find_element(By.ID, "hiddenElement")
js = JavaScript(driver)
result = js.unhide_DOM_element(element)
print(result)  # Выведет True или False в зависимости от успеха
```

#### `ready_state`

```python
@property
def ready_state(self) -> str:
    """Retrieves the document loading status.

    Returns:
        str: 'loading' if the document is still loading, 'complete' if loading is finished.
    """
    try:
        return self.driver.execute_script('return document.readyState;')
    except Exception as ex:
        logger.error('Error retrieving document.readyState: %s', ex)
        return ''
```

**Описание**: Извлекает статус загрузки документа.

**Как работает функция**:
- Выполняет JavaScript-код, который возвращает значение свойства `document.readyState`.
- Использует `try-except` блок для обработки возможных исключений.
- Логирует ошибку, если не удается получить статус загрузки документа.

**Возвращает**:
- `str`: `'loading'`, если документ еще загружается, `'complete'`, если загрузка завершена. Возвращает пустую строку `''` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка при выполнении JavaScript-кода.

**Примеры**:

```python
# Пример использования функции ready_state
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
js = JavaScript(driver)
ready_state = js.ready_state
print(ready_state)  # Выведет 'loading' или 'complete' в зависимости от статуса
```

#### `window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.
    """
    try:
        self.driver.execute_script('window.focus();')
    except Exception as ex:
        logger.error('Error executing window.focus(): %s', ex)
```

**Описание**: Устанавливает фокус на окно браузера, используя JavaScript.

**Как работает функция**:
- Выполняет JavaScript-код, который устанавливает фокус на окно браузера.
- Использует `try-except` блок для обработки возможных исключений.
- Логирует ошибку, если не удается установить фокус на окно браузера.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка при выполнении JavaScript-кода.

**Примеры**:

```python
# Пример использования функции window_focus
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
js = JavaScript(driver)
js.window_focus()  # Устанавливает фокус на окно браузера
```

#### `get_referrer`

```python
def get_referrer(self) -> str:
    """Retrieves the referrer URL of the current document.

    Returns:
        str: The referrer URL, or an empty string if unavailable.
    """
    try:
        return self.driver.execute_script('return document.referrer;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.referrer: %s', ex)
        return ''
```

**Описание**: Извлекает URL-адрес реферера текущего документа.

**Как работает функция**:
- Выполняет JavaScript-код, который возвращает значение свойства `document.referrer`.
- Использует `try-except` блок для обработки возможных исключений.
- Логирует ошибку, если не удается получить URL-адрес реферера.

**Возвращает**:
- `str`: URL-адрес реферера или пустую строку, если он недоступен.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка при выполнении JavaScript-кода.

**Примеры**:

```python
# Пример использования функции get_referrer
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
js = JavaScript(driver)
referrer = js.get_referrer()
print(referrer)  # Выведет URL-адрес реферера или пустую строку
```

#### `get_page_lang`

```python
def get_page_lang(self) -> str:
    """Retrieves the language of the current page.

    Returns:
        str: The language code of the page, or an empty string if unavailable.
    """
    try:
        return self.driver.execute_script('return document.documentElement.lang;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.documentElement.lang: %s', ex)
        return ''
```

**Описание**: Извлекает язык текущей страницы.

**Как работает функция**:
- Выполняет JavaScript-код, который возвращает значение свойства `document.documentElement.lang`.
- Использует `try-except` блок для обработки возможных исключений.
- Логирует ошибку, если не удается получить язык страницы.

**Возвращает**:
- `str`: Код языка страницы или пустую строку, если он недоступен.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка при выполнении JavaScript-кода.

**Примеры**:

```python
# Пример использования функции get_page_lang
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
js = JavaScript(driver)
page_lang = js.get_page_lang()
print(page_lang)  # Выведет код языка страницы или пустую строку
```