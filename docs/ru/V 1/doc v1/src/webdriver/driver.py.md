# Модуль `driver.py`

## Обзор

Модуль `driver.py` предназначен для работы с веб-драйверами Selenium. Он предоставляет унифицированный интерфейс для взаимодействия с различными веб-браузерами, такими как Chrome, Firefox и Edge. Класс `Driver` упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

## Подробней

Основной целью данного модуля является абстрагирование от конкретной реализации веб-драйвера, предоставляя удобный и гибкий интерфейс для автоматизации веб-тестов и сбора данных. Он включает методы для прокрутки страниц, определения языка страницы и сохранения кук.

## Классы

### `Driver`

**Описание**: Унифицированный класс для взаимодействия с Selenium WebDriver.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Driver`.
- `__init_subclass__`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__`: Прокси для доступа к атрибутам драйвера.
- `scroll`: Прокручивает страницу в указанном направлении.
- `locale`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open`: Открывает новую вкладку в текущем браузере и переключается на неё.
- `wait`: Ожидает указанное количество времени.
- `_save_cookies_localy`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html`: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `webdriver_cls` (type): Класс WebDriver, например `Chrome` или `Firefox`.
- `*args`: Позиционные аргументы для драйвера.
- `**kwargs`: Ключевые аргументы для драйвера.
- `item` (str): Имя атрибута.
- `scrolls` (int): Количество прокруток, по умолчанию 1.
- `frame_size` (int): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str): Направление ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float): Задержка между прокрутками, по умолчанию 0.3.
- `url` (str): URL для перехода.

**Примеры**
```python
from selenium.webdriver import Chrome

driver = Driver(Chrome, executable_path='/path/to/chromedriver')
driver.get_url('https://example.com')
```

## Функции

### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Инициализирует экземпляр класса Driver.

    Args:
        webdriver_cls: Класс WebDriver, например Chrome или Firefox.
        type: type
        args: Позиционные аргументы для драйвера.
        kwargs: Ключевые аргументы для драйвера.

    Example:
        >>> from selenium.webdriver import Chrome
        >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `Driver`.

**Параметры**:
- `webdriver_cls` (type): Класс WebDriver, например `Chrome` или `Firefox`.
- `*args`: Позиционные аргументы для драйвера.
- `**kwargs`: Ключевые аргументы для драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    """
    Автоматически вызывается при создании подкласса `Driver`.

    Args:
        browser_name: Имя браузера.
        type: str
        kwargs: Дополнительные аргументы.

    Raises:
        ValueError: Если browser_name не указан.
    """
    ...
```

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:
- `browser_name` (str): Имя браузера.
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

### `__getattr__`

```python
def __getattr__(self, item):
    """
    Прокси для доступа к атрибутам драйвера.

    Args:
        item: Имя атрибута.
        type: str

    Example:
        >>> driver.current_url
    """
    ...
```

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:
- `item` (str): Имя атрибута.

**Примеры**:
```python
driver.current_url
```

### `scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    Прокручивает страницу в указанном направлении.

    Args:
        scrolls: Количество прокруток, по умолчанию 1.
        type: int
        frame_size: Размер прокрутки в пикселях, по умолчанию 600.
        type: int
        direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
        type: str
        delay: Задержка между прокрутками, по умолчанию 0.3.
        type: float
    Returns:
        bool: True, если успешно, иначе False.
    rtype: bool

    Example:
        >>> driver.scroll(scrolls=3, direction='down')
    """
    ...
```

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:
- `scrolls` (int): Количество прокруток, по умолчанию 1.
- `frame_size` (int): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str): Направление ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float): Задержка между прокрутками, по умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Примеры**:
```python
driver.scroll(scrolls=3, direction='down')
```

### `locale`

```python
def locale(self) -> Optional[str]:
    """
    Определяет язык страницы на основе мета-тегов или JavaScript.

    Returns:
        Optional[str]: Код языка, если найден, иначе None.
    rtype: Optional[str]

    Example:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' или None
    """
    ...
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
    Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

    Args:
        url (str): URL для перехода.

    Returns:
        bool: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

    Raises:
        WebDriverException: Если возникает ошибка с WebDriver.
        InvalidArgumentException: Если URL некорректен.
        Exception: Для любых других ошибок при переходе.
    """
    ...
```

**Описание**: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен, иначе `False`.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка с WebDriver.
- `InvalidArgumentException`: Если URL некорректен.
- `Exception`: Для любых других ошибок при переходе.

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url (Optional[str]): URL to open in the new tab. Defaults to `None`.
    """
    ...
```

**Описание**: Открывает новую вкладку в текущем браузере и переключается на неё.

**Параметры**:
- `url` (Optional[str]): URL для открытия в новой вкладке. По умолчанию `None`.

### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное количество времени.

    Args:
        delay (float, optional): Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
    ...
```

**Описание**: Ожидает указанное количество времени.

**Параметры**:
- `delay` (float, optional): Время задержки в секундах. По умолчанию 0.3.

### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Сохраняет текущие куки веб-драйвера в локальный файл.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении куки.
    """
    ...
```

**Описание**: Сохраняет текущие куки веб-драйвера в локальный файл.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении куки.

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Извлекает HTML-контент из файла или веб-страницы.

    Args:
        url (str): Путь к файлу или URL для извлечения HTML-контента.

    Returns:
        Optional[bool]: Возвращает `True`, если контент успешно получен, иначе `None`.

    Raises:
        Exception: Если возникает ошибка при извлечении контента.
    """
    ...
```

**Описание**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `url` (str): Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:
- `Optional[bool]`: Возвращает `True`, если контент успешно получен, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при извлечении контента.