# Improved Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для создания файла `SUMMARY.md` для `mdbook`.
=========================================================================================

Модуль ``make_summary`` предназначен для автоматического создания файла `SUMMARY.md`,
необходимого для компиляции документации с помощью `mdbook`.
Функции модуля позволяют рекурсивно обходить директории с исходными файлами
формата `.md` и генерировать структуру оглавления в формате,
требуемом `mdbook`.

Пример использования:
--------------------

.. code-block:: python

    from pathlib import Path
    from src.endpoints.hypo69.code_assistant.make_summary import make_summary

    docs_dir = Path('путь/к/директории/с/документами')
    make_summary(docs_dir)

"""



from pathlib import Path
from src.logger.logger import logger  # Добавлен импорт logger


def make_summary(docs_dir: Path) -> None:
    """
    Создает файл `SUMMARY.md`, рекурсивно обходя указанную директорию.

    :param docs_dir: Путь к исходной директории с документацией.
    :type docs_dir: Path
    :return: None
    """
    # Формирование пути для файла `SUMMARY.md`.
    summary_file = prepare_summary_path(docs_dir)
    # Создание родительских директорий, если они не существуют.
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    # Вызов функции для рекурсивного создания структуры.
    _make_summary(docs_dir, summary_file)


def _make_summary(src_dir: Path, summary_file: Path) -> bool:
    """
    Рекурсивно обходит директорию и создает файл `SUMMARY.md` на основе `.md` файлов.

    :param src_dir: Путь к директории с исходными файлами `.md`.
    :type src_dir: Path
    :param summary_file: Путь к файлу `SUMMARY.md`, который будет создан.
    :type summary_file: Path
    :return: Возвращает `True` в случае успешного создания файла, `False` в случае ошибки.
    :rtype: bool
    """
    try:
        # Проверка на существование файла и вывод предупреждения.
        if summary_file.exists():
            print(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")

        # Открытие файла для записи с кодировкой UTF-8.
        with summary_file.open('w', encoding='utf-8') as summary:
            # Запись начального заголовка для `mdbook`.
            summary.write('# Summary\n\n')

            # Обход всех `.md` файлов в директории, включая поддиректории.
            for path in sorted(src_dir.rglob('*.md')):
                # Пропуск файла `SUMMARY.md`, чтобы избежать рекурсии.
                if path.name == 'SUMMARY.md':
                    continue
                # Формирование относительного пути.
                relative_path = path.relative_to(src_dir.parent)
                # Запись строки в файл `SUMMARY.md` с форматированием для `mdbook`.
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        # Логирование ошибки в случае исключения.
        logger.error(f"Ошибка создания файла `summary.md`", exc_info=ex)
        ...
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу `SUMMARY.md` на основе пути к исходной директории.
    Заменяет часть пути `/src` на `/docs`.

    :param src_dir: Исходный путь с `/src`.
    :type src_dir: Path
    :param file_name: Имя файла, который нужно создать. По умолчанию `SUMMARY.md`.
    :type file_name: str
    :return: Возвращает новый путь к файлу.
    :rtype: Path
    """
    # Замена `/src` на `/docs` в пути к директории.
    new_dir = Path(str(src_dir).replace('/src', '/docs'))
    # Создание полного пути к файлу `SUMMARY.md`.
    summary_file = new_dir / file_name
    return summary_file
```
# Changes Made
* Добавлен импорт `logger` из `src.logger.logger`.
* Добавлены docstrings в формате RST для модуля и всех функций.
* Изменен вывод ошибок в функции `_make_summary` на использование `logger.error` для логирования.
* Добавлены типы параметров и возвращаемых значений в docstring для функций.
* Добавлены комментарии для пояснения основных блоков кода.
# FULL Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для создания файла `SUMMARY.md` для `mdbook`.
=========================================================================================

Модуль ``make_summary`` предназначен для автоматического создания файла `SUMMARY.md`,
необходимого для компиляции документации с помощью `mdbook`.
Функции модуля позволяют рекурсивно обходить директории с исходными файлами
формата `.md` и генерировать структуру оглавления в формате,
требуемом `mdbook`.

Пример использования:
--------------------

.. code-block:: python

    from pathlib import Path
    from src.endpoints.hypo69.code_assistant.make_summary import make_summary

    docs_dir = Path('путь/к/директории/с/документами')
    make_summary(docs_dir)

"""



from pathlib import Path
from src.logger.logger import logger  # Добавлен импорт logger


def make_summary(docs_dir: Path) -> None:
    """
    Создает файл `SUMMARY.md`, рекурсивно обходя указанную директорию.

    :param docs_dir: Путь к исходной директории с документацией.
    :type docs_dir: Path
    :return: None
    """
    # Формирование пути для файла `SUMMARY.md`.
    summary_file = prepare_summary_path(docs_dir)
    # Создание родительских директорий, если они не существуют.
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    # Вызов функции для рекурсивного создания структуры.
    _make_summary(docs_dir, summary_file)


def _make_summary(src_dir: Path, summary_file: Path) -> bool:
    """
    Рекурсивно обходит директорию и создает файл `SUMMARY.md` на основе `.md` файлов.

    :param src_dir: Путь к директории с исходными файлами `.md`.
    :type src_dir: Path
    :param summary_file: Путь к файлу `SUMMARY.md`, который будет создан.
    :type summary_file: Path
    :return: Возвращает `True` в случае успешного создания файла, `False` в случае ошибки.
    :rtype: bool
    """
    try:
        # Проверка на существование файла и вывод предупреждения.
        if summary_file.exists():
            print(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")

        # Открытие файла для записи с кодировкой UTF-8.
        with summary_file.open('w', encoding='utf-8') as summary:
            # Запись начального заголовка для `mdbook`.
            summary.write('# Summary\n\n')

            # Обход всех `.md` файлов в директории, включая поддиректории.
            for path in sorted(src_dir.rglob('*.md')):
                # Пропуск файла `SUMMARY.md`, чтобы избежать рекурсии.
                if path.name == 'SUMMARY.md':
                    continue
                # Формирование относительного пути.
                relative_path = path.relative_to(src_dir.parent)
                # Запись строки в файл `SUMMARY.md` с форматированием для `mdbook`.
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        # Логирование ошибки в случае исключения.
        logger.error(f"Ошибка создания файла `summary.md`", exc_info=ex)
        ...
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу `SUMMARY.md` на основе пути к исходной директории.
    Заменяет часть пути `/src` на `/docs`.

    :param src_dir: Исходный путь с `/src`.
    :type src_dir: Path
    :param file_name: Имя файла, который нужно создать. По умолчанию `SUMMARY.md`.
    :type file_name: str
    :return: Возвращает новый путь к файлу.
    :rtype: Path
    """
    # Замена `/src` на `/docs` в пути к директории.
    new_dir = Path(str(src_dir).replace('/src', '/docs'))
    # Создание полного пути к файлу `SUMMARY.md`.
    summary_file = new_dir / file_name
    return summary_file