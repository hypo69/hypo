# Модуль `post_message`

## Обзор

Модуль `post_message` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление заголовка, описания и медиафайлов. Он предоставляет функции для загрузки медиа, обновления подписей к изображениям и публикации сообщения.

## Подробней

Этот модуль является частью системы автоматизации рекламы в Facebook. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook, автоматизируя шаги, которые пользователь обычно выполняет вручную. Модуль включает в себя функции для загрузки медиафайлов, добавления заголовков и описаний к постам, а также для управления процессом публикации. Расположение файла в проекте `hypotez/src/endpoints/advertisement/facebook/scenarios/post_message.py` указывает на то, что он отвечает за реализацию сценария публикации сообщения в Facebook.

## Функции

### `post_title`

```python
def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """ Sends the title and description of a campaign to the post message box.

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

**Описание**: Отправляет заголовок и описание кампании в поле сообщения.

**Как работает функция**:

1.  Выполняет скролл страницы назад.
2.  Открывает окно добавления поста.
3.  Формирует сообщение, объединяя заголовок и описание.
4.  Добавляет сообщение в поле для ввода.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `message` (SimpleNamespace | str): Объект, содержащий заголовок и описание, или строка с сообщением.

**Возвращает**:

*   `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
post_title(driver, category)
```

### `upload_media`

```python
def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """ Uploads media files to the images section and updates captions.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.

    Returns:
        bool: `True` if media files were uploaded successfully, otherwise `None`.

    Raises:
        Exception: If there is an error during media upload or caption update.

    Examples:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]
        >>> upload_media(driver, products)
        True
    """
```

**Описание**: Загружает медиафайлы в раздел изображений и обновляет подписи.

**Как работает функция**:

1.  Проверяет, есть ли медиа для загрузки.
2.  Открывает форму добавления медиа.
3.  Преобразует входные медиа в список.
4.  Итерируется по списку медиа и загружает каждый файл.
5.  Обновляет подписи для загруженных медиа.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Список объектов или строк с путями к медиафайлам.
*   `no_video` (bool): Флаг, указывающий, нужно ли исключить видео. По умолчанию `False`.
*   `without_captions` (bool): Флаг, указывающий, нужно ли исключить добавление подписей. По умолчанию `False`.

**Возвращает**:

*   `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка во время загрузки медиа или обновления подписей.

**Примеры**:

```python
driver = Driver(...)
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
upload_media(driver, products)
```

### `update_images_captions`

```python
def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Adds descriptions to uploaded media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there\'s an error updating the media captions.
    """
```

**Описание**: Добавляет описания к загруженным медиафайлам.

**Как работает функция**:

1.  Загружает локализованные единицы текста из файла `translations.json`.
2.  Определяет функцию `handle_product` для обновления подписи для каждого продукта.
3.  Итерируется по списку медиа и вызывает `handle_product` для каждого элемента.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `media` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
*   `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при обновлении подписей медиа.

### `publish`

```python
def publish(d:Driver, attempts = 5) -> bool:
    """"""
```

**Описание**: Опубликовывает сообщение.

**Как работает функция**:

1.  Выполняет попытки публикации сообщения.
2.  Обрабатывает возможные всплывающие окна и ошибки.
3.  Проверяет, освободилось ли поле ввода после публикации.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `attempts` (int): Количество попыток публикации. По умолчанию `5`.

**Возвращает**:

*   `bool`: `True`, если сообщение было успешно опубликовано.

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Как работает функция**:

1.  Отправляет заголовок и описание поста.
2.  Загружает медиафайлы.
3.  Выполняет публикацию.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `category` (SimpleNamespace): Детали категории для заголовка и описания поста.
*   `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
*   `no_video` (bool): Флаг, указывающий, нужно ли исключить видео. По умолчанию `False`.

**Примеры**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
promote_post(driver, category, products)
```

### `post_message`

```python
def post_message(d: Driver, message: SimpleNamespace,  no_video: bool = False,  images:Optional[str | list[str]] = None, without_captions:bool = False) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        message (SimpleNamespace): The message details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Описание**: Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

**Как работает функция**:

1.  Отправляет заголовок и описание сообщения.
2.  Загружает медиафайлы.
3.  Выполняет публикацию.

**Параметры**:

*   `d` (Driver): Экземпляр драйвера WebDriver для взаимодействия с веб-страницей.
*   `message` (SimpleNamespace): Детали сообщения для заголовка и описания поста.
*   `no_video` (bool): Флаг, указывающий, нужно ли исключить видео. По умолчанию `False`.
*   `images` (Optional[str | list[str]]): Список изображений для загрузки. По умолчанию `None`.
*   `without_captions` (bool): Флаг, указывающий, нужно ли исключить добавление подписей. По умолчанию `False`.

**Примеры**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
promote_post(driver, category, products)