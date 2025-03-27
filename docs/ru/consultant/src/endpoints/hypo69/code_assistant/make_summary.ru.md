# Анализ кода модуля `make_summary`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошее описание модуля и его назначения.
    - Понятные инструкции по установке и использованию.
    - Примеры вывода для разных языков.
- **Минусы**:
    - Отсутствует код модуля, что не позволяет оценить его соответствие стандартам написания кода и наличия ошибок
    - Не хватает описания структуры проекта.
    - Нет явного указания на использование библиотек для работы с путями (например, `pathlib`).
    - Не хватает информации об обработке возможных исключений.
    - Комментарии не соответствуют стандарту RST.

## Рекомендации по улучшению:
- Добавить код модуля и провести его рефакторинг в соответствии с требованиями к заданию.
- Добавить описание структуры проекта, включая описание файлов и директорий.
- В коде использовать `pathlib` для работы с путями для обеспечения кроссплатформенности.
- Добавить обработку возможных исключений, используя `logger.error`.
- Заменить обычные комментарии на комментарии в формате RST для всех функций и классов.
- Уточнить и унифицировать формат примеров кода.
-  Проверить и исправить все ошибки, выявленные в процессе анализа кода.
-  В примере использования добавить обработку исключений.

## Оптимизированный код:
```python
"""
Модуль для автоматического создания файла `SUMMARY.md`
=======================================================

Модуль рекурсивно обходит указанную директорию с исходными файлами `.md`
и генерирует оглавление для `mdbook`, включая или исключая файлы в зависимости от указанного языка.

Пример использования
----------------------
.. code-block:: python

    python src/endpoints/hypo69/code_assistant/make_summary.py -lang ru src

"""
import argparse
from pathlib import Path
from src.utils.jjson import j_loads_ns # Импорт j_loads_ns
from src.logger import logger # Импорт logger
from typing import List

def create_summary_md(
    directory: Path,
    lang: str = 'ru'
) -> str:
    """
    Создает контент для файла SUMMARY.md на основе файлов в директории.

    :param directory: Путь к директории с исходными файлами .md.
    :type directory: Path
    :param lang: Язык для фильтрации файлов ('ru' или 'en'). По умолчанию 'ru'.
    :type lang: str
    :return: Строка с содержимым для файла SUMMARY.md.
    :rtype: str

    Пример:
        >>> create_summary_md(Path('src'), 'ru')
        '# Summary\\n\\n- [file1](file1.md)\\n- [file2](file2.ru.md)\\n'
    """
    summary_content = '# Summary\n\n'
    for item in sorted(directory.rglob('*.md')): #  Рекурсивный поиск md файлов.
        relative_path = item.relative_to(directory)
        if lang == 'ru' and not str(item).endswith('.ru.md'):
            continue
        if lang == 'en' and str(item).endswith('.ru.md'):
             continue
        summary_content += f'- [{item.stem}]({relative_path})\n' # Формируем строку для файла SUMMARY.md
    return summary_content

async def save_text_file(
        file_path: Path,
        data: str,
        mode: str = 'w'
) -> bool:
    """
    Асинхронно сохраняет данные в текстовый файл.

    :param file_path: Путь к файлу для сохранения.
    :type file_path: Path
    :param data: Данные для записи.
    :type data: str
    :param mode: Режим записи ('w' для записи, 'a' для добавления).
    :type mode: str, optional
    :return: True, если файл успешно сохранён, иначе False.
    :rtype: bool
    :raises Exception: В случае ошибки при записи в файл.

    Пример:
        >>> import asyncio
        >>> asyncio.run(save_text_file(Path('example.txt'), 'Пример текста'))
        True
    """
    try:
        with open(file_path, mode, encoding='utf-8') as file: # Открываем файл в режиме mode
            file.write(data) # Записываем данные в файл
        return True
    except Exception as e: # Перехватываем ошибку и логируем её
        logger.error(f"Ошибка при записи в файл {file_path}: {e}")
        return False
        
def main():
    """
    Главная функция для обработки аргументов командной строки и создания файла SUMMARY.md.
    """
    parser = argparse.ArgumentParser(description='Генерация SUMMARY.md для mdbook.') # Описание парсера
    parser.add_argument('-lang', type=str, default='ru', choices=['ru', 'en'],
                        help='Язык для фильтрации файлов (ru или en).') # Аргумент для выбора языка
    parser.add_argument('directory', type=str, help='Директория с исходными .md файлами.') # Аргумент для указания директории
    args = parser.parse_args() # Парсим аргументы

    try:
        directory_path = Path(args.directory) # Создаем объект Path
        if not directory_path.is_dir(): # Проверяем, является ли путь директорией
            logger.error(f"Директория '{args.directory}' не найдена.")
            return
    except Exception as e:
            logger.error(f"Неверный путь к директории: {e}")
            return

    summary_content = create_summary_md(directory_path, args.lang) # Создаем контент для SUMMARY.md
    docs_dir = Path('docs') # Указываем директорию для сохранения
    docs_dir.mkdir(exist_ok=True) # Создаем директорию, если она не существует

    summary_file = docs_dir / 'SUMMARY.md' # Указываем файл
    import asyncio # Импортируем asyncio
    if not asyncio.run(save_text_file(summary_file, summary_content)): # Сохраняем контент в файл
        logger.error(f"Не удалось сохранить файл {summary_file}")

if __name__ == '__main__':
    main()