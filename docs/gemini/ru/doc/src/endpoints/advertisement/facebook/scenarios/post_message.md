# Модуль `hypotez/src/endpoints/advertisement/facebook/scenarios/post_message.py`

## Обзор

Данный модуль содержит функции для публикации сообщений на Facebook. Он предоставляет инструменты для добавления заголовка и описания, загрузки медиафайлов и публикации готового поста. Модуль использует Selenium WebDriver для взаимодействия с веб-сайтом Facebook.

## Оглавление

- [Функция `post_title`](#функция-post_title)
- [Функция `upload_media`](#функция-upload_media)
- [Функция `update_images_captions`](#функция-update_images_captions)
- [Функция `publish`](#функция-publish)
- [Функция `promote_post`](#функция-promote_post)
- [Функция `post_message`](#функция-post_message)


## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле для публикации сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace | str):  Информация о сообщении, включающая заголовок и описание. Может быть строкой (для простого текста), либо объектом `SimpleNamespace` с атрибутами `title` и `description`.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.


### `upload_media`

**Описание**: Загружает медиафайлы (изображения, видео) в раздел поста и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]):  Медиафайлы для загрузки. Может быть списком объектов `SimpleNamespace` с атрибутом `local_saved_image` (путь к изображению) или `local_saved_video` (путь к видео), строкой (для загрузки одиночного файла), или списком строк (для загрузки нескольких файлов).
- `no_video` (bool, optional): Флаг, указывающий на отсутствие загрузки видео. По умолчанию `False`.
- `without_captions` (bool, optional): Флаг, указывающий на отсутствие необходимости в обновлении подписей. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были загружены успешно, иначе `None`.

**Вызывает исключения**:
- `Exception`: Возникает, если произошла ошибка во время загрузки или обновления подписей.


### `update_images_captions`

**Описание**: Добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера.
- `media` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, содержащих данные для описаний.
- `textarea_list` (List[WebElement]): Список элементов `textarea`, где будут добавляться подписи.

**Вызывает исключения**:
- `Exception`: Возникает, если произошла ошибка при обновлении подписей.


### `publish`

**Описание**: Публикует пост.

**Параметры**:
- `d` (Driver): Экземпляр драйвера.
- `attempts` (int, optional): Максимальное количество попыток публикации. По умолчанию 5.

**Возвращает**:
- `bool`: `True`, если пост опубликован, иначе `None`.

**Примечание**: Функция имеет рекурсивную структуру для обработки возможных ошибок при публикации.


### `promote_post`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера.
- `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий заголовок и описание.
- `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace` с медиафайлами и деталями.
- `no_video` (bool, optional): Флаг, указывающий на отсутствие видео. По умолчанию `False`.

**Примеры**:
```python
>>> driver = Driver(...)
>>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
>>> products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
>>> promote_post(driver, category, products)
```


### `post_message`

**Описание**: Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера.
- `message` (SimpleNamespace): Объект `SimpleNamespace` с деталями сообщения.
- `no_video` (bool, optional): Флаг, указывающий на отсутствие видео. По умолчанию `False`.
- `images` (Optional[str | list[str]], optional): Путь к изображению или список путей к изображениям. По умолчанию `None`.
- `without_captions` (bool, optional): Флаг, указывающий на отсутствие необходимости в обновлении подписей. По умолчанию `False`.

**Примеры**:
```python
>>> driver = Driver(...)
>>> message = SimpleNamespace(title="Campaign Title", description="Campaign Description", products=[SimpleNamespace(local_saved_image='path/to/image.jpg')])
>>> post_message(driver, message)
```