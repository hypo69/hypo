# Модуль для работы с изображениями

## Обзор

Модуль `image.py` предоставляет набор функций для обработки изображений, включая конвертацию в различные форматы, изменение размеров, проверку формата и извлечение данных из URI. Он также включает классы для обработки запросов и ответов, связанных с изображениями.

## Подробней

Модуль предназначен для работы с изображениями в различных форматах и представлениях, обеспечивая их преобразование, проверку и подготовку для дальнейшей обработки или передачи. Он используется для обработки изображений, полученных из разных источников, таких как файлы, байтовые строки или URI данных. Модуль также предоставляет классы для структурирования запросов и ответов, связанных с изображениями.

## Классы

### `ImageDataResponse`

**Описание**: Класс для представления ответа, содержащего изображения и альтернативный текст.

**Принцип работы**:
Класс `ImageDataResponse` используется для хранения информации об изображении (или списке изображений) и альтернативном тексте, связанном с этими изображениями. Он предоставляет метод для получения списка изображений, независимо от того, было ли передано одно изображение или список.

**Атрибуты**:
- `images` (Union[str, list]): Изображение или список изображений.
- `alt` (str): Альтернативный текст для изображения.

**Методы**:
- `get_list()`: Возвращает список изображений. Если `self.images` является строкой, то возвращается список, содержащий эту строку. Если `self.images` является списком, то возвращается сам список.

### `ImageRequest`

**Описание**: Класс для представления запроса изображения с опциями.

**Принцип работы**:
Класс `ImageRequest` используется для хранения опций, связанных с запросом изображения. Он предоставляет метод для получения значения опции по ключу.

**Атрибуты**:
- `options` (dict): Словарь с опциями запроса.

**Методы**:
- `get(key: str)`: Возвращает значение опции по ключу. Если ключ не найден, возвращает `None`.

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
- `image` (ImageType): Входное изображение (строка, байты или объект `Image`).
- `is_svg` (bool, optional): Флаг, указывающий, является ли изображение SVG. По умолчанию `False`.

**Возвращает**:
- `Image`: Преобразованный объект `PIL Image`.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлены необходимые библиотеки (`pillow` или `cairosvg`).
- `ValueError`: Если data URI является невалидным или формат изображения не поддерживается.

**Как работает функция**:

1. **Проверка зависимостей**: Функция проверяет, установлена ли библиотека `pillow`, необходимая для работы с изображениями. Если она не установлена, вызывается исключение `MissingRequirementsError`.
2. **Обработка Data URI**: Если входное изображение является строкой и начинается с "data:", функция проверяет, является ли URI корректным изображением, и извлекает данные изображения из URI.
3. **Обработка SVG**: Если `is_svg` установлен в `True`, функция пытается импортировать библиотеку `cairosvg` и, если она не установлена, вызывает исключение `MissingRequirementsError`. Затем происходит преобразование SVG-изображения в PNG с использованием `cairosvg`.
4. **Обработка байтов**: Если входное изображение является байтами, функция проверяет, является ли формат изображения поддерживаемым, и открывает изображение с использованием `PIL.Image.open`.
5. **Обработка PIL Image**: Если входное изображение уже является объектом `PIL Image`, функция просто возвращает его.

**ASCII flowchart**:

```
A [Проверка наличия pillow]
|
B [Является ли изображение строкой и начинается ли с "data:"]
|
C [Проверка is_svg]
|
D [Является ли изображение байтами]
|
E [Является ли изображение PIL Image]
|
F [Возврат PIL Image]
```

**Примеры**:

```python
from PIL.Image import Image
from io import BytesIO
image_path = 'path/to/image.jpg'
image_bytes = b'...' # bytes of image
image_data_uri = 'data:image/png;base64,...'

# Преобразование из пути к файлу
image_from_path = to_image(image_path)

# Преобразование из байтов
image_from_bytes = to_image(image_bytes)

# Преобразование из data URI
image_from_data_uri = to_image(image_data_uri)
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

Функция проверяет, содержит ли имя файла точку (`.`) и входит ли расширение файла (в нижнем регистре) в список допустимых расширений (`ALLOWED_EXTENSIONS`).

**ASCII flowchart**:

```
A [Проверка наличия точки в имени файла]
|
B [Извлечение расширения файла]
|
C [Проверка расширения на соответствие списку ALLOWED_EXTENSIONS]
|
D [Возврат результата]
```

**Примеры**:

```python
# Допустимое расширение
is_allowed_extension('image.png')  # Вернет True

# Недопустимое расширение
is_allowed_extension('image.txt')  # Вернет False

# Имя файла без расширения
is_allowed_extension('image')      # Вернет False
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

**Назначение**: Проверяет, представляет ли заданный data URI изображение.

**Параметры**:
- `data_uri` (str): Data URI для проверки.

**Вызывает исключения**:
- `ValueError`: Если data URI невалиден или формат изображения не поддерживается.

**Как работает функция**:

Функция проверяет, начинается ли data URI с 'data:image' и содержит ли он формат изображения (например, jpeg, png, gif). Затем извлекается формат изображения из data URI и проверяется, входит ли он в список допустимых форматов.

**ASCII flowchart**:

```
A [Проверка начала data URI с 'data:image']
|
B [Извлечение формата изображения из data URI]
|
C [Проверка формата изображения на соответствие списку ALLOWED_EXTENSIONS]
|
D [Вызов исключения ValueError при невалидном URI или формате]
```

**Примеры**:

```python
# Валидный data URI
valid_data_uri = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+rAI0EyQNgFBAEcAwUAwt0KjUIAAAAASUVORK5CYII='
is_data_uri_an_image(valid_data_uri)  # Не вызовет исключение

# Невалидный data URI (не начинается с 'data:image')
invalid_data_uri = 'text/plain;base64,SGVsbG8sIHdvcmxkIQ=='
#is_data_uri_an_image(invalid_data_uri)  # Вызовет ValueError

# Неподдерживаемый формат изображения
invalid_format_uri = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMCwxMCBMOTAsOTAiLz48L3N2Zz4='
#is_data_uri_an_image(invalid_format_uri) # Вызовет ValueError
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

**Назначение**: Проверяет, представляет ли заданный набор двоичных данных изображение с допустимым форматом.

**Параметры**:
- `binary_data` (bytes): Двоичные данные для проверки.

**Возвращает**:
- `str`: Строка, представляющая MIME-тип изображения (например, `"image/jpeg"`).

**Вызывает исключения**:
- `ValueError`: Если формат изображения не поддерживается.

**Как работает функция**:

Функция проверяет двоичные данные на соответствие известным сигнатурам (magic numbers) различных форматов изображений (JPEG, PNG, GIF, WEBP). Если соответствие найдено, функция возвращает соответствующий MIME-тип.

**ASCII flowchart**:

```
A [Проверка сигнатуры JPEG]
|
B [Проверка сигнатуры PNG]
|
C [Проверка сигнатуры GIF]
|
D [Проверка сигнатуры JPEG (альтернативная)]
|
E [Проверка сигнатуры WEBP]
|
F [Вызов исключения ValueError при неподдерживаемом формате]
|
G [Возврат MIME-типа]
```

**Примеры**:

```python
# JPEG image
jpeg_data = b'\\xFF\\xD8\\xFF\\xE0\\x00\\x10JFIF\\x00\\x01...'
is_accepted_format(jpeg_data)  # Вернет "image/jpeg"

# PNG image
png_data = b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR...'
is_accepted_format(png_data)   # Вернет "image/png"

# Неподдерживаемый формат
unknown_data = b'\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x09...'
#is_accepted_format(unknown_data) # Вызовет ValueError
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

**Назначение**: Извлекает двоичные данные из заданного data URI.

**Параметры**:
- `data_uri` (str): Data URI.

**Возвращает**:
- `bytes`: Извлеченные двоичные данные.

**Как работает функция**:

Функция разделяет data URI по запятой, извлекает последнюю часть (содержащую base64-encoded data), декодирует ее из base64 и возвращает полученные двоичные данные.

**ASCII flowchart**:

```
A [Разделение data URI по запятой]
|
B [Извлечение base64-encoded data]
|
C [Декодирование из base64]
|
D [Возврат двоичных данных]
```

**Примеры**:

```python
data_uri = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+rAI0EyQNgFBAEcAwUAwt0KjUIAAAAASUVORK5CYII='
binary_data = extract_data_uri(data_uri)
print(type(binary_data)) # bytes
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
- `image` (Image): Изображение.

**Возвращает**:
- `int`: Значение ориентации.

**Как работает функция**:

Функция пытается получить EXIF-данные из изображения. Если EXIF-данные существуют, функция извлекает значение тега ориентации (274) и возвращает его.

**ASCII flowchart**:

```
A [Попытка получить EXIF-данные]
|
B [Проверка наличия EXIF-данных]
|
C [Извлечение значения тега ориентации (274)]
|
D [Возврат значения ориентации]
```

**Примеры**:

```python
from PIL import Image
image = Image.open('path/to/image_with_exif.jpg')
orientation = get_orientation(image)
print(orientation) # 6, 1, or None
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

1. **Коррекция ориентации**: Функция получает ориентацию изображения с помощью `get_orientation` и, если ориентация определена, выполняет транспонирование изображения для коррекции ориентации.
2. **Изменение размера**: Функция изменяет размер изображения с использованием метода `thumbnail`.
3. **Удаление прозрачности**: Если изображение имеет режим "RGBA", функция удаляет прозрачность, создавая новое белое изображение и вставляя в него исходное изображение с использованием маски.
4. **Преобразование в RGB**: Если изображение имеет режим, отличный от "RGB", функция преобразует его в режим "RGB".

**ASCII flowchart**:

```
A [Получение ориентации изображения]
|
B [Коррекция ориентации (транспонирование)]
|
C [Изменение размера (thumbnail)]
|
D [Удаление прозрачности (если режим RGBA)]
|
E [Преобразование в RGB (если режим не RGB)]
|
F [Возврат обработанного изображения]
```

**Примеры**:

```python
from PIL import Image
image = Image.open('path/to/image.jpg')
new_image = process_image(image, 200, 200)
new_image.save('path/to/processed_image.jpg')
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
- `image` (ImageType): Изображение для преобразования.

**Возвращает**:
- `bytes`: Изображение в виде байтов.

**Как работает функция**:

Функция проверяет тип входного изображения и преобразует его в байты в зависимости от типа:
- Если изображение уже является байтами, оно возвращается без изменений.
- Если изображение является строкой и начинается с "data:", вызывается `is_data_uri_an_image` для проверки формата и `extract_data_uri` для извлечения байтов.
- Если изображение является объектом `PIL Image`, оно сохраняется во временный буфер `BytesIO`, и его содержимое возвращается.
- Если изображение является строкой или объектом `Path`, представляющим путь к файлу, файл считывается и его содержимое возвращается.
- В противном случае, функция пытается считать содержимое изображения, предполагая, что это файлоподобный объект.

**ASCII flowchart**:

```
A [Проверка: является ли изображение байтами?]
|
B [Проверка: является ли изображение строкой, начинающейся с "data:"?]
|
C [Извлечение данных из URI]
|
D [Проверка: является ли изображение объектом PIL Image?]
|
E [Преобразование изображения в байты через BytesIO]
|
F [Проверка: является ли изображение строкой или Path (путь к файлу)?]
|
G [Чтение байтов из файла по указанному пути]
|
H [Чтение байтов из файлоподобного объекта]
|
I [Возврат изображения в виде байтов]
```

**Примеры**:

```python
from PIL import Image
from io import BytesIO
from pathlib import Path

# Преобразование изображения из PIL Image в байты
image = Image.new('RGB', (60, 30), color='red')
image_bytes = to_bytes(image)

# Преобразование изображения из пути к файлу в байты
image_path = Path('path/to/image.png')
image_bytes = to_bytes(image_path)

# Преобразование изображения из байтовой строки
image_bytes = b'...'  # Замените на реальные байты изображения
image_bytes_result = to_bytes(image_bytes)

# Преобразование изображения из файлоподобного объекта
with open('path/to/image.png', 'rb') as f:
    image_bytes_from_file = to_bytes(f)
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

**Назначение**: Преобразует заданное изображение в data URI.

**Параметры**:
- `image` (ImageType): Изображение для преобразования.

**Возвращает**:
- `str`: Изображение в формате data URI.

**Как работает функция**:

Функция проверяет, является ли входное изображение строкой. Если нет, она преобразует изображение в байты с помощью `to_bytes`, кодирует байты в base64 и возвращает data URI. Если изображение уже является строкой, функция возвращает его без изменений.

**ASCII flowchart**:

```
A [Проверка: является ли изображение строкой?]
|
B [Преобразование изображения в байты (to_bytes)]
|
C [Кодирование байтов в base64]
|
D [Формирование data URI]
|
E [Возврат data URI]
```

**Примеры**:

```python
from PIL import Image

# Преобразование изображения из PIL Image в data URI
image = Image.new('RGB', (60, 30), color='red')
data_uri = to_data_uri(image)
print(data_uri)  # Выведет data URI

# Преобразование изображения из пути к файлу в data URI
image_path = 'path/to/image.png'
data_uri = to_data_uri(image_path)
print(data_uri)  # Выведет data URI

# Преобразование изображения из байтовой строки
image_bytes = b'...'  # Замените на реальные байты изображения
data_uri = to_data_uri(image_bytes)
print(data_uri)  # Выведет data URI