# Анализ кода модуля `image.py`

**Качество кода**
10
-   Плюсы
    -   Код хорошо структурирован и документирован в формате Markdown.
    -   Предоставляет основные функции для работы с изображениями: загрузка, сохранение, чтение и поиск.
    -   Включает примеры использования и установки, что облегчает интеграцию в другие проекты.
    -   Использует асинхронность для операций, связанных с сетью и файлами.
    -   Использует `Path` для гибкости при работе с путями.
-   Минусы
    -   Отсутствует документация в формате reStructuredText для функций и модуля.
    -   Нет обработки исключений с использованием `logger.error`.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Не хватает импортов необходимых модулей.

**Рекомендации по улучшению**

1.  Преобразовать Markdown документацию в reStructuredText (RST).
2.  Добавить docstring к каждой функции в формате RST.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Добавить обработку исключений с использованием `logger.error` вместо стандартных `try-except`.
5.  Добавить необходимые импорты.
6.  Использовать `j_loads` или `j_loads_ns` при работе с JSON файлами, если это требуется, но в данном случае это не требуется.
7.  Переписать комментарии после `#` в соответствии с инструкциями.

**Оптимизированный код**

```python
"""
Модуль для работы с изображениями.
=========================================================================================

Этот модуль предоставляет утилиты для асинхронной загрузки, сохранения, чтения и поиска
случайных изображений. Он предназначен для использования в проектах, где требуется
обработка изображений.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image

    async def main():
        await save_png_from_url("https://example.com/image.png", "local_image.png")

        with open("example_image.png", "rb") as f:
            image_data = f.read()
        await save_png(image_data, "saved_image.png")

        data = get_image_data("saved_image.png")
        print(data)

        random_image_path = random_image("path/to/images")
        if random_image_path:
            print(f"Случайное изображение: {random_image_path}")
        else:
            print("Изображений не найдено.")

    if __name__ == "__main__":
        asyncio.run(main())
"""
import asyncio
from pathlib import Path
import aiohttp
import aiofiles
import os
import random
from PIL import Image
from src.logger.logger import logger

async def save_png_from_url(image_url: str, filename: str | Path) -> str | None:
    """
    Асинхронно загружает изображение по указанному URL и сохраняет его локально в формате PNG.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла или путь, куда сохранить изображение.
    :type filename: str | Path
    :return: Путь к сохранённому файлу или None, если операция завершилась неудачно.
    :rtype: str | None
    """
    try:
        # Код исполняет отправку HTTP-запроса для получения данных изображения
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
        # Код сохраняет полученные данные изображения в PNG файл
        return await save_png(image_data, filename)
    except aiohttp.ClientError as e:
        logger.error(f'Ошибка загрузки изображения по URL: {image_url}', exc_info=True)
        return None
    except Exception as e:
         logger.error(f'Неизвестная ошибка при загрузке изображения: {e}', exc_info=True)
         return None

async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """
    Асинхронно сохраняет переданные данные изображения в формате PNG.

    :param image_data: Двоичные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла или путь, куда сохранить изображение.
    :type file_name: str | Path
    :return: Путь к сохранённому файлу или None, если операция завершилась неудачно.
    :rtype: str | None
    """
    try:
        # Код исполняет запись данных изображения в файл
        async with aiofiles.open(file_name, 'wb') as f:
            await f.write(image_data)
        return str(file_name)
    except Exception as e:
        logger.error(f'Ошибка сохранения изображения в файл: {file_name}', exc_info=True)
        return None


def get_image_data(file_name: str | Path) -> bytes | None:
    """
    Синхронно считывает двоичные данные изображения из указанного файла.

    :param file_name: Имя файла или путь к изображению.
    :type file_name: str | Path
    :return: Двоичные данные изображения или None, если файл не найден или произошла ошибка.
    :rtype: bytes | None
    """
    try:
        # Код исполняет чтение данных изображения из файла
        with open(file_name, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_name}', exc_info=True)
        return None
    except Exception as e:
         logger.error(f'Неизвестная ошибка при чтении изображения: {e}', exc_info=True)
         return None


def random_image(root_path: str | Path) -> str | None:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает путь к нему.

    :param root_path: Директория для поиска изображений.
    :type root_path: str | Path
    :return: Путь к случайному изображению или None, если изображений не найдено.
    :rtype: str | None
    """
    images = []
    # Код исполняет рекурсивный поиск файлов изображений
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                 images.append(os.path.join(root, file))
    # Код исполняет выбор случайного изображения из списка
    if images:
        return random.choice(images)
    else:
         logger.error(f'Изображения не найдены в директории: {root_path}')
         return None
```