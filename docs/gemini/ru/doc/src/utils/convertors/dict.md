# Модуль `hypotez/src/utils/convertors/dict.py`

## Обзор

Модуль `hypotez/src/utils/convertors/dict.py` содержит функции для конвертации словарей в объекты `SimpleNamespace` и обратно, а также для экспорта данных в различные форматы.  Он предоставляет инструменты для обработки данных различной структуры, включая вложенные словари и списки.

## Функции

### `dict2ns`

**Описание**: Рекурсивно преобразует словари в объекты `SimpleNamespace`.

**Параметры**:

- `data` (Dict[str, Any] | List[Any]): Данные для преобразования. Может быть словарем или списком.

**Возвращает**:

- `Any`: Преобразованные данные в виде объекта `SimpleNamespace` или списка объектов `SimpleNamespace`.

### `replace_key_in_dict`

**Описание**: Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:

- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:

- `dict`: Обновленный словарь с замененными ключами.

**Примеры использования**: см. в документации к функции.


### `dict2pdf`

**Описание**: Сохраняет данные словаря в файл PDF.

**Параметры**:

- `data` (dict | SimpleNamespace): Словарь для преобразования в PDF.
- `file_path` (str | Path): Путь к выходному файлу PDF.

**Возвращает**:

- `None`

**Примечания**: Преобразует SimpleNamespace в словарь для обработки.


### `dict2xml`

**Описание**: Генерирует строку XML из словаря.

**Параметры**:

- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:

- `str`: Строка XML, представляющая входной словарь.

**Возможные исключения**:

- `Exception`: Если предоставлено более одного корневого узла.

### `dict2csv`

**Описание**: Сохраняет данные словаря или `SimpleNamespace` в CSV-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для сохранения в CSV-файл.
- `file_path` (str | Path): Путь к CSV-файлу.

**Возвращает**:

- `bool`: `True`, если файл был сохранен успешно; `False`, в противном случае.


### `dict2xls`

**Описание**: Сохраняет данные словаря или `SimpleNamespace` в XLS-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
- `file_path` (str | Path): Путь к XLS-файлу.

**Возвращает**:

- `bool`: `True`, если файл был сохранен успешно; `False`, в противном случае.


### `dict2html`

**Описание**: Генерирует строку HTML-таблицы из словаря или объекта `SimpleNamespace`.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:

- `str`: Строка HTML, представляющая входной словарь.