# <input code>

```python
## \file /src/endpoints/hypo69/code_assistant/make_summary.py
# -*- coding: utf-8 -*-\
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

**Шаг 1**: Функция `make_summary` принимает путь к директории `docs_dir`.

**Шаг 2**: Функция `prepare_summary_path` генерирует новый путь к файлу `SUMMARY.md` в директории `docs`, заменяя `src` на `docs` в исходном пути.

**Шаг 3**: Функция `make_summary` создает директорию родителя `summary_file` и вызывает функцию `_make_summary` с входными параметрами `docs_dir` и сгенерированным `summary_file`.


**Шаг 4**: Функция `_make_summary` открывает файл `summary_file` в режиме записи.

**Шаг 5**: Функция `_make_summary` добавляет строку `# Summary\n\n` в файл.

**Шаг 6**: Функция `_make_summary` перебирает все файлы с расширением `.md` в директории `src_dir` (с использованием `src_dir.rglob('*.md')`) в отсортированном порядке.

**Шаг 7**: Если имя файла равно `SUMMARY.md`,  он пропускается.

**Шаг 8**:  Функция `_make_summary` создает относительный путь `relative_path` к файлу, относительно `src_dir.parent`.

**Шаг 9**: Функция `_make_summary` добавляет строку в формате `- [{path.stem}]({relative_path.as_posix()})\n` в файл `summary_file`.

**Шаг 10**: После перебора всех файлов функция возвращает `True`.


**Пример**: Если `docs_dir` равняется `/src/endpoints/hypo69/code_assistant`,  то `summary_file` будет `/docs/endpoints/hypo69/code_assistant/SUMMARY.md`.  Данные передаются между функциями через аргументы. Функция `prepare_summary_path` генерирует путь, функция `make_summary` вызывает `_make_summary`.


# <mermaid>

```mermaid
graph TD
    A[make_summary(docs_dir)] --> B{prepare_summary_path(docs_dir)};
    B --> C[summary_file];
    C --> D{summary_file.parent.mkdir};
    D --> E[_make_summary(docs_dir, summary_file)];
    E --> F[open summary_file];
    F --> G[write "# Summary"];
    E --> H(sorted(src_dir.rglob('*.md')));
    H --> I[check if path.name == 'SUMMARY.md'];
    I --yes --> J[skip];
    I --no --> K{relative_path = path.relative_to(src_dir.parent)};
    K --> L[write - [{path.stem}]({relative_path.as_posix()})];
    L --> F;
    F --> M[return True];
    
    style E fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#ccf,stroke:#333,stroke-width:2px;


```

# <explanation>

**Импорты:**

- `from pathlib import Path`: Импортирует класс `Path` из модуля `pathlib`.  Он используется для работы с путями к файлам и директориям, предоставляя более безопасный и удобный способ манипулирования ими, особенно при работе с файловой системой.  Это основной импорт, необходимый для работы кода.

**Классы:**

- `Path`:  Класс из `pathlib`. Он представляет собой объект, представляющий путь к файлу или директории.  Он позволяет выполнять операции с путями (создание директорий, проверка существования файлов, получение относительных путей и т.д.).


**Функции:**

- `make_summary(docs_dir: Path) -> None`:  Функция для запуска процесса создания файла `summary.md`. Принимает путь к директории с документацией `docs_dir` и возвращает `None`. Она отвечает за подготовку пути и вызов функции `_make_summary`.
- `_make_summary(src_dir: Path, summary_file: Path) -> bool`: Функция, которая рекурсивно обходит директорию `src_dir` и формирует содержимое файла `summary.md`.  Возвращает `True` в случае успеха.
- `prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path`: Функция, которая формирует корректный путь к файлу `summary.md` в директории `docs` на основе входного пути `src_dir`. Возвращает `Path` объект.

**Переменные:**

- `MODE`: Строковая переменная, скорее всего, определяющая режим работы программы (например, 'dev', 'prod').
- `summary_file`: Переменная типа `Path`, хранит путь к файлу `SUMMARY.md`.
- `src_dir`, `docs_dir`: Переменные типа `Path`, хранят пути к исходным директориям.

**Возможные ошибки и улучшения:**

- **Обработка исключений:**  Обработка исключений в `_make_summary` недостаточно полная.  Необходимо указать конкретные типы исключений, которые нужно перехватить, и добавить более подробную информацию об ошибке (например, тип файла, в котором произошла ошибка, более конкретизированное описание).
- **Проверка входных данных:**  Необходимо добавить проверку на корректность входных данных `docs_dir`, чтобы предотвратить ошибки в случае неверного пути.
- **Избыточность:** Функция `prepare_summary_path` немного сложная для задачи. Возможно, логика может быть упрощена путем использования более прямого пути к папке "docs".
- **Чтение из файла с кодировкой:** Можно добавить проверку на кодировку файла во время чтения, чтобы избежать проблем, если файл не в UTF-8.



**Взаимосвязи с другими частями проекта:**

Функция `make_summary` используется для подготовки данных для сборки документации в формате `mdbook`.  Она зависит от наличия файлов `.md` в указанной директории и от того, что `mdbook` может обработать сгенерированный файл `summary.md`.  Взаимодействие с другими частями проекта происходит через файлы `.md` и директории, в которых они хранятся.