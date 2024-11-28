# Модуль hypotez/src/endpoints/advertisement/facebook/scenarios/post_message.py

## Обзор

Этот модуль предоставляет функции для публикации сообщений на Facebook через Selenium WebDriver. Он включает в себя функции для добавления заголовка и описания сообщения, загрузки медиа-файлов (изображений и видео) и публикации сообщения.  Модуль использует `SimpleNamespace` для передачи данных и `Driver`-объект для взаимодействия с веб-страницей.

## Оглавление

* [Функция `post_title`](#функция-post_title)
* [Функция `upload_media`](#функция-upload_media)
* [Функция `update_images_captions`](#функция-update_images_captions)
* [Функция `publish`](#функция-publish)
* [Функция `promote_post`](#функция-promote_post)
* [Функция `post_message`](#функция-post_message)


## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле для публикации сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `message` (SimpleNamespace | str): Заголовок и описание в формате SimpleNamespace или строка.


**Возвращает**:
- bool: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
post_title(driver, category)
```

### `upload_media`

**Описание**: Загружает медиа-файлы (изображения и видео) в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Медиа-файлы в формате SimpleNamespace, списке SimpleNamespace, строке или списке строк.
- `no_video` (bool, optional):  Флаг, запрещающий загрузку видео. По умолчанию `False`.
- `without_captions` (bool, optional): Флаг, чтобы пропустить обновление подписей к изображениям. По умолчанию `False`.


**Возвращает**:
- bool: `True`, если медиа-файлы были загружены успешно, иначе `None`.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках во время загрузки или обновления подписей.

**Примеры**:
```python
driver = Driver(...)
products = [SimpleNamespace(local_saved_image='path/to/image.jpg')]
upload_media(driver, products)
```


### `update_images_captions`

**Описание**: Добавляет описания к загруженным медиа-файлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `media` (List[SimpleNamespace]): Список объектов SimpleNamespace с данными для обновления.
- `textarea_list` (List[WebElement]): Список текстовых областей, куда добавляются подписи.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках во время обновления подписей.

**Примечание**: Использует `local_units` для локализации.

### `publish`

**Описание**: Публикует сообщение.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `attempts` (int, optional): Количество попыток публикации. По умолчанию `5`.

**Возвращает**:
- bool: `True`, если сообщение было опубликовано успешно, иначе `None`.

**Примечание**: Рекурсивно вызывает себя в случае ошибок.

### `promote_post`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиа-файлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории для заголовка и описания.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и данные для публикации.

**Примеры**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_saved_image='path/to/image.jpg')]
promote_post(driver, category, products)
```


### `post_message`

**Описание**: Управляет процессом публикации сообщения с заголовком, описанием, медиа-файлами и опциями.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Детали сообщения для заголовка и описания.
- `no_video` (bool, optional):  Флаг, запрещающий загрузку видео. По умолчанию `False`.
- `images` (Optional[str | list[str]], optional): Путь к изображению или список путей. По умолчанию `None`.
- `without_captions` (bool, optional): Флаг, чтобы пропустить обновление подписей к изображениям. По умолчанию `False`.

**Возвращает**:
- bool: `True`, если сообщение было опубликовано успешно, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
message = SimpleNamespace(title="Campaign Title", description="Campaign Description", products=[SimpleNamespace(local_saved_image='path/to/image.jpg')])
post_message(driver, message)
```

```