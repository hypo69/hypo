## \file hypotez/dev_utils/update_files_headers.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: dev_utils """

import os
import argparse
from pathlib import Path
import sys
import platform

PROJECT_ROOT_FOLDER = 'hypotez'

EXCLUDE_DIRS = ['venv', 'tmp', 'docs', 'data', '__pycache__']  # Добавим дополнительные папки для исключения

def find_project_root(start_path: Path, project_root_folder: str) -> Path:
    """Find the project root directory by searching for the specified folder."""
    current_path = start_path
    while current_path != current_path.parent:
        if (current_path / project_root_folder).exists():
            return current_path / project_root_folder
        current_path = current_path.parent
    raise FileNotFoundError(f"Project root folder '{project_root_folder}' not found.")

def get_interpreter_paths(project_root: Path) -> tuple:
    """Returns paths to all relevant Python interpreters for both Windows and Linux/macOS.

    Args:
        project_root (Path): The root directory of the project (contains the virtual environment).
    
    Returns:
        tuple: A tuple with paths to the Python interpreter for Windows (venv and system) and Linux/macOS (venv and system).
    """

    # Пути для Windows
    # w_venv_interpreter = project_root / 'venv' / 'Scripts' / 'python.exe'
    w_venv_interpreter = fr'venv/Scripts/python.exe'
    w_system_interpreter = fr'py'
    
    # Пути для Linux/macOS
    # linux_venv_interpreter = project_root / 'venv' / 'bin' / 'python'
    linux_venv_interpreter = fr'venv/bin/python'
    linux_system_interpreter = fr'/usr/bin/python'
    
    return (
        str(w_venv_interpreter), str(w_system_interpreter),
        str(linux_venv_interpreter), str(linux_system_interpreter)
    )

def add_or_replace_file_header(file_path: str, project_root: Path, force_update: bool):
    """Adds or replaces a header, interpreter lines, and module docstring in the specified Python file.

    Args:
        file_path (str): Path to the Python file being processed.
        project_root (Path): The root directory of the project.
        force_update (bool): If True, forces update even if headers already exist.
    """
    # Определяем относительный путь от корня проекта
    relative_path = Path(file_path).resolve().relative_to(project_root)
    header_line = f'## \\file hypotez/{relative_path.as_posix()}\n'
    coding_index = '# -*- coding: utf-8 -*-\n'
    
    # Получаем пути к интерпретаторам
    w_venv_interpreter, w_system_interpreter, linux_venv_interpreter, linux_system_interpreter = get_interpreter_paths(project_root)
    
    # Формируем строки для интерпретаторов
    w_venv_interpreter_line = f'#! {w_venv_interpreter} # <- venv win\n'
    w_system_interpreter_line = f'#! {w_system_interpreter} # <- system win\n'
    linux_venv_interpreter_line = f'#! {linux_venv_interpreter} # <- venv linux/macos\n'
    linux_system_interpreter_line = f'#! {linux_system_interpreter} # <- system linux/macos\n'
    closing_line = '## ~~~~~~~~~~~~~\n'
    
    # Создаем строку документации модуля и заменяем символы `/` на `.`
    module_path = relative_path.parent.as_posix().replace('/', '.')
    module_docstring = f'""" module: {module_path} """\n'

    print(f"Processing file: {file_path}")

    try:
        with open(file_path, 'r+', encoding='utf-8', newline='') as file:
            lines = file.readlines()

            # Удаляем BOM и ненужные строки заголовка, кодировки и интерпретатора
            cleaned_lines = [line.lstrip('\ufeff') for line in lines]  # Удаление BOM
            filtered_lines = [
                line for line in cleaned_lines
                if not (line.startswith("## \\file")
                        or line.startswith("# -*- coding")
                        or line.startswith("#!")
                        or line.startswith("## ~~~~~~~~~~~~~")
                        or line.strip().startswith('""" module:'))
            ]

            # Проверка необходимости обновления
            header_needs_update = not any(line == header_line for line in filtered_lines)
            coding_needs_update = not any(line == coding_index for line in filtered_lines)
            venv_interpreter_needs_update = not any(line == w_venv_interpreter_line or line == linux_venv_interpreter_line for line in filtered_lines)
            system_interpreter_needs_update = not any(line == w_system_interpreter_line or line == linux_system_interpreter_line for line in filtered_lines)
            closing_needs_update = not any(line == closing_line for line in filtered_lines)
            module_docstring_needs_update = not any(line.strip() == module_docstring.strip() for line in filtered_lines)

            # Если force_update включен, всегда обновляем
            if force_update:
                header_needs_update = True
                coding_needs_update = True
                venv_interpreter_needs_update = True
                system_interpreter_needs_update = True
                closing_needs_update = True
                module_docstring_needs_update = True

            # Добавляем новые строки заголовка, если это необходимо
            new_lines = []
            if header_needs_update:
                new_lines.append(header_line)
            if coding_needs_update:
                new_lines.append(coding_index)
            if venv_interpreter_needs_update:
                new_lines.append(w_venv_interpreter_line)
                #new_lines.append(linux_venv_interpreter_line)
            if system_interpreter_needs_update:
                # new_lines.append(w_system_interpreter_line)
                # new_lines.append(linux_system_interpreter_line)
                ...
            if closing_needs_update:
                new_lines.append(closing_line)
            if module_docstring_needs_update:
                new_lines.append(module_docstring)

            # Запись изменений в файл
            if new_lines:
                file.seek(0)  # Перемещаем указатель в начало файла
                file.writelines(new_lines + filtered_lines)  # Записываем новые строки и оставшиеся строки файла
                file.truncate()  # Обрезаем файл после добавленных строк
                print(f"Updated {file_path} successfully.")
            else:
                print(f"No updates necessary for {file_path}.")

    except IOError as ex:
        print(f"Error processing file {file_path}: {ex}")


def traverse_and_update(directory: Path, force_update: bool, exclude_venv: bool):
    """Traverses downwards from the given directory ('hypotez') and processes Python files."""
    print(f"Traversing directory: {directory}")

    for root, dirs, files in os.walk(directory):
        # Исключаем папки из EXCLUDE_DIRS
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_or_replace_file_header(file_path, directory, force_update)

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(description="Process Python files in the 'hypotez' project.")
    parser.add_argument('--force-update', action='store_true', help="Force update the headers and interpreter lines even if they already match.")
    parser.add_argument('-p', '--project-dir', type=str, help="Path to the project directory.")
    parser.add_argument('--exclude-venv', action='store_true', default=True, help="Exclude 'venv' directory from processing. Default is True.")

    args = parser.parse_args()

    # Преобразуем путь к проекту в объект Path
    if args.project_dir:
        project_dir = Path(args.project_dir).resolve()
    else:
        # Если проектная директория не указана, ищем проект выше
        try:
            project_dir = find_project_root(Path(__file__).parent, PROJECT_ROOT_FOLDER)
        except FileNotFoundError as ex:
            print(ex)
            return

    # Проверка существования директории проекта
    if not project_dir.exists():
        print(f"Error: The specified project directory does not exist: {project_dir}")
        return

    print(f"Starting downward traversal from: {project_dir}")
    traverse_and_update(project_dir, args.force_update, args.exclude_venv)


if __name__ == "__main__":
    main()
