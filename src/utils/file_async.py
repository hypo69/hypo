## \file /src/utils/file_async.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для асинхронных файловых операций.
=========================================================================================

Этот модуль предоставляет набор асинхронных утилит для работы с файлами,
таких как сохранение и чтение, с поддержкой обработки больших файлов
с использованием генераторов для экономии памяти.

Пример использования:
---------------------

.. code-block:: python

    import asyncio
    from pathlib import Path
    from src.utils.file_async import read_text_file_async

    async def main():
        file_path = Path('example.txt')
        content = await read_text_file_async(file_path)
        if content:
            print(f'File content: {content[:100]}...')

    if __name__ == "__main__":
        asyncio.run(main())
"""
import asyncio
import aiofiles
from pathlib import Path
from typing import List, Optional, AsyncGenerator, Union, Generator
from src.logger.logger import logger
import json


async def save_text_file_async(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w',
) -> bool:
    """
    Асинхронно сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).
    Returns:
        bool: `True`, если файл успешно сохранен, `False` в противном случае.
    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...    file_path = Path('example.txt')
        ...    data = 'Пример текста'
        ...    result = await save_text_file_async(file_path, data)
        ...    print(result)
        >>> if __name__ == "__main__":
        ...     asyncio.run(main())
        True
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents = True, exist_ok = True)

        async with aiofiles.open(file_path, mode, encoding = 'utf-8') as file:
            if isinstance(data, list):
                await file.writelines(f'{line}\n' for line in data)
            elif isinstance(data, dict):
                 await file.write(json.dumps(data, ensure_ascii = False, indent = 4))
            else:
                await file.write(str(data))
        return True
    except Exception as ex:
        logger.error(f'Ошибка при асинхронном сохранении файла {file_path}.', ex)
        ...
        return False



async def _read_file_content_async(file_path: Path, chunk_size: int) -> str:
    """
    Асинхронно читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Returns:
        str: Содержимое файла в виде строки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    content = ''
    async with aiofiles.open(file_path, mode = 'r', encoding = 'utf-8') as f:
        while True:
            chunk = await f.read(chunk_size)
            if not chunk:
                break
            content += chunk
        return content


async def _read_file_lines_generator_async(file_path: Path, chunk_size: int) -> AsyncGenerator[str, None]:
    """
    Асинхронно читает файл по строкам с помощью асинхронного генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Yields:
        str: Строки из файла.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    async with aiofiles.open(file_path, mode = 'r', encoding = 'utf-8') as f:
        while True:
                chunk = await f.read(chunk_size)
                if not chunk:
                    break
                lines = chunk.splitlines()
                # Если чанк не закончился полной строкой, то последнюю строку добавляем к следующему чанку
                if len(lines)>0 and not chunk.endswith('\n'):
                     next_chunk = await f.read(1)
                     if next_chunk != '':
                        lines[-1] = lines[-1] + next_chunk
                     else:
                        for line in lines:
                            yield line
                        break
                
                for line in lines:
                     yield line


async def read_text_file_async(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192
) -> AsyncGenerator[str, None] | str | None:
    """
    Асинхронно читает содержимое файла (или файлов из директории) с использованием генератора для экономии памяти.

    Args:
        file_path (str | Path): Путь к файлу или директории.
        as_list (bool, optional): Если `True`, то возвращает асинхронный генератор строк.
        extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.
    Returns:
         AsyncGenerator[str, None] | str | None: Асинхронный генератор строк, объединенная строка или `None` в случае ошибки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.

    Example:
        >>> import asyncio
        >>> from pathlib import Path
        >>> async def main():
        ...    file_path = Path('example.txt')
        ...    content = await read_text_file_async(file_path)
        ...    if content:
        ...       print(f'File content: {content[:100]}...')
        >>> if __name__ == "__main__":
        ...     asyncio.run(main())
        File content: Пример текста...
    """
    try:
        path = Path(file_path)
        if path.is_file():
           if as_list:
                return  _read_file_lines_generator_async(path, chunk_size=chunk_size)
           else:
                return await _read_file_content_async(path, chunk_size=chunk_size)
        elif path.is_dir():
            files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            if as_list:
               async def generate_lines_from_files():
                    for file in files:
                       async for line in read_text_file_async(file, as_list=True, chunk_size=chunk_size):
                           yield line
               return generate_lines_from_files()
            else:
                 contents = await asyncio.gather(*[read_text_file_async(p, chunk_size=chunk_size) for p in files])
                 return "\n".join(filter(None, contents) )
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            ...
            return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)
        ...
        return None