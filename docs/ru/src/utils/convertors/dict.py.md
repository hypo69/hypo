# Модуль для конвертации между dict и SimpleNamespace объектами
=================================================================

Модуль содержит функции для рекурсивного преобразования словарей в объекты SimpleNamespace и наоборот, а также для экспорта данных в различные форматы.

## Обзор

Модуль `src.utils.convertors.dict` предоставляет инструменты для преобразования данных между различными форматами, такими как словари, объекты SimpleNamespace, XML, CSV, JSON, XLS, HTML и PDF. Он содержит функции для рекурсивного преобразования словарей в объекты SimpleNamespace и наоборот, а также для экспорта данных в различные форматы.

## Подробней

Модуль содержит набор функций для преобразования данных между различными форматами. Он предоставляет инструменты для работы со словарями, объектами SimpleNamespace, XML, CSV, JSON, XLS, HTML и PDF. Модуль может быть использован для экспорта данных в различные форматы, а также для преобразования данных из одного формата в другой.

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
    ...
```

**Назначение**: Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:
- `dict`: Обновленный словарь с замененными ключами.

**Как работает функция**:

Функция `replace_key_in_dict` рекурсивно обходит переданную структуру данных (словарь или список) и заменяет все вхождения ключа `old_key` на `new_key`. Если элемент структуры является словарем, функция проходит по всем его ключам. Если ключ совпадает с `old_key`, он заменяется на `new_key`. Если значением ключа является словарь или список, функция рекурсивно вызывается для этого значения. Если элемент структуры является списком, функция рекурсивно вызывается для каждого элемента списка.

```
A[Проверка типа данных]
|
B[Является ли data словарем?] -- Да --> C[Цикл по ключам словаря]
|   |
|   Нет -> H[Является ли data списком?] -- Да --> I[Цикл по элементам списка]
|   |   |       |
|   |   |       Нет -> J[Возврат data без изменений]
|   |   |       ↓
|   |   |       K[Рекурсивный вызов replace_key_in_dict для элемента списка]
|   |   |       ↓
|   |   |       L[Конец цикла по элементам списка]
|   |   |       ↓
|   |   |       M[Возврат обновленного списка]
|   |   |
|   |   Нет -> J[Возврат data без изменений]
|   ↓
|   D[Совпадает ли текущий ключ с old_key?] -- Да --> E[Замена ключа]
|   |
|   Нет -> F[Является ли значение словарем или списком?] -- Да --> G[Рекурсивный вызов replace_key_in_dict для значения]
|       |
|       Нет -> H[Продолжение цикла по ключам словаря]
|   ↓
|   K[Конец цикла по ключам словаря]
|   ↓
|   L[Возврат обновленного словаря]
↓
M[Функция завершена]
```

**Примеры**:

```python
# Пример 1: Простой словарь
data = {"old_key": "value"}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"new_key": "value"}

# Пример 2: Вложенный словарь
data = {"outer": {"old_key": "value"}}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"outer": {"new_key": "value"}}

# Пример 3: Список словарей
data = [{"old_key": "value1"}, {"old_key": "value2"}]
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

# Пример 4: Смешанная вложенная структура со списками и словарями
data = {"outer": [{"inner": {"old_key": "value"}}]}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"outer": [{"inner": {"new_key": "value"}}]}
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
    ...
```

**Назначение**: Рекурсивно преобразует словари в объекты SimpleNamespace.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.

**Как работает функция**:

Функция `dict2ns` рекурсивно преобразует переданные словари в объекты SimpleNamespace. Если входные данные являются словарем, функция проходит по всем его элементам. Если значение элемента является словарем, функция рекурсивно вызывает саму себя для этого значения. Если значением элемента является список, функция преобразует каждый элемент списка в SimpleNamespace, если это возможно. Если входные данные являются списком, функция преобразует каждый элемент списка в SimpleNamespace, если это возможно.

```
A[Проверка типа данных]
|
B[Является ли data словарем?] -- Да --> C[Цикл по элементам словаря]
|   |
|   Нет -> H[Является ли data списком?] -- Да --> I[Преобразование каждого элемента списка]
|   |   |       |
|   |   |       Нет -> J[Возврат data без изменений]
|   |   |       ↓
|   |   |       K[Рекурсивный вызов dict2ns для элемента списка]
|   |   |       ↓
|   |   |       L[Конец преобразования каждого элемента списка]
|   |   |       ↓
|   |   |       M[Возврат преобразованного списка]
|   |   |
|   |   Нет -> J[Возврат data без изменений]
|   ↓
|   D[Проверка типа значения]
|   ↓
|   E[Является ли значение словарем?] -- Да --> F[Рекурсивный вызов dict2ns для значения]
|   |
|   Нет -> G[Является ли значение списком?]
|       |
|       Нет -> H[Продолжение цикла по элементам словаря]
|   ↓
|   K[Конец цикла по элементам словаря]
|   ↓
|   L[Преобразование словаря в SimpleNamespace]
|   ↓
|   M[Возврат SimpleNamespace]
↓
N[Функция завершена]
```

**Примеры**:

```python
data = {"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001"}}
ns = dict2ns(data)
print(ns.name)  # Вывод: John
print(ns.address.city)  # Вывод: New York
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
    ...
```

**Назначение**: Преобразует словарь в XML строку.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: XML строка, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

**Как работает функция**:

Функция `dict2xml` преобразует переданный словарь в XML строку. Она использует вспомогательные функции для обработки простых и сложных типов данных, а также для создания атрибутов XML элементов. Функция создает XML документ, добавляет в него корневой элемент и возвращает XML строку.

```
A[Создание XML документа]
|
B[Проверка количества корневых узлов]
|
C[Больше одного корневого узла?] -- Да --> D[Выброс исключения]
|   |
|   Нет -> E[Обработка корневого элемента]
|   ↓
|   F[Добавление корневого элемента в документ]
|   ↓
|   G[Преобразование документа в XML строку]
|   ↓
|   H[Возврат XML строки]
↓
I[Функция завершена]
```

**Внутренние функции**:

#### `_process_simple`

```python
def _process_simple(doc, tag, tag_value):
    """
    Generate a node for simple types (int, str).

    Args:
        doc (xml.dom.minidom.Document): XML document object.
        tag (str): Tag name for the XML element.
        tag_value (Any): Value of the tag.

    Returns:
        xml.dom.minidom.Element: Node representing the tag and value.
    """
    ...
```

**Назначение**: Создает узел для простых типов (int, str).

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML документа.
- `tag` (str): Имя тега для XML элемента.
- `tag_value` (Any): Значение тега.

**Возвращает**:
- `xml.dom.minidom.Element`: Узел, представляющий тег и значение.

#### `_process_attr`

```python
def _process_attr(doc, attr_value: Dict[str, Any]):
    """
    Generate attributes for an XML element.

    Args:
        doc (xml.dom.minidom.Document): XML document object.
        attr_value (Dict[str, Any]): Dictionary of attributes.

    Returns:
        List[xml.dom.minidom.Attr]: List of attributes for the XML element.
    """
    ...
```

**Назначение**: Создает атрибуты для XML элемента.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML документа.
- `attr_value` (Dict[str, Any]): Словарь атрибутов.

**Возвращает**:
- `List[xml.dom.minidom.Attr]`: Список атрибутов для XML элемента.

#### `_process_complex`

```python
def _process_complex(doc, children):
    """
    Generate nodes for complex types like lists or dicts.

    Args:
        doc (xml.dom.minidom.Document): XML document object.
        children (List[Tuple[str, Any]]): List of tag-value pairs.

    Returns:
        Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]: List of child nodes and attributes.
    """
    ...
```

**Назначение**: Создает узлы для сложных типов, таких как списки или словари.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML документа.
- `children` (List[Tuple[str, Any]]): Список пар тег-значение.

**Возвращает**:
- `Tuple[List[xml.dom.minidom.Element], List[xml.dom.minidom.Attr]]`: Список дочерних узлов и атрибутов.

#### `_process`

```python
def _process(doc, tag, tag_value):
    """
    Generate XML DOM object for a tag and its value.

    Args:
        doc (xml.dom.minidom.Document): XML document object.
        tag (str): Tag name for the XML element.
        tag_value (Any): Value of the tag.

    Returns:
        xml.dom.minidom.Element | List[xml.dom.minidom.Element]: Node or list of nodes for the tag and value.
    """
    ...
```

**Назначение**: Создает XML DOM объект для тега и его значения.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML документа.
- `tag` (str): Имя тега для XML элемента.
- `tag_value` (Any): Значение тега.

**Возвращает**:
- `xml.dom.minidom.Element | List[xml.dom.minidom.Element]`: Узел или список узлов для тега и значения.

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

xml_output = dict2xml(json_data)
print(xml_output)
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
    ...
```

**Назначение**: Сохраняет данные словаря или SimpleNamespace в CSV файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в CSV файл.
- `file_path` (str | Path): Путь к CSV файлу.

**Возвращает**:
- `bool`: True, если файл был успешно сохранен, False в противном случае.

**Как работает функция**:

Функция `dict2csv` сохраняет переданные данные (словарь или SimpleNamespace) в CSV файл. Для сохранения данных используется функция `save_csv_file`. Функция возвращает True, если файл был успешно сохранен, и False в противном случае.

```
A[Сохранение данных в CSV файл]
|
B[save_csv_file(data, file_path)]
|
C[Возврат результата сохранения]
↓
D[Функция завершена]
```

**Примеры**:

```python
data = {"name": "John", "age": 30, "city": "New York"}
file_path = "data.csv"
result = dict2csv(data, file_path)
print(result)  # Вывод: True
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
    ...
```

**Назначение**: Сохраняет данные словаря или SimpleNamespace в XLS файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в XLS файл.
- `file_path` (str | Path): Путь к XLS файлу.

**Возвращает**:
- `bool`: True, если файл был успешно сохранен, False в противном случае.

**Как работает функция**:

Функция `dict2xls` сохраняет переданные данные (словарь или SimpleNamespace) в XLS файл. Для сохранения данных используется функция `save_xls_file`. Функция возвращает True, если файл был успешно сохранен, и False в противном случае.

```
A[Сохранение данных в XLS файл]
|
B[save_xls_file(data, file_path)]
|
C[Возврат результата сохранения]
↓
D[Функция завершена]
```

**Примеры**:

```python
data = {"name": "John", "age": 30, "city": "New York"}
file_path = "data.xls"
result = dict2xls(data, file_path)
print(result)  # Вывод: True
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
    ...
```

**Назначение**: Преобразует словарь или SimpleNamespace объект в HTML таблицу.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: HTML строка, представляющая входной словарь.

**Как работает функция**:

Функция `dict2html` преобразует переданные данные (словарь или SimpleNamespace) в HTML таблицу. Она использует вспомогательную функцию `dict_to_html_table` для рекурсивного преобразования словаря в HTML таблицу. Функция возвращает HTML строку, представляющую входной словарь.

```
A[Проверка типа данных]
|
B[Является ли data SimpleNamespace?] -- Да --> C[Преобразование в словарь]
|   |
|   Нет -> D[Рекурсивное преобразование словаря в HTML таблицу]
|   ↓
|   E[dict_to_html_table(data)]
|   ↓
|   F[Формирование HTML структуры с таблицей]
|   ↓
|   G[Возврат HTML строки]
↓
H[Функция завершена]
```

**Внутренние функции**:

#### `dict_to_html_table`

```python
def dict_to_html_table(data: dict, depth: int = 0) -> str:
    """
    Recursively convert dictionary to HTML table.

    Args:
        data (dict): The dictionary data to convert.
        depth (int, optional): The depth of recursion, used for nested tables. Defaults to 0.

    Returns:
        str: The HTML table as a string.
    """
    ...
```

**Назначение**: Рекурсивно преобразует словарь в HTML таблицу.

**Параметры**:
- `data` (dict): Данные словаря для преобразования.
- `depth` (int, optional): Глубина рекурсии, используется для вложенных таблиц. По умолчанию 0.

**Возвращает**:
- `str`: HTML таблица в виде строки.

**Примеры**:

```python
data = {"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001"}}
html = dict2html(data)
print(html)
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

**Назначение**: Пример использования функции `json2xml`. <инструкция для модели gemini:Тут ты описывешь как работает функция, ее входные и выходные параметры, и примеры использования, если надо - создай новые примеры.>

**Параметры**:
- Отсутствуют

**Возвращает**:
- Отсутствует

**Как работает функция**:

Функция `example_json2xml` демонстрирует пример использования функции `json2xml` для преобразования JSON данных в XML формат. Она создает пример JSON структуры данных, содержащей информацию о продукте, такую как имя, цена, группа правил налогообложения и категория по умолчанию. Затем функция вызывает `json2xml` с этими данными и выводит полученный XML результат в консоль.

```
A[Определение примера JSON структуры данных]
|
B[Вызов функции json2xml с JSON данными]
|
C[Вывод полученного XML результата в консоль]
↓
D[Функция завершена]
```

**Примеры**:

```python
example_json2xml()