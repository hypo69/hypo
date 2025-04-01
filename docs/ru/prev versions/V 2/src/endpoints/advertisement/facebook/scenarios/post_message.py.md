# Модуль `post_message`

## Обзор

Модуль `post_message` предназначен для автоматизации процесса публикации сообщений в Facebook, включая текст, изображения и видео. Он предоставляет функции для добавления заголовка и описания, загрузки медиафайлов, а также для управления процессом публикации.

## Содержание

1.  [Функции](#функции)
    *   [`post_title`](#post_title)
    *   [`upload_media`](#upload_media)
    *   [`update_images_captions`](#update_images_captions)
    *   [`publish`](#publish)
    *  [`promote_post`](#promote_post)
    *   [`post_message`](#post_message)

## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле сообщения.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (`SimpleNamespace | str`): Объект, содержащий заголовок и описание для отправки. Может быть `SimpleNamespace` или `str`.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, в противном случае `None`.

**Пример использования**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
post_title(driver, category)
# Возвращает True
```

### `upload_media`

**Описание**: Загружает медиафайлы в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (`SimpleNamespace | List[SimpleNamespace] | str | list[str]`): Список объектов `SimpleNamespace` или путей к медиафайлам.
- `no_video` (`bool`, optional): Если `True`, то видео не загружаются, по умолчанию `False`.
- `without_captions` (`bool`, optional): Если `True`, то подписи не загружаются, по умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, в противном случае `None`.

**Вызывает исключения**:
- `Exception`: Если произошла ошибка при загрузке медиафайлов или обновлении подписей.

**Пример использования**:

```python
driver = Driver(...)
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
upload_media(driver, products)
# Возвращает True
```

### `update_images_captions`

**Описание**: Добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (`List[SimpleNamespace]`): Список продуктов с деталями для обновления.
- `textarea_list` (`List[WebElement]`): Список текстовых областей, куда добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникла ошибка при обновлении подписей к медиафайлам.

### `publish`

**Описание**: Функция для публикации поста.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `attempts` (`int`, optional): Количество попыток публикации, по умолчанию `5`.

**Возвращает**:
- `bool`: `True` если публикация прошла успешно, в противном случае `None`.

### `promote_post`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (`SimpleNamespace`): Детали категории, используемые для заголовка и описания поста.
- `products` (`List[SimpleNamespace]`): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (`bool`, optional): Если `True`, то видео не загружаются, по умолчанию `False`.

**Пример использования**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
promote_post(driver, category, products)
```

### `post_message`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (`SimpleNamespace`): Детали сообщения, используемые для заголовка и описания поста.
- `no_video` (`bool`, optional): Если `True`, то видео не загружаются, по умолчанию `False`.
- `images` (`Optional[str | list[str]]`, optional): Список путей к изображениям или одиночный путь.
- `without_captions` (`bool`, optional): Если `True`, то подписи не загружаются, по умолчанию `False`.

**Пример использования**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
post_message(driver, category, products)
```