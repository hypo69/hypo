# Модуль `src.utils.image`

## Обзор

Модуль `src.utils.image` предоставляет асинхронные функции для скачивания, сохранения и обработки изображений. Он включает в себя функциональность сохранения изображений из URL, сохранения данных изображений в файлы, получения данных изображений, поиска случайных изображений в каталогах, добавления водяных знаков, изменения размера и преобразования форматов изображений.

## Подробней

Этот модуль предоставляет инструменты для работы с изображениями, которые могут быть полезны для различных задач, таких как обработка изображений для веб-сайтов, автоматическое добавление водяных знаков и преобразование форматов изображений. Модуль использует библиотеку `PIL` (Pillow) для обработки изображений и `aiohttp` для асинхронной загрузки изображений из URL.

## Классы

### `ImageError`

**Описание**: Пользовательское исключение для ошибок, связанных с изображениями.

**Как работает класс**:
Этот класс используется для создания пользовательских исключений, которые могут быть вызваны при возникновении ошибок в процессе обработки изображений. Он наследуется от базового класса `Exception`.

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

**Описание**: Асинхронно скачивает изображение по URL и сохраняет его локально.

**Как работает функция**:
Функция принимает URL изображения и имя файла для сохранения. Она использует `aiohttp` для асинхронной загрузки изображения и `save_image_async` для сохранения данных изображения в файл. В случае ошибки при загрузке или сохранении изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_url` (str): URL изображения для скачивания.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если не удалось скачать или сохранить изображение.

**Примеры**:

```python
# Пример вызова функции
image_url = 'https://example.com/image.jpg'
filename = 'image.jpg'
save_image_from_url_async(image_url, filename)
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

**Как работает функция**:
Функция принимает бинарные данные изображения, имя файла для сохранения и формат изображения. Она создает каталог для файла, если он не существует, и сохраняет данные изображения в файл с использованием библиотеки `PIL`. В случае ошибки при создании или сохранении файла, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат изображения, по умолчанию `PNG`.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если не удалось создать или сохранить файл, или если сохраненный файл пуст.

**Примеры**:

```python
# Пример вызова функции
image_data = b'...'  # Replace with actual image data
file_name = 'image.png'
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
    ...
```

**Описание**: Асинхронно сохраняет данные изображения в файл в указанном формате.

**Как работает функция**:
Функция принимает бинарные данные изображения, имя файла для сохранения и формат изображения. Она создает каталог для файла, если он не существует, и сохраняет данные изображения в файл с использованием библиотеки `aiofiles`. В случае ошибки при создании или сохранении файла, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат изображения, по умолчанию `PNG`.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если не удалось создать или сохранить файл, или если сохраненный файл пуст.

**Примеры**:

```python
# Пример вызова функции
image_data = b'...'  # Replace with actual image data
file_name = 'image.png'
save_image_async(image_data, file_name)
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

**Описание**: Читает изображение с использованием Pillow и возвращает его байты в формате JPEG.

**Как работает функция**:
Функция принимает путь к файлу изображения и флаг, указывающий, возвращать ли `BytesIO` объект или байты. Она открывает изображение с помощью библиотеки `PIL`, сохраняет его в формате JPEG в `BytesIO` объект и возвращает его или его байтовое представление. В случае ошибки при чтении изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Path): Путь к файлу изображения.
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; в противном случае возвращает байты. По умолчанию `True`.

**Возвращает**:
- `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG, или `None`, если произошла ошибка.

**Примеры**:

```python
# Пример вызова функции
image_path = Path('image.jpg')
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
    ...
```

**Описание**: Извлекает необработанные двоичные данные файла, если он существует.

**Как работает функция**:
Функция принимает имя файла или путь к файлу. Она проверяет, существует ли файл, и, если да, читает его двоичные данные и возвращает их. В случае, если файл не существует или произошла ошибка при чтении файла, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла, или `None`, если файл не существует или произошла ошибка.

**Примеры**:

```python
# Пример вызова функции
file_name = 'image.jpg'
raw_image_data = get_raw_image_data(file_name)
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

**Как работает функция**:
Функция принимает путь к каталогу. Она рекурсивно ищет файлы изображений в каталоге и его подкаталогах, используя заданные расширения файлов. Если изображения найдены, функция выбирает случайное изображение и возвращает его путь. Если изображения не найдены, функция логирует предупреждение и возвращает `None`.

**Параметры**:
- `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
- `Optional[str]`: Путь к случайному изображению, или `None`, если изображения не найдены.

**Примеры**:

```python
# Пример вызова функции
root_path = 'images'
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
    ...
```

**Описание**: Добавляет текстовый водяной знак на изображение.

**Как работает функция**:
Функция принимает путь к файлу изображения, текст водяного знака и путь для сохранения изображения с водяным знаком. Она открывает изображение с помощью библиотеки `PIL`, создает прозрачный слой для водяного знака, рисует текст на этом слое и объединяет изображение и водяной знак. Затем она сохраняет изображение с водяным знаком в указанный файл. Если путь для сохранения не указан, изображение перезаписывается. В случае ошибки при обработке изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст для использования в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком, или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции
image_path = 'image.jpg'
watermark_text = 'My Watermark'
add_text_watermark(image_path, watermark_text)
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

**Описание**: Добавляет водяной знак изображения на другое изображение и сохраняет результат по указанному пути.

**Как работает функция**:
Функция принимает путь к исходному изображению, путь к изображению водяного знака и путь для сохранения изображения с водяным знаком. Она открывает оба изображения с помощью библиотеки `PIL`, изменяет размер водяного знака, определяет позицию для размещения водяного знака в правом нижнем углу исходного изображения с отступом в 20 пикселей от краев. Затем она создает новый прозрачный слой, на который помещает исходное изображение и водяной знак, и сохраняет полученное изображение с водяным знаком в указанный файл. Если путь для сохранения не указан, изображение сохраняется в подкаталоге "output". В случае ошибки при обработке изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком. Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком, или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции
input_image_path = Path('image.jpg')
watermark_image_path = Path('watermark.png')
add_image_watermark(input_image_path, watermark_image_path)
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

**Как работает функция**:
Функция принимает путь к файлу изображения, размеры (ширина и высота) и путь для сохранения измененного изображения. Она открывает изображение с помощью библиотеки `PIL`, изменяет его размер и сохраняет измененное изображение в указанный файл. Если путь для сохранения не указан, исходное изображение перезаписывается. В случае ошибки при обработке изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к измененному изображению, или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции
image_path = 'image.jpg'
size = (800, 600)
resize_image(image_path, size)
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

**Как работает функция**:
Функция принимает путь к файлу изображения, формат для преобразования и путь для сохранения преобразованного изображения. Она открывает изображение с помощью библиотеки `PIL`, преобразует его в указанный формат и сохраняет преобразованное изображение в указанный файл. Если путь для сохранения не указан, исходное изображение перезаписывается. В случае ошибки при обработке изображения, функция логирует ошибку и возвращает `None`.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `format` (str): Формат для преобразования изображения (например, "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к преобразованному изображению, или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции
image_path = 'image.jpg'
format = 'PNG'
convert_image(image_path, format)
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

**Как работает функция**:
Функция принимает путь к папке с изображениями и путь к изображению водяного знака. Она создает каталог "output", если он не существует, и обрабатывает каждый файл изображения в папке, добавляя водяной знак с помощью функции `add_image_watermark` и сохраняя его в каталоге "output". В случае ошибки при обработке изображения, функция логирует ошибку.

**Параметры**:
- `folder_path` (Path): Путь к папке, содержащей изображения.
- `watermark_path` (Path): Путь к изображению водяного знака.

**Примеры**:

```python
# Пример вызова функции
folder_path = Path('images')
watermark_path = Path('watermark.png')
process_images_with_watermark(folder_path, watermark_path)
```