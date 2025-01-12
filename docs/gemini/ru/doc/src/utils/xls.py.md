# `src.utils.xls`

## Обзор

Модуль `src.utils.xls` предоставляет функции для конвертации файлов Excel (`.xls`) в формат JSON и обратно. Он позволяет читать данные из Excel-файлов, включая обработку нескольких листов, и сохранять JSON-данные обратно в файлы Excel.

## Содержание

- [Функции](#Функции)
    - [`read_xls_as_dict`](#read_xls_as_dict)
    - [`save_xls_file`](#save_xls_file)

## Функции

### `read_xls_as_dict`

**Описание**:
Читает Excel-файл и преобразует его в JSON. Опционально, преобразует указанный лист и сохраняет результат в JSON-файл. Обрабатывает ошибки.

**Параметры**:
- `xls_file` (str): Путь к Excel-файлу.
- `json_file` (Optional[str], optional): Путь к JSON-файлу для сохранения результата. По умолчанию `None`.
- `sheet_name` (Optional[str | int], optional): Имя или индекс листа для чтения. По умолчанию `None`, что читает все листы.

**Возвращает**:
- `Union[Dict, List[Dict], bool]`: Возвращает словарь, где ключи — имена листов (если `sheet_name` не указан), а значения — списки словарей, представляющие строки. Если `sheet_name` указан, возвращает список словарей для конкретного листа. Возвращает `False` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если Excel-файл не найден.
- `Exception`: Возникает при других ошибках, например, при чтении или преобразовании данных.

```python
def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Reads an Excel file and converts it to JSON.  Optionally, converts a specific sheet and saves the result to a JSON file.
    Handles errors gracefully.
    """
```

### `save_xls_file`

**Описание**:
Сохраняет JSON-данные в файл Excel. Данные должны быть в виде словаря, где ключи — имена листов, а значения — списки словарей, представляющие строки. Обрабатывает ошибки.

**Параметры**:
- `data` (Dict[str, List[Dict]]): Данные для сохранения в Excel-файл. Ключи словаря соответствуют названиям листов, значения - спискам словарей, представляющим собой строки данных.
- `file_path` (str): Путь для сохранения Excel-файла.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного сохранения, иначе `False`.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках сохранения файла.

```python
def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """Saves JSON data to an Excel file. Handles errors gracefully."""
```