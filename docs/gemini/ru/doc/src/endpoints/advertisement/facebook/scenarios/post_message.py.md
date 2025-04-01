# Модуль для публикации сообщений в Facebook

## Обзор

Модуль `post_message.py` предназначен для автоматизации процесса публикации сообщений в Facebook, включая добавление заголовка, описания и медиафайлов. Он использует Selenium WebDriver для взаимодействия с веб-интерфейсом Facebook.

## Подробнее

Этот модуль содержит функции для выполнения следующих действий:

- Отправка заголовка и описания кампании в поле сообщения.
- Загрузка медиафайлов (изображений и видео) в раздел изображений.
- Обновление подписей для загруженных медиафайлов.
- Публикация сообщения.
- Управление процессом продвижения поста.

Модуль использует локаторы, хранящиеся в JSON-файле, для определения элементов веб-страницы, с которыми необходимо взаимодействовать.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `post_title`

```python
def post_title(d: Driver, message: SimpleNamespace | str) -> bool:
    """ Отправляет заголовок и описание кампании в поле сообщения.

    Args:
        d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
        message (SimpleNamespace | str): Объект, содержащий заголовок и описание для отправки.

    Returns:
        bool: `True`, если заголовок и описание были успешно отправлены, иначе `None`.

    Example:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
```

**Назначение**: Отправляет заголовок и описание сообщения (или кампании) в соответствующее поле на странице Facebook.

**Параметры**:

- `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
- `message` (SimpleNamespace | str): Объект, содержащий заголовок и описание сообщения. Если это `SimpleNamespace`, ожидается наличие атрибутов `title` и `description`. Если это `str`, то используется непосредственно как текст сообщения.

**Возвращает**:

- `bool`: `True`, если отправка прошла успешно, иначе `None`.

**Как работает функция**:

1.  **Прокрутка страницы**: Прокручивает страницу вверх, чтобы убедиться, что поле сообщения видимо.
2.  **Открытие поля добавления сообщения**: Кликает на локатор, который открывает поле для добавления нового сообщения.
3.  **Формирование сообщения**: Если `message` это `SimpleNamespace`, формирует строку сообщения, объединяя заголовок и описание с новой строкой между ними. Если `message` это строка, то она используется как есть.
4.  **Отправка сообщения**: Отправляет сформированное сообщение в поле ввода сообщения.

**ASII flowchart**:

```
A: Прокрутка страницы вверх
↓
B: Открытие поля добавления сообщения
↓
C: Формирование сообщения (заголовок + описание)
↓
D: Отправка сообщения в поле ввода
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver

# Пример с использованием SimpleNamespace
driver = Driver(...)
message = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")
result = post_title(driver, message)
print(result)  # Вывод: True или None

# Пример с использованием строки
driver = Driver(...)
message = "Текст сообщения"
result = post_title(driver, message)
print(result)  # Вывод: True или None
```

### `upload_media`

```python
def upload_media(d: Driver, media: SimpleNamespace | List[SimpleNamespace] | str | list[str],   no_video: bool = False, without_captions:bool = False) -> bool:
    """ Загружает медиафайлы в раздел изображений и обновляет подписи.

    Args:
        d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.

    Returns:
        bool: `True`, если медиафайлы были успешно загружены, иначе `None`.

    Raises:
        Exception: Если возникает ошибка во время загрузки медиа или обновления подписей.

    Example:
        >>> driver = Driver(...)
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> upload_media(driver, products)
        True
    """
```

**Назначение**: Загружает медиафайлы (изображения или видео) на страницу Facebook и при необходимости обновляет подписи к ним.

**Параметры**:

- `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
- `media` (SimpleNamespace | List[SimpleNamespace] | str | list[str]): Путь к медиафайлу или список путей. Может быть объектом `SimpleNamespace` с атрибутом `local_image_path` или `local_video_path`, строкой или списком строк.
- `no_video` (bool, optional): Если `True`, то видео не будут загружены. По умолчанию `False`.
- `without_captions` (bool, optional): Если `True`, то подписи к изображениям не будут обновлены. По умолчанию `False`.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, иначе `None`.

**Как работает функция**:

1.  **Проверка наличия медиафайлов**: Если список медиа пуст, функция завершается.
2.  **Открытие формы добавления медиа**: Кликает на кнопку/локатор, который открывает форму для добавления фото/видео.
3.  **Преобразование в список**: Преобразует входной параметр `media` в список, если он не является списком.
4.  **Итерация по медиафайлам**: Перебирает элементы списка `media_list`.
5.  **Определение пути к медиафайлу**: Определяет путь к файлу, проверяя атрибуты `local_video_path` и `local_image_path` (если `media` является `SimpleNamespace`).
6.  **Загрузка медиафайла**: Загружает медиафайл, отправляя путь к файлу в поле загрузки.
7.  **Обновление подписей**: Если `without_captions` равно `False`, пытается обновить подписи к загруженным изображениям, вызывая функцию `update_images_captions`.

**ASII flowchart**:

```
A: Проверка наличия медиафайлов
↓
B: Открытие формы добавления медиа
↓
C: Преобразование media в список
↓
D: Итерация по медиафайлам
│
└──> E: Определение пути к медиафайлу
│   ↓
│   F: Загрузка медиафайла
│   ↓
│   G: Обновление подписей (если without_captions=False)
↓
H: Завершение
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver

# Пример с использованием списка SimpleNamespace
driver = Driver(...)
products = [
    SimpleNamespace(local_image_path="path/to/image1.jpg", description="Описание 1"),
    SimpleNamespace(local_image_path="path/to/image2.jpg", description="Описание 2"),
]
result = upload_media(driver, products)
print(result)  # Вывод: True или None

# Пример с использованием списка строк
driver = Driver(...)
images = ["path/to/image1.jpg", "path/to/image2.jpg"]
result = upload_media(driver, images)
print(result)  # Вывод: True или None

# Пример с использованием SimpleNamespace и без обновления подписей
driver = Driver(...)
product = SimpleNamespace(local_image_path="path/to/image.jpg", description="Описание")
result = upload_media(driver, product, without_captions=True)
print(result)  # Вывод: True или None
```

### `update_images_captions`

```python
def update_images_captions(d: Driver, media: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """ Добавляет описания к загруженным медиафайлам.

    Args:
        d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов с деталями для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, куда добавляются подписи.

    Raises:
        Exception: Если возникает ошибка при обновлении подписей медиафайлов.
    """
```

**Назначение**: Обновляет подписи (описания) для загруженных медиафайлов на странице Facebook.

**Параметры**:

-   `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
-   `media` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, содержащих информацию о медиафайлах и их описаниях.
-   `textarea_list` (List[WebElement]): Список элементов `WebElement` (текстовых полей), в которые будут введены подписи.

**Как работает функция**:

1.  **Загрузка локализованных строк**: Загружает JSON-файл с локализованными строками для разных языков.
2.  **Определение внутренней функции `handle_product`**: Определяет внутреннюю функцию, которая обрабатывает обновление подписи для одного медиафайла.
3.  **Итерация по медиафайлам**: Перебирает элементы списка `media`.
4.  **Вызов `handle_product` для каждого медиафайла**: Для каждого медиафайла вызывает функцию `handle_product`, передавая ей информацию о продукте, список текстовых полей и индекс текущего медиафайла.

#### `handle_product`

```python
def handle_product(product: SimpleNamespace, textarea_list: List[WebElement], i: int) -> None:
    """ Обрабатывает обновление подписей медиа для одного продукта.

    Args:
        product (SimpleNamespace): Продукт для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, куда добавляются подписи.
        i (int): Индекс продукта в списке.
    """
```

**Назначение**: Обновляет подпись для одного медиафайла.

**Параметры**:

-   `product` (SimpleNamespace): Объект `SimpleNamespace`, содержащий информацию о медиафайле и его описании.
-   `textarea_list` (List[WebElement]): Список элементов `WebElement` (текстовых полей), в которые будут введены подписи.
-   `i` (int): Индекс текстового поля, соответствующего текущему медиафайлу.

**Как работает функция**:

1.  **Определение направления текста**: Определяет направление текста (LTR или RTL) на основе языка продукта.
2.  **Формирование сообщения**: Формирует строку сообщения, объединяя заголовок, описание, цену и другие детали продукта в зависимости от направления текста.
3.  **Отправка сообщения в текстовое поле**: Отправляет сформированное сообщение в соответствующее текстовое поле.

**ASII flowchart для `update_images_captions`**:

```
A: Загрузка локализованных строк
↓
B: Определение внутренней функции handle_product
↓
C: Итерация по медиафайлам
│
└──> D: Вызов handle_product для каждого медиафайла
↓
E: Завершение
```

**ASII flowchart для `handle_product`**:

```
A: Определение направления текста
↓
B: Формирование сообщения (заголовок, описание, цена и т.д.)
↓
C: Отправка сообщения в текстовое поле
↓
D: Завершение
```

**Примеры**:

```python
from types import SimpleNamespace
from selenium.webdriver.remote.webelement import WebElement
from src.webdriver.driver import Driver

# Пример использования
driver = Driver(...)
products = [
    SimpleNamespace(
        language="en",
        product_title="Product Title 1",
        description="Description 1",
        original_price="100",
        target_original_price_currency="$",
        sale_price="80",
        discount="20%",
        evaluate_rate="4.5",
        promotion_link="http://example.com/promo1",
    ),
    SimpleNamespace(
        language="ru",
        product_title="Название продукта 2",
        description="Описание 2",
        original_price="200",
        target_original_price_currency="₽",
        sale_price="160",
        discount="20%",
        evaluate_rate="4.8",
        promotion_link="http://example.com/promo2",
    ),
]
textarea_list = [
    WebElement(...),  # Замените на реальные WebElement
    WebElement(...),  # Замените на реальные WebElement
]
update_images_captions(driver, products, textarea_list)
```

### `publish`

```python
def publish(d:Driver, attempts = 5) -> bool:
    """"""
```

**Назначение**: Опубликовывает сообщение на странице Facebook.

**Параметры**:

-   `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
-   `attempts` (int, optional): Количество попыток для публикации. По умолчанию `5`.

**Возвращает**:

-   `bool`: `True`, если публикация прошла успешно.

**Как работает функция**:

1.  **Проверка количества попыток**: Если количество попыток меньше `0`, функция завершается.
2.  **Клик на кнопку завершения редактирования**: Кликает на кнопку, завершающую редактирование сообщения.
3.  **Клик на кнопку публикации**: Пытается опубликовать сообщение.
4.  **Обработка всплывающих окон**: Если появляется всплывающее окно, пытается закрыть его и повторить публикацию.
5.  **Ожидание освобождения поля ввода**: Ожидает, пока поле ввода сообщения не освободится.

**ASII flowchart**:

```
A: Проверка количества попыток
↓
B: Клик на кнопку завершения редактирования
↓
C: Клик на кнопку публикации
↓
D: Обработка всплывающих окон (если есть)
↓
E: Ожидание освобождения поля ввода
↓
F: Завершение
```

**Примеры**:

```python
from src.webdriver.driver import Driver

# Пример использования
driver = Driver(...)
result = publish(driver)
print(result)  # Вывод: True или None
```

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """ Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Инстанс драйвера, используемый для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]
        >>> promote_post(driver, category, products)
    """
```

**Назначение**: Управляет процессом продвижения поста в Facebook, включая добавление заголовка, описания и медиафайлов.

**Параметры**:

-   `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
-   `category` (SimpleNamespace): Объект `SimpleNamespace`, содержащий информацию о заголовке и описании поста.
-   `products` (List[SimpleNamespace]): Список объектов `SimpleNamespace`, содержащих информацию о медиафайлах и деталях продукта.
-   `no_video` (bool, optional): Если `True`, то видео не будут загружены. По умолчанию `False`.

**Возвращает**:

-   `bool`: `True`, если продвижение поста прошло успешно.

**Как работает функция**:

1.  **Отправка заголовка и описания**: Вызывает функцию `post_title` для отправки заголовка и описания поста.
2.  **Загрузка медиафайлов**: Вызывает функцию `upload_media` для загрузки медиафайлов.
3.  **Клик на кнопку завершения редактирования**: Кликает на кнопку, завершающую редактирование сообщения.
4.  **Публикация поста**: Пытается опубликовать пост.

**ASII flowchart**:

```
A: Отправка заголовка и описания
↓
B: Загрузка медиафайлов
↓
C: Клик на кнопку завершения редактирования
↓
D: Публикация поста
↓
F: Завершение
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver

# Пример использования
driver = Driver(...)
category = SimpleNamespace(title="Заголовок", description="Описание")
products = [SimpleNamespace(local_image_path="path/to/image.jpg")]
result = promote_post(driver, category, products)
print(result)  # Вывод: True или None
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

**Назначение**: Управляет процессом создания и публикации сообщения в Facebook, включая добавление заголовка, описания и медиафайлов.

**Параметры**:

-   `d` (Driver): Инстанс драйвера веб-браузера Selenium для управления браузером.
-   `message` (SimpleNamespace): Объект `SimpleNamespace`, содержащий информацию о заголовке, описании и медиафайлах сообщения.
-   `no_video` (bool, optional): Если `True`, видео не будут загружены. По умолчанию `False`.
-   `images` (Optional[str | list[str]], optional): Путь к изображению или список путей. По умолчанию `None`.
-   `without_captions` (bool, optional): Если `True`, подписи к изображениям не будут обновлены. По умолчанию `False`.

**Возвращает**:

-   `bool`: `True`, если публикация прошла успешно.

**Как работает функция**:

1.  **Отправка заголовка и описания**: Вызывает функцию `post_title` для отправки заголовка и описания сообщения.
2.  **Загрузка медиафайлов**: Вызывает функцию `upload_media` для загрузки медиафайлов, используя `message.products`.
3.  **Проверка наличия одного изображения**: Если загружено только одно изображение, кликает на кнопку отправки и завершает работу.
4.  **Клик на кнопку завершения редактирования**: Кликает на кнопку, завершающую редактирование сообщения.
5.  **Публикация сообщения**: Вызывает функцию `publish` для публикации сообщения.

**ASII flowchart**:

```
A: Отправка заголовка и описания
↓
B: Загрузка медиафайлов
↓
C: Проверка наличия одного изображения
│
└──> D1: Клик на кнопку отправки (если одно изображение)
│   ↓
│   E1: Завершение
↓
D2: Клик на кнопку завершения редактирования
↓
E2: Публикация сообщения
↓
F: Завершение
```

**Примеры**:

```python
from types import SimpleNamespace
from src.webdriver.driver import Driver

# Пример использования
driver = Driver(...)
message = SimpleNamespace(
    title="Заголовок сообщения",
    description="Описание сообщения",
    products=[SimpleNamespace(local_image_path="path/to/image.jpg")],
)
result = post_message(driver, message)
print(result)  # Вывод: True или None