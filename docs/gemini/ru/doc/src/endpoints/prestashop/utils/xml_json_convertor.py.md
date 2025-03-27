# Модуль: xml_json_convertor

## Обзор

Модуль `xml_json_convertor` предоставляет утилиты для преобразования данных XML в словари и наоборот. Он включает функции для разбора XML-строк и преобразования деревьев элементов XML в представления словарей.

## Подробней

Этот модуль предназначен для работы с данными в формате XML, часто используемом в PrestaShop. Он позволяет преобразовывать XML в JSON (словарь Python) для удобства обработки и обратно, чтобы формировать XML-запросы. Функции модуля обеспечивают гибкость при работе с различными структурами XML, включая атрибуты и пространства имен.

## Функции

### `dict2xml`

```python
def dict2xml(json_obj: dict, root_name: str = "product") -> str:
    """
    Args:
        json_obj (dict): JSON dictionary to convert.
        root_name (str, optional): Root element name. Defaults to "product".

    Returns:
        str: XML string representation of the JSON.
    """
```

**Описание**: Преобразует JSON-словарь в XML-строку.

**Параметры**:
- `json_obj` (dict): JSON-словарь, который нужно преобразовать.
- `root_name` (str, optional): Имя корневого элемента. По умолчанию "product".

**Возвращает**:
- `str`: XML-строковое представление JSON.

**Примеры**:
```python
json_data = {"product": {"name": "Test Product", "price": "10.00"}}
xml_output = dict2xml(json_data)
print(xml_output)
```

### `_parse_node`

```python
def _parse_node(node: ET.Element) -> dict | str:
    """
    Args:
        node (ET.Element): The XML element to parse.

    Returns:
        dict | str: A dictionary representation of the XML node, or a string if the node has no attributes or children.
    """
```

**Описание**: Преобразует XML-узел в словарь.

**Параметры**:
- `node` (ET.Element): XML-элемент для разбора.

**Возвращает**:
- `dict | str`: Представление XML-узла в виде словаря или строка, если у узла нет атрибутов или потомков.

**Примеры**:
```python
import xml.etree.ElementTree as ET
xml_string = '<product name="Test Product">10.00</product>'
root = ET.fromstring(xml_string)
node_dict = _parse_node(root)
print(node_dict)
```

### `_make_dict`

```python
def _make_dict(tag: str, value: any) -> dict:
    """
    Args:
        tag (str): The tag name of the XML element.
        value (any): The value associated with the tag.

    Returns:
        dict: A dictionary with the tag name as the key and the value as the dictionary value.
    """
```

**Описание**: Создает новый словарь с тегом и значением.

**Параметры**:
- `tag` (str): Имя тега XML-элемента.
- `value` (any): Значение, связанное с тегом.

**Возвращает**:
- `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

**Примеры**:
```python
tag = 'product'
value = {'name': 'Test Product', 'price': '10.00'}
result_dict = _make_dict(tag, value)
print(result_dict)
```

### `xml2dict`

```python
def xml2dict(xml: str) -> dict:
    """
    Args:
        xml (str): The XML string to parse.

    Returns:
        dict: The dictionary representation of the XML.
    """
```

**Описание**: Преобразует XML-строку в словарь.

**Параметры**:
- `xml` (str): XML-строка для разбора.

**Возвращает**:
- `dict`: Представление XML в виде словаря.

**Примеры**:
```python
xml_string = '<product name="Test Product">10.00</product>'
xml_dict = xml2dict(xml_string)
print(xml_dict)
```

### `ET2dict`

```python
def ET2dict(element_tree: ET.Element) -> dict:
    """
    Args:
        element_tree (ET.Element): The XML element tree.

    Returns:
        dict: The dictionary representation of the XML element tree.
    """
```

**Описание**: Преобразует дерево XML-элементов в словарь.

**Параметры**:
- `element_tree` (ET.Element): Дерево XML-элементов.

**Возвращает**:
- `dict`: Представление дерева XML-элементов в виде словаря.

**Примеры**:
```python
import xml.etree.ElementTree as ET
xml_string = '<product name="Test Product">10.00</product>'
root = ET.fromstring(xml_string)
tree_dict = ET2dict(root)
print(tree_dict)
```

### `presta_fields_to_xml`

```python
def presta_fields_to_xml(presta_fields_dict: dict) -> str:
    """
    Args:
        presta_fields_dict (dict): JSON dictionary containing the data (without 'prestashop' key).

    Returns:
        str: XML string representation of the JSON.
    """
```

**Описание**: Преобразует JSON-словарь в XML-строку с фиксированным корневым элементом 'prestashop'.

**Параметры**:
- `presta_fields_dict` (dict): JSON-словарь, содержащий данные (без ключа 'prestashop').

**Возвращает**:
- `str`: XML-строковое представление JSON.

**Примеры**:
```python
json_data = {"product": {"name": "Test Product", "price": "10.00"}}
xml_output = presta_fields_to_xml(json_data)
print(xml_output)
```