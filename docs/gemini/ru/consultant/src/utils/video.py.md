# Анализ кода модуля `video`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разделен на функции с четкими целями.
    - Присутствует документация в формате docstring для функций.
    - Используется асинхронность для операций ввода-вывода, что хорошо для производительности.
    - Есть обработка ошибок и логирование.
    - Проверки на существование и размер файла после сохранения.
-  Минусы
    -  Отсутствует общий docstring для модуля.
    -  Используется `asyncio.run` в `main()`, что может быть не оптимально для асинхронных приложений.
    -  В `main()` отсутствует обработка ошибок при выполнении `save_video_from_url`.

**Рекомендации по улучшению**

1.  **Добавить Docstring модуля:** В начале файла добавить docstring, описывающий назначение модуля.
2.  **Уточнить документацию:** Дополнить документацию, включая примеры использования, в соответствии с RST.
3.  **Улучшить обработку ошибок:** Логировать ошибки с использованием `logger.error`.
4.  **Использовать `j_loads`:** В данном модуле не требуется использование `j_loads`, так как нет работы с JSON.
5.  **Улучшить `main`:**  Обработать ошибку возвращаемую из `save_video_from_url` и переписать `main` для работы в асинхронном контексте
6.  **Унифицировать кавычки:** Использовать одинарные кавычки в коде Python, кроме случаев вывода.
7.  **Импортировать `logger`:** Использовать явный импорт `from src.logger.logger import logger`.

**Оптимизированный код**

```python
"""
Модуль для асинхронной загрузки и сохранения видео файлов.
=========================================================================================

Этот модуль предоставляет асинхронные функции для загрузки и сохранения видеофайлов,
а также для получения данных видео. Включает обработку ошибок и логирование для
обеспечения надежной работы.

Пример использования
--------------------

Пример использования асинхронной функции `save_video_from_url`:

.. code-block:: python

    import asyncio
    from pathlib import Path

    async def main():
        result = await save_video_from_url(
            'https://example.com/video.mp4', 'local_video.mp4'
        )
        if result:
            print(f'Видео сохранено по пути: {result}')
        else:
             print('Не удалось сохранить видео')

    asyncio.run(main())


Пример использования функции `get_video_data`:

.. code-block:: python

    data = get_video_data('local_video.mp4')
    if data:
        print(data[:10]) # Выводим первые 10 байт, чтобы проверить
    else:
         print('Не удалось прочитать видео')

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

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
    """Асинхронно загружает видео с URL и сохраняет его локально.

    Args:
        url (str): URL для загрузки видео.
        save_path (str): Путь для сохранения загруженного видео.

    Returns:
        Optional[Path]: Путь к сохраненному файлу или None, если операция не удалась.
            Возвращает None в случае ошибок и если размер файла равен 0 байт.

    Raises:
        aiohttp.ClientError: В случае сетевых ошибок во время загрузки.

    Example:
        >>> import asyncio
        >>> async def main():
        ...     result = await save_video_from_url('https://example.com/video.mp4', 'test.mp4')
        ...     if result:
        ...         print(f'Видео сохранено по пути: {result}')
        ...     else:
        ...          print('Не удалось сохранить видео')
        >>> asyncio.run(main())
        ... # PosixPath('test.mp4') или None если не удалось
    """
    # Преобразует путь к файлу в объект Path
    save_path = Path(save_path)

    try:
        # Создаёт асинхронную сессию для выполнения HTTP запроса
        async with aiohttp.ClientSession() as session:
            # Выполняет GET запрос по указанному URL
            async with session.get(url) as response:
                # Проверяет статус ответа на наличие ошибок HTTP
                response.raise_for_status()

                # Создаёт родительские директории, если они не существуют
                save_path.parent.mkdir(parents=True, exist_ok=True)

                # Открывает файл для записи в двоичном режиме
                async with aiofiles.open(save_path, 'wb') as file:
                    # Цикл для чтения данных из ответа
                    while True:
                        # Читает данные кусками по 8192 байта
                        chunk = await response.content.read(8192)
                        # Если данных нет, код завершает цикл
                        if not chunk:
                            break
                        # Записывает полученные данные в файл
                        await file.write(chunk)

        # Проверяет существование файла после сохранения
        if not save_path.exists():
            logger.error(f'Файл {save_path} не был сохранен.')
            return None

        # Проверяет, что файл не пустой
        if save_path.stat().st_size == 0:
            logger.error(f'Загруженный файл {save_path} пустой.')
            return None

        # Возвращает путь к сохранённому файлу в случае успеха
        return save_path

    # Обрабатывает сетевые ошибки при загрузке видео
    except aiohttp.ClientError as e:
        logger.error(f'Сетевая ошибка при загрузке видео: {e}')
        return None
    # Обрабатывает любые другие ошибки при сохранении видео
    except Exception as e:
        logger.error(f'Ошибка при сохранении видео {save_path}: {e}', exc_info=True)
        return None


def get_video_data(file_name: str) -> Optional[bytes]:
    """Получает бинарные данные видеофайла, если он существует.

    Args:
        file_name (str): Путь к видеофайлу для чтения.

    Returns:
        Optional[bytes]: Бинарные данные файла, если он существует, иначе `None`.
        Возвращает `None`, если файл не найден или произошла ошибка.

    Example:
        >>> data = get_video_data('test.mp4')
        >>> if data:
        ...    print(data[:10])
        ... # b'\\x00\\x00\\x00...' или None если не удалось
    """
    # Преобразует имя файла в объект Path
    file_path = Path(file_name)

    # Проверяет, существует ли файл
    if not file_path.exists():
        logger.error(f'Файл {file_name} не найден.')
        return None

    try:
        # Открывает файл в двоичном режиме для чтения
        with open(file_path, 'rb') as file:
            # Возвращает бинарные данные файла
            return file.read()
    # Обрабатывает любые ошибки при чтении файла
    except Exception as e:
        logger.error(f'Ошибка при чтении файла {file_name}: {e}', exc_info=True)
        return None


async def main():
    """
    Функция main для запуска асинхронной загрузки видео.
    """
    # Замените на валидный URL
    url = 'https://example.com/video.mp4'
    save_path = 'local_video.mp4'

    # Вызывает асинхронную функцию для загрузки и сохранения видео
    result = await save_video_from_url(url, save_path)

    # Проверяет результат и выводит сообщение об успехе или ошибке
    if result:
        print(f'Видео сохранено в {result}')
    else:
         print('Не удалось сохранить видео')

if __name__ == '__main__':
    # Запускает асинхронную функцию main
    asyncio.run(main())
```