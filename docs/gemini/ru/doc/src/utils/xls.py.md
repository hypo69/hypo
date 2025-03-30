# Модуль `src.utils.xls`

## Обзор

Модуль `src.utils.xls` предоставляет функциональность для конвертации файлов Excel (`.xls`) в формат JSON и наоборот. Он позволяет читать данные из Excel-файлов, преобразовывать их в JSON и сохранять JSON-данные в Excel-файлы. Модуль поддерживает работу с отдельными листами Excel, а также обеспечивает обработку ошибок для обеспечения надежной работы.

## Подробней

Этот модуль предназначен для облегчения обмена данными между Excel-файлами и JSON-форматом. Он предоставляет две основные функции: `read_xls_as_dict` для чтения данных из Excel и преобразования их в JSON и `save_xls_file` для сохранения JSON-данных в Excel-файл.

Расположение файла в проекте указывает на то, что он является частью утилит, используемых для обработки файлов, в частности, файлов Excel. Это может быть полезно для интеграции с другими частями проекта, где требуется обработка или хранение данных в формате Excel.

## Функции

### `read_xls_as_dict`

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

**Описание**: Читает Excel-файл и конвертирует его в JSON. Может конвертировать определенный лист и сохранять результат в JSON-файл. Обрабатывает ошибки.

**Параметры**:
- `xls_file` (str): Путь к Excel-файлу.
- `json_file` (str, optional): Путь к JSON-файлу для сохранения результата. По умолчанию `None`.
- `sheet_name` (Union[str, int], optional): Имя или индекс листа Excel для конвертации. По умолчанию `None`.

**Возвращает**:
- `Union[Dict, List[Dict], bool]`: Возвращает словарь или список словарей с данными из Excel-файла, или `False` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `Exception`: В случае других ошибок при обработке файла.

**Примеры**:

```python
data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
if data:
    print(data)
```

### `save_xls_file`

```python
def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """Saves JSON data to an Excel file. Handles errors gracefully."""
```

**Описание**: Сохраняет JSON-данные в Excel-файл. Обрабатывает ошибки.

**Параметры**:
- `data` (Dict[str, List[Dict]]): Словарь, где ключи - имена листов, а значения - списки словарей, представляющие строки данных.
- `file_path` (str): Путь для сохранения Excel-файла.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного сохранения, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: В случае ошибок при сохранении файла.

**Примеры**:

```python
data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
success = save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Successfully saved to output.xlsx")