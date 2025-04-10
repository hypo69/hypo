# Модуль для конвертации XLS файлов в словарь
## Обзор

Модуль предоставляет функцию `xls2dict` для преобразования содержимого XLS файла в словарь Python. Он использует функции из модуля `src.utils.xls` для чтения данных из XLS файла.

## Подробней

Этот модуль упрощает процесс извлечения данных из файлов формата XLS, преобразуя их в удобную структуру данных - словарь. Это может быть полезно для обработки и анализа данных, хранящихся в формате XLS.

## Функции

### `xls2dict`

```python
def xls2dict(xls_file: str | Path) -> dict | None:
    """
    Преобразует содержимое XLS файла в словарь.

    Args:
        xls_file (str | Path): Путь к XLS файлу.

    Returns:
        dict | None: Словарь, содержащий данные из XLS файла, или None в случае ошибки.
    """
```

**Назначение**: Преобразование XLS файла в словарь.

**Параметры**:
- `xls_file` (str | Path): Путь к XLS файлу.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из XLS файла, или `None` в случае ошибки.

**Как работает функция**:

1. Функция принимает путь к XLS файлу (`xls_file`) в качестве аргумента.
2. Вызывает функцию `read_xls_as_dict` из модуля `src.utils.xls`, передавая ей путь к XLS файлу.
3. Возвращает словарь, полученный от функции `read_xls_as_dict`.

**ASCII Flowchart**:

```
XLS_FILE_PATH
    ↓
read_xls_as_dict(xls_file=XLS_FILE_PATH)
    ↓
RETURN_DICT
```

**Примеры**:

```python
from pathlib import Path
# Пример 1: Преобразование XLS файла в словарь
xls_file_path = Path("example.xls")
data_dict = xls2dict(xls_file_path)
if data_dict:
    print(data_dict)
else:
    print("Ошибка при чтении XLS файла")