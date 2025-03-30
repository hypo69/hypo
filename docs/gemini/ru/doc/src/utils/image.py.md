# Модуль `src.utils.image`

## Обзор

Модуль `src.utils.image` предоставляет набор асинхронных функций для загрузки, сохранения и обработки изображений. Он включает в себя функциональность для сохранения изображений из URL-адресов, сохранения данных изображений в файлы, получения данных изображений, поиска случайных изображений в каталогах, добавления водяных знаков, изменения размера и преобразования форматов изображений.

## Подробней

Этот модуль предоставляет инструменты для работы с изображениями, такие как загрузка, сохранение, изменение размера и добавление водяных знаков. Он использует библиотеку Pillow (PIL) для обработки изображений и `aiohttp` для асинхронной загрузки изображений из сети. Модуль предназначен для использования в асинхронных приложениях, где требуется эффективная обработка изображений.

## Классы

### `ImageError`

**Описание**: Пользовательское исключение для ошибок, связанных с изображениями.

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
    ...
```

**Описание**: Асинхронно загружает изображение из URL-адреса и сохраняет его локально.

**Параметры**:
- `image_url` (str): URL-адрес для загрузки изображения.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если загрузка или сохранение изображения не удались.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат сохранения изображения, по умолчанию 'PNG'.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен или если сохраненный файл пуст.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Асинхронно сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат сохранения изображения, по умолчанию 'PNG'.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен или если сохраненный файл пуст.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Считывает изображение с использованием Pillow и возвращает его байты в формате JPEG.

**Параметры**:
- `image_path` (Path): Путь к файлу изображения.
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; в противном случае возвращает байты. По умолчанию `True`.

**Возвращает**:
- `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG или `None`, если произошла ошибка.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Извлекает необработанные двоичные данные файла, если он существует.

**Параметры**:
- `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла или `None`, если файл не существует или произошла ошибка.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Рекурсивно ищет случайное изображение в указанном каталоге.

**Параметры**:
- `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
- `Optional[str]`: Путь к случайному изображению или `None`, если изображения не найдены.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Добавляет текстовый водяной знак на изображение.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст для использования в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком или `None` в случае неудачи.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Добавляет изображение водяного знака на изображение и сохраняет результат по указанному пути вывода.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком. Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком или `None`, если операция не удалась.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Изменяет размер изображения до указанных размеров.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного размера изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к измененному размеру изображения или `None` в случае неудачи.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Преобразует изображение в указанный формат.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `format` (str): Формат для преобразования изображения (например, "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к преобразованному изображению или `None` в случае неудачи.

**Примеры**:
```python
# TODO добавить пример
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
    ...
```

**Описание**: Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в каталоге "output".

**Параметры**:
- `folder_path` (Path): Путь к папке, содержащей изображения.
- `watermark_path` (Path): Путь к изображению водяного знака.

**Примеры**:
```python
# TODO добавить пример