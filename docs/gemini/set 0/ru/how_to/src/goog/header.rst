Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет функцию `set_project_root`, которая находит корневую директорию проекта. Он ищет файлы (или директории), указанные в `marker_files`, начиная с текущей директории и поднимаясь по дереву каталогов. Если корневая директория найдена, она добавляется в `sys.path`.  Затем код загружает настройки из файла `settings.json` и, при успешном чтении, определяет имя проекта, версию, описание, автора и авторские права из этого файла, а при отсутствии файлов – использует значения по умолчанию.  Код также пытается загрузить README.MD для документации проекта.

Шаги выполнения
-------------------------
1. **Импортирует необходимые модули:** `sys`, `json`, `pathlib`, `Version` (из `packaging`).
2. **Определяет функцию `set_project_root`:**
    * Принимает аргумент `marker_files` (кортеж строк, обозначающих маркеры проекта).
    * Получает текущую директорию скрипта.
    * Инициализирует `__root__` текущей директорией.
    * Проходит по родительским директориям, проверяя наличие файлов или директорий из `marker_files`.
    * Если найден маркер, устанавливает `__root__` в текущую директорию и прерывает цикл.
    * Если корневая директория не найдена, возвращает текущую директорию.
    * Если корневая директория не в `sys.path`, добавляет ее в начало `sys.path`.
    * Возвращает путь к корневой директории.
3. **Вызывает функцию `set_project_root`**, чтобы получить корневую директорию проекта.  Результат сохраняется в переменной `__root__`.
4. **Пытается загрузить настройки из файла `settings.json` в переменную `settings`:**
    * Использует путь, основанный на `gs.path.root`.
    * Обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError` (в случае проблем при чтении или декодировании JSON).
5. **Пытается загрузить README.MD для документации проекта в переменную `doc_str`:**
    * Использует путь, основанный на `gs.path.root`.
    * Обрабатывает исключения `FileNotFoundError` и `json.JSONDecodeError`.
6. **Получает значения настроек, а если файл не найден, использует значения по умолчанию:**
    * `__project_name__`: имя проекта (из `settings`, по умолчанию - `hypotez`).
    * `__version__`: версия проекта (из `settings`, по умолчанию - пустая строка).
    * `__doc__`: описание проекта (из `doc_str`, по умолчанию - пустая строка).
    * `__details__`: дополнительные данные (по умолчанию - пустая строка).
    * `__author__`: автор проекта (из `settings`, по умолчанию - пустая строка).
    * `__copyright__`: авторские права (из `settings`, по умолчанию - пустая строка).
    * `__cofee__`: ссылка на поддержку разработчика (из `settings`, по умолчанию – заданная ссылка).

Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что модуль gs уже импортирован и `gs.path` содержит путь к проекту.
    from pathlib import Path

    # ... (ваш код, который использует функцию set_project_root) ...
    root_path = set_project_root()
    print(root_path)
    print(__project_name__)
    print(__version__)