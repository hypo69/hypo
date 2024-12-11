## Улучшенный код

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

Пример использования
--------------------

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image

    async def main():
        # Загрузка и сохранение изображения по URL
        image_path = await save_png_from_url("https://example.com/image.png", "local_image.png")
        if image_path:
            print(f"Изображение сохранено: {image_path}")

        # Сохранение изображения из байтов
        with open("example_image.png", "rb") as f:
            image_data = f.read()
        saved_image_path = await save_png(image_data, "saved_image.png")
        if saved_image_path:
           print(f"Изображение сохранено: {saved_image_path}")

        # Получение данных изображения
        image_data = get_image_data("saved_image.png")
        if image_data:
            print(f"Данные изображения: {image_data[:20]}...")

        # Получение случайного изображения
        random_image_path = random_image("path/to/images")
        if random_image_path:
           print(f"Случайное изображение: {random_image_path}")

    if __name__ == "__main__":
        asyncio.run(main())

"""
#  Импортируем необходимые модули
MODE = 'dev'
import aiohttp #  используется для асинхронных HTTP запросов
import aiofiles #  используется для асинхронных файловых операций
from PIL import Image #  используется для работы с изображениями
from pathlib import Path #  используется для работы с путями файлов и директорий
import asyncio #  используется для асинхронного программирования
import random #  используется для генерации случайных чисел
from src.logger.logger import logger #  используется для логирования ошибок и отладки
from src.utils.printer import pprint #  используется для печати отладочной информации


async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """
    Загружает изображение по URL и сохраняет его локально в формате PNG асинхронно.

    :param image_url: URL изображения для загрузки.
    :param filename: Имя файла для сохранения изображения.
    :return: Путь к сохраненному файлу или ``None``, если операция не удалась.

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        #  Инициализируем асинхронную сессию для выполнения HTTP запроса
        async with aiohttp.ClientSession() as session:
            #  Выполняем GET запрос по URL
            async with session.get(image_url) as response:
                #  Проверяем статус ответа, выбрасывая исключение в случае ошибки
                response.raise_for_status()
                #  Читаем данные изображения из ответа
                image_data = await response.read()
    except Exception as ex:
        #  Логируем ошибку при загрузке изображения
        logger.error("Error downloading image", ex, exc_info=True)
        return None

    #  Сохраняем полученные данные изображения в файл
    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """
    Сохраняет изображение в формате PNG асинхронно.

    :param image_data: Бинарные данные изображения.
    :param file_name: Имя файла для сохранения изображения.
    :return: Путь к сохраненному файлу или ``None``, если операция не удалась.

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    #  Преобразуем имя файла в объект Path
    file_path = Path(file_name)

    try:
        #  Создаем необходимые директории для файла, если их нет
        file_path.parent.mkdir(parents=True, exist_ok=True)

        #  Открываем файл для записи в бинарном режиме асинхронно
        async with aiofiles.open(file_path, "wb") as file:
            #  Записываем данные изображения в файл
            await file.write(image_data)

        #  Проверяем, был ли создан файл
        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            return None

        #  Открываем изображение с помощью PIL
        image = Image.open(file_path)
        #  Сохраняем изображение в формате PNG
        image.save(file_path, "PNG")

        #  Проверяем размер файла после сохранения
        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            return None

    except Exception as ex:
        #  Логируем критическую ошибку при сохранении файла
        logger.critical(f"Failed to save file {file_path}", ex, exc_info=True)
        return None

    #  Возвращаем путь к сохраненному файлу в виде строки
    return str(file_path)


def get_image_data(file_name: str | Path) -> bytes | None:
    """
    Получает бинарные данные файла, если он существует.

    :param file_name: Имя файла для чтения.
    :return: Бинарные данные файла или ``None``, если файл не найден или произошла ошибка.

    :example:
        >>> get_image_data("saved_image.png")
        b'\\x89PNG\\r\\n...'
    """
    #  Преобразуем имя файла в объект Path
    file_path = Path(file_name)

    #  Проверяем существование файла
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        #  Открываем файл для чтения в бинарном режиме
        with open(file_path, "rb") as file:
            #  Возвращаем бинарные данные файла
            return file.read()
    except Exception as ex:
        #  Логируем ошибку при чтении файла
        logger.error(f"Error reading file {file_path}", ex, exc_info=True)
        return None


def random_image(root_path: str | Path) -> str | None:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает его путь.

    :param root_path: Директория для поиска изображений.
    :return: Путь к случайному изображению или ``None``, если изображения не найдены.

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
    """
    #  Преобразуем путь к директории в объект Path
    root_path = Path(root_path)
    #  Список расширений файлов изображений
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    #  Список для хранения путей к файлам изображений
    image_files = []

    #  Рекурсивно ищем файлы изображений
    for file_path in root_path.rglob("*"):
        #  Проверяем, является ли путь файлом и имеет ли расширение изображения
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            #  Добавляем путь к файлу в список
            image_files.append(file_path)

    #  Проверяем, найдены ли изображения
    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    #  Возвращаем путь к случайному изображению
    return str(random.choice(image_files))
```

## Внесённые изменения

1.  **Добавлены импорты:**
    *   `from src.logger.logger import logger` для логирования.
    *   `from src.utils.printer import pprint` для печати отладочной информации.
2.  **Обновлены Docstrings:**
    *   Добавлены и улучшены описания модулей, функций и параметров в формате reStructuredText (RST).
    *   Добавлены примеры использования для каждой функции.
3.  **Изменена обработка ошибок:**
    *   Убраны лишние `try-except` блоки и заменены на `logger.error` для более эффективной обработки.
    *   Логирование ошибок вынесено в отдельные блоки.
4.  **Использование `Path`:**
    *   Используется `Path` для работы с путями файлов.
5.  **Улучшен код сохранения изображений:**
    *   Добавлена проверка размера сохраненного файла.
    *   Удален лишний импорт `os`
6.  **Форматирование кода:**
    *   Применен более читаемый стиль форматирования.
7.  **Добавлены комментарии к коду:**
    *   Добавлены подробные комментарии для пояснения работы каждого блока кода.

## Оптимизированный код

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

Пример использования
--------------------

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.image import save_png_from_url, save_png, get_image_data, random_image

    async def main():
        # Загрузка и сохранение изображения по URL
        image_path = await save_png_from_url("https://example.com/image.png", "local_image.png")
        if image_path:
            print(f"Изображение сохранено: {image_path}")

        # Сохранение изображения из байтов
        with open("example_image.png", "rb") as f:
            image_data = f.read()
        saved_image_path = await save_png(image_data, "saved_image.png")
        if saved_image_path:
           print(f"Изображение сохранено: {saved_image_path}")

        # Получение данных изображения
        image_data = get_image_data("saved_image.png")
        if image_data:
            print(f"Данные изображения: {image_data[:20]}...")

        # Получение случайного изображения
        random_image_path = random_image("path/to/images")
        if random_image_path:
           print(f"Случайное изображение: {random_image_path}")

    if __name__ == "__main__":
        asyncio.run(main())

"""
#  Импортируем необходимые модули
MODE = 'dev'
import aiohttp #  используется для асинхронных HTTP запросов
import aiofiles #  используется для асинхронных файловых операций
from PIL import Image #  используется для работы с изображениями
from pathlib import Path #  используется для работы с путями файлов и директорий
import asyncio #  используется для асинхронного программирования
import random #  используется для генерации случайных чисел
from src.logger.logger import logger #  используется для логирования ошибок и отладки
from src.utils.printer import pprint #  используется для печати отладочной информации


async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """
    Загружает изображение по URL и сохраняет его локально в формате PNG асинхронно.

    :param image_url: URL изображения для загрузки.
    :param filename: Имя файла для сохранения изображения.
    :return: Путь к сохраненному файлу или ``None``, если операция не удалась.

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        #  Инициализируем асинхронную сессию для выполнения HTTP запроса
        async with aiohttp.ClientSession() as session:
            #  Выполняем GET запрос по URL
            async with session.get(image_url) as response:
                #  Проверяем статус ответа, выбрасывая исключение в случае ошибки
                response.raise_for_status()
                #  Читаем данные изображения из ответа
                image_data = await response.read()
    except Exception as ex:
        #  Логируем ошибку при загрузке изображения
        logger.error("Error downloading image", ex, exc_info=True)
        return None

    #  Сохраняем полученные данные изображения в файл
    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """
    Сохраняет изображение в формате PNG асинхронно.

    :param image_data: Бинарные данные изображения.
    :param file_name: Имя файла для сохранения изображения.
    :return: Путь к сохраненному файлу или ``None``, если операция не удалась.

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    #  Преобразуем имя файла в объект Path
    file_path = Path(file_name)

    try:
        #  Создаем необходимые директории для файла, если их нет
        file_path.parent.mkdir(parents=True, exist_ok=True)

        #  Открываем файл для записи в бинарном режиме асинхронно
        async with aiofiles.open(file_path, "wb") as file:
            #  Записываем данные изображения в файл
            await file.write(image_data)

        #  Проверяем, был ли создан файл
        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            return None

        #  Открываем изображение с помощью PIL
        image = Image.open(file_path)
        #  Сохраняем изображение в формате PNG
        image.save(file_path, "PNG")

        #  Проверяем размер файла после сохранения
        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            return None

    except Exception as ex:
        #  Логируем критическую ошибку при сохранении файла
        logger.critical(f"Failed to save file {file_path}", ex, exc_info=True)
        return None

    #  Возвращаем путь к сохраненному файлу в виде строки
    return str(file_path)


def get_image_data(file_name: str | Path) -> bytes | None:
    """
    Получает бинарные данные файла, если он существует.

    :param file_name: Имя файла для чтения.
    :return: Бинарные данные файла или ``None``, если файл не найден или произошла ошибка.

    :example:
        >>> get_image_data("saved_image.png")
        b'\\x89PNG\\r\\n...'
    """
    #  Преобразуем имя файла в объект Path
    file_path = Path(file_name)

    #  Проверяем существование файла
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        #  Открываем файл для чтения в бинарном режиме
        with open(file_path, "rb") as file:
            #  Возвращаем бинарные данные файла
            return file.read()
    except Exception as ex:
        #  Логируем ошибку при чтении файла
        logger.error(f"Error reading file {file_path}", ex, exc_info=True)
        return None


def random_image(root_path: str | Path) -> str | None:
    """
    Рекурсивно ищет случайное изображение в указанной директории и возвращает его путь.

    :param root_path: Директория для поиска изображений.
    :return: Путь к случайному изображению или ``None``, если изображения не найдены.

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
    """
    #  Преобразуем путь к директории в объект Path
    root_path = Path(root_path)
    #  Список расширений файлов изображений
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    #  Список для хранения путей к файлам изображений
    image_files = []

    #  Рекурсивно ищем файлы изображений
    for file_path in root_path.rglob("*"):
        #  Проверяем, является ли путь файлом и имеет ли расширение изображения
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            #  Добавляем путь к файлу в список
            image_files.append(file_path)

    #  Проверяем, найдены ли изображения
    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    #  Возвращаем путь к случайному изображению
    return str(random.choice(image_files))