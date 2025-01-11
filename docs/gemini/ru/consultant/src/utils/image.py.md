### Анализ кода модуля `src.utils.image`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Асинхронная обработка изображений для повышения производительности.
    - Использование `Path` для работы с путями.
    - Наличие пользовательского исключения `ImageError`.
    - Логирование ошибок с помощью `logger`.
    - Функции для различных операций с изображениями (загрузка, сохранение, изменение размера, водяные знаки, форматы).
- **Минусы**:
    - Не все функции имеют docstring в формате RST.
    - Не везде используется `from src.logger.logger import logger`.
    - Есть неявные вызовы `Image.open`, которые могут привести к ошибкам.
    - Дублирование `Path` преобразований в функциях.
    - В некоторых местах отсутствует обработка ошибок при работе с файлами.
    - В функции `add_image_watermark`  происходит преобразование режима изображения, что не всегда корректно.
    - Пример использования в конце файла не соответствует концепции модуля.

**Рекомендации по улучшению**:

1.  **Документирование**:
    - Добавить docstring в формате RST для всех функций и классов, включая описание параметров, возвращаемых значений, исключений и примеры использования.
    - Улучшить docstring для класса `ImageError`
    - Добавить краткое описание модуля.

2.  **Импорты**:
    - Использовать `from src.logger.logger import logger` для логирования.
    - Упорядочить импорты по алфавиту.

3.  **Обработка ошибок**:
    - Избегать `try-except` без необходимости, использовать `logger.error` для логирования ошибок.
    - Проверять наличие файла перед операциями с ним.
    - Добавить обработку ошибок при открытии изображения в функции `add_image_watermark`, `resize_image`, `convert_image`.

4.  **Рефакторинг**:
    - Убрать дублирование `Path` преобразования в начале функций, где оно не нужно.
    - Улучшить форматирование кода для соответствия PEP8.
    - Упростить код в функции `add_image_watermark` путем вынесения повторяющихся операций.
    - В функции `add_image_watermark`  использовать более безопасный способ определения режима изображения, возможно, лучше использовать `img.convert('RGBA')` для всех изображений, где это необходимо, вместо `if image_mode == 'RGB'`, так как `P` mode это палетное изображение, в результате чего при преобразовании цвета будут некорректны.

5.  **Пример использования**:
    - Убрать пример использования из файла модуля. Он должен быть в отдельном файле примера, так как модули не должны содержать выполняемого кода при импорте.

**Оптимизированный код**:

```python
"""
Модуль для работы с изображениями
====================================

Этот модуль предоставляет асинхронные функции для загрузки, сохранения и обработки изображений.
Включает в себя функциональность сохранения изображений из URL, сохранения данных изображений в файлы,
получения данных изображений, поиска случайных изображений в директориях, добавления водяных знаков,
изменения размера и преобразования форматов изображений.

Пример использования
----------------------
.. code-block:: python

   from pathlib import Path
   from src.utils.image import process_images_with_watermark

   folder = Path(input("Enter Folder Path: "))
   watermark = Path(input("Enter Watermark Path: "))

   process_images_with_watermark(folder, watermark)
"""

import aiofiles
import aiohttp
import asyncio
import random
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple, Union

from PIL import Image, ImageDraw, ImageFont

from src.logger.logger import logger  # corrected import


class ImageError(Exception):
    """
    Пользовательское исключение для ошибок, связанных с изображениями.

    :param message: Сообщение об ошибке.
    :type message: str
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


async def save_image_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно загружает изображение из URL и сохраняет его локально.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла для сохранения изображения.
    :type filename: Union[str, Path]
    :return: Путь к сохраненному файлу или None, если операция не удалась.
    :rtype: Optional[str]
    :raises ImageError: Если загрузка или сохранение изображения не удались.

    Пример:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...     url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
        ...     file_path = Path("test_image.gif")
        ...     result = await save_image_from_url(url, file_path)
        ...     print(result)
        >>> asyncio.run(main())
        'test_image.gif'
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        logger.error(f"Error downloading image from {image_url}", exc_info=True)
        raise ImageError(f"Failed to download image from {image_url}") from ex

    return await save_image(image_data, filename)


async def save_image(image_data: bytes, file_name: Union[str, Path], format: str = 'PNG') -> Optional[str]:
    """
    Асинхронно сохраняет данные изображения в файл в указанном формате.

    :param image_data: Бинарные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла для сохранения изображения.
    :type file_name: Union[str, Path]
    :param format: Формат сохранения изображения, по умолчанию PNG.
    :type format: str, optional
    :return: Путь к сохраненному файлу или None, если операция не удалась.
    :rtype: Optional[str]
    :raises ImageError: Если файл не может быть создан, сохранен или если сохраненный файл пуст.

    Пример:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...     file_path = Path("test_image.png")
        ...     with open("test_image.png", "rb") as f:
        ...         image_data = f.read()
        ...     result = await save_image(image_data, file_path)
        ...     print(result)
        >>> asyncio.run(main())
        'test_image.png'
    """
    file_path = Path(file_name)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            raise ImageError(f"File {file_path} was not created.")

        img = Image.open(file_path)  #  add handling exceptions
        img.save(file_path, format=format)

        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            raise ImageError(f"File {file_path} saved, but its size is 0 bytes.")

        return str(file_path)

    except Exception as ex:
        logger.critical(f"Failed to save file {file_path}", exc_info=True)
        raise ImageError(f"Failed to save file {file_path}") from ex


def get_image_bytes(image_path: Path, raw: bool = True) -> Optional[Union[BytesIO, bytes]]:
    """
    Читает изображение с помощью Pillow и возвращает его байты в формате JPEG.

    :param image_path: Путь к файлу изображения.
    :type image_path: Path
    :param raw: Если True, возвращает объект BytesIO; иначе возвращает байты. По умолчанию True.
    :type raw: bool, optional
    :return: Байты изображения в формате JPEG или None в случае ошибки.
    :rtype: Optional[Union[BytesIO, bytes]]

    Пример:
        >>> from pathlib import Path
        >>> image_path = Path('test_image.png')
        >>> result = get_image_bytes(image_path)
        >>> print(result)
        <io.BytesIO object at ...>
    """
    try:
        img = Image.open(image_path)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="JPEG")
        return img_byte_arr if raw else img_byte_arr.getvalue()
    except Exception as ex:
        logger.error("Error reading image with Pillow:", exc_info=True)
        return None


def get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Извлекает необработанные бинарные данные файла, если он существует.

    :param file_name: Имя или путь к файлу для чтения.
    :type file_name: Union[str, Path]
    :return: Бинарные данные файла или None, если файл не существует или произошла ошибка.
    :rtype: Optional[bytes]

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('test_image.png')
        >>> result = get_raw_image_data(file_path)
        >>> print(result)
        b'\\x89PNG\\r\\n\\x1a\\n...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        return file_path.read_bytes()
    except Exception as ex:
        logger.error(f"Error reading file {file_path}", exc_info=True)
        return None


def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Рекурсивно ищет случайное изображение в указанной директории.

    :param root_path: Директория для поиска изображений.
    :type root_path: Union[str, Path]
    :return: Путь к случайному изображению или None, если изображения не найдены.
    :rtype: Optional[str]

    Пример:
        >>> from pathlib import Path
        >>> root_path = Path('.')
        >>> result = random_image(root_path)
        >>> print(result)
        './test_image.png'
    """
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [
        file_path
        for file_path in root_path.rglob("*")
        if file_path.is_file() and file_path.suffix.lower() in image_extensions
    ]

    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    return str(random.choice(image_files))


def add_text_watermark(image_path: Union[str, Path], watermark_text: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Добавляет текстовый водяной знак на изображение.

    :param image_path: Путь к файлу изображения.
    :type image_path: Union[str, Path]
    :param watermark_text: Текст для использования в качестве водяного знака.
    :type watermark_text: str
    :param output_path: Путь для сохранения изображения с водяным знаком.
                       По умолчанию перезаписывает исходное изображение.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Путь к изображению с водяным знаком или None в случае ошибки.
    :rtype: Optional[str]

    Пример:
        >>> from pathlib import Path
        >>> image_path = Path('test_image.png')
        >>> watermark_text = 'Watermark'
        >>> result = add_text_watermark(image_path, watermark_text)
        >>> print(result)
        'test_image.png'
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        image = Image.open(image_path).convert("RGBA")
        watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)

        font_size = min(image.size) // 10
        try:
            font = ImageFont.truetype("arial.ttf", size=font_size)
        except IOError:
            font = ImageFont.load_default(size=font_size)
            logger.warning("Font arial.ttf not found; using default font.")

        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path)

        return str(output_path)

    except Exception as ex:
        logger.error(f"Failed to add watermark to {image_path}", exc_info=True)
        return None


def add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]:
    """
    Добавляет водяной знак изображения на другое изображение.

    :param input_image_path: Путь к исходному изображению.
    :type input_image_path: Path
    :param watermark_image_path: Путь к изображению водяного знака.
    :type watermark_image_path: Path
    :param output_image_path: Путь для сохранения изображения с водяным знаком.
           Если не указан, изображение будет сохранено в директории "output".
    :type output_image_path: Optional[Path], optional
    :return: Путь к сохраненному изображению с водяным знаком или None в случае ошибки.
    :rtype: Optional[Path]

    Пример:
        >>> from pathlib import Path
        >>> input_image_path = Path('test_image.png')
        >>> watermark_image_path = Path('test_watermark.png')
        >>> result = add_image_watermark(input_image_path, watermark_image_path)
        >>> print(result)
        'output/test_image.png'
    """
    try:
        base_image = Image.open(input_image_path).convert("RGBA")
        watermark = Image.open(watermark_image_path).convert("RGBA")

        position = base_image.size
        newsize = (int(position[0] * 8 / 100), int(position[0] * 8 / 100))
        watermark = watermark.resize(newsize)
        new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20

        transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))
        transparent.paste(base_image, (0, 0))
        transparent.paste(watermark, new_position, watermark)

        if base_image.mode in ("RGB", "RGBA"):
            transparent = transparent.convert("RGB")
        else:
            transparent = transparent.convert('P')

        if output_image_path is None:
            output_image_path = input_image_path.parent / "output" / input_image_path.name
        output_image_path.parent.mkdir(parents=True, exist_ok=True)
        transparent.save(output_image_path, optimize=True, quality=100)
        logger.info(f"Saving {output_image_path}...")

        return output_image_path

    except Exception as ex:
        logger.error(f"Failed to add watermark to {input_image_path}: {ex}", exc_info=True)
        return None


def resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Изменяет размер изображения до указанных размеров.

    :param image_path: Путь к файлу изображения.
    :type image_path: Union[str, Path]
    :param size: Кортеж с желаемой шириной и высотой изображения.
    :type size: Tuple[int, int]
    :param output_path: Путь для сохранения измененного размера изображения.
           По умолчанию перезаписывает исходное изображение.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Путь к измененному размеру изображения или None в случае ошибки.
    :rtype: Optional[str]

    Пример:
        >>> from pathlib import Path
        >>> image_path = Path('test_image.png')
        >>> size = (100, 100)
        >>> result = resize_image(image_path, size)
        >>> print(result)
        'test_image.png'
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        resized_img = img.resize(size)
        resized_img.save(output_path)
        return str(output_path)

    except Exception as ex:
        logger.error(f"Failed to resize image {image_path}", exc_info=True)
        return None


def convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Преобразует изображение в указанный формат.

    :param image_path: Путь к файлу изображения.
    :type image_path: Union[str, Path]
    :param format: Формат для преобразования изображения (например, "JPEG", "PNG").
    :type format: str
    :param output_path: Путь для сохранения преобразованного изображения.
           По умолчанию перезаписывает исходное изображение.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Путь к преобразованному изображению или None в случае ошибки.
    :rtype: Optional[str]

    Пример:
        >>> from pathlib import Path
        >>> image_path = Path('test_image.png')
        >>> format = 'JPEG'
        >>> result = convert_image(image_path, format)
        >>> print(result)
        'test_image.png'
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        img.save(output_path, format=format)
        return str(output_path)
    except Exception as ex:
        logger.error(f"Failed to convert image {image_path}", exc_info=True)
        return None


def process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None:
    """
    Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в директории "output".

    :param folder_path: Путь к папке, содержащей изображения.
    :type folder_path: Path
    :param watermark_path: Путь к изображению водяного знака.
    :type watermark_path: Path
    """
    if not folder_path.is_dir():
        logger.error(f"Folder {folder_path} does not exist.")
        return

    output_dir = folder_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            output_image_path = output_dir / file_path.name
            add_image_watermark(file_path, watermark_path, output_image_path)