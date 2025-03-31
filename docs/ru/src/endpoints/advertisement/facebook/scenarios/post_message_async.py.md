# Модуль: src.endpoints.advertisement.facebook.scenarios.post_message_async

## Обзор

Модуль предназначен для автоматизации процесса публикации рекламных сообщений в Facebook, включая загрузку медиафайлов и добавление подписей к ним. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook.

## Подробней

Модуль `post_message_async.py` является частью системы автоматизации размещения рекламы в Facebook. Он содержит функции для отправки заголовка и описания рекламной кампании, загрузки медиафайлов (изображений и видео) и добавления подписей к ним.

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
    ...
```

**Назначение**: Отправляет заголовок и описание кампании в поле сообщения для публикации.

**Как работает функция**:
1. Выполняет прокрутку страницы вверх, чтобы убедиться, что все элементы видны.
2. Открывает окно добавления поста.
3. Формирует сообщение, объединяя заголовок и описание категории.
4. Добавляет сформированное сообщение в поле для ввода текста.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок (`title`) и описание (`description`) кампании.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

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
    ...
```

**Назначение**: Загружает медиафайлы (изображения или видео) в раздел изображений/видео и обновляет подписи к ним.

**Как работает функция**:
1. Открывает форму добавления медиафайлов.
2. Проверяет, является ли `products` списком, и преобразует его в список, если это не так.
3. Перебирает список продуктов, определяет путь к медиафайлу (видео или изображению).
4. Загружает медиафайл, используя локатор `foto_video_input`.
5. Открывает форму редактирования загруженных медиафайлов.
6. Получает список текстовых полей для ввода подписей.
7. Асинхронно обновляет подписи к изображениям, вызывая функцию `update_images_captions`.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool): Флаг, указывающий, следует ли игнорировать видеофайлы при загрузке медиа. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при загрузке медиафайла или обновлении подписи.

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
    ...
```

**Назначение**: Асинхронно добавляет описания к загруженным медиафайлам.

**Как работает функция**:
1. Загружает локализованные единицы текста из файла `translations.json`.
2. Определяет внутреннюю функцию `handle_product`, которая обновляет подпись для одного продукта.
3. Перебирает список продуктов и асинхронно вызывает `handle_product` для каждого продукта.

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих детали для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при обновлении подписей к медиафайлам.

**Внутренние функции**:

#### `handle_product`

```python
def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """ Handles the update of media captions for a single product synchronously.

    Args:
        product (SimpleNamespace): The product to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.
        i (int): Index of the product in the list.
    """
    ...
```

**Назначение**: Обновляет подпись для одного продукта синхронно.

**Как работает функция**:
1. Определяет направление текста (слева направо или справа налево) на основе языка продукта.
2. Формирует сообщение, добавляя детали продукта (название, цены, скидки и т.д.) в зависимости от направления текста.
3. Отправляет сообщение в соответствующее текстовое поле.

**Параметры**:
- `product` (SimpleNamespace): Продукт, для которого нужно обновить подпись.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.
- `i` (int): Индекс продукта в списке.

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
    ...
```

**Назначение**: Управляет процессом продвижения поста, включая добавление заголовка, описания и медиафайлов.

**Как работает функция**:
1. Вызывает функцию `post_title` для добавления заголовка и описания.
2. Вызывает функцию `upload_media` для загрузки медиафайлов.
3. Нажимает кнопку "Завершить редактирование".
4. Нажимает кнопку "Опубликовать".

**Параметры**:
- `d` (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиафайлы и детали для публикации.
- `no_video` (bool): Флаг, указывающий, следует ли игнорировать видеофайлы при загрузке медиа. По умолчанию `False`.

**Примеры**:
Примеры вызовов со всем спектром параметров. которы можно передать в функцию
```
>>> driver = Driver(...)
>>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
>>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
>>> await promote_post(driver, category, products)
```
```
>>> driver = Driver(...)
>>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
>>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', local_video_path='path/to/video.mp4')]
>>> await promote_post(driver, category, products, no_video=True)
```
```
>>> driver = Driver(...)
>>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
>>> products = [SimpleNamespace(local_image_path='path/to/image.jpg')]
>>> await promote_post(driver, category, products)