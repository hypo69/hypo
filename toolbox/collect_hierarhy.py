## \file /dev_utils/collect_hierarhy.py
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


"""Этот код выполняет следующую задачу:

1. **Описание функциональности**:
   - Скрипт рекурсивно проходит по папке `src/utils` и собирает иерархию файлов в словарь, включая только файлы с расширениями `.py`, `.json`, `.md`, `.dot`, и `.mer`.
   - Игнорируются папки `profiles`, `__pycache__`, `_experiments`, а также файлы и папки, названия которых начинаются с `___`, содержат `*`, `(`, или `)` в имени.
   - Все найденные файлы копируются в папку `prod`, при этом структура папок сохраняется.
   - После сбора иерархии файлов она сохраняется в файл `file_hierarchy.json` внутри папки `prod`.

2. **Функции**:
   - `collect_and_copy_files`: 
      - Рекурсивно проходит по каждому элементу в директории. Если элемент — папка, то вызывается рекурсия для обработки её содержимого, и создаётся поддиректория в целевом каталоге.
      - Если элемент — файл подходящего типа, он копируется в целевой каталог (`target_directory`) с сохранением структуры. 
      - Возвращает словарь с иерархией файлов, где ключами являются имена файлов и папок.
   
   - `main`:
      - Устанавливает начальную папку `src/utils` для поиска (`src_directory`) и создаёт папку `prod` для сохранения результатов.
      - Вызывает `collect_and_copy_files` для сбора структуры файлов и записывает её в `file_hierarchy.json` с использованием функции `j_dumps`.

3. **Используемые библиотеки**:
   - `Path` из `pathlib` для работы с файловыми путями.
   - `copy2` из `shutil` для копирования файлов.
   - `j_dumps` из модуля `src.utils.jjson` для сохранения словаря с иерархией в формате JSON.

**Результат выполнения**: при запуске скрипт создаёт иерархию файлов `src/utils` в виде JSON-файла, и одновременно копирует все указанные файлы в папку `prod`."""
import header
from pathlib import Path
from shutil import copy2
from src.utils.jjson import j_dumps

def collect_and_copy_files(directory: Path, target_directory: Path) -> dict:
    hierarchy = {}
    for item in directory.iterdir():
        if item.is_dir():
            if item.name not in ['profiles', '__pycache__', '_experiments'] and not item.name.startswith('___') and '*' not in item.name:
                hierarchy[item.name] = collect_and_copy_files(item, target_directory / item.name)
        else:
            if (item.suffix in ['.py', '.json', '.md', '.dot', '.mer']) and not item.name.startswith('___') and '*' not in item.name and '(' not in item.name and ')' not in item.name:
                hierarchy[item.name] = None
                target_file_path = target_directory / item.name
                target_file_path.parent.mkdir(parents=True, exist_ok=True)
                copy2(item, target_file_path)
    return hierarchy

def main():
    src_directory = Path(header.__root__ , 'src' , 'utils')
    project_structure_directory = Path(src_directory , 'prod')  # Создаем папку 'prod'
    file_hierarchy = collect_and_copy_files(src_directory, project_structure_directory)
    json_output_path = Path(project_structure_directory, 'file_hierarchy.json')
    j_dumps(file_hierarchy, json_output_path)

if __name__ == "__main__":
    main()
