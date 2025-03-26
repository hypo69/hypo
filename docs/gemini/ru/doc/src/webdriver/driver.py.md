# Модуль: src.webdriver.driver

## Обзор

Модуль `src.webdriver.driver` предназначен для работы с веб-драйверами Selenium. Он предоставляет унифицированный интерфейс для взаимодействия с различными веб-драйверами, такими как Chrome, Firefox и Edge.

## Оглавление

1.  [Класс `Driver`](#класс-driver)
    *   [`__init__`](#__init__)
    *   [`__init_subclass__`](#__init_subclass__)
    *   [`__getattr__`](#__getattr__)
    *   [`scroll`](#scroll)
    *   [`locale`](#locale)
    *   [`get_url`](#get_url)
    *   [`window_open`](#window_open)
    *   [`wait`](#wait)
    *   [`_save_cookies_localy`](#_save_cookies_localy)
    *   [`fetch_html`](#fetch_html)

## Классы

### `Driver`

**Описание**:
Унифицированный класс для взаимодействия с Selenium WebDriver. Обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

**Атрибуты**:
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

#### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Инициализирует экземпляр класса Driver.

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

#### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    """
    Автоматически вызывается при создании подкласса `Driver`.

    Args:
        browser_name: Имя браузера.
        kwargs: Дополнительные аргументы.

    Raises:
        ValueError: Если browser_name не указан.
    """
```

#### `__getattr__`

```python
def __getattr__(self, item):
    """
    Прокси для доступа к атрибутам драйвера.

    Args:
        item: Имя атрибута.

    Returns:
        Any: Значение атрибута драйвера.

    Example:
        >>> driver.current_url
    """
```

#### `scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    Прокручивает страницу в указанном направлении.

    Args:
        scrolls (int, optional): Количество прокруток, по умолчанию 1.
        frame_size (int, optional): Размер прокрутки в пикселях, по умолчанию 600.
        direction (str, optional): Направление ('both', 'down', 'up'), по умолчанию 'both'.
        delay (float, optional): Задержка между прокрутками, по умолчанию 0.3.

    Returns:
        bool: True, если успешно, иначе False.

    Example:
        >>> driver.scroll(scrolls=3, direction='down')
    """
```

#### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Определяет язык страницы на основе мета-тегов или JavaScript.

    Returns:
        Optional[str]: Код языка, если найден, иначе None.

    Example:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' или None
    """
```

#### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.

    Args:
        url (str): URL для перехода.

    Returns:
        bool: True, если переход успешен и текущий URL совпадает с ожидаемым, False в противном случае.

    Raises:
        WebDriverException: Если возникает ошибка с WebDriver.
        InvalidArgumentException: Если URL некорректен.
        Exception: Для любых других ошибок при переходе.
    """
```

#### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """
    Открывает новую вкладку в текущем окне браузера и переключается на неё.

    Args:
        url (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию None.
    """
```

#### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное количество времени.

    Args:
        delay (float, optional): Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
```

#### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Сохраняет текущие куки веб-драйвера в локальный файл.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении куки.
    """
```

#### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Извлекает HTML-контент из файла или веб-страницы.

    Args:
        url (str): Путь к файлу или URL для извлечения HTML-контента.

    Returns:
        Optional[bool]: Возвращает `True`, если контент успешно получен, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при извлечении контента.
    """