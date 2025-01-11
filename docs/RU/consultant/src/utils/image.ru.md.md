# Анализ кода модуля `image.ru.md`

**Качество кода**
8
-  Плюсы
    - Код хорошо документирован, с подробным описанием каждой функции, примерами использования и инструкциями по установке.
    - Используются асинхронные операции для загрузки и сохранения изображений, что повышает производительность.
    - Есть разделение на логические блоки с описаниями и примерами.
-  Минусы
    - Отсутствуют импорты в коде.
    - Комментарии не соответствуют формату reStructuredText (RST).
    - Нет обработки ошибок с помощью `logger.error`.
    - Используются избыточные `try-except` блоки.
    - Нет интеграции с `src.utils.jjson`.
    - Не используются константы для путей и форматов.
    - Повторяются примеры в разных разделах.

**Рекомендации по улучшению**

1.  Добавить необходимые импорты в начале модуля, такие как `os`, `random`, `aiohttp`, `aiofiles` и `Path` из `pathlib`, а также `logger` из `src.logger.logger`.
2.  Переписать все комментарии в формате reStructuredText (RST).
3.  Использовать `logger.error` вместо `print` для логирования ошибок и обрабатывать исключения более аккуратно.
4.  Избавиться от избыточных блоков `try-except`, если это не требуется для обработки специфических исключений.
5.  Добавить обработку исключений при открытии и чтении файлов.
6.  Не использовать `asyncio.run` в примерах внутри файла, лучше предоставить примеры без запуска `asyncio`.
7.  Использовать константы для путей и форматов файлов, если они используются несколько раз.
8.  Убрать повторения примеров в разных разделах и оставить их только в разделе "Примеры использования".
9.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов конфигурации, если это необходимо.
10. Заменить старые комментарии в формате `#` на новые в формате RST.

**Оптимизированный код**

```python
"""
Модуль для работы с изображениями.
=====================================

Модуль ``image`` предоставляет утилиты для асинхронной загрузки, сохранения,
чтения и поиска случайных изображений.
Он предназначен для использования в проектах, где требуется обработка
изображений, таких как загрузка изображений по URL, сохранение их в
локальное хранилище, а также рекурсивный поиск случайных изображений в
указанной директории.

Пример использования
--------------------

.. code-block:: python

    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image
    import asyncio
    from pathlib import Path


    async def main():
        # Пример сохранения изображения по URL
        image_url = "https://example.com/image.png"
        local_image_path = Path("local_image.png")
        await save_png_from_url(image_url, local_image_path)

        # Пример сохранения изображения из данных
        image_data = b'\\x89PNG\\r\\n...'  # Замените на реальные данные
        saved_image_path = Path("saved_image.png")
        await save_png(image_data, saved_image_path)

        # Пример чтения данных изображения
        image_data = get_image_data(saved_image_path)
        print(image_data)

        # Пример поиска случайного изображения
        random_image_path = random_image(Path("path/to/images"))
        if random_image_path:
            print(f"Случайное изображение: {random_image_path}")
        else:
             print("Изображения не найдено.")
    asyncio.run(main())
"""
import os
import random
from pathlib import Path
from typing import Optional
import aiohttp
import aiofiles
from src.logger.logger import logger

# from src.utils.jjson import j_loads, j_loads_ns # TODO add in feature if need

IMAGE_FORMAT = ".png"
"""Константа для формата изображения."""


async def save_png_from_url(image_url: str, filename: str | Path) -> Optional[str]:
    """
    Асинхронно загружает изображение по указанному URL и сохраняет его локально в формате PNG.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла или путь, куда сохранить изображение.
    :type filename: str | Path
    :return: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.
    :rtype: Optional[str]
    """
    try:
        # код исполняет запрос на получение изображения
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
        return await save_png(image_data, filename)
    except aiohttp.ClientError as ex:
        logger.error(f"Ошибка при загрузке изображения с {image_url}: {ex}")
        return None
    except Exception as ex:
        logger.error(f"Неизвестная ошибка при загрузке изображения с {image_url}: {ex}")
        return None


async def save_png(image_data: bytes, file_name: str | Path) -> Optional[str]:
    """
    Асинхронно сохраняет переданные данные изображения в формате PNG.

    :param image_data: Двоичные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла или путь, куда сохранить изображение.
    :type file_name: str | Path
    :return: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.
    :rtype: Optional[str]
    """
    try:
        # код исполняет сохранение изображения
        async with aiofiles.open(file_name, "wb") as f:
            await f.write(image_data)
        return str(file_name)
    except Exception as ex:
        logger.error(f"Ошибка при сохранении изображения в {file_name}: {ex}")
        return None


def get_image_data(file_name: str | Path) -> Optional[bytes]:
    """
    Синхронно считывает двоичные данные изображения из указанного файла.

    :param file_name: Имя файла или путь к изображению.
    :type file_name: str | Path
    :return: Двоичные данные изображения или `None`, если файл не найден или произошла ошибка.
    :rtype: Optional[bytes]
    """
    try:
        # код исполняет чтение данных из файла
        with open(file_name, "rb") as f:
            image_data = f.read()
        return image_data
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_name}")
        return None
    except Exception as ex:
        logger.error(f"Ошибка при чтении файла {file_name}: {ex}")
        return None


def random_image(root_path: str | Path) -> Optional[str]:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает путь к нему.

    :param root_path: Директория для поиска изображений.
    :type root_path: str | Path
    :return: Путь к случайному изображению или `None`, если изображений не найдено.
    :rtype: Optional[str]
    """
    image_files = []
    try:
        # код исполняет обход директории в поисках изображений
        for root, _, files in os.walk(root_path):
            for file in files:
                if file.lower().endswith(IMAGE_FORMAT):
                    image_files.append(os.path.join(root, file))

        if image_files:
            # код исполняет выбор случайного файла из списка
            return random.choice(image_files)
        else:
            logger.warning(f"Изображения не найдены в {root_path}")
            return None
    except Exception as ex:
         logger.error(f"Ошибка при поиске изображения в {root_path}: {ex}")
         return None
```