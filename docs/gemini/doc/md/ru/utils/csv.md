```markdown
# Модуль hypotez/src/utils/csv

## Обзор

Этот модуль предоставляет инструменты для работы с CSV и JSON файлами.  Он позволяет сохранять и читать данные CSV, конвертировать между CSV и JSON форматами, а также преобразовывать CSV-контент в формат словарей для удобной обработки.

## Функции

### `save_csv_file`

**Описание**: Сохраняет список словарей в CSV файл.  Если файл уже существует, данные добавляются в конец (при `mode='a'`), иначе происходит перезапись (при `mode='w'`).

**Параметры**:
- `data` (List[Dict[str, str] | SimpleNamespace]): Список словарей или `SimpleNamespace` объектов для сохранения.
- `file_path` (str | Path): Путь к CSV файлу.
- `mode` (str, optional): Режим открытия файла ('a' - добавление, 'w' - перезапись). По умолчанию 'a'.
- `exc_info` (bool, optional): Включать информацию об исключении в логе. По умолчанию True.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, иначе `False`.

**Вызывает исключения**:
- Различные исключения при работе с файлами.


### `read_csv_file`

**Описание**: Читает содержимое CSV файла в виде списка словарей.

**Параметры**:
- `file_path` (str | Path): Путь к CSV файлу.
- `exc_info` (bool, optional): Включать информацию об исключении в логе. По умолчанию True.

**Возвращает**:
- List[Dict[str, str]] | None: Список словарей с данными CSV или `None`, если произошла ошибка.

**Вызывает исключения**:
- Различные исключения при работе с файлами.


### `read_csv_as_json`

**Описание**: Преобразует CSV файл в JSON и сохраняет его в новый файл.

**Параметры**:
- `csv_file_path` (str | Path): Путь к CSV файлу.
- `json_file_path` (str | Path): Путь для сохранения JSON файла.
- `exc_info` (bool, optional): Включать информацию об исключении в логе. По умолчанию True.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, иначе `False`.

**Вызывает исключения**:
- Различные исключения при работе с файлами и преобразовании форматов.


### `read_csv_as_dict`

**Описание**: Преобразует содержимое CSV файла в словарь.

**Параметры**:
- `csv_file` (str | Path): Путь к CSV файлу.

**Возвращает**:
- dict | None: Словарь, представляющий содержимое CSV файла, или `None`, если произошла ошибка.

**Вызывает исключения**:
- Различные исключения при работе с файлами.


### `read_csv_as_ns`

**Описание**: Загружает данные CSV в список словарей с использованием Pandas.

**Параметры**:
- `file_path` (str | Path): Путь к CSV файлу.

**Возвращает**:
- List[dict]: Список словарей, представляющих содержимое CSV.

**Вызывает исключения**:
- Различные исключения при работе с файлами и Pandas.


## Классы

(В данном модуле нет классов)


```