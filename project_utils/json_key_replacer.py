"""! заменяет ключи в файлах json """
import header
from pathlib import Path
from src.logger import logger
from src.utils import j_loads, j_dumps

def replace_key_in_json(data, old_key, new_key):
    """!
    Рекурсивно заменяет ключ в словаре или списке.
    @param data: Словарь или список, в котором происходит замена ключей.
    @param old_key: Ключ, который нужно заменить.
    @param new_key: Новый ключ.
    """
    if isinstance(data, dict):
        for key in list(data.keys()):
            if key == old_key:
                data[new_key] = data.pop(old_key)
            if isinstance(data[key], (dict, list)):
                replace_key_in_json(data[key], old_key, new_key)
    elif isinstance(data, list):
        for item in data:
            replace_key_in_json(item, old_key, new_key)

def process_json_file(json_file: Path):
    """!
    Обрабатывает JSON файл, заменяя ключ `name` на `category_name`.
    @param json_file: Путь к JSON файлу.
    """
    try:
        data = j_loads(json_file.read_text())
        replace_key_in_json(data, 'name', 'category_name')
        json_file.write_text(j_dumps(data))
    except Exception as ex:
        logger.error(f"Error processing file: {json_file}", ex)

def recursive_process_json_files(directory: Path):
    """!
    Рекурсивно обходит папки и обрабатывает JSON файлы.
    @param directory: Путь к директории, которую нужно обработать.
    """
    for path in directory.rglob('*.json'):
        if path.is_file():
            process_json_file(path)

# Пример использования
if __name__ == "__main__":
    root_directory = Path('../data/aliexpress/campaigns')
    recursive_process_json_files(root_directory)
