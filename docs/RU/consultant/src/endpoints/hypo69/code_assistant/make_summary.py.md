# Анализ кода модуля `make_summary`

**Качество кода**
9
-  Плюсы
    -   Код хорошо структурирован, с разделением на функции для разных задач.
    -   Используется `pathlib` для работы с путями, что является хорошей практикой.
    -   Присутствует фильтрация файлов по языку.
    -   Есть возможность указать путь к директории через аргументы командной строки.
    -   Код соответствует PEP 8.
-  Минусы
    -   Отсутствует обработка ошибок через логирование, вместо этого используется `print`, что затрудняет отладку.
    -   Нет документации в формате RST.
    -   Отсутствует импорт `logger` из `src.logger`.
    -   Не используются `j_loads` и `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  **Логирование:** Заменить `print` на `logger.error` для более удобного отслеживания ошибок и предупреждений.
2.  **Документация:** Добавить документацию в формате RST ко всем функциям, методам и модулю.
3.  **Импорты:** Добавить отсутствующие импорты, такие как `logger` из `src.logger`.
4.  **Обработка ошибок:**  Улучшить обработку ошибок, используя `logger.error`.
5. **Соответствие стандартам:** Использовать одинарные кавычки в коде.
6. **Улучшение обработки файлов:** Использовать `j_loads` и `j_loads_ns` при работе с файлами, если это необходимо.
7.  **Проверка существования пути:**  Убедиться в существовании директории `src_dir`.
8. **Упрощение кода:**  Сделать код более читаемым и лаконичным.

**Оптимизированный код**

```python
"""
Модуль для создания файла SUMMARY.md для mdbook
=========================================================================================

Этот модуль создает файл `SUMMARY.md`, который используется для
структурирования документации в формате mdbook. Он рекурсивно обходит
указанную директорию, собирая все файлы `.md` и формируя из них
содержание в формате, понятном для mdbook.

Пример использования
--------------------

Пример вызова модуля из командной строки:

.. code-block:: bash

    python make_summary.py -lang ru src/my_docs_folder
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

from pathlib import Path
import argparse
from src.logger import logger  # Импортируем logger
import header  # Импорт модуля, который определяет корневой путь проекта

# Используем корневой путь проекта
PROJECT_ROOT = header.__root__

def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    Args:
        docs_dir (Path): Путь к исходной директории `src`.
        lang (str, optional): Язык фильтрации файлов. Возможные значения: `ru` или `en`. Defaults to 'en'.

    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    summary_file = prepare_summary_path(docs_dir)
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    _make_summary(docs_dir, summary_file, lang)


def _make_summary(src_dir: Path, summary_file: Path, lang: str = 'en') -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    Args:
        src_dir (Path): Путь к папке с исходниками .md.
        summary_file (Path): Путь для сохранения файла SUMMARY.md.
        lang (str, optional): Язык фильтрации файлов. Возможные значения: `ru` или `en`. Defaults to 'en'.

    Returns:
        bool: `True` если файл успешно создан, `False` в случае ошибки.
    """
    try:
        if summary_file.exists():
            logger.info(f'Файл {summary_file} уже существует. Его содержимое будет перезаписано.')

        with summary_file.open('w', encoding='utf-8') as summary:
            summary.write('# Summary\n\n')

            for path in sorted(src_dir.rglob('*.md')):
                if path.name == 'SUMMARY.md':
                    continue

                # Фильтрация файлов по языку
                if lang == 'ru' and not path.name.endswith('.ru.md'):
                    continue  # Пропускаем файлы без суффикса .ru.md
                elif lang == 'en' and path.name.endswith('.ru.md'):
                    continue  # Пропускаем файлы с суффиксом .ru.md

                relative_path = path.relative_to(src_dir.parent)
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        logger.error(f'Ошибка создания файла `summary.md`: {ex}') # Логируем ошибку
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути `src` на `docs` и добавляя имя файла.

    Args:
        src_dir (Path): Исходный путь с `src`.
        file_name (str, optional): Имя файла, который нужно создать. Defaults to 'SUMMARY.md'.

    Returns:
        Path: Новый путь к файлу.
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    new_dir = PROJECT_ROOT / 'docs'
    summary_file = new_dir / file_name
    return summary_file


if __name__ == '__main__':
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description='Создание файла SUMMARY.md с фильтрацией по языку.')
    parser.add_argument('-lang', type=str, choices=['ru', 'en'], default='en', help='Язык фильтрации файлов (ru или en). По умолчанию \'en\'.')
    parser.add_argument('src_dir', type=str, help='Путь к исходной директории `src`.')
    args = parser.parse_args()

    # Преобразование пути в объект Path
    src_dir = PROJECT_ROOT / args.src_dir

    # Проверка существования директории
    if not src_dir.exists():
        logger.error(f'Директория {src_dir} не существует.')
    else:
        # Вызов функции make_summary с переданными аргументами
        make_summary(src_dir, args.lang)
```