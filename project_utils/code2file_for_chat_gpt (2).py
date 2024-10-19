## \file utils/clear_files_for_chat_gpt.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Этот скрипт рекурсивно читает и обрабатывает все указанные текстовые и данные файлы в каталоге 
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
    """! Удаляет HTML-теги из содержимого.

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
    """! Удаляет все блоки с тройными кавычками `\"""` и `\'''` из текста.

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
    """! Рекурсивно удаляет все содержимое указанной директории.

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
    directory: str, output_file: str, remove_docs: bool = False
) -> None:
    """! Читает все указанные текстовые и данные файлы в каталоге и сохраняет объединенный текст в один файл,
    одновременно удаляя файлы и директории, которые начинаются с `_`, содержат `(` и `)`, 
    а также служебные директории типа `__pycache__` и временные файлы Python.

    Args:
        directory (str): Каталог для поиска файлов.
        output_file (str): Файл, в который будет сохранен объединенный текст.
        remove_docs (bool): Если `True`, удаляет блоки с тройными кавычками из текста. По умолчанию `False`.

    Returns:
        None

    Пример:
        >>> read_text_files('src', 'output.txt', remove_docs=True)
    """
    output_path = Path(output_file)
    output_path.touch(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(directory, topdown=False):
            # Удаляем файлы и директории, соответствующие условиям
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                # Удаляем служебные директории
                if dir_name in EXCLUDE_DIRS or dir_name.startswith("_") or "*" in dir_name:
                    delete_directory_contents(dir_path)

            for filename in files:
                file_path = Path(root) / filename
                # Удаляем временные файлы Python и другие ненужные файлы
                if filename.startswith("_") or ("(" in filename and ")" in filename) or file_path.suffix in EXCLUDE_EXTENSIONS:
                    try:
                        file_path.unlink()
                        logger.info(f"Deleted file: {file_path}")
                    except OSError as ex:
                        logger.error(f"Error deleting file {file_path=}", ex, exc_info=False)
                else:
                    # Обработка файлов, которые не подлежат удалению
                    try:
                        if file_path.suffix in [
                            ".py", ".txt", ".css", ".js", ".dot", ".mer", ".md", ".ps1", ".htm", ".html"
                        ]:
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                if remove_docs:
                                    content = remove_docstrings(content)
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix in [".html", ".htm"]:
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                cleaned_content = clean_html(content)
                                outfile.write(f"--- {filename} ---\n{cleaned_content}\n\n")

                        elif file_path.suffix == ".json":
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = json.dumps(json.load(infile), indent=4)
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".csv":
                            with file_path.open("r", encoding="utf-8") as infile:
                                reader = csv.reader(infile)
                                content = "\n".join([", ".join(row) for row in reader])
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".xml":
                            try:
                                tree = ET.parse(file_path)
                                root_element = tree.getroot()  # Корневой элемент дерева XML
                                content = ET.tostring(root_element, encoding="unicode", method="xml")
                                outfile.write(f"--- {filename} ---\n{content}\n\n")
                            except ET.ParseError as ex:
                                logger.error(f"Error parsing XML file {file_path=}: {ex}", exc_info=False)

                        elif file_path.suffix in [".xls", ".xlsx"]:
                            df = pd.read_excel(file_path, sheet_name=None)
                            content = "\n\n".join(df[sheet].to_string() for sheet in df)
                            outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".ipynb":
                            with file_path.open("r", encoding="utf-8") as infile:
                                notebook = json.load(infile)
                                content = json.dumps(notebook, indent=4)
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix in [".yaml", ".yml"]:
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = yaml.safe_load(infile)
                                content = yaml.dump(content, allow_unicode=True)
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".tex":
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".ini":
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".rdf":
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix == ".toml":
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

                        elif file_path.suffix in [".sqlite", ".db"]:
                            conn = sqlite3.connect(file_path)
                            cursor = conn.cursor()
                            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                            tables = cursor.fetchall()
                            content = ""
                            for table_name in tables:
                                table_name = table_name[0]
                                content += f"--- Table: {table_name} ---\n"
                                cursor.execute(f"SELECT * FROM {table_name};")
                                rows = cursor.fetchall()
                                columns = [description[0] for description in cursor.description]
                                content += f"{', '.join(columns)}\n"
                                content += "\n".join([", ".join(map(str, row)) for row in rows])
                                content += "\n\n"
                            conn.close()
                            outfile.write(content)

                    except (OSError, IOError, ValueError) as ex:
                        logger.error(f"Error processing file {file_path=}", ex, exc_info=False)

if __name__ == "__main__":
    # Указываем каталог для поиска и файл для сохранения вывода
    directory_to_search = "../data/chat_gpt/code2file"
    output_file_path = Path("../data/chat_gpt/code2file/code2file.txt")

    # Создаем директорию, если она не существует
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Создаем файл, если его не существует
    output_file_path.touch(exist_ok=True)

    read_text_files(directory_to_search, output_file_path, remove_docs=True)
