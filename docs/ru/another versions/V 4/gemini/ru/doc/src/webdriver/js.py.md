# Модуль `js`

## Обзор

Модуль `js` предоставляет JavaScript утилиты для взаимодействия с веб-страницей через Selenium WebDriver. Он расширяет возможности Selenium, добавляя JavaScript-функции для управления видимостью элементов, получения информации о странице и управления фокусом браузера.

## Подробней

Этот модуль предназначен для расширения возможностей Selenium WebDriver путем добавления общих функций на основе JavaScript для взаимодействия с веб-страницами, включая манипуляции с видимостью, получение информации о странице и управление фокусом браузера.

Ключевые особенности:
    1. Обеспечение видимости невидимых элементов DOM для взаимодействия.
    2. Получение метаданных, таких как состояние готовности документа, реферер или язык страницы.
    3. Программное управление фокусом окна браузера.

## Классы

### `JavaScript`

**Описание**: Предоставляет JavaScript утилиты для взаимодействия с веб-страницей.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `JavaScript`.
- `unhide_DOM_element`: Делает невидимый DOM-элемент видимым.
- `ready_state`: Возвращает статус загрузки документа.
- `window_focus`: Устанавливает фокус на окно браузера.
- `get_referrer`: Возвращает URL реферера текущего документа.
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

**Описание**: Инициализирует класс `JavaScript` с экземпляром `WebDriver` из Selenium.

**Параметры**:
- `driver` (WebDriver): Экземпляр `WebDriver` Selenium для выполнения JavaScript.

**Примеры**
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()  # или другой браузер
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

**Описание**: Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

**Параметры**:
- `element` (WebElement): DOM-элемент, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

**Примеры**:
```python
from selenium.webdriver.common.by import By
element = driver.find_element(By.ID, 'hiddenElement')
result = js_utils.unhide_DOM_element(element)
print(f"Element unhidden: {result}")
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
ready = js_utils.ready_state
print(f"Ready state: {ready}")
```

#### `window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.
    """
    ...
```

**Описание**: Устанавливает фокус на окно браузера, переводя его на передний план.

**Примеры**:
```python
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

**Описание**: Возвращает URL реферера текущего документа.

**Возвращает**:
- `str`: URL реферера или пустая строка, если он недоступен.

**Примеры**:
```python
referrer = js_utils.get_referrer()
print(f"Referrer URL: {referrer}")
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
page_lang = js_utils.get_page_lang()
print(f"Page language: {page_lang}")
```