# Модуль `src.webdriver.js`

## Обзор

Модуль `src.webdriver.js` предоставляет набор JavaScript-утилитных функций для взаимодействия с веб-страницей с использованием Selenium WebDriver. Он расширяет возможности Selenium WebDriver, добавляя общие JavaScript-функции для манипулирования видимостью элементов DOM, получения информации о странице и управления фокусом браузера.

## Подробней

Этот модуль предназначен для упрощения автоматизации задач, связанных с веб-страницами, где требуется динамическое взаимодействие с элементами DOM через JavaScript. Он позволяет выполнять такие действия, как изменение видимости элементов, получение информации о состоянии документа и управление фокусом окна браузера. Модуль предназначен для работы в окружении Selenium WebDriver и требует наличия экземпляра WebDriver для выполнения JavaScript-кода.

## Классы

### `JavaScript`

**Описание**: Предоставляет JavaScript-утилитные функции для взаимодействия с веб-страницей.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `JavaScript` с использованием экземпляра Selenium WebDriver.
- `unhide_DOM_element`: Делает невидимый элемент DOM видимым, изменяя его свойства стиля.
- `ready_state`: Возвращает статус загрузки документа.
- `window_focus`: Устанавливает фокус на окно браузера.
- `get_referrer`: Возвращает URL-адрес источника текущего документа.
- `get_page_lang`: Возвращает язык текущей страницы.

#### `__init__`

```python
def __init__(self, driver: WebDriver):
    """Initializes the JavaScript helper with a Selenium WebDriver instance.

    Args:
        driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
    """
    ...
```

**Описание**: Инициализирует класс `JavaScript` с экземпляром `WebDriver`.

**Параметры**:
- `driver` (WebDriver): Экземпляр `WebDriver` для выполнения JavaScript.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
js_utils = JavaScript(driver)
```

#### `unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Makes an invisible DOM element visible by modifying its style properties.

    Args:
        element (WebElement): The WebElement object to make visible.

    Returns:
        bool: True if the script executes successfully, False otherwise.
    """
    ...
```

**Описание**: Делает невидимый элемент DOM видимым, изменяя его свойства стиля.

**Параметры**:
- `element` (WebElement): Элемент `WebElement`, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

**Примеры**:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
element = driver.find_element(By.ID, "some_element")
if not element.is_displayed():
    js_utils.unhide_DOM_element(element)
```

#### `ready_state`

```python
@property
def ready_state(self) -> str:
    """Retrieves the document loading status.

    Returns:
        str: 'loading' if the document is still loading, 'complete' if loading is finished.
    """
    ...
```

**Описание**: Возвращает статус загрузки документа.

**Возвращает**:
- `str`: `'loading'`, если документ еще загружается, `'complete'`, если загрузка завершена.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
print(js_utils.ready_state)
```

#### `window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.
    """
    ...
```

**Описание**: Устанавливает фокус на окно браузера.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
js_utils.window_focus()
```

#### `get_referrer`

```python
def get_referrer(self) -> str:
    """Retrieves the referrer URL of the current document.

    Returns:
        str: The referrer URL, or an empty string if unavailable.
    """
    ...
```

**Описание**: Возвращает URL-адрес источника текущего документа.

**Возвращает**:
- `str`: URL-адрес источника или пустая строка, если он недоступен.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
print(js_utils.get_referrer())
```

#### `get_page_lang`

```python
def get_page_lang(self) -> str:
    """Retrieves the language of the current page.

    Returns:
        str: The language code of the page, or an empty string if unavailable.
    """
    ...
```

**Описание**: Возвращает язык текущей страницы.

**Возвращает**:
- `str`: Код языка страницы или пустая строка, если он недоступен.

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)
print(js_utils.get_page_lang())
```