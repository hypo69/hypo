# Модуль hypotez/src/endpoints/prestashop/api/header.py

## Обзор

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json` и чтения документации из файла `README.MD`.  Он также определяет переменные, содержащие информацию о проекте, такие как имя, версия, автор и т.д.

## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная от текущего файла.  Поиск ведется вверх по директориям, пока не будет найдена директория, содержащая указанные маркерные файлы (pyproject.toml, requirements.txt, .git).

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корень проекта. По умолчанию используются `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращает путь к директории текущего файла.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```


###  `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная от текущего файла.  Поиск ведется вверх по директориям, пока не будет найдена директория, содержащая указанные маркерные файлы (pyproject.toml, requirements.txt, .git).

**Параметры**:
- `marker_files` (tuple): Кортеж имен файлов или директорий, по которым определяется корень проекта. По умолчанию используются `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если найдена. В противном случае возвращает путь к директории текущего файла.


**Пример использования**:

```python
root_path = set_project_root()
print(root_path)
```



## Переменные

**Описание**:  Переменные, содержащие информацию о проекте (имя, версия, автор, описание, и т.д.), полученные из файла `settings.json` и `README.md`.


**Переменные**:

- `__root__` (Path): Путь к корневой директории проекта.
- `settings` (dict): Словарь с настройками проекта, полученный из файла `settings.json`. Может быть `None`, если файл не найден или содержит некорректные данные.
- `doc_str` (str):  Строка документации, прочитанная из файла `README.MD`. Может быть `None` при отсутствии файла или ошибке чтения.
- `__project_name__` (str): Имя проекта, полученное из настроек. По умолчанию `'hypotez'`.
- `__version__` (str): Версия проекта, полученная из настроек. По умолчанию `''`.
- `__doc__` (str): Текст документации, полученный из файла `README.MD`.  По умолчанию `''`.
- `__details__` (str): Дополнительные детали проекта. По умолчанию `''`.
- `__author__` (str): Автор проекта, полученный из настроек. По умолчанию `''`.
- `__copyright__` (str): Авторские права проекта, полученные из настроек. По умолчанию `''`.
- `__cofee__` (str): Ссылка для поддержки разработчика. По умолчанию ссылка на Boosty.


**Обработка исключений**:

В коде используются блоки `try...except`, чтобы обработать возможные исключения при работе с файлами (FileNotFoundError, json.JSONDecodeError). В случае ошибки, соответствующая переменная устанавливается в `None` или пустую строку.


```
```