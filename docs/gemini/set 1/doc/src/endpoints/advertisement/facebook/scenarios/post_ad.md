# Модуль `hypotez/src/endpoints/advertisement/facebook/scenarios/post_ad.py`

## Обзор

Модуль `post_ad.py` содержит функцию `post_ad`, предназначенную для публикации рекламных сообщений в группах Facebook.  Функция использует драйвер Selenium, загружает локаторы из JSON-файла и взаимодействует с интерфейсом Facebook для отправки заголовка, медиафайла (если указан) и публикации сообщения.

## Оглавление

- [Функции](#функции)


## Функции

### `post_ad`

**Описание**: Функция `post_ad` публикует рекламное сообщение в группе Facebook.  Она принимает драйвер Selenium и объект `SimpleNamespace` с данными сообщения, включая заголовок, описание и, опционально, путь к изображению.


**Параметры**:

- `d` (Driver): Экземпляр драйвера Selenium, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Объект `SimpleNamespace` содержащий данные сообщения.  Ожидаются атрибуты `description`, а также, опционально, `image_path`.


**Возвращает**:

- `bool`: `True`, если сообщение было опубликовано успешно; `None`, если произошла ошибка.


**Обработка исключений**:

- Возможные исключения (ошибки) обрабатываются внутри функции, записывая сообщения об ошибках в лог.  Для обработки ошибок используется `try-except`.


**Подробное описание реализации**:

Функция `post_ad` вызывает функции `post_message_title`, `upload_post_media` и `message_publish` для последовательной отправки заголовка, загрузки медиа (если приложено) и публикации сообщения. При обнаружении ошибки в процессе, функция возвращает `None`. Подробные параметры и возвращаемые значения функций-помощников (`post_message_title`, `upload_post_media`, `message_publish`) определены в их собственных документациях.

```python
def post_ad(d: Driver, message:SimpleNamespace) -> bool:
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
    global fails

    if not post_message_title(d, f"{ message.description}" ):
        logger.error("Failed to send event title", exc_info=False)
        fails += 1
        if fails < 15:
            print(f"{fails=}")
            return
        else:
            ...

    time.sleep(1)
    if hasattr(message, 'image_path') and message.image_path:
        if not upload_post_media(d, media = message.image_path, without_captions = True):
            return

    if not message_publish(d):
        return
    fails = 0
    return True
```