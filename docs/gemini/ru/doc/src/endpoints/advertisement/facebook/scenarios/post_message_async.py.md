# Модуль `post_message_async`

## Обзор

Модуль `post_message_async` предназначен для автоматизации процесса публикации рекламных сообщений в Facebook, включая добавление заголовка, описания и медиафайлов (изображений или видео). Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook.

## Подробней

Модуль содержит функции для выполнения следующих задач:

- Отправка заголовка и описания рекламной кампании в поле сообщения.
- Загрузка медиафайлов (изображений или видео) в раздел медиа.
- Обновление подписей к загруженным медиафайлам.
- Управление процессом продвижения поста, объединяя все вышеперечисленные шаги.

Код предназначен для работы в асинхронном режиме, что позволяет эффективно выполнять задачи, связанные с ожиданием загрузки и обработки данных в веб-браузере.

## Классы

В данном модуле классы отсутствуют.

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

**Назначение**: Отправляет заголовок и описание рекламной кампании в поле для создания поста в Facebook.

**Параметры**:

- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок и описание кампании.

**Возвращает**:

- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Как работает функция**:

1.  **Прокрутка страницы**: Выполняется прокрутка страницы назад для обеспечения видимости необходимых элементов.
2.  **Открытие поля добавления поста**: Функция пытается открыть поле для добавления поста.
3.  **Формирование сообщения**: Создается сообщение, объединяющее заголовок и описание кампании.
4.  **Добавление сообщения в поле поста**: Функция добавляет сформированное сообщение в поле для создания поста.

```ascii
    Начало
    ↓
    Прокрутка страницы
    ↓
    Открытие поля добавления поста
    ↓
    Формирование сообщения
    ↓
    Добавление сообщения в поле поста
    ↓
    Конец
```

**Примеры**:

```python
driver = Driver(Chrome)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
result = post_title(driver, category)
print(result)
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
    ...
```

**Назначение**: Загружает медиафайлы (изображения или видео) в раздел медиа и обновляет подписи к ним.

**Параметры**:

- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
- `no_video` (bool): Флаг, указывающий, следует ли загружать видео (по умолчанию `False`).

**Возвращает**:

- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке во время загрузки медиа или обновления подписи.

**Как работает функция**:

1.  **Открытие формы добавления медиа**: Функция пытается открыть форму для добавления медиафайлов.
2.  **Проверка типа `products`**: Гарантируется, что `products` является списком.
3.  **Итерация по продуктам**: Перебирает продукты и загружает медиафайлы для каждого продукта.
4.  **Загрузка медиафайла**: Загружает медиафайл, используя путь к изображению или видео.
5.  **Обновление подписей**: После загрузки всех медиафайлов функция обновляет подписи к ним, используя функцию `update_images_captions`.

```ascii
    Начало
    ↓
    Открытие формы добавления медиа
    ↓
    Проверка типа products
    ↓
    Итерация по продуктам
    ↓
    Загрузка медиафайла
    ↓
    Обновление подписей (вызов update_images_captions)
    ↓
    Конец
```

**Внутренние функции**:

- Отсутствуют.

**Примеры**:

```python
driver = Driver(Chrome)
products = [SimpleNamespace(local_image_path='path/to/image.jpg', product_title='Название продукта', language='ru')]
asyncio.run(upload_media(driver, products))
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
        Exception: If there\'s an error updating the media captions.
    """
    ...
```

**Назначение**: Добавляет описания к загруженным медиафайлам асинхронно.

**Параметры**:

- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список продуктов с деталями для обновления.
- `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке во время обновления подписей к медиафайлам.

**Как работает функция**:

1.  **Загрузка локализованных единиц**: Загружает локализованные строки из файла `translations.json`.
2.  **Определение функции `handle_product`**: Определяет внутреннюю функцию `handle_product` для обработки каждого продукта.
3.  **Асинхронная обработка продуктов**: Асинхронно обрабатывает продукты и обновляет их подписи, используя `asyncio.to_thread` для выполнения `handle_product` в отдельном потоке.

```ascii
    Начало
    ↓
    Загрузка локализованных единиц
    ↓
    Определение функции handle_product
    ↓
    Асинхронная обработка продуктов (вызов handle_product для каждого продукта)
    ↓
    Конец
```

**Внутренние функции**:

- `handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None`:
    - **Назначение**: Обновляет подпись к медиафайлу для одного продукта синхронно.
    - **Параметры**:
        - `product` (SimpleNamespace): Продукт, для которого нужно обновить подпись.
        - `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.
        - `i` (int): Индекс продукта в списке.
    - **Как работает**:
        1. Определяет направление текста (LTR или RTL) на основе языка продукта.
        2. Формирует сообщение, содержащее детали продукта (название, цены, скидки и т.д.) на основе локализованных строк.
        3. Отправляет сообщение в соответствующее текстовое поле.

```ascii
        Начало (handle_product)
        ↓
        Определение направления текста
        ↓
        Формирование сообщения
        ↓
        Отправка сообщения в текстовое поле
        ↓
        Конец (handle_product)
```

**Примеры**:

```python
driver = Driver(Chrome)
products = [SimpleNamespace(product_title='Название продукта', original_price='100', sale_price='50', discount='50%', evaluate_rate='4.5', promotion_link='link', tags='tags', language='ru')]
textarea_list = driver.execute_locator(locator.edit_image_properties_textarea)  # Предполагается, что locator.edit_image_properties_textarea возвращает список WebElement
asyncio.run(update_images_captions(driver, products, textarea_list))
```

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

**Параметры**:

- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиафайлы и детали для публикации.
- `no_video` (bool): Флаг, указывающий, следует ли загружать видео (по умолчанию `False`).

**Как работает функция**:

1.  **Публикация заголовка**: Вызывает функцию `post_title` для отправки заголовка и описания.
2.  **Загрузка медиа**: Вызывает функцию `upload_media` для загрузки медиафайлов.
3.  **Завершение редактирования**: Нажимает кнопку завершения редактирования.
4.  **Публикация**: Нажимает кнопку публикации для завершения процесса.

```ascii
    Начало
    ↓
    Публикация заголовка (вызов post_title)
    ↓
    Загрузка медиа (вызов upload_media)
    ↓
    Завершение редактирования
    ↓
    Публикация
    ↓
    Конец
```

**Примеры**:

```python
driver = Driver(Chrome)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='path/to/image.jpg')]
asyncio.run(promote_post(driver, category, products))