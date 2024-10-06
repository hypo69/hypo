"""! This script recursively traverses the 'src' directory, collects the file hierarchy, 
and saves it as a JSON file, excluding specific directories and files, and including only .py, .json, .md, .dot, and .mer files."""
import header
from pathlib import Path
from src.utils.jjson import j_dumps

def collect_file_hierarchy(directory: Path) -> dict:
    hierarchy = {}
    for item in directory.iterdir():
        if item.is_dir():
            if item.name not in ['profiles', '__pycache__', '_experiments'] and not item.name.startswith('___') and '*' not in item.name:
                hierarchy[item.name] = collect_file_hierarchy(item)
        else:
            if (item.suffix in ['.py', '.json', '.md', '.dot', '.mer']) and not item.name.startswith('___') and '*' not in item.name and '(' not in item.name and ')' not in item.name:
                hierarchy[item.name] = None
    return hierarchy

def main():
    src_directory = Path('..','tmp','aliexpress')
    file_hierarchy = collect_file_hierarchy(src_directory)
    json_output_path = Path('file_hierarchy.json')
    j_dumps(file_hierarchy, json_output_path)

if __name__ == "__main__":
    main()
