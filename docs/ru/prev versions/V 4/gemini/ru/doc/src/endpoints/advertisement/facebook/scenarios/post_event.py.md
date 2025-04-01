# Модуль `post_event`

## Обзор

Модуль `post_event` предназначен для автоматизации процесса публикации событий в группах Facebook с использованием Selenium WebDriver. Он содержит функции для отправки заголовка, даты, времени и описания события. Модуль использует локаторы, определенные в JSON-файле, для взаимодействия с элементами веб-страницы.

## Подробней

Этот модуль является частью системы автоматизации маркетинговых кампаний в Facebook. Он предоставляет функции для программного заполнения и отправки форм создания событий, что позволяет автоматизировать процесс публикации объявлений и экономить время.

## Функции

### `post_title`

```python
def post_title(d: Driver, title: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        title (str): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет заголовок события.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `title` (str): Заголовок события.

**Возвращает**:
- `bool`: `True`, если заголовок был успешно отправлен, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
title = "Заголовок события"
post_title(driver, title)
```

### `post_date`

```python
def post_date(d: Driver, date: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        date (str): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет дату события.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `date` (str): Дата события.

**Возвращает**:
- `bool`: `True`, если дата была успешно отправлена, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
date = "2024-01-01"
post_date(driver, date)
```

### `post_time`

```python
def post_time(d: Driver, time: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        time (str): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет время события.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `time` (str): Время события.

**Возвращает**:
- `bool`: `True`, если время было успешно отправлено, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
time = "10:00"
post_time(driver, time)
```

### `post_description`

```python
def post_description(d: Driver, description: str) -> bool:
    """ Sends the title of event.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        description (str): The event containing the title, data of event and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Event Description")
        >>> post_title(driver, event)
        True
    """
```

**Описание**: Отправляет описание события.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `description` (str): Описание события.

**Возвращает**:
- `bool`: `True`, если описание было успешно отправлено, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
description = "Описание события"
post_description(driver, description)
```

### `post_event`

```python
def post_event(d: Driver, event: SimpleNamespace) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        event (SimpleNamespace): The category details used for the post title and description.

    Returns:
        bool: `True` if the event was successfully posted, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> event = SimpleNamespace(title="Campaign Title", description="Campaign Description", start="2024-01-01 10:00", promotional_link="https://example.com")
        >>> post_event(driver, event)
    """
```

**Описание**: Управляет процессом публикации события, включая заголовок, дату, время и описание.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `event` (SimpleNamespace): Объект, содержащий детали события (заголовок, описание, дата, время, рекламная ссылка).

**Возвращает**:
- `bool`: `True`, если событие было успешно опубликовано, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
event = SimpleNamespace(title="Заголовок события", description="Описание события", start="2024-01-01 10:00", promotional_link="https://example.com")
post_event(driver, event)
```