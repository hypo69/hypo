# Модуль для конвертации XLS в Dict

## Обзор

Модуль предоставляет функции для конвертации данных из формата XLS (Excel) в формат Dict (словарь Python).
Он использует функции из модуля `src.utils.xls` для чтения и сохранения XLS-файлов.

## Подробней

Модуль `xls2dict` предоставляет удобный интерфейс для преобразования XLS-файлов в словари Python, что облегчает дальнейшую обработку данных.

## Функции

### `xls2dict`

```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """"""
    return read_xls_as_dict(xls_file = xls_file)
```

**Как работает функция**:
Функция `xls2dict` принимает путь к XLS-файлу и использует функцию `read_xls_as_dict` из модуля `src.utils.xls` для чтения данных из XLS-файла и преобразования их в словарь Python. Возвращает полученный словарь.

**Параметры**:
- `xls_file` (str | Path): Путь к XLS-файлу, который нужно преобразовать в словарь.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из XLS-файла, или `None`, если произошла ошибка при чтении файла.

**Примеры**:

```python
from pathlib import Path
from src.utils.convertors.xls import xls2dict

# Пример использования с указанием пути к файлу в виде строки
file_path_str = 'example.xls'
data_dict_str = xls2dict(file_path_str)
if data_dict_str:
    print(f'Словарь из файла {file_path_str}: {data_dict_str}')
else:
    print(f'Не удалось преобразовать файл {file_path_str} в словарь')

# Пример использования с указанием пути к файлу в виде объекта Path
file_path_path = Path('example.xls')
data_dict_path = xls2dict(file_path_path)
if data_dict_path:
    print(f'Словарь из файла {file_path_path}: {data_dict_path}')
else:
    print(f'Не удалось преобразовать файл {file_path_path} в словарь')
```