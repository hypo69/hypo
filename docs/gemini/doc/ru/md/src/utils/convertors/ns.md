# Модуль hypotez/src/utils/convertors/ns.py

## Обзор

Модуль `ns.py` предоставляет функции для преобразования объектов `SimpleNamespace` в различные форматы: `dict`, `JSON`, `CSV`, `XML` и `XLS`.  Он используется для конвертации данных в удобные для обработки и хранения структуры.

## Функции

### `ns2dict`

**Описание**: Преобразует объект `SimpleNamespace` в словарь Python.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.

**Возвращает**:
- `dict`: Преобразованный словарь.

### `ns2json`

**Описание**: Преобразует объект `SimpleNamespace` в формат JSON.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `json_file_path` (str | Path, необязательно): Путь к файлу, в который будет сохранён JSON. Если не указан, возвращает строку JSON.

**Возвращает**:
- `str | bool`: Строка JSON, если путь к файлу не указан. В противном случае `True`, если файл успешно записан, или `False` в случае ошибки.

**Обрабатываемые исключения**:
- Любые исключения, возникающие при работе с файлами или JSON, будут логироваться в `logger`.

### `ns2csv`

**Описание**: Преобразует объект `SimpleNamespace` в формат CSV.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `csv_file_path` (str | Path): Путь к файлу, в который будет сохранён CSV.

**Возвращает**:
- `bool`: `True`, если преобразование и запись в файл прошли успешно, иначе `False`.

**Обрабатываемые исключения**:
- Любые исключения, возникающие при работе с файлами или CSV, будут логироваться в `logger`.

### `ns2xml`

**Описание**: Преобразует объект `SimpleNamespace` в формат XML.

**Параметры**:
- `ns_obj` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `root_tag` (str, необязательно): Имя корневого тега в XML. По умолчанию `"root"`.

**Возвращает**:
- `str`: Результирующая строка XML.

**Обрабатываемые исключения**:
- Любые исключения, возникающие при работе с XML, будут логироваться в `logger`.

### `ns2xls`

**Описание**: Преобразует объект `SimpleNamespace` в формат XLS.

**Параметры**:
- `data` (SimpleNamespace): Объект `SimpleNamespace` для преобразования.
- `xls_file_path` (str | Path): Путь к файлу, в который будет сохранён XLS.

**Возвращает**:
- `bool`: `True`, если преобразование и запись в файл прошли успешно, иначе `False`.

**Обрабатываемые исключения**:
- Любые исключения, возникающие при работе с XLS, будут логироваться в `logger`.