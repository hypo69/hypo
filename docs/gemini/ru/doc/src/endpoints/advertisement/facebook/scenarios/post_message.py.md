# Модуль `post_message.py`

## Обзор

Модуль `post_message.py` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление текста, загрузку медиафайлов и обновление подписей к изображениям.

## Содержание

1. [Функции](#Функции)
    - [`post_title`](#post_title)
    - [`upload_media`](#upload_media)
    - [`update_images_captions`](#update_images_captions)
    - [`publish`](#publish)
    - [`promote_post`](#promote_post)
    - [`post_message`](#post_message)

## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле сообщения.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (`SimpleNamespace | str`): Объект с заголовком и описанием для отправки или строка сообщения.

**Возвращает**:
- `bool | None`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Пример**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
post_title(driver, category)
True
```

### `upload_media`

**Описание**: Загружает медиафайлы в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (`SimpleNamespace | List[SimpleNamespace] | str | list[str]`): Список объектов продуктов, содержащих пути к медиафайлам, или список путей к файлам.
- `no_video` (`bool`, optional): Если `True`, то не загружает видео. По умолчанию `False`.
- `without_captions` (`bool`, optional): Если `True`, то не обновляет подписи. По умолчанию `False`.

**Возвращает**:
- `bool | None`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке медиа или обновлении подписи.

**Пример**:
```python
driver = Driver(...)
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
upload_media(driver, products)
True
```

### `update_images_captions`

**Описание**: Добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (`List[SimpleNamespace]`): Список продуктов с деталями для обновления.
- `textarea_list` (`List[WebElement]`): Список полей ввода, куда добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей к медиафайлам.

### `publish`

**Описание**: Публикует сообщение.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `attempts` (`int`, optional): Количество попыток публикации. По умолчанию `5`.

**Возвращает**:
- `bool | None`: `True`, если сообщение было успешно опубликовано, иначе `None`.

### `promote_post`

**Описание**: Управляет процессом продвижения сообщения с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (`SimpleNamespace`): Детали категории, используемые для заголовка и описания сообщения.
- `products` (`List[SimpleNamespace]`): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (`bool`, optional): Если `True`, то не загружает видео. По умолчанию `False`.

**Пример**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
promote_post(driver, category, products)
```

### `post_message`

**Описание**: Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (`SimpleNamespace`): Детали сообщения, используемые для заголовка и описания сообщения.
- `no_video` (`bool`, optional): Если `True`, то не загружает видео. По умолчанию `False`.
- `images` (`Optional[str | list[str]]`, optional): Путь к изображению или список путей к изображениям. По умолчанию `None`.
- `without_captions` (`bool`, optional): Если `True`, то не обновляет подписи. По умолчанию `False`.

**Возвращает**:
- `bool | None`: `True`, если сообщение было успешно опубликовано, иначе `None`.

**Пример**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
promote_post(driver, category, products)
```