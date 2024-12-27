# Анализ кода модуля `image.py`

**Качество кода**
9
-  Плюсы
    -   Код хорошо документирован с примерами использования.
    -   Функции асинхронны там, где это необходимо.
    -   Используются Pathlib для работы с путями.
    -   Есть обработка ошибок и логирование.
-  Минусы
    -   Нет проверки типа для `image_data` в функции `save_png`.
    -   Не все комментарии в формате reStructuredText.
    -   Используется `try-except` без конкретизации исключений в `save_png_from_url` и `get_image_data`.
    -   Не используются `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**
1.  Добавить проверку типа для `image_data` в `save_png` и использовать `logger.error` для обработки ошибок.
2.  Переписать все комментарии в формате reStructuredText.
3.  Использовать более конкретные исключения и `logger.error` для обработки ошибок.
4.  Заменить `json.load` на `j_loads` или `j_loads_ns`, если это уместно.
5.  Добавить docstring к модулю, функциям и методам в стиле reStructuredText.
6.  Добавить импорты которые используются в коде.

**Оптимизированный код**

```python
"""
Модуль для работы с изображениями.
=========================================================================================

Этот модуль предоставляет утилиты для асинхронной загрузки, сохранения, чтения и поиска случайных изображений.
Он предназначен для использования в проектах, где требуется обработка изображений, например, загрузка изображений из URL,
сохранение их в локальное хранилище и рекурсивный поиск случайных изображений в указанном каталоге.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    import asyncio
    from pathlib import Path

    async def main():
        # Загрузка изображения из URL
        await save_png_from_url('https://example.com/image.png', 'local_image.png')

        # Сохранение изображения из байтов
        with open('example_image.png', 'rb') as f:
            image_data = f.read()
        await save_png(image_data, 'saved_image.png')

        # Чтение данных изображения
        data = get_image_data('saved_image.png')
        print(data)

        # Поиск случайного изображения
        random_image_path = random_image('path/to/images')
        if random_image_path:
            print(f'Случайное изображение: {random_image_path}')
        else:
            print('Изображения не найдены.')

    if __name__ == '__main__':
        asyncio.run(main())

"""
import asyncio
import os
import random
from pathlib import Path
from typing import Optional, Union

import aiofiles
import aiohttp
from PIL import Image

from src.logger.logger import logger #  Импортируем logger


async def save_png_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно загружает изображение из URL и сохраняет его локально в формате PNG.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла или путь, куда будет сохранено изображение.
    :type filename: Union[str, Path]
    :return: Путь к сохраненному файлу или None, если операция не удалась.
    :rtype: Optional[str]
    """
    try:
        # Код исполняет загрузку изображения по URL
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except aiohttp.ClientError as e:
         # Код логирует ошибку загрузки изображения
        logger.error(f'Ошибка загрузки изображения из {image_url}: {e}')
        return None
    
    # Код исполняет сохранение изображения
    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно сохраняет предоставленные данные изображения в формате PNG.

    :param image_data: Бинарные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла или путь, куда будет сохранено изображение.
    :type file_name: Union[str, Path]
    :return: Путь к сохраненному файлу или None, если операция не удалась.
    :rtype: Optional[str]
    """
    # Проверка типа данных изображения
    if not isinstance(image_data, bytes):
        logger.error(f'Неверный тип данных изображения: {type(image_data)}. Ожидался тип bytes.')
        return None
    try:
         # Код исполняет открытие файла для записи
        async with aiofiles.open(file_name, 'wb') as f:
            # Код исполняет запись данных изображения в файл
            await f.write(image_data)
        return str(Path(file_name).resolve())
    except (OSError, IOError) as e:
        # Код логирует ошибку при сохранении файла
        logger.error(f'Ошибка сохранения файла изображения {file_name}: {e}')
        return None


def get_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Синхронно читает бинарные данные изображения из указанного файла.

    :param file_name: Имя файла или путь к изображению.
    :type file_name: Union[str, Path]
    :return: Бинарные данные изображения или None, если файл не найден или произошла ошибка.
    :rtype: Optional[bytes]
    """
    try:
        # Код исполняет открытие файла для чтения
        with open(file_name, 'rb') as f:
            # Код исполняет чтение данных изображения из файла
            image_data = f.read()
        return image_data
    except FileNotFoundError:
        # Код логирует ошибку, если файл не найден
        logger.error(f'Файл изображения не найден: {file_name}')
        return None
    except (OSError, IOError) as e:
        # Код логирует ошибку при чтении файла
        logger.error(f'Ошибка чтения файла изображения {file_name}: {e}')
        return None


def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Рекурсивно ищет случайное изображение в указанном каталоге и возвращает его путь.

    :param root_path: Каталог для поиска изображений.
    :type root_path: Union[str, Path]
    :return: Путь к случайному изображению или None, если изображения не найдены.
    :rtype: Optional[str]
    """
    image_files = []
    # Код обходит все файлы и каталоги в заданном пути
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Код добавляет путь к изображению в список
                image_files.append(os.path.join(root, file))

    # Если изображения не найдены, возвращает None
    if not image_files:
        logger.debug(f'В каталоге {root_path} не найдено изображений.')
        return None
    # Код выбирает и возвращает случайное изображение
    return random.choice(image_files)
```