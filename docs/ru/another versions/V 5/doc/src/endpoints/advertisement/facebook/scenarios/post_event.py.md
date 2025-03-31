# Модуль `post_event`

## Обзор

Модуль предназначен для автоматизации процесса публикации календарных событий в группах Facebook с использованием Selenium WebDriver. Он содержит функции для заполнения полей заголовка, даты, времени и описания события, а также для отправки события.

## Подробней

Этот модуль предоставляет набор функций, автоматизирующих процесс создания и публикации событий в Facebook. Он использует Selenium WebDriver для управления браузером и взаимодействия с элементами веб-страницы.  Модуль загружает локаторы элементов страницы из JSON-файла для обеспечения гибкости и упрощения обслуживания.

## Функции

### `post_title`

```python
def post_title(d: Driver, title:str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        title (str): Заголовок события.

    Returns:
        bool: `True`, если заголовок успешно отправлен, иначе `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет заголовок события на веб-страницу.

**Как работает функция**:
Функция `post_title` принимает экземпляр драйвера Selenium (`d`) и заголовок события (`title`) в качестве аргументов. Она использует метод `execute_locator` драйвера для отправки заголовка в элемент, найденный по локатору `locator.event_title`. Если отправка не удалась, функция логирует ошибку и возвращает `None`. В случае успешной отправки возвращается `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium.
- `title` (str): Заголовок события для отправки.

**Возвращает**:
- `bool`: `True`, если заголовок успешно отправлен, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
title = "Заголовок события"
result = post_title(driver, title)
print(result)  # Выведет: True или None в случае ошибки
```

### `post_date`

```python
def post_date(d: Driver, date:str) -> bool:
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
```

**Описание**: Отправляет дату события на веб-страницу.

**Как работает функция**:
Функция `post_date` принимает экземпляр драйвера Selenium (`d`) и дату события (`date`) в качестве аргументов. Она использует метод `execute_locator` драйвера для отправки даты в элемент, найденный по локатору `locator.start_date`. Если отправка не удалась, функция логирует ошибку и возвращает `None`. В случае успешной отправки возвращается `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium.
- `date` (str): Дата события для отправки.

**Возвращает**:
- `bool`: `True`, если дата успешно отправлена, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
date = "2024-01-01"
result = post_date(driver, date)
print(result)  # Выведет: True или None в случае ошибки
```

### `post_time`

```python
def post_time(d: Driver, time:str) -> bool:
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
```

**Описание**: Отправляет время события на веб-страницу.

**Как работает функция**:
Функция `post_time` принимает экземпляр драйвера Selenium (`d`) и время события (`time`) в качестве аргументов. Она использует метод `execute_locator` драйвера для отправки времени в элемент, найденный по локатору `locator.start_time`. Если отправка не удалась, функция логирует ошибку и возвращает `None`. В случае успешной отправки возвращается `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium.
- `time` (str): Время события для отправки.

**Возвращает**:
- `bool`: `True`, если время успешно отправлено, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
time = "10:00"
result = post_time(driver, time)
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
```

**Описание**: Отправляет описание события на веб-страницу.

**Как работает функция**:
Функция `post_description` принимает экземпляр драйвера Selenium (`d`) и описание события (`description`) в качестве аргументов.  Перед отправкой описания выполняется скролл страницы вниз.  Затем используется метод `execute_locator` драйвера для отправки описания в элемент, найденный по локатору `locator.event_description`. Если отправка не удалась, функция логирует ошибку и возвращает `None`. В случае успешной отправки возвращается `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium.
- `description` (str): Описание события для отправки.

**Возвращает**:
- `bool`: `True`, если описание успешно отправлено, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
description = "Описание события"
result = post_description(driver, description)
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
```

**Описание**: Управляет процессом публикации события, включая заголовок, дату, время и описание.

**Как работает функция**:
Функция `post_event` принимает экземпляр драйвера Selenium (`d`) и объект `event` типа `SimpleNamespace`, содержащий данные события.  Она последовательно вызывает функции `post_title`, `post_date`, `post_time` и `post_description` для заполнения соответствующих полей на веб-странице.  Затем нажимает на элемент, найденный по локатору `locator.event_send`. После этого происходит ожидание в 30 секунд. Если какая-либо из операций не удалась, функция немедленно возвращает `None`. В случае успешного выполнения всех операций возвращается `True`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера Selenium.
- `event` (SimpleNamespace): Объект, содержащий данные события (заголовок, дату, время, описание и рекламную ссылку).

**Возвращает**:
- `bool`: `True`, если все операции выполнены успешно, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
event = SimpleNamespace(
    title="Заголовок события",
    start="2024-01-01 10:00",
    description="Описание события",
    promotional_link="https://example.com"
)
result = post_event(driver, event)
print(result)  # Выведет: True или None в случае ошибки