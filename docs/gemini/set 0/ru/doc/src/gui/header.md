# Модуль `hypotez/src/gui/header.py`

## Обзор

Этот модуль определяет корневой путь к проекту `hypotez`.  Он находит директорию проекта, начиная с текущей директории и проходя вверх по дереву директорий, пока не найдет директорию, содержащую файлы `pyproject.toml`, `requirements.txt` или `.git`.  Затем, он добавляет этот корневой путь в `sys.path`, чтобы гарантировать, что все импорты работали корректно. Модуль также загружает настройки из файла `settings.json` и документацию из файла `README.MD` в корневом каталоге проекта.

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта (по умолчанию `('pyproject.toml', 'requirements.txt', '.git')`).

**Возвращает**:
- `Path`: Путь к корневой директории проекта. Если корневая директория не найдена, возвращается директория, в которой находится текущий файл.

**Вызывает исключения**:
- Нет.


## Переменные

### `__root__`

**Описание**: Путь к корневой директории проекта, полученный с помощью функции `set_project_root()`.

**Тип**: `Path`


## Загрузка настроек и документации

**Описание**: Загружает настройки проекта из файла `settings.json` и документацию из файла `README.MD` в корневой директории.  При отсутствии этих файлов, значения по умолчанию устанавливаются в переменные.


**Переменные**:

* `settings`: Словарь со значениями настроек проекта.  Используется значение по умолчанию 'hypotez', если файл `settings.json` не найден или некорректен.
* `doc_str`: Строка, содержащая содержимое файла `README.MD`. Используется пустая строка, если файл не найден или некорректен.
* `__project_name__`: Строка, содержащая имя проекта. Получается из `settings`, значение по умолчанию 'hypotez'.
* `__version__`: Строка, содержащая версию проекта. Получается из `settings`, значение по умолчанию ''.
* `__doc__`: Строка, содержащая документацию проекта. Получается из `doc_str`, значение по умолчанию ''.
* `__details__`: Строка, содержащая дополнительные детали. Значение по умолчанию ''.
* `__author__`: Строка, содержащая имя автора проекта. Получается из `settings`, значение по умолчанию ''.
* `__copyright__`: Строка, содержащая информацию о копирайтах. Получается из `settings`, значение по умолчанию ''.
* `__cofee__`: Строка, содержащая ссылку для поддержки разработчика. Получается из `settings`, значение по умолчанию ссылка.


**Обработка ошибок**:

- Используются блоки `try...except` для обработки `FileNotFoundError` и `json.JSONDecodeError`, чтобы предотвратить аварийную остановку программы при отсутствии или некорректном формате файлов настроек и документации.  В случае ошибки, соответствующие переменные получают значения по умолчанию.