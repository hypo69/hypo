## \file hypotez/src/endpoints/hypo69/onela_bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.hypo69 """

""" Отсылатель кода в модель gemini
https://stackoverflow.com/questions/78382534/googlegenerativeaierror-error-embedding-contentmodels-embeddings-001-is-not-fo
"""

import re
from pathlib import Path
import time
import argparse
from typing import Iterator

from __init__ import gs
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import yield_files_content, read_text_file
from src.logger import logger

# Глобальная переменная для роли
role: str = None


generation_config: dict = {"response_mime_type": "text/plain"}
model_name: str = "gemini-1.5-flash-8b"
model: GoogleGenerativeAI 


def parse_args() -> None:
    """! Парсинг аргументов командной строки для задания роли.

    Присваивает значение глобальной переменной `role` на основе переданного ключа `--role`.
    """
    global role
    parser = argparse.ArgumentParser(description="Запуск onela_bot с указанием роли")
    parser.add_argument("--role", type=str, required=True, help="Укажите роль (например, code_checker)")
    args = parser.parse_args()
    role = args.role


def main() -> None:
    """! Main function to process files and interact with the model.

    This function reads a comment file, iterates over specified files in the source directory,
    and sends the file content to a model for analysis. It then processes the model's response.
    """
    global model

    # Проверка наличия роли
    if not role:
        logger.error("Роль не указана. Используйте ключ --role для задания роли.")
        return
    if role == 'code_checker':
        comment_for_model_about_piece_of_code = 'code_checker.md'
        system_instruction: str = "improve_code.md"
    if role == 'doc_creator':
        comment_for_model_about_piece_of_code = 'code_checker.md'
        system_instruction: str = 'create_documentation.md'

    # Read the comment for model input from a markdown file
    comment_for_model_about_piece_of_code: str = read_text_file(
        gs.path.src / 'endpoints' / 'hypo69' / 'onela_bot' / 'instructions' / comment_for_model_about_piece_of_code
    )
    system_instruction: str = read_text_file(gs.path.src / "ai" / "prompts" / "developer" / system_instruction)

    model = GoogleGenerativeAI(
    api_key=gs.credentials.gemini.onela,
    model_name=model_name,
    system_instruction=system_instruction,
    generation_config=generation_config,
    )
    # Process each file based on the specified patterns
    for file_path, content in yield_files_content(
        gs.path.src, ["*.py"]
    ):
        # Construct the input content for the model
        content: str = (
            f"{comment_for_model_about_piece_of_code}\n"
            f"Расположение файла в проекте: `{file_path}`.\n"
            f"Роль выполнения: `{role}`.\n"
            "Код:\n\n"
            f"```{content}```\n"
        )
        try:
            # Get the response from the model
            response = model.ask(content)

            # Save the model's response, changing the file suffix to `.md`
            save_response(file_path, response)
        except Exception as ex:
            logger.error(ex)
            ...
        # Optional sleep to prevent API rate limits or throttling
        time.sleep(20)

def save_response(file_path: Path, response: str) -> None:
    """! Save the model's response to a markdown file with updated path based on role.

    Args:
        file_path (Path): The original file path being processed.
        response (str): The response from the model to be saved.

    This function modifies the original file path's suffix to `.md` and saves the response as a markdown file.
    The path where the file is saved depends on the current role.
    """
    global role

    # Словарь, ассоциирующий роли с директориями
    role_directories = {
        'doc_creator': 'docs/raw_rst_from_ai',
        'code_checker': 'gemini_consultant',
        # Добавьте другие роли и их директории по мере необходимости
    }

    # Проверка наличия роли в словаре
    if role not in role_directories:
        logger.error(f"Неизвестная роль: {role}. Файл не будет сохранен.")
        return

    # Получаем директорию, соответствующую роли
    role_directory = role_directories[role]

    # Формируем новый путь с учетом роли
    export_file_path = file_path.parts
    new_parts = []

    for part in export_file_path:
        if part == 'src':
            new_parts.append(role_directory)
        else:
            new_parts.append(part)

    # Сформировать новый путь с замененной частью
    export_file_path = Path(*new_parts)

    # Изменить суффикс файла на .md
    export_file_path = export_file_path.with_suffix(".md")

    # Убедиться, что директория существует
    export_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Сохранить ответ в новый файл
    export_file_path.write_text(response, encoding="utf-8")
    print(f"Response saved to: {export_file_path}")

def yield_files_content(
    src_path: Path, patterns: list[str]
) -> Iterator[tuple[Path, str]]:
    """! Yield file content based on patterns from the source directory, excluding certain patterns and directories.

    Args:
        src_path (Path): The base directory to search for files.
        patterns (list[str]): List of file patterns to include (e.g., ['*.py', '*.txt']).

    Yields:
        Iterator[tuple[Path, str]]: A tuple of file path and its content as a string.
    """
    # Регулярные выражения для исключаемых файлов
    exclude_file_patterns = [
        re.compile(r'.*\(.*\).*'),  # Файлы с круглыми скобками
        re.compile(r'___.*\..*'),   # Файлы, начинающиеся с трех подчеркиваний
    ]

    # Список служебных директорий, которые необходимо исключить
    exclude_dirs = {'.ipynb_checkpoints', '_experiments', '__pycache__', '.git', '.venv'}

    for pattern in patterns:
        for file_path in src_path.rglob(pattern):
            # Пропустить файлы, которые находятся в исключаемых директориях
            if any(exclude_dir in file_path.parts for exclude_dir in exclude_dirs):
                continue

            # Пропустить файлы, соответствующие исключаемым паттернам
            if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                continue

            # Чтение содержимого файла
            content = file_path.read_text(encoding="utf-8")
            yield file_path, content


if __name__ == "__main__":
    print("Starting training ...")
    parse_args()  # Парсим аргументы командной строки
    main()
