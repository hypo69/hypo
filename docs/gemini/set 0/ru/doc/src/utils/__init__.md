# Модуль utils

## Обзор

Этот модуль содержит набор небольших, полезных утилит, предназначенных для упрощения повседневных задач программирования. Модуль включает инструменты для конвертации данных, работы с файлами и формата вывода. Это позволяет ускорить разработку, предоставляя простые и переиспользуемые функции.

## Утилиты для конвертации данных

### `csv2dict`

**Описание**: Функция конвертирует данные из CSV-файла в словарь Python.

**Параметры**:
- `filename` (str): Путь к файлу CSV.

**Возвращает**:
- `dict`: Словарь, содержащий данные из CSV-файла. Возвращает `None`, если файл не найден или обработка завершилась ошибкой.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл CSV не найден.
- `ValueError`: Если данные в CSV-файле не соответствуют ожидаемому формату.


### `json2xls`

**Описание**: Функция конвертирует данные из JSON-файла в XLSX-файл.

**Параметры**:
- `filename` (str): Путь к файлу JSON.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл JSON не найден.
- `ValueError`: Если данные в JSON-файле не соответствуют ожидаемому формату.
- `Exception`: В случае других ошибок при конвертации.


### `save_text_file`

**Описание**: Функция сохраняет текст в указанный текстовый файл.

**Параметры**:
- `filename` (str): Путь к файлу.
- `text` (str): Текст для сохранения.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `IOError`: Если произошла ошибка ввода-вывода при записи файла.


## Утилиты для работы с файлами

### `read_text_file`

**Описание**: Функция считывает содержимое текстового файла.

**Параметры**:
- `filename` (str): Путь к файлу.

**Возвращает**:
- `str`: Содержимое файла.
- `None`: Если файл не найден или произошла ошибка.

**Вызывает исключения**:
- `FileNotFoundError`: Если указанный файл не найден.
- `IOError`: Если произошла ошибка ввода-вывода.


### `save_csv_file`

**Описание**: Функция сохраняет данные в CSV-файл.

**Параметры**:
- `filename` (str): Путь к файлу.
- `data` (list[list]): Данные для сохранения в формате списка списков.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, `False` в противном случае.

**Вызывает исключения**:
- `IOError`: Если произошла ошибка при записи в файл.
- `TypeError`: Если тип данных `data` не соответствует ожидаемому.


## Другие утилиты


### `get_filenames`

**Описание**: Возвращает список имен файлов в указанной директории.

**Параметры**:
- `directory` (str): Путь к директории.

**Возвращает**:
- `list[str]`: Список имен файлов в указанной директории.
- `None`: Если указанная директория не найдена или произошла ошибка.

**Вызывает исключения**:
- `FileNotFoundError`: Если директория не найдена.
- `OSError`: Если произошла ошибка при работе с файловой системой.


### `TimeoutCheck`

**Описание**: Класс для проверки на превышение таймаута.

**Описание методов** (в случае методов, если не указано, то предполагается, что метод имеет стандартные параметры для работы с таймером):

- (Подробные описания методов по каждому классу нужно дописывать, если есть необходимые методы)


(Повторить аналогичные разделы для остальных функций и классов из модуля `src.utils`, используя предоставленные комментарии и информацию о параметрах, возвращаемых значениях и исключениях.)