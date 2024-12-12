# Модуль `hypotez/src/utils/convertors/csv.py`

## Обзор

Модуль `hypotez/src/utils/convertors/csv.py` предоставляет функции для конвертации данных в формате CSV в различные структуры данных, включая словари и объекты `SimpleNamespace`.  Также модуль включает функцию для преобразования CSV в JSON и сохранения его в файл.

## Функции

### `csv2dict`

**Описание**: Преобразует данные из файла CSV в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к файлу CSV для чтения.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV, преобразованные в формат JSON, или `None`, если преобразование завершилось неудачно.

**Возможные исключения**:
- `Exception`: Если чтение CSV файла невозможно.


### `csv2ns`

**Описание**: Преобразует данные из файла CSV в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к файлу CSV для чтения.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV, или `None`, если преобразование завершилось неудачно.

**Возможные исключения**:
- `Exception`: Если чтение CSV файла невозможно.


### `csv_to_json`

**Описание**: Преобразует файл CSV в формат JSON и сохраняет его в файл JSON.

**Параметры**:
- `csv_file_path` (str | Path): Путь к файлу CSV для чтения.
- `json_file_path` (str | Path): Путь к файлу JSON для сохранения.
- `exc_info` (bool, optional): Если `True`, включает информацию о трассировке стека в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Данные JSON в виде списка словарей, или `None`, если преобразование завершилось неудачно.

**Пример использования**:
```python
>>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
>>> print(json_data)
[{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```

**Возможные исключения**:
- `Exception`: Если возникает ошибка при чтении CSV или записи JSON.  Ошибка будет записана в лог.


##  Используемые модули


- `json`
- `csv`
- `pathlib`
- `typing`
- `types`
- `src.logger.logger`
- `src.utils.csv`