### Анализ кода модуля `make_summary`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код в целом выполняет поставленную задачу по созданию файла `SUMMARY.md`.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует разделение на функции для более читаемого кода.
    - Присутствует возможность фильтрации файлов по языку.
- **Минусы**:
    - Используется стандартный `print` для вывода ошибок и уведомлений, что не соответствует требованиям логирования.
    - Отсутствует обработка потенциальных ошибок при создании или записи файла.
    - Не хватает подробной документации в формате RST для функций и модуля.
    - Жестко задано имя файла `SUMMARY.md` в функции `prepare_summary_path`.

**Рекомендации по улучшению:**

1.  **Логирование:**
    - Заменить все вызовы `print` на `logger.info` для информационных сообщений и `logger.error` для сообщений об ошибках.
    - Импортировать `logger` из `src.logger`.
2.  **Обработка ошибок:**
    - В функции `_make_summary` использовать `logger.error` для вывода сообщения об ошибке, не прерывая выполнение программы.
    - Вместо `try-except` использовать `with` для открытия файла, что автоматически обрабатывает закрытие файла.
3.  **Документация:**
    - Добавить документацию в формате RST для модуля и всех функций, включая описание параметров, возвращаемых значений и исключений.
    - Добавить примеры использования функций в документации.
4.  **Гибкость:**
    - Сделать имя файла `SUMMARY.md` в `prepare_summary_path` параметром.
5. **Импорты**:
    - Выровнять импорты по алфавиту.

**Оптимизированный код:**

```python
"""
Модуль для создания файла SUMMARY.md для mdbook
=================================================

Модуль `make_summary` отвечает за создание файла `SUMMARY.md`, который используется
для компиляции документации средствами `mdbook`. Он рекурсивно обходит указанную директорию,
собирая все файлы с расширением `.md` и добавляя их в `SUMMARY.md` с учетом фильтрации по языку.

Пример использования
----------------------
.. code-block:: python

    from pathlib import Path
    from src.endpoints.hypo69.code_assistant.make_summary import make_summary

    docs_dir = Path('./src') # Укажите путь к вашей директории 'src'
    make_summary(docs_dir, lang='ru')
"""

from pathlib import Path
import argparse
from src.logger import logger # Импорт logger
import header  # Импорт модуля, который определяет корневой путь проекта


# Используем корневой путь проекта
PROJECT_ROOT = header.__root__


def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    :param docs_dir: Путь к исходной директории 'src'.
    :type docs_dir: Path
    :param lang: Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    :type lang: str, optional
    :raises Exception: В случае ошибки при создании файла `summary.md`
    
    Пример:
        >>> from pathlib import Path
        >>> docs_dir = Path('./src')
        >>> make_summary(docs_dir, lang='ru')
    """
    # Используем корневой путь для формирования пути к SUMMARY.md
    summary_file = prepare_summary_path(docs_dir)
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    _make_summary(docs_dir, summary_file, lang)


def _make_summary(src_dir: Path, summary_file: Path, lang: str = 'en') -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    :param src_dir: Путь к папке с исходниками .md.
    :type src_dir: Path
    :param summary_file: Путь для сохранения файла SUMMARY.md.
    :type summary_file: Path
    :param lang: Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    :type lang: str, optional
    :return: True, если файл успешно создан или перезаписан, иначе False.
    :rtype: bool
    
    Пример:
        >>> from pathlib import Path
        >>> src_dir = Path('./src')
        >>> summary_file = Path('./docs/SUMMARY.md')
        >>> _make_summary(src_dir, summary_file, lang='ru')
        True
    """
    try:
        if summary_file.exists():
            logger.info(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.") # Логируем информационное сообщение

        with summary_file.open('w', encoding='utf-8') as summary: # Используем with для открытия файла
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
        logger.error(f"Ошибка создания файла `summary.md`: {ex}") # Логируем сообщение об ошибке
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути 'src' на 'docs' и добавляя имя файла.

    :param src_dir: Исходный путь с 'src'.
    :type src_dir: Path
    :param file_name: Имя файла, который нужно создать. По умолчанию 'SUMMARY.md'.
    :type file_name: str, optional
    :return: Новый путь к файлу.
    :rtype: Path

    Пример:
        >>> from pathlib import Path
        >>> src_dir = Path('./src')
        >>> prepare_summary_path(src_dir)
        PosixPath('docs/SUMMARY.md')
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
    make_summary(src_dir, args.lang)