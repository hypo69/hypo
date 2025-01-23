## \file /dev_utils/update_files_headers.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module: dev_utils 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""

Описание:
Скрипт предназначен для обработки Python файлов в проекте "hypotez" с целью добавления или замены 
заголовков, строк интерпретаторов и строк документации. Он выполняет обход всех файлов в проекте и 
при необходимости обновляет их, добавляя информацию о проекте, интерпретаторе и метаданных.

Скрипт позволяет:
- Идентифицировать корневую папку проекта
- Найти и добавить строку кодировки
- Добавить строки с интерпретатором для Windows и Linux
- Добавить строку документации для модуля
- Установить значение режима работы проекта
- Очистить заголовочные строки

Примеры запуска:

1. Стандартный запуск:
   python update_files_headers.py

2. Принудительное обновление файлов:
   python update_files_headers.py --force-update

3. Очистка заголовков:
   python update_files_headers.py --clean
"""

from csv import QUOTE_STRINGS
import os
import argparse
from pathlib import Path
import sys
import platform

PROJECT_ROOT_FOLDER = os.path.abspath('..')
EXCLUDE_DIRS = ['venv', 'tmp', 'docs', 'data', '__pycache__','.ipynb_checkpoints']

def find_project_root(start_path: Path, project_root_folder: str) -> Path:
    """Find the project root directory by searching for the specified folder."""
    current_path = start_path
    while current_path != current_path.parent:
        if (current_path / project_root_folder).exists():
            return current_path / project_root_folder
        current_path = current_path.parent
    raise FileNotFoundError(f"Project root folder '{project_root_folder}' not found.")

def get_interpreter_paths(project_root: Path) -> tuple:
    """Returns paths to Python interpreters for Windows and Linux/macOS."""
    w_venv_interpreter = fr'venv/Scripts/python.exe'
    linux_venv_interpreter = fr'venv/bin/python/python3.12'
    return w_venv_interpreter, 'py', linux_venv_interpreter, '/usr/bin/python'

def add_or_replace_file_header(file_path: str, project_root: Path, force_update: bool):
    """Adds or replaces header, interpreter lines, and module docstring."""
    relative_path = Path(file_path).resolve().relative_to(project_root)
    header_line = f'## \\file hypotez/{relative_path.as_posix()}\n'
    coding_index = '# -*- coding: utf-8 -*-\n'
    w_venv_interpreter, _, linux_venv_interpreter, _ = get_interpreter_paths(project_root)
    w_venv_interpreter_line = f'#! {w_venv_interpreter}\n'
    linux_venv_interpreter_line = f'#! {linux_venv_interpreter}\n'
    docstring_module = f'.. module: {relative_path.parent.as_posix().replace("/", ".")} \n'
    docstring_platform = '\t:platform: Windows, Unix\n'
    docstring_synopsis = '\t:synopsis:\n'
    triple_quote = '\n"""\n'
    mode_line = "MODE = 'development'\n"

    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            cleaned_lines = [line.lstrip('\ufeff') for line in lines]
            filtered_lines = [
                line for line in cleaned_lines if not (
                    line.startswith("## \\file") or
                    line.startswith("# -*- coding") or
                    line.startswith("#!") or
                    line.strip().startswith('"""module:') or 
                    line.strip().startswith('""".. module:') or
                    line.strip().startswith('module:') or
                    line.strip().startswith('.. module:') or
                    line.strip().startswith('    :platform:') or
                    line.strip().startswith('    :synopsis:') or                    
                    line.strip().startswith('\t:platform:') or
                    line.strip().startswith('\t:synopsis:') or
                    line.strip().startswith('MODE =')
                )
            ]

            # Проверка необходимости обновления
            needs_update = force_update or any(
                not any(line.strip() == check_line.strip() for line in filtered_lines)
                for check_line in [
                    header_line,
                    coding_index,
                    w_venv_interpreter_line,
                    linux_venv_interpreter_line,
                    docstring_module,
                    docstring_platform,
                    docstring_synopsis,
                    mode_line
                ]
            )

            if needs_update:
                new_lines = [
                    header_line,
                    coding_index,
                    w_venv_interpreter_line,
                    linux_venv_interpreter_line,
                    triple_quote,
                    docstring_module,
                    docstring_platform,
                    docstring_synopsis,
                    triple_quote,
                    mode_line
                ]
                file.seek(0)
                file.writelines(new_lines + filtered_lines)
                file.truncate()
                print(f"Updated {file_path}")
            else:
                print(f"No updates necessary for {file_path}")

    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")

def clean(file_path: str):
    """Removes specified header lines from the file and replaces them with empty lines."""
    header_prefix = '## \\file'
    coding_prefix = '# -*- coding'
    interpreter_prefix = '#!'
    docstring_module_1 = '.. module::'
    docstring_module_2 = 'module:'
    docstring_module_3 = '""".. module:'
    docstring_module_3 = '"""module:'
    docstring_platform = '  :platform:'
    docstring_synopsis = '  :synopsis:'
    mode_str = "MODE = "

    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            cleaned_lines = [line.lstrip('\ufeff') for line in lines]
            filtered_lines = [
                '' if (
                    line.startswith(header_prefix) or
                    line.startswith(coding_prefix) or
                    line.startswith(interpreter_prefix) or
                    line.strip().startswith(docstring_module_1) or 
                    line.strip().startswith(docstring_module_2) or
                    line.strip().startswith(docstring_module_3) or
                    line.strip().startswith(docstring_platform) or
                    line.strip().startswith(docstring_synopsis) or
                    line.strip().startswith('MODE = ')
                ) else line
                for line in cleaned_lines
            ]
            file.seek(0)
            file.writelines(filtered_lines)
            file.truncate()
            print(f"Cleaned {file_path}")
    except IOError as ex:
        print(f"Error cleaning file \n{file_path}:\n {ex}")


def traverse_and_update(directory: Path, force_update: bool):
    """Traverses the directory and updates headers in Python files."""
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith('.py'):
                add_or_replace_file_header(os.path.join(root, file), directory, force_update)

def traverse_and_clean(directory: Path):
    """Traverses the directory and cleans specified headers from Python files."""
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            # if file.endswith(('.py', '.txt', '.md', '.js', '.dot', '.ps1')):
            if file.endswith(('.py')):
                clean(os.path.join(root, file))


def main():
    """Main function to execute the script."""
    # parser = argparse.ArgumentParser(description="Process Python files in the 'hypotez' project.")
    # parser.add_argument('--force-update', action='store_true', help="Force update the headers even if they already match.")
    # parser.add_argument('--clean', action='store_true', help="Clean specified headers from Python files.")
    # parser.add_argument('-p', '--project', type=Path, default=Path(os.getcwd()), help="Path to the project root folder.")
    # args = parser.parse_args()

    # try:
    #     project_root = find_project_root(args.project, PROJECT_ROOT_FOLDER)
    #     if args.clean:
    #         traverse_and_clean(project_root)
    #     else:
    #         traverse_and_update(project_root, args.force_update)
    # except FileNotFoundError as ex:
    #     print(f"Error: {ex}")
    
    ## CLEAN LINES
    # traverse_and_clean(PROJECT_ROOT_FOLDER)
    traverse_and_update(PROJECT_ROOT_FOLDER, True)

if __name__ == '__main__':
    main()
