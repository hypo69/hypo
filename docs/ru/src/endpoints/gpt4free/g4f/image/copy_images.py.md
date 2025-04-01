# Модуль для копирования изображений

## Обзор

Модуль предназначен для скачивания и локального сохранения изображений, обеспечивая Unicode-безопасные имена файлов. Он предоставляет функции для обработки различных типов медиа, включая изображения, аудио и видео, а также обеспечивает совместимость с различными источниками, включая URL и data URI. Модуль является частью проекта `hypotez` и используется для обработки и хранения медиафайлов, сгенерированных или полученных из внешних источников.

## Подробней

Модуль содержит функции для:

- Извлечения расширений медиафайлов из URL или имени файла.
- Создания директории для хранения изображений, если она не существует.
- Извлечения исходного URL из параметра изображения.
- Проверки допустимости типа медиа.
- Сохранения медиафайлов из ответа на локальный диск.
- Создания имен файлов на основе тегов, альтернативного текста, расширения и хеша изображения.
- Копирования медиафайлов с использованием асинхронных операций.

## Функции

### `get_media_extension`

```python
def get_media_extension(media: str) -> str:
    """Extract media file extension from URL or filename"""
```

**Назначение**: Извлекает расширение медиафайла из URL или имени файла.

**Параметры**:
- `media` (str): URL или имя файла.

**Возвращает**:
- `str`: Расширение файла (например, ".jpg", ".mp3") или пустая строка, если расширение не найдено.

**Вызывает исключения**:
- `ValueError`: Если расширение медиафайла не поддерживается.

**Как работает функция**:

1. Анализирует URL, чтобы извлечь путь.
2. Извлекает расширение из пути URL или непосредственно из имени файла.
3. Проверяет, поддерживается ли расширение, сравнивая его с `EXTENSIONS_MAP`.
4. Возвращает расширение или вызывает исключение, если расширение не поддерживается.

**Примеры**:

```python
get_media_extension("https://example.com/image.jpg")  # возвращает ".jpg"
get_media_extension("audio.mp3")  # возвращает ".mp3"
```

### `ensure_images_dir`

```python
def ensure_images_dir():
    """Create images directory if it doesn't exist"""
```

**Назначение**: Создает директорию для хранения изображений, если она не существует.

**Как работает функция**:

1. Проверяет, существует ли директория `images_dir` (определена как "./generated_images").
2. Если директория не существует, создает её.

**Примеры**:

```python
ensure_images_dir()
```

### `get_source_url`

```python
def get_source_url(image: str, default: str = None) -> str:
    """Extract original URL from image parameter if present"""
```

**Назначение**: Извлекает исходный URL из параметра изображения, если он присутствует.

**Параметры**:
- `image` (str): Строка, содержащая URL изображения.
- `default` (str, optional): Значение по умолчанию, возвращаемое, если URL не найден. По умолчанию `None`.

**Возвращает**:
- `str`: Исходный URL или значение по умолчанию, если URL не найден.

**Как работает функция**:

1. Проверяет, содержит ли параметр `image` строку "url=".
2. Если содержит, декодирует URL из параметра `image`.
3. Проверяет, начинается ли декодированный URL с "http://" или "https://".
4. Возвращает декодированный URL или значение по умолчанию, если URL не найден.

**Примеры**:

```python
get_source_url("image.jpg?url=https://example.com/image.jpg")  # возвращает "https://example.com/image.jpg"
get_source_url("image.jpg", "default_image.jpg")  # возвращает "default_image.jpg"
```

### `is_valid_media_type`

```python
def is_valid_media_type(content_type: str) -> bool:
    """Check if the content type is a valid media type"""
```

**Назначение**: Проверяет, является ли указанный content type допустимым типом медиа.

**Параметры**:
- `content_type` (str): Content type для проверки.

**Возвращает**:
- `bool`: `True`, если content type является допустимым типом медиа, иначе `False`.

**Как работает функция**:

1. Проверяет, содержится ли `content_type` в `MEDIA_TYPE_MAP` или начинается ли с "audio/" или "video/".
2. Возвращает `True`, если условие выполнено, иначе `False`.

**Примеры**:

```python
is_valid_media_type("image/jpeg")  # возвращает True
is_valid_media_type("audio/mpeg")  # возвращает True
is_valid_media_type("text/html")  # возвращает False
```

### `save_response_media`

```python
async def save_response_media(response: StreamResponse, prompt: str, tags: list[str]) -> AsyncIterator:
    """Save media from response to local file and return URL"""
```

**Назначение**: Сохраняет медиафайл из ответа на локальный диск и возвращает URL.

**Параметры**:
- `response` (StreamResponse): Объект ответа, содержащий медиафайл.
- `prompt` (str): Описание изображения.
- `tags` (list[str]): Список тегов для формирования имени файла.

**Возвращает**:
- `AsyncIterator`: Асинхронный итератор, возвращающий объекты `ImageResponse`, `AudioResponse` или `VideoResponse` в зависимости от типа контента.

**Вызывает исключения**:
- `ValueError`: Если тип медиафайла не поддерживается.

**Как работает функция**:

1. Извлекает `content-type` из заголовков ответа.
2. Определяет расширение файла на основе `content-type`.
3. Генерирует имя файла с использованием тегов, альтернативного текста и расширения.
4. Сохраняет содержимое ответа в локальный файл.
5. Формирует URL для доступа к сохраненному файлу.
6. Возвращает объект `ImageResponse`, `AudioResponse` или `VideoResponse` в зависимости от типа контента.

**Внутренние функции**: Отсутствуют.

**Примеры**:

```python
# Пример использования с моковым объектом response
class MockResponse:
    def __init__(self, headers, content, method, url):
        self.headers = headers
        self.content = content
        self.method = method
        self.url = url
    async def iter_content(self):
        yield b"test data" # Моковые данные

    async def iter_any(self):
        yield b"test data"

async def test():
    response = MockResponse({"content-type": "image/jpeg"}, b"test data", "GET", "https://example.com/image.jpg")
    tags = ["tag1", "tag2"]
    async for item in save_response_media(response, "prompt", tags):
        print(item)
asyncio.run(test())
```

### `get_filename`

```python
def get_filename(tags: list[str], alt: str, extension: str, image: str) -> str:
    """Generates a filename for media files"""
```

**Назначение**: Генерирует имя файла для медиафайлов на основе тегов, альтернативного текста, расширения и хеша изображения.

**Параметры**:
- `tags` (list[str]): Список тегов для включения в имя файла.
- `alt` (str): Альтернативный текст для включения в имя файла.
- `extension` (str): Расширение файла.
- `image` (str): Исходное изображение (используется для генерации хеша).

**Возвращает**:
- `str`: Сгенерированное имя файла.

**Как работает функция**:

1. Формирует имя файла, используя текущее время, теги, альтернативный текст и хеш изображения.
2. Использует функцию `secure_filename` для обеспечения безопасности имени файла.

**Примеры**:

```python
tags = ["tag1", "tag2"]
alt = "alternative_text"
extension = ".jpg"
image = "https://example.com/image.jpg"
filename = get_filename(tags, alt, extension, image)
print(filename)
```

### `copy_media`

```python
async def copy_media(
    images: list[str],
    cookies: Optional[Cookies] = None,
    headers: Optional[dict] = None,
    proxy: Optional[str] = None,
    alt: str = None,
    tags: list[str] = None,
    add_url: bool = True,
    target: str = None,
    ssl: bool = None
) -> list[str]:
    """
    Download and store images locally with Unicode-safe filenames
    Returns list of relative image URLs
    """
```

**Назначение**: Загружает и сохраняет изображения локально, обеспечивая Unicode-безопасные имена файлов.

**Параметры**:
- `images` (list[str]): Список URL изображений для загрузки.
- `cookies` (Optional[Cookies], optional): Куки для использования при загрузке изображений. По умолчанию `None`.
- `headers` (Optional[dict], optional): Заголовки для использования при загрузке изображений. По умолчанию `None`.
- `proxy` (Optional[str], optional): Прокси-сервер для использования при загрузке изображений. По умолчанию `None`.
- `alt` (str, optional): Альтернативный текст для использования при формировании имени файла. По умолчанию `None`.
- `tags` (list[str], optional): Список тегов для использования при формировании имени файла. По умолчанию `None`.
- `add_url` (bool, optional): Определяет, следует ли добавлять URL в имя файла. По умолчанию `True`.
- `target` (str, optional): Целевой путь для сохранения изображения. По умолчанию `None`.
- `ssl` (bool, optional): Определяет, следует ли использовать SSL. По умолчанию `None`.

**Возвращает**:
- `list[str]`: Список относительных URL изображений.

**Как работает функция**:

1. Инициализирует сессию `ClientSession` с заданными параметрами (proxy, cookies, headers).
2. Определяет, следует ли добавлять URL к имени файла.
3. Создает директорию для хранения изображений, если она не существует.
4. Для каждого изображения в списке:
   - Проверяет, является ли изображение локальным. Если да, пропускает его.
   - Генерирует имя файла с использованием тегов, альтернативного текста и расширения.
   - Сохраняет изображение локально, обрабатывая data URI и URL.
   - Проверяет формат файла и переименовывает его, если необходимо.
   - Формирует URL для доступа к сохраненному файлу.
5. Возвращает список относительных URL изображений.

**Внутренние функции**:

#### `copy_image`

```python
async def copy_image(image: str, target: str = None) -> str:
    """Process individual image and return its local URL"""
```

**Назначение**: Обрабатывает отдельное изображение и возвращает его локальный URL.

**Параметры**:
- `image` (str): URL изображения для обработки.
- `target` (str, optional): Целевой путь для сохранения изображения. По умолчанию `None`.

**Возвращает**:
- `str`: Локальный URL изображения.

**Как работает функция**:

1. Проверяет, является ли изображение локальным. Если да, возвращает его.
2. Генерирует имя файла с использованием тегов, альтернативного текста и расширения.
3. Сохраняет изображение локально, обрабатывая data URI и URL.
4. Проверяет формат файла и переименовывает его, если необходимо.
5. Формирует URL для доступа к сохраненному файлу.
6. Обрабатывает ошибки при копировании изображения и возвращает исходный URL в случае ошибки.

**Примеры**:

```python
import asyncio
async def test():
    images = ["https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"]
    result = await copy_media(images)
    print(result)
asyncio.run(test())