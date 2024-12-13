# Модуль `dict.py`

## Обзор

Модуль `dict.py` предоставляет набор инструментов для преобразования данных между форматами `dict` и `SimpleNamespace`, а также для экспорта данных в различные форматы, такие как `XML`, `CSV`, `JSON`, `XLS`, `HTML` и `PDF`.

## Оглавление

- [Функции](#Функции)
    - [`replace_key_in_dict`](#replace_key_in_dict)
    - [`dict2pdf`](#dict2pdf)
    - [`dict2ns`](#dict2ns)
    - [`dict2xml`](#dict2xml)
    - [`dict2csv`](#dict2csv)
    - [`dict2xls`](#dict2xls)
    - [`dict2html`](#dict2html)

## Функции

### `replace_key_in_dict`

**Описание**:
Рекурсивно заменяет ключ в словаре или списке.

**Параметры**:
- `data` (dict | list): Словарь или список, в котором выполняется замена ключа.
- `old_key` (str): Ключ, который нужно заменить.
- `new_key` (str): Новый ключ.

**Возвращает**:
- `dict`: Обновленный словарь с замененными ключами.

**Пример использования**:
```python
replace_key_in_dict(data, 'name', 'category_name')

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

**Описание**:
Сохраняет данные словаря в файл PDF.

**Параметры**:
- `data` (dict | SimpleNamespace): Словарь для конвертации в PDF.
- `file_path` (str | Path): Путь к выходному PDF файлу.

**Возвращает**:
- `None`

### `dict2ns`

**Описание**:
Рекурсивно преобразует словари в объекты SimpleNamespace.

**Параметры**:
- `data` (Dict[str, Any] | List[Any]): Данные для преобразования.

**Возвращает**:
- `Any`: Преобразованные данные в виде SimpleNamespace или списка SimpleNamespace.

### `dict2xml`

**Описание**:
Генерирует строку XML из словаря.

**Параметры**:
- `data` (Dict[str, Any]): Данные для преобразования в XML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: Строка XML, представляющая входной словарь.

**Вызывает исключения**:
- `Exception`: Если предоставлено более одного корневого узла.

### `dict2csv`

**Описание**:
Сохраняет данные словаря или SimpleNamespace в файл CSV.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в файл CSV.
- `file_path` (str | Path): Путь к файлу CSV.

**Возвращает**:
- `bool`: `True`, если файл был успешно сохранен, иначе `False`.

### `dict2xls`

**Описание**:
Сохраняет данные словаря или SimpleNamespace в файл XLS.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для сохранения в файл XLS.
- `file_path` (str | Path): Путь к файлу XLS.

**Возвращает**:
- `bool`: `True`, если файл был успешно сохранен, иначе `False`.

### `dict2html`

**Описание**:
Генерирует строку HTML-таблицы из словаря или объекта SimpleNamespace.

**Параметры**:
- `data` (dict | SimpleNamespace): Данные для преобразования в HTML.
- `encoding` (str, optional): Кодировка данных. По умолчанию 'UTF-8'.

**Возвращает**:
- `str`: Строка HTML, представляющая входной словарь.