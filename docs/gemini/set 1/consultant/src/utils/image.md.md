# Анализ кода модуля `image.py`

**Качество кода**
8
- Плюсы
    -  Хорошее описание модуля и его функций.
    -  Примеры использования функций.
    -  Инструкции по установке и использованию.
    -  Описание логирования, лицензии и автора.
- Минусы
    - Отсутствуют docstring в коде.
    -  Не используются асинхронные операции там где это возможно.
    -  Не все импорты добавлены в код.
    -  Не везде используется `logger.error` для обработки ошибок.

**Рекомендации по улучшению**

1.  Добавить docstring к модулю, функциям и переменным в формате reStructuredText (RST).
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error`.
4.  Добавить необходимые импорты.
5.  Использовать асинхронность там где это возможно.
6.  Избегать избыточного использования `try-except` блоков.

**Оптимизированный код**
```python
"""
Модуль для работы с изображениями.
=========================================================================================

Этот модуль предоставляет утилиты для асинхронной загрузки, сохранения, чтения и поиска случайных изображений.
Модуль предназначен для использования в проектах, где требуется обработка изображений, такая как загрузка изображений из URL-адресов,
сохранение их в локальное хранилище и рекурсивный поиск случайных изображений в указанном каталоге.

Пример использования
--------------------

Пример использования функции `save_png_from_url`:

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.image import save_png_from_url

    async def main():
        await save_png_from_url("https://example.com/image.png", Path("local_image.png"))

    if __name__ == "__main__":
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

from src.logger.logger import logger

async def save_png_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно загружает изображение из указанного URL и сохраняет его локально в формате PNG.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла или путь, куда будет сохранено изображение.
    :type filename: Union[str, Path]
    :return: Путь к сохраненному файлу или None в случае ошибки.
    :rtype: Optional[str]

    :Example:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...     await save_png_from_url("https://example.com/image.png", Path("local_image.png"))
        ...
        >>> asyncio.run(main())
    """
    try:
        # Код выполняет асинхронную загрузку изображения по URL
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
        # Код вызывает функцию save_png для сохранения загруженного изображения
        return await save_png(image_data, filename)
    except aiohttp.ClientError as e:
        logger.error(f'Ошибка при загрузке изображения по URL: {image_url}', exc_info=True)
        return None
    except Exception as e:
        logger.error(f'Неизвестная ошибка при загрузке и сохранении изображения по URL: {image_url}', exc_info=True)
        return None

async def save_png(image_data: bytes, file_name: Union[str, Path]) -> Optional[str]:
    """
    Асинхронно сохраняет предоставленные двоичные данные изображения в формате PNG.

    :param image_data: Двоичные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла или путь, куда будет сохранено изображение.
    :type file_name: Union[str, Path]
    :return: Путь к сохраненному файлу или None в случае ошибки.
    :rtype: Optional[str]

    :Example:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...     with open("example_image.png", "rb") as f:
        ...         image_data = f.read()
        ...     await save_png(image_data, Path("saved_image.png"))
        ...
        >>> asyncio.run(main())
    """
    try:
        # Код выполняет открытие файла в асинхронном режиме для записи
        async with aiofiles.open(file_name, "wb") as f:
            # Код выполняет асинхронную запись данных изображения в файл
            await f.write(image_data)
        return str(file_name)
    except Exception as e:
        logger.error(f'Ошибка при сохранении изображения в файл: {file_name}', exc_info=True)
        return None

def get_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Синхронно считывает двоичные данные изображения из указанного файла.

    :param file_name: Имя файла или путь к изображению.
    :type file_name: Union[str, Path]
    :return: Двоичные данные изображения или None, если файл не найден или произошла ошибка.
    :rtype: Optional[bytes]

    :Example:
        >>> data = get_image_data("saved_image.png")
        >>> print(data)
        b'\\x89PNG\\r\\n...'
    """
    try:
        # Код выполняет открытие файла в режиме чтения двоичных данных
        with open(file_name, "rb") as f:
            # Код выполняет чтение данных изображения из файла
            return f.read()
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_name}', exc_info=True)
        return None
    except Exception as e:
        logger.error(f'Ошибка при чтении данных изображения из файла: {file_name}', exc_info=True)
        return None

def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Рекурсивно ищет случайное изображение в указанном каталоге и возвращает его путь.

    :param root_path: Путь к каталогу для поиска изображений.
    :type root_path: Union[str, Path]
    :return: Путь к случайному изображению или None, если изображения не найдены.
    :rtype: Optional[str]

    :Example:
        >>> random_image_path = random_image("path/to/images")
        >>> if random_image_path:
        ...     print(f"Случайное изображение: {random_image_path}")
        ... else:
        ...     print("Изображения не найдены.")
    """
    images = []
    # Код выполняет преобразование пути к типу Path
    root_path = Path(root_path)
    # Код выполняет обход директории рекурсивно
    for root, _, files in os.walk(root_path):
        for file in files:
            # Код проверяет расширение файла и добавляет в список если файл картинка
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                images.append(Path(root) / file)
    # Код выполняет выбор случайного изображения из списка
    if images:
        return str(random.choice(images))
    else:
         logger.error(f'Изображения не найдены в каталоге: {root_path}', exc_info=True)
         return None
```