# Анализ кода модуля src.utils.image

**Качество кода: 7/10**
- Плюсы:
    - Код хорошо структурирован и разбит на отдельные функции, каждая из которых выполняет определенную задачу.
    - Используется асинхронное программирование для операций ввода-вывода, что позволяет обрабатывать изображения параллельно.
    - Присутствует обработка ошибок с использованием `try-except` блоков и логирование ошибок с помощью `logger.error`.
    - Есть документация к каждой функции, что облегчает понимание их назначения и использования.
    - Использование Pathlib для работы с путями.
- Минусы:
    - Некоторые docstring не полные и не соответствуют стандарту RST.
    - Избыточное использование try-except блоков, особенно в простых операциях.
    - Некоторые комментарии не дают достаточно информации о коде.
    - Не везде используется форматирование строк f-string.
    - В некоторых местах можно улучшить читаемость кода, например, за счет использования более описательных переменных.

**Рекомендации по улучшению:**

1. **Документация:**
   - Дополнить docstring для функций, методов и переменных в соответствии со стандартами RST (Sphinx).
   - Добавить примеры использования в docstring.

2. **Обработка ошибок:**
   - Избегать избыточного использования `try-except` блоков там, где это не требуется.
   - Использовать `logger.error` с `exc_info=True` для логирования ошибок, включая трассировку.

3. **Форматирование кода:**
   - Использовать f-строки для форматирования строк, где это возможно.
   - Следовать PEP8 в именовании переменных и функций.

4. **Комментарии:**
   - Улучшить комментарии, добавив больше пояснений к логике кода.

5. **Структура:**
    - Перенести код `if __name__ == "__main__":` в отдельную функцию.

6. **Импорты:**
    - Сгруппировать импорты по типу (стандартные, сторонние, локальные).

7. **Использовать `j_loads` или `j_loads_ns`**:
   - В данном модуле нет работы с json, поэтому это не требуется.

**Оптимизированный код:**
```python
"""
Модуль для обработки изображений
=========================================================================================

Этот модуль предоставляет асинхронные функции для загрузки, сохранения и обработки изображений.
Он включает функциональность для сохранения изображений из URL-адресов, сохранения данных изображения в файлы,
получения данных изображения, поиска случайных изображений в каталогах, добавления водяных знаков, изменения размера
и преобразования форматов изображений.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    import asyncio

    async def main():
        image_url = 'https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif'
        file_path = Path('test_image.gif')
        await save_image_from_url(image_url, file_path)

        image_path = Path('test_image.gif')
        watermark_text = 'Watermark'
        watermarked_path = await add_text_watermark(image_path, watermark_text, 'watermarked.gif')
        if watermarked_path:
            print(f'Watermarked image saved to {watermarked_path}')

        folder = Path('./') # текущая папка
        random_image_path = random_image(folder)
        if random_image_path:
            print(f'Random image: {random_image_path}')


        size = (100, 100)
        resized_image_path = await resize_image(image_path, size, 'resized_image.gif')

    if __name__ == "__main__":
        asyncio.run(main())
"""
import aiohttp
import aiofiles
import asyncio
import random
from pathlib import Path
from typing import Optional, Union, Tuple
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

from src.logger.logger import logger


class ImageError(Exception):
    """
    Пользовательское исключение для ошибок, связанных с изображениями.
    """
    pass


async def save_image_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно загружает изображение из URL и сохраняет его локально.

    Args:
        image_url (str): URL-адрес для загрузки изображения.
        filename (Union[str, Path]): Имя файла для сохранения изображения.

    Returns:
        Optional[str]: Путь к сохраненному файлу или None, если операция не удалась.

    Raises:
        ImageError: Если загрузка или сохранение изображения не удались.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()  # Вызывает HTTPError для плохих ответов (4xx или 5xx)
                image_data = await response.read()
    except Exception as ex:
        logger.error(f'Ошибка загрузки изображения из {image_url}', exc_info=True)
        raise ImageError(f'Не удалось загрузить изображение из {image_url}') from ex

    return await save_image(image_data, filename)


async def save_image(image_data: bytes, file_name: Union[str, Path], format: str = 'PNG') -> Optional[str]:
    """
    Асинхронно сохраняет данные изображения в файл в указанном формате.

    Args:
        image_data (bytes): Бинарные данные изображения.
        file_name (Union[str, Path]): Имя файла для сохранения изображения.
        format (str): Формат для сохранения изображения, по умолчанию PNG.

    Returns:
        Optional[str]: Путь к сохраненному файлу или None, если операция не удалась.

    Raises:
        ImageError: Если файл не может быть создан, сохранен или если сохраненный файл пуст.
    """
    file_path = Path(file_name)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Создает родительские каталоги, если они не существуют
        async with aiofiles.open(file_path, 'wb') as file:
            await file.write(image_data)

        if not file_path.exists():
            logger.error(f'Файл {file_path} не был создан.')
            raise ImageError(f'Файл {file_path} не был создан.')

        img = Image.open(file_path)
        img.save(file_path, format=format)

        if file_path.stat().st_size == 0:
            logger.error(f'Файл {file_path} сохранен, но его размер равен 0 байт.')
            raise ImageError(f'Файл {file_path} сохранен, но его размер равен 0 байт.')

        return str(file_path)

    except Exception as ex:
        logger.critical(f'Не удалось сохранить файл {file_path}', exc_info=True)
        raise ImageError(f'Не удалось сохранить файл {file_path}') from ex


def get_image_bytes(image_path: Path, raw: bool = True) -> Optional[Union[BytesIO, bytes]]:
    """
    Читает изображение с использованием Pillow и возвращает его байты в формате JPEG.

    Args:
        image_path (Path): Путь к файлу изображения.
        raw (bool): Если True, возвращает объект BytesIO; в противном случае возвращает байты. По умолчанию True.

    Returns:
        Optional[Union[BytesIO, bytes]]: Байты изображения в формате JPEG или None, если произошла ошибка.
    """
    try:
        img = Image.open(image_path)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return img_byte_arr if raw else img_byte_arr.getvalue()
    except Exception as ex:
        logger.error('Ошибка чтения изображения с помощью Pillow:', exc_info=True)
        return None


def get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Возвращает необработанные двоичные данные файла, если он существует.

    Args:
        file_name (Union[str, Path]): Имя или путь к файлу для чтения.

    Returns:
        Optional[bytes]: Двоичные данные файла или None, если файл не существует или произошла ошибка.
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f'Файл {file_path} не существует.')
        return None

    try:
        return file_path.read_bytes()
    except Exception as ex:
        logger.error(f'Ошибка чтения файла {file_path}', exc_info=True)
        return None


def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Рекурсивно ищет случайное изображение в указанном каталоге.

    Args:
        root_path (Union[str, Path]): Каталог для поиска изображений.

    Returns:
        Optional[str]: Путь к случайному изображению или None, если изображения не найдены.
    """
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [file_path for file_path in root_path.rglob('*')
                   if file_path.is_file() and file_path.suffix.lower() in image_extensions]

    if not image_files:
        logger.warning(f'Изображения не найдены в {root_path}.')
        return None

    return str(random.choice(image_files))


def add_text_watermark(image_path: Union[str, Path], watermark_text: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Добавляет текстовый водяной знак на изображение.

    Args:
        image_path (Union[str, Path]): Путь к файлу изображения.
        watermark_text (str): Текст для использования в качестве водяного знака.
        output_path (Optional[Union[str, Path]]): Путь для сохранения изображения с водяным знаком.
            По умолчанию перезаписывает исходное изображение.

    Returns:
        Optional[str]: Путь к изображению с водяным знаком или None при ошибке.
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        image = Image.open(image_path).convert('RGBA')

        # Создаем прозрачный слой для водяного знака
        watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)

        font_size = min(image.size) // 10  # Размер шрифта в зависимости от размера изображения
        try:
            font = ImageFont.truetype('arial.ttf', size=font_size)
        except IOError:
            font = ImageFont.load_default(size=font_size)
            logger.warning('Шрифт arial.ttf не найден; используется шрифт по умолчанию.')

        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        # Рисуем текст на прозрачном слое
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Объединяем изображение и водяной знак
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path)

        return str(output_path)

    except Exception as ex:
        logger.error(f'Не удалось добавить водяной знак к {image_path}', exc_info=True)
        return None


def add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]:
    """
    Добавляет водяной знак на изображение и сохраняет результат по указанному пути вывода.

    Args:
        input_image_path (Path): Путь к исходному изображению.
        watermark_image_path (Path): Путь к изображению водяного знака.
        output_image_path (Optional[Path]): Путь для сохранения изображения с водяным знаком.
            Если не указан, изображение будет сохранено в каталоге "output".

    Returns:
        Optional[Path]: Путь к сохраненному изображению с водяным знаком или None, если операция не удалась.
    """
    try:
        # Открывает исходное изображение
        base_image = Image.open(input_image_path)

        # Открывает изображение водяного знака и конвертируем его в RGBA
        watermark = Image.open(watermark_image_path).convert('RGBA')

        # Устанавливает размер водяного знака (8% от ширины исходного изображения)
        position = base_image.size  # Размер исходного изображения (ширина, высота)
        newsize = (int(position[0] * 8 / 100), int(position[0] * 8 / 100))  # Новый размер водяного знака
        watermark = watermark.resize(newsize)  # Изменяет размер водяного знака

        # Определяет позицию для размещения водяного знака (нижний правый угол с отступом 20px)
        new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20

        # Создает новый прозрачный слой для объединения изображений
        transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))

        # Вставляет исходное изображение на новый слой
        transparent.paste(base_image, (0, 0))

        # Вставляет водяной знак поверх исходного изображения
        transparent.paste(watermark, new_position, watermark)

        # Проверяет режим изображения и конвертирует прозрачный слой в исходный режим
        image_mode = base_image.mode
        if image_mode == 'RGB':
            transparent = transparent.convert(image_mode)  # Конвертируем в RGB
        else:
            transparent = transparent.convert('P')  # Конвертируем в палитру

        # Сохраняет конечное изображение в указанный путь с оптимизированным качеством
        if output_image_path is None:
            output_image_path = input_image_path.parent / 'output' / input_image_path.name
        output_image_path.parent.mkdir(parents=True, exist_ok=True)  # Создает выходной каталог, если он не существует
        transparent.save(output_image_path, optimize=True, quality=100)
        logger.info(f'Сохранение {output_image_path}...')

        return output_image_path

    except Exception as ex:
        logger.error(f'Не удалось добавить водяной знак к {input_image_path}: {ex}', exc_info=True)
        return None


def resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Изменяет размер изображения до указанных размеров.

    Args:
        image_path (Union[str, Path]): Путь к файлу изображения.
        size (Tuple[int, int]): Кортеж, содержащий желаемую ширину и высоту изображения.
        output_path (Optional[Union[str, Path]]): Путь для сохранения изображения измененного размера.
            По умолчанию перезаписывает исходное изображение.

    Returns:
        Optional[str]: Путь к изображению измененного размера или None при ошибке.
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        resized_img = img.resize(size)
        resized_img.save(output_path)
        return str(output_path)

    except Exception as ex:
        logger.error(f'Не удалось изменить размер изображения {image_path}', exc_info=True)
        return None


def convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Преобразует изображение в указанный формат.

    Args:
        image_path (Union[str, Path]): Путь к файлу изображения.
        format (str): Формат для преобразования изображения (например, "JPEG", "PNG").
        output_path (Optional[Union[str, Path]]): Путь для сохранения преобразованного изображения.
            По умолчанию перезаписывает исходное изображение.

    Returns:
        Optional[str]: Путь к преобразованному изображению или None при ошибке.
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        img.save(output_path, format=format)
        return str(output_path)
    except Exception as ex:
        logger.error(f'Не удалось преобразовать изображение {image_path}', exc_info=True)
        return None


def process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None:
    """
    Обрабатывает все изображения в указанной папке, добавляя водяной знак и сохраняя их в каталоге "output".

    Args:
        folder_path (Path): Путь к папке, содержащей изображения.
        watermark_path (Path): Путь к изображению водяного знака.
    """
    if not folder_path.is_dir():
        logger.error(f'Папка {folder_path} не существует.')
        return

    # Создаем каталог "output", если он не существует
    output_dir = folder_path / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Обрабатываем каждый файл в папке
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            output_image_path = output_dir / file_path.name
            add_image_watermark(file_path, watermark_path, output_image_path)


def main():
    """
    Функция для запуска обработки изображений из командной строки.
    """
    folder = Path(input('Введите путь к папке: '))  # Путь к папке с изображениями
    watermark = Path(input('Введите путь к изображению водяного знака: '))  # Путь к изображению водяного знака

    process_images_with_watermark(folder, watermark)


if __name__ == '__main__':
    main()