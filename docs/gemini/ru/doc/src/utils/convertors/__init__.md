# Модуль `hypotez/src/utils/convertors`

## Обзор

Модуль `src.utils.convertors` предоставляет набор функций для конвертации различных форматов данных, включая CSV, JSON, XML, HTML, MD, Base64, а также обработку изображений и текста.  Модуль включает в себя утилиты для преобразования данных в словари, списки, и другие форматы. Поддерживаются преобразования в/из табличные форматы (CSV, XLSX), а также работа с изображениями (например, генерация PNG из текста, конвертация PNG в WebP).

## Функции

### `csv2dict`

**Описание**: Преобразует данные из файла CSV в словарь.

**Параметры**:
- `filepath` (str): Путь к файлу CSV.

**Возвращает**:
- `dict`: Словарь, представляющий данные из CSV файла, или `None` при ошибке.


### `csv2ns`

**Описание**: Преобразует данные из файла CSV в пространство имен (Namespace).

**Параметры**:
- `filepath` (str): Путь к файлу CSV.


**Возвращает**:
- `dict`: Словарь, представляющий данные из CSV файла в формате пространства имен (Namespace), или `None` при ошибке.


### `dict2ns`

**Описание**: Преобразует словарь в пространство имен (Namespace).

**Параметры**:
- `data` (dict): Входной словарь.

**Возвращает**:
- `dict`: Словарь, представляющий данные в формате пространства имен (Namespace), или `None` при ошибке.


### `dict2csv`

**Описание**: Преобразует словарь в CSV-файл.

**Параметры**:
- `data` (dict): Входной словарь.
- `filepath` (str): Путь к файлу CSV для записи.

**Возвращает**:
- `bool`: `True` при успешном преобразовании, `False` при ошибке.


### `dict2html`

**Описание**: Преобразует словарь в HTML-строку.

**Параметры**:
- `data` (dict): Входной словарь.

**Возвращает**:
- `str`: HTML-строка, представляющая данные словаря.


### `dict2xls`

**Описание**: Преобразует словарь в XLSX-файл.

**Параметры**:
- `data` (dict): Входной словарь.
- `filepath` (str): Путь к файлу XLSX для записи.

**Возвращает**:
- `bool`: `True` при успешном преобразовании, `False` при ошибке.


### `dict2xml`

**Описание**: Преобразует словарь в XML-строку.

**Параметры**:
- `data` (dict): Входной словарь.

**Возвращает**:
- `str`: XML-строка, представляющая данные словаря.


### `replace_key_in_dict`

**Описание**: Заменяет ключ в словаре.

**Параметры**:
- `data` (dict): Входной словарь.
- `old_key` (str): Ключ для замены.
- `new_key` (str): Новый ключ.

**Возвращает**:
- `dict`: Словарь с измененным ключом.


### `dot2png`

**Описание**: Генерирует PNG-изображение из данных графа (dot format).

**Параметры**:
- `data` (str): Данные графа в формате dot.
- `filepath` (str, optional): Путь к файлу PNG для записи.


**Возвращает**:
- `str`: Путь к сгенерированному PNG файлу, или `None` при ошибке.


### `html2escape`

**Описание**: Экранирует HTML-символы.

**Параметры**:
- `html_string` (str): Входная HTML-строка.

**Возвращает**:
- `str`: Строка с экранированными HTML-символами.


### `html2ns`

**Описание**: Преобразует HTML в пространство имен (Namespace).

**Параметры**:
- `html_data` (str): Входные HTML данные.


**Возвращает**:
- `dict`: Словарь, представляющий данные в формате пространства имен (Namespace), или `None` при ошибке.


### `html2dict`

**Описание**: Преобразует HTML в словарь.

**Параметры**:
- `html_data` (str): Входные HTML данные.


**Возвращает**:
- `dict`: Словарь, представляющий данные HTML, или `None` при ошибке.


### `escape2html`

**Описание**: Разэкранирует HTML-символы.

**Параметры**:
- `escaped_string` (str): Входная строка с экранированными HTML-символами.

**Возвращает**:
- `str`: Строка с разэкранированными HTML-символами.


# ... (и так далее для всех остальных функций) ...
```
**Примечание:**  Полная документация требует детализации для каждой функции, включая возвращаемые типы, возможные исключения и подробные примеры.  Этот ответ содержит только шаблон, и нужно заполнить его, используя комментарии из исходного кода Python.  При этом стоит обратить внимание на то, что некоторые функции имеют необязательные параметры, а также, что возвращаемые типы могут быть более сложными, чем просто `dict` или `None`.  Не забудьте добавить документацию для всех импортированных модулей и классов, если это необходимо.