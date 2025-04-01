# Модуль для работы с изображениями

## Обзор

Модуль `image.py` предоставляет набор функций и классов для обработки изображений, включая преобразование форматов, изменение размеров, проверку форматов и извлечение данных из URI. Он также включает классы для обработки запросов и ответов, связанных с изображениями.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для обработки изображений, полученных или генерируемых в рамках проекта. Он обеспечивает функциональность для работы с различными форматами изображений и преобразования их в нужный вид.

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

**Назначение**: Преобразует входное изображение в объект `PIL Image`.

**Параметры**:
- `image` (ImageType): Входное изображение, которое может быть строкой (путь к файлу), байтами или объектом `PIL Image`.
- `is_svg` (bool, optional): Указывает, является ли изображение SVG. По умолчанию `False`.

**Возвращает**:
- `Image`: Преобразованный объект `PIL Image`.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлены необходимые библиотеки (`pillow` или `cairosvg`).
- `ValueError`: Если `data URI` является невалидным или формат изображения не поддерживается.

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `pillow`. Если нет, вызывает исключение `MissingRequirementsError`.
2.  Если входное изображение является строкой и начинается с `data:`, проверяет, является ли это `data URI` изображением, и извлекает данные из `URI`.
3.  Если изображение является `SVG`, проверяет, установлена ли библиотека `cairosvg`, и конвертирует `SVG` в `PNG` с использованием `cairosvg`.
4.  Если изображение представлено в виде байтов, проверяет, является ли формат изображения поддерживаемым.
5.  Если изображение не является экземпляром `PIL Image`, пытается открыть его с помощью `open_image` и загрузить.

**Примеры**:

```python
from PIL.Image import Image
from pathlib import Path

# Преобразование изображения из файла
image_path = "example.png" #Укажите путь к вашему изображению
image = to_image(image_path)
assert isinstance(image, Image)

# Преобразование изображения из байтов
with open(image_path, "rb") as f:
    image_bytes = f.read()
image = to_image(image_bytes)
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

**Назначение**: Проверяет, имеет ли указанное имя файла допустимое расширение.

**Параметры**:
- `filename` (str): Имя файла для проверки.

**Возвращает**:
- `bool`: `True`, если расширение допустимо, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, содержит ли имя файла точку (`.`).
2.  Извлекает расширение файла (часть после последней точки) и приводит его к нижнему регистру.
3.  Проверяет, входит ли расширение в список допустимых расширений (`ALLOWED_EXTENSIONS`).

**Примеры**:

```python
# Проверка допустимого расширения
filename = "example.png"
is_allowed = is_allowed_extension(filename)
assert is_allowed == True

# Проверка недопустимого расширения
filename = "example.txt"
is_allowed = is_allowed_extension(filename)
assert is_allowed == False
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

**Назначение**: Проверяет, представляет ли указанный `data URI` изображение.

**Параметры**:
- `data_uri` (str): `Data URI` для проверки.

**Вызывает исключения**:
- `ValueError`: Если `data URI` является невалидным или формат изображения не поддерживается.

**Как работает функция**:

1.  Проверяет, начинается ли `data URI` с `data:image/` и содержит ли формат изображения (например, `jpeg`, `png`, `gif`).
2.  Извлекает формат изображения из `data URI` и приводит его к нижнему регистру.
3.  Проверяет, входит ли формат изображения в список допустимых расширений (`ALLOWED_EXTENSIONS`), а также допускает `svg+xml`.

**Примеры**:

```python
# Проверка валидного data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+r8vMzAIp4MxYEAAGkCKqKWq9sAAAAASUVORK5CYII="
try:
    is_data_uri_an_image(data_uri)
except ValueError as ex:
    assert False, f"Проверка не должна была вызвать исключение: {ex}"

# Проверка невалидного data URI
data_uri = "data:text/plain;base64,SGVsbG8sIFdvcmxkIQ=="
try:
    is_data_uri_an_image(data_uri)
    assert False, "Проверка должна была вызвать исключение"
except ValueError:
    pass
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

**Назначение**: Проверяет, представляет ли указанные двоичные данные изображение с допустимым форматом.

**Параметры**:
- `binary_data` (bytes): Двоичные данные для проверки.

**Возвращает**:
- `str`: Строка, представляющая тип изображения (`image/jpeg`, `image/png`, `image/gif`, `image/webp`), если формат допустим.

**Вызывает исключения**:
- `ValueError`: Если формат изображения не поддерживается.

**Как работает функция**:

1.  Проверяет двоичные данные на наличие определенных сигнатур, соответствующих различным форматам изображений (`JPEG`, `PNG`, `GIF`, `WEBP`).
2.  Если обнаружена соответствующая сигнатура, возвращает строку, указывающую формат изображения.
3.  Если ни одна из сигнатур не обнаружена, вызывает исключение `ValueError`.

**Примеры**:

```python
# Проверка JPEG изображения
jpeg_data = b'\xFF\xD8\xFF'
image_format = is_accepted_format(jpeg_data)
assert image_format == "image/jpeg"

# Проверка PNG изображения
png_data = b'\x89PNG\r\n\x1a\n'
image_format = is_accepted_format(png_data)
assert image_format == "image/png"

# Проверка неподдерживаемого формата
unknown_data = b'Some random bytes'
try:
    is_accepted_format(unknown_data)
    assert False, "Проверка должна была вызвать исключение"
except ValueError:
    pass
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

**Назначение**: Извлекает двоичные данные из указанного `data URI`.

**Параметры**:
- `data_uri` (str): `Data URI` для извлечения данных.

**Возвращает**:
- `bytes`: Извлеченные двоичные данные.

**Как работает функция**:

1.  Разделяет `data URI` по запятой (`,`) и берет последнюю часть, которая содержит закодированные данные в формате `Base64`.
2.  Декодирует данные из `Base64` в двоичный формат.

**Примеры**:

```python
# Извлечение данных из data URI
data_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+r8vMzAIp4MxYEAAGkCKqKWq9sAAAAASUVORK5CYII="
binary_data = extract_data_uri(data_uri)
assert isinstance(binary_data, bytes)
assert len(binary_data) > 0
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

**Назначение**: Получает ориентацию указанного изображения из `EXIF`-данных.

**Параметры**:
- `image` (Image): Изображение для получения ориентации.

**Возвращает**:
- `int | None`: Значение ориентации, если оно присутствует в `EXIF`-данных, иначе `None`.

**Как работает функция**:

1.  Пытается получить `EXIF`-данные из изображения, используя `image.getexif()` или `image._getexif()`, в зависимости от наличия атрибута `getexif`.
2.  Если `EXIF`-данные существуют, пытается получить значение тега ориентации (274).
3.  Если значение ориентации найдено, возвращает его.

**Примеры**:

```python
from PIL import Image

# Пример с изображением, у которого есть EXIF-данные
image_path = "example.jpg"  # Укажите путь к вашему изображению с EXIF-данными
try:
    image = Image.open(image_path)
    orientation = get_orientation(image)
    if orientation:
        print(f"Orientation: {orientation}")
    else:
        print("No orientation information found.")
except FileNotFoundError:
    print(f"File not found: {image_path}")

# Пример с изображением, у которого нет EXIF-данных
image = Image.new('RGB', (100, 100))
orientation = get_orientation(image)
assert orientation is None
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

**Назначение**: Обрабатывает указанное изображение, корректируя его ориентацию и изменяя его размер.

**Параметры**:
- `image` (Image): Изображение для обработки.
- `new_width` (int): Новая ширина изображения.
- `new_height` (int): Новая высота изображения.

**Возвращает**:
- `Image`: Обработанное изображение.

**Как работает функция**:

1.  Исправляет ориентацию изображения на основе `EXIF`-данных, используя функцию `get_orientation`.
2.  Изменяет размер изображения с помощью `image.thumbnail((new_width, new_height))`.
3.  Удаляет прозрачность, если изображение в формате `RGBA`, путем создания нового изображения `RGB` с белым фоном и вставки исходного изображения на него.
4.  Преобразует изображение в формат `RGB`, если оно не в этом формате.

**Примеры**:

```python
from PIL import Image

# Пример обработки изображения
image_path = "example.png"  # Укажите путь к вашему изображению
try:
    image = Image.open(image_path)
    new_width = 200
    new_height = 150
    processed_image = process_image(image, new_width, new_height)
    processed_image.save("processed_example.png")
    print("Image processed and saved as processed_example.png")
except FileNotFoundError:
    print(f"File not found: {image_path}")
except Exception as ex:
    print(f"Error processing image: {ex}")
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

**Назначение**: Преобразует указанное изображение в байты.

**Параметры**:
- `image` (ImageType): Изображение для преобразования.

**Возвращает**:
- `bytes`: Изображение в виде байтов.

**Как работает функция**:

1.  Проверяет тип входного изображения и выполняет соответствующее преобразование:
    -   Если изображение уже является байтами, возвращает его без изменений.
    -   Если изображение является строкой, начинающейся с `data:`, проверяет и извлекает данные из `data URI`.
    -   Если изображение является экземпляром `PIL Image`, сохраняет его в `BytesIO` и возвращает полученные байты.
    -   Если изображение является строкой или `Path`, читает файл и возвращает его содержимое в виде байтов.
    -   Если ни один из вышеперечисленных случаев не подходит, пытается прочитать изображение, предполагая, что это файловый объект.

**Примеры**:

```python
from PIL import Image
from pathlib import Path

# Пример преобразования изображения из файла в байты
image_path = "example.png"  # Укажите путь к вашему изображению
try:
    image_bytes = to_bytes(image_path)
    assert isinstance(image_bytes, bytes)
    assert len(image_bytes) > 0
    print("Image converted to bytes successfully.")
except FileNotFoundError:
    print(f"File not found: {image_path}")
except Exception as ex:
    print(f"Error converting image to bytes: {ex}")

# Пример преобразования изображения из PIL Image в байты
image = Image.new('RGB', (100, 100))
image_bytes = to_bytes(image)
assert isinstance(image_bytes, bytes)
assert len(image_bytes) > 0
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

**Назначение**: Преобразует указанное изображение в `data URI`.

**Параметры**:
- `image` (ImageType): Изображение для преобразования.

**Возвращает**:
- `str`: Изображение в формате `data URI`.

**Как работает функция**:

1.  Проверяет, является ли входное изображение строкой. Если да, возвращает его без изменений (предполагая, что это уже `data URI`).
2.  Если изображение не является строкой, преобразует его в байты с помощью функции `to_bytes`.
3.  Кодирует полученные байты в `Base64`.
4.  Определяет формат изображения с помощью функции `is_accepted_format`.
5.  Формирует `data URI` с использованием формата изображения и закодированных данных.

**Примеры**:

```python
from PIL import Image

# Пример преобразования изображения из PIL Image в data URI
image = Image.new('RGB', (100, 100))
data_uri = to_data_uri(image)
assert isinstance(data_uri, str)
assert data_uri.startswith("data:image")
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

**Описание**: Класс для представления ответа с данными изображения.

**Принцип работы**:

Класс `ImageDataResponse` предназначен для хранения и обработки информации об изображениях, возвращаемых в качестве ответа. Он принимает список изображений (или одно изображение в виде строки) и альтернативный текст (`alt`) для этих изображений.

**Методы**:

- `__init__(self, images: Union[str, list], alt: str)`:
    -   **Назначение**: Конструктор класса. Инициализирует объект `ImageDataResponse` с переданными изображениями и альтернативным текстом.
    -   **Параметры**:
        -   `images` (Union[str, list]): Список изображений или одно изображение в виде строки.
        -   `alt` (str): Альтернативный текст для изображений.
- `get_list(self) -> list[str]`:
    -   **Назначение**: Возвращает список изображений. Если `images` является строкой, преобразует ее в список из одного элемента.
    -   **Возвращает**:
        -   `list[str]`: Список изображений.

**Примеры**:

```python
# Пример создания экземпляра класса и получения списка изображений
image_data = ImageDataResponse(images=["image1.png", "image2.jpg"], alt="Примеры изображений")
image_list = image_data.get_list()
assert isinstance(image_list, list)
assert len(image_list) == 2

image_data = ImageDataResponse(images="image1.png", alt="Пример изображения")
image_list = image_data.get_list()
assert isinstance(image_list, list)
assert len(image_list) == 1
assert image_list[0] == "image1.png"
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

**Описание**: Класс для представления запроса изображения.

**Принцип работы**:

Класс `ImageRequest` предназначен для хранения и обработки опций запроса, связанных с изображениями. Он принимает словарь опций и предоставляет метод для получения значения опции по ключу.

**Методы**:

- `__init__(self, options: dict = {})`:
    -   **Назначение**: Конструктор класса. Инициализирует объект `ImageRequest` с переданными опциями.
    -   **Параметры**:
        -   `options` (dict, optional): Словарь опций запроса. По умолчанию `{}`.
- `get(self, key: str)`:
    -   **Назначение**: Возвращает значение опции по указанному ключу.
    -   **Параметры**:
        -   `key` (str): Ключ опции для получения.
    -   **Возвращает**:
        -   Значение опции или `None`, если опция с указанным ключом не найдена.

**Примеры**:

```python
# Пример создания экземпляра класса и получения значения опции
request_options = {"width": 200, "height": 150}
image_request = ImageRequest(options=request_options)
width = image_request.get("width")
assert width == 200

height = image_request.get("height")
assert height == 150

nonexistent_option = image_request.get("quality")
assert nonexistent_option is None