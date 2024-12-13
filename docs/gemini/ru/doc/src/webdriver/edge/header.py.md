# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для инициализации основных настроек и путей проекта, а также для загрузки конфигурационных данных и документации. Он устанавливает корневую директорию проекта, загружает настройки из файла `settings.json`, читает документацию из `README.MD` и определяет основные переменные проекта, такие как имя, версия, автор и т.д.

## Оглавление

1. [Функции](#функции)
   - [`set_project_root`](#set_project_root)
2. [Переменные](#переменные)
   - [`MODE`](#mode)
   - [`__root__`](#__root__)
   - [`settings`](#settings)
   - [`doc_str`](#doc_str)
   - [`__project_name__`](#__project_name__)
   - [`__version__`](#__version__)
   - [`__doc__`](#__doc__)
   - [`__details__`](#__details__)
   - [`__author__`](#__author__)
   - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)


## Функции

### `set_project_root`

**Описание**:
Функция `set_project_root` находит корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх по родительским директориям. Поиск останавливается, когда найдена директория, содержащая хотя бы один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, которые служат маркерами корневой директории проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Объект `Path`, представляющий корневую директорию проекта. Если маркеры не найдены, возвращается директория, где расположен скрипт.

```python
def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

## Переменные

### `MODE`

**Описание**:
`MODE` - это строковая переменная, определяющая режим работы проекта. В данном случае по умолчанию установлено значение `dev`, что, вероятно, указывает на режим разработки.

```python
MODE = 'dev'
```

### `__root__`

**Описание**:
`__root__` - это переменная типа `Path`, содержащая путь к корневой директории проекта, полученный с помощью функции `set_project_root`.

```python
__root__ = set_project_root()
```

### `settings`

**Описание**:
`settings` - это словарь, который содержит настройки проекта, загруженные из файла `settings.json`. Если файл не найден или содержит ошибки JSON, переменная остается `None`.

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `doc_str`

**Описание**:
`doc_str` - это строка, которая содержит текст из файла `README.MD`. Если файл не найден или содержит ошибки, переменная остается `None`.

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

### `__project_name__`

**Описание**:
`__project_name__` - это строка, содержащая имя проекта, извлеченное из файла настроек. Если в `settings` нет ключа `project_name`, по умолчанию устанавливается значение `hypotez`.

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

### `__version__`

**Описание**:
`__version__` - это строка, содержащая версию проекта, извлеченную из файла настроек. Если в `settings` нет ключа `version`, по умолчанию устанавливается пустая строка.

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

### `__doc__`

**Описание**:
`__doc__` - это строка, содержащая документацию проекта, загруженную из файла `README.MD`. Если `doc_str` имеет значение, отличное от `None`, то оно устанавливается как значение переменной `__doc__`. В противном случае значение будет пустой строкой.

```python
__doc__: str = doc_str if doc_str else ''
```

### `__details__`

**Описание**:
`__details__` - это строка, предназначенная для хранения дополнительной информации о проекте. В данном коде она инициализируется пустой строкой и может быть изменена позже в процессе работы.

```python
__details__: str = ''
```

### `__author__`

**Описание**:
`__author__` - это строка, содержащая имя автора проекта, извлеченное из файла настроек. Если в `settings` нет ключа `author`, по умолчанию устанавливается пустая строка.

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

### `__copyright__`

**Описание**:
`__copyright__` - это строка, содержащая информацию об авторских правах проекта, извлеченную из файла настроек. Если в `settings` нет ключа `copyrihgnt`, по умолчанию устанавливается пустая строка.

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```
### `__cofee__`
**Описание**:
`__cofee__` - это строка, содержащая сообщение о поддержке разработчика, извлеченное из файла настроек. Если в `settings` нет ключа `cofee`, по умолчанию устанавливается строка: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```