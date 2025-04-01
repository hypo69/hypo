# Модуль для работы с изображениями
======================================

Модуль `src.utils.image` предоставляет асинхронные функции для скачивания, сохранения и обработки изображений.
Он включает в себя функциональность, такую как сохранение изображений из URL, сохранение данных изображений в файлы,
извлечение данных изображений, поиск случайных изображений в каталогах, добавление водяных знаков, изменение размера,
и преобразование форматов изображений.

Пример использования
----------------------

```python
from pathlib import Path
from src.utils.image import save_image_from_url_async

async def main():
    image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
    file_name = Path("downloaded_image.gif")
    result = await save_image_from_url_async(image_url, file_name)
    if result:
        print(f"Изображение сохранено в: {result}")
    else:
        print("Не удалось сохранить изображение.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

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

## Подробнее

Модуль предназначен для облегчения операций с изображениями, такими как скачивание, сохранение, изменение размера и добавление водяных знаков. Он предоставляет набор функций, которые могут быть использованы для автоматизации обработки изображений в различных приложениях.
Использование асинхронных функций позволяет выполнять операции с изображениями не блокируя основной поток выполнения программы.

## Классы

### `ImageError`

**Описание**: Пользовательское исключение для ошибок, связанных с обработкой изображений.

**Наследует**:
   - `Exception`

**Атрибуты**:
   - Отсутствуют

**Методы**:
   - Отсутствуют

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

**Назначение**: Асинхронно скачивает изображение по URL и сохраняет его локально.

**Параметры**:
   - `image_url` (str): URL изображения для скачивания.
   - `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
   - `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
   - `ImageError`: Если скачивание или сохранение изображения не удалось.

**Как работает функция**:
 1. Функция принимает URL изображения и имя файла для сохранения.
 2. Использует `aiohttp.ClientSession` для асинхронного скачивания изображения.
 3. Проверяет статус ответа, чтобы убедиться, что запрос выполнен успешно.
 4. Получает данные изображения в виде байтов.
 5. Вызывает `save_image_async` для сохранения данных изображения в файл.
 6. Возвращает путь к сохраненному файлу или `None` в случае ошибки.

```
A [Начало]
|
B [Асинхронное скачивание изображения по URL]
|
C [Проверка статуса ответа]
|
D [Получение данных изображения в виде байтов]
|
E [Сохранение данных изображения в файл через save_image_async]
|
F [Возврат пути к сохраненному файлу или None]
|
G [Завершение]
```

**Примеры**:

```python
from pathlib import Path
import asyncio
from src.utils.image import save_image_from_url_async

async def main():
    image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
    file_name = Path("downloaded_image.gif")
    result = await save_image_from_url_async(image_url, file_name)
    if result:
        print(f"Изображение сохранено в: {result}")
    else:
        print("Не удалось сохранить изображение.")

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
```

**Назначение**: Сохраняет данные изображения в файл в указанном формате.

**Параметры**:
   - `image_data` (bytes): Бинарные данные изображения.
   - `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
   - `format` (str): Формат сохранения изображения, по умолчанию 'PNG'.

**Возвращает**:
   - `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
   - `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Как работает функция**:
 1. Функция принимает бинарные данные изображения, имя файла и формат для сохранения.
 2. Создает объект `Path` из имени файла.
 3. Создает директорию для файла, если она не существует.
 4. Использует `BytesIO` для работы с данными изображения в памяти.
 5. Открывает изображение с помощью `PIL.Image.open`.
 6. Сохраняет изображение в указанном формате.
 7. Записывает отформатированные данные изображения в файл.
 8. Проверяет, был ли файл создан и не является ли он пустым.
 9. Возвращает путь к сохраненному файлу или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объекта Path из имени файла]
|
C [Создание директории для файла, если она не существует]
|
D [Использование BytesIO для работы с данными изображения в памяти]
|
E [Открытие изображения с помощью PIL.Image.open]
|
F [Сохранение изображения в указанном формате]
|
G [Запись отформатированных данных изображения в файл]
|
H [Проверка, был ли файл создан и не является ли он пустым]
|
I [Возврат пути к сохраненному файлу или None]
|
J [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import save_image

image_data = b"\\x89PNG\\r\\n\\x1A\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x01\\x08\\x06\\x00\\x00\\x00\\x1F\x15\\xC4\\x89\\x00\\x00\\x00\\nIDATx\\x9CC\\x00\\x01\\x00\\x00\\x00\\xC2\\xA0\\xF7Om\\x00\\x00\\x00\\x00IEND\\xAEB`\\x82"
file_name = Path("saved_image.png")
result = save_image(image_data, file_name)
if result:
    print(f"Изображение сохранено в: {result}")
else:
    print("Не удалось сохранить изображение.")
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

**Параметры**:
   - `image_data` (bytes): Бинарные данные изображения.
   - `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
   - `format` (str): Формат сохранения изображения, по умолчанию 'PNG'.

**Возвращает**:
   - `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
   - `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Как работает функция**:
 1. Функция принимает бинарные данные изображения, имя файла и формат для сохранения.
 2. Создает объект `Path` из имени файла.
 3. Асинхронно создает директорию для файла, если она не существует.
 4. Использует `aiofiles` для асинхронной записи данных изображения в файл.
 5. ~~Использует `BytesIO` для работы с данными изображения в памяти.~~
 6. ~~Открывает изображение с помощью `PIL.Image.open`.~~
 7. ~~Сохраняет изображение в указанном формате.~~
 8. ~~Записывает отформатированные данные изображения в файл.~~
 9. ~~Проверяет, был ли файл создан и не является ли он пустым.~~
 10. Возвращает путь к сохраненному файлу или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объекта Path из имени файла]
|
C [Асинхронное создание директории для файла, если она не существует]
|
D [Асинхронная запись данных изображения в файл с помощью aiofiles]
|
E [Возврат пути к сохраненному файлу или None]
|
F [Завершение]
```

**Примеры**:

```python
from pathlib import Path
import asyncio
from src.utils.image import save_image_async

async def main():
    image_data = b"\\x89PNG\\r\\n\\x1A\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x01\\x08\\x06\\x00\\x00\\x00\\x1F\x15\\xC4\\x89\\x00\\x00\\x00\\nIDATx\\x9CC\\x00\\x01\\x00\\x00\\x00\\xC2\\xA0\\xF7Om\\x00\\x00\\x00\\x00IEND\\xAEB`\\x82"
    file_name = Path("saved_image_async.png")
    result = await save_image_async(image_data, file_name)
    if result:
        print(f"Изображение сохранено в: {result}")
    else:
        print("Не удалось сохранить изображение.")

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
```

**Назначение**: Читает изображение, используя Pillow, и возвращает его байты в формате JPEG.

**Параметры**:
   - `image_path` (Path): Путь к файлу изображения.
   - `raw` (bool): Если `True`, возвращает объект `BytesIO`; иначе, возвращает `bytes`. По умолчанию `True`.

**Возвращает**:
   - `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG, или `None`, если произошла ошибка.

**Как работает функция**:
 1. Функция принимает путь к файлу изображения и флаг `raw`.
 2. Открывает изображение с помощью `PIL.Image.open`.
 3. Создает объект `BytesIO`.
 4. Сохраняет изображение в формате JPEG в объект `BytesIO`.
 5. Возвращает объект `BytesIO` или байты изображения в зависимости от значения флага `raw`.

```
A [Начало]
|
B [Открытие изображения с помощью PIL.Image.open]
|
C [Создание объекта BytesIO]
|
D [Сохранение изображения в формате JPEG в объект BytesIO]
|
E [Возврат объекта BytesIO или байтов изображения в зависимости от флага raw]
|
F [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import get_image_bytes

image_path = Path("saved_image.png")
image_bytes = get_image_bytes(image_path)
if image_bytes:
    print(f"Байты изображения: {image_bytes[:100]}...")
else:
    print("Не удалось получить байты изображения.")
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

**Назначение**: Извлекает необработанные бинарные данные файла, если он существует.

**Параметры**:
   - `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
   - `Optional[bytes]`: Бинарные данные файла, или `None`, если файл не существует или произошла ошибка.

**Как работает функция**:
 1. Функция принимает имя файла.
 2. Создает объект `Path` из имени файла.
 3. Проверяет, существует ли файл.
 4. Читает бинарные данные файла.
 5. Возвращает бинарные данные файла или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объекта Path из имени файла]
|
C [Проверка, существует ли файл]
|
D [Чтение бинарных данных файла]
|
E [Возврат бинарных данных файла или None]
|
F [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import get_raw_image_data

file_name = Path("saved_image.png")
raw_data = get_raw_image_data(file_name)
if raw_data:
    print(f"Необработанные бинарные данные: {raw_data[:100]}...")
else:
    print("Не удалось получить необработанные бинарные данные.")
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

**Параметры**:
   - `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
   - `Optional[str]`: Путь к случайному изображению, или `None`, если изображения не найдены.

**Как работает функция**:
 1. Функция принимает путь к корневому каталогу.
 2. Создает объект `Path` из пути к корневому каталогу.
 3. Определяет список расширений изображений.
 4. Рекурсивно ищет файлы изображений в каталоге и его подкаталогах.
 5. Если изображения не найдены, возвращает `None`.
 6. Выбирает случайное изображение из списка найденных файлов.
 7. Возвращает путь к случайному изображению.

```
A [Начало]
|
B [Создание объекта Path из пути к корневому каталогу]
|
C [Определение списка расширений изображений]
|
D [Рекурсивный поиск файлов изображений в каталоге и его подкаталогах]
|
E [Если изображения не найдены, возврат None]
|
F [Выбор случайного изображения из списка найденных файлов]
|
G [Возврат пути к случайному изображению]
|
H [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import random_image

root_path = Path(".")
random_image_path = random_image(root_path)
if random_image_path:
    print(f"Случайное изображение: {random_image_path}")
else:
    print("Изображения не найдены.")
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

**Назначение**: Добавляет текстовый водяной знак на изображение.

**Параметры**:
   - `image_path` (Union[str, Path]): Путь к файлу изображения.
   - `watermark_text` (str): Текст для использования в качестве водяного знака.
   - `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком.
     По умолчанию перезаписывает исходное изображение.

**Возвращает**:
   - `Optional[str]`: Путь к изображению с водяным знаком, или `None` в случае неудачи.

**Как работает функция**:
 1. Функция принимает путь к изображению, текст водяного знака и путь для сохранения.
 2. Создает объекты `Path` из путей к изображению и для сохранения.
 3. Открывает изображение с помощью `PIL.Image.open` и конвертирует его в формат RGBA.
 4. Создает прозрачный слой для водяного знака.
 5. Инициализирует объект `ImageDraw` для рисования на прозрачном слое.
 6. Определяет размер шрифта на основе размера изображения.
 7. Загружает шрифт Arial или использует шрифт по умолчанию, если Arial не найден.
 8. Определяет размеры текста водяного знака.
 9. Вычисляет координаты для размещения текста по центру изображения.
 10. Рисует текст на прозрачном слое.
 11. Объединяет изображение и водяной знак.
 12. Сохраняет изображение с водяным знаком.
 13. Возвращает путь к изображению с водяным знаком или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объектов Path из путей к изображению и для сохранения]
|
C [Открытие изображения и конвертация в формат RGBA]
|
D [Создание прозрачного слоя для водяного знака]
|
E [Инициализация объекта ImageDraw для рисования на прозрачном слое]
|
F [Определение размера шрифта на основе размера изображения]
|
G [Загрузка шрифта Arial или использование шрифта по умолчанию, если Arial не найден]
|
H [Определение размеров текста водяного знака]
|
I [Вычисление координат для размещения текста по центру изображения]
|
J [Рисование текста на прозрачном слое]
|
K [Объединение изображения и водяного знака]
|
L [Сохранение изображения с водяным знаком]
|
M [Возврат пути к изображению с водяным знаком или None]
|
N [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import add_text_watermark

image_path = Path("saved_image.png")
watermark_text = "Watermark"
output_path = Path("watermarked_image.png")
result = add_text_watermark(image_path, watermark_text, output_path)
if result:
    print(f"Изображение с водяным знаком сохранено в: {result}")
else:
    print("Не удалось добавить водяной знак.")
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

**Назначение**: Добавляет изображение водяного знака на изображение и сохраняет результат по указанному пути.

**Параметры**:
   - `input_image_path` (Path): Путь к исходному изображению.
   - `watermark_image_path` (Path): Путь к изображению водяного знака.
   - `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком.
     Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
   - `Optional[Path]`: Путь к сохраненному изображению с водяным знаком, или `None`, если операция не удалась.

**Как работает функция**:
 1. Функция принимает пути к исходному изображению, изображению водяного знака и путь для сохранения.
 2. Открывает исходное изображение с помощью `PIL.Image.open`.
 3. Открывает изображение водяного знака и конвертирует его в формат RGBA.
 4. Определяет размер водяного знака (8% от ширины исходного изображения).
 5. Изменяет размер водяного знака.
 6. Вычисляет позицию для размещения водяного знака (в нижнем правом углу с отступом 20px).
 7. Создает новый прозрачный слой для объединения изображений.
 8. Вставляет исходное изображение на новый слой.
 9. Вставляет водяной знак поверх исходного изображения.
 10. Проверяет режим изображения и конвертирует прозрачный слой в исходный режим.
 11. Сохраняет конечное изображение по указанному пути с оптимизированным качеством.
 12. Возвращает путь к сохраненному изображению с водяным знаком или `None` в случае ошибки.

```
A [Начало]
|
B [Открытие исходного изображения]
|
C [Открытие изображения водяного знака и конвертация в RGBA]
|
D [Определение размера водяного знака (8% от ширины исходного изображения)]
|
E [Изменение размера водяного знака]
|
F [Вычисление позиции для размещения водяного знака]
|
G [Создание нового прозрачного слоя для объединения изображений]
|
H [Вставка исходного изображения на новый слой]
|
I [Вставка водяного знака поверх исходного изображения]
|
J [Проверка режима изображения и конвертация прозрачного слоя в исходный режим]
|
K [Сохранение конечного изображения по указанному пути с оптимизированным качеством]
|
L [Возврат пути к сохраненному изображению с водяным знаком или None]
|
N [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import add_image_watermark

input_image_path = Path("saved_image.png")
watermark_image_path = Path("watermark.png")
output_image_path = Path("watermarked_image.png")
result = add_image_watermark(input_image_path, watermark_image_path, output_image_path)
if result:
    print(f"Изображение с водяным знаком сохранено в: {result}")
else:
    print("Не удалось добавить водяной знак.")
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

**Параметры**:
   - `image_path` (Union[str, Path]): Путь к файлу изображения.
   - `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
   - `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения.
     По умолчанию перезаписывает исходное изображение.

**Возвращает**:
   - `Optional[str]`: Путь к измененному изображению, или `None` в случае неудачи.

**Как работает функция**:
 1. Функция принимает путь к изображению, размеры и путь для сохранения.
 2. Создает объекты `Path` из путей к изображению и для сохранения.
 3. Открывает изображение с помощью `PIL.Image.open`.
 4. Изменяет размер изображения до указанных размеров.
 5. Сохраняет измененное изображение.
 6. Возвращает путь к измененному изображению или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объектов Path из путей к изображению и для сохранения]
|
C [Открытие изображения с помощью PIL.Image.open]
|
D [Изменение размера изображения до указанных размеров]
|
E [Сохранение измененного изображения]
|
F [Возврат пути к измененному изображению или None]
|
G [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import resize_image

image_path = Path("saved_image.png")
size = (200, 200)
output_path = Path("resized_image.png")
result = resize_image(image_path, size, output_path)
if result:
    print(f"Изображение изменено и сохранено в: {result}")
else:
    print("Не удалось изменить размер изображения.")
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

**Параметры**:
   - `image_path` (Union[str, Path]): Путь к файлу изображения.
   - `format` (str): Формат для преобразования изображения (например, "JPEG", "PNG").
   - `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения.
     По умолчанию перезаписывает исходное изображение.

**Возвращает**:
   - `Optional[str]`: Путь к преобразованному изображению или `None` в случае неудачи.

**Как работает функция**:
 1. Функция принимает путь к изображению, формат и путь для сохранения.
 2. Создает объекты `Path` из путей к изображению и для сохранения.
 3. Открывает изображение с помощью `PIL.Image.open`.
 4. Сохраняет изображение в указанном формате.
 5. Возвращает путь к преобразованному изображению или `None` в случае ошибки.

```
A [Начало]
|
B [Создание объектов Path из путей к изображению и для сохранения]
|
C [Открытие изображения с помощью PIL.Image.open]
|
D [Сохранение изображения в указанном формате]
|
E [Возврат пути к преобразованному изображению или None]
|
F [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.utils.image import convert_image

image_path = Path("saved_image.png")
format = "JPEG"
output_path = Path("converted_image.jpg")
result = convert_image(image_path, format, output_path)
if result:
    print(f"Изображение преобразовано и сохранено в: {result}")
else:
    print("Не удалось преобразовать изображение.")
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

**Параметры**:
   - `folder_path` (Path): Путь к папке, содержащей изображения.
   - `watermark_path` (Path): Путь к изображению водяного знака.

**Возвращает**:
   - `None`

**Как работает функция**:
 1. Функция принимает пути к папке с изображениями и изображению водяного знака.
 2. Проверяет, существует ли папка с изображениями.
 3. Создает каталог "output", если он не существует.
 4. Перебирает все файлы в папке с изображениями.
 5. Если файл является изображением (PNG, JPG, JPEG), добавляет водяной знак и сохраняет его в каталоге "output".

```
A [Начало]
|
B [Проверка, существует ли папка с изображениями]
|
C [Создание каталога "output", если он не существует]
|
D [Перебор всех файлов в папке с изображениями]
|
E [Если файл является изображением, добавление водяного знака и сохранение в каталоге "output"]
|
F [Завершение]
```

**Примеры**:

```python
from pathlib import Path
from src.