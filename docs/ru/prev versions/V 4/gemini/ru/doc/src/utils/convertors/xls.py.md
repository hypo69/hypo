# Модуль xls

## Обзор

Модуль `xls` предоставляет функциональность для конвертации файлов Excel (xls) в формат словаря Python. Он использует функции из модуля `src.utils.xls` для чтения данных из xls файлов.

## Подробнее

Этот модуль предназначен для извлечения данных из Excel файлов и представления их в виде словаря, что упрощает дальнейшую обработку и анализ данных. Он может быть полезен для интеграции данных из устаревших xls файлов в современные системы, использующие Python.

## Функции

### `xls2dict`

```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """
    Args:
        xls_file (str | Path): Путь к xls файлу.

    Returns:
        dict | None: Словарь, представляющий данные из xls файла, или None в случае ошибки.

    **Как работает функция**:
    Функция `xls2dict` принимает путь к xls файлу, вызывает функцию `read_xls_as_dict` из модуля `src.utils.xls` для чтения данных из файла и возвращает полученный словарь.

    """
```

**Описание**: Конвертирует xls файл в словарь Python.

**Параметры**:
- `xls_file` (str | Path): Путь к xls файлу, который необходимо конвертировать.

**Возвращает**:
- `dict | None`: Словарь, представляющий данные из xls файла, или `None` в случае ошибки.

**Примеры**:
```python
from pathlib import Path
from src.utils.convertors.xls import xls2dict

file_path = Path('example.xls')
data = xls2dict(file_path)
if data:
    print(data)
```
```python
from src.utils.convertors.xls import xls2dict

file_path = 'example.xls'
data = xls2dict(file_path)
if data:
    print(data)
```
```python
from pathlib import Path
from src.utils.convertors.xls import xls2dict

file_path = Path('example_no_exists.xls')
data = xls2dict(file_path)
if data is None:
    print('File not found')
```
```python
from src.utils.convertors.xls import xls2dict

file_path = 'example_no_exists.xls'
data = xls2dict(file_path)
if data is None:
    print('File not found')