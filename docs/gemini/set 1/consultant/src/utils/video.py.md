# Анализ кода модуля `video.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован, функции имеют четкое назначение.
    -   Используется асинхронное программирование для загрузки видео, что повышает производительность.
    -   Присутствует обработка ошибок и логирование.
    -   Используются `Path` для работы с путями, что делает код более читаемым и кроссплатформенным.
    -   Есть примеры использования функций в docstring.
-   Минусы
    -   Не все комментарии и docstring соответствуют формату reStructuredText.
    -   Используется стандартный блок try-except, где можно было бы использовать `logger.error` без исключений.

**Рекомендации по улучшению**

1.  **Форматирование документации**:
    -   Переписать все комментарии и docstring в формате reStructuredText.
    -   Добавить подробное описание параметров и возвращаемых значений.
2.  **Логирование ошибок**:
    -   Избегать использования общих блоков `try-except` и вместо этого использовать `logger.error`.
3.  **Импорты**:
    -   Убедиться, что все необходимые импорты присутствуют.
4.  **Сохранение комментариев**:
    -   Сохранить все существующие комментарии после `#` без изменений.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для асинхронной загрузки и сохранения видеофайлов.
======================================================

Этот модуль предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также получения данных видео.
Он включает обработку ошибок и логирование для надежной работы.

Функции:
    - save_video_from_url(url: str, save_path: str) -> Optional[Path]:
      Загружает видео по URL и сохраняет его локально асинхронно. Обрабатывает возможные сетевые проблемы и ошибки сохранения файла.

    - get_video_data(file_name: str) -> Optional[bytes]:
      Извлекает двоичные данные видеофайла, если он существует. Обрабатывает ошибки отсутствия файла и ошибки чтения.

Примеры:
    >>> import asyncio
    >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
    PosixPath('local_video.mp4')  # или None в случае ошибки

    >>> data = get_video_data("local_video.mp4")
    >>> if data:
    ...     print(data[:10])  # Выведет первые 10 байт для проверки
    b'\\x00\\x00\\x00...'
"""

import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional
import asyncio
from src.logger.logger import logger


  # Режим работы (разработка, продакшн)


async def save_video_from_url(
    url: str,
    save_path: str
) -> Optional[Path]:
    """
    Загружает видео по URL и сохраняет его локально асинхронно.

    :param url: URL для загрузки видео.
    :type url: str
    :param save_path: Путь для сохранения загруженного видео.
    :type save_path: str
    :return: Путь к сохраненному файлу или None в случае ошибки. Возвращает None при ошибках и если размер файла 0 байт.
    :rtype: Optional[Path]
    :raises aiohttp.ClientError: При сетевых ошибках во время загрузки.
    """
    # Преобразует путь к файлу в объект Path
    save_path = Path(save_path)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверяет HTTP ошибки

                # Создаёт родительские директории, если они не существуют
                save_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(save_path, "wb") as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)

        # Проверка после сохранения файла
        if not save_path.exists():
            logger.error(f"Файл {save_path} не был сохранен успешно.")
            return None

        if save_path.stat().st_size == 0:
            logger.error(f"Загруженный файл {save_path} пустой.")
            return None

        return save_path

    except aiohttp.ClientError as e:
        # Логирование ошибки при сетевых проблемах
        logger.error(f"Сетевая ошибка при загрузке видео: {e}")
        return None
    except Exception as e:
        # Логирование ошибки при сохранении файла
        logger.error(f"Ошибка при сохранении видео {save_path}: {e}", exc_info=True)
        return None


def get_video_data(file_name: str) -> Optional[bytes]:
    """
    Извлекает двоичные данные видеофайла, если он существует.

    :param file_name: Путь к видеофайлу для чтения.
    :type file_name: str
    :return: Двоичные данные файла, если он существует, или None если файл не найден или произошла ошибка.
    :rtype: Optional[bytes]
    """
    # Преобразует имя файла в объект Path
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"Файл {file_name} не найден.")
        return None

    try:
        # Читает двоичные данные из файла
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as e:
        # Логирование ошибки при чтении файла
        logger.error(f"Ошибка чтения файла {file_name}: {e}", exc_info=True)
        return None


def main():
    # Пример использования функций
    url = "https://example.com/video.mp4"  # Замените на валидный URL
    save_path = "local_video.mp4"
    result = asyncio.run(save_video_from_url(url, save_path))
    if result:
        print(f"Видео сохранено в {result}")


if __name__ == "__main__":
    main()
```