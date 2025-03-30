# Модуль `xml_json_convertor`

## Обзор

Модуль `xml_json_convertor` предоставляет утилиты для преобразования данных XML в словари и наоборот. Он включает функции для разбора XML-строк и преобразования деревьев элементов XML в представления словарей. Модуль предназначен для работы с данными в формате PrestaShop.

## Подробней

Этот модуль содержит набор функций для преобразования данных между форматами XML и JSON, что полезно при взаимодействии с API PrestaShop. Основные функции включают преобразование JSON в XML и XML в словарь Python. Он включает функции для разбора XML-строк и преобразования деревьев элементов XML в представления словарей.

## Функции

### `dict2xml`

```python
def dict2xml(json_obj: dict, root_name: str = "product") -> str:
    """! Converts a JSON dictionary to an XML string.

    Args:
        json_obj (dict): JSON dictionary to convert.
        root_name (str, optional): Root element name. Defaults to "product".

    Returns:
        str: XML string representation of the JSON.
    """
```

**Описание**: Преобразует словарь JSON в строку XML.

**Параметры**:

-   `json_obj` (dict): Словарь JSON для преобразования.
-   `root_name` (str, optional): Имя корневого элемента. По умолчанию `"product"`.

**Возвращает**:

-   `str`: Строковое представление XML JSON.

**Примеры**:

```python
json_data = {"product": {"name": "Test Product", "price": "10.00"}}
xml_output = dict2xml(json_data)
print(xml_output)
```

### `_parse_node`

```python
def _parse_node(node: ET.Element) -> dict | str:
    """Parse an XML node into a dictionary.

    Args:
        node (ET.Element): The XML element to parse.

    Returns:
        dict | str: A dictionary representation of the XML node, or a string if the node has no attributes or children.
    """
```

**Описание**: Преобразует XML-узел в словарь.

**Параметры**:

-   `node` (ET.Element): XML-элемент для анализа.

**Возвращает**:

-   `dict | str`: Представление XML-узла в виде словаря или строка, если у узла нет атрибутов или дочерних элементов.

**Примеры**:

```python
import xml.etree.ElementTree as ET
xml_string = "<product><name>Test Product</name></product>"
element_tree = ET.fromstring(xml_string)
parsed_node = _parse_node(element_tree)
print(parsed_node)
```

### `_make_dict`

```python
def _make_dict(tag: str, value: any) -> dict:
    """Generate a new dictionary with tag and value.

    Args:
        tag (str): The tag name of the XML element.
        value (any): The value associated with the tag.

    Returns:
        dict: A dictionary with the tag name as the key and the value as the dictionary value.
    """
```

**Описание**: Создает новый словарь с тегом и значением.

**Параметры**:

-   `tag` (str): Имя тега XML-элемента.
-   `value` (any): Значение, связанное с тегом.

**Возвращает**:

-   `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

**Примеры**:

```python
tag = "name"
value = "Test Product"
new_dict = _make_dict(tag, value)
print(new_dict)
```

### `xml2dict`

```python
def xml2dict(xml: str) -> dict:
    """Parse XML string into a dictionary.

    Args:
        xml (str): The XML string to parse.

    Returns:
        dict: The dictionary representation of the XML.
    """
```

**Описание**: Преобразует XML-строку в словарь.

**Параметры**:

-   `xml` (str): XML-строка для анализа.

**Возвращает**:

-   `dict`: Представление XML в виде словаря.

**Примеры**:

```python
xml_string = "<product><name>Test Product</name></product>"
xml_dict = xml2dict(xml_string)
print(xml_dict)
```

### `ET2dict`

```python
def ET2dict(element_tree: ET.Element) -> dict:
    """Convert an XML element tree into a dictionary.

    Args:
        element_tree (ET.Element): The XML element tree.

    Returns:
        dict: The dictionary representation of the XML element tree.
    """
```

**Описание**: Преобразует дерево элементов XML в словарь.

**Параметры**:

-   `element_tree` (ET.Element): Дерево элементов XML.

**Возвращает**:

-   `dict`: Представление дерева элементов XML в виде словаря.

**Примеры**:

```python
import xml.etree.ElementTree as ET
xml_string = "<product><name>Test Product</name></product>"
element_tree = ET.fromstring(xml_string)
xml_dict = ET2dict(element_tree)
print(xml_dict)
```

### `presta_fields_to_xml`

```python
def presta_fields_to_xml(presta_fields_dict: dict) -> str:
    """! Converts a JSON dictionary to an XML string with a fixed root name 'prestashop'.

    Args:
        presta_fields_dict (dict): JSON dictionary containing the data (without 'prestashop' key).

    Returns:
        str: XML string representation of the JSON.
    """
```

**Описание**: Преобразует словарь JSON в строку XML с фиксированным корневым элементом "prestashop".

**Параметры**:

-   `presta_fields_dict` (dict): Словарь JSON, содержащий данные (без ключа "prestashop").

**Возвращает**:

-   `str`: Строковое представление XML JSON.

**Примеры**:

```python
json_data = {"product": {"name": "Test Product", "price": "10.00"}}
xml_output = presta_fields_to_xml(json_data)
print(xml_output)