# Анализ кода модуля `video.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и использует асинхронные операции для скачивания видео.
    - Присутствует базовая обработка ошибок с логированием.
    - Код соответствует PEP 8.
    - Документация в формате docstring присутствует.
-  Минусы
    -  Используются стандартные блоки `try-except`, вместо обработки ошибок с помощью `logger.error`.
    - Отсутствуют комментарии в коде, объясняющие логику работы.
    - Не все импорты необходимы (например `asyncio`).
    - Отсутствует явное указание кодировки при открытии файлов.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**

1. **Импорты**: Удалить ненужный импорт `asyncio`.
2. **Логирование**: Использовать `logger.error` для обработки ошибок вместо общих `try-except` блоков, за исключением случаев где нужно перехватить исключения для вызова `logger.error`.
3. **Комментарии**: Добавить комментарии в формате RST для функций и переменных, а также добавлять комментарии в самом коде, для объяснения логики работы.
4. **Кодировка файлов**: Явно указать кодировку `utf-8` при работе с файлами.
5. **Обработка ошибок**: Переработать обработку ошибок для большей ясности и унификации, используя возможности логирования.
6. **Документация**: Дополнить docstring для соответствия стандартам RST.
7.  **Удалить `main()`**:  Функция `main` не используется и может быть удалена.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с видео.
=========================================================================================

Этот модуль предоставляет асинхронные функции для скачивания и сохранения видеофайлов, а также извлечения видеоданных.
Включает обработку ошибок и логирование для надежной работы.

:platform: Windows, Unix
:synopsis: Утилиты для сохранения видео.

.. moduleauthor:: Timofey

Функции:
    - save_video_from_url(url: str, save_path: str) -> Optional[Path]:
        Асинхронно скачивает видео по URL и сохраняет его локально. Обрабатывает потенциальные сетевые проблемы и ошибки сохранения файлов.
    - get_video_data(file_name: str) -> Optional[bytes]:
        Извлекает бинарные данные видеофайла, если он существует. Обрабатывает ошибки отсутствия файла и чтения.
    

Примеры:
    >>> import asyncio
    >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
    PosixPath('local_video.mp4')  # или None в случае ошибки

    >>> data = get_video_data("local_video.mp4")
    >>> if data:
    ...     print(data[:10])  # Вывод первых 10 байт для проверки
    b'\\x00\\x00\\x00...'
"""

import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional
from src.logger.logger import logger





async def save_video_from_url(
    url: str,
    save_path: str
) -> Optional[Path]:
    """
    Асинхронно скачивает видео по URL и сохраняет его локально.

    :param url: URL для скачивания видео.
    :type url: str
    :param save_path: Путь для сохранения скачанного видео.
    :type save_path: str
    :return: Путь к сохраненному файлу или None, если операция не удалась.
    :rtype: Optional[Path]
    :raises aiohttp.ClientError: При сетевых ошибках во время загрузки.
    """
    # Преобразовывает путь к строке в объект Path
    save_path = Path(save_path)

    try:
        # Код выполняет асинхронный запрос на скачивание видео
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка HTTP ошибок

                # Код создает родительские каталоги, если они не существуют
                save_path.parent.mkdir(parents=True, exist_ok=True)

                # Код открывает файл для записи в бинарном режиме
                async with aiofiles.open(save_path, "wb") as file:
                    # Код читает файл частями и записывает
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)

        # Код проверяет, что файл был сохранен и его размер больше 0
        if not save_path.exists():
            logger.error(f"Файл {save_path} не был успешно сохранен.")
            return None

        if save_path.stat().st_size == 0:
            logger.error(f"Загруженный файл {save_path} пуст.")
            return None

        return save_path

    except aiohttp.ClientError as e:
         # Код логгирует ошибки при сетевых запросах
        logger.error(f"Сетевая ошибка при загрузке видео: {e}")
        return None
    except Exception as e:
        # Код логгирует ошибки при записи файла
        logger.error(f"Ошибка сохранения видео {save_path}: {e}", exc_info=True)
        return None


def get_video_data(file_name: str) -> Optional[bytes]:
    """
    Извлекает бинарные данные видеофайла, если он существует.

    :param file_name: Путь к видеофайлу для чтения.
    :type file_name: str
    :return: Бинарные данные файла, если он существует, или None в случае ошибки.
    :rtype: Optional[bytes]
    """
    # Преобразовывает путь к строке в объект Path
    file_path = Path(file_name)

    # Код проверяет существование файла
    if not file_path.exists():
        logger.error(f"Файл {file_name} не найден.")
        return None

    try:
        # Код открывает файл для чтения в бинарном режиме
        with open(file_path, "rb") as file:
            # Код возвращает содержимое файла
            return file.read()
    except Exception as e:
        # Код логгирует ошибки при чтении файла
        logger.error(f"Ошибка чтения файла {file_name}: {e}", exc_info=True)
        return None
```