# Модуль: src.endpoints.advertisement.facebook.post_message_async

## Обзор

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса размещения сообщений на Facebook. Он включает в себя функции для отправки заголовка и описания кампании, загрузки медиафайлов (изображений и видео) и обновления их подписей. Скрипт взаимодействует со страницей Facebook, используя локаторы для выполнения различных действий.

## Подробнее

Модуль предоставляет асинхронные функции для выполнения задач, связанных с публикацией рекламных постов на Facebook. Он использует драйвер Selenium для автоматизации действий в браузере, таких как ввод текста, загрузка медиафайлов и нажатие кнопок.

**Основные возможности:**

1.  **Отправка заголовка и описания**: Отправляет заголовок и описание кампании в поле сообщения Facebook.
2.  **Загрузка медиафайлов**: Загружает медиафайлы (изображения и видео) в пост Facebook и обновляет их подписи.
3.  **Продвижение поста**: Управляет всем процессом продвижения поста с заголовком, описанием и медиафайлами.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """
    Args:
        d (Driver): The `Driver` instance used for interacting with the webpage.
        category (SimpleNamespace): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.
    """
    ...
```

**Описание**: Отправляет заголовок и описание кампании в поле сообщения Facebook.

**Параметры**:

*   `d` (Driver): Экземпляр `Driver`, используемый для взаимодействия с веб-страницей.
*   `category` (SimpleNamespace): Объект, содержащий заголовок и описание для отправки.

**Возвращает**:

*   `bool`: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

**Пример**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация драйвера
driver = Driver(...)

# Создание объекта category
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")

# Отправка заголовка
post_title(driver, category)
```

### `upload_media`

```python
def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Args:
        d (Driver): The `Driver` instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.
        no_video (bool, optional): Flag indicating whether to skip video uploads. Defaults to False.

    Returns:
        bool: `True` if media files were uploaded successfully, otherwise `None`.
    """
    ...
```

**Описание**: Загружает медиафайлы в пост Facebook и обновляет их подписи.

**Параметры**:

*   `d` (Driver): Экземпляр `Driver`, используемый для взаимодействия с веб-страницей.
*   `products` (List[SimpleNamespace]): Список объектов, содержащих пути к медиафайлам.
*   `no_video` (bool, optional): Флаг, указывающий, следует ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:

*   `bool`: `True`, если медиафайлы были успешно загружены, иначе `None`.

**Пример**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация драйвера
driver = Driver(...)

# Создание списка products
products = [SimpleNamespace(local_image_path='путь/к/изображению.jpg', ...)]

# Загрузка медиафайлов
upload_media(driver, products)
```

### `update_images_captions`

```python
def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Args:
        d (Driver): The `Driver` instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products with details to update.
        textarea_list (List[WebElement]): List of textareas where captions are added.
    """
    ...
```

**Описание**: Асинхронно добавляет описания к загруженным медиафайлам.

**Параметры**:

*   `d` (Driver): Экземпляр `Driver`, используемый для взаимодействия с веб-страницей.
*   `products` (List[SimpleNamespace]): Список объектов с деталями для обновления.
*   `textarea_list` (List[WebElement]): Список текстовых полей, в которые добавляются подписи.

**Пример**:

```python
from src.webdriver.driver import Driver
from selenium.webdriver.remote.webelement import WebElement
from types import SimpleNamespace

# Инициализация драйвера
driver = Driver(...)

# Создание списка products
products = [SimpleNamespace(description='Описание изображения', ...)]

# Создание списка textarea_list
textarea_list = [WebElement(...), ...]

# Обновление подписей изображений
update_images_captions(driver, products, textarea_list)
```

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Args:
        d (Driver): The `Driver` instance used for interacting with the webpage.
        category (SimpleNamespace): The category details used for the post title and description.
        products (List[SimpleNamespace]): List of products containing media and details to be posted.
        no_video (bool, optional): Flag indicating whether to skip video uploads. Defaults to False.

    Returns:
        bool: `True` if the post was promoted successfully, otherwise `None`.
    """
    ...
```

**Описание**: Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

**Параметры**:

*   `d` (Driver): Экземпляр `Driver`, используемый для взаимодействия с веб-страницей.
*   `category` (SimpleNamespace): Объект с деталями категории, используемый для заголовка и описания поста.
*   `products` (List[SimpleNamespace]): Список объектов, содержащих медиа и детали для публикации.
*   `no_video` (bool, optional): Флаг, указывающий, следует ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:

*   `bool`: `True`, если пост был успешно продвинут, иначе `None`.

**Пример**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация драйвера
driver = Driver(...)

# Создание объектов category и products
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
products = [SimpleNamespace(local_image_path='путь/к/изображению.jpg', ...)]

# Продвижение поста
promote_post(driver, category, products)
```

## Зависимости

*   `selenium`: Для автоматизации веб-браузера.
*   `asyncio`: Для асинхронных операций.
*   `pathlib`: Для работы с путями к файлам.
*   `types`: Для создания простых пространств имен.
*   `typing`: Для аннотаций типов.

## Обработка ошибок

Скрипт включает надежную обработку ошибок, чтобы обеспечить продолжение выполнения, даже если определенные элементы не найдены или возникли проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.