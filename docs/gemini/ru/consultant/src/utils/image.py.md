# Анализ кода модуля `image.py`

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован и разбит на логические функции.
    -  Используется асинхронное программирование для операций ввода-вывода, что хорошо для производительности.
    -  Присутствует логирование ошибок с использованием `logger`.
    -  Используются `Path` для работы с путями, что улучшает кроссплатформенность.
    -  Есть примеры использования в docstring.
-  Минусы
    -  Некоторые проверки избыточны (например, проверка размера файла после сохранения).
    -  Смешивание проверок и обработки ошибок внутри одного блока `try`.
    -  В функции `save_png` повторно открывается и сохраняется изображение.
    -  Отсутствуют комментарии в коде, объясняющие конкретные действия.
    -  В `random_image` не обрабатывается исключение `OSError` или `PermissionError`, которые могут возникнуть во время поиска файлов.

**Рекомендации по улучшению**

1.  **Улучшение обработки ошибок:** Вместо общего `try-except` блока, стоит использовать более специфичные блоки для обработки разных исключений.  Использовать `logger.exception` для записи ошибки с трассировкой.
2.  **Избегание повторной обработки изображения:** В функции `save_png` можно избежать повторного открытия и сохранения изображения, поскольку изображение уже сохранено на диск.  Можно просто проверить что файл существует и не пустой.
3.  **Добавление комментариев:** Добавить комментарии в формате RST для каждой функции, метода, класса и важных участков кода.
4.  **Проверка размера файла:** Проверка размера файла после сохранения изображения избыточна, так как размер файла уже проверен сразу после записи.
5.  **Обработка исключений в `random_image`:** Добавить обработку исключений `OSError` или `PermissionError` в цикле `rglob`, которые могут возникнуть при доступе к файловой системе.
6.  **Удаление неиспользуемых импортов:** Удалить импорт `printer`.
7.  **Использование `f-string`:** Использовать `f-string` для форматирования строк, когда это возможно.

**Оптимизированный код**

```python
"""
Модуль для работы с изображениями.
=========================================================================================

Этот модуль предоставляет асинхронные функции для загрузки, сохранения и получения данных изображений.

Функции:
    - :func:`save_png_from_url`
    - :func:`save_png`
    - :func:`get_image_data`
    - :func:`random_image`

Пример использования
--------------------

Пример сохранения изображения по URL:

.. code-block:: python

    asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))

Пример сохранения изображения из байтов:

.. code-block:: python

    with open("example_image.png", "rb") as f:
        image_data = f.read()
    asyncio.run(save_png(image_data, "saved_image.png"))

Пример получения данных изображения:

.. code-block:: python

    get_image_data("saved_image.png")

Пример получения случайного изображения:

.. code-block:: python

    random_image("path/to/images")

"""
MODE = 'dev'
import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
import random
from src.logger.logger import logger

async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """
    Загружает изображение по URL и сохраняет его локально асинхронно.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла для сохранения изображения.
    :type filename: str | Path
    :return: Путь к сохраненному файлу или ``None`` в случае ошибки.
    :rtype: str | None

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        #  Код устанавливает асинхронную сессию
        async with aiohttp.ClientSession() as session:
             # Код отправляет GET запрос по URL
            async with session.get(image_url) as response:
                response.raise_for_status()
                # Код читает содержимое ответа
                image_data = await response.read()
    except aiohttp.ClientError as ex:
        # Код логирует ошибку загрузки изображения
        logger.error(f"Ошибка загрузки изображения по URL: {image_url}", exc_info=True)
        return None
    # Код вызывает асинхронную функцию сохранения изображения
    return await save_png(image_data, filename)

async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """
    Сохраняет изображение в формате PNG асинхронно.

    :param image_data: Бинарные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла для сохранения изображения.
    :type file_name: str | Path
    :return: Путь к сохраненному файлу или ``None`` в случае ошибки.
    :rtype: str | None

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    file_path = Path(file_name)
    try:
        # Код создает необходимые родительские директории
        file_path.parent.mkdir(parents=True, exist_ok=True)
        #  Код открывает файл для записи
        async with aiofiles.open(file_path, "wb") as file:
             # Код асинхронно записывает бинарные данные в файл
            await file.write(image_data)
        # Код открывает изображение с помощью Pillow
        image = Image.open(file_path)
         # Код сохраняет изображение в формате PNG
        image.save(file_path, "PNG")
         # Код проверяет, создан ли файл и не пустой ли он
        if not file_path.exists() or file_path.stat().st_size == 0:
            logger.error(f"Файл {file_path} не был создан или имеет нулевой размер.")
            return None
    except (OSError, ValueError) as ex:
        # Код логирует ошибку, если не удалось сохранить файл
        logger.error(f"Не удалось сохранить файл {file_path}", exc_info=True)
        return None

    return str(file_path)

def get_image_data(file_name: str | Path) -> bytes | None:
    """
    Извлекает бинарные данные файла, если он существует.

    :param file_name: Имя файла для чтения.
    :type file_name: str | Path
    :return: Бинарные данные файла или ``None`` если файл не найден или произошла ошибка.
    :rtype: bytes | None

    :example:
        >>> get_image_data("saved_image.png")
        b'\\x89PNG\\r\\n...'
    """
    file_path = Path(file_name)
    # Код проверяет, существует ли файл
    if not file_path.exists():
        logger.error(f"Файл {file_path} не существует.")
        return None
    try:
        # Код открывает файл для чтения в бинарном режиме
        with open(file_path, "rb") as file:
             # Код возвращает содержимое файла
            return file.read()
    except OSError as ex:
         # Код логирует ошибку, если не удалось прочитать файл
        logger.error(f"Ошибка чтения файла {file_path}", exc_info=True)
        return None

def random_image(root_path: str | Path) -> str | None:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает его путь.

    :param root_path: Директория для поиска изображений.
    :type root_path: str | Path
    :return: Путь к случайному изображению или ``None`` если изображения не найдены.
    :rtype: str | None

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
    """
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = []
    # Код рекурсивно обходит все файлы в указанной директории
    for file_path in root_path.rglob("*"):
        try:
             # Код проверяет является ли путь файлом, и имеет ли он одно из поддерживаемых расширений
            if file_path.is_file() and file_path.suffix.lower() in image_extensions:
                image_files.append(file_path)
        except (OSError, PermissionError) as ex:
           # Код логирует ошибку если не удалось получить доступ к файлу или директории
            logger.error(f"Ошибка доступа к файлу или директории: {file_path}", exc_info=True)
            continue
    # Код проверяет, найдены ли изображения
    if not image_files:
        logger.warning(f"Изображения не найдены в {root_path}.")
        return None
    # Код возвращает путь к случайному изображению
    return str(random.choice(image_files))