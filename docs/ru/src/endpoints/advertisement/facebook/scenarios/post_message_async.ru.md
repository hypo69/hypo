# Документация модуля `src.endpoints.advertisement.facebook.post_message_async`

## Обзор

Этот модуль предназначен для автоматизации процесса публикации сообщений на Facebook. Он позволяет отправлять заголовок и описание, загружать медиафайлы и продвигать пост. Модуль является частью директории `hypotez/src/endpoints/advertisement/facebook/scenarios`.

## Подробней

Модуль автоматизирует процесс продвижения постов на Facebook, начиная с отправки заголовка и описания, заканчивая загрузкой медиафайлов и их продвижением. Это полезно для автоматизации маркетинговых кампаний и поддержания актуальности контента на странице Facebook. Модуль использует веб-драйвер для взаимодействия с интерфейсом Facebook, что позволяет имитировать действия пользователя и автоматизировать рутинные задачи.

## Содержание

- [Функции](#Функции)
    - [`post_title`](#post_title)
    - [`upload_media`](#upload_media)
    - [`update_images_captions`](#update_images_captions)
    - [`promote_post`](#promote_post)

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения на Facebook.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        category (SimpleNamespace): Категория, содержащая заголовок и описание для отправки.

    Returns:
        bool: `True`, если заголовок и описание были успешно отправлены, иначе `None`.
    """
    ...
```

**Назначение**: Функция отправляет заголовок и описание кампании в поле сообщения на Facebook.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-браузера, используемый для взаимодействия с веб-страницей Facebook.
- `category` (SimpleNamespace): Объект SimpleNamespace, содержащий атрибуты `title` (заголовок) и `description` (описание) для отправки в поле сообщения.

**Возвращает**:

- `bool`: Возвращает `True`, если заголовок и описание успешно отправлены, иначе `None`.

**Как работает функция**:

1. **Инициализация**: Функция принимает экземпляр драйвера и объект категории с заголовком и описанием.
2. **Отправка заголовка и описания**: Функция использует методы драйвера для поиска элементов на веб-странице и отправки в них заголовка и описания из объекта категории.
3. **Проверка успешности**: После отправки данных функция проверяет, успешно ли отправлены заголовок и описание.
4. **Возврат значения**: Функция возвращает `True`, если отправка прошла успешно, иначе `None`.

**ASCII flowchart**:

```
Начало
  ↓
Получение драйвера и категории
  ↓
Отправка заголовка и описания в поле сообщения Facebook
  ↓
Проверка успешности отправки
  ↓
Возврат True или None
  ↓
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация Driver (пример)
driver = Driver(...)

# Создание объекта category
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")

# Вызов функции
result = post_title(driver, category)
if result:
    print("Заголовок и описание успешно отправлены")
else:
    print("Не удалось отправить заголовок и описание")
```

### `upload_media`

```python
def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Загружает медиафайлы на пост Facebook и обновляет их подписи.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
        no_video (bool, optional): Флаг, указывающий, следует ли пропустить загрузку видео. По умолчанию `False`.

    Returns:
        bool: `True`, если медиафайлы были успешно загружены, иначе `None`.
    """
    ...
```

**Назначение**: Функция загружает медиафайлы (изображения и видео) на пост Facebook.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-браузера для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов SimpleNamespace, содержащих пути к медиафайлам для загрузки.
- `no_video` (bool, optional): Флаг, указывающий, нужно ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:

- `bool`: Возвращает `True`, если медиафайлы успешно загружены, иначе `None`.

**Как работает функция**:

1. **Инициализация**: Функция принимает экземпляр драйвера и список продуктов с путями к медиафайлам.
2. **Загрузка медиафайлов**: Функция использует методы драйвера для поиска элементов на веб-странице и загрузки медиафайлов из указанных путей.
3. **Проверка успешности**: После загрузки каждого файла функция проверяет, успешно ли загружен файл.
4. **Возврат значения**: Функция возвращает `True`, если все медиафайлы загружены успешно, иначе `None`.

**ASCII flowchart**:

```
Начало
  ↓
Получение драйвера и списка продуктов
  ↓
Загрузка медиафайлов (изображений и видео)
  ↓
Проверка успешности загрузки каждого файла
  ↓
Возврат True или None
  ↓
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace
from typing import List

# Инициализация Driver (пример)
driver = Driver(...)

# Создание списка продуктов
products: List[SimpleNamespace] = [
    SimpleNamespace(local_image_path='путь/к/изображению1.jpg'),
    SimpleNamespace(local_image_path='путь/к/изображению2.jpg'),
    SimpleNamespace(local_video_path='путь/к/видео.mp4')
]

# Вызов функции
result = upload_media(driver, products, no_video=False)
if result:
    print("Медиафайлы успешно загружены")
else:
    print("Не удалось загрузить медиафайлы")
```

### `update_images_captions`

```python
def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Асинхронно добавляет описания к загруженным медиафайлам.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов с деталями для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, куда добавляются подписи.
    """
    ...
```

**Назначение**: Функция добавляет описания к загруженным медиафайлам на Facebook.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-браузера для взаимодействия с веб-страницей.
- `products` (List[SimpleNamespace]): Список объектов SimpleNamespace, содержащих детали для обновления (например, описания).
- `textarea_list` (List[WebElement]): Список элементов textarea, в которые нужно добавить описания.

**Возвращает**:

- `None`: Функция ничего не возвращает.

**Как работает функция**:

1. **Инициализация**: Функция принимает экземпляр драйвера, список продуктов с деталями и список текстовых полей.
2. **Обновление подписей**: Функция использует методы драйвера для поиска элементов на веб-странице и добавления описаний из списка продуктов в соответствующие текстовые поля.
3. **Завершение**: Функция завершает работу после обновления всех подписей.

**ASCII flowchart**:

```
Начало
  ↓
Получение драйвера, списка продуктов и списка текстовых полей
  ↓
Добавление описаний к медиафайлам в текстовые поля
  ↓
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace
from typing import List
from selenium.webdriver.remote.webelement import WebElement

# Инициализация Driver (пример)
driver = Driver(...)

# Создание списка продуктов
products: List[SimpleNamespace] = [
    SimpleNamespace(description="Описание для изображения 1"),
    SimpleNamespace(description="Описание для изображения 2")
]

# Создание списка текстовых полей (пример)
textarea_list: List[WebElement] = [...]  # Заполните список WebElement

# Вызов функции
update_images_captions(driver, products, textarea_list)
print("Подписи к изображениям успешно обновлены")
```

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
        no_video (bool, optional): Флаг, указывающий, следует ли пропустить загрузку видео. По умолчанию `False`.

    Returns:
        bool: `True`, если пост был успешно продвинут, иначе `None`.
    """
    ...
```

**Назначение**: Функция управляет процессом продвижения поста с заголовком, описанием и медиафайлами на Facebook.

**Параметры**:

- `d` (Driver): Экземпляр драйвера веб-браузера для взаимодействия с веб-страницей.
- `category` (SimpleNamespace): Объект SimpleNamespace, содержащий детали категории для заголовка и описания поста.
- `products` (List[SimpleNamespace]): Список объектов SimpleNamespace, содержащих медиа и детали для публикации.
- `no_video` (bool, optional): Флаг, указывающий, следует ли пропустить загрузку видео. По умолчанию `False`.

**Возвращает**:

- `bool`: Возвращает `True`, если пост был успешно продвинут, иначе `None`.

**Как работает функция**:

1. **Инициализация**: Функция принимает экземпляр драйвера, объект категории и список продуктов с деталями.
2. **Выполнение шагов продвижения**: Функция выполняет шаги, необходимые для продвижения поста, такие как отправка заголовка, загрузка медиа и обновление подписей.
3. **Проверка успешности**: После выполнения всех шагов функция проверяет, успешно ли продвинут пост.
4. **Возврат значения**: Функция возвращает `True`, если пост успешно продвинут, иначе `None`.

**ASCII flowchart**:

```
Начало
  ↓
Получение драйвера, категории и списка продуктов
  ↓
Отправка заголовка и описания
  ↓
Загрузка медиафайлов
  ↓
Обновление подписей к медиафайлам
  ↓
Выполнение шагов продвижения поста
  ↓
Проверка успешности продвижения
  ↓
Возврат True или None
  ↓
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace
from typing import List

# Инициализация Driver (пример)
driver = Driver(...)

# Создание объекта category
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")

# Создание списка продуктов
products: List[SimpleNamespace] = [
    SimpleNamespace(local_image_path='путь/к/изображению1.jpg', description="Описание 1"),
    SimpleNamespace(local_image_path='путь/к/изображению2.jpg', description="Описание 2")
]

# Вызов функции
result = promote_post(driver, category, products, no_video=False)
if result:
    print("Пост успешно продвинут")
else:
    print("Не удалось продвинуть пост")