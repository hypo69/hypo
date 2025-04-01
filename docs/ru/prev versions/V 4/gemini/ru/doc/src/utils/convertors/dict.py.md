# Модуль `dict`

## Обзор

Модуль `dict` содержит функции для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно, а также для экспорта данных в различные форматы, такие как `XML`, `CSV`, `JSON`, `XLS`, `HTML` и `PDF`.

## Подробней

Этот модуль предоставляет инструменты для работы с данными, представленными в виде словарей, и позволяет преобразовывать их в другие форматы для удобства использования в различных целях, таких как хранение, передача и визуализация данных. Он используется для преобразования структур данных между различными форматами, облегчая интеграцию и взаимодействие между различными системами и приложениями.

## Функции

### `replace_key_in_dict`

```python
def replace_key_in_dict(data: dict | list, old_key: str, new_key: str) -> dict:
    """
    Args:
        data (dict | list): The dictionary or list where key replacement occurs.
        old_key (str): The key to be replaced.
        new_key (str): The new key.

    Returns:
        dict: The updated dictionary with replaced keys.

    Example Usage:

        replace_key_in_json(data, 'name', 'category_name')

        # Example 1: Simple dictionary
        data = {"old_key": "value"}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"new_key": "value"}

        # Example 2: Nested dictionary
        data = {"outer": {"old_key": "value"}}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": {"new_key": "value"}}

        # Example 3: List of dictionaries
        data = [{"old_key": "value1"}, {"old_key": "value2"}]
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes [{"new_key": "value1"}, {"new_key": "value2"}]

        # Example 4: Mixed nested structure with lists and dictionaries
        data = {"outer": [{"inner": {"old_key": "value"}}]}
        updated_data = replace_key_in_json(data, "old_key", "new_key")
        # updated_data becomes {"outer": [{"inner": {"new_key": "value"}}]}

    """
    ...
```

**Описание**: Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:
- `dict`: Обновленный словарь с замененными ключами.

**Как работает функция**:
Функция `replace_key_in_dict` рекурсивно проходит по словарю или списку и заменяет все вхождения ключа `old_key` на `new_key`. Если значением элемента является словарь или список, функция вызывает себя рекурсивно для этого значения.

### `dict2ns`

```python
def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """
    Args:
        data (Dict[str, Any] | List[Any]): The data to convert.

    Returns:
        Any: Converted data as a SimpleNamespace or a list of SimpleNamespace.
    """
    ...
```

**Описание**: Рекурсивно преобразует словари в `SimpleNamespace`.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

**Как работает функция**:

Функция `dict2ns` рекурсивно преобразует словарь в объект `SimpleNamespace`. Если значением элемента является словарь, функция вызывает себя рекурсивно для этого значения. Если значением элемента является список, функция преобразует каждый элемент списка в `SimpleNamespace`, если это возможно.

### `dict2xml`

```python
def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Args:
        data (Dict[str, Any]): The data to convert to XML.
        encoding (str, optional): Data encoding. Defaults to 'UTF-8'.

    Returns:
        str: The XML string representing the input dictionary.

    Raises:
        Exception: If more than one root node is provided.
    """
    ...
```

**Описание**: Генерирует XML строку из словаря.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: XML строка, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

**Как работает функция**:

Функция `dict2xml` преобразует словарь в XML строку. Она использует рекурсивные вызовы для обработки вложенных словарей и списков. Функция создает XML документ и добавляет в него элементы и атрибуты на основе данных из словаря.

### `dict2csv`

```python
def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Args:
        data (dict | SimpleNamespace): The data to save to a CSV file.
        file_path (str | Path): Path to the CSV file.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    ...
```

**Описание**: Сохраняет данные из словаря или `SimpleNamespace` в CSV файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в CSV файл.
- `file_path` (str | Path): Путь к CSV файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Как работает функция**:

Функция `dict2csv` использует функцию `save_csv_file` из модуля `src.utils.csv` для сохранения данных в CSV файл. Она принимает словарь или объект `SimpleNamespace` и путь к файлу в качестве аргументов.

### `dict2xls`

```python
def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Args:
        data (dict | SimpleNamespace): The data to save to an XLS file.
        file_path (str | Path): Path to the XLS file.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    ...
```

**Описание**: Сохраняет данные из словаря или `SimpleNamespace` в XLS файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в XLS файл.
- `file_path` (str | Path): Путь к XLS файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Как работает функция**:

Функция `dict2xls` использует функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в XLS файл. Она принимает словарь или объект `SimpleNamespace` и путь к файлу в качестве аргументов.

### `dict2html`

```python
def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Args:
        data (dict | SimpleNamespace): The data to convert to HTML.
        encoding (str, optional): Data encoding. Defaults to 'UTF-8'.

    Returns:
        str: The HTML string representing the input dictionary.
    """
    ...
```

**Описание**: Генерирует HTML таблицу из словаря или объекта `SimpleNamespace`.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: HTML строка, представляющая входной словарь.

**Как работает функция**:

Функция `dict2html` преобразует словарь в HTML таблицу. Она использует рекурсивную функцию `dict_to_html_table` для обработки вложенных словарей и списков. Функция создает HTML документ с таблицей, содержащей данные из словаря.

### `dict2pdf`

```python
    """
    Save dictionary data to a PDF file.

    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
    ...
```

**Описание**: Сохраняет данные словаря в PDF файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь для преобразования в PDF.
- `file_path` (str | Path): Путь к выходному PDF файлу.

**Как работает функция**:

Функция `dict2pdf` преобразует словарь в PDF файл. Она создает PDF документ и добавляет в него текст на основе данных из словаря. Функция поддерживает создание новых страниц, если данные не помещаются на одной странице.

### `example_json2xml`

```python
def example_json2xml():
    """
    
    """
    ...
```

**Описание**: пример использования `json2xml`

**Как работает функция**:
Функция `example_json2xml` показывает пример преобразования `json` в `xml`

```
flowchart TB
    A[Начало] --> B{Данные json};
    B --> C{Вызов функции json2xml(json)};
    C --> D{Результат xml};
    D --> E[Конец]