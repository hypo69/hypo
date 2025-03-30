# Модуль `post_message`

## Обзор

Модуль `post_message` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление заголовка, описания и медиафайлов. Он предоставляет функции для управления этим процессом через Selenium WebDriver.

## Подробней

Этот модуль содержит функции, которые позволяют автоматизировать процесс публикации сообщений в Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook, загружает локаторы элементов интерфейса из JSON-файла и выполняет различные действия, такие как ввод текста, загрузка медиафайлов и публикация сообщения. Модуль предназначен для использования в сценариях, где требуется автоматизированная публикация рекламных сообщений.

## Функции

### `post_title`

```python
def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace | str): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
```

**Описание**: Отправляет заголовок и описание кампании в поле сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace | str): Объект, содержащий заголовок и описание для отправки.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

### `upload_media`

```python
def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.

    Returns:
        bool: `True` if media files were uploaded successfully, otherwise `None`.

    Raises:
        Exception: If there is an error during media upload or caption update.

    Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
```

**Описание**: Загружает медиафайлы и обновляет подписи.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool, optional): Определяет, следует ли исключать видео из загрузки. По умолчанию `False`.
- `without_captions` (bool, optional): Определяет, следует ли загружать медиа без подписей. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время загрузки медиафайлов или обновления подписей.

### `update_images_captions`

```python
def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there's an error updating the media captions.
    """
```

**Описание**: Добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, где добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей к медиафайлам.

### `publish`

```python
def publish(d:Driver, attempts = 5) -> bool:
    """"""
```

**Описание**: 

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `attempts` (int, optional): Кол-во попыток для публикации. По умолчанию `5`.

**Возвращает**:
- `bool`: `True`, если публикация прошла успешно, иначе `None`.

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (bool, optional): Определяет, следует ли исключать видео из загрузки. По умолчанию `False`.

### `post_message`

```python
def post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False,  images:Optional[str | list[str]] = None, without_captions:bool = False) -> bool:
    """
    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace): The message details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Детали сообщения, используемые для заголовка и описания поста.
- `no_video` (bool, optional): Определяет, следует ли исключать видео из загрузки. По умолчанию `False`.
- `images` (Optional[str | list[str]], optional): Список изображений для загрузки. По умолчанию `None`.
- `without_captions` (bool, optional): Определяет, следует ли загружать медиа без подписей. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если публикация прошла успешно, иначе `None`.