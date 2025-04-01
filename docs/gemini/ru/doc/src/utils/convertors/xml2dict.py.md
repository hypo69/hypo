# Модуль `xml2dict`

## Обзор

Модуль `xml2dict` предоставляет утилиты для конвертации XML данных в словари. Он включает функции для парсинга XML строк и преобразования деревьев XML элементов в словарные представления.

## Подробнее

Этот модуль предназначен для упрощения работы с XML данными, позволяя представлять их в виде словарей Python, что облегчает доступ к данным и их обработку. Модуль использует библиотеки `xml.etree.cElementTree` или `xml.etree.ElementTree` для парсинга XML.

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
- `node` (ET.Element): XML-элемент для парсинга.

**Возвращает**:
- `dict | str`: Словарь, представляющий XML-узел, или строка, если у узла нет атрибутов или потомков.

**Как работает функция**:
1. Инициализируется пустой словарь `tree` для хранения структуры узла.
2. Инициализируется пустой словарь `attrs` для хранения атрибутов узла.
3. Проход по атрибутам узла. Если атрибут является `href`, он пропускается.
4. Обновление словаря `attrs` атрибутами текущего узла с помощью функции `_make_dict`.
5. Получение значения текста узла, если он существует, и удаление лишних пробелов.
6. Если есть атрибуты, они добавляются в словарь `tree` под ключом `'attrs'`.
7. Проход по дочерним элементам узла.
8. Рекурсивный вызов `_parse_node` для каждого дочернего элемента.
9. Создание словаря `cdict` с помощью функции `_make_dict` для каждого дочернего элемента.
10. Если дочерние элементы существуют, значение текущего узла становится пустой строкой.
11. Если тег дочернего элемента не найден в словаре `tree`, он добавляется в `tree`.
12. Если тег уже существует, текущее значение преобразуется в список, и новый элемент добавляется в этот список.
13. Если у узла нет дочерних элементов, его значение сохраняется в `tree['value']`.
14. Если в словаре `tree` есть только ключ `'value'`, возвращается только значение.

**ASCII flowchart**:

```
Начало
  ↓
Создание tree = {} и attrs = {}
  ↓
Проход по атрибутам node
  │
  └─> Если attr_tag == '{http://www.w3.org/1999/xlink}href': Пропустить
  │
  └─> Обновление attrs с помощью _make_dict
  ↓
Получение и очистка node.text -> value
  ↓
Если attrs: Добавить attrs в tree
  ↓
Проход по дочерним элементам child
  │
  └─> ctree = _parse_node(child)
  │
  └─> cdict = _make_dict(ctag, ctree)
  │
  └─> Если ctree: value = ''
  │
  └─> Если ctag не в tree: Добавить cdict в tree
  │
  └─> Иначе: Преобразовать tree[ctag] в список и добавить ctree
  ↓
Если нет дочерних элементов: tree['value'] = value
  ↓
Если list(tree.keys()) == ['value']: tree = tree['value']
  ↓
Конец: вернуть tree
```

**Примеры**:

```python
# Пример 1: Простой узел с атрибутами и значением
node = ET.XML('<root attr1="value1">text</root>')
result = _parse_node(node)
print(result)
# {'attrs': {'attr1': {'value': 'value1'}}, 'value': 'text'}

# Пример 2: Узел с дочерними элементами
node = ET.XML('<root><child1>text1</child1><child2>text2</child2></root>')
result = _parse_node(node)
print(result)
# {'child1': {'value': 'text1'}, 'child2': {'value': 'text2'}}

# Пример 3: Узел только со значением
node = ET.XML('<root>text</root>')
result = _parse_node(node)
print(result)
# 'text'
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
1. Присваивание значения тега переменной `tag_values`.
2. Проверка наличия пространства имен в теге с использованием регулярного выражения.
3. Если пространство имен найдено, создается словарь `tag_values` со значением и пространством имен.
4. Возвращается словарь с тегом в качестве ключа и `tag_values` в качестве значения.

**ASCII flowchart**:

```
Начало
  ↓
tag_values = value
  ↓
Проверка на наличие пространства имен в tag
  │
  └─> Если пространство имен найдено:
  │    └─> Создание tag_values = {'value': value}
  │    └─> Извлечение xmlns и tag из результата поиска
  ↓
Конец: вернуть {tag: tag_values}
```

**Примеры**:

```python
# Пример 1: Создание словаря с простым тегом и значением
result = _make_dict('tag', 'value')
print(result)
# {'tag': 'value'}

# Пример 2: Создание словаря с тегом и словарем значений
result = _make_dict('tag', {'key': 'value'})
print(result)
# {'tag': {'key': 'value'}}

# Пример 3: Создание словаря с тегом, содержащим пространство имен
result = _make_dict('{http://example.com}tag', 'value')
print(result)
# {'tag': {'value': 'value', 'xmlns': 'http://example.com'}}
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
- `xml` (str): XML-строка для парсинга.

**Возвращает**:
- `dict`: Словарь, представляющий XML.

**Как работает функция**:
1. Преобразует XML-строку в дерево элементов с помощью `ET.fromstring`.
2. Преобразует дерево элементов в словарь с помощью функции `ET2dict`.
3. Возвращает полученный словарь.

**ASCII flowchart**:

```
Начало
  ↓
element_tree = ET.fromstring(xml)
  ↓
Конец: вернуть ET2dict(element_tree)
```

**Примеры**:

```python
# Пример 1: Преобразование простой XML-строки в словарь
xml_string = '<root><child>text</child></root>'
result = xml2dict(xml_string)
print(result)
# {'root': {'child': {'value': 'text'}}}

# Пример 2: Преобразование XML-строки с атрибутами в словарь
xml_string = '<root attr="value"><child>text</child></root>'
result = xml2dict(xml_string)
print(result)
# {'root': {'child': {'value': 'text'}, 'attrs': {'attr': {'value': 'value'}}}}
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
1. Вызывает функцию `_make_dict`, передавая ей корневой тег дерева элементов и результат вызова `_parse_node` для всего дерева.
2. Возвращает полученный словарь.

**ASCII flowchart**:

```
Начало
  ↓
Конец: вернуть _make_dict(element_tree.tag, _parse_node(element_tree))
```

**Примеры**:

```python
# Пример 1: Преобразование простого дерева элементов в словарь
element = ET.XML('<root><child>text</child></root>')
result = ET2dict(element)
print(result)
# {'root': {'child': {'value': 'text'}}}

# Пример 2: Преобразование дерева элементов с атрибутами в словарь
element = ET.XML('<root attr="value"><child>text</child></root>')
result = ET2dict(element)
print(result)
# {'root': {'child': {'value': 'text'}, 'attrs': {'attr': {'value': 'value'}}}}