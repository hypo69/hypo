# Модуль `driver`

## Обзор

Модуль `driver` предназначен для работы с веб-драйверами Selenium. Он предоставляет унифицированный интерфейс для взаимодействия с различными веб-браузерами, такими как Chrome, Firefox и Edge. Модуль содержит класс `Driver`, который упрощает задачи инициализации драйвера, навигации по URL, управления куками и обработки исключений.

## Подробнее

Этот модуль является центральным элементом для управления веб-драйверами в проекте `hypotez`. Он абстрагирует детали реализации конкретных драйверов (Chrome, Firefox и т.д.) и предоставляет единый интерфейс для выполнения основных операций, таких как открытие страниц, прокрутка, сохранение кук и извлечение HTML-контента.
Файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`.

## Классы

### `Driver`

**Описание**: Класс обеспечивает удобный интерфейс для работы с различными драйверами, такими как Chrome, Firefox и Edge.

**Принцип работы**: Класс `Driver` инициализируется с использованием класса веб-драйвера (например, `Chrome` или `Firefox`). Он предоставляет методы для навигации по URL, управления куками, прокрутки страницы и извлечения HTML-контента. Класс также обрабатывает исключения, которые могут возникнуть в процессе работы с веб-драйвером.

**Аттрибуты**:
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Методы**:
- `__init__(webdriver_cls, *args, **kwargs)`: Инициализирует экземпляр класса `Driver`.
- `__init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__(self, item: str)`: Прокси для доступа к атрибутам драйвера.
- `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`: Прокручивает страницу в указанном направлении.
- `locale` (property): Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url(self, url: str) -> bool`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open(self, url: Optional[str] = None) -> None`: Открывает новую вкладку в текущем окне браузера и переключается на нее.
- `wait(self, delay: float = .3) -> None`: Ожидает указанное количество времени.
- `_save_cookies_localy(self) -> None`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html(self, url: str) -> Optional[bool]`: Извлекает HTML-контент из файла или веб-страницы.

### `Driver.__init__`

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

**Назначение**: Инициализирует экземпляр класса `Driver`, создавая экземпляр указанного веб-драйвера.

**Параметры**:
- `webdriver_cls`: Класс WebDriver, который будет использован (например, `Chrome`, `Firefox`).
- `*args`: Позиционные аргументы, передаваемые конструктору `webdriver_cls`.
- `**kwargs`: Ключевые аргументы, передаваемые конструктору `webdriver_cls`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не имеет атрибута `get`, что указывает на недопустимый класс WebDriver.

**Как работает функция**:
1. Проверяется, является ли `webdriver_cls` допустимым классом WebDriver (имеет ли он атрибут `get`).
2. Создается экземпляр `webdriver_cls` с переданными аргументами `*args` и `**kwargs`.
3. Сохраненяется созданный экземпляр в атрибуте `self.driver`.

**Примеры**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

### `Driver.__init_subclass__`

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
```

**Назначение**: Автоматически вызывается при создании подкласса `Driver` и устанавливает атрибут `browser_name` для подкласса.

**Параметры**:
- `browser_name` (Optional[str]): Имя браузера.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

**Как работает функция**:
1. Вызывается метод `__init_subclass__` родительского класса.
2. Проверяется, передан ли аргумент `browser_name`.
3. Если `browser_name` не передан, вызывается исключение `ValueError`.
4. Устанавливается атрибут `browser_name` для класса.

**Примеры**:

```python
class MyDriver(Driver, browser_name="Chrome"):
    pass
```

### `Driver.__getattr__`

```python
def __getattr__(self, item: str):
    """
    Прокси для доступа к атрибутам драйвера.

    Args:
        item: Имя атрибута.

    Example:
        >>> driver.current_url
    """
```

**Назначение**: Обеспечивает доступ к атрибутам объекта `self.driver` (экземпляра веб-драйвера) через экземпляр класса `Driver`.

**Параметры**:
- `item` (str): Имя атрибута, к которому необходимо получить доступ.

**Возвращает**:
- Значение атрибута `item` из объекта `self.driver`.

**Как работает функция**:
1. Пытается получить атрибут `item` из объекта `self.driver` с помощью функции `getattr`.
2. Возвращает полученное значение.

**Примеры**:

```python
driver = Driver(Chrome)
url = driver.current_url  # Получение текущего URL через прокси
```

### `Driver.scroll`

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

**Назначение**: Прокручивает веб-страницу в заданном направлении на определенное количество "прокруток" с заданной задержкой между ними.

**Параметры**:
- `scrolls` (int): Количество прокруток для выполнения. По умолчанию равно 1.
- `frame_size` (int): Размер каждой прокрутки в пикселях. По умолчанию равно 600.
- `direction` (str): Направление прокрутки. Может быть `'both'` (вниз и вверх), `'down'` (вниз), или `'up'` (вверх). По умолчанию `'both'`.
- `delay` (float): Задержка в секундах между каждой прокруткой. По умолчанию 0.3 секунды.

**Возвращает**:
- `bool`: Возвращает `True`, если прокрутка выполнена успешно, и `False` в случае ошибки.

**Вызывает исключения**:
- Исключения, возникающие в процессе выполнения JavaScript кода для прокрутки.

**Как работает функция**:
1. Определяется направление прокрутки на основе параметра `direction`.
2. Вызывается внутренняя функция `carousel` для выполнения фактической прокрутки.
3. В случае `direction == 'both'`, функция `carousel` вызывается дважды: один раз для прокрутки вниз и один раз для прокрутки вверх.
4. Функция `carousel` выполняет прокрутку на `frame_size` пикселей в заданном направлении `scrolls` раз, с задержкой `delay` между прокрутками.
5. Любые исключения, возникающие в процессе прокрутки, перехватываются, логируются, и функция возвращает `False`.

**Внутренние функции**:

#### `carousel`

```python
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
```

**Назначение**: Выполняет прокрутку экрана в заданном направлении на указанное количество пикселей с заданной задержкой.

**Параметры**:
- `direction` (str): Направление прокрутки. Может быть `''` (вниз) или `'-'` (вверх). По умолчанию `''`.
- `scrolls` (int): Количество прокруток. По умолчанию 1.
- `frame_size` (int): Размер каждой прокрутки в пикселях. По умолчанию 600.
- `delay` (float): Задержка между прокрутками в секундах. По умолчанию 0.3.

**Возвращает**:
- `bool`: Возвращает `True`, если прокрутка выполнена успешно, и `False` в случае ошибки.

**Как работает функция**:
1. Выполняет цикл `scrolls` раз.
2. В каждой итерации цикла выполняет JavaScript код `window.scrollBy(0,{direction}{frame_size})`, который прокручивает экран на `frame_size` пикселей в заданном направлении.
3. После каждой прокрутки ждет `delay` секунд с помощью метода `self.wait(delay)`.
4. Если в процессе прокрутки возникает исключение, оно перехватывается, логируется с помощью `logger.error`, и функция возвращает `False`.

**Примеры**:
```python
# Прокрутка вниз 3 раза с размером прокрутки 500 пикселей и задержкой 0.5 секунды
driver.scroll(scrolls=3, frame_size=500, direction='down', delay=0.5)
```

**ASCII Flowchart**:

```
Начало
  ↓
Определение направления
  ↓
Вызов carousel()
  ↓
Цикл scrolls раз
  ↓
Выполнение JS-скрипта прокрутки
  ↓
Ожидание delay секунд
  ↓
Конец цикла
  ↓
Конец
```

### `Driver.locale`

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
    try:
        meta_language = self.find_element(By.CSS_SELECTOR, "meta[http-equiv='Content-Language']")
        return meta_language.get_attribute('content')
    except Exception as ex:
        logger.debug('Не удалось определить язык сайта из META', ex)
        try:
            return self.get_page_lang()
        except Exception as ex:
            logger.debug('Не удалось определить язык сайта из JavaScript', ex)
            return
```

**Назначение**: Определяет язык страницы, сначала пытаясь получить его из мета-тега `Content-Language`, а затем, если это не удается, используя JavaScript.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Optional[str]`: Код языка страницы (например, `'en'`, `'ru'`), если он найден. В противном случае возвращает `None`.

**Как работает функция**:
1. Пытается найти мета-тег `Content-Language` с помощью CSS-селектора `"meta[http-equiv='Content-Language']"`.
2. Если мета-тег найден, извлекает значение атрибута `content` и возвращает его.
3. Если мета-тег не найден или возникает исключение при его поиске, исключение перехватывается и логируется с уровнем `DEBUG`.
4. После этого пытается получить язык страницы с помощью JavaScript, вызывая метод `self.get_page_lang()`.
5. Если вызов `self.get_page_lang()` успешен, возвращает полученный код языка.
6. Если вызов `self.get_page_lang()` также не удается или возникает исключение, исключение перехватывается и логируется с уровнем `DEBUG`, и функция возвращает `None`.

**ASCII Flowchart**:

```
Начало
  ↓
Поиск META-тега Content-Language
  ↓
Успех? → Извлечение content
  |      ↓
  Нет    Попытка получить язык через JS
         ↓
         Успех? → Возврат языка
         |      ↓
         Нет    Возврат None
```

**Примеры**:

```python
driver = Driver(Chrome)
lang = driver.locale
if lang:
    print(f"Язык страницы: {lang}")
else:
    print("Язык страницы не определен")
```

### `Driver.get_url`

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
    _previous_url: str = copy.copy(self.current_url)

    try:
        self.driver.get(url)
       
        attempts = 5
        while self.ready_state not in ('complete','interactive'):
            """ Ожидание завершения загрузки страницы """
            attempts -= 5
            if attempts < 0: # Если страница не загрузилась за 5 попыток, то цикл прерывается с выводом сообщения об ошибке
                logger.error(f'Страница не загрузилась за 5 попыток: {url=}')
                ...
                break
            time.sleep(1)

        if url != _previous_url:
            self.previous_url = _previous_url

        self._save_cookies_localy()
        return True
        
    except WebDriverException as ex:
        logger.error('WebDriverException', ex)
        return False

    except InvalidArgumentException as ex:
        logger.error(f"InvalidArgumentException {url}", ex)
        return False
    except Exception as ex:
        logger.error(f'Ошибка при переходе по URL: {url}\n', ex)
        return False
```

**Назначение**: Переходит по указанному URL, сохраняет текущий URL как предыдущий, сохраняет куки и проверяет успешность перехода.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка, связанная с WebDriver.
- `InvalidArgumentException`: Если URL является некорректным.
- `Exception`: Для любых других ошибок, возникающих при переходе по URL.

**Как работает функция**:
1. Сохраняет текущий URL в переменную `_previous_url`.
2. Пытается перейти по указанному `url` с помощью метода `self.driver.get(url)`.
3. Ожидает завершения загрузки страницы, проверяя свойство `self.ready_state`. Если страница не загружается за 5 попыток, прерывает цикл и логирует ошибку.
4. Если URL отличается от предыдущего, сохраняет предыдущий URL в атрибуте `self.previous_url`.
5. Сохраняет куки с помощью метода `self._save_cookies_localy()`.
6. Возвращает `True`, если все шаги выполнены успешно.
7. В случае возникновения исключений `WebDriverException`, `InvalidArgumentException` или `Exception`, логирует ошибку и возвращает `False`.

**ASCII Flowchart**:

```
Начало
  ↓
Сохранение current_url в _previous_url
  ↓
driver.get(url)
  ↓
Ожидание загрузки страницы (ready_state)
  ↓
url != _previous_url?
  |       ↓
  Нет    Сохранение _previous_url в previous_url
  ↓
_save_cookies_localy()
  ↓
Возврат True
  ↓
Обработка исключений (WebDriverException, InvalidArgumentException, Exception)
  ↓
Логирование ошибки
  ↓
Возврат False
```

**Примеры**:
```python
driver = Driver(Chrome)
url = "https://www.example.com"
success = driver.get_url(url)
if success:
    print(f"Успешно перешли на {url}")
else:
    print(f"Не удалось перейти на {url}")
```

### `Driver.window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url: URL to open in the new tab. Defaults to `None`.
    """
    self.execute_script('window.open();')
    self.switch_to.window(self.window_handles[-1])
    if url:
        self.get(url)
```

**Назначение**: Открывает новую вкладку в текущем окне браузера и переключается на нее. При необходимости загружает указанный URL в новую вкладку.

**Параметры**:
- `url` (Optional[str]): URL, который нужно открыть в новой вкладке. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Выполняет JavaScript-код `window.open();`, который открывает новую вкладку в браузере.
2. Переключается на новую вкладку, используя `self.switch_to.window(self.window_handles[-1])`. `self.window_handles` — это список всех открытых вкладок, а `[-1]` — индекс последней (только что открытой) вкладки.
3. Если указан параметр `url`, загружает его в новой вкладке, используя метод `self.get(url)`.

**ASCII Flowchart**:

```
Начало
  ↓
Выполнение JS-кода window.open()
  ↓
Переключение на последнюю вкладку
  ↓
url указан?
  |       ↓
  Да     Загрузка URL в новой вкладке
  ↓
Конец
```

**Примеры**:

```python
driver = Driver(Chrome)
driver.window_open("https://www.example.com")  # Открывает новую вкладку с example.com
driver.window_open()  # Открывает пустую новую вкладку
```

### `Driver.wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное количество времени.

    Args:
        delay: Время задержки в секундах. По умолчанию 0.3.

    Returns:
        None
    """
    time.sleep(delay)
```

**Назначение**: Приостанавливает выполнение программы на заданное количество секунд.

**Параметры**:
- `delay` (float): Время задержки в секундах. По умолчанию 0.3 секунды.

**Возвращает**:
- `None`

**Как работает функция**:
1. Использует функцию `time.sleep(delay)` для приостановки выполнения программы на `delay` секунд.

**ASCII Flowchart**:

```
Начало
  ↓
time.sleep(delay)
  ↓
Конец
```

**Примеры**:

```python
driver = Driver(Chrome)
print("Начало ожидания")
driver.wait(1)  # Ожидание в течение 1 секунды
print("Ожидание завершено")
```

### `Driver._save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Сохраняет текущие куки веб-драйвера в локальный файл.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении куки.
    """
    return True # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ debug
    try:
        with open(gs.cookies_filepath, 'wb') as cookiesfile:
            pickle.dump(self.driver.get_cookies(), cookiesfile)
    except Exception as ex:
        logger.error('Ошибка при сохранении куки:', ex)
```

**Назначение**: Сохраняет куки текущего сеанса веб-драйвера в локальный файл, используя модуль `pickle` для сериализации данных.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при открытии файла или сериализации куки.

**Как работает функция**:
1. Функция закомментирована и всегда возвращает `True` (отладочный код).
2. Пытается открыть файл, путь к которому берется из `gs.cookies_filepath`, в режиме записи байтов (`'wb'`).
3. Использует `pickle.dump()` для сериализации куки, полученных из `self.driver.get_cookies()`, и записи их в файл.
4. Если во время этой операции возникает исключение, оно перехватывается, и информация об ошибке логируется с помощью `logger.error()`.

**ASCII Flowchart**:

```
Начало
  ↓
try
  ↓
Открытие файла для записи куки
  ↓
Сериализация и запись куки в файл
  ↓
except Exception
  ↓
Логирование ошибки
  ↓
Конец
```

**Примеры**:

```python
driver = Driver(Chrome)
driver.get_url("https://www.example.com")
driver._save_cookies_localy()
```

### `Driver.fetch_html`

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
    if url.startswith('file://'):
        cleaned_url = url.replace('file://', '')
        match = re.search(r'[a-zA-Z]:[\\/].*', cleaned_url)
        if match:
            file_path = Path(match.group(0))
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.html_content = file.read()
                    return True
                except Exception as ex:
                    logger.error('Ошибка при чтении файла:', ex)
                    return False
            else:
                logger.error('Локальный файл не найден:', file_path)
                return False
        else:
            logger.error('Некорректный путь к файлу:', cleaned_url)
            return False
    elif url.startswith('http://') or url.startswith('https://'):
        try:
            if self.get_url(url):
                self.html_content = self.page_source
                return True
        except Exception as ex:
            logger.error(f"Ошибка при получении {url}:", ex)
            return False
    else:
        logger.error("Ошибка: Неподдерживаемый протокол для URL:", url)
        return False
```

**Назначение**: Извлекает HTML-контент из указанного URL, который может быть как локальным файлом, так и веб-страницей.

**Параметры**:
- `url` (str): URL или путь к файлу, из которого нужно извлечь HTML-контент.

**Возвращает**:
- `Optional[bool]`:
  - `True`, если HTML-контент успешно извлечен.
  - `False`, если произошла ошибка при извлечении контента из файла.
  - `None`, если URL имеет неподдерживаемый протокол или произошла ошибка при получении веб-страницы.

**Вызывает исключения**:
- `Exception`: В случае ошибки при чтении локального файла или при получении веб-страницы.

**Как работает функция**:
1. **Проверка типа URL**:
   - Проверяет, начинается ли URL с `file://`. Если да, обрабатывает как локальный файл.
   - Если URL начинается с `http://` или `https://`, обрабатывает как веб-страницу.
   - Если URL не соответствует ни одному из этих протоколов, логирует ошибку и возвращает `False`.

2. **Обработка локального файла**:
   - Удаляет префикс `file://` из URL.
   - Извлекает путь к файлу с помощью регулярного выражения.
   - Проверяет, существует ли файл по указанному пути.
   - Если файл существует, пытается открыть и прочитать его содержимое в кодировке UTF-8.
   - Если чтение успешно, сохраняет содержимое в атрибут `self.html_content` и возвращает `True`.
   - Если происходит ошибка при чтении файла, логирует ошибку и возвращает `False`.
   - Если файл не существует или путь к файлу некорректен, логирует соответствующую ошибку и возвращает `False`.

3. **Обработка веб-страницы**:
   - Если URL начинается с `http://` или `https://`, пытается получить веб-страницу с помощью метода `self.get_url(url)`.
   - Если получение веб-страницы успешно, сохраняет HTML-контент из `self.page_source` в атрибут `self.html_content` и возвращает `True`.
   - Если происходит ошибка при получении веб-страницы, логирует ошибку и возвращает `False`.

**ASCII Flowchart**:

```
Начало
  ↓
Проверка протокола URL
  ↓
file://?
  ├── Да → Обработка локального файла
  │      │
  │      Удаление префикса file://
  │      │
  │      Извлечение пути к файлу
  │      │
  │      Файл существует?
  │      ├── Да → Чтение файла (UTF-8)
  │      │      │
  │      │      Сохранение содержимого в self.html_content
  │      │      │
  │      │      Возврат True
  │      │
  │      └── Нет → Логирование "Локальный файл не найден"
  │             │
  │             Возврат False
  │
  ├── http:// или https://? → Обработка веб-страницы
  │      │
  │      Получение веб-страницы (self.get_url)
  │      │
  │      Успешно?
  │      ├── Да → Сохранение self.page_source в self.html_content
  │      │      │
  │      │      Возврат True
  │      │
  │      └── Нет → Логирование ошибки получения веб-страницы
  │             │
  │             Возврат False
  │
  └── Нет → Логирование "Неподдерживаемый протокол для URL"
         │
         Возврат False
  ↓
Конец
```

**Примеры**:

```python
driver = Driver(Chrome)

# Извлечение HTML-контента из локального файла
file_url = "file://C:/path/to/your/file.html"
if driver.fetch_html(file_url):
    print("HTML-контент успешно извлечен из файла")
else:
    print("Не удалось извлечь HTML-контент из файла")

# Извлечение HTML-контента из веб-страницы
web_url = "https://www.example.com"
if driver.fetch_html(web_url):
    print("HTML-контент успешно извлечен из веб-страницы")
else:
    print("Не удалось извлечь HTML-контент из веб-страницы")