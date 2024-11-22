## \file hypotez/src/utils/string/remove_outer_quotes.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string.remove_outer_quotes 
	:platform: Windows, Unix
	:synopsis: Script for processing text files to remove triple quotes around code blocks. 
Supports blocks formatted with Python, Markdown, and reStructuredText (reST).

"""
MODE = 'development'

import header
from pathlib import Path
import re


def process_files_in_directory(directory: Path) -> None:
    """
    Processes all files in the specified directory. Removes triple quotes around 
    code blocks formatted with Python, Markdown, or reStructuredText.

    :param directory: Path to the directory containing files to process.
    :type directory: Path
    """
    # Проходим по всем файлам в указанной директории
    for file_path in directory.glob('*'):
        if file_path.is_file():
            # Считываем содержимое файла
            with file_path.open('r', encoding='utf-8') as file:
                content = file.read()

            # Удаляем тройные кавычки вокруг блоков кода
            updated_content = re.sub(
                r"(['\"]{3})```(python|markdown|rst)\b(.*?)```(['\"]{3})",
                r'```\2\3```',
                content,
                flags=re.DOTALL
            )

            # Сохраняем изменения, если файл был изменен
            if content != updated_content:
                with file_path.open('w', encoding='utf-8') as file:
                    file.write(updated_content)

if __name__ == '__main__':
    """
    Entry point for the script. Processes files in the specified directory.
    """
    # Указываем путь к директории
    directory_path = Path('../../../docs/model_docs')

    # Запуск обработки файлов
    process_files_in_directory(directory_path)
