# Модуль `post_event.py`

## Обзор

Модуль предназначен для автоматизации процесса публикации календарных событий в группах Facebook с использованием Selenium WebDriver. Он предоставляет функции для ввода заголовка, даты, времени и описания события, а также отправки события.

## Подробнее

Модуль `post_event.py` содержит функции, которые позволяют автоматизировать процесс создания и публикации событий в Facebook. Он использует библиотеку Selenium для управления веб-браузером и взаимодействия с элементами веб-страницы. Модуль загружает локаторы элементов страницы из JSON-файла, что позволяет легко адаптировать код к изменениям в структуре страницы Facebook. Основное назначение модуля - упростить и ускорить процесс публикации событий, избегая ручного ввода данных.

## Функции

### `post_title`

```python
def post_title(d: Driver, title:str) -> bool:
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

**Как работает функция**:
1. Функция `post_title` принимает объект драйвера `d` и заголовок события `title` в качестве аргументов.
2. Использует метод `execute_locator` объекта драйвера `d` для отправки заголовка события в соответствующее поле на веб-странице. Локатор поля заголовка события берется из `locator.event_title`.
3. Если отправка заголовка не удалась, функция регистрирует ошибку с помощью `logger.error` и возвращает `None`.
4. В случае успешной отправки заголовка функция возвращает `True`.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `title` (str): Заголовок события, который необходимо отправить.

**Возвращает**:
- `bool`: `True`, если заголовок успешно отправлен, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
event = SimpleNamespace(title="Campaign Title", description="Event Description")
post_title(driver, event)
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
    ...
```

**Как работает функция**:
1. Функция `post_date` принимает объект драйвера `d` и дату события `date` в качестве аргументов.
2. Использует метод `execute_locator` объекта драйвера `d` для отправки даты события в соответствующее поле на веб-странице. Локатор поля даты берется из `locator.start_date`.
3. Если отправка даты не удалась, функция регистрирует ошибку с помощью `logger.error` и возвращает `None`.
4. В случае успешной отправки даты функция возвращает `True`.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `date` (str): Дата события, которую необходимо отправить.

**Возвращает**:
- `bool`: `True`, если дата успешно отправлена, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
event = SimpleNamespace(title="Campaign Title", description="Event Description")
post_date(driver, event)
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
    ...
```

**Как работает функция**:
1. Функция `post_time` принимает объект драйвера `d` и время события `time` в качестве аргументов.
2. Использует метод `execute_locator` объекта драйвера `d` для отправки времени события в соответствующее поле на веб-странице. Локатор поля времени берется из `locator.start_time`.
3. Если отправка времени не удалась, функция регистрирует ошибку с помощью `logger.error` и возвращает `None`.
4. В случае успешной отправки времени функция возвращает `True`.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `time` (str): Время события, которое необходимо отправить.

**Возвращает**:
- `bool`: `True`, если время успешно отправлено, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
event = SimpleNamespace(title="Campaign Title", description="Event Description")
post_time(driver, event)
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

**Как работает функция**:
1. Функция `post_description` принимает объект драйвера `d` и описание события `description` в качестве аргументов.
2. Выполняет прокрутку страницы вниз на 300 пикселей с помощью `d.scroll(1,300,'down')`.
3. Использует метод `execute_locator` объекта драйвера `d` для отправки описания события в соответствующее поле на веб-странице. Локатор поля описания берется из `locator.event_description`.
4. Если отправка описания не удалась, функция регистрирует ошибку с помощью `logger.error` и возвращает `None`.
5. В случае успешной отправки описания функция возвращает `True`.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `description` (str): Описание события, которое необходимо отправить.

**Возвращает**:
- `bool`: `True`, если описание успешно отправлено, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
event = SimpleNamespace(title="Campaign Title", description="Event Description")
post_description(driver, event)
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
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]
        >>> promote_post(driver, category, products)
    """
    ...
```

**Как работает функция**:
1. Функция `post_event` принимает объект драйвера `d` и объект события `event` типа `SimpleNamespace` в качестве аргументов.
2. Вызывает функцию `post_title` для отправки заголовка события. Если отправка не удалась, функция возвращает `None`.
3. Разделяет строку `event.start` на дату и время, используя метод `split()`.
4. Вызывает функцию `post_date` для отправки даты события. Если отправка не удалась, функция возвращает `None`.
5. Вызывает функцию `post_time` для отправки времени события. Если отправка не удалась, функция возвращает `None`.
6. Формирует полное описание события, объединяя `event.description` и `event.promotional_link`.
7. Вызывает функцию `post_description` для отправки полного описания события. Если отправка не удалась, функция возвращает `None`.
8. Использует метод `execute_locator` объекта драйвера `d` для отправки события. Локатор кнопки отправки события берется из `locator.event_send`. Если отправка не удалась, функция возвращает `None`.
9. Приостанавливает выполнение программы на 30 секунд с помощью `time.sleep(30)`.
10. Возвращает `True` после успешной отправки события.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `event` (SimpleNamespace): Объект, содержащий данные события, такие как заголовок, дата, время, описание и рекламная ссылка.

**Возвращает**:
- `bool`: `True`, если событие успешно отправлено, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
promote_post(driver, category, products)