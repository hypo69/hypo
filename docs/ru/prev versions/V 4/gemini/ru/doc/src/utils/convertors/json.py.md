# Модуль `json`

## Обзор

Модуль `json` предоставляет функциональность для преобразования данных из формата JSON в различные другие форматы, такие как CSV, SimpleNamespace, XML и XLS. Расположен в `hypotez/src/utils/convertors/json.py` и предназначен для обеспечения совместимости и удобства работы с данными, полученными в формате JSON.

## Подробней

Модуль содержит функции для преобразования JSON данных в различные форматы, такие как:

- CSV (Comma-Separated Values): для представления табличных данных.
- SimpleNamespace: для доступа к данным через атрибуты объектов.
- XML (Extensible Markup Language): для структурированного представления данных.
- XLS (Excel Spreadsheet): для создания файлов электронных таблиц.

Этот модуль используется для интеграции с другими частями проекта, где требуется обработка и преобразование JSON данных в различные форматы.

## Функции

### `json2csv`

```python
def json2csv(json_data: str | list | dict | Path, csv_file_path: str | Path) -> bool:
    """
    Args:
        json_data (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
        csv_file_path (str | Path): Путь к CSV файлу для записи.

    Returns:
        bool: True, если успешно, False в противном случае.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удалось распарсить JSON или записать CSV.

     **Как работает функция**:
    ```
    +---------------------+
    |  Начало             |
    +---------------------+
    |  Принимает json_data и csv_file_path  |
    +---------------------+
    |  Определяет тип json_data             |
    +---------------------+
    |  Загружает JSON данные в зависимости от типа (dict, str, list, Path)  |
    +---------------------+
    |  Вызывает save_csv_file для записи данных в CSV файл      |
    +---------------------+
    |  Возвращает True, если запись успешна, иначе вызывает исключение и возвращает False  |
    +---------------------+
    |  Конец               |
    +---------------------+
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат CSV с разделителем-запятой.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `csv_file_path` (str | Path): Путь к CSV файлу для записи.

**Возвращает**:
- `bool`: `True`, если преобразование и запись прошли успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON или записать CSV файл.

**Примеры**:

```python
json_data = '{"name": "John", "age": 30}'
csv_file_path = 'output.csv'
result = json2csv(json_data, csv_file_path)
print(result)  # Вывод: True

json_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
csv_file_path = 'output.csv'
result = json2csv(json_data, csv_file_path)
print(result)  # Вывод: True
```

### `json2ns`

```python
def json2ns(json_data: str | dict | Path) -> SimpleNamespace:
    """
    Args:
        json_data (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.

    Returns:
        SimpleNamespace: Распарсенные JSON данные в виде объекта SimpleNamespace.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удалось распарсить JSON.

     **Как работает функция**:
    ```
    +---------------------+
    |  Начало             |
    +---------------------+
    |  Принимает json_data  |
    +---------------------+
    |  Определяет тип json_data (str, dict, Path)  |
    +---------------------+
    |  Загружает JSON данные в зависимости от типа  |
    +---------------------+
    |  Создает объект SimpleNamespace из JSON данных  |
    +---------------------+
    |  Возвращает объект SimpleNamespace, иначе вызывает исключение и логирует ошибку  |
    +---------------------+
    |  Конец               |
    +---------------------+
    """
```

**Описание**: Преобразует JSON данные или JSON файл в объект `SimpleNamespace`.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace`, представляющий JSON данные.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON.

**Примеры**:

```python
json_data = '{"name": "John", "age": 30}'
result = json2ns(json_data)
print(result.name)  # Вывод: John

json_data = {"name": "John", "age": 30}
result = json2ns(json_data)
print(result.age)  # Вывод: 30
```

### `json2xml`

```python
def json2xml(json_data: str | dict | Path, root_tag: str = "root") -> str:
    """
    Args:
        json_data (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.
        root_tag (str): Корневой тег для XML.

    Returns:
        str: Результирующая XML строка.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удалось распарсить JSON или преобразовать в XML.

     **Как работает функция**:
    ```
    +---------------------+
    |  Начало             |
    +---------------------+
    |  Принимает json_data и root_tag  |
    +---------------------+
    |  Вызывает dict2xml для преобразования JSON в XML  |
    +---------------------+
    |  Возвращает XML строку, полученную от dict2xml  |
    +---------------------+
    |  Конец               |
    +---------------------+
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат XML.

**Параметры**:
- `json_data` (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.
- `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:
- `str`: XML строка, представляющая JSON данные.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON или преобразовать в XML.

**Примеры**:

```python
json_data = '{"name": "John", "age": 30}'
result = json2xml(json_data)
print(result)
# Вывод:
# <root><name>John</name><age>30</age></root>

json_data = {"name": "John", "age": 30}
result = json2xml(json_data, root_tag="person")
print(result)
# Вывод:
# <person><name>John</name><age>30</age></person>
```

### `json2xls`

```python
def json2xls(json_data: str | list | dict | Path, xls_file_path: str | Path) -> bool:
    """
    Args:
        json_data (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
        xls_file_path (str | Path): Путь к XLS файлу для записи.

    Returns:
        bool: True, если успешно, False в противном случае.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удалось распарсить JSON или записать XLS.

     **Как работает функция**:
    ```
    +---------------------+
    |  Начало             |
    +---------------------+
    |  Принимает json_data и xls_file_path  |
    +---------------------+
    |  Вызывает save_xls_file для записи JSON данных в XLS файл  |
    +---------------------+
    |  Возвращает результат вызова save_xls_file  |
    +---------------------+
    |  Конец               |
    +---------------------+
    """
```

**Описание**: Преобразует JSON данные или JSON файл в формат XLS.

**Параметры**:
- `json_data` (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
- `xls_file_path` (str | Path): Путь к XLS файлу для записи.

**Возвращает**:
- `bool`: `True`, если преобразование и запись прошли успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось распарсить JSON или записать XLS.

**Примеры**:

```python
json_data = '{"name": "John", "age": 30}'
xls_file_path = 'output.xls'
result = json2xls(json_data, xls_file_path)
print(result)  # Вывод: True

json_data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
xls_file_path = 'output.xls'
result = json2xls(json_data, xls_file_path)
print(result)  # Вывод: True