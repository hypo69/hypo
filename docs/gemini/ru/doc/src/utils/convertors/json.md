# Модуль hypotez/src/utils/convertors/json

## Обзор

Этот модуль предоставляет функции для конвертации данных в формате JSON в различные форматы, такие как CSV, SimpleNamespace, XML и XLS.

## Функции

### `json2csv`

**Описание**: Преобразует данные в формате JSON в CSV формат с запятой в качестве разделителя. Поддерживает входные данные в виде строки JSON, списка словарей, словаря или пути к файлу JSON.

**Параметры**:
- `json_data` (str | list | dict | Path): Данные в формате JSON (строка, список словарей, словарь или путь к файлу JSON).
- `csv_file_path` (str | Path): Путь к файлу CSV, в который будут записаны данные.

**Возвращает**:
- bool: `True`, если преобразование выполнено успешно, `False` - в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось разобрать JSON или записать CSV.


### `json2ns`

**Описание**: Преобразует данные в формате JSON в объект `SimpleNamespace`. Поддерживает входные данные в виде строки JSON, словаря или пути к файлу JSON.

**Параметры**:
- `json_data` (str | dict | Path): Данные в формате JSON (строка, словарь или путь к файлу JSON).

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace`, содержащий данные из JSON.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось разобрать JSON.


### `json2xml`

**Описание**: Преобразует данные в формате JSON в XML формат. Поддерживает входные данные в виде строки JSON, словаря или пути к файлу JSON.

**Параметры**:
- `json_data` (str | dict | Path): Данные в формате JSON (строка, словарь или путь к файлу JSON).
- `root_tag` (str, опционально): Имя тега корневого элемента XML. По умолчанию "root".

**Возвращает**:
- str: Результирующая строка XML.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось разобрать JSON или преобразовать данные в XML.


### `json2xls`

**Описание**: Преобразует данные в формате JSON в XLS формат. Поддерживает входные данные в виде строки JSON, списка словарей, словаря или пути к файлу JSON.

**Параметры**:
- `json_data` (str | list | dict | Path): Данные в формате JSON (строка, список словарей, словарь или путь к файлу JSON).
- `xls_file_path` (str | Path): Путь к файлу XLS, в который будут записаны данные.

**Возвращает**:
- bool: `True`, если преобразование выполнено успешно, `False` - в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если не удалось разобрать JSON или записать XLS.