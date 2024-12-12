# Модуль hypotez/src/webdriver/driver.py

## Обзор

Модуль `hypotez/src/webdriver/driver.py` предоставляет класс `Driver` для работы с веб-драйверами Selenium.  Класс обеспечивает унифицированный интерфейс для инициализации, навигации, работы с куки и обработки исключений при взаимодействии с веб-страницами.

## Оглавление

- [Модуль hypotez/src/webdriver/driver.py](#модуль-hypotezsrcwebdriverdriverpy)
- [Класс Driver](#класс-driver)
    - [Метод __init__(self, webdriver_cls, *args, **kwargs)](#метод-initself-webdriver_cls-args-kwargs)
    - [Метод __init_subclass__(cls, *, browser_name=None, **kwargs)](#метод-init_subclasscls-browser_name-kwargs)
    - [Метод __getattr__(self, item)](#метод-getattrself-item)
    - [Метод scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)](#метод-scrollself-scrolls-frame_size-direction-delay)
    - [Метод carousel(direction='', scrolls=1, frame_size=600, delay=.3)](#метод-carouseldirection-scrolls-frame_size-delay)
    - [Свойство locale(self)](#свойство-localeself)
    - [Метод get_url(self, url: str)](#метод-get_urlself-url)
    - [Метод window_open(self, url: Optional[str] = None)](#метод-window_openself-url)
    - [Метод wait(self, delay: float = .3)](#метод-waitself-delay)
    - [Метод _save_cookies_localy(self)](#метод-_save_cookies_localyself)
    - [Метод fetch_html(self, url: str)](#метод-fetch_htmlself-url)


## Классы

### `Driver`

**Описание**: Класс `Driver` предоставляет унифицированный интерфейс для работы с различными веб-драйверами (например, Chrome, Firefox, Edge), обеспечивая удобный способ взаимодействия с веб-страницами.

**Атрибуты**:

- `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Методы**:

#### `__init__(self, webdriver_cls, *args, **kwargs)`

**Описание**: Инициализирует экземпляр класса `Driver`.

**Параметры**:

- `webdriver_cls` (type): Класс WebDriver, например `Chrome` или `Firefox`.
- `args`: Позиционные аргументы для драйвера.
- `kwargs`: Ключевые аргументы для драйвера.

**Пример**:
```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

#### `__init_subclass__(cls, *, browser_name=None, **kwargs)`

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:

- `browser_name` (str): Имя браузера.
- `kwargs`: Дополнительные аргументы.

**Исключения**:

- `ValueError`: Если `browser_name` не указан.

#### `__getattr__(self, item)`

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:

- `item` (str): Имя атрибута.

**Пример**:
```python
driver.current_url
```

#### `scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)`

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:

- `scrolls` (int): Количество прокруток (по умолчанию 1).
- `frame_size` (int): Размер прокрутки в пикселях (по умолчанию 600).
- `direction` (str): Направление ('both', 'down', 'up') (по умолчанию 'both').
- `delay` (float): Задержка между прокрутками (по умолчанию 0.3).

**Возвращает**:

- `bool`: `True`, если успешно, иначе `False`.

#### `get_url(self, url: str)`

**Описание**: Переходит по указанному URL.

**Параметры**:

- `url` (str): URL для перехода.

**Возвращает**:

- `bool`: `True`, если переход успешен, `False` - в противном случае.


**Исключения**:
- `WebDriverException`: Ошибка с WebDriver.
- `InvalidArgumentException`: Некорректный URL.
- `Exception`: Любые другие ошибки при переходе.


(Другие методы и свойства документированы аналогичным образом)