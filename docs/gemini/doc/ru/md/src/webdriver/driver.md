# Модуль hypotez/src/webdriver/driver.py

## Обзор

Модуль `hypotez/src/webdriver/driver.py` предоставляет класс `Driver` для работы с веб-драйверами Selenium. Он обеспечивает унифицированный интерфейс для взаимодействия с различными драйверами (например, Chrome, Firefox, Edge), а также предоставляет методы для навигации, прокрутки, работы с куками и обработки исключений.

## Классы

### `Driver`

**Описание**:  Унифицированный класс для работы с Selenium WebDriver. Обеспечивает удобный интерфейс для инициализации, управления и взаимодействия с веб-драйверами.

**Атрибуты**:

* `driver` (selenium.webdriver): Экземпляр Selenium WebDriver.

**Методы**:

#### `__init__(self, webdriver_cls, *args, **kwargs)`

**Описание**: Инициализирует экземпляр класса `Driver`.

**Параметры**:

* `webdriver_cls` (type): Класс WebDriver (например, `Chrome`).
* `*args`: Позиционные аргументы для драйвера.
* `**kwargs`: Ключевые аргументы для драйвера.

**Пример**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

#### `__init_subclass__(cls, *, browser_name=None, **kwargs)`

**Описание**: Автоматически вызывается при создании подкласса `Driver`.

**Параметры**:

* `browser_name` (str, optional): Имя браузера. Обязательно для подклассов.
* `**kwargs`: Дополнительные аргументы.

**Исключения**:

* `ValueError`: Если `browser_name` не указан.


#### `__getattr__(self, item)`

**Описание**: Прокси для доступа к атрибутам драйвера.

**Параметры**:

* `item` (str): Имя атрибута.

**Пример**:

```python
driver.current_url
```


#### `scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)`

**Описание**: Прокручивает страницу в указанном направлении.

**Параметры**:

* `scrolls` (int, optional): Количество прокруток. По умолчанию 1.
* `frame_size` (int, optional): Размер прокрутки в пикселях. По умолчанию 600.
* `direction` (str, optional): Направление ('both', 'down', 'up'). По умолчанию 'both'.
* `delay` (float, optional): Задержка между прокрутками. По умолчанию 0.3.

**Возвращает**:

* `bool`: `True`, если прокрутка успешна, иначе `False`.

**Пример**:

```python
driver.scroll(scrolls=3, direction='down')
```

#### `get_url(self, url: str) -> bool`

**Описание**: Переходит по указанному URL.

**Параметры**:

* `url` (str): URL для перехода.

**Возвращает**:

* `bool`: `True`, если переход успешен, `False` в противном случае.

**Исключения**:

* `WebDriverException`: Ошибка с WebDriver.
* `InvalidArgumentException`: Некорректный URL.
* `Exception`: Любые другие ошибки.

#### `window_open(self, url: Optional[str] = None) -> None`

**Описание**: Открывает новую вкладку и переходит по URL (если указан).

**Параметры**:

* `url` (Optional[str], optional): URL для новой вкладки. По умолчанию None.

#### `wait(self, delay: float = .3) -> None`

**Описание**: Ожидает указанное количество времени.

**Параметры**:

* `delay` (float, optional): Время задержки в секундах. По умолчанию 0.3.

#### `_save_cookies_localy(self) -> None`

**Описание**: Сохраняет куки в локальный файл.

**Возвращает**:

* `None`

**Исключения**:

* `Exception`: Любые ошибки при сохранении.

#### `fetch_html(self, url: str) -> Optional[bool]`

**Описание**: Извлекает HTML-контент из файла или веб-страницы.

**Параметры**:

* `url` (str): Путь к файлу или URL.

**Возвращает**:

* `Optional[bool]`: `True`, если контент успешно извлечён, иначе `None`.

**Исключения**:

* `Exception`: Любые ошибки при извлечении контента.


## Функции

(Нет функций в этом модуле)


## Логирование

Модуль использует модуль `logger` для логирования ошибок и информации.


## Обработка исключений

Блоки `try...except` используются для обработки различных исключений, таких как `WebDriverException`, `InvalidArgumentException` и других, с последующим логированием ошибок.


## Зависимости

Модуль использует библиотеки `selenium`, `copy`, `pickle`, `time`, `re`, `pathlib`, `typing`, `header`, `gs`, `logger`, и `logger.exceptions`.