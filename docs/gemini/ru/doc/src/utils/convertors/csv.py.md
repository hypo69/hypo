# Модуль `src.utils.convertors.csv`

## Обзор

Модуль `src.utils.convertors.csv` предоставляет утилиты для конвертации данных между форматами CSV и JSON. Он включает функции для чтения CSV файлов, преобразования их в словари или объекты `SimpleNamespace`, а также для сохранения данных в JSON формате.

## Оглавление
1. [Функции](#Функции)
    - [`csv2dict`](#csv2dict)
    - [`csv2ns`](#csv2ns)
    - [`csv_to_json`](#csv_to_json)

## Функции

### `csv2dict`

**Описание**: Конвертирует данные из CSV файла в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу для чтения.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV, преобразованные в формат JSON, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV.

### `csv2ns`

**Описание**: Конвертирует данные из CSV файла в объекты `SimpleNamespace`.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу для чтения.

**Возвращает**:
- `SimpleNamespace | None`: Объект `SimpleNamespace`, содержащий данные из CSV, или `None`, если преобразование не удалось.

**Вызывает исключения**:
- `Exception`: Если не удается прочитать CSV.

### `csv_to_json`

**Описание**: Конвертирует данные из CSV файла в JSON формат и сохраняет их в JSON файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV файлу для чтения.
- `json_file_path` (str | Path): Путь к JSON файлу для сохранения.
- `exc_info` (bool, optional): Если `True`, включает информацию трассировки в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: JSON данные в виде списка словарей, или `None`, если преобразование не удалось.

**Пример**:
```python
json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
print(json_data)
# Вывод: [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```