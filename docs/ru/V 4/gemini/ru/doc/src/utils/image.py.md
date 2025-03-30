# Модуль src.utils.image

## Обзор

Модуль предоставляет асинхронные функции для загрузки, сохранения и обработки изображений.
Он включает в себя такие функции, как сохранение изображений из URL-адресов, сохранение данных изображений в файлы,
получение данных изображений, поиск случайных изображений в каталогах, добавление водяных знаков, изменение размера
и преобразование форматов изображений.

## Подробней

Этот модуль предоставляет набор утилит для работы с изображениями, включая загрузку, сохранение, изменение размера и добавление водяных знаков.
Он использует библиотеки `aiohttp`, `aiofiles` и `PIL (Pillow)` для обеспечения асинхронной и эффективной обработки изображений.

Модуль предназначен для использования в проектах, где требуется обрабатывать изображения, например, для создания
миниатюр, добавления водяных знаков или преобразования форматов. Он может быть использован как часть веб-сервиса
или приложения для обработки изображений в пакетном режиме.

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
- `image_url` (str): URL-адрес изображения для загрузки.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если загрузка или сохранение изображения не удались.

**Как работает функция**:

```ascii
    +-----------------------+
    |  save_image_from_url_async  |
    +-----------------------+
             |
             V
    +-----------------------+
    |  aiohttp.ClientSession  |
    +-----------------------+
             |
             V
    +-----------------------+
    |   session.get(image_url)  |
    +-----------------------+
             |
             V
    +-----------------------+
    |   response.read()      |
    +-----------------------+
             |
             V
    +-----------------------+
    |   save_image_async     |
    +-----------------------+
             |
             V
    +-----------------------+
    |      Сохранение файла    |
    +-----------------------+
```

**Примеры**:

```python
import asyncio
from pathlib import Path

async def main():
    image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
    filename = Path("test_image.gif")
    result = await save_image_from_url_async(image_url, filename)
    if result:
        print(f"Image saved to {result}")
    else:
        print("Image saving failed")

if __name__ == "__main__":
    asyncio.run(main())
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

**Как работает функция**:

```ascii
    +-----------------------+
    |      save_image       |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(file_name)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |   Создание директории  |
    +-----------------------+
             |
             V
    +-----------------------+
    |      BytesIO(image_data)|
    +-----------------------+
             |
             V
    +-----------------------+
    |       Image.open       |
    +-----------------------+
             |
             V
    +-----------------------+
    |        img.save        |
    +-----------------------+
             |
             V
    +-----------------------+
    |   Проверка размера файла|
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

image_data = b"данные изображения"  # Замените на реальные данные изображения
filename = Path("test_image.png")
result = save_image(image_data, filename)
if result:
    print(f"Image saved to {result}")
else:
    print("Image saving failed")
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

**Как работает функция**:

```ascii
    +-----------------------+
    |   save_image_async    |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(file_name)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Создание директории  |
    +-----------------------+
             |
             V
    +-----------------------+
    |  aiofiles.open(file_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |   file.write(image_data)|
    +-----------------------+
             |
             V
    +-----------------------+
    | Проверка размера файла |
    +-----------------------+
```

**Примеры**:

```python
import asyncio
from pathlib import Path

async def main():
    image_data = b"данные изображения"  # Замените на реальные данные изображения
    filename = Path("test_image_async.png")
    result = await save_image_async(image_data, filename)
    if result:
        print(f"Image saved to {result}")
    else:
        print("Image saving failed")

if __name__ == "__main__":
    asyncio.run(main())
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
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; в противном случае возвращает `bytes`. По умолчанию `True`.

**Возвращает**:
- `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG или `None`, если произошла ошибка.

**Как работает функция**:

```ascii
    +-----------------------+
    |    get_image_bytes    |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Image.open(image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |        BytesIO()       |
    +-----------------------+
             |
             V
    +-----------------------+
    |   img.save(format="JPEG")|
    +-----------------------+
             |
             V
    +-----------------------+
    |    Возврат BytesIO или bytes |
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

image_path = Path("test_image.png")  # Замените на существующий файл изображения
image_bytes = get_image_bytes(image_path)
if image_bytes:
    print(f"Image bytes: {image_bytes[:100]}...")  # Вывод первых 100 байт
else:
    print("Failed to read image bytes")
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

**Как работает функция**:

```ascii
    +-----------------------+
    |  get_raw_image_data   |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(file_name)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Проверка существования файла |
    +-----------------------+
             |
             V
    +-----------------------+
    |    file_path.read_bytes()|
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

file_path = Path("test_image.png")  # Замените на существующий файл
raw_data = get_raw_image_data(file_path)
if raw_data:
    print(f"Raw data: {raw_data[:100]}...")  # Вывод первых 100 байт
else:
    print("Failed to read raw data")
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

**Как работает функция**:

```ascii
    +-----------------------+
    |     random_image      |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(root_path)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |   root_path.rglob("*") |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Фильтрация файлов по расширению |
    +-----------------------+
             |
             V
    +-----------------------+
    | random.choice(image_files)|
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

root_path = Path(".")  # Текущий каталог
random_image_path = random_image(root_path)
if random_image_path:
    print(f"Random image: {random_image_path}")
else:
    print("No images found")
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

**Описание**: Добавляет текстовый водяной знак к изображению.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст для использования в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком или `None` в случае ошибки.

**Как работает функция**:

```ascii
    +-----------------------+
    |  add_text_watermark   |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(image_path)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Image.open(image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |  Создание прозрачного слоя |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Рисование текста на слое |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Объединение слоев     |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Сохранение изображения |
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

image_path = Path("test_image.png")  # Замените на существующий файл изображения
watermark_text = "Пример водяного знака"
output_path = Path("watermarked_image.png")
result = add_text_watermark(image_path, watermark_text, output_path)
if result:
    print(f"Watermarked image saved to {result}")
else:
    print("Failed to add watermark")
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

**Описание**: Добавляет водяной знак к изображению и сохраняет результат по указанному пути вывода.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком. Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком или `None`, если операция не удалась.

**Как работает функция**:

```ascii
    +-----------------------+
    |  add_image_watermark  |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Image.open(input_image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    | Image.open(watermark_image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |  Изменение размера водяного знака|
    +-----------------------+
             |
             V
    +-----------------------+
    |  Создание прозрачного слоя |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Объединение слоев     |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Сохранение изображения |
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

input_image_path = Path("test_image.png")  # Замените на существующий файл изображения
watermark_image_path = Path("watermark.png")  # Замените на существующий файл водяного знака
output_image_path = Path("watermarked_image.png")
result = add_image_watermark(input_image_path, watermark_image_path, output_image_path)
if result:
    print(f"Watermarked image saved to {result}")
else:
    print("Failed to add watermark")
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
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с измененным размером. По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с измененным размером или `None` в случае ошибки.

**Как работает функция**:

```ascii
    +-----------------------+
    |     resize_image      |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(image_path)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Image.open(image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |       img.resize(size)  |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Сохранение изображения |
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

image_path = Path("test_image.png")  # Замените на существующий файл изображения
size = (500, 500)  # Новые размеры изображения
output_path = Path("resized_image.png")
result = resize_image(image_path, size, output_path)
if result:
    print(f"Resized image saved to {result}")
else:
    print("Failed to resize image")
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
- `Optional[str]`: Путь к преобразованному изображению или `None` в случае ошибки.

**Как работает функция**:

```ascii
    +-----------------------+
    |     convert_image     |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Path(image_path)    |
    +-----------------------+
             |
             V
    +-----------------------+
    |    Image.open(image_path)|
    +-----------------------+
             |
             V
    +-----------------------+
    |   img.save(format=format)|
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

image_path = Path("test_image.png")  # Замените на существующий файл изображения
format = "JPEG"  # Формат для преобразования
output_path = Path("converted_image.jpg")
result = convert_image(image_path, format, output_path)
if result:
    print(f"Converted image saved to {result}")
else:
    print("Failed to convert image")
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

**Как работает функция**:

```ascii
    +-----------------------+
    |process_images_with_watermark|
    +-----------------------+
             |
             V
    +-----------------------+
    |   Проверка папки     |
    +-----------------------+
             |
             V
    +-----------------------+
    |   Создание "output"  |
    +-----------------------+
             |
             V
    +-----------------------+
    |  Перебор файлов в папке|
    +-----------------------+
             |
             V
    +-----------------------+
    | add_image_watermark   |
    +-----------------------+
```

**Примеры**:

```python
from pathlib import Path

folder_path = Path("images")  # Замените на существующую папку с изображениями
watermark_path = Path("watermark.png")  # Замените на существующий файл водяного знака
process_images_with_watermark(folder_path, watermark_path)