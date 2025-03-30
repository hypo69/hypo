# Модуль `csv`

## Обзор

Модуль `csv` предоставляет утилиты для конвертации данных между форматами CSV и JSON. Он включает функции для преобразования CSV данных в словари и объекты `SimpleNamespace`, а также для сохранения CSV данных в JSON формат.

## Подробней

Этот модуль предназначен для облегчения обмена данными между CSV и JSON форматами. Он использует функции `read_csv_as_dict`, `read_csv_as_ns`, `save_csv_file` и `read_csv_file` из модуля `src.utils.csv` для чтения и обработки CSV файлов. Модуль также включает функцию `csv_to_json`, которая конвертирует CSV файл в JSON формат и сохраняет его в указанный файл. Это может быть полезно для интеграции данных из различных источников и для работы с данными в различных приложениях.

## Функции

### `csv2dict`

```python
def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.

    Returns:
        dict | None: Словарь, содержащий данные из CSV, преобразованные в формат JSON, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV.
    """
```

**Описание**: Преобразует CSV данные в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу, который необходимо прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_dict`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_dict`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV файла, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV файл.

### `csv2ns`

```python
def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.

    Returns:
        SimpleNamespace | None: Объект SimpleNamespace, содержащий данные из CSV, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV.
    """
```

**Описание**: Преобразует CSV данные в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу, который необходимо прочитать.
- `*args`: Произвольные позиционные аргументы, передаваемые в `read_csv_as_ns`.
- `**kwargs`: Произвольные именованные аргументы, передаваемые в `read_csv_as_ns`.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV файла, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать CSV файл.

### `csv_to_json`

```python
def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """
    Args:
        csv_file_path (str | Path): Путь к CSV файлу для чтения.
        json_file_path (str | Path): Путь к JSON файлу для сохранения.
        exc_info (bool, optional): Если `True`, включает информацию трассировки в лог. По умолчанию `True`.

    Returns:
        List[Dict[str, str]] | None: JSON данные в виде списка словарей, или `None`, если преобразование не удалось.

    Example:
        >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
        >>> print(json_data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
```

**Описание**: Преобразует CSV файл в JSON формат и сохраняет его в JSON файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV файлу, который необходимо прочитать.
- `json_file_path` (str | Path): Путь к JSON файлу, в который нужно сохранить данные.
- `exc_info` (bool, optional): Если `True`, включает информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: JSON данные в виде списка словарей, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Возникает, если не удается прочитать или преобразовать CSV файл.

**Примеры**:

Преобразование CSV файла в JSON:

```python
json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
print(json_data)
# Вывод: [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]