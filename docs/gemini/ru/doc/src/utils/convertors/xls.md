# Модуль `hypotez/src/utils/convertors/xls.py`

## Обзор

Модуль `xls.py` содержит функции для работы с файлами Excel (формат XLS). Он предоставляет средства для чтения данных из файла Excel в виде словаря и записи данных в файл Excel.

## Функции

### `xls2dict`

**Описание**: Функция `xls2dict` считывает данные из файла Excel и возвращает их в формате словаря.

**Параметры**:
- `xls_file` (str | Path): Путь к файлу Excel.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из файла Excel, или `None`, если произошла ошибка.

**Вызывает исключения**:
- Возможны исключения, связанные с ошибками чтения файла Excel.
```
```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """
    Args:
        xls_file (str | Path): Путь к файлу Excel.

    Returns:
        dict | None: Словарь, содержащий данные из файла Excel, или None, если произошла ошибка.

    Raises:
        FileNotFoundError: Файл не найден.
        Exception: Другие ошибки при чтении файла Excel.
    """
    return read_xls_as_dict(xls_file=xls_file)
```