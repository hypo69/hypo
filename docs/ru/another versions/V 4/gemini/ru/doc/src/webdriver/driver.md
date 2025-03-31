# Модуль `src.webdriver.driver`

## Обзор

Модуль `src.webdriver.driver` предназначен для работы с веб-драйверами Selenium. Основная цель класса `Driver` - предоставить унифицированный интерфейс для взаимодействия с веб-драйверами Selenium. Класс предлагает методы для инициализации драйвера, навигации, управления куки, обработки исключений и других операций.

## Подробней

Этот модуль упрощает взаимодействие с Selenium, предоставляя удобные методы для выполнения различных задач, таких как навигация по страницам, управление cookie и обработка ошибок. Он абстрагирует сложность работы с веб-драйверами, делая код более читаемым и поддерживаемым.

## Классы

### `Driver`

**Описание**:
Класс `Driver` предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами Selenium.

**Методы**:
- `__init__`: Инициализирует экземпляр веб-драйвера.
- `__init_subclass__`: Автоматически вызывается при создании подкласса `Driver`.
- `__getattr__`: Предоставляет прокси для доступа к атрибутам драйвера.
- `scroll`: Прокручивает страницу в указанном направлении.
- `locale`: Определяет язык страницы на основе мета-тегов или JavaScript.
- `get_url`: Переходит по указанному URL и сохраняет текущие URL и куки.
- `window_open`: Открывает новую вкладку в браузере.
- `wait`: Ожидает указанное время.
- `_save_cookies_localy`: Сохраняет куки веб-драйвера в локальный файл.
- `fetch_html`: Получает HTML-контент из файла или веб-страницы.

**Параметры**:
- `webdriver_cls`: Класс веб-драйвера (например, Chrome, Firefox).
- `*args`: Позиционные аргументы для инициализации драйвера.
- `**kwargs`: Именованные аргументы для инициализации драйвера.

**Примеры**

```python
from selenium.webdriver import Chrome

driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get_url('https://example.com')
```

## Функции

### `__init__`

```python
def __init__(self, webdriver_cls, *args, **kwargs):
    """
    Инициализирует экземпляр веб-драйвера.

    Args:
        webdriver_cls: Класс веб-драйвера (например, Chrome, Firefox).
        *args: Позиционные аргументы для инициализации драйвера.
        **kwargs: Именованные аргументы для инициализации драйвера.

    Raises:
        TypeError: Если `webdriver_cls` не является допустимым классом веб-драйвера.
    """
```

**Описание**:
Инициализирует экземпляр веб-драйвера, проверяя, что переданный класс является допустимым классом веб-драйвера.

**Параметры**:
- `webdriver_cls`: Класс веб-драйвера (например, Chrome, Firefox).
- `*args`: Позиционные аргументы для инициализации драйвера.
- `**kwargs**: Именованные аргументы для инициализации драйвера.

**Вызывает исключения**:
- `TypeError`: Если `webdriver_cls` не является допустимым классом веб-драйвера.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
```

### `__init_subclass__`

```python
def __init_subclass__(cls, *, browser_name=None, **kwargs):
    """
    Автоматически вызывается при создании подкласса `Driver`.

    Args:
        browser_name: Имя браузера.
        **kwargs: Дополнительные аргументы.

    Raises:
        ValueError: Если `browser_name` не указан.
    """
```

**Описание**:
Автоматически вызывается при создании подкласса `Driver` для установки имени браузера.

**Параметры**:
- `browser_name`: Имя браузера.
- `**kwargs**: Дополнительные аргументы.

**Вызывает исключения**:
- `ValueError`: Если `browser_name` не указан.

**Примеры**:

```python
class ChromeDriver(Driver, browser_name='chrome'):
    def __init__(self, *args, **kwargs):
        super().__init__(Chrome, *args, **kwargs)
```

### `__getattr__`

```python
def __getattr__(self, item):
    """
    Предоставляет прокси для доступа к атрибутам драйвера.

    Args:
        item: Имя атрибута.

    Returns:
        object: Значение атрибута.
    """
```

**Описание**:
Предоставляет прокси для доступа к атрибутам драйвера, позволяя обращаться к атрибутам и методам веб-драйвера напрямую через экземпляр класса `Driver`.

**Параметры**:
- `item`: Имя атрибута.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get('https://example.com')  # Вызов метода get драйвера Chrome через __getattr__
```

### `scroll`

```python
def scroll(self, scrolls: int = 1, frame_size: int = 600, direction: str = 'both', delay: float = .3) -> bool:
    """
    Прокручивает страницу в указанном направлении.

    Args:
        scrolls (int, optional): Количество прокруток. По умолчанию 1.
        frame_size (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
        direction (str, optional): Направление прокрутки ('both', 'down', 'up'). По умолчанию 'both'.
        delay (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.

    Returns:
        bool: `True`, если прокрутка выполнена успешно, `False` в случае ошибки.
    """
```

**Описание**:
Прокручивает страницу в заданном направлении на указанное количество прокруток с заданной задержкой между ними.

**Параметры**:
- `scrolls` (int, optional): Количество прокруток. По умолчанию 1.
- `frame_size` (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
- `direction` (str, optional): Направление прокрутки ('both', 'down', 'up'). По умолчанию 'both'.
- `delay` (float, optional): Задержка между прокрутками в секундах. По умолчанию 0.3.

**Возвращает**:
- `bool`: `True`, если прокрутка выполнена успешно, `False` в случае ошибки.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get_url('https://example.com')
driver.scroll(scrolls=2, direction='down')
```

### `locale`

```python
@property
def locale(self) -> Optional[str]:
    """
    Определяет язык страницы на основе мета-тегов или JavaScript.

    Returns:
        Optional[str]: Языковой код, если найден, иначе `None`.
    """
```

**Описание**:
Определяет язык страницы, анализируя мета-теги и выполняя JavaScript-код.

**Возвращает**:
- `Optional[str]`: Языковой код, если найден, иначе `None`.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get_url('https://example.com')
language = driver.locale
print(language)
```

### `get_url`

```python
def get_url(self, url: str) -> bool:
    """
    Переходит по указанному URL и сохраняет текущие URL и куки.

    Args:
        url (str): URL для перехода.

    Returns:
        bool: `True`, если навигация выполнена успешно, `False` в случае ошибки.
    """
```

**Описание**:
Переходит по указанному URL, сохраняет текущий URL, предыдущий URL и куки.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `bool`: `True`, если навигация выполнена успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `WebDriverException`: Если возникла ошибка при навигации.
- `InvalidArgumentException`: Если URL имеет неверный формат.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
success = driver.get_url('https://example.com')
if success:
    print('Navigation successful')
else:
    print('Navigation failed')
```

### `window_open`

```python
def window_open(self, url: Optional[str] = None) -> None:
    """
    Открывает новую вкладку в браузере.

    Args:
        url (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию `None`.
    """
```

**Описание**:
Открывает новую вкладку в браузере и переключается на неё. Если указан URL, открывает его в новой вкладке.

**Параметры**:
- `url` (Optional[str], optional): URL для открытия в новой вкладке. По умолчанию `None`.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.window_open('https://example.com')
```

### `wait`

```python
def wait(self, delay: float = .3) -> None:
    """
    Ожидает указанное время.

    Args:
        delay (float, optional): Время ожидания в секундах. По умолчанию 0.3.
    """
```

**Описание**:
Приостанавливает выполнение на указанное количество секунд.

**Параметры**:
- `delay` (float, optional): Время ожидания в секундах. По умолчанию 0.3.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get_url('https://example.com')
driver.wait(2)  # Ожидание 2 секунды
```

### `_save_cookies_localy`

```python
def _save_cookies_localy(self) -> None:
    """
    Сохраняет куки веб-драйвера в локальный файл.
    """
```

**Описание**:
Сохраняет текущие куки веб-драйвера в локальный файл.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
driver.get_url('https://example.com')
driver._save_cookies_localy()
```

### `fetch_html`

```python
def fetch_html(self, url: str) -> Optional[bool]:
    """
    Получает HTML-контент из файла или веб-страницы.

    Args:
        url (str): URL или путь к файлу для получения HTML-контента.

    Returns:
        Optional[bool]: `True`, если контент успешно получен, `False` в случае ошибки.
    """
```

**Описание**:
Получает HTML-контент из указанного URL или локального файла.

**Параметры**:
- `url` (str): URL или путь к файлу для получения HTML-контента.

**Возвращает**:
- `Optional[bool]`: `True`, если контент успешно получен, `False` в случае ошибки.

**Примеры**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/путь/к/chromedriver')
success = driver.fetch_html('https://example.com')
if success:
    print('HTML content fetched successfully')
else:
    print('Failed to fetch HTML content')
```