# Модуль для публикации сообщений в Facebook

## Обзор

Модуль `post_message.py` предназначен для автоматизации процесса публикации сообщений в Facebook, включая ввод заголовка и описания, загрузку медиафайлов и обновление подписей к изображениям.

## Подробней

Модуль предоставляет функции для взаимодействия с веб-интерфейсом Facebook с использованием Selenium WebDriver. Он автоматизирует шаги, необходимые для создания и публикации сообщений, такие как открытие формы добавления сообщения, ввод текста, загрузка изображений и видео, а также публикация самого сообщения.

## Классы

В данном модуле классы отсутствуют.

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

**Назначение**: Отправляет заголовок и описание кампании в поле сообщения.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace | str): Объект SimpleNamespace или строка, содержащая заголовок и описание для отправки.

**Возвращает**:
- `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Как работает функция**:

1. Прокручивает страницу назад.
2. Открывает окно добавления сообщения.
3. Добавляет сообщение в поле сообщения, формируя его из заголовка и описания, если `message` - экземпляр `SimpleNamespace`, или используя `message` напрямую, если это строка.

**ASCII flowchart**:

```
A: Прокрутка страницы назад
|
B: Открытие окна добавления сообщения
|
C: Добавление сообщения в поле сообщения
```

**Примеры**:

```python
driver = Driver(Firefox)
message = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
post_title(driver, message)

driver = Driver(Firefox)
message = "Текст сообщения"
post_title(driver, message)
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
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
```

**Назначение**: Загружает медиафайлы и обновляет подписи к изображениям.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Путь к медиафайлу или список путей к медиафайлам.
- `no_video` (bool): Флаг, указывающий, нужно ли игнорировать видеофайлы. По умолчанию `False`.
- `without_captions` (bool): Флаг, указывающий, нужно ли загружать подписи к изображениям. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Как работает функция**:

1. Открывает форму добавления медиа.
2. Преобразует `media` в список, если это не список.
3. Итерируется по списку медиафайлов и загружает каждый файл.
4. Если `without_captions` равен `False`, обновляет подписи для загруженных медиафайлов, вызывая функцию `update_images_captions`.

**ASCII flowchart**:

```
A: Открытие формы добавления медиа
|
B: Преобразование media в список
|
C: Загрузка медиафайлов
|
D: Обновление подписей (если without_captions == False)
```

**Примеры**:

```python
driver = Driver(Firefox)
media = [SimpleNamespace(local_image_path='path/to/image1.jpg'), SimpleNamespace(local_image_path='path/to/image2.jpg')]
upload_media(driver, media)

driver = Driver(Firefox)
media = 'path/to/image.jpg'
upload_media(driver, media)
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

**Назначение**: Добавляет описания к загруженным медиафайлам.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `media` (List[SimpleNamespace]): Список объектов SimpleNamespace с деталями для обновления.
- `textarea_list` (List[WebElement]): Список элементов textarea, в которые добавляются подписи.

**Как работает функция**:

1. Загружает локальные единицы из файла `translations.json`.
2. Определяет внутреннюю функцию `handle_product`, которая обновляет подписи для одного продукта.
3. Итерируется по списку `media` и вызывает `handle_product` для каждого продукта.

**Внутренние функции**:

#### `handle_product`

```python
def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """ Handles the update of media captions for a single product.

    Args:
        product (SimpleNamespace): The product to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.
        i (int): Index of the product in the list.
    """
```

**Назначение**: Обновляет подписи для одного продукта.

**Параметры**:
- `product` (SimpleNamespace): Продукт для обновления.
- `textarea_list` (List[WebElement]): Список элементов textarea, в которые добавляются подписи.
- `i` (int): Индекс продукта в списке.

**Как работает функция**:

1. Определяет язык продукта и направление текста (LTR или RTL).
2. Формирует сообщение, добавляя детали продукта (название, описание, цену и т.д.) в зависимости от направления текста.
3. Отправляет сообщение в соответствующий textarea.

**ASCII flowchart**:

```
A: Определение языка и направления текста
|
B: Формирование сообщения с деталями продукта
|
C: Отправка сообщения в textarea
```

**ASCII flowchart (update_images_captions)**:

```
A: Загрузка локальных единиц
|
B: Итерация по списку media
|
C: Вызов handle_product для каждого продукта
```

**Примеры**:

```python
driver = Driver(Firefox)
media = [SimpleNamespace(product_title='Product 1', description='Description 1', language='ru'), SimpleNamespace(product_title='Product 2', description='Description 2', language='en')]
textarea_list = [driver.find_element(By.XPATH, '//textarea[1]'), driver.find_element(By.XPATH, '//textarea[2]')]
update_images_captions(driver, media, textarea_list)
```

### `publish`

```python
def publish(d:Driver, attempts = 5) -> bool:
    """"""
```

**Назначение**: Публикует сообщение.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `attempts` (int): Количество попыток публикации. По умолчанию 5.

**Возвращает**:
- `bool`: `True`, если сообщение опубликовано успешно.

**Как работает функция**:

Функция пытается опубликовать сообщение, используя заданные локаторы. Если публикация не удалась, она пробует закрыть всплывающие окна или нажать кнопку "Не сейчас" и повторяет попытку.

**ASCII flowchart**:

```
A: Нажатие кнопки "Завершить редактирование"
|
B: Нажатие кнопки "Опубликовать"
|
C: Если не удалось опубликовать:
    - Попытка закрыть всплывающее окно
    - Попытка нажать кнопку "Не сейчас"
    - Повторная попытка публикации
```

**Примеры**:

```python
driver = Driver(Firefox)
publish(driver)
```

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
```

**Назначение**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
- `no_video` (bool): Флаг, указывающий, нужно ли игнорировать видеофайлы. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если сообщение опубликовано успешно.

**Как работает функция**:

1. Отправляет заголовок и описание поста.
2. Загружает медиафайлы.
3. Нажимает кнопку "Завершить редактирование".
4. Нажимает кнопку "Опубликовать".

**ASCII flowchart**:

```
A: Отправка заголовка и описания поста
|
B: Загрузка медиафайлов
|
C: Нажатие кнопки "Завершить редактирование"
|
D: Нажатие кнопки "Опубликовать"
```

**Примеры**:

```python
driver = Driver(Firefox)
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='path/to/image1.jpg'), SimpleNamespace(local_image_path='path/to/image2.jpg')]
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
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Назначение**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:
- `d` (Driver): Экземпляр драйвера, используемый для взаимодействия с веб-страницей.
- `message` (SimpleNamespace): Детали сообщения, используемые для заголовка и описания поста.
- `no_video` (bool): Флаг, указывающий, нужно ли игнорировать видеофайлы. По умолчанию `False`.
- `images` (Optional[str | list[str]]): Список изображений для публикации.
- `without_captions` (bool): Флаг, указывающий, нужно ли загружать подписи к изображениям. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если сообщение опубликовано успешно.

**Как работает функция**:

1. Отправляет заголовок и описание поста.
2. Загружает медиафайлы.
3. Если было только одно изображение, выходит.
4. Нажимает кнопку "Завершить редактирование".
5. Публикует сообщение.

**ASCII flowchart**:

```
A: Отправка заголовка и описания поста
|
B: Загрузка медиафайлов
|
C: Если было одно изображение:
    - Выход
|
D: Нажатие кнопки "Завершить редактирование"
|
E: Публикация сообщения
```

**Примеры**:

```python
driver = Driver(Firefox)
message = SimpleNamespace(title="Заголовок сообщения", description="Описание сообщения", products=[SimpleNamespace(local_image_path='path/to/image1.jpg'), SimpleNamespace(local_image_path='path/to/image2.jpg')])
post_message(driver, message)