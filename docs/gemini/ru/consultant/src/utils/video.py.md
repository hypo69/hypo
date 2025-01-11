# Анализ кода модуля `video`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на отдельные функции.
    - Используется асинхронное программирование для эффективной загрузки видео.
    - Присутствует обработка ошибок и логирование.
    - Есть docstring для функций.
    - Используются `Path` для работы с путями к файлам.
- Минусы
    - Отсутствует описание модуля в начале файла.
    - Не используется `j_loads` или `j_loads_ns`.
    - В некоторых местах используется `print`, нужно заменить на `logger`.
    - `exc_info=True` при логировании ошибок не всегда нужен.
    - Не все docstring соответствуют стандарту Sphinx.
    - Отсутствует проверка размера файла после скачивания
    - `main()` не соответствует общему стилю кода

**Рекомендации по улучшению**
1.  Добавить описание модуля в начале файла.
2.  Заменить `print` в `main` на `logger.info`.
3.  Уточнить docstring в соответствии со стандартами Sphinx.
4.  Убрать `exc_info=True` из logger.error, где это не нужно.
5.  Добавить проверку размера файла после скачивания.
6.  Сделать `main` асинхронной.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для работы с видео файлами.
=========================================================================================

Этот модуль предоставляет асинхронные функции для загрузки и сохранения видео файлов,
а также для получения данных видео. Включает обработку ошибок и логирование для
надежной работы.

Пример использования
--------------------

Примеры использования функций:

.. code-block:: python

    import asyncio
    from pathlib import Path

    async def main():
        # Загрузка видео по URL
        video_path = await save_video_from_url('https://example.com/video.mp4', 'local_video.mp4')
        if video_path:
            print(f"Видео успешно сохранено в: {video_path}")
        else:
            print("Не удалось сохранить видео.")

        # Получение данных из видео файла
        if video_path:
            video_data = get_video_data(str(video_path))
            if video_data:
                print(f"Первые 10 байт видео: {video_data[:10]}")
            else:
                print("Не удалось получить данные видео.")


    if __name__ == "__main__":
        asyncio.run(main())
"""
import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional
import asyncio
from src.logger.logger import logger


async def save_video_from_url(
    url: str,
    save_path: str
) -> Optional[Path]:
    """
    Асинхронно загружает видео по URL и сохраняет его локально.

    Args:
        url (str): URL для загрузки видео.
        save_path (str): Путь для сохранения видео.

    Returns:
        Optional[Path]: Путь к сохраненному файлу, или None в случае ошибки.

    Raises:
        aiohttp.ClientError: Возникает при сетевых ошибках во время загрузки.

    Example:
        >>> import asyncio
        >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
        PosixPath('local_video.mp4')  # or None if failed
    """
    save_path = Path(save_path)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка HTTP ошибок

                # Создает родительские директории, если они не существуют
                save_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(save_path, 'wb') as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)

        # Проверки после сохранения
        if not save_path.exists():
            logger.error(f'Файл {save_path} не был успешно сохранен.')
            return None

        if save_path.stat().st_size == 0:
            logger.error(f'Загруженный файл {save_path} пустой.')
            return None

        return save_path

    except aiohttp.ClientError as e:
        logger.error(f'Сетевая ошибка при загрузке видео: {e}')
        return None
    except Exception as e:
        logger.error(f'Ошибка при сохранении видео {save_path}: {e}')
        return None


def get_video_data(file_name: str) -> Optional[bytes]:
    """
    Получает бинарные данные видео файла.

    Args:
        file_name (str): Путь к видео файлу.

    Returns:
        Optional[bytes]: Бинарные данные файла, или None, если файл не найден или произошла ошибка.

    Example:
        >>> data = get_video_data("local_video.mp4")
        >>> if data:
        ...     print(data[:10])
        b'\\x00\\x00\\x00...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f'Файл {file_name} не найден.')
        return None

    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except Exception as e:
        logger.error(f'Ошибка при чтении файла {file_name}: {e}')
        return None


async def main():
    """
    Функция для демонстрации работы функций сохранения и получения видео.
    """
    url = 'https://example.com/video.mp4'  # Замените на корректный URL
    save_path = 'local_video.mp4'
    result = await save_video_from_url(url, save_path)
    if result:
        logger.info(f'Видео сохранено в {result}')


if __name__ == '__main__':
    asyncio.run(main())
```