# Модуль для работы с веб-драйверами Selenium `driver.py`

## Обзор

Модуль `driver.py` предоставляет класс `Driver`, предназначенный для унифицированного взаимодействия с веб-драйверами Selenium. Он обеспечивает удобный интерфейс для управления веб-браузерами, такими как Chrome, Firefox и Edge, абстрагируя детали инициализации и управления драйверами.

## Подробнее

Основное назначение класса `Driver` — упростить работу с веб-драйверами, предоставляя методы для навигации по URL, управления куками, выполнения JavaScript-кода и обработки исключений. Это позволяет разработчикам сосредоточиться на логике автоматизации, а не на особенностях работы с конкретными драйверами. Файлы настроек для веб-браузеров находятся в: `chrome\\chrome.json`, `firefox\\firefox.json`, `edge\\edge.json`, `playwright\\playwright.json`.

## Классы

### `Driver`

**Описание**:
Класс `Driver` обеспечивает удобный интерфейс для работы с различными веб-драйверами, такими как Chrome, Firefox и Edge.

**Атрибуты**:
- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Методы**:
- `__init__(webdriver_cls, *args, **kwargs)`: Инициализирует экземпляр класса `Driver`.
- `__init_subclass__(cls, *, browser_name: Optional[str] = None, **kwargs)`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__(self, item: str)`: Прокси для доступа к атрибутам драйвера.
- `scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool`: Прокручивает страницу в указанном направлении.
- `locale(self) -> Optional[str]`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url(self, url: str) -> bool`: Переходит по указанному URL и сохраняет текущий URL, предыдущий URL и куки.
- `window_open(self, url: Optional[str] = None) -> None`: Открывает новую вкладку в текущем окне браузера и переключается на неё.
- `wait(self, delay: float = .3) -> None`: Ожидает указанное количество времени.
- `_save_cookies_localy(self) -> None`: Сохраняет текущие куки веб-драйвера в локальный файл.
- `fetch_html(self, url: str) -> Optional[bool]`: Извлекает HTML-контент из файла или веб-страницы.

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

**Назначение**:
Инициализирует экземпляр класса `Driver`, создавая экземпляр указанного класса WebDriver (например, Chrome, Firefox).

**Параметры**:
- `webdriver_cls`: Класс WebDriver, который необходимо инстанцировать (например, `Chrome` или `Firefox`).
- `*args`: Позиционные аргументы, передаваемые конструктору `webdriver_cls`.
- `**kwargs`: Ключевые аргументы, передаваемые конструктору `webdriver_cls`.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом WebDriver (т.е. не имеет атрибута `get`).

**Как работает функция**:

1. **Проверка типа webdriver_cls**: Проверяет, является ли переданный `webdriver_cls` допустимым классом WebDriver, проверяя наличие у него атрибута `get`.
2. **Создание экземпляра драйвера**: Создает экземпляр класса `webdriver_cls` с переданными аргументами и сохраняет его в атрибуте `self.driver`.

```
Проверка webdriver_cls (наличие атрибута 'get')
|
да
|
Создание экземпляра webdriver_cls
|
Сохранение экземпляра в self.driver
```

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

**Назначение**:
Автоматически вызывается при создании подкласса `Driver`. Используется для установки имени браузера для подкласса.

**Параметры**:
- `cls`: Класс, для которого вызывается метод.
- `browser_name` (Optional[str]): Имя браузера (например, "Chrome", "Firefox").
- `**kwargs`: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

**Как работает функция**:

1. **Вызов родительского метода**: Вызывает метод `__init_subclass__` родительского класса.
2. **Проверка browser_name**: Проверяет, указано ли имя браузера (`browser_name`). Если нет, вызывает исключение `ValueError`.
3. **Установка атрибута browser_name**: Устанавливает атрибут `browser_name` класса равным переданному значению.

```
Вызов super().__init_subclass__()
|
Проверка наличия browser_name
|
нет -> ValueError
|
да
|
Установка cls.browser_name = browser_name
```

**Примеры**:
```python
class MyChromeDriver(Driver, browser_name='Chrome'):
    ...
```

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

**Назначение**:
Перехватывает обращение к несуществующим атрибутам экземпляра класса `Driver` и пытается получить их из экземпляра Selenium WebDriver, хранящегося в `self.driver`.

**Параметры**:
- `item` (str): Имя атрибута, к которому происходит обращение.

**Как работает функция**:

1. **Перехват атрибута**: При попытке доступа к атрибуту, которого нет в экземпляре `Driver`, вызывается метод `__getattr__`.
2. **Получение атрибута из WebDriver**: Метод пытается получить атрибут с именем `item` из экземпляра Selenium WebDriver, хранящегося в `self.driver`.
3. **Возврат атрибута**: Если атрибут найден в экземпляре WebDriver, он возвращается. Если атрибут не найден, будет вызвано исключение `AttributeError`.

```
Перехват обращения к несуществующему атрибуту
|
Попытка получения атрибута из self.driver
|
Атрибут найден -> возврат атрибута
|
Атрибут не найден -> AttributeError
```

**Примеры**:
```python
driver = Driver(Chrome)
url = driver.current_url  # Обращение к атрибуту current_url экземпляра Chrome
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

**Назначение**:
Прокручивает страницу в указанном направлении заданное количество раз с определенным размером шага и задержкой.

**Параметры**:
- `scrolls` (int): Количество прокруток, по умолчанию 1.
- `frame_size` (int): Размер прокрутки в пикселях, по умолчанию 600.
- `direction` (str): Направление прокрутки ('both', 'down', 'up'), по умолчанию 'both'.
- `delay` (float): Задержка между прокрутками в секундах, по умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в случае ошибки.

**Внутренние функции**:
- `carousel(direction: str = '', scrolls: int = 1, frame_size: int = 600, delay: float = .3) -> bool`:
    - **Назначение**: Внутренняя функция для выполнения фактической прокрутки страницы в заданном направлении.
    - **Параметры**:
        - `direction` (str): Направление прокрутки ('down', 'up').
        - `scrolls` (int): Количество прокруток.
        - `frame_size` (int): Размер прокрутки в пикселях.
        - `delay` (float): Задержка между прокрутками в секундах.
    - **Возвращает**:
        - `bool`: `True`, если прокрутка выполнена успешно, `False` в случае ошибки.

**Как работает функция**:

1. **Выбор направления**: В зависимости от значения параметра `direction`, функция вызывает внутреннюю функцию `carousel` с соответствующими параметрами.
2. **Обработка направления 'both'**: Если `direction` равно 'both', функция вызывает `carousel` дважды: один раз для прокрутки вниз, другой раз для прокрутки вверх.
3. **Обработка исключений**: Если в процессе прокрутки возникает исключение, оно логируется, и функция возвращает `False`.

**Как работает внутренняя функция `carousel`**:

1. **Цикл прокрутки**: Выполняет цикл прокрутки страницы `scrolls` раз.
2. **Выполнение JavaScript**: В каждой итерации цикла выполняет JavaScript-код, который прокручивает страницу на `frame_size` пикселей в указанном направлении.
3. **Задержка**: После каждой прокрутки ожидает `delay` секунд.
4. **Обработка исключений**: Если в процессе прокрутки возникает исключение, оно логируется, и функция возвращает `False`.

```
Начало функции scroll
|
Выбор направления
|
direction == 'forward' или 'down' -> carousel('', scrolls, frame_size, delay)
|
direction == 'backward' или 'up' -> carousel('-', scrolls, frame_size, delay)
|
direction == 'both' -> carousel('', scrolls, frame_size, delay) и carousel('-', scrolls, frame_size, delay)
|
Обработка исключений
|
Конец функции scroll

Начало функции carousel
|
Цикл прокрутки (scrolls раз)
|
Выполнение JavaScript (window.scrollBy)
|
Задержка (time.sleep)
|
Обработка исключений
|
Конец функции carousel
```

**Примеры**:
```python
driver.scroll(scrolls=3, direction='down')  # Прокрутить страницу 3 раза вниз
driver.scroll(direction='both')  # Прокрутить страницу вверх и вниз по одному разу
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

**Назначение**:
Определяет язык страницы, анализируя мета-теги и выполняя JavaScript-код.

**Возвращает**:
- `Optional[str]`: Код языка страницы (например, 'en', 'ru') в случае успеха, `None` в противном случае.

**Как работает функция**:

1. **Поиск мета-тега**: Пытается найти мета-тег `Content-Language` с помощью CSS-селектора.
2. **Извлечение языка из мета-тега**: Если мета-тег найден, извлекает значение атрибута `content`, которое содержит код языка.
3. **Использование JavaScript**: Если мета-тег не найден или произошла ошибка, пытается определить язык страницы с помощью JavaScript-функции `get_page_lang`.
4. **Обработка исключений**: Если ни один из способов не позволил определить язык страницы, возвращает `None`.

```
Поиск мета-тега Content-Language
|
Мета-тег найден -> извлечение кода языка
|
Мета-тег не найден или ошибка -> попытка определить язык через JavaScript
|
JavaScript успешно выполнен -> возврат кода языка
|
JavaScript не выполнен или ошибка -> возврат None
```

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

**Назначение**:
Переходит по указанному URL, сохраняет текущий и предыдущий URL, а также куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если переход успешен и текущий URL совпадает с ожидаемым, `False` в противном случае.

**Вызывает исключения**:
- `WebDriverException`: Если возникает ошибка с WebDriver.
- `InvalidArgumentException`: Если URL некорректен.
- `Exception`: Для любых других ошибок при переходе.

**Как работает функция**:

1. **Сохранение предыдущего URL**: Сохраняет текущий URL в переменную `_previous_url`.
2. **Переход по URL**: Использует метод `driver.get(url)` для перехода по указанному URL.
3. **Ожидание загрузки страницы**: Ожидает завершения загрузки страницы, проверяя `ready_state`. Если страница не загрузилась за 5 попыток, прерывает выполнение. <инструкция для модели gemini: добавить обработку таймаута при загрузке страницы>
4. **Сохранение куки**: Вызывает метод `_save_cookies_localy()` для сохранения куки.
5. **Обработка исключений**: Перехватывает исключения `WebDriverException`, `InvalidArgumentException` и `Exception`, логирует ошибки и возвращает `False`.

```
Сохранение предыдущего URL
|
Переход по URL (driver.get(url))
|
Ожидание загрузки страницы
|
Сохранение куки (_save_cookies_localy())
|
Обработка исключений
|
Возврат True или False
```

**Примеры**:
```python
success = driver.get_url('https://www.example.com')
if success:
    print('Переход успешен')
else:
    print('Переход не удался')
```

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """Open a new tab in the current browser window and switch to it.

    Args:
        url: URL to open in the new tab. Defaults to `None`.
    """
    ...
```

**Назначение**:
Открывает новую вкладку в текущем окне браузера и переключается на неё.

**Параметры**:
- `url` (Optional[str]): URL для открытия в новой вкладке. Если не указан, открывается пустая вкладка.

**Как работает функция**:

1. **Открытие новой вкладки**: Выполняет JavaScript-код `window.open();`, который открывает новую вкладку в браузере.
2. **Переключение на новую вкладку**: Переключается на новую вкладку, используя `self.switch_to.window(self.window_handles[-1])`.
3. **Переход по URL**: Если указан URL, переходит по нему в новой вкладке, используя `self.get(url)`.

```
Открытие новой вкладки (window.open())
|
Переключение на новую вкладку
|
Если указан URL -> переход по URL
```

**Примеры**:
```python
driver.window_open()  # Открыть пустую вкладку
driver.window_open('https://www.example.com')  # Открыть вкладку с URL
```

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

**Назначение**:
Приостанавливает выполнение программы на указанное количество секунд.

**Параметры**:
- `delay` (float): Время задержки в секундах. По умолчанию 0.3.

**Как работает функция**:

1. **Приостановка выполнения**: Использует функцию `time.sleep(delay)` для приостановки выполнения программы на `delay` секунд.

```
Приостановка выполнения (time.sleep(delay))
```

**Примеры**:
```python
driver.wait(1)  # Ожидать 1 секунду
driver.wait()  # Ожидать 0.3 секунды (по умолчанию)
```

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

**Назначение**:
Сохраняет текущие куки веб-драйвера в локальный файл.

**Как работает функция**:
Пока возвращает True. (debug)
1. **Открытие файла**: Открывает файл для записи куки в бинарном формате. Путь к файлу берется из `gs.cookies_filepath`.
2. **Сохранение куки**: Использует `pickle.dump()` для сериализации и сохранения куки в файл. Куки получаются из `self.driver.get_cookies()`.
3. **Обработка исключений**: Перехватывает исключения, возникающие при открытии файла или сохранении куки, и логирует ошибки.

```
Открытие файла для записи куки
|
Сериализация и сохранение куки в файл
|
Обработка исключений
```

**Примеры**:
```python
driver._save_cookies_localy()
```

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

**Назначение**:
Извлекает HTML-контент из указанного URL, который может быть как локальным файлом, так и веб-страницей.

**Параметры**:
- `url` (str): URL для извлечения HTML-контента. Может начинаться с `file://`, `http://` или `https://`.

**Возвращает**:
- `Optional[bool]`: `True`, если контент успешно получен и сохранен в `self.html_content`, `False` в случае ошибки.

**Как работает функция**:

1. **Определение типа URL**: Проверяет, начинается ли URL с `file://`, `http://` или `https://`, чтобы определить, как извлекать контент.
2. **Извлечение из локального файла**:
    - Если URL начинается с `file://`, извлекает путь к файлу из URL.
    - Проверяет существование файла.
    - Открывает файл в режиме чтения с кодировкой UTF-8.
    - Читает содержимое файла и сохраняет его в `self.html_content`.
3. **Извлечение из веб-страницы**:
    - Если URL начинается с `http://` или `https://`, использует метод `self.get_url(url)` для перехода по URL.
    - Если переход успешен, сохраняет `self.page_source` (HTML-код страницы) в `self.html_content`.
4. **Обработка ошибок**: Логирует ошибки и возвращает `False` в случае возникновения исключений.

```
Определение типа URL
|
URL начинается с file://
|
Извлечение пути к файлу
|
Проверка существования файла
|
Чтение содержимого файла
|
Сохранение в self.html_content
|
URL начинается с http:// или https://
|
Переход по URL (self.get_url(url))
|
Сохранение self.page_source в self.html_content
|
Обработка ошибок
```

**Примеры**:
```python
success = driver.fetch_html('file://path/to/local/file.html')
if success:
    print('HTML-контент успешно получен из файла')

success = driver.fetch_html('https://www.example.com')
if success:
    print('HTML-контент успешно получен с веб-страницы')