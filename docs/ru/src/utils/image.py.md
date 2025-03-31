# Модуль `src.utils.image`

## Обзор

Модуль предоставляет асинхронные функции для загрузки, сохранения и обработки изображений.
Он включает в себя функциональность, такую как сохранение изображений из URL-адресов, сохранение данных изображений в файлы,
получение данных изображений, поиск случайных изображений в каталогах, добавление водяных знаков, изменение размера
и преобразование форматов изображений.

## Подробнее

Этот модуль предоставляет набор утилит для работы с изображениями, включая асинхронную загрузку и сохранение,
а также различные операции обработки изображений, такие как добавление водяных знаков, изменение размера и преобразование форматов.
Он использует библиотеки `aiohttp`, `aiofiles` и `PIL` (Pillow) для выполнения этих задач.
Модуль предназначен для упрощения работы с изображениями в асинхронных приложениях.

## Содержание

- [Классы](#Классы)
    - [ImageError](#ImageError)
- [Функции](#Функции)
    - [save_image_from_url_async](#save_image_from_url_async)
    - [save_image](#save_image)
    - [save_image_async](#save_image_async)
    - [get_image_bytes](#get_image_bytes)
    - [get_raw_image_data](#get_raw_image_data)
    - [random_image](#random_image)
    - [add_text_watermark](#add_text_watermark)
    - [add_image_watermark](#add_image_watermark)
    - [resize_image](#resize_image)
    - [convert_image](#convert_image)
    - [process_images_with_watermark](#process_images_with_watermark)

## Классы

### `ImageError`

**Описание**: Пользовательское исключение для ошибок, связанных с изображениями.

**Как работает класс**:
Этот класс используется для создания пользовательских исключений, специфичных для операций с изображениями.
Он наследуется от базового класса `Exception` и может быть использован для обработки ошибок, возникающих в функциях,
связанных с обработкой изображений.

## Функции

### `save_image_from_url_async`

```python
async def save_image_from_url_async(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Downloads an image from a URL and saves it locally asynchronously.

    Args:
        image_url (str): The URL to download the image from.
        filename (Union[str, Path]): The name of the file to save the image to.

    Returns:
        Optional[str]: The path to the saved file, or None if the operation failed.

    Raises:
        ImageError: If the image download or save operation fails.
    """
```

**Назначение**: Асинхронно загружает изображение из URL-адреса и сохраняет его локально.

**Как работает функция**:
Функция принимает URL-адрес изображения и имя файла для сохранения.
Она использует `aiohttp` для асинхронной загрузки изображения и `save_image_async` для сохранения данных изображения в файл.
В случае возникновения ошибок при загрузке или сохранении изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_url` (str): URL-адрес изображения для загрузки.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если загрузка или сохранение изображения не удалось.

**Примеры**:

```python
image_url = 'https://example.com/image.png'
filename = 'path/to/save/image.png'
await save_image_from_url_async(image_url, filename)
```

### `save_image`

```python
def save_image(image_data: bytes, file_name: str | Path, format: str = 'PNG') -> Optional[str]:
    """
    Saves image data to a file in the specified format.

    Args:
        image_data (bytes): The binary image data.
        file_name (Union[str, Path]): The name of the file to save the image to.
        format (str): The format to save the image in, default is PNG.

    Returns:
        Optional[str]: The path to the saved file, or None if the operation failed.

    Raises:
        ImageError: If the file cannot be created, saved, or if the saved file is empty.
    """
```

**Назначение**: Сохраняет данные изображения в файл в указанном формате.

**Как работает функция**:
Функция принимает двоичные данные изображения, имя файла и формат изображения (по умолчанию PNG).
Она использует библиотеку `PIL` (Pillow) для обработки изображения и сохранения его в указанном формате.
Функция также проверяет, был ли создан файл и не является ли он пустым.
В случае возникновения ошибок при создании или сохранении файла, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат для сохранения изображения, по умолчанию PNG.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Примеры**:

```python
image_data = b'...'  # Двоичные данные изображения
file_name = 'path/to/save/image.png'
save_image(image_data, file_name)
```

### `save_image_async`

```python
async def save_image_async(image_data: bytes, file_name: str | Path, format: str = 'PNG') -> Optional[str]:
    """
    Saves image data to a file in the specified format asynchronously.

    Args:
        image_data (bytes): The binary image data.
        file_name (Union[str, Path]): The name of the file to save the image to.
        format (str): The format to save the image in, default is PNG.

    Returns:
        Optional[str]: The path to the saved file, or None if the operation failed.

    Raises:
        ImageError: If the file cannot be created, saved, or if the saved file is empty.
    """
```

**Назначение**: Асинхронно сохраняет данные изображения в файл в указанном формате.

**Как работает функция**:
Функция принимает двоичные данные изображения, имя файла и формат изображения (по умолчанию PNG).
Она использует библиотеку `PIL` (Pillow) для обработки изображения и сохранения его в указанном формате.
Асинхронно создает директорию, если она не существует.
Функция также проверяет, был ли создан файл и не является ли он пустым.
В случае возникновения ошибок при создании или сохранении файла, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат для сохранения изображения, по умолчанию PNG.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Примеры**:

```python
image_data = b'...'  # Двоичные данные изображения
file_name = 'path/to/save/image.png'
await save_image_async(image_data, file_name)
```

### `get_image_bytes`

```python
def get_image_bytes(image_path: Path, raw: bool = True) -> Optional[BytesIO | bytes]:
    """
    Reads an image using Pillow and returns its bytes in JPEG format.

    Args:
        image_path (Path): The path to the image file.
        raw (bool): If True, returns a BytesIO object; otherwise, returns bytes. Defaults to True.

    Returns:
        Optional[Union[BytesIO, bytes]]: The bytes of the image in JPEG format, or None if an error occurs.
    """
```

**Назначение**: Читает изображение с использованием Pillow и возвращает его байты в формате JPEG.

**Как работает функция**:
Функция принимает путь к файлу изображения и флаг `raw`, который определяет, возвращать ли объект `BytesIO` или байты.
Она использует библиотеку `PIL` (Pillow) для открытия изображения и сохранения его в формате JPEG.
В случае возникновения ошибок при чтении изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Path): Путь к файлу изображения.
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; в противном случае возвращает байты. По умолчанию `True`.

**Возвращает**:
- `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG или `None`, если произошла ошибка.

**Примеры**:

```python
image_path = Path('path/to/image.png')
image_bytes = get_image_bytes(image_path)
```

### `get_raw_image_data`

```python
def get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Retrieves the raw binary data of a file if it exists.

    Args:
        file_name (Union[str, Path]): The name or path of the file to read.

    Returns:
        Optional[bytes]: The binary data of the file, or None if the file does not exist or an error occurs.
    """
```

**Назначение**: Извлекает необработанные двоичные данные файла, если он существует.

**Как работает функция**:
Функция принимает имя файла или путь к файлу.
Она проверяет, существует ли файл, и, если да, читает его двоичные данные.
В случае, если файл не существует или происходит ошибка при чтении, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла или `None`, если файл не существует или произошла ошибка.

**Примеры**:

```python
file_name = 'path/to/file.txt'
file_data = get_raw_image_data(file_name)
```

### `random_image`

```python
def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Recursively searches for a random image in the specified directory.

    Args:
        root_path (Union[str, Path]): The directory to search for images.

    Returns:
        Optional[str]: The path to a random image, or None if no images are found.
    """
```

**Назначение**: Рекурсивно ищет случайное изображение в указанном каталоге.

**Как работает функция**:
Функция принимает путь к каталогу.
Она рекурсивно ищет файлы изображений с определенными расширениями ('.jpg', '.jpeg', '.png', '.gif', '.bmp') в указанном каталоге.
Если изображения найдены, функция выбирает случайное изображение и возвращает его путь.
В случае, если изображения не найдены, функция логирует предупреждение и возвращает `None`.

**Параметры**:
- `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
- `Optional[str]`: Путь к случайному изображению или `None`, если изображения не найдены.

**Примеры**:

```python
root_path = 'path/to/directory'
random_image_path = random_image(root_path)
```

### `add_text_watermark`

```python
def add_text_watermark(image_path: str | Path, watermark_text: str, output_path: Optional[str | Path] = None) -> Optional[str]:
    """
    Adds a text watermark to an image.

    Args:
        image_path (Union[str, Path]): Path to the image file.
        watermark_text (str): Text to use as the watermark.
        output_path (Optional[Union[str, Path]]): Path to save the watermarked image.
            Defaults to overwriting the original image.

    Returns:
        Optional[str]: Path to the watermarked image, or None on failure.
    """
```

**Назначение**: Добавляет текстовый водяной знак к изображению.

**Как работает функция**:
Функция принимает путь к изображению, текст водяного знака и путь для сохранения изображения с водяным знаком.
Она использует библиотеку `PIL` (Pillow) для добавления водяного знака на изображение.
Если `output_path` не указан, изображение перезаписывается.
В случае возникновения ошибок при добавлении водяного знака, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст для использования в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком или `None` в случае неудачи.

**Примеры**:

```python
image_path = 'path/to/image.png'
watermark_text = 'Watermark'
output_path = 'path/to/watermarked_image.png'
add_text_watermark(image_path, watermark_text, output_path)
```

### `add_image_watermark`

```python
def add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]:
    """
    Adds a watermark to an image and saves the result to the specified output path.

    Args:
        input_image_path (Path): Path to the input image.
        watermark_image_path (Path): Path to the watermark image.
        output_image_path (Optional[Path]): Path to save the watermarked image.
            If not provided, the image will be saved in an "output" directory.

    Returns:
        Optional[Path]: Path to the saved watermarked image, or None if the operation failed.
    """
```

**Назначение**: Добавляет водяной знак к изображению и сохраняет результат по указанному пути вывода.

**Как работает функция**:
Функция принимает путь к исходному изображению, путь к изображению водяного знака и путь для сохранения изображения с водяным знаком.
Она использует библиотеку `PIL` (Pillow) для добавления водяного знака на изображение.
Если `output_image_path` не указан, изображение сохраняется в каталоге "output".
В случае возникновения ошибок при добавлении водяного знака, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком. Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком или `None`, если операция не удалась.

**Примеры**:

```python
input_image_path = Path('path/to/image.png')
watermark_image_path = Path('path/to/watermark.png')
output_image_path = Path('path/to/watermarked_image.png')
add_image_watermark(input_image_path, watermark_image_path, output_image_path)
```

### `resize_image`

```python
def resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Resizes an image to the specified dimensions.

    Args:
        image_path (Union[str, Path]): Path to the image file.
        size (Tuple[int, int]): A tuple containing the desired width and height of the image.
        output_path (Optional[Union[str, Path]]): Path to save the resized image.
            Defaults to overwriting the original image.

    Returns:
        Optional[str]: Path to the resized image, or None on failure.
    """
```

**Назначение**: Изменяет размер изображения до указанных размеров.

**Как работает функция**:
Функция принимает путь к изображению, размеры (ширина и высота) и путь для сохранения измененного изображения.
Она использует библиотеку `PIL` (Pillow) для изменения размера изображения.
Если `output_path` не указан, изображение перезаписывается.
В случае возникновения ошибок при изменении размера изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к измененному изображению или `None` в случае неудачи.

**Примеры**:

```python
image_path = 'path/to/image.png'
size = (800, 600)
output_path = 'path/to/resized_image.png'
resize_image(image_path, size, output_path)
```

### `convert_image`

```python
def convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Converts an image to the specified format.

    Args:
        image_path (Union[str, Path]): Path to the image file.
        format (str): Format to convert image to (e.g., "JPEG", "PNG").
        output_path (Optional[Union[str, Path]]): Path to save the converted image.
            Defaults to overwriting the original image.

    Returns:
        Optional[str]: Path to the converted image or None on failure.
    """
```

**Назначение**: Преобразует изображение в указанный формат.

**Как работает функция**:
Функция принимает путь к изображению, формат для преобразования (например, "JPEG", "PNG") и путь для сохранения преобразованного изображения.
Она использует библиотеку `PIL` (Pillow) для преобразования изображения в указанный формат.
Если `output_path` не указан, изображение перезаписывается.
В случае возникновения ошибок при преобразовании изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `format` (str): Формат для преобразования изображения (например, "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к преобразованному изображению или `None` в случае неудачи.

**Примеры**:

```python
image_path = 'path/to/image.png'
format = 'JPEG'
output_path = 'path/to/converted_image.jpg'
convert_image(image_path, format, output_path)
```

### `process_images_with_watermark`

```python
def process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None:
    """
    Processes all images in the specified folder by adding a watermark and saving them in an "output" directory.

    Args:
        folder_path (Path): Path to the folder containing images.
        watermark_path (Path): Path to the watermark image.
    """
```

**Назначение**: Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в каталоге "output".

**Как работает функция**:
Функция принимает путь к папке с изображениями и путь к изображению водяного знака.
Она создает каталог "output", если он не существует, и обрабатывает каждый файл изображения в папке, добавляя водяной знак.
В случае, если папка не существует, функция логирует ошибку и завершает работу.

**Параметры**:
- `folder_path` (Path): Путь к папке, содержащей изображения.
- `watermark_path` (Path): Путь к изображению водяного знака.

**Примеры**:

```python
folder_path = Path('path/to/images')
watermark_path = Path('path/to/watermark.png')
process_images_with_watermark(folder_path, watermark_path)
```