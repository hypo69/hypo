from pathlib import Path

import header
from src import gs

# Путь к директории с файлами .md
src_path = Path(gs.path.root / 'docs' / 'gemini' / 'consultant' / 'ru' / 'src')

# Путь для сохранения SUMMARY.md
summary_path = src_path / 'SUMMARY.md'

def make_summary(src_dir: Path = src_path , summary_file: Path = summary_path) -> None:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.
    Если файл SUMMARY.md уже существует, он будет перезаписан.

    Args:
        src_dir (Path): Путь к папке с исходниками .md.
        summary_file (Path): Путь для сохранения файла SUMMARY.md.
    
    How to use:
    -----------------------
    1. Убедитесь, что у вас есть папка с .md файлами (например, 'docs/gemini/consultant/ru/src').
    2. Убедитесь, что модуль `gs` правильно настроен для получения пути корневой директории.
    3. Запустите скрипт. Он автоматически создаст файл `SUMMARY.md` в указанной папке.
    4. Файл `SUMMARY.md` будет содержать список всех `.md` файлов в директории, структурированный в виде глав с вложениями.
    """

    # Проверяем, существует ли файл, если нет - создаем его
    if not summary_file.exists():
        print(f'Файл {summary_file} не существует. Создаем новый.')
    else:
        print(f'Файл {summary_file} уже существует. Его содержимое будет перезаписано.')

    # Открываем файл для записи
    with summary_file.open('w', encoding='utf-8') as summary:
        summary.write('# Summary\n\n')  # Заголовок для файла

        # Рекурсивно обходим все .md файлы в директории
        for path in sorted(src_dir.rglob('*.md')):
            if path.name == 'SUMMARY.md':  # Пропускаем сам файл SUMMARY.md
                continue

            # Формируем относительный путь и название главы
            rel_path = path.relative_to(src_dir).as_posix()  # Относительный путь для ссылки
            chapter_name = path.stem.replace('_', ' ').capitalize()  # Преобразуем название в читаемый формат

            # Определяем уровень вложенности, чтобы правильно оформить отступы
            indent = '  ' * rel_path.count('/')
            # Записываем главу в файл SUMMARY.md
            summary.write(f'{indent}- [{chapter_name}]({rel_path})\n')

    print(f'Файл SUMMARY.md успешно создан/перезаписан: {summary_file}')

# Выполнение скрипта
make_summary(src_path, summary_path)
