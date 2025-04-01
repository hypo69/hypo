# Модуль для работы с изображениями

## Обзор

Модуль предоставляет набор функций для обработки изображений, включая конвертацию, проверку формата, извлечение данных из URI, изменение размера и преобразование в различные форматы. Он также включает классы для обработки запросов и ответов, связанных с изображениями.

## Подробней

Этот модуль используется для работы с изображениями в проекте. Он предоставляет функциональность для обработки изображений, включая преобразование в различные форматы, проверку допустимости форматов, извлечение данных из URI, изменение ориентации и размера изображений.
Модуль также включает классы `ImageDataResponse` и `ImageRequest` для обработки запросов и ответов, связанных с изображениями. Это позволяет унифицировать и упростить работу с изображениями в различных частях проекта.
Модуль использует библиотеку PIL (Pillow) для обработки изображений, а также библиотеки `cairosvg` для работы с SVG изображениями.

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
- `image` (str | bytes | Image): Входное изображение, которое может быть путем к файлу, байтами или объектом PIL Image.
- `is_svg` (bool, optional): Флаг, указывающий, является ли изображение SVG. По умолчанию `False`.

**Возвращает**:
- `Image`: Преобразованный объект PIL Image.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлены необходимые библиотеки (`pillow` для обычных изображений, `cairosvg` для SVG).
- `ValueError`: Если входное изображение имеет неверный формат URI данных.

**Как работает функция**:
1. Функция проверяет, установлены ли необходимые библиотеки (`pillow` для обычных изображений и `cairosvg` для SVG). Если какая-либо из библиотек не установлена, вызывается исключение `MissingRequirementsError`.
2. Если входное изображение является строкой и начинается с "data:", функция проверяет, является ли это изображение допустимым URI данных, и извлекает данные изображения.
3. Если изображение является SVG, используется `cairosvg` для преобразования SVG в PNG, и возвращается объект PIL Image.
4. Если изображение является байтами, проверяется допустимость формата изображения, и возвращается объект PIL Image.
5. Если изображение не является объектом PIL Image, оно открывается с помощью PIL и возвращается.
6. Если изображение уже является объектом PIL Image, оно возвращается без изменений.

**Примеры**:

```python
from PIL.Image import Image
from io import BytesIO
# Пример 1: Преобразование изображения из байтов
image_bytes = b'\x89PNG\r\n\x1a\n...'  # Замените реальными байтами PNG
image = to_image(image_bytes)
assert isinstance(image, Image)

# Пример 2: Преобразование изображения из пути к файлу
# Создайте временный файл изображения для примера
with open("temp_image.png", "wb") as f:
    f.write(b'\x89PNG\r\n\x1a\n...')  # Замените реальными байтами PNG
image = to_image("temp_image.png")
assert isinstance(image, Image)

# Пример 3: Преобразование изображения из объекта PIL Image
from PIL import Image as PILImage
image = PILImage.new('RGB', (60, 30), color='red')
image = to_image(image)
assert isinstance(image, Image)

# Пример 4: Преобразование SVG из байтов
image_bytes = b'<svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>'
image = to_image(image_bytes, is_svg=True)
assert isinstance(image, Image)
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
Функция проверяет, содержит ли имя файла точку (`.`) и входит ли расширение файла (после точки) в список допустимых расширений `ALLOWED_EXTENSIONS`.

**Примеры**:

```python
# Пример 1: Допустимое расширение
filename = "image.png"
result = is_allowed_extension(filename)
assert result is True

# Пример 2: Недопустимое расширение
filename = "document.txt"
result = is_allowed_extension(filename)
assert result is False

# Пример 3: Имя файла без расширения
filename = "image"
result = is_allowed_extension(filename)
assert result is False
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
- `ValueError`: Если URI данных недействителен или формат изображения не разрешен.

**Как работает функция**:
Функция проверяет, начинается ли URI данных с `data:image` и содержит ли допустимый формат изображения (например, jpeg, png, gif). Если URI данных не соответствует ожидаемому формату или формат изображения не разрешен, вызывается исключение `ValueError`. Функция использует регулярные выражения для проверки формата URI данных и извлечения формата изображения.

**Примеры**:

```python
# Пример 1: Допустимый data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+bAwP8G8v8AAQTQdQYlMQ=="
is_data_uri_an_image(data_uri)  # Не вызовет исключение

# Пример 2: Недопустимый data URI (не начинается с data:image)
data_uri = "text/plain;base64,SGVsbG8sIHdvcmxkIQ=="
try:
    is_data_uri_an_image(data_uri)
except ValueError as ex:
    assert str(ex) == "Invalid data URI image."

# Пример 3: Недопустимый data URI (недопустимый формат изображения)
data_uri = "data:image/tiff;base64,AAAA"
try:
    is_data_uri_an_image(data_uri)
except ValueError as ex:
    assert str(ex) == "Invalid image format (from mime file type)."
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

**Назначение**: Проверяет, представляет ли данный двоичный код изображение с допустимым форматом.

**Параметры**:
- `binary_data` (bytes): Двоичные данные для проверки.

**Возвращает**:
- `str`: MIME type изображения, если формат допустимый.

**Вызывает исключения**:
- `ValueError`: Если формат изображения не разрешен.

**Как работает функция**:
Функция проверяет двоичные данные изображения, чтобы определить его формат. Она проверяет начальные байты (magic numbers) данных, чтобы определить, является ли это изображение в формате JPEG, PNG, GIF или WebP. Если формат изображения не распознан, вызывается исключение `ValueError`.

**Примеры**:

```python
# Пример 1: JPEG изображение
jpeg_data = b'\xFF\xD8\xFF...'  # Замените реальными байтами JPEG
format = is_accepted_format(jpeg_data)
assert format == "image/jpeg"

# Пример 2: PNG изображение
png_data = b'\x89PNG\r\n\x1a\n...'  # Замените реальными байтами PNG
format = is_accepted_format(png_data)
assert format == "image/png"

# Пример 3: GIF изображение
gif_data = b'GIF87a...'  # Замените реальными байтами GIF
format = is_accepted_format(gif_data)
assert format == "image/gif"

# Пример 4: WebP изображение
webp_data = b'RIFF....WEBPVP8 '  # Замените реальными байтами WebP
format = is_accepted_format(webp_data)
assert format == "image/webp"

# Пример 5: Недопустимый формат изображения
invalid_data = b'InvalidData'
try:
    is_accepted_format(invalid_data)
except ValueError as ex:
    assert str(ex) == "Invalid image format (from magic code)."
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
- `data_uri` (str): URI данных.

**Возвращает**:
- `bytes`: Извлеченные двоичные данные.

**Как работает функция**:
Функция разделяет URI данных на основе запятой (`,`) и извлекает последнюю часть, которая содержит данные в кодировке base64. Затем она декодирует данные base64 и возвращает двоичные данные.

**Примеры**:

```python
# Пример 1: Извлечение данных из data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+bAwP8G8v8AAQTQdQYlMQ=="
binary_data = extract_data_uri(data_uri)
# binary_data будет содержать декодированные байты PNG изображения

# Пример 2: Проверка, что функция правильно декодирует данные
import base64
data = "hello world"
data_base64 = base64.b64encode(data.encode()).decode()
data_uri = f"data:text/plain;base64,{data_base64}"
extracted_data = extract_data_uri(data_uri)
assert extracted_data == b"hello world"
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

**Назначение**: Получает ориентацию данного изображения.

**Параметры**:
- `image` (Image): Изображение.

**Возвращает**:
- `int`: Значение ориентации.

**Как работает функция**:
Функция пытается получить данные EXIF из изображения. Если данные EXIF существуют, она извлекает значение тега ориентации (274) и возвращает его. Если данные EXIF отсутствуют или тег ориентации не найден, возвращается `None`.

**Примеры**:

```python
from PIL import Image as PILImage

# Создайте тестовое изображение
image = PILImage.new('RGB', (100, 100), color='white')

# Пример 1: Изображение без EXIF данных
orientation = get_orientation(image)
assert orientation is None

# Пример 2: Изображение с EXIF данными (нужно создать EXIF данные и присвоить их изображению)
from PIL import ExifTags
exif_data = {
    ExifTags.Base.Orientation: 6  # Значение 6 соответствует повороту на 90 градусов
}
image.info["exif"] = image.getexif()
image.info["exif"][ExifTags.Base.Orientation] = 6
orientation = get_orientation(image)
# В этом случае orientation должно быть 6, если EXIF данные правильно установлены
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

**Назначение**: Обрабатывает данное изображение, корректируя его ориентацию и изменяя размер.

**Параметры**:
- `image` (Image): Изображение для обработки.
- `new_width` (int): Новая ширина изображения.
- `new_height` (int): Новая высота изображения.

**Возвращает**:
- `Image`: Обработанное изображение.

**Как работает функция**:
1. **Коррекция ориентации**: Функция получает ориентацию изображения с помощью `get_orientation(image)`. Если ориентация определена, она корректирует изображение, используя методы `transpose` из PIL для поворота или отражения изображения в соответствии со значением ориентации.
2. **Изменение размера изображения**: Функция изменяет размер изображения до заданных значений `new_width` и `new_height`, используя метод `thumbnail`.
3. **Удаление прозрачности**: Если изображение имеет режим `RGBA` (включая альфа-канал), функция создает новое изображение `RGB` белого цвета и вставляет исходное изображение в него, используя альфа-канал в качестве маски. Это удаляет прозрачность, заменяя ее белым фоном.
4. **Преобразование в RGB**: Если изображение не в режиме `RGB`, функция преобразует его в режим `RGB`.
5. Функция возвращает обработанное изображение.

**Примеры**:

```python
from PIL import Image as PILImage

# Создайте тестовое изображение
image = PILImage.new('RGBA', (100, 100), color=(0, 0, 0, 0))  # Прозрачное изображение

# Пример 1: Обработка изображения без изменения ориентации
new_width = 50
new_height = 50
processed_image = process_image(image, new_width, new_height)
assert processed_image.size == (new_width, new_height)
assert processed_image.mode == 'RGB'

# Пример 2: Обработка изображения с изменением ориентации (нужно создать EXIF данные и присвоить их изображению)
from PIL import ExifTags
from PIL import Image as PILImage

image = PILImage.new('RGBA', (100, 100), color=(0, 0, 0, 0))
exif_data = {
    ExifTags.Base.Orientation: 6  # Значение 6 соответствует повороту на 90 градусов
}
image.info["exif"] = image.getexif()
image.info["exif"][ExifTags.Base.Orientation] = 6
new_width = 50
new_height = 50
processed_image = process_image(image, new_width, new_height)
assert processed_image.size == (new_width, new_height)
assert processed_image.mode == 'RGB'
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

**Назначение**: Преобразует данное изображение в байты.

**Параметры**:
- `image` (ImageType): Изображение для преобразования. Может быть `bytes`, `str`, `os.PathLike`, `Path` или `Image`.

**Возвращает**:
- `bytes`: Изображение в виде байтов.

**Как работает функция**:
Функция проверяет тип входного изображения и преобразует его в байты соответствующим образом:
1. Если изображение уже является байтами, оно возвращается без изменений.
2. Если изображение является строкой, начинающейся с "data:", оно извлекается из URI данных.
3. Если изображение является объектом PIL Image, оно сохраняется в BytesIO и возвращается в виде байтов.
4. Если изображение является строкой или `os.PathLike`, оно читается из файла по указанному пути и возвращается в виде байтов.
5. Если изображение является объектом Path, оно читается из файла и возвращается в виде байтов.
6. В противном случае, если у объекта изображения есть метод `read`, он вызывается для чтения данных в виде байтов.

**Примеры**:

```python
from PIL import Image as PILImage
from io import BytesIO
from pathlib import Path
import os

# Пример 1: Преобразование изображения из байтов
image_bytes = b'\x89PNG\r\n\x1a\n...'  # Замените реальными байтами PNG
result = to_bytes(image_bytes)
assert isinstance(result, bytes)

# Пример 2: Преобразование изображения из строки (путь к файлу)
# Сначала создадим временный файл для примера
with open("temp_image.png", "wb") as f:
    f.write(b'\x89PNG\r\n\x1a\n...')  # Замените реальными байтами PNG
result = to_bytes("temp_image.png")
assert isinstance(result, bytes)

# Пример 3: Преобразование изображения из объекта PIL Image
image = PILImage.new('RGB', (60, 30), color='red')
result = to_bytes(image)
assert isinstance(result, bytes)

# Пример 4: Преобразование изображения из объекта Path
path = Path("temp_image.png")  # Используем тот же временный файл, что и раньше
result = to_bytes(path)
assert isinstance(result, bytes)

# Пример 5: Преобразование изображения из data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+bAwP8G8v8AAQTQdQYlMQ=="
result = to_bytes(data_uri)
assert isinstance(result, bytes)
```

### `to_data_uri`

```python
def to_data_uri(image: ImageType) -> str:
    """
    <инструкция для модели gemini:Напиши docstring для функции `to_data_uri`. Docstring должен быть на русском языке>
    """
    if not isinstance(image, str):
        data = to_bytes(image)
        data_base64 = base64.b64encode(data).decode()
        return f"data:{is_accepted_format(data)};base64,{data_base64}"
    return image
```

**Назначение**: Преобразует изображение в data URI.

**Параметры**:
- `image` (ImageType): Изображение для преобразования.

**Возвращает**:
- `str`: Изображение в виде data URI.

**Как работает функция**:
Если входное изображение не является строкой, оно сначала преобразуется в байты с помощью функции `to_bytes`. Затем байты кодируются в base64, и формируется строка data URI, включающая MIME-тип изображения, полученный с помощью `is_accepted_format`. Если входное изображение уже является строкой, оно возвращается без изменений.

**Примеры**:

```python
from PIL import Image as PILImage

# Пример 1: Преобразование изображения из объекта PIL Image
image = PILImage.new('RGB', (60, 30), color='red')
data_uri = to_data_uri(image)
assert data_uri.startswith("data:image/png;base64,")

# Пример 2: Преобразование изображения из байтов
image_bytes = b'\x89PNG\r\n\x1a\n...'  # Замените реальными байтами PNG
data_uri = to_data_uri(image_bytes)
assert data_uri.startswith("data:image/png;base64,")

# Пример 3: Преобразование строки (data URI)
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+bAwP8G8v8AAQTQdQYlMQ=="
result = to_data_uri(data_uri)
assert result == data_uri
```

## Классы

### `ImageDataResponse`

```python
class ImageDataResponse():
    def __init__(
        self,
        images: Union[str, list],
        alt: str,
    ):
        self.images = images
        self.alt = alt

    def get_list(self) -> list[str]:
        return [self.images] if isinstance(self.images, str) else self.images
```

**Описание**: Класс для представления ответа, содержащего данные изображения.

**Принцип работы**:
Класс `ImageDataResponse` используется для хранения данных об изображении, таких как URL изображения и альтернативный текст. Конструктор класса принимает URL изображения (или список URL) и альтернативный текст. Метод `get_list` возвращает список URL изображений. Если `images` является строкой, он преобразует ее в список из одного элемента. Если `images` уже является списком, он возвращает его без изменений.

**Методы**:

- `__init__`:
  ```python
    def __init__(
        self,
        images: Union[str, list],
        alt: str,
    ):
        self.images = images
        self.alt = alt
  ```

  **Параметры**:
  - `images` (str | list): URL изображения или список URL изображений.
  - `alt` (str): Альтернативный текст для изображения.

- `get_list`:
  ```python
    def get_list(self) -> list[str]:
        return [self.images] if isinstance(self.images, str) else self.images
  ```

  **Назначение**: Возвращает список URL изображений. Если `images` является строкой, он преобразует ее в список из одного элемента. Если `images` уже является списком, он возвращает его без изменений.

**Примеры**:

```python
# Пример 1: Создание объекта ImageDataResponse с одним изображением
response = ImageDataResponse(images="https://example.com/image.png", alt="Пример изображения")
image_list = response.get_list()
assert image_list == ["https://example.com/image.png"]

# Пример 2: Создание объекта ImageDataResponse со списком изображений
response = ImageDataResponse(images=["https://example.com/image1.png", "https://example.com/image2.png"], alt="Примеры изображений")
image_list = response.get_list()
assert image_list == ["https://example.com/image1.png", "https://example.com/image2.png"]
```

### `ImageRequest`

```python
class ImageRequest():
    def __init__(
        self,
        options: dict = {}
    ):
        self.options = options

    def get(self, key: str):
        return self.options.get(key)
```

**Описание**: Класс для представления запроса, связанного с изображением.

**Принцип работы**:
Класс `ImageRequest` используется для хранения параметров запроса, связанных с изображением. Конструктор класса принимает словарь параметров запроса. Метод `get` позволяет получить значение параметра по ключу.

**Методы**:

- `__init__`:
  ```python
    def __init__(
        self,
        options: dict = {}
    ):
        self.options = options
  ```

  **Параметры**:
  - `options` (dict, optional): Словарь параметров запроса. По умолчанию `{}`.

- `get`:
  ```python
    def get(self, key: str):
        return self.options.get(key)
  ```

  **Параметры**:
  - `key` (str): Ключ параметра для получения.

  **Возвращает**:
  - Значение параметра по ключу.

**Примеры**:

```python
# Пример 1: Создание объекта ImageRequest с параметрами
request = ImageRequest(options={"width": 100, "height": 200})
width = request.get("width")
assert width == 100

height = request.get("height")
assert height == 200

# Пример 2: Создание объекта ImageRequest без параметров
request = ImageRequest()
value = request.get("some_key")
assert value is None