# Модуль для работы с изображениями
=========================================

Модуль `src.utils.image` предоставляет асинхронные функции для скачивания, сохранения и обработки изображений.
Он включает в себя функциональность сохранения изображений из URL, сохранения данных изображения в файлы,
получения данных изображения, поиска случайных изображений в каталогах, добавления водяных знаков, изменения размера
и преобразования форматов изображений.

Пример использования
----------------------

```python
from pathlib import Path
from src.utils.image import save_image_from_url_async

async def main():
    image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
    filename = Path("test_image.gif")
    saved_path = await save_image_from_url_async(image_url, filename)
    if saved_path:
        print(f"Изображение сохранено в: {saved_path}")
    else:
        print("Не удалось сохранить изображение.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Оглавление

- [Классы](#классы)
    - [ImageError](#imageerror)
- [Функции](#функции)
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

## Обзор

Модуль `src.utils.image` предоставляет набор инструментов для работы с изображениями, включая загрузку, сохранение, изменение размера, добавление водяных знаков и преобразование форматов. Он использует библиотеки `aiohttp`, `aiofiles`, `asyncio` и `PIL (Pillow)` для асинхронной обработки изображений.

## Подробнее

Модуль предназначен для выполнения различных операций с изображениями, такими как загрузка изображений из интернета, сохранение изображений на диск, изменение размеров изображений и добавление водяных знаков. Он предоставляет как синхронные, так и асинхронные функции для выполнения этих операций. Асинхронные функции позволяют выполнять операции с изображениями без блокировки основного потока выполнения, что особенно полезно при работе с большим количеством изображений или при выполнении операций в веб-приложениях.

## Классы

### `ImageError`

**Описание**: Пользовательское исключение для ошибок, связанных с обработкой изображений.

**Наследует**:
- `Exception`: Наследует класс `Exception`.

**Атрибуты**:
- Нет дополнительных атрибутов.

**Методы**:
- Нет дополнительных методов.

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

**Назначение**: Асинхронно скачивает изображение из URL и сохраняет его локально.

**Параметры**:
- `image_url` (str): URL изображения для скачивания.
- `filename` (Union[str, Path]): Имя файла для сохранения изображения.

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если скачивание или сохранение изображения не удалось.

**Как работает функция**:
1. Функция принимает URL изображения и имя файла в качестве аргументов.
2. Открывает асинхронную сессию с помощью `aiohttp.ClientSession`.
3. Отправляет GET-запрос к указанному URL для скачивания изображения.
4. Проверяет статус ответа и вызывает исключение `HTTPError` для плохих ответов (4xx или 5xx).
5. Считывает данные изображения из ответа.
6. Вызывает функцию `save_image_async` для сохранения изображения в файл.
7. Возвращает путь к сохраненному файлу или `None`, если операция не удалась.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
import asyncio
from pathlib import Path
from src.utils.image import save_image_from_url_async

async def main():
    image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
    filename = Path("test_image.gif")
    saved_path = await save_image_from_url_async(image_url, filename)
    if saved_path:
        print(f"Изображение сохранено в: {saved_path}")
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
    ...
```

**Назначение**: Сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат сохранения изображения (по умолчанию 'PNG').

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Как работает функция**:
1. Функция принимает бинарные данные изображения, имя файла и формат в качестве аргументов.
2. Создает объект `Path` из имени файла.
3. Создает родительский каталог файла, если он не существует.
4. Использует `BytesIO` для избежания двойной записи на диск.
5. Открывает изображение из `BytesIO` с помощью `PIL.Image.open`.
6. Сохраняет изображение в `BytesIO` в указанном формате.
7. Получает бинарные данные изображения из `BytesIO`.
8. Записывает данные изображения в файл.
9. Проверяет, был ли создан файл и не является ли он пустым.
10. Возвращает путь к сохраненному файлу или `None`, если операция не удалась.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import save_image, get_raw_image_data

# Пример использования
image_path = Path("example.jpg")  # Замените на путь к вашему изображению
image_data = get_raw_image_data(image_path)  # Функция для получения бинарных данных изображения

if image_data:
    saved_path = save_image(image_data, "saved_image.png", format="PNG")
    if saved_path:
        print(f"Изображение успешно сохранено в: {saved_path}")
    else:
        print("Не удалось сохранить изображение.")
else:
    print("Не удалось получить данные изображения.")
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

**Назначение**: Асинхронно сохраняет данные изображения в файл в указанном формате.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (Union[str, Path]): Имя файла для сохранения изображения.
- `format` (str): Формат сохранения изображения (по умолчанию 'PNG').

**Возвращает**:
- `Optional[str]`: Путь к сохраненному файлу, или `None`, если операция не удалась.

**Вызывает исключения**:
- `ImageError`: Если файл не может быть создан, сохранен, или если сохраненный файл пуст.

**Как работает функция**:
1. Функция принимает бинарные данные изображения, имя файла и формат в качестве аргументов.
2. Создает объект `Path` из имени файла.
3. Асинхронно создает родительский каталог файла, если он не существует.
4. Использует `BytesIO` для избежания двойной записи на диск.
5. Открывает изображение из `BytesIO` с помощью `PIL.Image.open`.
6. Сохраняет изображение в `BytesIO` в указанном формате.
7. Получает бинарные данные изображения из `BytesIO`.
8. Асинхронно записывает данные изображения в файл.
9. Асинхронно проверяет, был ли создан файл и не является ли он пустым.
10. Возвращает путь к сохраненному файлу или `None`, если операция не удалась.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
import asyncio
from pathlib import Path
from src.utils.image import save_image_async, get_raw_image_data

async def main():
    # Пример использования
    image_path = Path("example.jpg")  # Замените на путь к вашему изображению
    image_data = get_raw_image_data(image_path)  # Функция для получения бинарных данных изображения

    if image_data:
        saved_path = await save_image_async(image_data, "saved_image_async.png", format="PNG")
        if saved_path:
            print(f"Изображение успешно сохранено в: {saved_path}")
        else:
            print("Не удалось сохранить изображение.")
    else:
        print("Не удалось получить данные изображения.")

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

**Назначение**: Читает изображение с использованием Pillow и возвращает его байты в формате JPEG.

**Параметры**:
- `image_path` (Path): Путь к файлу изображения.
- `raw` (bool): Если `True`, возвращает объект `BytesIO`; иначе, возвращает `bytes`. По умолчанию `True`.

**Возвращает**:
- `Optional[BytesIO | bytes]`: Байты изображения в формате JPEG, или `None`, если произошла ошибка.

**Как работает функция**:
1. Функция принимает путь к файлу изображения и флаг `raw` в качестве аргументов.
2. Открывает изображение с помощью `PIL.Image.open`.
3. Создает объект `BytesIO`.
4. Сохраняет изображение в `BytesIO` в формате JPEG.
5. Возвращает объект `BytesIO` или байты изображения в зависимости от значения флага `raw`.
6. В случае ошибки логирует ее и возвращает `None`.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import get_image_bytes

# Пример использования
image_path = Path("example.jpg")  # Замените на путь к вашему изображению

image_bytes = get_image_bytes(image_path)

if image_bytes:
    print(f"Изображение успешно прочитано, тип: {type(image_bytes)}")
else:
    print("Не удалось прочитать изображение.")
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

**Назначение**: Извлекает необработанные двоичные данные файла, если он существует.

**Параметры**:
- `file_name` (Union[str, Path]): Имя или путь к файлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла, или `None`, если файл не существует или произошла ошибка.

**Как работает функция**:
1. Функция принимает имя файла или путь к файлу в качестве аргумента.
2. Создает объект `Path` из имени файла.
3. Проверяет, существует ли файл.
4. Если файл существует, считывает его двоичные данные с помощью `file_path.read_bytes()`.
5. Возвращает двоичные данные файла или `None`, если файл не существует или произошла ошибка.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import get_raw_image_data

# Пример использования
file_path = Path("example.jpg")  # Замените на путь к вашему файлу

raw_data = get_raw_image_data(file_path)

if raw_data:
    print(f"Данные успешно прочитаны, размер: {len(raw_data)} байт")
else:
    print("Не удалось прочитать данные из файла.")
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

**Назначение**: Рекурсивно ищет случайное изображение в указанном каталоге.

**Параметры**:
- `root_path` (Union[str, Path]): Каталог для поиска изображений.

**Возвращает**:
- `Optional[str]`: Путь к случайному изображению, или `None`, если изображения не найдены.

**Как работает функция**:
1. Функция принимает путь к каталогу в качестве аргумента.
2. Создает объект `Path` из пути к каталогу.
3. Определяет список расширений файлов изображений.
4. Рекурсивно ищет все файлы в каталоге и его подкаталогах.
5. Фильтрует файлы, оставляя только файлы изображений с указанными расширениями.
6. Если изображения не найдены, логирует предупреждение и возвращает `None`.
7. Выбирает случайное изображение из списка найденных изображений.
8. Возвращает путь к случайному изображению.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import random_image

# Пример использования
root_path = Path(".")  # Замените на путь к вашему каталогу с изображениями

random_image_path = random_image(root_path)

if random_image_path:
    print(f"Случайное изображение: {random_image_path}")
else:
    print("Изображения не найдены в указанном каталоге.")
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

**Назначение**: Добавляет текстовый водяной знак на изображение.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `watermark_text` (str): Текст для использования в качестве водяного знака.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком.
  По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к изображению с водяным знаком, или `None` в случае неудачи.

**Как работает функция**:
1. Функция принимает путь к изображению, текст водяного знака и путь для сохранения в качестве аргументов.
2. Создает объекты `Path` из путей к изображению и для сохранения.
3. Открывает изображение с помощью `PIL.Image.open` и преобразует его в формат RGBA.
4. Создает прозрачный слой для водяного знака.
5. Инициализирует объект `ImageDraw` для рисования на прозрачном слое.
6. Определяет размер шрифта на основе размера изображения.
7. Загружает шрифт Arial или использует шрифт по умолчанию, если Arial не найден.
8. Вычисляет размеры текста водяного знака.
9. Вычисляет координаты для размещения текста по центру изображения.
10. Рисует текст на прозрачном слое.
11. Объединяет изображение и водяной знак с помощью `Image.alpha_composite`.
12. Сохраняет изображение с водяным знаком по указанному пути.
13. Возвращает путь к изображению с водяным знаком или `None` в случае неудачи.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import add_text_watermark

# Пример использования
image_path = Path("example.jpg")  # Замените на путь к вашему изображению
watermark_text = "Watermark"
output_path = Path("watermarked_image.jpg")

watermarked_image_path = add_text_watermark(image_path, watermark_text, output_path)

if watermarked_image_path:
    print(f"Изображение с водяным знаком успешно сохранено в: {watermarked_image_path}")
else:
    print("Не удалось добавить водяной знак на изображение.")
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

**Назначение**: Добавляет водяной знак на изображение и сохраняет результат по указанному пути вывода.

**Параметры**:
- `input_image_path` (Path): Путь к исходному изображению.
- `watermark_image_path` (Path): Путь к изображению водяного знака.
- `output_image_path` (Optional[Path]): Путь для сохранения изображения с водяным знаком.
  Если не указан, изображение будет сохранено в каталоге "output".

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному изображению с водяным знаком, или `None`, если операция не удалась.

**Как работает функция**:
1. Функция принимает путь к исходному изображению, путь к изображению водяного знака и путь для сохранения в качестве аргументов.
2. Открывает исходное изображение и изображение водяного знака с помощью `PIL.Image.open`.
3. Преобразует изображение водяного знака в формат RGBA.
4. Изменяет размер водяного знака, чтобы его ширина составляла 8% от ширины исходного изображения.
5. Вычисляет позицию для размещения водяного знака в правом нижнем углу изображения с отступом в 20 пикселей.
6. Создает новый прозрачный слой для объединения изображений.
7. Вставляет исходное изображение на прозрачный слой.
8. Вставляет водяной знак поверх исходного изображения на прозрачном слое.
9. Проверяет режим изображения и преобразует прозрачный слой в соответствующий режим.
10. Сохраняет изображение с водяным знаком по указанному пути.
11. Возвращает путь к изображению с водяным знаком или `None` в случае неудачи.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import add_image_watermark

# Пример использования
input_image_path = Path("example.jpg")  # Замените на путь к вашему изображению
watermark_image_path = Path("watermark.png")  # Замените на путь к вашему водяному знаку
output_image_path = Path("watermarked_image.jpg")

watermarked_image_path = add_image_watermark(input_image_path, watermark_image_path, output_image_path)

if watermarked_image_path:
    print(f"Изображение с водяным знаком успешно сохранено в: {watermarked_image_path}")
else:
    print("Не удалось добавить водяной знак на изображение.")
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

**Назначение**: Изменяет размер изображения до указанных размеров.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `size` (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения измененного изображения.
  По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к измененному изображению, или `None` в случае неудачи.

**Как работает функция**:
1. Функция принимает путь к изображению, размеры и путь для сохранения в качестве аргументов.
2. Создает объекты `Path` из путей к изображению и для сохранения.
3. Открывает изображение с помощью `PIL.Image.open`.
4. Изменяет размер изображения с помощью `img.resize(size)`.
5. Сохраняет измененное изображение по указанному пути.
6. Возвращает путь к измененному изображению или `None` в случае неудачи.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import resize_image

# Пример использования
image_path = Path("example.jpg")  # Замените на путь к вашему изображению
size = (800, 600)  # Новые размеры изображения
output_path = Path("resized_image.jpg")

resized_image_path = resize_image(image_path, size, output_path)

if resized_image_path:
    print(f"Изображение успешно изменено и сохранено в: {resized_image_path}")
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
    ...
```

**Назначение**: Преобразует изображение в указанный формат.

**Параметры**:
- `image_path` (Union[str, Path]): Путь к файлу изображения.
- `format` (str): Формат для преобразования изображения (например, "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения.
  По умолчанию перезаписывает исходное изображение.

**Возвращает**:
- `Optional[str]`: Путь к преобразованному изображению, или `None` в случае неудачи.

**Как работает функция**:
1. Функция принимает путь к изображению, формат и путь для сохранения в качестве аргументов.
2. Создает объекты `Path` из путей к изображению и для сохранения.
3. Открывает изображение с помощью `PIL.Image.open`.
4. Сохраняет изображение в указанном формате с помощью `img.save(output_path, format=format)`.
5. Возвращает путь к преобразованному изображению или `None` в случае неудачи.

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import convert_image

# Пример использования
image_path = Path("example.jpg")  # Замените на путь к вашему изображению
format = "PNG"  # Формат для преобразования
output_path = Path("converted_image.png")

converted_image_path = convert_image(image_path, format, output_path)

if converted_image_path:
    print(f"Изображение успешно преобразовано и сохранено в: {converted_image_path}")
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
    ...
```

**Назначение**: Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в папке "output".

**Параметры**:
- `folder_path` (Path): Путь к папке, содержащей изображения.
- `watermark_path` (Path): Путь к изображению водяного знака.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Функция принимает путь к папке с изображениями и путь к изображению водяного знака в качестве аргументов.
2. Проверяет, является ли указанный путь папкой.
3. Если указанный путь не является папкой, логирует ошибку и завершает выполнение.
4. Создает папку "output" в указанной папке, если она не существует.
5. Перебирает все файлы в указанной папке.
6. Для каждого файла проверяет, является ли он изображением с расширением .png, .jpg или .jpeg.
7. Если файл является изображением, создает путь для сохранения обработанного изображения в папке "output".
8. Вызывает функцию `add_image_watermark` для добавления водяного знака на изображение и сохранения его в папке "output".

**Внутренние функции**:
- Нет внутренних функций.

**Примеры**:
```python
from pathlib import Path
from src.utils.image import process_images_with_watermark

# Пример использования
folder_path = Path("images")  # Замените на путь к вашей папке с изображениями
watermark_path = Path("watermark.png")  # Замените на путь к вашему водяному знаку

process_images_with_watermark(folder_path, watermark_path)