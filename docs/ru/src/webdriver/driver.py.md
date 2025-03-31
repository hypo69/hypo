# Модуль для работы с веб-драйверами Selenium

## Обзор

Модуль `driver.py` предоставляет класс `Driver`, который обеспечивает унифицированный интерфейс для работы с веб-драйверами Selenium. Он упрощает взаимодействие с веб-браузерами, такими как Chrome, Firefox и Edge.

## Подробней

Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium. Он предоставляет интерфейс для взаимодействия с веб-браузерами, такими как Chrome, Firefox и Edge. Код вебдрайверов находится в подмодулях `chrome`, `firefox`, `edge`, `playwright`. Файлы настроек для веб-браузеров находятся в: `chrome\chrome.json`, `firefox\firefox.json`, `edge\edge.json`, `playwright\playwright.json`. Класс Driver упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

## Классы

### `Driver`

**Описание**: Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

**Как работает класс**:
Класс `Driver` инициализируется с использованием класса веб-драйвера (например, `Chrome`, `Firefox`). Он предоставляет методы для навигации по URL, управления куками и выполнения JavaScript.  Класс также содержит вспомогательные методы, такие как `scroll` для прокрутки страницы и `fetch_html` для извлечения HTML-контента. В целом, класс предназначен для упрощения и стандартизации взаимодействия с веб-браузерами через Selenium.

**Методы**:
- `__init__(self, webdriver_cls, *args, **kwargs)`: Инициализирует экземпляр класса Driver.
- `__init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__(self, item: str)`: Прокси для доступа к атрибутам драйвера.
- `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3)`: Прокручивает страницу в указанном направлении.
- `locale(self)`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url(self, url: str)`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open(self, url: Optional[str] = None)`: Открывает новую вкладку в текущем окне браузера и переключается на неё.
- `wait(self, delay: float = .3)`: Ожидает указанное количество времени.
- `_save_cookies_localy(self)`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html(self, url: str)`: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `webdriver_cls`: Класс WebDriver, например Chrome или Firefox.
- `args`: Позиционные аргументы для драйвера.
- `kwargs`: Ключевые аргументы для драйвера.
- `browser_name` (Optional[str], optional): Имя браузера. По умолчанию `None`.
- `item` (str): Имя атрибута.
- `scrolls` (int, optional): Количество прокруток, по умолчанию 1.
- `frame_size` (int, optional): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str, optional): Направление ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float, optional): Задержка между прокрутками, по умолчанию 0.3.
- `url` (str): URL для перехода.

**Примеры**
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```
```python
driver.current_url
```
```python
driver.scroll(scrolls=3, direction='down')
```
```python
lang = driver.locale
print(lang)  # 'en' или None
```

## Функции

### `__init__`

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
    ...
```

**Как работает функция**:
Метод `__init__` инициализирует экземпляр класса `Driver`. Он принимает класс веб-драйвера (`webdriver_cls`), а также произвольные позиционные и ключевые аргументы, которые передаются конструктору этого класса. Если переданный класс не имеет атрибута `get`, возбуждается исключение `TypeError`.

**Параметры**:
- `webdriver_cls`: Класс WebDriver, например `Chrome` или `Firefox`.
- `*args`: Произвольные позиционные аргументы для драйвера.
- `**kwargs`: Произвольные ключевые аргументы для драйвера.

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
    Автоматически вызывается при создании подкласса `Driver`.

    Args:
        browser_name: Имя браузера.
        kwargs: Дополнительные аргументы.

    Raises:
        ValueError: Если browser_name не указан.
    """
    ...
```

**Как работает функция**:
Метод `__init_subclass__` автоматически вызывается при создании подкласса `Driver`. Он проверяет, указано ли имя браузера (`browser_name`) в аргументах ключевых слов. Если имя браузера не указано, возбуждается исключение `ValueError`. Этот метод гарантирует, что каждый подкласс `Driver` имеет связанное с ним имя браузера.

**Параметры**:
- `browser_name` (Optional[str], optional): Имя браузера. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

### `__getattr__`

```python
def __getattr__(self, item: str):
    """
    Прокси для доступа к атрибутам драйвера.

    Args:
        item: Имя атрибута.

    Example:
        >>> driver.current_url
    """
    ...
```

**Как работает функция**:
Метод `__getattr__` используется для перехвата обращений к атрибутам, которые не существуют непосредственно в классе `Driver`. Он перенаправляет эти обращения к атрибутам базового объекта `driver` (экземпляру Selenium WebDriver). Это позволяет экземпляру `Driver` прозрачно предоставлять доступ ко всем атрибутам и методам базового драйвера Selenium.

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
        frame_size: Размер прокрутки в пикселях, по умолчанию 600.
        direction: Направление ('both', 'down', 'up'), по умолчанию 'both'.
        delay: Задержка между прокрутками, по умолчанию 0.3.

    Returns:
        True, если успешно, иначе False.

    Example:
        >>> driver.scroll(scrolls=3, direction='down')
    """
    ...
```

**Как работает функция**:
Метод `scroll` прокручивает веб-страницу в указанном направлении. Он использует JavaScript для прокрутки страницы на заданное количество пикселей (`frame_size`) указанное количество раз (`scrolls`) с заданной задержкой (`delay`) между прокрутками. Направление прокрутки определяется параметром `direction`, который может принимать значения `'forward'`, `'down'`, `'backward'`, `'up'` или `'both'`.

**Параметры**:
- `scrolls` (int, optional): Количество прокруток, по умолчанию 1.
- `frame_size` (int, optional): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str, optional): Направление ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float, optional): Задержка между прокрутками, по умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, иначе `False`.

**Примеры**:
```python
driver.scroll(scrolls=3, direction='down')
```

### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Определяет язык страницы на основе мета-тегов или JavaScript.

    Returns:
        Код языка, если найден, иначе None.

    Example:
        >>> lang = driver.locale
        >>> print(lang)  # 'en' или None
    """
    ...
```

**Как работает функция**:
Свойство `locale` определяет язык страницы, сначала пытаясь извлечь его из мета-тега `Content-Language`, а затем, если это не удается, вызывая метод `get_page_lang()` (предположительно, определенный в другом месте) для получения языка с использованием JavaScript. Если ни один из этих методов не дает результата, возвращается `None`.

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
        url: URL для перехода.

    Returns:
        `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

    Raises:
        WebDriverException: Если возникает ошибка с WebDriver.
        InvalidArgumentException: Если URL некорректен.
        Exception: Для любых других ошибок при переходе.
    """
    ...
```

**Как работает функция**:
Метод `get_url` переходит по указанному URL, сохраняя текущий URL в `previous_url` и сохраняя куки. Он также обрабатывает исключения, которые могут возникнуть при переходе, такие как `WebDriverException` и `InvalidArgumentException`.

**Параметры**:
- `url` (str): URL для перехода.

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
    ...
```

**Как работает функция**:
Метод `window_open` открывает новую вкладку в текущем окне браузера и переключается на неё. Если указан URL, он открывается в новой вкладке.

**Параметры**:
- `url` (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию `None`.

### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное количество времени.

    Args:
        delay: Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
    ...
```

**Как работает функция**:
Метод `wait` приостанавливает выполнение программы на указанное количество секунд.

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

**Как работает функция**:
Метод `_save_cookies_localy` сохраняет текущие куки веб-драйвера в локальный файл, используя модуль `pickle`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении куки.

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Извлекает HTML-контент из файла или веб-страницы.

    Args:
        url: Путь к файлу или URL для извлечения HTML-контента.

    Returns:
        Возвращает `True`, если контент успешно получен, иначе `None`.

    Raises:
        Exception: Если возникает ошибка при извлечении контента.
    """
    ...
```

**Как работает функция**:
Метод `fetch_html` извлекает HTML-контент либо из локального файла, либо из веб-страницы по указанному URL. Если URL начинается с `file://`, он пытается прочитать содержимое файла. Если URL начинается с `http://` или `https://`, он использует метод `get_url` для получения HTML-контента.

**Параметры**:
- `url` (str): Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:
- `Optional[bool]`: Возвращает `True`, если контент успешно получен, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при извлечении контента.