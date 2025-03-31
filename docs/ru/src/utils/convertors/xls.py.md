# Модуль для конвертации XLS в Dict

## Обзор

Модуль предоставляет функцию для конвертации файлов XLS в формат dict.

## Подробней

Модуль `xls2dict` предназначен для преобразования данных из файлов формата XLS в словари Python. Он использует функции из модуля `src.utils.xls` для чтения данных из XLS файлов и возвращает их в виде словаря. Этот модуль полезен, когда необходимо обрабатывать данные из старых форматов файлов XLS и преобразовывать их в более удобный для обработки формат.

## Функции

### `xls2dict`

```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """"""
    return read_xls_as_dict(xls_file = xls_file)
```

**Как работает функция**:
Функция `xls2dict` принимает путь к файлу XLS, вызывает функцию `read_xls_as_dict` из модуля `src.utils.xls` для чтения данных из файла и возвращает полученный словарь.

**Параметры**:
- `xls_file` (str | Path): Путь к XLS файлу, который необходимо преобразовать в словарь.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из XLS файла. Возвращает `None` в случае ошибки.

**Примеры**:

```python
from pathlib import Path
from src.utils.convertors.xls import xls2dict

# Пример использования с указанием пути к файлу строкой
file_path_str = 'example.xls'
data_dict_str = xls2dict(file_path_str)
if data_dict_str:
    print(f'Данные из файла {file_path_str}: {data_dict_str}')
else:
    print(f'Не удалось прочитать файл {file_path_str}')

# Пример использования с указанием пути к файлу через объект Path
file_path_path = Path('example.xls')
data_dict_path = xls2dict(file_path_path)
if data_dict_path:
    print(f'Данные из файла {file_path_path}: {data_dict_path}')
else:
    print(f'Не удалось прочитать файл {file_path_path}')