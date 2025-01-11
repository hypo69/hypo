from pathlib import Path

def remove_md_suffix_recursively(directory):
    # Преобразуем путь в объект Path
    directory_path = Path(directory)
    
    # Проходим рекурсивно по всем файлам
    for file_path in directory_path.rglob('*'):
        # Проверяем, является ли объект файлом и заканчивается ли он на '.md'
        if file_path.is_file() and file_path.suffix == '.md' and len(file_path.suffixes) > 1:
            # Убираем только последний '.md'
            new_name = file_path.with_suffix('')
            # Переименовываем файл
            file_path.rename(new_name)
            print(f'Renamed: {file_path} -> {new_name}')

# Укажите путь к директории, которую нужно обработать
directory_path = "/path/to/your/directory"
remove_md_suffix_recursively(directory_path)
