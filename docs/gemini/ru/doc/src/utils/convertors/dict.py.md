# Модуль `dict`

## Обзор

Модуль `dict` содержит функции для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно, а также для экспорта данных в различные форматы, такие как XML, CSV, JSON, XLS, HTML и PDF.

## Подробней

Этот модуль предоставляет набор инструментов для работы с данными, представленными в виде словарей и объектов `SimpleNamespace`. Он облегчает преобразование данных между различными форматами, что полезно при интеграции с различными системами и сервисами. Модуль включает функции для сохранения данных в файлы различных форматов, а также для генерации HTML-таблиц и PDF-документов на основе данных словаря.

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

**Описание**: Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:

- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:

- `dict`: Обновленный словарь с замененными ключами.

**Примеры**:

```python
data = {"old_key": "value"}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
print(updated_data)  # {"new_key": "value"}

data = {"outer": {"old_key": "value"}}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
print(updated_data)  # {"outer": {"new_key": "value"}}

data = [{"old_key": "value1"}, {"old_key": "value2"}]
updated_data = replace_key_in_dict(data, "old_key", "new_key")
print(updated_data)  # [{"new_key": "value1"}, {"new_key": "value2"}]

data = {"outer": [{"inner": {"old_key": "value"}}]}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
print(updated_data)  # {"outer": [{"inner": {"new_key": "value"}}]}
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

**Описание**: Рекурсивно преобразует словари в объекты `SimpleNamespace`.

**Параметры**:

- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:

- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

**Примеры**:

```python
data = {"key1": "value1", "key2": {"nested_key": "nested_value"}}
ns = dict2ns(data)
print(ns.key1)  # value1
print(ns.key2.nested_key)  # nested_value

data = [{"key1": "value1"}, {"key2": "value2"}]
ns_list = dict2ns(data)
print(ns_list[0].key1)  # value1
print(ns_list[1].key2)  # value2
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

**Параметры**:

- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:

- `str`: XML-строка, представляющая входной словарь.

**Вызывает исключения**:

- `Exception`: Если предоставлено более одного корневого узла.

**Примеры**:

```python
data = {"root": {"key1": "value1", "key2": "value2"}}
xml_string = dict2xml(data)
print(xml_string)
# <?xml version="1.0" encoding="UTF-8"?>
# <root><key1>value1</key1><key2>value2</key2></root>

data = {"root": {"key1": "value1", "key2": {"attrs": {"attr1": "attr_value"}, "value": "value2"}}}
xml_string = dict2xml(data)
print(xml_string)
# <?xml version="1.0" encoding="UTF-8"?>
# <root key2="value2"><key1>value1</key1></root>
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

**Описание**: Сохраняет данные словаря или `SimpleNamespace` в CSV-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для сохранения в CSV-файл.
- `file_path` (str | Path): Путь к CSV-файлу.

**Возвращает**:

- `bool`: `True`, если файл был успешно сохранен, `False` в противном случае.

**Примеры**:

```python
data = {"key1": "value1", "key2": "value2"}
file_path = "data.csv"
result = dict2csv(data, file_path)
print(result)  # True
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

**Описание**: Сохраняет данные словаря или `SimpleNamespace` в XLS-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
- `file_path` (str | Path): Путь к XLS-файлу.

**Возвращает**:

- `bool`: `True`, если файл был успешно сохранен, `False` в противном случае.

**Примеры**:

```python
data = {"key1": "value1", "key2": "value2"}
file_path = "data.xls"
result = dict2xls(data, file_path)
print(result)  # True
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

**Описание**: Генерирует HTML-строку таблицы из словаря или объекта `SimpleNamespace`.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:

- `str`: HTML-строка, представляющая входной словарь.

**Примеры**:

```python
data = {"key1": "value1", "key2": {"nested_key": "nested_value"}}
html_string = dict2html(data)
print(html_string)
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="UTF-8">
# <title>Dictionary to HTML</title>
# </head>
# <body>
# <table border="1" cellpadding="5" cellspacing="0">
# <tr>
# <td><strong>key1</strong></td>
# <td>value1</td>
# </tr>
# <tr>
# <td><strong>key2</strong></td>
# <td>
# <table border="1" cellpadding="5" cellspacing="0">
# <tr>
# <td><strong>nested_key</strong></td>
# <td>nested_value</td>
# </tr>
# </table>
# </td>
# </tr>
# </table>
# </body>
# </html>
```
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
```python
if __name__ ==  '__main__':
    ...
    #example_json2xml()
```
```
### example_json2xml
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

**Описание**: пример использования функции `json2xml`.

**Параметры**:

- Нет

**Возвращает**:

- Нет

**Примеры**:
```python
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
```
```
xml_output = json2xml(json_data)
    print(xml_output)