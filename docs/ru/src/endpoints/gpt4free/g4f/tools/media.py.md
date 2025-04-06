# Модуль для работы с медиа-контентом

## Обзор

Этот модуль содержит функции для обработки медиа-контента, включая рендеринг изображений и аудио, а также объединение медиа-файлов с сообщениями. Он предоставляет инструменты для преобразования медиа-данных в различные форматы, подходящие для использования в сообщениях и других контекстах.

## Подробней

Модуль предназначен для работы с медиа-файлами, хранящимися в buckets (хранилищах). Он предоставляет функции для рендеринга медиа-контента, объединения медиа-файлов с сообщениями и преобразования медиа-данных в различные форматы, подходящие для использования в сообщениях. Функции модуля используются для обработки медиа-данных, полученных из различных источников, и подготовки их для отображения или воспроизведения.

## Функции

### `render_media`

```python
def render_media(bucket_id: str, name: str, url: str, as_path: bool = False, as_base64: bool = False) -> Union[str, Path]:
    """
    Генерирует путь, base64 или data URI для медиа-файла.

    Args:
        bucket_id (str): ID бакета, в котором находится медиа-файл.
        name (str): Имя медиа-файла.
        url (str): URL медиа-файла.
        as_path (bool, optional): Если `True`, возвращает путь к файлу. По умолчанию `False`.
        as_base64 (bool, optional): Если `True`, возвращает медиа-файл в формате base64. По умолчанию `False`.

    Returns:
        Union[str, Path]: Путь к файлу, base64 представление или data URI медиа-файла.

    Как работает функция:
    1. Проверяет, нужно ли вернуть путь к файлу, base64 представление или data URI.
    2. Если `as_base64` или `as_path` равны `True`, или `url` начинается с "/", формирует путь к файлу.
    3. Если `as_path` равен `True`, возвращает путь к файлу.
    4. Читает содержимое файла.
    5. Кодирует содержимое файла в base64.
    6. Если `as_base64` равен `True`, возвращает base64 представление файла.
    7. Формирует data URI и возвращает его.
    8. Если ни одно из условий не выполнено, возвращает исходный URL.

    ASCII flowchart:
    Проверка условий (as_base64, as_path, url.startswith("/"))
    │
    └───> as_path == True? ───> Вернуть путь к файлу
    │   │
    │   └───> as_base64 == True или url.startswith("/") ───> Формирование пути к файлу ───> Чтение байтов файла ───> Кодирование в base64
    │       │
    │       └───> as_base64 == True? ───> Вернуть base64
    │           │
    │           └───> Формирование data URI ───> Вернуть data URI
    │
    └───> Вернуть URL

    Примеры:
    >>> render_media('test_bucket', 'image.png', 'http://example.com/image.png')
    'http://example.com/image.png'

    >>> render_media('test_bucket', 'image.png', '/media/image.png', as_base64=True)
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
    """
    ...
```

### `render_part`

```python
def render_part(part: dict) -> dict:
    """
    Преобразует часть сообщения в формат, подходящий для рендеринга.

    Args:
        part (dict): Словарь, представляющий часть сообщения.

    Returns:
        dict: Преобразованный словарь с информацией о типе контента и его содержимом.

    Как работает функция:
    1. Проверяет наличие ключа "type" в словаре `part`. Если он есть, возвращает `part` без изменений.
    2. Если ключа "type" нет, пытается получить имя файла из `part`.
    3. Если имя файла отсутствует, формирует путь к директории бакета и читает содержимое бакета, возвращая текстовое сообщение.
    4. Если имя файла присутствует, проверяет, является ли файл аудио.
    5. Если файл является аудио, возвращает словарь с типом "input_audio" и данными в формате base64.
    6. Если файл не является аудио, возвращает словарь с типом "image_url" и URL изображения.

    ASCII flowchart:
    Проверка наличия "type" в part
    │
    └───> "type" in part? ───> Вернуть part
    │
    └───> filename = part.get("name")
        │
        └───> filename is None? ───> Формирование пути к bucket_dir ───> Чтение bucket ───> Вернуть текст
            │
            └───> is_data_an_audio(filename=filename)? ───> Вернуть input_audio с данными в base64
                │
                └───> Вернуть image_url с URL

    Примеры:
    >>> render_part({'bucket_id': 'test_bucket', 'name': 'audio.mp3'})
    {'type': 'input_audio', 'input_audio': {'data': '...', 'format': 'mp3'}}

    >>> render_part({'bucket_id': 'test_bucket', 'name': 'image.png'})
    {'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,...'}}
    """
    ...
```

### `merge_media`

```python
def merge_media(media: list, messages: list) -> Iterator:
    """
    Объединяет медиа-файлы с сообщениями.

    Args:
        media (list): Список медиа-файлов.
        messages (list): Список сообщений.

    Yields:
        Iterator: Итератор медиа-файлов и URL.

    Как работает функция:
    1. Итерируется по списку сообщений.
    2. Если роль сообщения "user", извлекает контент сообщения.
    3. Если контент является списком, итерируется по частям контента.
    4. Если в части контента нет ключа "type" и есть ключ "name", формирует путь к медиа-файлу и добавляет его в буфер.
    5. Если тип части контента "image_url", добавляет URL изображения в буфер.
    6. После обработки сообщений, возвращает медиа-файлы из буфера.
    7. Если `media` не `None`, возвращает медиа-файлы из `media`.

    ASCII flowchart:
    Итерация по сообщениям
    │
    └───> message["role"] == "user"?
        │
        └───> content - list?
            │
            └───> Итерация по частям content
                │
                └───> "type" not in part and "name" in part? ───> Формирование пути к медиа-файлу ───> Добавление в буфер
                    │
                    └───> part["type"] == "image_url"? ───> Добавление URL изображения в буфер
    │
    └───> Возврат буфера
    │
    └───> media is not None? ───> Возврат media

    Примеры:
    >>> messages = [{'role': 'user', 'content': [{'name': 'image.png', 'bucket_id': 'test_bucket'}]}]
    >>> list(merge_media(None, messages))
    [(PosixPath('/path/to/test_bucket/image.png'), 'image.png')]

    >>> messages = [{'role': 'user', 'content': [{'image_url': 'http://example.com/image.png'}]}]
    >>> list(merge_media(None, messages))
    [('http://example.com/image.png', None)]
    """
    ...
```

### `render_messages`

```python
def render_messages(messages: Messages, media: list = None) -> Iterator:
    """
    Рендерит сообщения, объединяя медиа-файлы с контентом.

    Args:
        messages (Messages): Список сообщений.
        media (list, optional): Список медиа-файлов. По умолчанию `None`.

    Yields:
        Iterator: Итератор рендеренных сообщений.

    Как работает функция:
    1. Итерируется по списку сообщений.
    2. Если контент сообщения является списком, рендерит каждую часть контента с помощью функции `render_part`.
    3. Если контент сообщения не является списком и `media` не `None`, объединяет медиа-файлы с контентом сообщения.
    4. Для каждого медиа-файла проверяет, является ли он аудио.
    5. Если файл является аудио, преобразует его в формат `input_audio`.
    6. Если файл не является аудио, преобразует его в формат `image_url`.
    7. Возвращает рендеренные сообщения.

    ASCII flowchart:
    Итерация по сообщениям
    │
    └───> content - list?
        │
        └───> Рендеринг каждой части контента с помощью render_part
    │
    └───> media is not None? ───> Объединение media с контентом сообщения
        │
        └───> Проверка является ли media аудио? ───> Преобразование в формат input_audio
            │
            └───> Преобразование в формат image_url
    │
    └───> Возврат рендеренных сообщений

    Примеры:
    >>> messages = [{'role': 'user', 'content': [{'name': 'image.png', 'bucket_id': 'test_bucket'}]}]
    >>> list(render_messages(messages))
    [{'role': 'user', 'content': [{'image_url': {'url': 'data:image/png;base64,...'}}]}]

    >>> messages = [{'role': 'user', 'content': 'Some text'}]
    >>> media = [('data:audio/mp3;base64,...', 'audio.mp3')]
    >>> list(render_messages(messages, media))
    [{'role': 'user', 'content': [{'input_audio': {'data': 'data:audio/mp3;base64,...', 'format': 'mp3'}}, {'text': 'Some text'}]}]
    """
    ...