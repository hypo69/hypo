# Анализ кода модуля `image.py`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и разбит на отдельные функции, каждая из которых выполняет свою задачу.
    - Используются асинхронные операции, что позволяет выполнять ввод-вывод не блокируя основной поток.
    - Документация в формате reStructuredText (RST) присутствует, хотя и требует некоторых улучшений.
    - Присутствует логирование ошибок с использованием `logger.error`, что облегчает отладку и мониторинг работы модуля.
    - Используются аннотации типов, что повышает читаемость и надежность кода.
- Минусы
    - Не все функции имеют полные docstring, требуются более точные описания и примеры.
    - Присутствует избыточное использование `try-except` блоков, которые можно заменить на обработку ошибок с помощью `logger.error`.
    - В некоторых местах не хватает обработки возможных ошибок.
    - Необходимо более точное описание возвращаемых значений, особенно в случае ошибок.
    - Отсутствует импорт `Path` из модуля `pathlib`.

**Рекомендации по улучшению**

1.  **Импорт**: Добавьте `from pathlib import Path` если он не импортируется.
2.  **Улучшение документации**:
    - Дополните docstring всех функций, добавьте примеры использования.
    - Уточните описание возвращаемых значений, в том числе при возникновении ошибок.
    - Используйте более точные формулировки в комментариях и docstring, избегайте слов вроде "получаем" и "делаем".
3.  **Обработка ошибок**:
    - Избегайте избыточного использования `try-except`, где это возможно, заменяя на `logger.error`.
    - Логируйте все ошибки и причины их возникновения.
4.  **Улучшение функций**:
    - В функции `save_png` проверьте корректность сохранения изображения после открытия с помощью `PIL`
5.  **Общая структура**:
    - Разместите константы и глобальные переменные в начале файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с изображениями.
=========================================================================================

Этот модуль предоставляет асинхронные функции для загрузки, сохранения и получения данных изображений.

Функции:
    - :func:`save_png_from_url`
    - :func:`save_png`
    - :func:`get_image_data`
    - :func:`random_image`

Примеры использования:
--------------------

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image

    # Пример использования функции save_png_from_url
    async def main():
        image_url = "https://example.com/image.png"
        filename = "local_image.png"
        result = await save_png_from_url(image_url, filename)
        print(f"Saved image: {result}")

        # Пример использования функции save_png
        image_data = b'\\x89PNG\\r\\n...'  # Замените на реальные данные изображения
        filename = "saved_image.png"
        result = await save_png(image_data, filename)
        print(f"Saved image: {result}")

        # Пример использования функции get_image_data
        image_data = get_image_data("saved_image.png")
        print(f"Image data: {image_data}")

        # Пример использования функции random_image
        root_path = Path("path/to/images")
        result = random_image(root_path)
        print(f"Random image path: {result}")

    if __name__ == "__main__":
        asyncio.run(main())
"""
MODE = 'dev'
import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
import random
from src.logger.logger import logger
from src.utils.printer import pprint


async def save_png_from_url(image_url: str, filename: str | Path) -> str | None:
    """
    Асинхронно загружает изображение из URL и сохраняет его локально.

    :param image_url: URL изображения для загрузки.
    :type image_url: str
    :param filename: Имя файла для сохранения изображения.
    :type filename: str | Path
    :return: Путь к сохраненному файлу, если операция успешна, иначе None.
    :rtype: str | None

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        # код выполняет асинхронную загрузку изображения по URL
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        # Логирование ошибки загрузки изображения
        logger.error(f"Ошибка при загрузке изображения по URL: {image_url}", exc_info=True)
        return None

    # Код вызывает функцию сохранения изображения
    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """
    Асинхронно сохраняет изображение в формате PNG.

    :param image_data: Бинарные данные изображения.
    :type image_data: bytes
    :param file_name: Имя файла для сохранения изображения.
    :type file_name: str | Path
    :return: Путь к сохраненному файлу, если операция успешна, иначе None.
    :rtype: str | None

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    file_path = Path(file_name)
    try:
        # Код создает необходимые директории
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Код записывает данные изображения в файл
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        # Код проверяет, создан ли файл
        if not file_path.exists():
            logger.error(f"Файл {file_path} не был создан.")
            return None

        # Код открывает и сохраняет изображение, преобразуя его в формат PNG.
        image = Image.open(file_path)
        image.save(file_path, "PNG")

        # Код проверяет размер файла после сохранения
        if file_path.stat().st_size == 0:
            logger.error(f"Файл {file_path} сохранен, но его размер равен 0 байт.")
            return None

    except Exception as ex:
        # Логирование критической ошибки сохранения файла
        logger.critical(f"Не удалось сохранить файл {file_path}", exc_info=True)
        return None

    # Код возвращает путь к файлу
    return str(file_path)


def get_image_data(file_name: str | Path) -> bytes | None:
    """
    Извлекает бинарные данные файла, если он существует.

    :param file_name: Имя файла для чтения.
    :type file_name: str | Path
    :return: Бинарные данные файла, если файл существует, иначе None.
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
        # Код читает данные из файла
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        # Логирование ошибки чтения файла
        logger.error(f"Ошибка чтения файла {file_path}", exc_info=True)
        return None


def random_image(root_path: str | Path) -> str | None:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает его путь.

    :param root_path: Директория для поиска изображений.
    :type root_path: str | Path
    :return: Путь к случайному изображению, если изображения найдены, иначе None.
    :rtype: str | None

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
    """
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = []

    # Код рекурсивно ищет файлы изображений
    for file_path in root_path.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            image_files.append(file_path)

    # Код проверяет, найдены ли изображения
    if not image_files:
        logger.warning(f"Изображения не найдены в {root_path}.")
        return None

    # Код возвращает путь к случайному изображению
    return str(random.choice(image_files))
```