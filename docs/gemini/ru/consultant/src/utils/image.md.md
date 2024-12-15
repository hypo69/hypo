# Анализ кода модуля `image.py`

**Качество кода**
**7**
-  Плюсы
    -  Хорошая и подробная документация в формате Markdown.
    -  Код предоставляет основные функции для работы с изображениями.
    -  Примеры использования функций для каждой функции.
    -  Присутствуют описания установки и использования модуля.
    -  Упоминание о логировании.
-  Минусы
    -  Отсутствует сам код модуля `image.py`.
    -  Не используется reStructuredText (RST) для документации.
    -  Нет подробной информации по обработке ошибок.
    -  Нет информации о зависимостях в начале модуля, также нет импортов.
    -  Нет документации для всех параметров и возвращаемых значений функций в формате reStructuredText.
    -  Нет обработки возможных исключений внутри функций.

**Рекомендации по улучшению**

1.  **Преобразование документации в RST**:
    -  Заменить Markdown на reStructuredText (RST).
    -  Добавить docstring к функциям.
    -  Включить документацию по параметрам и возвращаемым значениям в формате RST.
2.  **Добавить импорты**:
    - Добавить необходимые импорты в начало файла.
3.  **Обработка ошибок**:
    -  Использовать `try-except` блоки с `logger.error` для обработки ошибок.
    -  Удалить `...` и заменить на конкретную логику.
4.  **Документирование модуля**:
    -  Добавить подробное описание модуля в начале файла в формате RST.
    -  Добавить информацию о зависимостях в начало модуля.
5.  **Обновление примеров**:
    -  Привести примеры использования в соответствие с новым форматом документации RST.

**Оптимизированный код**

```python
"""
Модуль для работы с изображениями
=========================================================================================

Этот модуль предоставляет утилиты для асинхронной загрузки, сохранения, чтения и поиска случайных изображений.
Предназначен для проектов, требующих обработки изображений, таких как загрузка изображений из URL-адресов, их сохранение
в локальное хранилище и рекурсивный поиск случайных изображений в указанном каталоге.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image
    import asyncio

    async def main():
        # Загрузка изображения из URL и сохранение
        await save_png_from_url("https://example.com/image.png", "local_image.png")

        # Чтение данных из файла
        data = get_image_data("local_image.png")
        print(data)

        # Поиск случайного изображения
        random_image_path = random_image("path/to/images")
        if random_image_path:
            print(f"Случайное изображение: {random_image_path}")
        else:
            print("Изображения не найдены.")

    if __name__ == "__main__":
        asyncio.run(main())
"""
import asyncio
from pathlib import Path
from typing import Union
import aiohttp
import aiofiles
import os
import random
from src.logger.logger import logger # импортируем logger


async def save_png_from_url(image_url: str, filename: Union[str, Path]) -> Union[str, None]:
    """
    Асинхронно загружает изображение из указанного URL и сохраняет его локально в формате PNG.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла или путь, куда будет сохранено изображение.
    :type filename: Union[str, Path]
    :return: Путь к сохраненному файлу или None в случае неудачи.
    :rtype: Union[str, None]
    
    :raises aiohttp.ClientError: If there is an error with the aiohttp client.
    :raises Exception: If any other error occurs during the process.

    Пример:
    
    .. code-block:: python
    
        import asyncio

        asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    return await save_png(image_data, filename)
                else:
                    logger.error(f'Ошибка при загрузке изображения из {image_url}: HTTP {response.status}')
                    return None
    except aiohttp.ClientError as e:
        logger.error(f'Ошибка клиента aiohttp при загрузке изображения из {image_url}: {e}')
        return None
    except Exception as e:
        logger.error(f'Неизвестная ошибка при загрузке изображения из {image_url}: {e}')
        return None

async def save_png(image_data: bytes, file_name: Union[str, Path]) -> Union[str, None]:
    """
    Асинхронно сохраняет предоставленные данные изображения в формате PNG.

    :param image_data: Двоичные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла или путь, куда будет сохранено изображение.
    :type file_name: Union[str, Path]
    :return: Путь к сохраненному файлу или None в случае неудачи.
    :rtype: Union[str, None]

    :raises aiofiles.os.error.OSError: If there is an OS error.
    :raises Exception: If any other error occurs during the process.

    Пример:
    
    .. code-block:: python
    
        import asyncio

        with open("example_image.png", "rb") as f:
            image_data = f.read()
        asyncio.run(save_png(image_data, "saved_image.png"))
    """
    try:
        async with aiofiles.open(file_name, "wb") as f:
            await f.write(image_data)
        return str(file_name)
    except OSError as e:
        logger.error(f'Ошибка ОС при сохранении изображения в {file_name}: {e}')
        return None
    except Exception as e:
         logger.error(f'Неизвестная ошибка при сохранении изображения в {file_name}: {e}')
         return None


def get_image_data(file_name: Union[str, Path]) -> Union[bytes, None]:
    """
    Синхронно читает двоичные данные изображения из указанного файла.

    :param file_name: Имя файла или путь к изображению.
    :type file_name: Union[str, Path]
    :return: Двоичные данные изображения или None, если файл не найден или произошла ошибка.
    :rtype: Union[bytes, None]

    :raises FileNotFoundError: If the file is not found.
    :raises Exception: If any other error occurs during the process.
    
    Пример:
    
    .. code-block:: python
    
        data = get_image_data("saved_image.png")
        print(data)  # Вывод: b'\\x89PNG\\r\\n...'
    """
    try:
        with open(file_name, "rb") as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_name}')
        return None
    except Exception as e:
        logger.error(f'Неизвестная ошибка при чтении изображения из {file_name}: {e}')
        return None


def random_image(root_path: Union[str, Path]) -> Union[str, None]:
    """
    Рекурсивно ищет случайное изображение в указанном каталоге и возвращает его путь.

    :param root_path: Каталог для поиска изображений.
    :type root_path: Union[str, Path]
    :return: Путь к случайному изображению или None, если изображения не найдены.
    :rtype: Union[str, None]
    
    :raises Exception: If an error occurs while searching for images.
    
    Пример:
    
    .. code-block:: python
    
        random_image_path = random_image("path/to/images")
        if random_image_path:
            print(f"Случайное изображение: {random_image_path}")
        else:
            print("Изображения не найдены.")
    """
    try:
        image_files = []
        for dirpath, _, filenames in os.walk(root_path):
            for filename in filenames:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_files.append(os.path.join(dirpath, filename))
        if image_files:
            return random.choice(image_files)
        else:
           logger.debug(f'Изображения не найдены в каталоге: {root_path}')
           return None
    except Exception as e:
        logger.error(f'Неизвестная ошибка при поиске случайного изображения в {root_path}: {e}')
        return None

```