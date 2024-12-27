# Анализ кода модуля `make_summary`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на функции.
    - Используются `pathlib.Path` для работы с путями, что делает код более читаемым и безопасным.
    - Присутствует обработка аргументов командной строки.
    - Присутствует описание модуля и функций в формате docstring.
    - Присутствует разделение логики на несколько функций.
    - Код соблюдает PEP 8.
- Минусы
    - Используется стандартный `print` для вывода информации и ошибок, рекомендуется использовать `src.logger.logger` для логирования.
    - Отсутствует обработка специфичных ошибок при работе с файлами.
    - Нет явной проверки существования каталога `src_dir`.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, хотя это не требуется в данном коде.
    - Не производится обработка ошибки при создании директории через `parents=True, exist_ok=True`, не производится логирование.

**Рекомендации по улучшению**

1.  **Логирование**: Замените `print` на `logger.info`, `logger.debug` и `logger.error` из `src.logger.logger`.
2.  **Обработка ошибок**: Добавьте более специфичную обработку исключений при работе с файловой системой, особенно при создании директорий и открытии/записи файлов.
3.  **Проверка существования директории**: Проверьте, существует ли `src_dir`, перед началом работы.
4.  **Сохранение комментариев**: Убедитесь, что все существующие комментарии после `#` сохранены без изменений.
5.  **Соответствие именам**: Убедитесь, что имена функций и переменных соответствуют соглашениям.
6.  **Документация**: Улучшите docstring, добавив более конкретные описания.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для создания файла SUMMARY.md для mdbook.
=========================================================================================

Этот модуль предоставляет функции для автоматического создания файла `SUMMARY.md`,
необходимого для mdbook, путем рекурсивного обхода указанной директории и
фильтрации файлов по языку.

Пример использования
--------------------

Пример вызова функции make_summary из командной строки:

.. code-block:: bash

    python make_summary.py -lang ru src/path/to/docs

"""
from pathlib import Path
import argparse
from src.logger.logger import logger
import header  # Импорт модуля, который определяет корневой путь проекта

# Используем корневой путь проекта
PROJECT_ROOT = header.__root__

def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    :param docs_dir: Путь к исходной директории 'src'.
    :type docs_dir: Path
    :param lang: Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    :type lang: str
    :raises FileNotFoundError: Если директория `docs_dir` не существует.
    :return: None
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    summary_file = prepare_summary_path(docs_dir)
    try:
        summary_file.parent.mkdir(parents=True, exist_ok=True)
    except Exception as ex:
        logger.error(f'Ошибка создания директории {summary_file.parent}: {ex}')
        return
    # Проверка существования директории
    if not docs_dir.exists():
        logger.error(f"Директория не найдена: {docs_dir}")
        raise FileNotFoundError(f"Директория не найдена: {docs_dir}")
    _make_summary(docs_dir, summary_file, lang)


def _make_summary(src_dir: Path, summary_file: Path, lang: str = 'en') -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    :param src_dir: Путь к папке с исходниками .md.
    :type src_dir: Path
    :param summary_file: Путь для сохранения файла SUMMARY.md.
    :type summary_file: Path
    :param lang: Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    :type lang: str
    :return: True в случае успешного создания файла, False в случае ошибки.
    :rtype: bool
    """
    try:
        if summary_file.exists():
            logger.info(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")

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
        logger.error(f"Ошибка создания файла `summary.md`: {ex}")
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути 'src' на 'docs' и добавляя имя файла.

    :param src_dir: Исходный путь с 'src'.
    :type src_dir: Path
    :param file_name: Имя файла, который нужно создать. По умолчанию 'SUMMARY.md'.
    :type file_name: str
    :return: Новый путь к файлу.
    :rtype: Path
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    new_dir = PROJECT_ROOT / 'docs'
    summary_file = new_dir / file_name
    return summary_file


if __name__ == '__main__':
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Создание файла SUMMARY.md с фильтрацией по языку.")
    parser.add_argument('-lang', type=str, choices=['ru', 'en'], default='en', help="Язык фильтрации файлов (ru или en). По умолчанию 'en'.")
    parser.add_argument('src_dir', type=str, help="Путь к исходной директории 'src'.")
    args = parser.parse_args()

    # Преобразование пути в объект Path
    src_dir = PROJECT_ROOT / args.src_dir

    # Вызов функции make_summary с переданными аргументами
    try:
        make_summary(src_dir, args.lang)
    except FileNotFoundError as ex:
        logger.error(f"Ошибка при создании SUMMARY.md: {ex}")
```