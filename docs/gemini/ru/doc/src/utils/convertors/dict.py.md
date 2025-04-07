# Модуль `src.utils.convertors.dict`

## Обзор

Модуль предоставляет инструменты для преобразования данных между форматами `dict` (словарь) и `SimpleNamespace`, а также для экспорта данных в различные форматы, такие как `XML`, `CSV`, `JSON`, `XLS`, `HTML` и `PDF`.

## Подробней

Этот модуль содержит набор функций для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно. Кроме того, он предоставляет функции для экспорта данных в различные форматы файлов, облегчая интеграцию и обмен данными между различными системами и приложениями.

## Функции

### `replace_key_in_dict`

```python
def replace_key_in_dict(data, old_key, new_key) -> dict:
    """
    Рекурсивно заменяет ключ в словаре или списке.

    Args:
        data (dict | list): Словарь или список, в котором происходит замена ключа.
        old_key (str): Ключ, который нужно заменить.
        new_key (str): Новый ключ.

    Returns:
        dict: Обновленный словарь с замененными ключами.

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

**Назначение**: Рекурсивно заменяет ключ `old_key` на `new_key` в словаре или списке.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором будет произведена замена ключа.
- `old_key` (str): Ключ, который требуется заменить.
- `new_key` (str): Новый ключ, на который будет заменен `old_key`.

**Возвращает**:
- `dict`: Обновленный словарь с замененными ключами.

**Как работает функция**:
1. Функция проверяет, является ли входной параметр `data` словарем или списком.
2. Если `data` является словарем, функция проходит по всем ключам словаря.
3. Если текущий ключ совпадает с `old_key`, он заменяется на `new_key` с сохранением значения.
4. Если значением текущего ключа является словарь или список, функция рекурсивно вызывает саму себя для этого значения.
5. Если `data` является списком, функция проходит по всем элементам списка и рекурсивно вызывает саму себя для каждого элемента.
6. В конце функция возвращает обновленный словарь.

```
  A (Проверка типа данных)
  |
  ├── B (Если словарь)
  |   │
  |   ├── C (Итерация по ключам)
  |   |   │
  |   |   ├── D (Совпадает ли ключ с old_key?)
  |   |   |   │
  |   |   |   └── E (Замена ключа)
  |   |   │
  |   |   └── F (Является ли значение словарем/списком?)
  |   |       │
  |   |       └── G (Рекурсивный вызов)
  |   │
  ├── H (Если список)
  |   │
  |   └── I (Итерация по элементам списка)
  |       │
  |       └── J (Рекурсивный вызов)
  |
  └── K (Возврат обновленных данных)
```

**Примеры**:
```python
data = {"old_key": "value"}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"new_key": "value"}

data = {"outer": {"old_key": "value"}}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"outer": {"new_key": "value"}}

data = [{"old_key": "value1"}, {"old_key": "value2"}]
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

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
```

**Назначение**: Рекурсивно преобразует словари в объекты `SimpleNamespace`.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

**Как работает функция**:
1. Функция проверяет, является ли входной параметр `data` словарем или списком.
2. Если `data` является словарем, функция проходит по всем элементам словаря.
3. Если значением элемента является словарь, функция рекурсивно вызывает саму себя для этого значения.
4. Если значением элемента является список, функция проходит по всем элементам списка и рекурсивно вызывает саму себя для каждого элемента, являющегося словарем.
5. В конце функция возвращает объект `SimpleNamespace`, созданный на основе словаря, или список объектов `SimpleNamespace`.

```
A (Проверка типа данных)
|
├── B (Если словарь)
|   │
|   ├── C (Итерация по элементам)
|   |   │
|   |   ├── D (Значение - словарь?)
|   |   |   │
|   |   |   └── E (Рекурсивный вызов)
|   |   │
|   |   └── F (Значение - список?)
|   |       │
|   |       └── G (Итерация по списку, рекурсивный вызов для словарей)
|   │
|   └── H (Создание SimpleNamespace)
|
└── I (Если список)
    │
    └── J (Итерация по списку, рекурсивный вызов для словарей)
```

**Примеры**:

```python
data = {'a': 1, 'b': {'c': 2, 'd': 3}}
ns = dict2ns(data)
print(ns.a) # Вывод: 1
print(ns.b.c) # Вывод: 2

data = [{'a': 1}, {'b': 2}]
ns_list = dict2ns(data)
print(ns_list[0].a) # Вывод: 1
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

**Назначение**: Генерирует XML-строку из словаря.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: XML-строка, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

**Как работает функция**:
1. Функция определяет внутренние функции `_process_simple`, `_process_attr`, `_process_complex` и `_process` для рекурсивной обработки словаря и создания XML-элементов.
2. Функция `_process_simple` создает XML-узел для простых типов данных (int, str).
3. Функция `_process_attr` создает атрибуты для XML-элемента.
4. Функция `_process_complex` создает узлы для сложных типов данных, таких как списки или словари.
5. Функция `_process` является основной функцией, которая определяет тип данных и вызывает соответствующие функции для их обработки.
6. Функция создает XML-документ и вызывает функцию `_process_complex` для обработки корневого узла.
7. Если в словаре больше одного корневого узла, выбрасывается исключение.
8. В конце функция возвращает XML-строку.

```
A (Создание XML документа)
|
├── B (Проверка количества корневых узлов)
|   │
|   └── C (Если больше одного корневого узла - исключение)
|
└── D (Обработка корневого узла функцией _process_complex)
    │
    └── E (Рекурсивная обработка данных функциями _process, _process_simple, _process_attr)
    │
    └── F (Возврат XML строки)
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
```

**Назначение**: Создает узел для простых типов данных (int, str).

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML-документа.
- `tag` (str): Имя тега для XML-элемента.
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
```

**Назначение**: Создает атрибуты для XML-элемента.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML-документа.
- `attr_value` (Dict[str, Any]): Словарь атрибутов.

**Возвращает**:
- `List[xml.dom.minidom.Attr]`: Список атрибутов для XML-элемента.

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
```

**Назначение**: Создает узлы для сложных типов данных, таких как списки или словари.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML-документа.
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
```

**Назначение**: Создает XML DOM объект для тега и его значения.

**Параметры**:
- `doc` (xml.dom.minidom.Document): Объект XML-документа.
- `tag` (str): Имя тега для XML-элемента.
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
```

**Назначение**: Сохраняет данные из словаря или `SimpleNamespace` в CSV-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в CSV-файл.
- `file_path` (str | Path): Путь к CSV-файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Как работает функция**:
1. Функция вызывает функцию `save_csv_file` из модуля `src.utils.csv` для сохранения данных в CSV-файл.
2. Функция возвращает результат вызова `save_csv_file`.

```
A (Вызов функции save_csv_file)
|
└── B (Возврат результата)
```

**Примеры**:
```python
data = {'a': 1, 'b': 2, 'c': 3}
file_path = 'data.csv'
result = dict2csv(data, file_path)
print(result)  # Вывод: True или False в зависимости от успеха сохранения
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

**Назначение**: Сохраняет данные из словаря или `SimpleNamespace` в XLS-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
- `file_path` (str | Path): Путь к XLS-файлу.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Как работает функция**:
1. Функция вызывает функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в XLS-файл.
2. Функция возвращает результат вызова `save_xls_file`.

```
A (Вызов функции save_xls_file)
|
└── B (Возврат результата)
```

**Примеры**:
```python
data = {'a': 1, 'b': 2, 'c': 3}
file_path = 'data.xls'
result = dict2xls(data, file_path)
print(result)  # Вывод: True или False в зависимости от успеха сохранения
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

**Назначение**: Генерирует HTML-строку таблицы из словаря или объекта `SimpleNamespace`.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: HTML-строка, представляющая входной словарь.

**Как работает функция**:
1. Функция определяет внутреннюю функцию `dict_to_html_table` для рекурсивного преобразования словаря в HTML-таблицу.
2. Если входные данные являются объектом `SimpleNamespace`, они преобразуются в словарь.
3. Функция вызывает `dict_to_html_table` для преобразования данных в HTML-таблицу.
4. Функция создает HTML-документ, содержащий HTML-таблицу, и возвращает его в виде строки.

```
A (Проверка типа данных)
|
└── B (Если SimpleNamespace, преобразование в словарь)
    │
    └── C (Вызов функции dict_to_html_table)
    │
    └── D (Создание HTML-документа)
    │
    └── E (Возврат HTML-строки)
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
```

**Назначение**: Рекурсивно преобразует словарь в HTML-таблицу.

**Параметры**:
- `data` (dict): Данные словаря для преобразования.
- `depth` (int, optional): Глубина рекурсии, используется для вложенных таблиц. По умолчанию `0`.

**Возвращает**:
- `str`: HTML-таблица в виде строки.

**Примеры**:

```python
data = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': [4, 5, 6]}
html_output = dict2html(data)
print(html_output)
```
```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dictionary to HTML</title>
</head>
<body>
<table border="1" cellpadding="5" cellspacing="0">
<tr>
<td><strong>a</strong></td>
<td>1</td>
</tr>
<tr>
<td><strong>b</strong></td>
<td><table border="1" cellpadding="5" cellspacing="0">
<tr>
<td><strong>c</strong></td>
<td>2</td>
</tr>
<tr>
<td><strong>d</strong></td>
<td>3</td>
</tr>
</table></td>
</tr>
<tr>
<td><strong>e</strong></td>
<td><ul>
<li>4</li>
<li>5</li>
<li>6</li>
</ul></td>
</tr>
</table>
</body>
</html>
```
### `dict2pdf`

```python
    """
    Save dictionary data to a PDF file.

    Args:
        data (dict | SimpleNamespace): The dictionary to convert to PDF.
        file_path (str | Path): Path to the output PDF file.
    """
```

**Назначение**: Сохраняет данные из словаря в PDF-файл.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь, который нужно преобразовать в PDF.
- `file_path` (str | Path): Путь к выходному PDF-файлу.

**Как работает функция**:

1.  Если входные данные являются объектом `SimpleNamespace`, они преобразуются в словарь.
2.  Создается объект `canvas.Canvas` из библиотеки `reportlab` для работы с PDF.
3.  Устанавливается шрифт "Helvetica" размером 12.
4.  Происходит итерация по элементам словаря, где для каждого элемента создается строка вида `"ключ: значение"`.
5.  Строка добавляется на PDF-страницу с помощью метода `drawString`.
6.  Координата `y` уменьшается на 20 для следующей строки.
7.  Если места на странице недостаточно, создается новая страница.
8.  PDF-файл сохраняется.

```
A (Проверка типа данных)
|
└── B (Преобразование SimpleNamespace в словарь, если необходимо)
    │
    └── C (Создание PDF-документа)
    │
    └── D (Установка шрифта)
    │
    └── E (Итерация по элементам словаря)
    │
    └── F (Добавление строк на страницу)
    │
    └── G (Проверка наличия места на странице)
    │
    └── H (Создание новой страницы, если необходимо)
    │
    └── I (Сохранение PDF-файла)
```

**Примеры**:

```python
data = {'a': 1, 'b': 2, 'c': 3}
file_path = 'data.pdf'
dict2pdf(data, file_path)
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

    xml_output = dict2xml(json_data)
    print(xml_output)
```

**Назначение**: Пример использования функции `json2xml`.
В коде указано, что функция `json2xml` вызывается, но сама она не определена. В примере демонстрируется, как можно преобразовать JSON-данные в XML, используя функцию `dict2xml`.

**Как работает функция**:
1. Определяются JSON-данные в виде словаря.
2. Вызывается функция `dict2xml` с JSON-данными в качестве аргумента.
3. Результат (XML-строка) выводится на экран.

```
A (Определение JSON-данных)
|
└── B (Вызов функции json2xml)
    │
    └── C (Вывод XML-строки на экран)