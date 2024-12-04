# <input code>

```python
## \file /src/endpoints/hypo69/code_assistant/make_summary.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.endpoints.hypo69.code_assistant.make_summary
	:platform: Windows, Unix
	:synopsis: Модуль собирает файл `summary.md` для компиляции средствами `mdbook`
    Подробнее: https://chatgpt.com/share/6742f054-aaa0-800d-9f84-0ab035a2a2c2
"""
MODE = 'dev'


from pathlib import Path


def make_summary(docs_dir: Path) -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    Args:
        src_dir (Path): Путь к исходной директории 'src'.
    """
    summary_file = prepare_summary_path(docs_dir)
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    return _make_summary(docs_dir, summary_file)


def _make_summary(src_dir: Path, summary_file: Path) -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    Args:
        src_dir (Path): Путь к папке с исходниками .md.
        summary_file (Path): Путь для сохранения файла SUMMARY.md.
    """
    try:
        if summary_file.exists():
            print(f"Файл {summary_file} уже существует. Его содержимое будет перезаписано.")

        with summary_file.open('w', encoding='utf-8') as summary:
            summary.write('# Summary\n\n')

            for path in sorted(src_dir.rglob('*.md')):
                if path.name == 'SUMMARY.md':
                    continue
                relative_path = path.relative_to(src_dir.parent)
                summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')
        return True
    except Exception as ex:
        print(f"Ошибка создания файла `summary.md` {ex}")
        ...
        return


def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути 'src' на 'docs' и добавляя имя файла.

    Args:
        src_dir (Path): Исходный путь с 'src'.
        file_name (str): Имя файла, который нужно создать. По умолчанию 'SUMMARY.md'.

    Returns:
        Path: Новый путь к файлу.
    """
    new_dir = Path(str(src_dir).replace('/src', '/docs'))
    summary_file = new_dir / file_name
    return summary_file
```

# <algorithm>

**Шаг 1:** Функция `make_summary` принимает `docs_dir` (путь к папке с документацией).

**Шаг 2:** Функция `prepare_summary_path` генерирует правильный путь к файлу `SUMMARY.md` в папке `docs`, заменяя `/src` на `/docs` в пути `src_dir`.

**Шаг 3:** Функция `make_summary` создает папку родительскую к `summary_file` (если она не существует).

**Шаг 4:** Функция `make_summary` вызывает `_make_summary` с `src_dir` и `summary_file`.

**Шаг 5:** Функция `_make_summary` открывает `summary_file` в режиме записи.

**Шаг 6:** Функция `_make_summary` добавляет заголовок "# Summary".

**Шаг 7:** Функция `_make_summary` итерируется по всем файлам `.md` в `src_dir` с использованием `src_dir.rglob('*.md')`, сортирует их по имени.

**Шаг 8:** Если файл равен `SUMMARY.md`, то он пропускается.

**Шаг 9:** Функция `_make_summary` генерирует относительный путь к файлу `.md` от корня `src_dir.parent`.

**Шаг 10:** Функция `_make_summary` добавляет строку в `summary_file` с названием и ссылкой на файл `.md`.


**Пример:**

Если `src_dir` - `/src/docs/mydoc`, а `docs_dir` - `/src`, то `summary_file` будет `/docs/mydoc/SUMMARY.md`

# <mermaid>

```mermaid
graph LR
    A[make_summary(docs_dir)] --> B{prepare_summary_path(docs_dir)};
    B --> C[summary_file];
    C --> D(summary_file.parent.mkdir);
    D --> E[_make_summary(docs_dir, summary_file)];
    E --> F{summary_file.exists()};
    F -- yes --> G[Файл существует, перезапись];
    F -- no --> G;
    G --> H[with summary_file.open('w')];
    H --> I[summary.write('# Summary')];
    E --> J(sorted(src_dir.rglob('*.md')));
    J --> K[Loop through files];
    K --> L{path.name == 'SUMMARY.md'};
    L -- yes --> K;
    L -- no --> M[relative_path = path.relative_to(src_dir.parent)];
    M --> N[summary.write(f'- [{path.stem}]({relative_path.as_posix()})')];
    K --> O[return True];
    E -- fail --> P[Ошибка создания файла];
    P --> O;
```


# <explanation>

**Импорты:**

- `from pathlib import Path`: Импортирует класс `Path` из модуля `pathlib`. Используется для работы с путями файлов и каталогов, обеспечивая платформонезависимость.


**Классы:**

- Нет определенных классов в коде.


**Функции:**

- `make_summary(docs_dir: Path) -> None`:  Функция для создания файла `SUMMARY.md`. Принимает путь к папке с документацией (`docs_dir`). Создает файл `SUMMARY.md` в папке `docs`, содержащий ссылки на все файлы `.md` в папке `src`.
- `_make_summary(src_dir: Path, summary_file: Path) -> bool`: Рекурсивно обходит папку и создаёт файл `SUMMARY.md`. Принимает путь к исходной папке (`src_dir`) и путь к создаваемому файлу (`summary_file`). Возвращает `True` в случае успешного создания файла, `None` - в случае ошибки.  Рекурсивно обращается к себе при нахождении подкаталогов, позволяя обрабатывать всю иерархию директорий.
- `prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path`: Формирует путь к файлу `SUMMARY.md` в папке `docs` на основе пути к исходной папке (`src_dir`). Возвращает `Path` к файлу `SUMMARY.md`.


**Переменные:**

- `MODE`:  Переменная с константой, предположительно используется для настройки режима работы (например, 'dev' или 'prod').  Рекомендуется использовать константы `DEV` или `PROD` для более ясного обозначения.
- `summary_file`: Хранит путь к файлу `SUMMARY.md` в папке `docs`.
- `src_dir`, `docs_dir`, `relative_path`: хранят пути к файлам и каталогам.


**Возможные ошибки и улучшения:**

- Обработка ошибок: Хотя есть `try...except`, обработка конкретных ошибок (например, `FileNotFoundError`) была бы лучше.
- Возможно, было бы полезно добавить проверку, что `src_dir` существует.
- Вместо `...` в блоке `except` нужно добавить более подробную обработку ошибок, логирование или информацию пользователю о произошедшей ошибке.
- Использование `file_name` в `prepare_summary_path` делает функцию более гибкой.
- Вместо `summary.write(f'- [{path.stem}]({relative_path.as_posix()})\n')` можно использовать `summary.write(f'- [{path.stem}]({str(relative_path)})\n')` чтобы избежать `as_posix()`.
- Можно добавить проверку, что `path` действительно является файлом `.md`, а не каталогом.

**Связь с другими частями проекта:**

- Модуль `make_summary`  принадлежит к `endpoints/hypo69/code_assistant` и служит для генерации файла `SUMMARY.md`.  Предполагается, что этот файл используется `mdbook` для создания таблицы оглавления. Вероятно, существует процесс сборки документации (например, `mdbook build`), который использует этот файл.  Отсутствие детальной информации о том, как этот файл используется в `mdbook` может затруднить понимание полной логики проекта.