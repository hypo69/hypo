# Модуль для конвертации между `dict` и `SimpleNamespace` объектами

## Обзор

Модуль `src.utils.convertors.dict` предоставляет инструменты для преобразования данных между форматами `dict` и `SimpleNamespace`, а также для экспорта данных в различные форматы, такие как XML, CSV, JSON, XLS, HTML и PDF.

## Подробней

Этот модуль содержит функции для рекурсивного преобразования словарей в объекты `SimpleNamespace` и обратно. Кроме того, он предоставляет возможность экспортировать данные в различные форматы, что может быть полезно для интеграции с различными системами и приложениями.
Модуль включает в себя функции для работы с XML, CSV, JSON, XLS, HTML и PDF форматами. Он обеспечивает гибкость и удобство при работе с данными, позволяя легко преобразовывать их между различными форматами.

## Содержание

- [Функции](#Функции)
    - [replace_key_in_dict](#replace_key_in_dict)
    - [dict2ns](#dict2ns)
    - [dict2xml](#dict2xml)
    - [dict2csv](#dict2csv)
    - [dict2xls](#dict2xls)
    - [dict2html](#dict2html)
    - [example_json2xml](#example_json2xml)

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

**Как работает функция**: Функция проверяет, является ли входной параметр `data` словарем или списком. Если это словарь, она перебирает все ключи и заменяет `old_key` на `new_key`. Если значением ключа является словарь или список, функция рекурсивно вызывает саму себя для этого значения. Если `data` является списком, функция перебирает все элементы и рекурсивно вызывает саму себя для каждого элемента.

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
    Рекурсивно преобразует словари в SimpleNamespace.

    Args:
        data (Dict[str, Any] | List[Any]): Данные для преобразования.

    Returns:
        Any: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.
    """
```

**Назначение**: Рекурсивно преобразует словари в объекты `SimpleNamespace`.

**Как работает функция**: Функция проверяет, является ли входной параметр `data` словарем или списком. Если это словарь, она перебирает все элементы словаря и рекурсивно вызывает саму себя для каждого значения, которое является словарем. Если значением является список, то функция преобразует каждый элемент списка в `SimpleNamespace`, если это возможно. Если `data` является списком, функция применяет те же преобразования к каждому элементу списка.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.

### `dict2xml`

```python
def dict2xml(data: Dict[str, Any], encoding: str = 'UTF-8') -> str:
    """
    Генерирует XML строку из словаря.

    Args:
        data (Dict[str, Any]): Данные для преобразования в XML.
        encoding (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

    Returns:
        str: XML строка, представляющая входной словарь.

    Raises:
        Exception: Если предоставлено более одного корневого узла.
    """
```

**Назначение**: Генерирует XML строку из словаря.

**Как работает функция**: Функция использует рекурсивный подход для преобразования словаря в XML. Она определяет вспомогательные функции для обработки простых типов данных (int, str), атрибутов и сложных типов данных (списки, словари). Основная функция `_process` определяет тип значения и вызывает соответствующую функцию для его обработки. Если значение является словарем, создается XML элемент с атрибутами и дочерними элементами. Если значение является списком, создается набор XML элементов.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: XML строка, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

### `dict2csv`

```python
def dict2csv(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные словаря или SimpleNamespace в CSV файл.

    Args:
        data (dict | SimpleNamespace): Данные для сохранения в CSV файл.
        file_path (str | Path): Путь к CSV файлу.

    Returns:
        bool: True, если файл был успешно сохранен, False в противном случае.
    """
```

**Назначение**: Сохраняет данные словаря или `SimpleNamespace` в CSV файл.

**Как работает функция**: Функция вызывает функцию `save_csv_file` из модуля `<укажите модуль>` для сохранения данных в CSV файл. Функция просто передает входные параметры в `save_csv_file`.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в CSV файл.
- `file_path` (str | Path): Путь к CSV файлу.

**Возвращает**:
- `bool`: `True`, если файл был успешно сохранен, `False` в противном случае.

### `dict2xls`

```python
def dict2xls(data: dict | SimpleNamespace, file_path: str | Path) -> bool:
    """
    Сохраняет данные словаря или SimpleNamespace в XLS файл.

    Args:
        data (dict | SimpleNamespace): Данные для сохранения в XLS файл.
        file_path (str | Path): Путь к XLS файлу.

    Returns:
        bool: True, если файл был успешно сохранен, False в противном случае.
    """
```

**Назначение**: Сохраняет данные словаря или `SimpleNamespace` в XLS файл.

**Как работает функция**: Функция вызывает функцию `save_xls_file` из модуля `src.utils.xls` для сохранения данных в XLS файл. Функция просто передает входные параметры в `save_xls_file`.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в XLS файл.
- `file_path` (str | Path): Путь к XLS файлу.

**Возвращает**:
- `bool`: `True`, если файл был успешно сохранен, `False` в противном случае.

### `dict2html`

```python
def dict2html(data: dict | SimpleNamespace, encoding: str = 'UTF-8') -> str:
    """
    Генерирует HTML таблицу из словаря или объекта SimpleNamespace.

    Args:
        data (dict | SimpleNamespace): Данные для преобразования в HTML.
        encoding (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

    Returns:
        str: HTML строка, представляющая входной словарь.
    """
```

**Назначение**: Генерирует HTML таблицу из словаря или объекта `SimpleNamespace`.

**Как работает функция**: Функция преобразует входные данные в HTML таблицу. Если входные данные являются объектом `SimpleNamespace`, они преобразуются в словарь. Затем функция использует рекурсивную функцию `dict_to_html_table` для преобразования словаря в HTML таблицу. Функция `dict_to_html_table` рекурсивно перебирает элементы словаря и создает HTML таблицу с ключами и значениями. Если значение является словарем, функция вызывает саму себя для этого значения. Если значение является списком, создается HTML список.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:
- `str`: HTML строка, представляющая входной словарь.

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

**Назначение**: Пример использования функции `json2xml`.

**Как работает функция**: Функция создает пример JSON данных и преобразует их в XML с использованием функции `json2xml`. Результат выводится в консоль.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.