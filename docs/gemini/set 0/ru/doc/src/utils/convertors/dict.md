# Модуль hypotez/src/utils/convertors/dict.py

## Обзор

Данный модуль предоставляет функции для конвертации словарей в объекты `SimpleNamespace` и обратно, а также для экспорта данных в различные форматы.

## Функции

### `replace_key_in_dict`

**Описание**: Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:

- `data` (dict | list): Словарь или список, в котором происходит замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:

- `dict`: Обновленный словарь с заменёнными ключами.

**Примеры использования**:

```python
# Пример 1: Простой словарь
data = {"old_key": "value"}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"new_key": "value"}

# Пример 2: Вложенный словарь
data = {"outer": {"old_key": "value"}}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"outer": {"new_key": "value"}}

# Пример 3: Список словарей
data = [{"old_key": "value1"}, {"old_key": "value2"}]
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится [{"new_key": "value1"}, {"new_key": "value2"}]

# Пример 4: Смешанная вложенная структура со списками и словарями
data = {"outer": [{"inner": {"old_key": "value"}}]}
updated_data = replace_key_in_dict(data, "old_key", "new_key")
# updated_data становится {"outer": [{"inner": {"new_key": "value"}}]}
```


### `dict2pdf`

**Описание**: Сохраняет данные словаря в файл PDF.

**Параметры**:

- `data` (dict | SimpleNamespace): Словарь, который нужно преобразовать в PDF.
- `file_path` (str | Path): Путь к выходному файлу PDF.

**Возвращает**:

- `None`.


### `dict2ns`

**Описание**: Рекурсивно преобразует словари в объекты `SimpleNamespace`.

**Параметры**:

- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:

- `Any`: Преобразованные данные в виде `SimpleNamespace` или списка `SimpleNamespace`.


### `dict2xml`

**Описание**: Создаёт строку XML из словаря.

**Параметры**:

- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

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

- `bool`: `True`, если файл был успешно сохранён, `False` в противном случае.

**Примечание**: Предполагает наличие функции `save_csv_file` (не определена в представленном коде).


### `dict2xls`

**Описание**: Сохраняет данные словаря или `SimpleNamespace` в XLS-файл.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для сохранения в XLS-файл.
- `file_path` (str | Path): Путь к XLS-файлу.

**Возвращает**:

- `bool`: `True`, если файл был успешно сохранён, `False` в противном случае.

**Примечание**: Предполагает наличие функции `save_xls_file` (не определена в представленном коде).


### `dict2html`

**Описание**: Генерирует строку HTML-таблицы из словаря или объекта `SimpleNamespace`.

**Параметры**:

- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию `'UTF-8'`.

**Возвращает**:

- `str`: Строка HTML, представляющая входной словарь.

```