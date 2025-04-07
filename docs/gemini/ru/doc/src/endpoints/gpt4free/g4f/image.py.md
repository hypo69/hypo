# Модуль для обработки изображений

## Обзор

Модуль `image.py` предоставляет инструменты для работы с изображениями, включая преобразование форматов, изменение размеров, проверку допустимости форматов и извлечение данных из URI. Он использует библиотеку PIL (Pillow) для обработки изображений и включает поддержку SVG с использованием cairosvg.

## Подробней

Этот модуль разработан для обработки изображений, получаемых из различных источников, и приведения их к нужному формату для дальнейшего использования в проекте `hypotez`. Он обеспечивает проверку форматов, преобразование в PIL Image объекты, изменение размеров и извлечение данных из Data URI. Модуль также поддерживает работу с SVG изображениями, требуя установки дополнительных зависимостей.
В данном коде широко используются библиотеки `PIL (Pillow)` и `cairosvg`. Если не установлены - будет выкинута ошибка `MissingRequirementsError`
Так же в модуле реализована поддержка Data URI и преобразование изображений в байты и обратно.

## Классы

### `ImageDataResponse`

**Описание**: Класс, представляющий собой ответ с данными изображения.

**Атрибуты**:
- `images` (Union[str, list]): Изображение или список изображений.
- `alt` (str): Альтернативный текст для изображения.

**Методы**:
- `get_list()`: Возвращает список изображений. Если `images` является строкой, то возвращается список, содержащий эту строку.

```python
class ImageDataResponse():
    """
    Args:
        images (Union[str, list]): Изображение или список изображений.
        alt (str): Альтернативный текст для изображения.
    """
    def __init__(
        self,
        images: Union[str, list],
        alt: str,
    ):
        self.images = images
        self.alt = alt

    def get_list(self) -> list[str]:
        """Возвращает список изображений. Если `self.images` является строкой, то возвращается список, содержащий эту строку.
        Returns:
            list[str]: Список изображений.
        """
        return [self.images] if isinstance(self.images, str) else self.images
```

### `ImageRequest`

**Описание**: Класс для представления запроса изображения с опциями.

**Атрибуты**:
- `options` (dict): Словарь с опциями запроса.

**Методы**:
- `get(key: str)`: Возвращает значение опции по ключу.

```python
class ImageRequest():
    """
    Args:
        options (dict, optional): Словарь с опциями запроса. По умолчанию `{}`.
    """
    def __init__(
        self,
        options: dict = {}
    ):
        self.options = options

    def get(self, key: str):
        """Возвращает значение опции по ключу.
        Args:
            key (str): Ключ опции.

        Returns:
            Any: Значение опции или `None`, если ключ не найден.
        """
        return self.options.get(key)
```

## Функции

### `to_image`

```python
def to_image(image: ImageType, is_svg: bool = False) -> Image:
    """
    Args:
        image (Union[str, bytes, Image]): Изображение, которое необходимо преобразовать. Может быть путем к файлу, байтами или объектом PIL Image.
        is_svg (bool, optional): Указывает, является ли изображение SVG. По умолчанию `False`.

    Returns:
        Image: Объект PIL Image, представляющий преобразованное изображение.

    Raises:
        MissingRequirementsError: Если отсутствует библиотека `pillow` для работы с изображениями или `cairosvg` для работы с SVG.
        ValueError: Если Data URI имеет неверный формат или недопустимый формат изображения.
    """
```

**Назначение**: Преобразует входное изображение в объект PIL Image.

**Параметры**:
- `image` (ImageType): Изображение для преобразования. Может быть строкой (путь к файлу или data URI), байтами или объектом PIL Image.
- `is_svg` (bool): Флаг, указывающий, является ли изображение SVG. По умолчанию `False`.

**Возвращает**:
- `Image`: Объект PIL Image, представляющий преобразованное изображение.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлены необходимые библиотеки (`pillow` или `cairosvg`).
- `ValueError`: Если передан некорректный URI.
- `Exception`: Если возникает ошибка при открытии файла изображения.

**Как работает функция**:

1. **Проверка зависимостей**: Проверяет, установлена ли библиотека `pillow`. Если нет, вызывает исключение `MissingRequirementsError`.
2. **Обработка Data URI**: Если изображение является строкой и начинается с "data:", проверяет и извлекает данные из URI.
3. **Обработка SVG**: Если `is_svg` равен `True`, пытается импортировать `cairosvg` и преобразует SVG в PNG.
4. **Обработка байтов**: Если изображение является байтами, проверяет формат и открывает как PIL Image.
5. **Обработка PIL Image**: Если изображение уже является PIL Image, возвращает его.
6. **Открытие изображения**: Если изображение является путем к файлу, открывает его с помощью PIL.

**ASCII flowchart**:

```
A [Проверка наличия pillow]
|
B [Обработка Data URI?] -- No --> C [Обработка SVG?] -- No --> D [Обработка байтов?] -- No --> E [Обработка PIL Image?] -- No --> F [Открытие изображения]
| Yes                               | Yes                                | Yes                                   | Yes                              |
|
G [Проверка Data URI]               H [Импорт и преобразование SVG]     I [Проверка формата]                    J [Возврат PIL Image]             K [Возврат PIL Image]
|
L [Извлечение данных URI]           M [Открытие PIL Image из буфера]
|
N [Открытие PIL Image из данных]
```

**Примеры**:

```python
from pathlib import Path
from PIL import Image

# Пример 1: Преобразование изображения из файла
image_path = Path("example.jpg")  # Создайте файл example.jpg в той же директории
image = to_image(image_path)
print(type(image))

# Пример 2: Преобразование изображения из байтов
with open(image_path, "rb") as f:
    image_bytes = f.read()
image = to_image(image_bytes)
print(type(image))

# Пример 3: Преобразование изображения из объекта PIL Image
image_pil = Image.open(image_path)
image = to_image(image_pil)
print(type(image))
```

### `is_allowed_extension`

```python
def is_allowed_extension(filename: str) -> bool:
    """
    Args:
        filename (str): Имя файла для проверки.

    Returns:
        bool: `True`, если расширение допустимо, `False` в противном случае.
    """
```

**Назначение**: Проверяет, имеет ли указанное имя файла допустимое расширение.

**Параметры**:
- `filename` (str): Имя файла для проверки.

**Возвращает**:
- `bool`: `True`, если расширение допустимо, `False` в противном случае.

**Как работает функция**:

1. **Проверка наличия точки**: Убеждается, что в имени файла есть точка (`.`).
2. **Извлечение расширения**: Извлекает расширение файла (часть после последней точки).
3. **Проверка расширения**: Сравнивает расширение с допустимыми расширениями из `ALLOWED_EXTENSIONS`.

**ASCII flowchart**:

```
A [Проверка наличия точки]
|
B [Извлечение расширения]
|
C [Проверка расширения в ALLOWED_EXTENSIONS]
```

**Примеры**:

```python
# Пример 1: Проверка допустимого расширения
filename = "image.png"
is_allowed = is_allowed_extension(filename)
print(is_allowed)

# Пример 2: Проверка недопустимого расширения
filename = "document.txt"
is_allowed = is_allowed_extension(filename)
print(is_allowed)
```

### `is_data_uri_an_image`

```python
def is_data_uri_an_image(data_uri: str) -> bool:
    """
    Args:
        data_uri (str): Data URI для проверки.

    Raises:
        ValueError: Если Data URI имеет неверный формат или недопустимый формат изображения.
    """
```

**Назначение**: Проверяет, является ли указанный data URI изображением.

**Параметры**:
- `data_uri` (str): Data URI для проверки.

**Вызывает исключения**:
- `ValueError`: Если Data URI имеет неверный формат или недопустимый формат изображения.

**Как работает функция**:

1. **Проверка формата URI**: Проверяет, начинается ли URI с `data:image/` и содержит ли формат изображения.
2. **Извлечение формата**: Извлекает формат изображения из URI.
3. **Проверка формата**: Проверяет, является ли формат допустимым (есть в `ALLOWED_EXTENSIONS` или является "svg+xml").

**ASCII flowchart**:

```
A [Проверка формата URI]
|
B [Извлечение формата]
|
C [Проверка формата в ALLOWED_EXTENSIONS или "svg+xml"]
```

**Примеры**:

```python
# Пример 1: Проверка допустимого Data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+r8jAwODQ0MDAwMAEUQBcOb9w6jgAAAAABJRU5ErkJggg=="
try:
    is_data_uri_an_image(data_uri)
    print("Valid data URI")
except ValueError as ex:
    print(f"Invalid data URI: {ex}")

# Пример 2: Проверка недопустимого Data URI
data_uri = "data:text/plain;base64,SGVsbG8sIHdvcmxkIQ=="
try:
    is_data_uri_an_image(data_uri)
    print("Valid data URI")
except ValueError as ex:
    print(f"Invalid data URI: {ex}")
```

### `is_accepted_format`

```python
def is_accepted_format(binary_data: bytes) -> str:
    """
    Args:
        binary_data (bytes): Двоичные данные для проверки.

    Returns:
        str: MIME тип изображения, если формат допустим.

    Raises:
        ValueError: Если формат изображения недопустим.
    """
```

**Назначение**: Проверяет, представляет ли двоичные данные изображение с допустимым форматом.

**Параметры**:
- `binary_data` (bytes): Двоичные данные для проверки.

**Возвращает**:
- `str`: MIME тип изображения, если формат допустим.

**Вызывает исключения**:
- `ValueError`: Если формат изображения недопустим.

**Как работает функция**:

1. **Проверка сигнатур**: Проверяет двоичные данные на наличие известных сигнатур для различных форматов изображений (JPEG, PNG, GIF, WEBP).

**ASCII flowchart**:

```
A [Проверка JPEG сигнатуры]
| No
B [Проверка PNG сигнатуры]
| No
C [Проверка GIF сигнатуры]
| No
D [Проверка JPEG сигнатуры (JFIF)]
| No
E [Проверка WEBP сигнатуры]
| No
F [Вызов ValueError]
```

**Примеры**:

```python
# Пример 1: Проверка JPEG изображения
jpeg_data = b'\xFF\xD8\xFF\xE0\x00\x10JFIF'
try:
    image_format = is_accepted_format(jpeg_data)
    print(f"Image format: {image_format}")
except ValueError as ex:
    print(f"Invalid image format: {ex}")

# Пример 2: Проверка недопустимых данных
invalid_data = b'This is not an image'
try:
    image_format = is_accepted_format(invalid_data)
    print(f"Image format: {image_format}")
except ValueError as ex:
    print(f"Invalid image format: {ex}")
```

### `extract_data_uri`

```python
def extract_data_uri(data_uri: str) -> bytes:
    """
    Args:
        data_uri (str): Data URI для извлечения.

    Returns:
        bytes: Извлеченные двоичные данные.
    """
```

**Назначение**: Извлекает двоичные данные из data URI.

**Параметры**:
- `data_uri` (str): Data URI для извлечения.

**Возвращает**:
- `bytes`: Извлеченные двоичные данные.

**Как работает функция**:

1. **Разделение URI**: Разделяет data URI на части, используя `,` в качестве разделителя, и берет последнюю часть (данные в base64).
2. **Декодирование base64**: Декодирует данные из base64 в двоичный формат.

**ASCII flowchart**:

```
A [Разделение URI]
|
B [Декодирование base64]
```

**Примеры**:

```python
# Пример: Извлечение данных из Data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+r8jAwODQ0MDAwMAEUQBcOb9w6jgAAAAABJRU5ErkJggg=="
binary_data = extract_data_uri(data_uri)
print(f"Extracted binary data: {binary_data[:20]}...")
```

### `get_orientation`

```python
def get_orientation(image: Image) -> int:
    """
    Args:
        image (Image): Изображение для получения ориентации.

    Returns:
        int: Значение ориентации.
    """
```

**Назначение**: Получает ориентацию изображения из EXIF данных.

**Параметры**:
- `image` (Image): Изображение для получения ориентации.

**Возвращает**:
- `int`: Значение ориентации.

**Как работает функция**:

1. **Получение EXIF данных**: Пытается получить EXIF данные из изображения.
2. **Извлечение ориентации**: Извлекает значение тега ориентации (274) из EXIF данных.

**ASCII flowchart**:

```
A [Получение EXIF данных]
|
B [Извлечение ориентации]
```

**Примеры**:

```python
from pathlib import Path
from PIL import Image

# Пример: Получение ориентации изображения
image_path = Path("example.jpg")  # Создайте файл example.jpg в той же директории
image = Image.open(image_path)
orientation = get_orientation(image)
print(f"Image orientation: {orientation}")
```

### `process_image`

```python
def process_image(image: Image, new_width: int, new_height: int) -> Image:
    """
    Args:
        image (Image): Изображение для обработки.
        new_width (int): Новая ширина изображения.
        new_height (int): Новая высота изображения.

    Returns:
        Image: Обработанное изображение.
    """
```

**Назначение**: Обрабатывает изображение, корректируя ориентацию и изменяя размер.

**Параметры**:
- `image` (Image): Изображение для обработки.
- `new_width` (int): Новая ширина изображения.
- `new_height` (int): Новая высота изображения.

**Возвращает**:
- `Image`: Обработанное изображение.

**Как работает функция**:

1. **Коррекция ориентации**: Получает ориентацию изображения и применяет необходимые повороты и отражения.
2. **Изменение размера**: Изменяет размер изображения до указанных размеров.
3. **Удаление прозрачности**: Если изображение имеет прозрачность (RGBA), создает новое RGB изображение с белым фоном и вставляет исходное изображение.
4. **Преобразование в RGB**: Если изображение не в формате RGB, преобразует его.

**ASCII flowchart**:

```
A [Получение ориентации]
|
B [Коррекция ориентации]
|
C [Изменение размера]
|
D [Удаление прозрачности (RGBA)]
|
E [Преобразование в RGB]
```

**Примеры**:

```python
from pathlib import Path
from PIL import Image

# Пример: Обработка изображения
image_path = Path("example.jpg")  # Создайте файл example.jpg в той же директории
image = Image.open(image_path)
new_width = 200
new_height = 150
processed_image = process_image(image, new_width, new_height)
processed_image.save("processed_image.jpg")
```

### `to_bytes`

```python
def to_bytes(image: ImageType) -> bytes:
    """
    Args:
        image (ImageType): Изображение для преобразования в байты.

    Returns:
        bytes: Изображение в виде байтов.
    """
```

**Назначение**: Преобразует изображение в байты.

**Параметры**:
- `image` (ImageType): Изображение для преобразования в байты.

**Возвращает**:
- `bytes`: Изображение в виде байтов.

**Как работает функция**:

1. **Проверка типа**: Определяет тип входного изображения и выполняет соответствующее преобразование.
2. **Обработка различных типов**:
   - Если изображение уже является байтами, возвращает его.
   - Если изображение является строкой и начинается с "data:", извлекает данные из URI.
   - Если изображение является PIL Image, сохраняет в BytesIO и получает байты.
   - Если изображение является путем к файлу, читает файл и возвращает байты.
   - В противном случае пытается прочитать изображение как файл.

**ASCII flowchart**:

```
A [Проверка типа изображения]
|
B [ImageType is bytes?] -- Yes --> G [Возврат bytes]
| No
C [ImageType is data URI?] -- Yes --> H [Извлечение данных из URI и возврат bytes]
| No
D [ImageType is PIL Image?] -- Yes --> I [Сохранение в BytesIO и возврат bytes]
| No
E [ImageType is PathLike or str?] -- Yes --> J [Чтение файла и возврат bytes]
| No
F [Попытка чтения как файла и возврат bytes]
```

**Примеры**:

```python
from pathlib import Path
from PIL import Image

# Пример 1: Преобразование изображения из файла в байты
image_path = Path("example.jpg")  # Создайте файл example.jpg в той же директории
image_bytes = to_bytes(image_path)
print(f"Image bytes: {image_bytes[:20]}...")

# Пример 2: Преобразование PIL Image в байты
image = Image.open(image_path)
image_bytes = to_bytes(image)
print(f"Image bytes: {image_bytes[:20]}...")
```

### `to_data_uri`

```python
def to_data_uri(image: ImageType) -> str:
    """
    Args:
        image (ImageType): Изображение для преобразования в Data URI.

    Returns:
        str: Data URI изображения.
    """
```

**Назначение**: Преобразует изображение в Data URI.

**Параметры**:
- `image` (ImageType): Изображение для преобразования в Data URI.

**Возвращает**:
- `str`: Data URI изображения.

**Как работает функция**:

1. **Проверка типа**: Проверяет, является ли изображение строкой. Если да, возвращает его.
2. **Преобразование в байты**: Преобразует изображение в байты.
3. **Кодирование в base64**: Кодирует байты в base64.
4. **Формирование Data URI**: Формирует Data URI с MIME типом и закодированными данными.

**ASCII flowchart**:

```
A [Проверка типа изображения (is str?)]
| Yes
B [Возврат изображения (str)]
| No
C [Преобразование изображения в байты]
|
D [Кодирование байтов в base64]
|
E [Формирование Data URI]
|
F [Возврат Data URI]
```

**Примеры**:

```python
from pathlib import Path
from PIL import Image

# Пример: Преобразование изображения в Data URI
image_path = Path("example.png")  # Создайте файл example.png в той же директории
image = Image.open(image_path)
data_uri = to_data_uri(image)
print(f"Data URI: {data_uri[:50]}...")