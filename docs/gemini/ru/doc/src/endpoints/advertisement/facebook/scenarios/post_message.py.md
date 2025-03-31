# Модуль `post_message.py`

## Обзор

Модуль `post_message.py` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление заголовка, описания и медиафайлов (изображений и видео). Он содержит функции для загрузки медиа, обновления подписей к изображениям и публикации сообщения.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для автоматизации маркетинговых кампаний в Facebook. Он предоставляет набор функций для управления процессом создания и публикации рекламных постов.

## Оглавление

- [Функции](#Функции)
    - [`post_title`](#post_title)
    - [`upload_media`](#upload_media)
    - [`update_images_captions`](#update_images_captions)
        - [`handle_product`](#handle_product)
    - [`publish`](#publish)
    - [`promote_post`](#promote_post)
    - [`post_message`](#post_message)

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
    ...
```

**Назначение**: Отправляет заголовок и описание кампании в поле сообщения для публикации.

**Как работает функция**:
1. Прокручивает страницу вверх, чтобы убедиться, что поле сообщения видимо.
2. Открывает поле добавления поста.
3. Формирует сообщение, объединяя заголовок и описание, если `message` является экземпляром `SimpleNamespace`.
4. Добавляет сформированное сообщение в поле для ввода сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace | str): Объект `SimpleNamespace` или строка, содержащая заголовок и описание сообщения.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

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
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
    ...
```

**Назначение**: Загружает медиафайлы (изображения и видео) и обновляет подписи к ним.

**Как работает функция**:
1. Проверяет, есть ли медиафайлы для загрузки. Если нет, завершает работу.
2. Открывает форму добавления медиа.
3. Преобразует входной параметр `media` в список, если он не является списком.
4. Итерируется по списку медиафайлов и загружает каждый файл.
5. Если `without_captions` равен `True`, завершает работу.
6. Открывает форму редактирования загруженных медиафайлов.
7. Получает список текстовых полей для ввода подписей к изображениям.
8. Вызывает функцию `update_images_captions` для обновления подписей.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool, optional): Флаг, указывающий, следует ли исключать видеофайлы. По умолчанию `False`.
- `without_captions` (bool, optional): Флаг, указывающий, следует ли пропускать обновление подписей. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время загрузки медиафайлов или обновления подписей.

### `update_images_captions`

```python
def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Adds descriptions to uploaded media files.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there's an error updating the media captions.
    """
    ...
```

**Назначение**: Добавляет описания к загруженным медиафайлам.

**Как работает функция**:
1. Загружает локализованные единицы текста из файла `translations.json`.
2. Определяет внутреннюю функцию `handle_product` для обработки каждого продукта.
3. Итерируется по списку медиафайлов и вызывает `handle_product` для каждого файла.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей к медиафайлам.

#### `handle_product`

```python
def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """ Handles the update of media captions for a single product.

    Args:
        product (SimpleNamespace): The product to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.
        i (int): Index of the product in the list.
    """
    ...
```

**Назначение**: Обрабатывает обновление подписей к медиафайлам для одного продукта.

**Как работает функция**:
1. Определяет язык продукта.
2. Определяет направление текста (LTR или RTL) на основе языка.
3. Формирует сообщение, добавляя детали продукта (название, описание, цену и т.д.) в зависимости от направления текста.
4. Отправляет сообщение в соответствующее текстовое поле.

**Параметры**:
- `product` (SimpleNamespace): Продукт для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.
- `i` (int): Индекс продукта в списке.

### `publish`

```python
def publish(d:Driver, attempts = 5) -> bool:
    """"""
    ...
```

**Назначение**: Опубликовывает сообщение.

**Как работает функция**:
1. Пытается нажать кнопку "Опубликовать" несколько раз, если первая попытка не удалась.
2. Если появляется всплывающее окно, пытается его закрыть и повторить попытку.
3. После успешной публикации ждет, пока поле ввода сообщения не станет доступным.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `attempts` (int, optional): Количество попыток публикации. По умолчанию 5.

**Возвращает**:
- `bool`: `True`, если сообщение было успешно опубликовано, иначе `None`.

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
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    ...
```

**Назначение**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Как работает функция**:
1. Добавляет заголовок и описание к посту с помощью функции `post_title`.
2. Загружает медиафайлы с помощью функции `upload_media`.
3. Нажимает кнопку "Завершить редактирование".
4. Нажимает кнопку "Опубликовать".

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиафайлы и детали для публикации.
- `no_video` (bool, optional): Флаг, указывающий, следует ли исключать видеофайлы. По умолчанию `False`.

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
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
    ...
```

**Назначение**: Управляет процессом публикации сообщения с заголовком, описанием и медиафайлами.

**Как работает функция**:
1. Добавляет заголовок и описание к посту с помощью функции `post_title`.
2. Загружает медиафайлы с помощью функции `upload_media`.
3. Если загружено только одно изображение, нажимает кнопку "Отправить".
4. Нажимает кнопку "Завершить редактирование".
5. Публикует сообщение с помощью функции `publish`.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Детали сообщения, используемые для заголовка и описания поста.
- `no_video` (bool, optional): Флаг, указывающий, следует ли исключать видеофайлы. По умолчанию `False`.
- `images` (Optional[str | list[str]], optional): Список изображений для публикации. По умолчанию `None`.
- `without_captions` (bool, optional): Флаг, указывающий, следует ли пропускать обновление подписей. По умолчанию `False`.