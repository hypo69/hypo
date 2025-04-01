# Модуль `ns`

## Обзор

Модуль `ns` предназначен для конвертации объектов `SimpleNamespace` в различные форматы данных, такие как `dict`, `JSON`, `CSV`, `XML` и `XLS`. Он предоставляет набор функций для упрощения процесса преобразования и сохранения данных в нужном формате.

## Подробнее

Этот модуль предоставляет функции для преобразования объектов `SimpleNamespace` в различные форматы, что позволяет легко экспортировать и сохранять данные в нужном виде. Он использует другие утилиты, такие как `xml2dict`, `save_csv_file` и `save_xls_file`, для выполнения фактического сохранения в соответствующие форматы.

## Функции

### `ns2dict`

```python
def ns2dict(obj: Any) -> Dict[str, Any]:
    """
    Recursively convert an object with key-value pairs to a dictionary.
    Handles empty keys by substituting them with an empty string.

    Args:
        obj (Any): The object to convert. Can be SimpleNamespace, dict, or any object
                   with a similar structure.

    Returns:
        Dict[str, Any]: Converted dictionary with nested structures handled.
    """
    ...
```

**Описание**: Рекурсивно преобразует объект с парами ключ-значение в словарь. Обрабатывает пустые ключи, заменяя их пустой строкой.

**Как работает функция**:
Функция `ns2dict` принимает объект `obj` в качестве аргумента и рекурсивно преобразует его в словарь. Если значение имеет атрибут `__dict__` (например, `SimpleNamespace` или пользовательские объекты), оно преобразуется в словарь, где ключи и значения обрабатываются рекурсивно. Пустые ключи заменяются пустой строкой. Если значение является словарем, то его элементы также рекурсивно преобразуются. Если значение является списком, то каждый элемент списка также рекурсивно преобразуется.

**Параметры**:
- `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым объектом с аналогичной структурой.

**Возвращает**:
- `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

### `ns2csv`

```python
def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to CSV format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        csv_file_path (str | Path): Path to save the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат CSV.

**Как работает функция**:
Функция `ns2csv` принимает объект `SimpleNamespace` и путь к файлу CSV в качестве аргументов. Она преобразует объект `SimpleNamespace` в словарь с помощью функции `ns2dict`, а затем сохраняет его в формате CSV, используя функцию `save_csv_file`. В случае ошибки логирует исключение и возвращает `False`.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `csv_file_path` (str | Path): Путь для сохранения CSV-файла.

**Возвращает**:
- `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время преобразования или сохранения файла, исключение логируется.

### `ns2xml`

```python
def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Convert SimpleNamespace object to XML format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        root_tag (str): The root element tag for the XML.

    Returns:
        str: The resulting XML string.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат XML.

**Как работает функция**:
Функция `ns2xml` принимает объект `SimpleNamespace` и корневой тег для XML в качестве аргументов. Она преобразует объект `SimpleNamespace` в словарь с помощью функции `ns2dict`, а затем преобразует его в XML, используя функцию `xml2dict`. В случае ошибки логирует исключение и возвращает пустую строку.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:
- `str`: Результирующая XML строка.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка во время преобразования, исключение логируется.

### `ns2xls`

```python
def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Convert SimpleNamespace object to XLS format.

    Args:
        ns_obj (SimpleNamespace): The SimpleNamespace object to convert.
        xls_file_path (str | Path): Path to save the XLS file.

    Returns:
        bool: True if successful, False otherwise.
    """
    ...
```

**Описание**: Преобразует объект `SimpleNamespace` в формат XLS.

**Как работает функция**:
Функция `ns2xls` принимает объект `SimpleNamespace` и путь к файлу XLS в качестве аргументов. Она сохраняет объект `SimpleNamespace` в формате XLS, используя функцию `save_xls_file`.

**Параметры**:
- `data` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `xls_file_path` (str | Path): Путь для сохранения XLS-файла.

**Возвращает**:
- `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в противном случае.