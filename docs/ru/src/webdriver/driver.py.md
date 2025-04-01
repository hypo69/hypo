# Модуль `driver.py`

## Обзор

Модуль `driver.py` предназначен для работы с веб-драйверами Selenium, предоставляя унифицированный интерфейс для взаимодействия с различными веб-браузерами, такими как Chrome, Firefox и Edge. Он упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

## Подробнее

Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium. Он предоставляет интерфейс для взаимодействия с веб-браузерами, такими как Chrome, Firefox и Edge. Код вебдрайверов находится в подмодулях `chrome`, `firefox`, `edge`, `playwright` . Файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`.

## Классы

### `Driver`

**Описание**: Класс `Driver` обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

**Атрибуты**:
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Методы**:
- `__init__(self, webdriver_cls, *args, **kwargs)`: Инициализирует экземпляр класса `Driver`.
- `__init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__(self, item: str)`: Прокси для доступа к атрибутам драйвера.
- `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3)`: Прокручивает страницу в указанном направлении.
- `locale(self)`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url(self, url: str)`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open(self, url: Optional[str] = None)`: Открывает новую вкладку в текущем окне браузера и переключается на нее.
- `wait(self, delay: float = .3)`: Ожидает указанное количество времени.
- `_save_cookies_localy(self)`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html(self, url: str)`: Извлекает HTML-контент из файла или веб-страницы.

#### `__init__(self, webdriver_cls, *args, **kwargs)`

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

**Назначение**: Инициализирует экземпляр класса `Driver`, устанавливая класс WebDriver (например, Chrome или Firefox) и передавая ему аргументы.

**Параметры**:
- `webdriver_cls`: Класс WebDriver для инициализации.
- `*args`: Позиционные аргументы, передаваемые в конструктор `webdriver_cls`.
- `**kwargs`: Ключевые аргументы, передаваемые в конструктор `webdriver_cls`.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver (т.е. не имеет атрибута `get`).

**Как работает функция**:
1. Проверяет, является ли переданный `webdriver_cls` допустимым классом WebDriver, проверяя наличие у него атрибута `get`.
2. Если проверка проходит, создает экземпляр класса `webdriver_cls`, передавая все дополнительные аргументы `*args` и `**kwargs`.
3. Сохраняет созданный экземпляр WebDriver в атрибуте `self.driver`.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

#### `__init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs)`

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

**Назначение**: Автоматически вызывается при создании подкласса `Driver` для установки имени браузера.

**Параметры**:
- `browser_name`: Имя браузера, которое необходимо установить.
- `kwargs`: Дополнительные ключевые аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

**Как работает функция**:
1. Вызывает метод `__init_subclass__` родительского класса.
2. Проверяет, был ли указан аргумент `browser_name`.
3. Если `browser_name` не указан, вызывает исключение `ValueError`.
4. Устанавливает атрибут `browser_name` класса равным переданному значению.

**Примеры**:

```python
class MyDriver(Driver, browser_name='Chrome'):
    pass
```

#### `__getattr__(self, item: str)`

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

**Назначение**: Предоставляет прокси-доступ к атрибутам экземпляра `self.driver`.

**Параметры**:
- `item`: Имя атрибута, к которому необходимо получить доступ.

**Как работает функция**:
1. Пытается получить атрибут с именем `item` из экземпляра `self.driver` с помощью `getattr`.
2. Возвращает полученный атрибут.

**Примеры**:

```python
driver = Driver(Chrome)
url = driver.current_url
```

#### `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3)`

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
    def carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool:
        """
        Локальный метод для прокрутки экрана.

        Args:
            direction: Направление ('down', 'up').
            scrolls: Количество прокруток.
            frame_size: Размер прокрутки.
            delay: Задержка между прокрутками.

        Returns:
            True, если успешно, иначе False.
        """
        try:
            for _ in range(scrolls):
                self.execute_script(f'window.scrollBy(0,{direction}{frame_size})')
                self.wait(delay)
            return True
        except Exception as ex:
            logger.error('Ошибка при прокрутке', exc_info=ex)
            return False

    try:
        if direction == 'forward' or direction == 'down':
            return carousel('', scrolls, frame_size, delay)
        elif direction == 'backward' or direction == 'up':
            return carousel('-', scrolls, frame_size, delay)
        elif direction == 'both':
            return carousel('', scrolls, frame_size, delay) and carousel('-', scrolls, frame_size, delay)
    except Exception as ex:
        logger.error('Ошибка в функции прокрутки', ex)
        return False
```

**Назначение**: Прокручивает страницу в указанном направлении заданное количество раз.

**Параметры**:
- `scrolls` (int): Количество прокруток, по умолчанию 1.
- `frame_size` (int): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str): Направление прокрутки ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float): Задержка между прокрутками в секундах, по умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в противном случае.

**Внутренние функции**:

#### `carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3)`

**Назначение**:  Выполняет фактическую прокрутку экрана.

**Параметры**:
- `direction` (str): Направление прокрутки ('down', 'up').
- `scrolls` (int): Количество прокруток.
- `frame_size` (int): Размер прокрутки в пикселях.
- `delay` (float): Задержка между прокрутками в секундах.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в противном случае.

**Как работает функция**:
1. Определяет направление прокрутки на основе входного параметра `direction`.
2. В зависимости от направления вызывает функцию `carousel` с соответствующими параметрами.
3. Если `direction` равен `'both'`, вызывает `carousel` дважды: один раз для прокрутки вниз, другой раз для прокрутки вверх.
4. Возвращает `True`, если все операции прокрутки выполнены успешно, `False` в противном случае.

**Примеры**:

```python
driver.scroll(scrolls=3, direction='down')
```

#### `locale(self)`

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

**Назначение**: Определяет язык страницы на основе мета-тегов или JavaScript.

**Возвращает**:
- `Optional[str]`: Код языка, если он найден, иначе `None`.

**Как работает функция**:
1. Пытается найти мета-тег с атрибутом `http-equiv="Content-Language"`.
2. Если мета-тег найден, возвращает значение его атрибута `content`.
3. Если мета-тег не найден или произошла ошибка, пытается получить язык страницы с помощью JavaScript.
4. Если язык не удалось определить ни одним из способов, возвращает `None`.

**Примеры**:

```python
lang = driver.locale
print(lang)  # 'en' или None
```

#### `get_url(self, url: str)`

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

**Назначение**: Переходит по указанному URL, сохраняет текущий и предыдущий URL, а также куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка с WebDriver.
- `InvalidArgumentException`: Если URL некорректен.
- `Exception`: Для любых других ошибок при переходе.

**Как работает функция**:
1. Сохраняет текущий URL в переменную `_previous_url`.
2. Пытается перейти по указанному URL с помощью `self.driver.get(url)`.
3. Сохраняет куки локально с помощью `self._save_cookies_localy()`.
4. Возвращает `True`, если переход успешен, и `False` в случае ошибки.

**Примеры**:

```python
success = driver.get_url('https://www.example.com')
```

#### `window_open(self, url: Optional[str] = None)`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url: URL to open in the new tab. Defaults to `None`.
    """
    ...
```

**Назначение**: Открывает новую вкладку в текущем окне браузера и переключается на нее.

**Параметры**:
- `url` (Optional[str]): URL для открытия в новой вкладке. По умолчанию `None`.

**Как работает функция**:
1. Использует JavaScript для открытия новой вкладки.
2. Переключается на новую вкладку.
3. Если указан URL, открывает его в новой вкладке.

**Примеры**:

```python
driver.window_open('https://www.example.com')
```

#### `wait(self, delay: float = .3)`

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

**Назначение**: Приостанавливает выполнение программы на указанное количество секунд.

**Параметры**:
- `delay` (float): Время задержки в секундах. По умолчанию 0.3.

**Как работает функция**:
1. Использует функцию `time.sleep()` для приостановки выполнения программы на заданное количество секунд.

**Примеры**:

```python
driver.wait(1)  # Ожидание в течение 1 секунды
```

#### `_save_cookies_localy(self)`

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

**Назначение**: Сохраняет текущие куки веб-драйвера в локальный файл.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении куки.

**Как работает функция**:
1. Открывает файл для записи куки.
2. Сохраняет куки в файл, используя `pickle.dump()`.
3. Обрабатывает возможные исключения и логирует их.

**Примеры**:

```python
driver._save_cookies_localy()
```

#### `fetch_html(self, url: str)`

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

**Назначение**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:
- `url` (str): Путь к файлу или URL для извлечения HTML-контента.

**Возвращает**:
- `Optional[bool]`: Возвращает `True`, если контент успешно получен, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при извлечении контента.

**Как работает функция**:
1. Проверяет, начинается ли URL с `file://`. Если да, пытается прочитать HTML-контент из локального файла.
2. Если URL начинается с `http://` или `https://`, использует `self.get_url()` для получения HTML-контента с веб-страницы.
3. В случае успеха сохраняет контент в `self.html_content` и возвращает `True`.
4. Если URL не соответствует ни одному из поддерживаемых протоколов, логирует ошибку и возвращает `False`.

**Примеры**:

```python
driver.fetch_html('file:///path/to/file.html')
driver.fetch_html('https://www.example.com')