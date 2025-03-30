# Модуль `post_message_async`

## Обзор

Модуль `post_message_async` предназначен для автоматизации процесса публикации рекламных сообщений в Facebook, включая загрузку медиафайлов и добавление подписей к ним. Он содержит функции для отправки заголовка и описания рекламной кампании, загрузки медиафайлов (изображений и видео) и обновления подписей к изображениям.

## Подробней

Этот модуль автоматизирует взаимодействие с Facebook через Selenium WebDriver, выполняя следующие шаги: открытие формы добавления поста, ввод заголовка и описания, загрузку медиафайлов, добавление подписей к изображениям и, наконец, публикацию поста. Модуль использует локаторы, хранящиеся в JSON-файле, для поиска элементов на странице Facebook.

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
```

**Описание**: Отправляет заголовок и описание кампании в поле сообщения для публикации.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок и описание для отправки.

**Возвращает**:
- `bool`: `True`, если заголовок и описание успешно отправлены, иначе `None`.

### `upload_media`

```python
async def upload_media(d: Driver, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.

    Returns:
        bool: `True` if media files were uploaded successfully, otherwise `None`.

    Raises:
        Exception: If there is an error during media upload or caption update.

    Examples:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> await upload_media(driver, products)
        True
    """
```

**Описание**: Загружает медиафайлы в раздел изображений и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool): Флаг, указывающий, следует ли игнорировать видеофайлы. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке медиафайлов или обновлении подписей.

### `update_images_captions`

```python
async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there's an error updating the media captions.
    """
```

**Описание**: Асинхронно добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
- `textarea_list` (List[WebElement]): Список элементов `<textarea>`, в которые добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей к медиафайлам.

### `promote_post`

```python
async def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> await promote_post(driver, category, products)
    """
```

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (bool): Флаг, указывающий, следует ли игнорировать видеофайлы. По умолчанию `False`.

**Примеры**:

```python
>>> driver = Driver(...)
>>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
>>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
>>> await promote_post(driver, category, products)