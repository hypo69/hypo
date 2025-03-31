# Модуль `xml2dict`

## Обзор

Модуль `xml2dict` предоставляет утилиты для преобразования XML-данных в словари. Он включает функции для разбора XML-строк и преобразования деревьев XML-элементов в словарные представления.

## Подробнее

Этот модуль предназначен для упрощения работы с XML-данными, позволяя преобразовывать их в более удобный формат словарей Python. Он использует библиотеки `xml.etree.cElementTree` или `xml.etree.ElementTree` для разбора XML и рекурсивные функции для преобразования структуры XML в словарь.

## Содержание

- [Функции](#Функции)
  - [`_parse_node`](#_parse_node)
  - [`_make_dict`](#_make_dict)
  - [`xml2dict`](#xml2dict)
  - [`ET2dict`](#ET2dict)

## Функции

### `_parse_node`

```python
def _parse_node(node: ET.Element) -> dict | str:
    """Parse an XML node into a dictionary.

    Args:
        node (ET.Element): The XML element to parse.

    Returns:
        dict | str: A dictionary representation of the XML node, or a string if the node has no attributes or children.
    """
    ...
```

**Назначение**: Преобразует XML-узел в словарь.

**Как работает функция**:
Функция рекурсивно обрабатывает XML-узел, извлекая атрибуты и дочерние элементы. Если у узла есть атрибуты, они сохраняются в словаре под ключом `'attrs'`. Если у узла есть дочерние элементы, функция рекурсивно вызывает саму себя для каждого дочернего элемента и сохраняет результаты в словаре. Если у узла нет атрибутов и дочерних элементов, возвращается текстовое значение узла.

**Параметры**:
- `node` (ET.Element): XML-элемент для разбора.

**Возвращает**:
- `dict | str`: Представление XML-узла в виде словаря или строка, если у узла нет атрибутов или дочерних элементов.

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
    ...
```

**Назначение**: Создает новый словарь с тегом и значением.

**Как работает функция**:
Функция создает словарь, где ключом является тег XML-элемента, а значением - значение этого элемента. Если тег содержит пространство имен, он также извлекается и добавляется в словарь.

**Параметры**:
- `tag` (str): Имя тега XML-элемента.
- `value` (any): Значение, связанное с тегом.

**Возвращает**:
- `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

### `xml2dict`

```python
def xml2dict(xml: str) -> dict:
    """Parse XML string into a dictionary.

    Args:
        xml (str): The XML string to parse.

    Returns:
        dict: The dictionary representation of the XML.
    """
    ...
```

**Назначение**: Преобразует XML-строку в словарь.

**Как работает функция**:
Функция принимает XML-строку в качестве входных данных, преобразует её в дерево элементов с помощью `ET.fromstring()`, а затем преобразует это дерево в словарь с помощью функции `ET2dict()`.

**Параметры**:
- `xml` (str): XML-строка для разбора.

**Возвращает**:
- `dict`: Представление XML в виде словаря.

### `ET2dict`

```python
def ET2dict(element_tree: ET.Element) -> dict:
    """Convert an XML element tree into a dictionary.

    Args:
        element_tree (ET.Element): The XML element tree.

    Returns:
        dict: The dictionary representation of the XML element tree.
    """
    ...
```

**Назначение**: Преобразует дерево XML-элементов в словарь.

**Как работает функция**:
Функция принимает дерево XML-элементов в качестве входных данных и преобразует его в словарь с помощью функции `_make_dict()`, которая рекурсивно обрабатывает узлы дерева.

**Параметры**:
- `element_tree` (ET.Element): Дерево XML-элементов.

**Возвращает**:
- `dict`: Представление дерева XML-элементов в виде словаря.