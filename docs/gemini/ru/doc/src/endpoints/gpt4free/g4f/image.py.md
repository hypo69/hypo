# Модуль для работы с изображениями
=====================================

Модуль предоставляет функциональность для обработки и конвертации изображений, включая проверку формата, извлечение данных из URI, изменение размера и т.д.
Модуль содержит класс :class:`ImageDataResponse`, который используется для обработки ответов, содержащих изображения, и класс :class:`ImageRequest`, который используется для обработки запросов изображений.

## Обзор

Модуль `image.py` предоставляет инструменты для работы с изображениями различных форматов, включая PNG, JPG, JPEG, GIF, WEBP и SVG. Он включает функции для конвертации изображений, проверки их формата, извлечения данных из URI, изменения размера и обработки ориентации.
Модуль предназначен для работы с изображениями, полученными из разных источников, таких как файлы, байтовые данные или URI данных.

## Подробнее

Модуль предоставляет набор функций и классов для работы с изображениями, включая:

- Конвертацию изображений в различные форматы.
- Проверку допустимости расширений файлов изображений.
- Извлечение бинарных данных из URI данных.
- Изменение размера и обработку ориентации изображений.
- Преобразование изображений в байты и URI данных.

Модуль используется для обработки и подготовки изображений для использования в других частях проекта.

## Классы

### `ImageDataResponse`

**Описание**: Класс предназначен для хранения и обработки данных об изображении, таких как список изображений и альтернативный текст.

**Принцип работы**:
Класс `ImageDataResponse` инициализируется с списком URL-адресов изображений и альтернативным текстом. Он предоставляет метод `get_list`, который возвращает список URL-адресов изображений, преобразуя одиночный URL-адрес в список, если это необходимо.

**Аттрибуты**:

- `images` (Union[str, list]): URL-адрес изображения или список URL-адресов изображений.
- `alt` (str): Альтернативный текст для изображения.

**Методы**:

- `get_list()`: Возвращает список URL-адресов изображений.

### `ImageRequest`

**Описание**: Класс предназначен для хранения и обработки опций запроса изображений.

**Принцип работы**:
Класс `ImageRequest` инициализируется со словарём опций. Он предоставляет метод `get`, который возвращает значение опции по ключу, если она существует.

**Аттрибуты**:

- `options` (dict): Словарь опций запроса.

**Методы**:

- `get(key: str)`: Возвращает значение опции по ключу.

## Функции

### `to_image`

```python
def to_image(image: ImageType, is_svg: bool = False) -> Image:
    """
    Converts the input image to a PIL Image object.

    Args:
        image (Union[str, bytes, Image]): The input image.

    Returns:
        Image: The converted PIL Image object.
    """
```

**Назначение**: Преобразует входное изображение в объект PIL Image.

**Параметры**:

- `image` (ImageType): Входное изображение, которое может быть строкой (путь к файлу), байтами или объектом PIL Image.
- `is_svg` (bool, optional): Указывает, является ли изображение SVG. По умолчанию `False`.

**Возвращает**:

- `Image`: Преобразованный объект PIL Image.

**Вызывает исключения**:

- `MissingRequirementsError`: Если не установлены необходимые пакеты (`pillow` или `cairosvg` для SVG).
- `ValueError`: Если URI данных изображения недопустим.

**Как работает функция**:

1. **Проверка зависимостей**:
   - Проверяет, установлен ли пакет `pillow`. Если нет, вызывает исключение `MissingRequirementsError`.
2. **Обработка URI данных**:
   - Если изображение является строкой и начинается с "data:", проверяет, является ли URI данных изображением, и извлекает данные из URI.
3. **Обработка SVG**:
   - Если `is_svg` равно `True`, пытается импортировать `cairosvg`. Если не удается, вызывает `MissingRequirementsError`.
   - Преобразует SVG-изображение в PNG, используя `cairosvg`, и открывает его как PIL Image.
4. **Обработка байтов**:
   - Если изображение является байтами, проверяет, является ли формат изображения допустимым, и открывает его как PIL Image.
5. **Обработка PIL Image**:
   - Если изображение уже является объектом PIL Image, возвращает его без изменений.
6. **Обработка пути к файлу**:
   - Если изображение является путем к файлу (строкой), открывает его как PIL Image.

**ASCII flowchart**:

```
A: Проверка pillow
|
-- B: Обработка data URI (если есть)
|
-- C: Обработка SVG (если is_svg)
|
-- D: Обработка bytes
|
-- E: Обработка PIL Image
|
-- F: Обработка пути к файлу
|
G: Возврат PIL Image
```

**Примеры**:

```python
from PIL.Image import Image
from pathlib import Path

# Пример 1: Преобразование изображения из пути к файлу
image_path = "image.png"
image = to_image(image_path)

# Пример 2: Преобразование изображения из байтов
with open(image_path, "rb") as f:
    image_bytes = f.read()
image = to_image(image_bytes)

# Пример 3: Преобразование изображения из объекта PIL Image
image = to_image(image)  # Предполагаем, что image уже является объектом PIL Image
```

### `is_allowed_extension`

```python
def is_allowed_extension(filename: str) -> bool:
    """
    Checks if the given filename has an allowed extension.

    Args:
        filename (str): The filename to check.

    Returns:
        bool: True if the extension is allowed, False otherwise.
    """
```

**Назначение**: Проверяет, имеет ли заданное имя файла допустимое расширение.

**Параметры**:

- `filename` (str): Имя файла для проверки.

**Возвращает**:

- `bool`: `True`, если расширение допустимо, `False` в противном случае.

**Как работает функция**:

1. **Проверка наличия точки**:
   - Проверяет, содержит ли имя файла точку (`.`). Если нет, возвращает `False`.
2. **Извлечение расширения**:
   - Извлекает расширение файла, разделяя имя файла по последней точке.
3. **Проверка расширения**:
   - Приводит расширение к нижнему регистру и проверяет, содержится ли оно в множестве допустимых расширений `ALLOWED_EXTENSIONS`.

**ASCII flowchart**:

```
A: Проверка наличия точки
|
-- B: Извлечение расширения
|
C: Проверка расширения в ALLOWED_EXTENSIONS
|
D: Возврат True или False
```

**Примеры**:

```python
# Пример 1: Проверка имени файла с допустимым расширением
filename = "image.png"
is_allowed = is_allowed_extension(filename)  # Возвращает True

# Пример 2: Проверка имени файла с недопустимым расширением
filename = "document.txt"
is_allowed = is_allowed_extension(filename)  # Возвращает False
```

### `is_data_uri_an_image`

```python
def is_data_uri_an_image(data_uri: str) -> bool:
    """
    Checks if the given data URI represents an image.

    Args:
        data_uri (str): The data URI to check.

    Raises:
        ValueError: If the data URI is invalid or the image format is not allowed.
    """
```

**Назначение**: Проверяет, представляет ли заданный URI данных изображение.

**Параметры**:

- `data_uri` (str): URI данных для проверки.

**Вызывает исключения**:

- `ValueError`: Если URI данных недопустим или формат изображения не разрешен.

**Как работает функция**:

1. **Проверка формата URI данных**:
   - Использует регулярное выражение для проверки, начинается ли URI данных с "data:image/" и содержит ли формат изображения (например, jpeg, png, gif).
   - Если формат URI данных не соответствует ожидаемому, вызывает исключение `ValueError`.
2. **Извлечение формата изображения**:
   - Извлекает формат изображения из URI данных с использованием регулярного выражения.
3. **Проверка допустимости формата изображения**:
   - Преобразует формат изображения в нижний регистр и проверяет, содержится ли он в множестве допустимых расширений `ALLOWED_EXTENSIONS`.
   - Если формат изображения не является допустимым, вызывает исключение `ValueError`.

**ASCII flowchart**:

```
A: Проверка формата data URI
|
-- B: Извлечение формата изображения
|
C: Проверка допустимости формата изображения
|
D: Возврат True или вызов ValueError
```

**Примеры**:

```python
# Пример 1: Проверка допустимого URI данных изображения
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+b4AI1QNQzAwMDA9gJBAHQgvgEAMUgVFP0bXgAAAAASUVORK5CYII="
is_data_uri_an_image(data_uri)  # Не вызывает исключение

# Пример 2: Проверка недопустимого URI данных изображения
data_uri = "data:text/plain;base64,SGVsbG8sIHdvcmxkIQ=="
try:
    is_data_uri_an_image(data_uri)
except ValueError as ex:
    print(f"Error: {ex}")  # Вызывает ValueError: Invalid data URI image.

# Пример 3: Проверка URI данных изображения с недопустимым форматом
data_uri = "data:image/tiff;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+b4AI1QNQzAwMDA9gJBAHQgvgEAMUgVFP0bXgAAAAASUVORK5CYII="
try:
    is_data_uri_an_image(data_uri)
except ValueError as ex:
    print(f"Error: {ex}")  # Вызывает ValueError: Invalid image format (from mime file type).
```

### `is_accepted_format`

```python
def is_accepted_format(binary_data: bytes) -> str:
    """
    Checks if the given binary data represents an image with an accepted format.

    Args:
        binary_data (bytes): The binary data to check.

    Raises:
        ValueError: If the image format is not allowed.
    """
```

**Назначение**: Проверяет, представляет ли заданный двоичный код изображение с допустимым форматом.

**Параметры**:

- `binary_data` (bytes): Двоичные данные для проверки.

**Возвращает**:

- `str`: Строка, представляющая тип изображения (например, "image/jpeg", "image/png" и т. д.), если формат принят.

**Вызывает исключения**:

- `ValueError`: Если формат изображения не разрешен.

**Как работает функция**:

1. **Проверка сигнатур двоичных данных**:
   - Проверяет двоичные данные на наличие известных сигнатур для различных форматов изображений (JPEG, PNG, GIF, WEBP).
   - Если двоичные данные начинаются с определенной сигнатуры, функция возвращает соответствующий тип изображения.
2. **Обработка неизвестных форматов**:
   - Если двоичные данные не соответствуют ни одной из известных сигнатур, функция вызывает исключение `ValueError`, указывающее, что формат изображения не разрешен.

**ASCII flowchart**:

```
A: Проверка JPEG-сигнатуры
|
-- B: Проверка PNG-сигнатуры
|
-- C: Проверка GIF-сигнатуры
|
-- D: Проверка JPEG-сигнатуры (JFIF)
|
-- E: Проверка JPEG-сигнатуры (xFFxD8)
|
-- F: Проверка WEBP-сигнатуры
|
G: Вызов ValueError, если формат не распознан
```

**Примеры**:

```python
# Пример 1: Проверка JPEG-изображения
jpeg_data = b'\xFF\xD8\xFF\xE0\x00\x10JFIF...'
image_format = is_accepted_format(jpeg_data)  # Возвращает "image/jpeg"

# Пример 2: Проверка PNG-изображения
png_data = b'\x89PNG\r\n\x1a\n...'
image_format = is_accepted_format(png_data)  # Возвращает "image/png"

# Пример 3: Проверка неподдерживаемого формата
unknown_data = b'This is not an image...'
try:
    image_format = is_accepted_format(unknown_data)
except ValueError as ex:
    print(f"Error: {ex}")  # Вызывает ValueError: Invalid image format (from magic code).
```

### `extract_data_uri`

```python
def extract_data_uri(data_uri: str) -> bytes:
    """
    Extracts the binary data from the given data URI.

    Args:
        data_uri (str): The data URI.

    Returns:
        bytes: The extracted binary data.
    """
```

**Назначение**: Извлекает двоичные данные из заданного URI данных.

**Параметры**:

- `data_uri` (str): URI данных для извлечения.

**Возвращает**:

- `bytes`: Извлеченные двоичные данные.

**Как работает функция**:

1. **Разделение URI данных**:
   - Разделяет URI данных по запятой (`,`) и выбирает последнюю часть, которая содержит данные в кодировке base64.
2. **Декодирование Base64**:
   - Декодирует данные из кодировки base64 в двоичный формат.

**ASCII flowchart**:

```
A: Разделение data URI
|
B: Декодирование Base64
|
C: Возврат двоичных данных
```

**Примеры**:

```python
# Пример: Извлечение данных из data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+b4AI1QNQzAwMDA9gJBAHQgvgEAMUgVFP0bXgAAAAASUVORK5CYII="
binary_data = extract_data_uri(data_uri)
print(binary_data)
```

### `get_orientation`

```python
def get_orientation(image: Image) -> int:
    """
    Gets the orientation of the given image.

    Args:
        image (Image): The image.

    Returns:
        int: The orientation value.
    """
```

**Назначение**: Получает ориентацию заданного изображения.

**Параметры**:

- `image` (Image): Изображение для получения ориентации.

**Возвращает**:

- `int`: Значение ориентации.

**Как работает функция**:

1. **Извлечение данных EXIF**:
   - Пытается получить данные EXIF из изображения, используя `image.getexif()`, если атрибут существует, в противном случае использует `image._getexif()`.
2. **Получение ориентации**:
   - Если данные EXIF существуют, извлекает значение ориентации из тега 274, который соответствует тегу ориентации в EXIF.
3. **Возврат ориентации**:
   - Если значение ориентации найдено, возвращает его. В противном случае возвращает `None`.

**ASCII flowchart**:

```
A: Извлечение данных EXIF
|
B: Получение ориентации из данных EXIF
|
C: Возврат ориентации
```

**Примеры**:

```python
from PIL import Image

# Пример: Получение ориентации изображения
image = Image.open("image.jpg")
orientation = get_orientation(image)
if orientation:
    print(f"Orientation: {orientation}")
else:
    print("Orientation not found")
```

### `process_image`

```python
def process_image(image: Image, new_width: int, new_height: int) -> Image:
    """
    Processes the given image by adjusting its orientation and resizing it.

    Args:
        image (Image): The image to process.
        new_width (int): The new width of the image.
        new_height (int): The new height of the image.

    Returns:
        Image: The processed image.
    """
```

**Назначение**: Обрабатывает заданное изображение, корректируя его ориентацию и изменяя размер.

**Параметры**:

- `image` (Image): Изображение для обработки.
- `new_width` (int): Новая ширина изображения.
- `new_height` (int): Новая высота изображения.

**Возвращает**:

- `Image`: Обработанное изображение.

**Как работает функция**:

1. **Коррекция ориентации**:
   - Получает ориентацию изображения с помощью `get_orientation`.
   - Если ориентация найдена, применяет соответствующие преобразования (отражение, поворот) для исправления ориентации.
2. **Изменение размера изображения**:
   - Изменяет размер изображения до заданных `new_width` и `new_height` с помощью `image.thumbnail`.
3. **Удаление прозрачности**:
   - Если изображение имеет режим RGBA (прозрачность), создает новое изображение RGB с белым фоном и вставляет исходное изображение на него, удаляя прозрачность.
4. **Преобразование в RGB**:
   - Если изображение не имеет режим RGB, преобразует его в режим RGB.

**ASCII flowchart**:

```
A: Получение ориентации
|
-- B: Коррекция ориентации (если есть)
|
C: Изменение размера изображения
|
D: Удаление прозрачности (если RGBA)
|
E: Преобразование в RGB (если не RGB)
|
F: Возврат обработанного изображения
```

**Примеры**:

```python
from PIL import Image

# Пример: Обработка изображения
image = Image.open("image.png")
new_width = 200
new_height = 200
processed_image = process_image(image, new_width, new_height)
processed_image.save("processed_image.jpg")
```

### `to_bytes`

```python
def to_bytes(image: ImageType) -> bytes:
    """
    Converts the given image to bytes.

    Args:
        image (ImageType): The image to convert.

    Returns:
        bytes: The image as bytes.
    """
```

**Назначение**: Преобразует заданное изображение в байты.

**Параметры**:

- `image` (ImageType): Изображение для преобразования. Может быть байтами, строкой (путь к файлу или URI данных), объектом PIL Image или объектом Path.

**Возвращает**:

- `bytes`: Изображение в виде байтов.

**Как работает функция**:

1. **Проверка типа изображения**:
   - Если изображение уже является байтами, возвращает его без изменений.
   - Если изображение является строкой и начинается с "data:", проверяет, является ли URI данных изображением, и извлекает двоичные данные из URI.
   - Если изображение является объектом PIL Image, сохраняет его во временный буфер в памяти и возвращает содержимое буфера в виде байтов.
   - Если изображение является строкой (путь к файлу) или объектом Path, читает содержимое файла в виде байтов.
   - В противном случае пытается прочитать содержимое изображения с помощью `image.read()`.

**ASCII flowchart**:

```
A: Проверка, является ли изображение байтами
|
-- B: Проверка, является ли изображение data URI
|
-- C: Проверка, является ли изображение PIL Image
|
-- D: Проверка, является ли изображение путем к файлу
|
E: Попытка чтения изображения с помощью image.read()
|
F: Возврат изображения в виде байтов
```

**Примеры**:

```python
from PIL import Image
from pathlib import Path

# Пример 1: Преобразование изображения из пути к файлу в байты
image_path = "image.png"
image_bytes = to_bytes(image_path)

# Пример 2: Преобразование изображения из объекта PIL Image в байты
image = Image.open(image_path)
image_bytes = to_bytes(image)

# Пример 3: Преобразование изображения из URI данных в байты
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+b4AI1QNQzAwMDA9gJBAHQgvgEAMUgVFP0bXgAAAAASUVORK5CYII="
image_bytes = to_bytes(data_uri)
```

### `to_data_uri`

```python
def to_data_uri(image: ImageType) -> str:
    if not isinstance(image, str):
        data = to_bytes(image)
        data_base64 = base64.b64encode(data).decode()
        return f"data:{is_accepted_format(data)};base64,{data_base64}"
    return image
```

**Назначение**: Преобразует заданное изображение в URI данных.

**Параметры**:

- `image` (ImageType): Изображение для преобразования. Может быть байтами, строкой (путь к файлу или URI данных), объектом PIL Image или объектом Path.

**Возвращает**:

- `str`: Изображение в виде URI данных.

**Как работает функция**:

1. **Проверка типа изображения**:
   - Если изображение уже является строкой, возвращает его без изменений.
   - Если изображение не является строкой, преобразует его в байты с помощью функции `to_bytes`.
   - Кодирует полученные байты в base64.
   - Определяет тип изображения, используя функцию `is_accepted_format`.
   - Формирует URI данных, объединяя тип изображения и закодированные в base64 данные.

**ASCII flowchart**:

```
A: Проверка, является ли изображение строкой
|
-- B: Преобразование изображения в байты
|
C: Кодирование байтов в base64
|
D: Определение типа изображения
|
E: Формирование data URI
|
F: Возврат data URI
```

**Примеры**:

```python
from PIL import Image

# Пример: Преобразование изображения из пути к файлу в data URI
image_path = "image.png"
data_uri = to_data_uri(image_path)

# Пример 2: Преобразование изображения из объекта PIL Image в data URI
image = Image.open(image_path)
data_uri = to_data_uri(image)