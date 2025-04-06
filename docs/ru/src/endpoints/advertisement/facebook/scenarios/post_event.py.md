# Модуль `post_event.py`

## Обзор

Модуль предназначен для публикации календарных событий в группах Facebook с использованием Selenium WebDriver. Он содержит функции для отправки заголовка, даты, времени и описания события, а также функцию `post_event`, которая управляет всем процессом публикации.

## Подробней

Этот модуль является частью системы автоматизации постинга рекламы в Facebook. Он использует драйвер веб-браузера для взаимодействия с веб-интерфейсом Facebook и заполнения необходимых полей для создания события. Модуль загружает локаторы веб-элементов из JSON-файла для обеспечения гибкости и удобства обслуживания.

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
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `title` (str): Заголовок события, который необходимо отправить.

**Возвращает**:
- `bool`: `True`, если заголовок успешно отправлен, иначе `None`.

**Как работает функция**:
1. Пытается отправить заголовок события, используя локатор `locator.event_title`.
2. Если отправка не удалась, записывает сообщение об ошибке в лог.

```ascii
Начало
  │
  ├── Отправка заголовка события (d.execute_locator)
  │
  ├── Успех: Вернуть True
  │
  └── Неудача: Логирование ошибки и возврат None
  │
Конец
```

**Примеры**:

```python
driver = Driver(Firefox)
title = "Заголовок события"
result = post_title(driver, title)
print(result)
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
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `date` (str): Дата события, которую необходимо отправить.

**Возвращает**:
- `bool`: `True`, если дата успешно отправлена, иначе `None`.

**Как работает функция**:
1. Пытается отправить дату события, используя локатор `locator.start_date`.
2. Если отправка не удалась, записывает сообщение об ошибке в лог.

```ascii
Начало
  │
  ├── Отправка даты события (d.execute_locator)
  │
  ├── Успех: Вернуть True
  │
  └── Неудача: Логирование ошибки и возврат None
  │
Конец
```

**Примеры**:

```python
driver = Driver(Firefox)
date = "2024-01-01"
result = post_date(driver, date)
print(result)
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
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `time` (str): Время события, которое необходимо отправить.

**Возвращает**:
- `bool`: `True`, если время успешно отправлено, иначе `None`.

**Как работает функция**:
1. Пытается отправить время события, используя локатор `locator.start_time`.
2. Если отправка не удалась, записывает сообщение об ошибке в лог.

```ascii
Начало
  │
  ├── Отправка времени события (d.execute_locator)
  │
  ├── Успех: Вернуть True
  │
  └── Неудача: Логирование ошибки и возврат None
  │
Конец
```

**Примеры**:

```python
driver = Driver(Firefox)
time = "10:00"
result = post_time(driver, time)
print(result)
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
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `description` (str): Описание события, которое необходимо отправить.

**Возвращает**:
- `bool`: `True`, если описание успешно отправлено, иначе `None`.

**Как работает функция**:
1. Прокручивает страницу вниз.
2. Пытается отправить описание события, используя локатор `locator.event_description`.
3. Если отправка не удалась, записывает сообщение об ошибке в лог.

```ascii
Начало
  │
  ├── Прокрутка страницы вниз (d.scroll)
  │
  ├── Отправка описания события (d.execute_locator)
  │
  ├── Успех: Вернуть True
  │
  └── Неудача: Логирование ошибки и возврат None
  │
Конец
```

**Примеры**:

```python
driver = Driver(Firefox)
description = "Описание события"
result = post_description(driver, description)
print(result)
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
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `event` (SimpleNamespace): Объект, содержащий информацию о событии, такую как заголовок, дата, время и описание.

**Возвращает**:
- `bool`: `True`, если публикация события прошла успешно, иначе `None`.

**Как работает функция**:
1. Отправляет заголовок события, вызывая функцию `post_title`.
2. Разбивает строку даты и времени события на отдельные значения.
3. Отправляет дату события, вызывая функцию `post_date`.
4. Отправляет время события, вызывая функцию `post_time`.
5. Отправляет описание события, вызывая функцию `post_description`.
6. Отправляет событие, используя локатор `locator.event_send`.
7. Делает паузу на 30 секунд.

```ascii
Начало
  │
  ├── Отправка заголовка (post_title)
  │
  ├── Разделение даты и времени
  │
  ├── Отправка даты (post_date)
  │
  ├── Отправка времени (post_time)
  │
  ├── Отправка описания (post_description)
  │
  ├── Отправка события (d.execute_locator)
  │
  ├── Пауза (time.sleep)
  │
Конец
```

**Примеры**:

```python
driver = Driver(Firefox)
event = SimpleNamespace(
    title="Заголовок события",
    start="2024-01-01 10:00",
    description="Описание события",
    promotional_link="https://example.com"
)
result = post_event(driver, event)
print(result)