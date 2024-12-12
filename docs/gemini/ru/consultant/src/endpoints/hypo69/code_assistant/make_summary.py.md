# Анализ кода модуля `make_summary.py`

**Качество кода**
7
-  Плюсы
    - Код выполняет поставленную задачу по созданию `SUMMARY.md`.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть базовая структура функций и разделение на логические блоки.
    - Функция `prepare_summary_path` корректно формирует путь к файлу `SUMMARY.md`.
-  Минусы
    -  Отсутствует обработка ошибок через `logger`.
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя это и не требуется в данном контексте).
    -  Не используется reStructuredText (RST) для документирования функций.
    -  Отсутствуют импорты для используемых модулей, хотя они могут быть стандартными.
    -  Использование `print` для вывода сообщений об ошибках и логов (следует использовать `logger`).
    -  Лишние shebang в начале файла.

**Рекомендации по улучшению**
1.  **Документация:** Переписать все docstrings в формате reStructuredText (RST).
2.  **Логирование:** Использовать `logger.error` для логирования ошибок вместо `print`.
3.  **Импорты:** Добавить необходимые импорты, в частности `from src.logger.logger import logger`.
4.  **Обработка ошибок:** Улучшить обработку ошибок, используя `logger.error` и возвращая `False` в случае ошибки.
5.  **Комментарии:** Добавить более подробные комментарии к коду.
6.  **Удалить Shebang:** Удалить shebang из начала файла.
7. **Удалить переменные** `MODE` так как она не используется.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

"""
Модуль для создания файла SUMMARY.md
===================================================

Этот модуль создает файл `SUMMARY.md` для использования с `mdbook`.
Он рекурсивно обходит указанную директорию и генерирует оглавление
на основе найденных файлов `.md`.

Подробнее о `mdbook`: https://chatgpt.com/share/6742f054-aaa0-800d-9f84-0ab035a2a2c2

"""

from pathlib import Path
from src.logger.logger import logger #  Импортируем логгер
# from src.utils.jjson import j_loads, j_loads_ns # импортируем j_loads и j_loads_ns (не используется в данном коде, но добавлено для соответствия инструкциям)


def make_summary(docs_dir: Path) -> None:
    """
    Создает файл `SUMMARY.md`, рекурсивно обходя указанную директорию.

    :param docs_dir: Путь к директории, содержащей файлы `.md`.
    :type docs_dir: Path
    :raises FileNotFoundError: Если директория не существует
    :raises Exception: При возникновении других ошибок
    """
    summary_file = prepare_summary_path(docs_dir)
    # Создаем родительскую директорию для файла `SUMMARY.md`, если она не существует
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    # Вызов функции _make_summary для создания `SUMMARY.md`
    _make_summary(docs_dir, summary_file)


def _make_summary(src_dir: Path, summary_file: Path) -> bool:
    """
    Рекурсивно обходит папку и создает файл `SUMMARY.md` с главами на основе файлов `.md`.

    :param src_dir: Путь к папке с исходными файлами `.md`.
    :type src_dir: Path
    :param summary_file: Путь, куда следует сохранить файл `SUMMARY.md`.
    :type summary_file: Path
    :return: `True`, если файл успешно создан, `False` в случае ошибки.
    :rtype: bool
    """
    try:
        #  Проверка на существование файла
        if summary_file.exists():
            logger.info(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")

        # Открытие файла для записи
        with summary_file.open('w', encoding='utf-8') as summary:
            #  Записываем заголовок
            summary.write('# Summary\n\n')
            #  Итерируемся по всем файлам .md в директории
            for path in sorted(src_dir.rglob('*.md')):
                #  Пропуск файла `SUMMARY.md`
                if path.name == 'SUMMARY.md':
                    continue
                # Формируем относительный путь
                relative_path = path.relative_to(src_dir.parent)
                # Записываем строку в файл в формате `md`
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        #  Логируем ошибку и возвращаем `False`
        logger.error(f"Ошибка создания файла `summary.md`", exc_info=ex)
        ...
        return False


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути `src` на `docs` и добавляя имя файла.

    :param src_dir: Исходный путь, содержащий `src`.
    :type src_dir: Path
    :param file_name: Имя файла, который необходимо создать. По умолчанию `SUMMARY.md`.
    :type file_name: str
    :return: Новый путь к файлу.
    :rtype: Path
    """
    #  Заменяем /src на /docs в пути
    new_dir = Path(str(src_dir).replace('/src', '/docs'))
    #  Соединяем путь с именем файла
    summary_file = new_dir / file_name
    return summary_file
```