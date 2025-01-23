## \file /dev_utils/code2file_for_chat_gpt_but_comments.py
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
из файлов Python, если это указано, но в этой версии все комментарии и докстринги сохраняются.

Функции:
- clean_html: Удаляет HTML-теги из содержимого.
- delete_directory_contents: Рекурсивно удаляет все содержимое указанной директории.
- read_text_files: Читает все указанные файлы в каталоге и сохраняет объединенный текст в один файл.

Примеры:
read_text_files('../temp/chat_gpt', 'output.txt')
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
from src.logger import logger

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
    directory: str, output_file: str
) -> None:
    """ Читает все указанные текстовые и данные файлы в каталоге и сохраняет объединенный текст в один файл,
    одновременно удаляя файлы и директории, которые начинаются с `_` или содержат `(` и `)`.

    Args:
        directory (str): Каталог для поиска файлов.
        output_file (str): Файл, в который будет сохранен объединенный текст.

    Returns:
        None

    Пример:
        >>> read_text_files('src', 'output.txt')
    """
    output_path = Path(output_file)
    output_path.touch(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(directory, topdown=False):
            # Удаляем файлы и директории, соответствующие условиям
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                if dir_name.startswith("_") or "*" in dir_name:
                    delete_directory_contents(dir_path)

            for filename in files:
                file_path = Path(root) / filename
                if filename.startswith("_") or ("(" in filename and ")" in filename):
                    try:
                        file_path.unlink()
                        logger.info(f"Deleted file: {file_path}")
                    except OSError as ex:
                        logger.error(f"Error deleting file {file_path=}", ex, exc_info=False)
                else:
                    # Обработка файлов, которые не подлежат удалению
                    try:
                        if file_path.suffix in [
                            ".py", ".txt", ".css", ".js", ".dot", ".mer", ".md", ".ps1"
                        ]:
                            with file_path.open("r", encoding="utf-8") as infile:
                                content = infile.read()
                                outfile.write(f"--- {filename} ---\n{content}\n\n")

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
                            tree = ET.parse(file_path)
                            root = tree.getroot()
                            content = ET.tostring(root, encoding="unicode", method="xml")
                            outfile.write(f"--- {filename} ---\n{content}\n\n")

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
    directory_to_search = "../src/suppliers/kazarinov/react"
    output_file_path = Path("../data/kazarinov_react.txt")

    # Создаем директорию, если она не существует
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Создаем файл, если его не существует
    output_file_path.touch(exist_ok=True)

    read_text_files(directory_to_search, output_file_path)
