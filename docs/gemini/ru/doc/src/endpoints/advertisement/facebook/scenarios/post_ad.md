# Модуль `hypotez/src/endpoints/advertisement/facebook/scenarios/post_ad.py`

## Обзор

Модуль `post_ad.py` содержит функцию `post_ad`, предназначенную для публикации рекламного объявления в группе Facebook. Функция взаимодействует с веб-драйвером, используя функции из других модулей для отправки заголовка объявления, загрузки медиафайла (если он есть) и публикации объявления.

## Оглавление

* [Функции](#функции)


## Функции

### `post_ad`

**Описание**: Функция `post_ad` публикует рекламное объявление в группе Facebook. Она принимает веб-драйвер и объект `SimpleNamespace`, содержащий данные объявления.

**Параметры**:

- `d` (Driver): Экземпляр веб-драйвера для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Объект, содержащий данные объявления (описание, путь к изображению (необязательно)).

**Возвращает**:

- `bool`: `True`, если объявление было успешно опубликовано, иначе `None`.

**Вызывает исключения**:

- Возможны исключения, генерируемые функциями `post_message_title`, `upload_post_media`, и `message_publish`.  Обработка исключений выполняется внутри функции `post_ad` с использованием `try...except` блоков.


**Детали**:

Функция `post_ad` последовательно выполняет следующие действия:

1. Отправляет заголовок объявления (используя `post_message_title`).
2. Если указан путь к изображению, загружает его (используя `upload_post_media`).
3. Публикует объявление (используя `message_publish`).
4. Обнуляет счетчик неудачных попыток (`fails`).
5. Возвращает `True` в случае успешной публикации объявления.


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

    # ... (код функции)
```