# Модуль `hypotez/src/suppliers/visualdg/header.py`

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и получения информации о проекте (название, версия, документация).

## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории файла и идя вверх по иерархии директорий.  Останавливается на первой директории, содержащей один из указанных маркеров (файлов или директорий).

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или директорий, используемых в качестве маркеров для определения корневой директории. По умолчанию: `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена. В противном случае возвращает путь к директории, где находится текущий скрипт.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```

**Примечание**: Функция добавляет найденную корневую директорию в `sys.path`, что позволяет импортировать модули из других папок проекта.

###  (Внутренние переменные, инициализируемые в модуле)


**Описание**:  Переменные инициализируются внутри модуля.


**__root__ (Path):**  Путь к корневой директории проекта.
**settings (dict):** Словарь с настройками проекта, загруженный из `settings.json`.
**doc_str (str):** Строка с текстом документации (README), загруженная из `README.MD`.
**__project_name__ (str):** Название проекта (извлечено из `settings.json`, по умолчанию 'hypotez').
**__version__ (str):** Версия проекта (извлечено из `settings.json`, по умолчанию '').
**__doc__ (str):** Документация проекта (извлечено из `README.MD`, по умолчанию '').
**__details__ (str):** Дополнительные детали о проекте (по умолчанию '').
**__author__ (str):** Автор проекта (извлечено из `settings.json`, по умолчанию '').
**__copyright__ (str):** Авторские права проекта (извлечено из `settings.json`, по умолчанию '').
**__cofee__ (str):** Ссылка для поддержки разработчика (извлечено из `settings.json`, по умолчанию - ссылка на бусти).

**Обработка исключений**:

- `FileNotFoundError`:  Исключение, выбрасываемое, если файл `settings.json` или `README.MD` не найден.
- `json.JSONDecodeError`: Исключение, выбрасываемое, если данные в `settings.json` не могут быть декодированы как JSON.

В блоках `try...exept` используется `...`, так как ожидается, что исключения будут обработаны в зависимости от контекста, но в данном коде это не происходит.

**Примечания**:
-  Функция `set_project_root` необходима для корректного импорта зависимостей проекта.
- Переменные `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`  могут быть использованы в других частях кода для доступа к конфигурации проекта.