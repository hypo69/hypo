# Модуль `ns`

## Обзор

Модуль `ns` предназначен для конвертации объектов `SimpleNamespace` в различные форматы, такие как `dict`, `JSON`, `CSV`, `XML` и `XLS`. Это упрощает интеграцию данных из `SimpleNamespace` в различные системы и форматы файлов.

## Подробнее

Этот модуль предоставляет набор функций для преобразования объектов `SimpleNamespace` в различные форматы данных. `SimpleNamespace` – это простой класс, который позволяет получать доступ к своим атрибутам как к полям объекта. Модуль включает функции для преобразования в словарь, JSON, CSV, XML и XLS, что делает его удобным для работы с разными типами данных и интеграции с различными системами. Модуль использует другие утилиты, такие как `xml2dict`, `save_csv_file` и `save_xls_file`, для выполнения фактических преобразований и сохранения данных.

## Функции

### `ns2dict`

```python
def ns2dict(obj: Any) -> Dict[str, Any]:
    """
    Рекурсивно преобразует объект с парами ключ-значение в словарь.
    Обрабатывает пустые ключи, заменяя их пустой строкой.

    Args:
        obj (Any): Объект для преобразования. Может быть SimpleNamespace, dict или любым объектом
                   с аналогичной структурой.

    Returns:
        Dict[str, Any]: Преобразованный словарь с обработанными вложенными структурами.
    """
    def convert(value: Any) -> Any:
        """
        Рекурсивно обрабатывает значения для обработки вложенных структур и пустых ключей.

        Args:
            value (Any): Значение для обработки.

        Returns:
            Any: Преобразованное значение.
        """
        # Если значение имеет атрибут `__dict__` (например, SimpleNamespace или пользовательские объекты)
        if hasattr(value, '__dict__'):
            return {key or "": convert(val) for key, val in vars(value).items()}
        # Если значение является объектом, подобным словарю (имеет .items())
        elif hasattr(value, 'items'):
            return {key or "": convert(val) for key, val in value.items()}
        # Если значение является списком или другим итерируемым объектом
        elif isinstance(value, list):
            return [convert(item) for item in value]
        return value

    return convert(obj)
```

**Как работает функция**:

Функция `ns2dict` преобразует объект `SimpleNamespace` в словарь. Она рекурсивно проходит по атрибутам объекта, обрабатывая вложенные структуры данных. Внутренняя функция `convert` проверяет тип каждого значения и рекурсивно преобразует его, если это `SimpleNamespace`, словарь или список. Пустые ключи заменяются пустой строкой.

**Параметры**:

-   `obj` (Any): Объект для преобразования. Может быть `SimpleNamespace`, `dict` или любым объектом с аналогичной структурой.

**Возвращает**:

-   `Dict[str, Any]`: Преобразованный словарь с обработанными вложенными структурами.

**Примеры**:

```python
from types import SimpleNamespace
obj = SimpleNamespace(name='John', age=30, address=SimpleNamespace(city='New York', zip='10001'))
result = ns2dict(obj)
print(result)  # {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}
```

### `ns2csv`

```python
def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Преобразует объект SimpleNamespace в формат CSV.

    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для преобразования.
        csv_file_path (str | Path): Путь для сохранения CSV-файла.

    Returns:
        bool: True, если успешно, False в противном случае.
    """
    try:
        data = [ns2dict(ns_obj)]
        save_csv_file(data, csv_file_path)
        return True
    except Exception as ex:
        logger.error(f"ns2csv failed", ex, True)
```

**Как работает функция**:

Функция `ns2csv` преобразует объект `SimpleNamespace` в формат CSV. Сначала она преобразует `SimpleNamespace` в словарь с помощью функции `ns2dict`, а затем использует функцию `save_csv_file` для сохранения данных в CSV-файл по указанному пути. В случае ошибки, информация об ошибке логируется.

**Параметры**:

-   `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
-   `csv_file_path` (str | Path): Путь для сохранения CSV-файла.

**Возвращает**:

-   `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в противном случае.

**Вызывает исключения**:

-   `Exception`: Возникает, если происходит ошибка при преобразовании в CSV или сохранении файла.

**Примеры**:

```python
from types import SimpleNamespace
import tempfile
from pathlib import Path
import os

# Создаем временный файл для теста
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
temp_path = Path(temp_file.name)
temp_file.close()

ns_obj = SimpleNamespace(name='John', age=30)
result = ns2csv(ns_obj, temp_path)
print(result)

# Удаляем временный файл
os.unlink(temp_path)
```

### `ns2xml`

```python
def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Преобразует объект SimpleNamespace в формат XML.

    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для преобразования.
        root_tag (str): Корневой тег для XML.

    Returns:
        str: Результирующая XML строка.
    """
    try:
        data = ns2dict(ns_obj)
        return xml2dict(data)
    except Exception as ex:
        logger.error(f"ns2xml failed", ex, True)
```

**Как работает функция**:

Функция `ns2xml` преобразует объект `SimpleNamespace` в XML формат. Она использует функцию `ns2dict` для преобразования `SimpleNamespace` в словарь, а затем вызывает функцию `xml2dict` для преобразования словаря в XML строку. В случае ошибки, информация об ошибке логируется.

**Параметры**:

-   `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
-   `root_tag` (str): Корневой тег для XML. По умолчанию "root".

**Возвращает**:

-   `str`: Результирующая XML строка.

**Вызывает исключения**:

-   `Exception`: Возникает, если происходит ошибка при преобразовании в XML.

**Примеры**:

```python
from types import SimpleNamespace

ns_obj = SimpleNamespace(name='John', age=30)
xml_string = ns2xml(ns_obj)
print(xml_string)
```

### `ns2xls`

```python
def ns2xls(data: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Преобразует объект SimpleNamespace в формат XLS.

    Args:
        ns_obj (SimpleNamespace): Объект SimpleNamespace для преобразования.
        xls_file_path (str | Path): Путь для сохранения XLS файла.

    Returns:
        bool: True, если успешно, False в противном случае.
    """
    return save_xls_file(data,xls_file_path)
```

**Как работает функция**:

Функция `ns2xls` преобразует объект `SimpleNamespace` в формат XLS. Она вызывает функцию `save_xls_file` для сохранения данных в XLS файл по указанному пути.

**Параметры**:

-   `data` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
-   `xls_file_path` (str | Path): Путь для сохранения XLS файла.

**Возвращает**:

-   `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в противном случае.

**Примеры**:

```python
from types import SimpleNamespace
import tempfile
from pathlib import Path
import os

# Создаем временный файл для теста
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xls')
temp_path = Path(temp_file.name)
temp_file.close()

data = SimpleNamespace(name='John', age=30)
result = ns2xls(data, temp_path)
print(result)

# Удаляем временный файл
os.unlink(temp_path)