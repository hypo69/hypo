# Модуль для преобразования XML в JSON и обратно

## Обзор

Модуль `xml_json_convertor.py` предоставляет утилиты для преобразования данных из формата XML в словари Python (JSON-подобные) и обратно. Он включает функции для разбора XML-строк и преобразования XML-деревьев элементов в словарные представления.

## Подробней

Этот модуль используется для преобразования данных между форматами, которые используются в PrestaShop API, где XML часто применяется для передачи данных.

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

**Назначение**: Преобразует словарь JSON в строку XML.

**Параметры**:

-   `json_obj` (dict): Словарь JSON для преобразования.
-   `root_name` (str, optional): Имя корневого элемента XML. По умолчанию "product".

**Возвращает**:

-   `str`: XML-строковое представление JSON.

**Как работает функция**:

1.  Определяет внутреннюю функцию `build_xml_element`, которая рекурсивно строит XML-элементы из JSON-данных.
2.  Создает корневой элемент с именем, заданным в `root_name`.
3.  Вызывает `build_xml_element` для заполнения корневого элемента данными из `json_obj`.
4.  Преобразует XML-дерево в строку и возвращает ее.

**Внутренние функции**:

#### `build_xml_element`

```python
def build_xml_element(parent, data):
    """Recursively constructs XML elements from JSON data."""
```

**Назначение**: Рекурсивно строит XML-элементы из JSON-данных.

**Параметры**:

-   `parent`: Родительский XML-элемент.
-   `data`: Данные JSON для преобразования.

**Как работает функция**:

1.  Проверяет тип данных `data`.
2.  Если `data` является словарем, итерируется по его элементам.
    *   Если ключ начинается с "@", устанавливает его как атрибут родительского элемента.
    *   Если ключ равен "#text", устанавливает его как текстовое значение родительского элемента.
    *   Иначе создает дочерний элемент и рекурсивно вызывает себя для этого элемента.
3.  Если `data` является списком, рекурсивно вызывает себя для каждого элемента списка.
4.  Иначе устанавливает `data` как текстовое значение родительского элемента.

**Примеры**:

```python
json_data = {
    "product": {
        "name": "Test Product",
        "price": "10.00"
    }
}
xml_output = dict2xml(json_data)
print(xml_output)
```

ASCII схема работы функции `dict2xml`:

```
JSON-объект
  │
  ▼
Создание XML-элемента root
  │
  ▼
Рекурсивное построение XML-элементов
  │
  ▼
Преобразование XML-дерева в строку
  │
  ▼
Строка XML
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

**Назначение**: Разбирает XML-узел в словарь.

**Параметры**:

-   `node` (ET.Element): XML-элемент для разбора.

**Возвращает**:

-   `dict | str`: Словарь, представляющий XML-узел, или строка, если у узла нет атрибутов или дочерних элементов.

**Как работает функция**:

1.  Инициализирует словарь `tree` для хранения результата.
2.  Инициализирует словарь `attrs` для хранения атрибутов XML-узла.
3.  Итерируется по атрибутам узла и добавляет их в словарь `attrs`, пропуская атрибуты `href`.
4.  Получает текстовое значение узла и удаляет пробелы в начале и конце.
5.  Если есть атрибуты, добавляет их в словарь `tree` под ключом `attrs`.
6.  Итерируется по дочерним элементам узла.
7.  Для каждого дочернего элемента рекурсивно вызывает себя и добавляет результат в словарь `tree`.
8.  Если у узла нет дочерних элементов, добавляет текстовое значение в словарь `tree` под ключом `value`.
9.  Если в словаре `tree` есть только ключ `value`, возвращает значение этого ключа.
10. Возвращает словарь `tree`.

**Примеры**:

```python
import xml.etree.ElementTree as ET

xml_string = "<root><child attribute='value'>text</child></root>"
root = ET.fromstring(xml_string)
result = _parse_node(root[0])
print(result)
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

**Назначение**: Создает новый словарь с тегом и значением.

**Параметры**:

-   `tag` (str): Имя тега XML-элемента.
-   `value` (any): Значение, связанное с тегом.

**Возвращает**:

-   `dict`: Словарь с именем тега в качестве ключа и значением в качестве значения словаря.

**Как работает функция**:

1.  Инициализирует переменную `tag_values` значением `value`.
2.  Ищет в теге регулярное выражение `r"\\{(.*)\\}(.*)"`.
3.  Если находит совпадение, создает словарь `tag_values` со значением `value`, а также добавляет пространство имен и тег.
4.  Возвращает словарь с тегом в качестве ключа и `tag_values` в качестве значения.

**Примеры**:

```python
result = _make_dict("tag", "value")
print(result)
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

**Назначение**: Преобразует XML-строку в словарь.

**Параметры**:

-   `xml` (str): XML-строка для разбора.

**Возвращает**:

-   `dict`: Словарь, представляющий XML.

**Как работает функция**:

1.  Разбирает XML-строку в дерево элементов с помощью `ET.fromstring()`.
2.  Преобразует дерево элементов в словарь с помощью функции `ET2dict()`.
3.  Возвращает полученный словарь.

**Примеры**:

```python
xml_string = "<root><child>text</child></root>"
result = xml2dict(xml_string)
print(result)
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

**Назначение**: Преобразует дерево XML-элементов в словарь.

**Параметры**:

-   `element_tree` (ET.Element): Дерево XML-элементов.

**Возвращает**:

-   `dict`: Словарь, представляющий дерево XML-элементов.

**Как работает функция**:

1.  Вызывает функцию `_make_dict()` с тегом корневого элемента и результатом функции `_parse_node()`.
2.  Возвращает полученный словарь.

**Примеры**:

```python
import xml.etree.ElementTree as ET

xml_string = "<root><child>text</child></root>"
element_tree = ET.fromstring(xml_string)
result = ET2dict(element_tree)
print(result)
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

**Назначение**: Преобразует словарь JSON в XML-строку с фиксированным корневым элементом "prestashop".

**Параметры**:

-   `presta_fields_dict` (dict): JSON-словарь, содержащий данные (без ключа "prestashop").

**Возвращает**:

-   `str`: XML-строковое представление JSON.

**Как работает функция**:

1.  Определяет внутреннюю функцию `build_xml_element`, которая рекурсивно строит XML-элементы из JSON-данных.
2.  Проверяет, не пуст ли входной словарь `presta_fields_dict`. Если пуст, возвращает пустую строку.
3.  Получает первый ключ из словаря `presta_fields_dict` (например, 'product', 'category' и т. д.).
4.  Создает корневой элемент "prestashop".
5.  Создает динамический дочерний элемент корневого элемента с ключом, полученным на шаге 3.
6.  Вызывает функцию `build_xml_element` для заполнения динамического элемента данными из словаря `presta_fields_dict`.
7.  Преобразует XML-дерево в строку и возвращает ее.

**Внутренние функции**:

#### `build_xml_element`

```python
def build_xml_element(parent, data):
    """Recursively constructs XML elements from JSON data."""
```

**Назначение**: Рекурсивно строит XML-элементы из JSON-данных.

**Параметры**:

-   `parent`: Родительский XML-элемент.
-   `data`: Данные JSON для преобразования.

**Как работает функция**:

1.  Проверяет тип данных `data`.
2.  Если `data` является словарем, итерируется по его элементам.
    *   Если ключ начинается с "@", устанавливает его как атрибут родительского элемента.
    *   Если ключ равен "#text", устанавливает его как текстовое значение родительского элемента.
    *   Иначе создает дочерний элемент и рекурсивно вызывает себя для этого элемента.
3.  Если `data` является списком, рекурсивно вызывает себя для каждого элемента списка.
4.  Иначе устанавливает `data` как текстовое значение родительского элемента.

**Примеры**:

```python
json_data = {
    "product": {
        "name": {
            "language": [
                {
                    "@id": "1",
                    "#text": "Test Product"
                }
            ]
        },
        "price": "10.00"
    }
}
xml_output = presta_fields_to_xml(json_data)
print(xml_output)
```

ASCII схема работы функции `presta_fields_to_xml`:

```
JSON-объект (presta_fields_dict)
  │
  ▼
Создание XML-элемента "prestashop"
  │
  ▼
Создание динамического дочернего элемента
  │
  ▼
Рекурсивное построение XML-элементов
  │
  ▼
Преобразование XML-дерева в строку
  │
  ▼
Строка XML