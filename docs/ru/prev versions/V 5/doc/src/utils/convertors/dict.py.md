# Модуль для конвертации `dict` в различные форматы

## Обзор

Модуль `src.utils.convertors.dict` предоставляет инструменты для преобразования данных между форматом словаря (`dict`) и `SimpleNamespace`, а также для экспорта данных в различные форматы, такие как XML, CSV, JSON, XLS, HTML и PDF. Он содержит функции для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно.

## Подробней

Этот модуль предназначен для упрощения работы с данными, представленными в виде словарей, и их преобразования в другие форматы, необходимые для различных задач, таких как экспорт данных, создание отчетов и т.д. Модуль содержит функции для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно, а также для экспорта данных в различные форматы.

## Функции

### `replace_key_in_dict`

```python
def replace_key_in_dict(data, old_key, new_key) -> dict:
    """
    Recursively replaces a key in a dictionary or list.
    
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
```

**Описание**: Рекурсивно заменяет ключ `old_key` на `new_key` в словаре или списке.

**Как работает функция**: 
Функция проверяет, является ли входной параметр `data` словарем или списком. Если это словарь, она проходит по всем ключам словаря и заменяет `old_key` на `new_key`. Если значением ключа является словарь или список, функция рекурсивно вызывает себя для этого значения. Если `data` является списком, функция проходит по всем элементам списка и рекурсивно вызывает себя для каждого элемента.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором производится замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:
- `dict`: Обновленный словарь с замененными ключами.

**Примеры**:

```python
data = {"old_key": "value"}
updated_data = replace_key_in_json(data, "old_key", "new_key")
# updated_data становится {"new_key": "value"}

data = {"outer": {"old_key": "value"}}
updated_data = replace_key_in_json(data, "old_key", "new_key")
# updated_data становится {"outer": {"new_key": "value"}}

data = [{"old_key": "value1"}, {"old_key": "value2"}]
updated_data = replace_key_in_json(data, "old_key", "new_key")
# updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

data = {"outer": [{"inner": {"old_key": "value"}}]}
updated_data = replace_key_in_json(data, "old_key", "new_key")
# updated_data становится {"outer": [{"inner": {"new_key": "value"}}]}
```

### `dict2pdf`

```python
def dict2pdf(data: dict | SimpleNamespace, file_path: str | Path):
    """
    Save dictionary data to a PDF file.

    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
```

**Описание**: Сохраняет данные словаря в PDF-файл.

**Как работает функция**:
Функция преобразует словарь в PDF-файл. Если входные данные представлены в виде `SimpleNamespace`, они преобразуются в словарь. Затем создается PDF-файл, в который построчно записываются ключи и значения словаря. Если места на странице не хватает, создается новая страница.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь для преобразования в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Примеры**:
```python
data = {'name': 'Product', 'price': 10.0}
dict2pdf(data, 'product.pdf')
```

### `dict2ns`

```python
def dict2ns(data: Dict[str, Any] | List[Any]) -> Any:
    """
    Recursively convert dictionaries to SimpleNamespace.

    Args:
        data (Dict[str, Any] | List[Any]): The data to convert.

    Returns:
        Any: Converted data as a SimpleNamespace or a list of SimpleNamespace.
    """
```

**Описание**: Рекурсивно преобразует словари в `SimpleNamespace`.

**Как работает функция**:
Функция рекурсивно преобразует словарь в объект `SimpleNamespace`. Если значением ключа является словарь, функция рекурсивно вызывает себя для этого значения. Если значением ключа является список, функция проходит по всем элементам списка и рекурсивно вызывает себя для каждого элемента, если элемент является словарем.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

**Примеры**:

```python
data = {'name': 'Product', 'price': 10.0}
ns = dict2ns(data)
print(ns.name)  # Вывод: Product
```

### `dict2xml`

```python
def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Generate an XML string from a dictionary.

    Args:
        data (Dict[str, Any]): The data to convert to XML.
        encoding (str, optional): Data encoding. Defaults to 'UTF-8'.

    Returns:
        str: The XML string representing the input dictionary.

    Raises:
        Exception: If more than one root node is provided.
    """
```

**Описание**: Генерирует XML-строку из словаря.

**Как работает функция**:
Функция преобразует словарь в XML-строку. Она использует внутренние функции `_process_simple`, `_process_attr`, `_process_complex` и `_process` для рекурсивной обработки словаря и создания XML-элементов. Функция `_process_simple` создает узлы для простых типов данных (int, str). Функция `_process_attr` создает атрибуты для XML-элементов. Функция `_process_complex` создает узлы для сложных типов данных, таких как списки или словари. Функция `_process` является основной функцией, которая вызывает другие функции для обработки различных типов данных.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: XML-строка, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

**Примеры**:

```python
data = {'product': {'name': 'Product', 'price': 10.0}}
xml_string = dict2xml(data)
print(xml_string)
```

### `dict2csv`

```python
def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Save dictionary or SimpleNamespace data to a CSV file.

    Args:
        data (dict | SimpleNamespace): The data to save to a CSV file.
        file_path (str | Path): Path to the CSV file.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
```

**Описание**: Сохраняет данные из словаря или `SimpleNamespace` в CSV-файл.

**Как работает функция**:
Функция вызывает функцию `save_csv_file` из модуля `src.utils.csv` для сохранения данных в CSV-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в CSV-файл.
- `file_path` (str | Path): Путь к CSV-файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Примеры**:

```python
data = {'name': 'Product', 'price': 10.0}
success = dict2csv(data, 'product.csv')
if success:
    print('CSV file saved successfully.')
```

### `dict2xls`

```python
def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Save dictionary or SimpleNamespace data to an XLS file.

    Args:
        data (dict | SimpleNamespace): The data to save to an XLS file.
        file_path (str | Path): Path to the XLS file.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
```

**Описание**: Сохраняет данные из словаря или `SimpleNamespace` в XLS-файл.

**Как работает функция**:
Функция вызывает функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в XLS-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
- `file_path` (str | Path): Путь к XLS-файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Примеры**:

```python
data = {'name': 'Product', 'price': 10.0}
success = dict2xls(data, 'product.xls')
if success:
    print('XLS file saved successfully.')
```

### `dict2html`

```python
def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Generate an HTML table string from a dictionary or SimpleNamespace object.

    Args:
        data (dict | SimpleNamespace): The data to convert to HTML.
        encoding (str, optional): Data encoding. Defaults to 'UTF-8'.

    Returns:
        str: The HTML string representing the input dictionary.
    """
```

**Описание**: Генерирует HTML-таблицу из словаря или объекта `SimpleNamespace`.

**Как работает функция**:
Функция преобразует словарь или `SimpleNamespace` в HTML-таблицу. Если входные данные представлены в виде `SimpleNamespace`, они преобразуются в словарь. Затем функция `dict_to_html_table` рекурсивно преобразует словарь в HTML-таблицу.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: HTML-строка, представляющая входной словарь.

**Примеры**:

```python
data = {'name': 'Product', 'price': 10.0}
html_string = dict2html(data)
print(html_string)
```

### `example_json2xml`

```python
def example_json2xml():

    # Example usage
    json_data = {
        "product": {
            "name": {
                "language": [
                    {
                        "@id": "1",
                        "#text": "Test Product"
                    },
                    {
                        "@id": "2",
                        "#text": "Test Product"
                    },
                    {
                        "@id": "3",
                        "#text": "Test Product"
                    }
                ]
            },
            "price": "10.00",
            "id_tax_rules_group": "13",
            "id_category_default": "2"
        }
    }

    xml_output = json2xml(json_data)
    print(xml_output)
```

**Описание**: Пример использования функции `json2xml` (не существует в предоставленном коде).

**Как работает функция**:
Функция содержит пример данных в формате JSON и вызывает функцию `json2xml` (которой нет в предоставленном коде) для преобразования JSON в XML. Результат выводится на экран.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Примеры**:
```python
example_json2xml()