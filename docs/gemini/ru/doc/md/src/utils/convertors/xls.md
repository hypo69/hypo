# Модуль `hypotez/src/utils/convertors/xls.py`

## Обзор

Данный модуль предоставляет функции для работы с файлами в формате XLS, включая чтение данных в виде словаря и сохранение в файл.

## Функции

### `xls2dict`

**Описание**: Функция для чтения файла XLS и возвращения данных в формате словаря.

**Параметры**:

- `xls_file` (str | Path): Путь к файлу XLS для чтения.

**Возвращает**:

- `dict | None`: Словарь, содержащий данные из файла XLS, или `None` в случае ошибки.

**Вызывает исключения**:

- Любые исключения, генерируемые функцией `read_xls_as_dict`.


```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """
    Args:
        xls_file (str | Path): Путь к файлу XLS для чтения.

    Returns:
        dict | None: Словарь, содержащий данные из файла XLS, или None в случае ошибки.

    Raises:
        Exception: Любые исключения, генерируемые функцией read_xls_as_dict.
    """
    return read_xls_as_dict(xls_file=xls_file)
```