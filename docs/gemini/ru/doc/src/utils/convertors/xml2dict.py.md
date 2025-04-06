# Модуль `xml2dict`

## Обзор

Модуль `xml2dict` предоставляет инструменты для преобразования данных XML в словари Python. Он включает функции для разбора XML-строк и преобразования деревьев XML-элементов в словарные представления.

## Подробнее

Этот модуль полезен, когда требуется представить XML-данные в более удобном для работы формате словаря. Он позволяет легко извлекать данные из XML-структуры, используя ключи словаря.

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

**Параметры**:
- `node` (ET.Element): XML-элемент, который необходимо преобразовать.

**Возвращает**:
- `dict | str`: Словарь, представляющий XML-узел, или строка, если у узла нет атрибутов или дочерних элементов.

**Как работает функция**:

1.  Инициализирует пустой словарь `tree` для хранения структуры узла и пустой словарь `attrs` для хранения атрибутов узла.
2.  Перебирает атрибуты XML-узла:
    *   Если атрибут является `href`, атрибут пропускается.
    *   В противном случае, атрибут преобразуется в словарь с помощью функции `_make_dict` и добавляется в словарь `attrs`.
3.  Извлекает текст (значение) из XML-узла, удаляет начальные и конечные пробелы. Если текста нет, присваивает пустую строку.
4.  Если есть атрибуты, добавляет их в словарь `tree` под ключом `'attrs'`.
5.  Перебирает дочерние элементы XML-узла:
    *   Устанавливает флаг `has_child` в `True`, чтобы указать, что у узла есть дочерние элементы.
    *   Рекурсивно вызывает `_parse_node` для каждого дочернего элемента.
    *   Преобразует дочерний элемент в словарь с помощью `_make_dict`.
    *   Если есть дочерние элементы, значение текущего узла устанавливается в пустую строку.
    *   Если тег дочернего элемента еще не встречался в словаре `tree`, добавляет его.
    *   Если тег дочернего элемента уже есть в словаре `tree`, преобразует существующее значение в список и добавляет новый дочерний элемент в этот список.
6.  Если у узла нет дочерних элементов, добавляет значение узла в словарь `tree` под ключом `'value'`.
7.  Если в словаре `tree` есть только ключ `'value'`, возвращает значение напрямую.
8.  Возвращает словарь `tree`, представляющий XML-узел.

**ASCII Flowchart**:

```
    Начало
    │
    ├──→ Инициализация: tree = {}, attrs = {}
    │
    ├──→ Перебор атрибутов узла
    │   │
    │   └──→ Проверка атрибута href
    │       │
    │       ├──→ Да: Пропустить
    │       │
    │       └──→ Нет: Преобразование атрибута в словарь (_make_dict) и добавление в attrs
    │
    ├──→ Извлечение значения узла
    │
    ├──→ Если есть атрибуты: Добавление attrs в tree
    │
    ├──→ Перебор дочерних элементов узла
    │   │
    │   └──→ Рекурсивный вызов _parse_node для дочернего элемента
    │       │
    │       ├──→ Преобразование дочернего элемента в словарь (_make_dict)
    │       │
    │       ├──→ Если есть дочерние элементы: Значение узла = ''
    │       │
    │       ├──→ Если тег дочернего элемента не в tree: Добавление в tree
    │       │
    │       └──→ Иначе: Преобразование существующего значения в список и добавление нового элемента
    │
    ├──→ Если нет дочерних элементов: Добавление значения узла в tree
    │
    ├──→ Если только 'value' в tree: Вернуть значение
    │
    └──→ Вернуть tree
```

**Примеры**:

```python
import xml.etree.ElementTree as ET

# Пример 1: Узел с атрибутами и значением
node_xml = '<node attr1="value1">text</node>'
node = ET.fromstring(node_xml)
result = _parse_node(node)
print(result)  # {'attrs': {'attr1': {'value': 'value1', 'xmlns': None}}, 'value': 'text'}

# Пример 2: Узел с дочерними элементами
node_xml = '<node><child1>text1</child1><child2>text2</child2></node>'
node = ET.fromstring(node_xml)
result = _parse_node(node)
print(result)
# {'child1': {'value': 'text1'}, 'child2': {'value': 'text2'}}

# Пример 3: Узел без атрибутов и дочерних элементов
node_xml = '<node>text</node>'
node = ET.fromstring(node_xml)
result = _parse_node(node)
print(result)  # text
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
    ...
```

**Назначение**: Создает новый словарь с тегом и значением.

**Параметры**:
- `tag` (str): Имя тега XML-элемента.
- `value` (any): Значение, связанное с тегом.

**Возвращает**:
- `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

**Как работает функция**:

1.  Инициализирует переменную `tag_values` значением параметра `value`.
2.  Использует регулярное выражение для поиска пространства имен в теге XML.
3.  Если пространство имен найдено:
    *   Создает словарь `tag_values` с ключом `'value'` и значением параметра `value`.
    *   Извлекает пространство имен и имя тега из результата регулярного выражения.
4.  Возвращает словарь с именем тега в качестве ключа и `tag_values` в качестве значения.

**ASCII Flowchart**:

```
    Начало
    │
    ├──→ Инициализация: tag_values = value
    │
    ├──→ Поиск пространства имен в теге
    │
    ├──→ Если пространство имен найдено:
    │   │
    │   ├──→ Создание словаря tag_values с ключом 'value'
    │   │
    │   └──→ Извлечение пространства имен и имени тега
    │
    └──→ Вернуть словарь {tag: tag_values}
```

**Примеры**:

```python
# Пример 1: Создание словаря с простым тегом и значением
tag = 'name'
value = 'John'
result = _make_dict(tag, value)
print(result)  # {'name': 'John'}

# Пример 2: Создание словаря с тегом и значением, содержащим пространство имен
tag = '{http://example.com}title'
value = 'Example'
result = _make_dict(tag, value)
print(result)  # {'title': {'value': 'Example', 'xmlns': 'http://example.com'}}
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
    ...
```

**Назначение**: Преобразует XML-строку в словарь.

**Параметры**:
- `xml` (str): XML-строка для преобразования.

**Возвращает**:
- `dict`: Словарь, представляющий XML.

**Как работает функция**:

1.  Преобразует XML-строку в дерево элементов с помощью `ET.fromstring()`.
2.  Вызывает функцию `ET2dict` для преобразования дерева элементов в словарь.
3.  Возвращает полученный словарь.

**ASCII Flowchart**:

```
    Начало
    │
    ├──→ Преобразование XML-строки в дерево элементов (ET.fromstring)
    │
    ├──→ Преобразование дерева элементов в словарь (ET2dict)
    │
    └──→ Вернуть словарь
```

**Примеры**:

```python
# Пример 1: Преобразование простой XML-строки в словарь
xml_string = '<root><name>John</name><age>30</age></root>'
result = xml2dict(xml_string)
print(result)  # {'root': {'name': {'value': 'John'}, 'age': {'value': '30'}}}

# Пример 2: Преобразование XML-строки с атрибутами в словарь
xml_string = '<root attr="value"><name>John</name></root>'
result = xml2dict(xml_string)
print(result)
# {'root': {'attrs': {'attr': {'value': 'value', 'xmlns': None}}, 'name': {'value': 'John'}}}
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
    ...
```

**Назначение**: Преобразует дерево XML-элементов в словарь.

**Параметры**:
- `element_tree` (ET.Element): Дерево XML-элементов.

**Возвращает**:
- `dict`: Словарь, представляющий дерево XML-элементов.

**Как работает функция**:

1.  Вызывает функцию `_make_dict`, передавая тег корневого элемента дерева и результат вызова функции `_parse_node` для корневого элемента.
2.  Возвращает полученный словарь.

**ASCII Flowchart**:

```
    Начало
    │
    ├──→ Вызов _make_dict с тегом корневого элемента и результатом _parse_node
    │
    └──→ Вернуть словарь
```

**Примеры**:

```python
import xml.etree.ElementTree as ET

# Пример 1: Преобразование дерева элементов в словарь
xml_string = '<root><name>John</name></root>'
element_tree = ET.fromstring(xml_string)
result = ET2dict(element_tree)
print(result)  # {'root': {'name': {'value': 'John'}}}

# Пример 2: Преобразование дерева элементов с атрибутами в словарь
xml_string = '<root attr="value"><name>John</name></root>'
element_tree = ET.fromstring(xml_string)
result = ET2dict(element_tree)
print(result)
# {'root': {'attrs': {'attr': {'value': 'value', 'xmlns': None}}, 'name': {'value': 'John'}}}