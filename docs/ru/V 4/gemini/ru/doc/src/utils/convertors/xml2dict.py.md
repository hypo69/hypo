# Модуль `xml2dict.py`

## Обзор

Модуль `xml2dict.py` предоставляет утилиты для преобразования XML данных в словари. Он включает функции для разбора XML строк и преобразования деревьев элементов XML в словарные представления.

## Подробнее

Модуль содержит функции для разбора XML-строк и преобразования их в словари. Это полезно, когда необходимо обрабатывать XML-данные в формате, более удобном для работы в Python. Функции модуля позволяют извлекать данные из XML-файлов и использовать их в различных приложениях и сервисах.

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

**Описание**: Разбирает XML-узел в словарь.

**Параметры**:
- `node` (ET.Element): XML-элемент для разбора.

**Возвращает**:
- `dict | str`: Словарь, представляющий XML-узел, или строка, если узел не имеет атрибутов или дочерних элементов.

**Как работает функция**:
Функция `_parse_node` рекурсивно разбирает XML-узел и его атрибуты, преобразуя их в словарь. Если узел имеет атрибуты, они сохраняются в словаре под ключом `'attrs'`. Если узел имеет дочерние элементы, они также рекурсивно разбираются и добавляются в словарь. Если узел не имеет ни атрибутов, ни дочерних элементов, возвращается строковое значение узла.

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

**Описание**: Создает новый словарь с тегом и значением.

**Параметры**:
- `tag` (str): Имя тега XML-элемента.
- `value` (any): Значение, связанное с тегом.

**Возвращает**:
- `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

**Как работает функция**:
Функция `_make_dict` создает словарь, где ключом является тег XML-элемента, а значением - его значение. Если тег содержит пространство имен, оно также извлекается и добавляется в словарь.

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

**Описание**: Разбирает XML-строку в словарь.

**Параметры**:
- `xml` (str): XML-строка для разбора.

**Возвращает**:
- `dict`: Словарное представление XML.

**Как работает функция**:
Функция `xml2dict` принимает XML-строку в качестве аргумента, преобразует ее в дерево элементов с использованием `ET.fromstring()`, а затем вызывает функцию `ET2dict` для преобразования дерева элементов в словарь.

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

**Описание**: Преобразует дерево элементов XML в словарь.

**Параметры**:
- `element_tree` (ET.Element): Дерево элементов XML.

**Возвращает**:
- `dict`: Словарное представление дерева элементов XML.

**Как работает функция**:
Функция `ET2dict` принимает дерево элементов XML в качестве аргумента и вызывает функцию `_make_dict` для преобразования дерева элементов в словарь.