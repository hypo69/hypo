# Модуль `js`

## Обзор

Модуль `js` предоставляет утилиты JavaScript для взаимодействия с веб-страницей.

Этот модуль предназначен для расширения возможностей Selenium WebDriver путем добавления общих JavaScript-функций для взаимодействия с веб-страницами, включая манипуляции с видимостью, получение информации о странице и управление фокусом браузера.

Основные возможности:
1. Сделать невидимые элементы DOM видимыми для взаимодействия.
2. Получение метаданных, таких как состояние готовности документа, referrer или язык страницы.
3. Программное управление фокусом окна браузера.

## Подробнее

Модуль содержит класс `JavaScript`, который предоставляет методы для выполнения JavaScript-кода в контексте веб-страницы, управляемой Selenium WebDriver. Это позволяет автоматизировать действия, которые сложно или невозможно выполнить с использованием стандартных методов Selenium.

## Содержание

- [Классы](#Классы)
  - [JavaScript](#JavaScript)
    - [Описание](#Описание)
    - [Методы](#Методы)
      - [`__init__`](#__init__)
      - [`unhide_DOM_element`](#unhide_dom_element)
      - [`ready_state`](#ready_state)
      - [`window_focus`](#window_focus)
      - [`get_referrer`](#get_referrer)
      - [`get_page_lang`](#get_page_lang)

## Классы

### `JavaScript`

**Описание**: Предоставляет утилиты JavaScript для взаимодействия с веб-страницей.

**Как работает класс**: Класс инициализируется экземпляром `WebDriver` и предоставляет методы для выполнения JavaScript-кода в контексте текущей веб-страницы. Это позволяет выполнять задачи, такие как изменение стилей элементов, получение информации о странице и управление фокусом окна браузера.

**Методы**:

- [`__init__`](#__init__)
- [`unhide_DOM_element`](#unhide_dom_element)
- [`ready_state`](#ready_state)
- [`window_focus`](#window_focus)
- [`get_referrer`](#get_referrer)
- [`get_page_lang`](#get_page_lang)

#### `__init__`

```python
def __init__(self, driver: WebDriver):
    """Инициализирует JavaScript helper с экземпляром Selenium WebDriver.

    Args:
        driver (WebDriver): Экземпляр Selenium WebDriver для выполнения JavaScript.
    """
    self.driver = driver
```

**Назначение**: Инициализация экземпляра класса `JavaScript` с использованием переданного экземпляра `WebDriver`.

**Как работает метод**: Метод сохраняет переданный экземпляр `WebDriver` в атрибуте `driver` класса `JavaScript`. Это позволяет использовать `driver` для выполнения JavaScript-кода в других методах класса.

**Параметры**:
- `driver` (WebDriver): Экземпляр Selenium WebDriver, который будет использоваться для выполнения JavaScript-кода.

**Возвращает**:
- `None`

#### `unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Делает невидимый элемент DOM видимым, изменяя его свойства стиля.

    Args:
        element (WebElement): Объект WebElement, который нужно сделать видимым.

    Returns:
        bool: True, если скрипт выполнен успешно, False в противном случае.
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

**Назначение**: Метод изменяет CSS-стили элемента DOM, чтобы сделать его видимым.

**Как работает метод**: Метод выполняет JavaScript-код, который устанавливает свойства `opacity` и `transform` элемента DOM, переданного в качестве аргумента. Это делает элемент видимым, даже если он был скрыт с использованием CSS. Дополнительно, метод прокручивает элемент в область видимости.

**Параметры**:
- `element` (WebElement): Объект WebElement, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении JavaScript-кода.

#### `ready_state`

```python
@property
def ready_state(self) -> str:
    """Получает статус загрузки документа.

    Returns:
        str: 'loading', если документ еще загружается, 'complete', если загрузка завершена.
    """
    try:
        return self.driver.execute_script('return document.readyState;')
    except Exception as ex:
        logger.error('Error retrieving document.readyState: %s', ex)
        return ''
```

**Назначение**: Метод возвращает текущий статус загрузки документа.

**Как работает метод**: Метод выполняет JavaScript-код, который возвращает значение свойства `document.readyState`. Это свойство указывает, находится ли документ в состоянии загрузки или загрузка завершена.

**Возвращает**:
- `str`: `'loading'`, если документ еще загружается, `'complete'`, если загрузка завершена, или пустая строка в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении JavaScript-кода.

#### `window_focus`

```python
def window_focus(self) -> None:
    """Устанавливает фокус на окно браузера с помощью JavaScript.

    Пытается вывести окно браузера на передний план.
    """
    try:
        self.driver.execute_script('window.focus();')
    except Exception as ex:
        logger.error('Error executing window.focus(): %s', ex)
```

**Назначение**: Метод устанавливает фокус на окно браузера.

**Как работает метод**: Метод выполняет JavaScript-код, который вызывает метод `window.focus()`. Это приводит к тому, что окно браузера получает фокус, и пользователь может взаимодействовать с ним.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении JavaScript-кода.

#### `get_referrer`

```python
def get_referrer(self) -> str:
    """Получает URL-адрес referrer текущего документа.

    Returns:
        str: URL-адрес referrer или пустая строка, если он недоступен.
    """
    try:
        return self.driver.execute_script('return document.referrer;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.referrer: %s', ex)
        return ''
```

**Назначение**: Метод возвращает URL-адрес referrer текущего документа.

**Как работает метод**: Метод выполняет JavaScript-код, который возвращает значение свойства `document.referrer`. Это свойство содержит URL-адрес страницы, с которой пользователь перешел на текущую страницу.

**Возвращает**:
- `str`: URL-адрес referrer или пустая строка, если он недоступен.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении JavaScript-кода.

#### `get_page_lang`

```python
def get_page_lang(self) -> str:
    """Получает язык текущей страницы.

    Returns:
        str: Код языка страницы или пустая строка, если он недоступен.
    """
    try:
        return self.driver.execute_script('return document.documentElement.lang;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.documentElement.lang: %s', ex)
        return ''
```

**Назначение**: Метод возвращает язык текущей страницы.

**Как работает метод**: Метод выполняет JavaScript-код, который возвращает значение свойства `document.documentElement.lang`. Это свойство содержит код языка, указанный в HTML-теге `<html lang="...">`.

**Возвращает**:
- `str`: Код языка страницы или пустая строка, если он недоступен.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении JavaScript-кода.