# Модуль utils

## Обзор

Этот модуль содержит набор утилит для работы с данными, файлами и форматированием вывода. Он предоставляет инструменты для конвертации данных, работы с файлами, и упрощения задач программирования.  Модуль включает в себя функции для работы с CSV, JSON, HTML, XML, текстовыми файлами, изображениями, датами, URL и т.д.

## Функции

### `csv2dict`

**Описание**: Преобразует CSV-файл в словарь Python.

**Параметры**:
- `filepath` (str): Путь к CSV-файлу.

**Возвращает**:
- `dict`: Словарь, представляющий данные CSV. Возвращает пустой словарь, если файл не найден или пуст.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `ValueError`: Если в файле неверный формат CSV или встречаются ошибки при парсинге.


### `json2xls`

**Описание**: Преобразует JSON-файл в XLSX-файл.

**Параметры**:
- `filepath` (str): Путь к JSON-файлу.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно; `False` - в противном случае.


**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.
- `ValueError`: Если в файле неверный формат JSON или встречаются ошибки при парсинге.
- `TypeError`: Если данные в JSON не в подходящем формате для конвертации в XLSX.


### `save_text_file`

**Описание**: Сохраняет текст в текстовый файл.

**Параметры**:
- `filepath` (str): Путь к файлу для сохранения.
- `text` (str): Текст для сохранения.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно; `False` - в противном случае.


**Вызывает исключения**:
- `TypeError`: Если тип `text` не `str`.
- `IOError`: Если произошла ошибка при записи в файл.


### ... (Остальные функции) ...

## Классы

### ... (Если есть классы, добавьте их документацию здесь) ...

## Модули

### `convertors`

### `csv`

### `date_time`

### `file`

### `image`

### `jjson`

### `pdf`

### `printer`

### `string`

### `url`

### `video`

### `path`

... (Остальные модули)


## Использование

См. примеры использования в docstrings отдельных функций и классов.