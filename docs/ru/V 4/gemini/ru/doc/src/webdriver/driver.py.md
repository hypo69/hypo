# Модуль `driver.py`

## Обзор

Модуль `driver.py` предоставляет класс `Driver`, который обеспечивает унифицированный интерфейс для работы с веб-драйверами Selenium. Это упрощает взаимодействие с веб-браузерами, такими как Chrome, Firefox и Edge. Класс `Driver` упрощает инициализацию драйвера, навигацию по URL, управление куками и обработку исключений. Код веб-драйверов находится в подмодулях `chrome`, `firefox`, `edge`, `playwright`, а файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`.

## Подробней

Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium. Он предоставляет интерфейс для взаимодействия с веб-браузерами, такими как Chrome, Firefox и Edge. Код вебдрайверов находится в подмодулях `chrome`, `firefox`, `edge`, `playwright`. Файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`. Класс Driver упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

## Классы

### `Driver`

**Описание**:
Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

**Методы**:
- `__init__`: Инициализирует экземпляр класса Driver.
- `__init_subclass__`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__`: Прокси для доступа к атрибутам драйвера.
- `scroll`: Прокручивает страницу в указанном направлении.
- `locale`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open`: Открывает новую вкладку в текущем окне браузера и переключается на нее.
- `wait`: Ожидает указанное количество времени.
- `_save_cookies_localy`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html`: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

## Функции

### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Args:
        webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        args: Позиционные аргументы для драйвера.
        kwargs: Ключевые аргументы для драйвера.

    Raises:
        TypeError: Если `webdriver_cls` не является допустимым классом WebDriver.

    Example:
        >>> from selenium.webdriver import Chrome
        >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """
```

**Описание**: Инициализирует экземпляр класса `Driver`.

**Параметры**:
- `webdriver_cls`: Класс WebDriver, например Chrome или Firefox.
- `args`: Позиционные аргументы для драйвера.
- `kwargs`: Ключевые аргументы для драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs):
    """
    Args:
        browser_name: Имя браузера.
        kwargs: Дополнительные аргументы.

    Raises:
        ValueError: Если browser_name не указан.
    """
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:
- `browser_name`: Имя браузера.
- `kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

### `__getattr__`

```python
def __getattr__(self, item: str):
    """
    Args:
        item: Имя атрибута.

    Example:
        >>> driver.current_url
    """
```

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:
- `item`: Имя атрибута.

**Примеры**:
```python
driver.current_url
```

### `scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    Args:
        scrolls: Количество прокруток, по умолчанию 1.
        frame_size: Размер прокрутки в пикселях, по умолчанию 600.
        direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
        delay: Задержка между прокрутками, по умолчанию 0.3.

    Returns:
        True, если успешно, иначе False.

    Example:
        >>> driver.scroll(scrolls=3, direction='down')
    """
```

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:
- `scrolls`: Количество прокруток, по умолчанию 1.
- `frame_size`: Размер прокрутки в пикселях, по умолчанию 600.
- `direction`: Направление ('both', 'down', 'up'), по умолчанию 'both'.
- `delay`: Задержка между прокрутками, по умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Примеры**:
```python
driver.scroll(scrolls=3, direction='down')
```

### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Returns:
        Код языка, если найден, иначе None.

    Example:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' или None
    """
```

**Описание**: Определяет язык страницы на основе мета-тегов или JavaScript.

**Возвращает**:
- `Optional[str]`: Код языка, если найден, иначе `None`.

**Примеры**:
```python
lang = driver.locale
print(lang)  # 'en' или None
```

### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Args:
        url: URL для перехода.

    Returns:
        `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

    Raises:
        WebDriverException: Если возникает ошибка с WebDriver.
        InvalidArgumentException: Если URL некорректен.
        Exception: Для любых других ошибок при переходе.
    """
```

**Описание**: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

**Параметры**:
- `url`: URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка с WebDriver.
- `InvalidArgumentException`: Если URL некорректен.
- `Exception`: Для любых других ошибок при переходе.

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url: URL to open in the new tab. Defaults to `None`.
    """
```

**Описание**: Открывает новую вкладку в текущем окне браузера и переключается на нее.

**Параметры**:
- `url`: URL для открытия в новой вкладке. По умолчанию `None`.

### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Args:
        delay: Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
```

**Описание**: Ожидает указанное количество времени.

**Параметры**:
- `delay`: Время задержки в секундах. По умолчанию 0.3.

**Возвращает**:
- `None`

### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении куки.
    """
```

**Описание**: Сохраняет текущие куки веб-драйвера в локальный файл.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении куки.

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Args:
        url: Путь к файлу или URL для извлечения HTML-контента.

    Returns:
        Возвращает `True`, если контент успешно получен, иначе `None`.

    Raises:
        Exception: Если возникает ошибка при извлечении контента.
    """
```

**Описание**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `url`: Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:
- `Optional[bool]`: Возвращает `True`, если контент успешно получен, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при извлечении контента.