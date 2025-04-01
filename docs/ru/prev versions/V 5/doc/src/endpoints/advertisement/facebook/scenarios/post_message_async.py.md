# Модуль `post_message_async`

## Обзор

Модуль `post_message_async` предназначен для автоматизации процесса публикации рекламных сообщений в Facebook, включая добавление заголовка, описания и медиафайлов (изображений или видео). Он использует `selenium` для взаимодействия с веб-интерфейсом Facebook и выполняет действия асинхронно для повышения эффективности.

## Подробней

Этот модуль является частью системы автоматизации маркетинговых кампаний. Он берет на себя задачу формирования и публикации рекламных постов в Facebook на основе данных о товарах, категориях и локализованных текстов. Асинхронный подход позволяет параллельно загружать медиафайлы и обновлять подписи, что ускоряет процесс публикации.

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
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

**Описание**: Отправляет заголовок и описание рекламной кампании в поле для создания сообщения в Facebook.

**Как работает функция**:
1. Прокручивает страницу вверх, чтобы убедиться, что поле для ввода сообщения видно.
2. Открывает окно добавления поста.
3. Формирует сообщение, объединяя заголовок и описание категории.
4. Вставляет сообщение в поле для ввода.

**Параметры**:
- `d` (Driver): Экземпляр драйвера `selenium`, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок (`title`) и описание (`description`) категории.

**Возвращает**:
- `bool`: `True`, если заголовок и описание успешно отправлены, иначе `None`.

**Примеры**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
post_title(driver, category)
```

### `upload_media`

```python
async def upload_media(d: Driver, products: List[SimpleNamespace], no_video:bool = False) -> bool:
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
        >>> await upload_media(driver, products)
        True
    """
```

**Описание**: Загружает медиафайлы (изображения или видео) в секцию изображений Facebook и обновляет подписи к ним.

**Как работает функция**:
1. Открывает форму добавления медиафайлов.
2. Проверяет, является ли `products` списком, и если нет, преобразует его в список.
3. Итерируется по списку продуктов, определяя путь к медиафайлу (видео, если `no_video = False`, иначе изображение).
4. Загружает медиафайл, используя локатор `foto_video_input`.
5. Открывает форму редактирования загруженных медиафайлов.
6. Получает список текстовых полей для ввода подписей к изображениям.
7. Вызывает функцию `update_images_captions` для асинхронного обновления подписей.

**Параметры**:
- `d` (Driver): Экземпляр драйвера `selenium`.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool, optional): Если `True`, загружаются только изображения, даже если доступно видео. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке медиафайлов или обновлении подписей.

**Примеры**:

```python
driver = Driver(...)
products = [SimpleNamespace(local_image_path='путь/к/изображению.jpg', ...)]
await upload_media(driver, products)
```

### `update_images_captions`

```python
async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Adds descriptions to uploaded media files asynchronously.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.

    Raises:
        Exception: If there's an error updating the media captions.
    """
```

**Описание**: Асинхронно добавляет описания к загруженным медиафайлам.

**Как работает функция**:
1. Загружает локализованные текстовые ресурсы из файла `translations.json`.
2. Определяет функцию `handle_product`, которая формирует сообщение с информацией о продукте на основе его атрибутов (`product_title`, `original_price`, `sale_price` и т. д.) и локализует текст в зависимости от языка продукта.
3. Отправляет сформированное сообщение в соответствующее текстовое поле для подписи к изображению.
4. Итерируется по списку продуктов и асинхронно вызывает `handle_product` для каждого продукта.

**Параметры**:
- `d` (Driver): Экземпляр драйвера `selenium`.
- `products` (List[SimpleNamespace]): Список продуктов с информацией для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей.

### `promote_post`

```python
async def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """ Manages the process of promoting a post with a title, description, and media files.

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

**Описание**: Управляет процессом продвижения поста, включая добавление заголовка, описания и медиафайлов.

**Как работает функция**:
1. Вызывает функцию `post_title` для добавления заголовка и описания.
2. Вызывает функцию `upload_media` для загрузки медиафайлов.
3. Нажимает кнопку завершения редактирования.
4. Нажимает кнопку публикации.

**Параметры**:
- `d` (Driver): Экземпляр драйвера `selenium`.
- `category` (SimpleNamespace): Объект с информацией о категории для заголовка и описания.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиафайлы и детали для публикации.
- `no_video` (bool, optional): Если `True`, загружаются только изображения, даже если доступно видео. По умолчанию `False`.

**Примеры**:

```python
driver = Driver(...)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='путь/к/изображению.jpg', ...)]
await promote_post(driver, category, products)
```