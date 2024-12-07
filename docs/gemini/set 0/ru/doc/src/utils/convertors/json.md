# Модуль hypotez/src/utils/convertors/json

## Обзор

Модуль `json` предоставляет функции для преобразования данных в формате JSON в различные форматы: CSV, `SimpleNamespace`, XML и XLS. Он предназначен для работы с данными JSON, загружаемыми из файлов или в виде строк, списков или словарей.

## Функции

### `json2csv`

**Описание**: Функция преобразует данные JSON в формат CSV с разделителем запятая. Она может принимать данные JSON в виде строки, списка словарей или пути к файлу JSON.  Функция сохраняет данные в указанный CSV файл.

**Параметры**:
- `json_data` (str | list | dict | Path): Данные JSON в виде строки, списка словарей, словаря или пути к файлу JSON.
- `csv_file_path` (str | Path): Путь к файлу CSV, в который будут записаны данные.

**Возвращает**:
- bool: `True`, если преобразование прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если произошла ошибка при парсинге JSON или записи в CSV-файл.


### `json2ns`

**Описание**: Преобразует данные JSON в объект `SimpleNamespace`.

**Параметры**:
- `json_data` (str | dict | Path): Данные JSON в виде строки, словаря или пути к файлу JSON.

**Возвращает**:
- `SimpleNamespace`: Объект `SimpleNamespace`, содержащий данные из JSON.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если произошла ошибка при парсинге JSON.


### `json2xml`

**Описание**: Преобразует данные JSON в формат XML.

**Параметры**:
- `json_data` (str | dict | Path): Данные JSON в виде строки, словаря или пути к файлу JSON.
- `root_tag` (str, optional): Имя тега корня XML. По умолчанию "root".


**Возвращает**:
- str: Результирующая строка XML.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если произошла ошибка при парсинге JSON или преобразовании в XML.

### `json2xls`

**Описание**: Преобразует данные JSON в формат XLS.

**Параметры**:
- `json_data` (str | list | dict | Path): Данные JSON в виде строки, списка словарей или пути к файлу JSON.
- `xls_file_path` (str | Path): Путь к файлу XLS, в который будут записаны данные.


**Возвращает**:
- bool: `True`, если преобразование прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `ValueError`: Если тип `json_data` не поддерживается.
- `Exception`: Если произошла ошибка при парсинге JSON или записи в XLS-файл.