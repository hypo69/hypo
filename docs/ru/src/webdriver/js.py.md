# Модуль для работы с JavaScript в WebDriver
## Обзор

Модуль `src.webdriver.js` предоставляет класс `JavaScript` с набором утилитных функций, предназначенных для расширения возможностей Selenium WebDriver через выполнение JavaScript-кода на веб-странице. Он включает в себя функции для управления видимостью DOM-элементов, получения метаданных страницы (таких как состояние готовности документа, URL-адрес источника перехода и язык страницы) и управления фокусом браузера.

## Подробнее

Модуль предназначен для упрощения взаимодействия с веб-страницами, особенно в тех случаях, когда стандартных средств Selenium WebDriver недостаточно. Он позволяет выполнять специфические JavaScript-команды для решения задач, таких как отображение скрытых элементов или получение информации о странице.
Этот модуль расширяет возможности Selenium WebDriver, добавляя функции на основе JavaScript для взаимодействия с веб-страницами, включая манипуляции с видимостью, получение информации о странице и управление фокусом браузера.

## Классы

### `JavaScript`

**Описание**: Класс предоставляет утилиты JavaScript для взаимодействия с веб-страницей.

**Принцип работы**:
Класс инициализируется экземпляром WebDriver и предоставляет методы для выполнения JavaScript-кода в контексте текущей веб-страницы. Это позволяет автоматизировать задачи, которые сложно выполнить стандартными средствами Selenium.

**Методы**:
- `__init__(driver: WebDriver)`: Инициализирует экземпляр класса `JavaScript` с заданным драйвером WebDriver.
- `unhide_DOM_element(element: WebElement) -> bool`: Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.
- `ready_state() -> str`: Возвращает состояние готовности документа.
- `window_focus() -> None`: Устанавливает фокус на окно браузера.
- `get_referrer() -> str`: Возвращает URL-адрес источника перехода для текущего документа.
- `get_page_lang() -> str`: Возвращает язык текущей страницы.

### `__init__`

```python
    def __init__(self, driver: WebDriver):
        """Initializes the JavaScript helper with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
        """
```

**Назначение**: Инициализирует объект `JavaScript`, привязывая его к экземпляру `WebDriver`.

**Параметры**:
- `driver` (WebDriver): Экземпляр `WebDriver`, который будет использоваться для выполнения JavaScript-кода.

**Как работает функция**:
1.  Принимает экземпляр `WebDriver`.
2.  Сохраняет ссылку на этот экземпляр в атрибуте `self.driver`, чтобы его можно было использовать для выполнения JavaScript-кода.

```
  WebDriver instance
  │
  ↓
  self.driver = driver
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
js_utils = JavaScript(driver)
```

### `unhide_DOM_element`

```python
    def unhide_DOM_element(self, element: WebElement) -> bool:
        """Makes an invisible DOM element visible by modifying its style properties.

        Args:
            element (WebElement): The WebElement object to make visible.

        Returns:
            bool: True if the script executes successfully, False otherwise.
        """
```

**Назначение**: Делает невидимый DOM-элемент видимым, изменяя его CSS-свойства.

**Параметры**:
- `element` (WebElement): DOM-элемент, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если выполнение скрипта прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при выполнении JavaScript.

**Как работает функция**:
1.  Определяет JavaScript-код, который изменяет CSS-свойства элемента, чтобы сделать его видимым.
2.  Пытается выполнить этот код с помощью `driver.execute_script`.
3.  Если выполнение прошло успешно, возвращает `True`.
4.  Если происходит ошибка, логирует её и возвращает `False`.

```
   element (WebElement)
    │
    ↓
    JavaScript code execution (CSS modification)
    │
    ↓
    Try: execute_script
    │
    ↓
    Success: return True
    │
    Exception: log error -> return False
```

**Примеры**:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
hidden_element = driver.find_element(By.ID, "hiddenElement")
success = js_utils.unhide_DOM_element(hidden_element)
print(f"Element unhidden successfully: {success}")
```

### `ready_state`

```python
    @property
    def ready_state(self) -> str:
        """Retrieves the document loading status.

        Returns:
            str: 'loading' if the document is still loading, 'complete' if loading is finished.
        """
```

**Назначение**: Возвращает текущее состояние загрузки документа.

**Возвращает**:
- `str`: `'loading'`, если документ еще загружается, `'complete'`, если загрузка завершена.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при получении состояния готовности документа.

**Как работает функция**:
1.  Выполняет JavaScript-код `return document.readyState;` для получения состояния готовности документа.
2.  Возвращает полученное состояние.
3.  В случае ошибки логирует её и возвращает пустую строку.

```
    JavaScript code execution (document.readyState)
    │
    ↓
    Try: execute_script
    │
    ↓
    Success: return document.readyState
    │
    Exception: log error -> return ''
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
ready_state = js_utils.ready_state
print(f"Document ready state: {ready_state}")
```

### `window_focus`

```python
    def window_focus(self) -> None:
        """Sets focus to the browser window using JavaScript.

        Attempts to bring the browser window to the foreground.
        """
```

**Назначение**: Устанавливает фокус на окно браузера.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при установке фокуса на окно.

**Как работает функция**:
1.  Выполняет JavaScript-код `window.focus();` для установки фокуса на окно браузера.
2.  В случае ошибки логирует её.

```
    JavaScript code execution (window.focus())
    │
    ↓
    Try: execute_script
    │
    ↓
    Success: None
    │
    Exception: log error
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
js_utils.window_focus()
```

### `get_referrer`

```python
    def get_referrer(self) -> str:
        """Retrieves the referrer URL of the current document.

        Returns:
            str: The referrer URL, or an empty string if unavailable.
        """
```

**Назначение**: Возвращает URL-адрес страницы, с которой пользователь перешел на текущую страницу.

**Возвращает**:
- `str`: URL-адрес источника перехода или пустую строку, если он недоступен.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при получении URL-адреса источника перехода.

**Как работает функция**:
1.  Выполняет JavaScript-код `return document.referrer;` для получения URL-адреса источника перехода.
2.  Возвращает полученный URL-адрес.
3.  В случае ошибки логирует её и возвращает пустую строку.

```
    JavaScript code execution (document.referrer)
    │
    ↓
    Try: execute_script
    │
    ↓
    Success: return document.referrer or ''
    │
    Exception: log error -> return ''
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
referrer = js_utils.get_referrer()
print(f"Referrer URL: {referrer}")
```

### `get_page_lang`

```python
    def get_page_lang(self) -> str:
        """Retrieves the language of the current page.

        Returns:
            str: The language code of the page, or an empty string if unavailable.
        """
```

**Назначение**: Возвращает язык текущей страницы.

**Возвращает**:
- `str`: Код языка страницы или пустую строку, если он недоступен.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при получении языка страницы.

**Как работает функция**:
1.  Выполняет JavaScript-код `return document.documentElement.lang;` для получения языка страницы.
2.  Возвращает полученный код языка.
3.  В случае ошибки логирует её и возвращает пустую строку.

```
    JavaScript code execution (document.documentElement.lang)
    │
    ↓
    Try: execute_script
    │
    ↓
    Success: return document.documentElement.lang or ''
    │
    Exception: log error -> return ''
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
page_lang = js_utils.get_page_lang()
print(f"Page language: {page_lang}")