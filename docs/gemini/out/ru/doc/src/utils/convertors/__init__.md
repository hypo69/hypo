# Модуль convertors

## Обзор

Модуль `convertors` предоставляет функции для конвертации различных форматов данных, включая CSV, JSON, XML, HTML, Markdown, Base64, изображения и текст.  Он включает утилиты для работы с данными в различных структурах, такими как словари, списки и таблицы.  Также поддерживается работа с изображениями (генерация, конвертация PNG в WebP), аудио (преобразование речи в текст и обратно) и кодирование/декодирование Base64.

## Функции

### `csv2dict`

**Описание**: Функция конвертирует данные из файла CSV в словарь.

**Параметры**:
- `filepath` (str): Путь к файлу CSV.

**Возвращает**:
- `dict`: Словарь, содержащий данные из файла CSV. Возвращает `None`, если файл не найден или некорректен.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл CSV не найден.
- `ValueError`: Если данные в файле CSV имеют неправильный формат.

### `csv2ns`

**Описание**: Функция конвертирует данные из файла CSV в пространство имен.

**Параметры**:
- `filepath` (str): Путь к файлу CSV.

**Возвращает**:
- `dict`: Словарь, содержащий данные из файла CSV, отформатированные как пространство имен. Возвращает `None`, если файл не найден или некорректен.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл CSV не найден.
- `ValueError`: Если данные в файле CSV имеют неправильный формат.


### `dict2ns`

**Описание**: Функция конвертирует словарь в представление пространства имен (namespace).


**Параметры**:
- `data` (dict): Входной словарь.

**Возвращает**:
- `dict`:  Данные в формате пространства имен. Возвращает `None`, если входной словарь некорректен.

**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.


### `dict2csv`

**Описание**: Функция конвертирует данные из словаря в формат CSV.

**Параметры**:
- `data` (dict): Входной словарь.
- `output_filepath` (str, optional): Путь к файлу для сохранения CSV данных. Если не указан, данные возвращаются в виде строки.

**Возвращает**:
- `str`: Строка в формате CSV, если `output_filepath` не указан.
- `None`: Если входной словарь некорректен.


**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.
- `IOError`: Проблемы при записи в файл (если `output_filepath` указан).


### `dict2html`

**Описание**: Преобразует словарь в HTML-строку.


**Параметры**:
- `data` (dict): Входной словарь.

**Возвращает**:
- `str`: HTML-строка, представляющая данные словаря. Возвращает `None`, если входной словарь некорректен.

**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.


### `dict2xls`

**Описание**: Функция преобразует словарь в формат XLSX.


**Параметры**:
- `data` (dict): Входной словарь.
- `output_filepath` (str, optional): Путь к выходному XLSX-файлу.

**Возвращает**:
- `None`:  Если данные словаря не могут быть преобразованы.

**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.
- `IOError`: Проблемы при записи в файл (если `output_filepath` указан).


### `dict2xml`

**Описание**: Конвертирует данные из словаря в XML-строку.

**Параметры**:
- `data` (dict):  Входной словарь.

**Возвращает**:
- `str`: XML-строка, представляющая данные из словаря. Возвращает `None`, если входной словарь некорректен.

**Вызывает исключения**:
- `TypeError`: Если `data` не является словарем.


... (и так далее для остальных функций)