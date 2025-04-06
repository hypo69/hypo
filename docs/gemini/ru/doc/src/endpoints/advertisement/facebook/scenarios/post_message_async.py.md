# Модуль: `post_message_async`

## Обзор

Модуль `post_message_async.py` предназначен для автоматизации процесса публикации рекламных сообщений в Facebook, включая загрузку медиафайлов и добавление подписей к ним. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook.

## Подробней

Этот модуль является частью системы автоматизации маркетинговых кампаний в Facebook. Он предоставляет функции для составления и публикации рекламных постов, включая добавление текста, изображений и видео. Модуль асинхронный и позволяет параллельно обрабатывать несколько продуктов, что ускоряет процесс публикации.

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """ Отправляет заголовок и описание кампании в поле сообщения.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        category (SimpleNamespace): Объект, содержащий заголовок и описание для отправки.

    Returns:
        bool: `True`, если заголовок и описание успешно отправлены, в противном случае `None`.

    Example:
        >>> driver = Driver(...)\n
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")\n
        >>> post_title(driver, category)\n
        True
    """
```

**Назначение**: Функция отправляет заголовок и описание рекламной кампании в поле для создания нового поста в Facebook.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок (`title`) и описание (`description`) кампании.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, в противном случае `None`.

**Как работает функция**:

1.  **Прокрутка страницы**: Прокручивает страницу вверх, чтобы убедиться, что все элементы видны.
2.  **Открытие окна добавления поста**: Нажимает на кнопку "Добавить пост", чтобы открыть форму для создания нового сообщения.
3.  **Формирование сообщения**: Собирает текст сообщения, используя заголовок и описание из объекта `category`.
4.  **Ввод сообщения**: Вставляет сформированное сообщение в текстовое поле поста.

**ASCII flowchart**:

```
A: Прокрутка страницы
↓
B: Открытие окна добавления поста
↓
C: Формирование сообщения (заголовок + описание)
↓
D: Ввод сообщения в текстовое поле
↓
E: Возврат True (если успешно) или None (если ошибка)
```

**Примеры**:

```python
driver = Driver(Chrome)
category = SimpleNamespace(title="Супер скидки!", description="Только сегодня!")
result = post_title(driver, category)
print(result)  # Выведет True, если успешно
```

### `upload_media`

```python
async def upload_media(d: Driver, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """ Загружает медиафайлы в раздел изображений и обновляет подписи.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
        no_video (bool): Если True - не загружать видео даже если `product` содержит `local_video_path`. По умолчанию `False`.

    Returns:
        bool: `True`, если медиафайлы были успешно загружены, в противном случае `None`.

    Raises:
        Exception: Если возникает ошибка во время загрузки медиа или обновления подписи.

    Example:
        >>> driver = Driver(...)\n
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]\n
        >>> await upload_media(driver, products)\n
        True
    """
```

**Назначение**: Функция загружает медиафайлы (изображения или видео) в рекламный пост в Facebook и обновляет подписи к ним.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов, содержащих информацию о продуктах, включая пути к медиафайлам.
- `no_video` (bool):  Если `True` - не загружать видео даже если `product` содержит `local_video_path`. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, в противном случае `None`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка во время загрузки медиа или обновления подписи.

**Как работает функция**:

1.  **Открытие формы добавления медиа**: Открывает форму для добавления фото/видео в пост.
2.  **Обработка списка продуктов**: Проверяет, что `products` является списком, и если нет, преобразует его в список.
3.  **Загрузка медиа для каждого продукта**: Перебирает продукты и загружает медиафайлы (сначала пытается загрузить видео, если `no_video = False`, иначе загружает изображение).
4.  **Обновление подписей**: После загрузки всех медиафайлов нажимает кнопку редактирования и вызывает функцию `update_images_captions` для добавления подписей к изображениям.

**ASCII flowchart**:

```
A: Открытие формы добавления медиа
↓
B: Проверка типа products (list или не list)
↓
C: Цикл по products
    ↓
    D: Определение типа медиа (видео или изображение)
    ↓
    E: Загрузка медиафайла
    ↓
F: Нажатие кнопки редактирования медиа
↓
G: Вызов update_images_captions
↓
H: Возврат True (если успешно) или None (если ошибка)
```

**Примеры**:

```python
driver = Driver(Chrome)
products = [
    SimpleNamespace(local_image_path="image1.jpg", product_title="Product 1"),
    SimpleNamespace(local_image_path="image2.jpg", product_title="Product 2")
]
asyncio.run(upload_media(driver, products))
```

### `update_images_captions`

```python
async def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Добавляет описания к загруженным медиафайлам асинхронно.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов с деталями для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, где добавляются подписи.

    Raises:
        Exception: Если возникает ошибка при обновлении подписей медиафайлов.
    """
```

**Назначение**: Функция добавляет описания (подписи) к загруженным медиафайлам в Facebook.  Функция асинхронная.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов с информацией о продуктах, для которых нужно добавить подписи.
- `textarea_list` (List[WebElement]): Список элементов `<textarea>`, в которые нужно добавить текст подписи.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при обновлении подписей медиафайлов.

**Внутренние функции**:

#### `handle_product`

```python
def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """ Обрабатывает обновление подписей медиафайлов для одного продукта синхронно.

    Args:
        product (SimpleNamespace): Продукт для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, где добавляются подписи.
        i (int): Индекс продукта в списке.
    """
```

**Назначение**: Внутренняя функция, которая формирует текст подписи для одного продукта и добавляет его в соответствующее текстовое поле.

**Параметры**:
- `product` (SimpleNamespace): Объект с информацией о продукте.
- `textarea_list` (List[WebElement]): Список элементов `<textarea>`.
- `i` (int): Индекс текущего продукта в списке.

**Как работает функция**:

1.  **Определение направления текста**: Определяет направление текста (слева направо или справа налево) на основе языка продукта.
2.  **Формирование сообщения**: Формирует текст сообщения, используя детали продукта (название, цены, скидки и т.д.) и локализованные строки из файла `translations.json`.
3.  **Отправка сообщения в textarea**: Отправляет сформированный текст в соответствующий элемент `<textarea>`.

**ASCII flowchart `handle_product`**:

```
A: Определение направления текста (LTR/RTL)
↓
B: Формирование сообщения (название, цены, скидки, локализация)
↓
C: Отправка сообщения в textarea
```

**Как работает функция `update_images_captions`**:

1.  **Загрузка локализованных строк**: Загружает локализованные строки из файла `translations.json`.
2.  **Цикл по продуктам**: Перебирает все продукты в списке.
3.  **Асинхронный вызов handle_product**: Для каждого продукта асинхронно вызывает функцию `handle_product`, чтобы добавить подпись.

**ASCII flowchart `update_images_captions`**:

```
A: Загрузка локализованных строк из translations.json
↓
B: Цикл по products
↓
C: Асинхронный вызов handle_product для каждого продукта
```

**Примеры**:

```python
driver = Driver(Chrome)
products = [
    SimpleNamespace(language="ru", product_title="Продукт 1", original_price="1000", sale_price="500"),
    SimpleNamespace(language="en", product_title="Product 2", original_price="20", sale_price="10")
]
textarea_list = driver.execute_locator(locator.edit_image_properties_textarea)  # Получаем список textarea элементов
asyncio.run(update_images_captions(driver, products, textarea_list))
```

### `promote_post`

```python
async def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video:bool = False) -> bool:
    """ Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
        no_video (bool): Если True - не загружать видео даже если `product` содержит `local_video_path`. По умолчанию `False`.

    Example:
        >>> driver = Driver(...)\n
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")\n
        >>> products = [SimpleNamespace(local_image_path=\'path/to/image.jpg\', ...)]\n
        >>> await promote_post(driver, category, products)
    """
```

**Назначение**: Функция управляет процессом создания и публикации рекламного поста в Facebook, включая добавление заголовка, описания и медиафайлов.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект, содержащий заголовок и описание рекламной кампании.
- `products` (List[SimpleNamespace]): Список объектов с информацией о продуктах (медиафайлы и детали).
- `no_video` (bool): Если True - не загружать видео даже если `product` содержит `local_video_path`. По умолчанию `False`.

**Как работает функция**:

1.  **Публикация заголовка**: Вызывает функцию `post_title` для добавления заголовка и описания в пост.
2.  **Загрузка медиа**: Вызывает функцию `upload_media` для загрузки медиафайлов (изображений или видео).
3.  **Завершение редактирования**: Нажимает кнопку "Завершить редактирование".
4.  **Публикация поста**: Нажимает кнопку "Опубликовать".

**ASCII flowchart**:

```
A: Вызов post_title (добавление заголовка и описания)
↓
B: Вызов upload_media (загрузка медиафайлов)
↓
C: Нажатие кнопки "Завершить редактирование"
↓
D: Нажатие кнопки "Опубликовать"
↓
E: Возврат True (если успешно) или None (если ошибка)
```

**Примеры**:

```python
driver = Driver(Chrome)
category = SimpleNamespace(title="Новая коллекция", description="Скидки до 50%!")
products = [
    SimpleNamespace(local_image_path="product1.jpg"),
    SimpleNamespace(local_image_path="product2.jpg")
]
asyncio.run(promote_post(driver, category, products))