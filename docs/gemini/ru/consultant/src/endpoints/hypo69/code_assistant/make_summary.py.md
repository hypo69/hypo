# Анализ кода модуля src.endpoints.hypo69.code_assistant.make_summary

**Качество кода**
7
-  Плюсы
    -  Код выполняет поставленную задачу по созданию файла `SUMMARY.md` на основе структуры каталогов и файлов.
    -  Используется `pathlib.Path` для работы с путями, что делает код кроссплатформенным.
    -  Присутствует базовая обработка ошибок через `try-except`.
    -  Реализована фильтрация файлов по языку (`ru` или `en`).
    -  Код достаточно хорошо структурирован, с разделением на функции.
    -  Используется `argparse` для обработки аргументов командной строки.
-  Минусы
    -  Отсутствует полная документация в формате reStructuredText (RST).
    -  Используется `print` для вывода сообщений, вместо использования логгера.
    -  Недостаточно подробные комментарии в некоторых местах кода.
    -  Используется стандартный блок `try-except`, вместо `logger.error`.
    -  Импорт `header` не имеет docstring.
    -  Не все переменные имеют аннотацию типов.

**Рекомендации по улучшению**
1.  Добавить reStructuredText (RST) документацию для модуля, функций и переменных.
2.  Заменить `print` на `logger.info` и `logger.error` для более структурированного логирования.
3.  Удалить избыточный `try-except`, заменив его на `logger.error`.
4.  Добавить аннотацию типов для всех переменных и аргументов функций.
5.  Сделать более подробные комментарии к блокам кода.
6.  Удалить комментарии `#! venv/Scripts/python.exe` `#! venv/bin/python/python3.12` так как это специфические пути интерпретатора python.
7.  Указать импорты из `src.logger.logger`
8.  Привести в соответствие имена переменных и функций с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для создания файла SUMMARY.md для mdbook.
=========================================================================================

Этот модуль предоставляет функциональность для создания файла `SUMMARY.md`,
используемого `mdbook` для организации структуры книги.
Он сканирует директорию с исходными файлами Markdown,
фильтрует их по языку и генерирует оглавление в формате `mdbook`.

Пример использования
--------------------

Пример вызова функции make_summary:

.. code-block:: python

    from pathlib import Path
    from src.endpoints.hypo69.code_assistant.make_summary import make_summary

    docs_dir = Path('src')
    lang = 'ru'
    make_summary(docs_dir, lang)
"""
# -*- coding: utf-8 -*-
from pathlib import Path
import argparse
# Импорт модуля, который определяет корневой путь проекта
import header
# импорт logger
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns as j_loads
# Используем корневой путь проекта
PROJECT_ROOT = header.__root__


def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    :param docs_dir: Путь к исходной директории 'src'.
    :type docs_dir: Path
    :param lang: Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    :type lang: str
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    summary_file = _prepare_summary_path(docs_dir)
    # Создаем директорию, если ее не существует
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    # Вызываем функцию для создания файла
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
    :return: `True` в случае успешного создания файла, `False` в случае ошибки.
    :rtype: bool
    """
    try:
        # Проверяем, существует ли файл
        if summary_file.exists():
            logger.info(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")
        # Открываем файл для записи
        with summary_file.open('w', encoding='utf-8') as summary:
            # Записываем заголовок файла
            summary.write('# Summary\n\n')
            # Проходим по всем файлам .md в директории
            for path in sorted(src_dir.rglob('*.md')):
                # Пропускаем сам файл SUMMARY.md
                if path.name == 'SUMMARY.md':
                    continue
                # Фильтрация файлов по языку
                if lang == 'ru' and not path.name.endswith('.ru.md'):
                    # Пропускаем файлы без суффикса .ru.md
                    continue
                elif lang == 'en' and path.name.endswith('.ru.md'):
                    # Пропускаем файлы с суффиксом .ru.md
                    continue
                # Создаем относительный путь к файлу
                relative_path = path.relative_to(src_dir.parent)
                # Записываем строку в файл SUMMARY.md
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        # Логируем ошибку
        logger.error(f"Ошибка создания файла `summary.md`: {ex}")
        return False


def _prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
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
    # Формируем путь к файлу
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
    make_summary(src_dir, args.lang)
```