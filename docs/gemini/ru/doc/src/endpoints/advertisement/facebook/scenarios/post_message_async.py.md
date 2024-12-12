# Модуль `post_message_async`

## Обзор

Модуль `post_message_async` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление заголовка, описания и медиафайлов (изображений или видео). Он использует Selenium WebDriver для взаимодействия с веб-страницей Facebook.

## Содержание

- [Функции](#Функции)
  - [`post_title`](#post_title)
  - [`upload_media`](#upload_media)
  - [`update_images_captions`](#update_images_captions)
  - [`promote_post`](#promote_post)

## Функции

### `post_title`

**Описание**: Отправляет заголовок и описание кампании в поле сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Категория, содержащая заголовок и описание для отправки.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Примеры**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
post_title(driver, category)
# True
```

### `upload_media`

**Описание**: Загружает медиафайлы в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool): флаг, который определяет, нужно ли загружать видео или изображения, по умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время загрузки медиафайла или обновления подписи.

**Примеры**:
```python
driver = Driver(...)
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
await upload_media(driver, products)
# True
```

### `update_images_captions`

**Описание**: Асинхронно добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при обновлении подписей медиафайлов.

### `promote_post`

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (bool): флаг, который определяет, нужно ли загружать видео или изображения, по умолчанию `False`.

**Примеры**:
```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_saved_image='path/to/image.jpg', ...)]
await promote_post(driver, category, products)
```