# Модуль `post_event.py`

## Обзор

Модуль предназначен для автоматизации процесса публикации календарных событий в группах Facebook с использованием Selenium WebDriver. Он содержит функции для ввода заголовка, даты, времени и описания события, а также для отправки события.

## Подробней

Модуль предоставляет набор функций, которые взаимодействуют с веб-страницей Facebook через Selenium WebDriver. Он использует локаторы, хранящиеся в JSON-файле, для поиска элементов на странице и выполнения действий, таких как ввод текста и нажатие кнопок. Модуль предназначен для упрощения процесса создания и публикации событий в Facebook группах, что может быть полезно для автоматизации маркетинговых кампаний и продвижения мероприятий.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `post_title`

```python
def post_title(d: Driver, title: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...
```

**Назначение**: Отправляет заголовок события на веб-страницу.

**Параметры**:

-   `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
-   `title` (str): Заголовок события, который нужно отправить.

**Возвращает**:

-   `bool`: `True`, если заголовок успешно отправлен, иначе `None`.

**Как работает функция**:

1.  Пытается отправить заголовок события, используя локатор `locator.event_title` и метод `execute_locator` драйвера.
2.  Если отправка не удалась, регистрирует ошибку с помощью `logger.error` и возвращает `None`.
3.  В случае успешной отправки возвращает `True`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Создание экземпляра драйвера (пример с Firefox)
driver = Driver(Firefox)

# Создание объекта SimpleNamespace с данными события
event = SimpleNamespace(title="Заголовок кампании", description="Описание события")

# Вызов функции post_title
result = post_title(driver, event.title)

# Вывод результата
print(result)  # Выведет: True или None в случае ошибки
```

### `post_date`

```python
def post_date(d: Driver, date: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...
```

**Назначение**: Отправляет дату события на веб-страницу.

**Параметры**:

-   `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
-   `date` (str): Дата события, которую нужно отправить.

**Возвращает**:

-   `bool`: `True`, если дата успешно отправлена, иначе `None`.

**Как работает функция**:

1.  Пытается отправить дату события, используя локатор `locator.start_date` и метод `execute_locator` драйвера.
2.  Если отправка не удалась, регистрирует ошибку с помощью `logger.error` и возвращает `None`.
3.  В случае успешной отправки возвращает `True`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Создание экземпляра драйвера (пример с Firefox)
driver = Driver(Firefox)

# Создание объекта SimpleNamespace с данными события
event = SimpleNamespace(start="2024-01-01 12:00")
date = event.start.split()[0]

# Вызов функции post_date
result = post_date(driver, date)

# Вывод результата
print(result)  # Выведет: True или None в случае ошибки
```

### `post_time`

```python
def post_time(d: Driver, time: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...
```

**Назначение**: Отправляет время события на веб-страницу.

**Параметры**:

-   `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
-   `time` (str): Время события, которое нужно отправить.

**Возвращает**:

-   `bool`: `True`, если время успешно отправлено, иначе `None`.

**Как работает функция**:

1.  Пытается отправить время события, используя локатор `locator.start_time` и метод `execute_locator` драйвера.
2.  Если отправка не удалась, регистрирует ошибку с помощью `logger.error` и возвращает `None`.
3.  В случае успешной отправки возвращает `True`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Создание экземпляра драйвера (пример с Firefox)
driver = Driver(Firefox)

# Создание объекта SimpleNamespace с данными события
event = SimpleNamespace(start="2024-01-01 12:00")
time = event.start.split()[1]

# Вызов функции post_time
result = post_time(driver, time)

# Вывод результата
print(result)  # Выведет: True или None в случае ошибки
```

### `post_description`

```python
def post_description(d: Driver, description: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
    ...
```

**Назначение**: Отправляет описание события на веб-страницу.

**Параметры**:

-   `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
-   `description` (str): Описание события, которое нужно отправить.

**Возвращает**:

-   `bool`: `True`, если описание успешно отправлено, иначе `None`.

**Как работает функция**:

1.  Прокручивает страницу вниз на 300 пикселей.
2.  Пытается отправить описание события, используя локатор `locator.event_description` и метод `execute_locator` драйвера.
3.  Если отправка не удалась, регистрирует ошибку с помощью `logger.error` и возвращает `None`.
4.  В случае успешной отправки возвращает `True`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Создание экземпляра драйвера (пример с Firefox)
driver = Driver(Firefox)

# Создание объекта SimpleNamespace с данными события
event = SimpleNamespace(description="Описание события")

# Вызов функции post_description
result = post_description(driver, event.description)

# Вывод результата
print(result)  # Выведет: True или None в случае ошибки
```

### `post_event`

```python
def post_event(d: Driver, event: SimpleNamespace) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    ...
```

**Назначение**: Управляет процессом публикации события, включая отправку заголовка, даты, времени и описания.

**Параметры**:

-   `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
-   `event` (SimpleNamespace): Объект, содержащий данные события (заголовок, дату, время, описание и ссылку).

**Возвращает**:

-   `bool`: `True`, если все этапы публикации прошли успешно, иначе `None`.

**Как работает функция**:

1.  Отправляет заголовок события, вызывая функцию `post_title`. Если отправка не удалась, возвращает `None`.
2.  Разделяет дату и время из атрибута `event.start`.
3.  Отправляет дату события, вызывая функцию `post_date`. Если отправка не удалась, возвращает `None`.
4.  Отправляет время события, вызывая функцию `post_time`. Если отправка не удалась, возвращает `None`.
5.  Отправляет описание события, вызывая функцию `post_description`, добавляя рекламную ссылку к описанию. Если отправка не удалась, возвращает `None`.
6.  Нажимает кнопку отправки события, используя локатор `locator.event_send` и метод `execute_locator` драйвера. Если нажатие не удалось, возвращает `None`.
7.  Приостанавливает выполнение на 30 секунд.
8.  Возвращает `True`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Создание экземпляра драйвера (пример с Firefox)
driver = Driver(Firefox)

# Создание объекта SimpleNamespace с данными события
event = SimpleNamespace(
    title="Заголовок кампании",
    start="2024-01-01 12:00",
    description="Описание события",
    promotional_link="https://example.com"
)

# Вызов функции post_event
result = post_event(driver, event)

# Вывод результата
print(result)  # Выведет: True или None в случае ошибки
```

## ASCII flowchart

```
A: post_event (driver, event)
|
|-- B: post_title (driver, event.title)
|   |
|   `-- Возвращает None, если не удалось отправить заголовок
|
|-- C: Разделение event.start на дату и время
|
|-- D: post_date (driver, dt)
|   |
|   `-- Возвращает None, если не удалось отправить дату
|
|-- E: post_time (driver, tm)
|   |
|   `-- Возвращает None, если не удалось отправить время
|
|-- F: post_description (driver, f"{event.description}\n{event.promotional_link}")
|   |
|   `-- Возвращает None, если не удалось отправить описание
|
|-- G: driver.execute_locator (locator.event_send)
|   |
|   `-- Возвращает None, если не удалось нажать кнопку отправки
|
|-- H: time.sleep(30)
|
`-- Возвращает True