```markdown
# Модуль src.webdriver.js

## Обзор

Модуль `src.webdriver.js` предоставляет функции на JavaScript для взаимодействия с веб-страницей, расширяя возможности Selenium WebDriver.  Он включает в себя функции для отображения невидимых элементов DOM, получения метаданных страницы (статус загрузки, referrer, язык) и управления фокусом браузера.


## Оглавление

* [Классы](#классы)
    * [JavaScript](#javascript)
* [Функции](#функции)
    * [`unhide_DOM_element`](#unhide_dom_element)
    * [`ready_state`](#ready_state)
    * [`window_focus`](#window_focus)
    * [`get_referrer`](#get_referrer)
    * [`get_page_lang`](#get_page_lang)


## Классы

### `JavaScript`

**Описание**: Класс `JavaScript` предоставляет функции для взаимодействия с веб-страницей посредством JavaScript.

**Конструктор**:

```python
def __init__(self, driver: WebDriver):
    """Initializes the JavaScript helper with a Selenium WebDriver instance.

    Args:
        driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
    """
```


**Методы**:

#### `unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Makes an invisible DOM element visible by modifying its style properties.

    Args:
        element (WebElement): The WebElement object to make visible.

    Returns:
        bool: True if the script executes successfully, False otherwise.

    Raises:
        Exception: Any exception raised during JavaScript execution.
    """
```

#### `ready_state`

```python
@property
def ready_state(self) -> str:
    """Retrieves the document loading status.

    Returns:
        str: 'loading' if the document is still loading, 'complete' if loading is finished.

    Raises:
        Exception: Any exception during script execution.
    """
```

#### `window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.

    Raises:
        Exception: Any exception during script execution.
    """
```

#### `get_referrer`

```python
def get_referrer(self) -> str:
    """Retrieves the referrer URL of the current document.

    Returns:
        str: The referrer URL, or an empty string if unavailable.

    Raises:
        Exception: Any exception during script execution.
    """
```


#### `get_page_lang`

```python
def get_page_lang(self) -> str:
    """Retrieves the language of the current page.

    Returns:
        str: The language code of the page, or an empty string if unavailable.

    Raises:
        Exception: Any exception during script execution.
    """
```

## Функции

(Нет функций, не относящихся к методам класса)


```
```
