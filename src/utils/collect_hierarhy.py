## \file src/utils/collect_hierarhy.py
"""! This script recursively traverses the 'src' directory, collects the file hierarchy, and saves it as a JSON file, excluding specific directories and files, and including only .py, .json, .md, .dot, and .mer files. It also copies the found files to the 'project_structure' directory, maintaining the hierarchy."""
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
