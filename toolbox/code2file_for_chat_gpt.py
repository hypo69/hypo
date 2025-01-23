## \file /dev_utils/code2file_for_chat_gpt.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module: dev_utils 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""
	:platform: Windows, Unix
	:synopsis:

"""
 

"""
 
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'development'
  
"""  """


""" Этот скрипт рекурсивно читает и обрабатывает все указанные текстовые и данные файлы в каталоге 
и сохраняет объединенное содержимое в один файл. Скрипт также позволяет удалять блоки с тройными кавычками 
из файлов Python, если это указано.

Функции:
- clean_html: Удаляет HTML-теги из содержимого.
- remove_docstrings: Удаляет блоки с тройными кавычками из содержимого.
- delete_directory_contents: Рекурсивно удаляет все содержимое указанной директории.
- read_text_files: Читает все указанные файлы в каталоге и сохраняет объединенный текст в один файл.

Примеры:
read_text_files('../temp/chat_gpt', 'output.txt', remove_docs=True)
"""
import header
import os
import json
import csv
import xml.etree.ElementTree as ET
import pandas as pd
import yaml
import sqlite3
from pathlib import Path
from bs4 import BeautifulSoup
import re
from src.logger import logger

# Добавляем список директорий и файлов, которые нужно удалить
EXCLUDE_DIRS = ['__pycache__', '.git', '.egg-info', '.ipynb_checkpoints']
EXCLUDE_EXTENSIONS = ['.pyc', '.pyo']  # Временные файлы Python

def clean_html(content: str) -> str:
    """ Удаляет HTML-теги из содержимого.

    Args:
        content (str): HTML-содержимое для очистки.

    Returns:
        str: Содержимое без HTML-тегов.

    Пример:
        >>> clean_html('<p>Hello, World!</p>')
        'Hello, World!'
    """
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()

def remove_docstrings(content: str) -> str:
    """ Удаляет все блоки с тройными кавычками `\"""` и `\'''` из текста.

    Args:
        content (str): Текстовое содержимое, из которого нужно удалить блоки с тройными кавычками.

    Returns:
        str: Текст без блоков с тройными кавычками.

    Пример:
        >>> remove_docstrings('''def foo():\n    \"""This is a docstring\"""\\n    pass''')
        'def foo():\\n    pass'
    """
    # Удаляем многострочные докстринги на основе тройных двойных кавычек
    content = re.sub(r'\"\"\"[\s\S]*?\"\"\"', "", content)
    # Удаляем многострочные докстринги на основе тройных одинарных кавычек
    content = re.sub(r"\'\'\'[\s\S]*?\'\'\'", "", content)
    return content

def delete_directory_contents(directory: Path) -> None:
    """ Рекурсивно удаляет все содержимое указанной директории.

    Args:
        directory (Path): Путь к директории, содержимое которой нужно удалить.

    Returns:
        None

    Пример:
        >>> delete_directory_contents(Path('../tmp/chat_gpt/aliexpress'))
    """
    for item in directory.iterdir():
        if item.is_dir():
            delete_directory_contents(item)
            try:
                item.rmdir()
                logger.info(f"Deleted directory: {item}")
            except OSError as ex:
                logger.error(f"Error deleting directory {item=}", ex, exc_info=False)
        else:
            try:
                item.unlink()
                logger.info(f"Deleted file: {item}")
            except OSError as ex:
                logger.error(f"Error deleting file {item=}", ex, exc_info=False)

def read_text_files(
    directory: str, output_file: str, remove_docs: bool = False, max_chars: int = 2000
) -> None:
    """ Читает все указанные Python файлы в каталоге и сохраняет объединенный текст в несколько файлов,
    если размер содержания превышает 2000 символов.

    Args:
        directory (str): Каталог для поиска файлов.
        output_file (str): Базовое имя файла для сохранения объединенного текста.
        remove_docs (bool): Если `True`, удаляет блоки с тройными кавычками из текста. По умолчанию `False`.
        max_chars (int): Максимальное количество символов для каждого файла. По умолчанию 2000.

    Returns:
        None

    Пример:
        >>> read_text_files('src', 'output.txt', remove_docs=True)
    """
    output_path = Path(output_file)
    base_name = output_path.stem
    extension = output_path.suffix
    output_dir = output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    file_number = 1
    current_char_count = 0
    current_output_file = output_dir / f"{base_name}_{file_number}{extension}"
    current_output_file.touch(exist_ok=True)

    logger.info(f"Начинаем обработку каталога: {directory}")
    
    with current_output_file.open("w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(directory, topdown=False):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                if dir_name in EXCLUDE_DIRS or dir_name.startswith("_") or "*" in dir_name:
                    delete_directory_contents(dir_path)

            for filename in files:
                file_path = Path(root) / filename
                # Проверяем, является ли файл Python-файлом
                if file_path.suffix == ".py":
                    logger.info(f"Обрабатываем файл: {file_path}")
                    try:
                        with file_path.open("r", encoding="utf-8") as infile:
                            content = infile.read()

                            if not content.strip():
                                logger.warning(f"Файл пустой: {file_path}")
                                continue

                            if remove_docs:
                                content = remove_docstrings(content)

                        # Проверяем, нужно ли создавать новый файл
                        if current_char_count + len(content) > max_chars:
                            outfile.close()
                            file_number += 1
                            current_char_count = 0
                            current_output_file = output_dir / f"{base_name}_{file_number}{extension}"
                            current_output_file.touch(exist_ok=True)
                            logger.info(f"Создан новый файл для вывода: {current_output_file}")
                            outfile = current_output_file.open("w", encoding="utf-8")

                        outfile.write(f"--- {filename} ---\n{content}\n\n")
                        current_char_count += len(content)

                    except (OSError, IOError, ValueError) as ex:
                        logger.error(f"Ошибка при обработке файла {file_path=}: {ex}", exc_info=True)


if __name__ == "__main__":
    # Указываем каталог для поиска и файл для сохранения вывода
    directory_to_search = "../data/chat_gpt/code2file"
    output_file_path = Path("../data/chat_gpt/code2file/code2file.txt")

    # Создаем директорию, если она не существует
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Создаем файл, если его не существует
    output_file_path.touch(exist_ok=True)

    read_text_files(directory_to_search, output_file_path, remove_docs=True)
