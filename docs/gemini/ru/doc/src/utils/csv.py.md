# Модуль для работы с CSV и JSON файлами
=================================================

Модуль содержит функции для сохранения, чтения и конвертации данных между CSV и JSON форматами.
Он предоставляет утилиты для работы с файлами, обеспечивая гибкость и удобство при обработке структурированных данных.

## Обзор

Этот модуль предоставляет набор функций для работы с CSV и JSON файлами. Он позволяет сохранять данные в формате CSV, читать CSV файлы и конвертировать их в JSON формат.
Модуль использует стандартные библиотеки `csv` и `json`, а также библиотеку `pandas` для более удобной работы с данными.
Все функции модуля поддерживают обработку исключений и логирование ошибок с использованием модуля `logger` из `src.logger.logger`.

## Подробней

Модуль предназначен для упрощения операций, связанных с CSV и JSON файлами.
Он предоставляет функции для сохранения данных в формате CSV, чтения данных из CSV файлов и конвертации CSV файлов в JSON формат.
Все функции модуля поддерживают обработку исключений и логирование ошибок, что делает его надежным инструментом для работы с данными.

## Функции

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """
    Saves a list of dictionaries to a CSV file.

    Args:
        data (List[Dict[str, str]]): List of dictionaries to save.
        file_path (Union[str, Path]): Path to the CSV file.
        mode (str): File mode ('a' to append, 'w' to overwrite). Default is 'a'.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if successful, otherwise False.

    Raises:
        TypeError: If input data is not a list of dictionaries.
        ValueError: If input data is empty.
    """
```

**Назначение**: Сохраняет список словарей в CSV файл.

**Параметры**:
- `data` (List[Dict[str, str]]): Список словарей для сохранения.
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `mode` (str): Режим открытия файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
- `exc_info` (bool): Включать ли информацию об исключении в логи.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, иначе `False`.

**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком словарей.
- `ValueError`: Если входные данные пусты.

**Как работает функция**:
1. Проверяет, что входные данные являются списком словарей.
2. Проверяет, что список словарей не пуст.
3. Преобразует `file_path` в объект `Path`.
4. Создает родительские директории, если они не существуют.
5. Открывает файл в указанном режиме (`mode`) с кодировкой `utf-8`.
6. Создает объект `csv.DictWriter` для записи словарей в CSV файл.
7. Если файл открыт для перезаписи (`mode == 'w'`) или файл не существует, записывает заголовок CSV файла.
8. Записывает данные в CSV файл.
9. Возвращает `True`, если запись прошла успешно.
10. В случае ошибки логирует ошибку и возвращает `False`.

```
Начало
  │
  ├── Проверка типа данных (List[Dict])
  │   └── Если не List[Dict]: TypeError
  │
  ├── Проверка на пустоту списка
  │   └── Если список пуст: ValueError
  │
  ├── Преобразование file_path в Path
  │   │
  │   ├── Создание родительских директорий
  │   │   │
  │   │   ├── Открытие файла (CSV)
  │   │   │   │
  │   │   │   ├── Создание writer
  │   │   │   │   │
  │   │   │   │   ├── Запись заголовка (если необходимо)
  │   │   │   │   │   │
  │   │   │   │   │   ├── Запись строк в CSV
  │   │   │   │   │   │   │
  │   │   │   │   │   │   └── Успех: True
  │   │   │   │   │   │
  │   │   │   │   │   └── Ошибка: False
  │   │   │   │   │
  │   │   │   │   └── Закрытие файла
  │   │   │   │
  │   │   │   └── Обработка исключений
  │   │   │       └── Логирование ошибки
  │   │   │           └── Возврат False
  │   │   │
  │   │   └── Возврат True
  │   │
  │   └── Логирование
  │       └── Конец
  │
  └── Конец
```

**Примеры**:

```python
data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
file_path = 'data.csv'
result = save_csv_file(data, file_path, mode='w')
print(result)  # Вывод: True

data = [{'name': 'Alice', 'age': '28'}]
file_path = 'data.csv'
result = save_csv_file(data, file_path, mode='a')
print(result)  # Вывод: True
```

### `read_csv_file`

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Reads CSV content as a list of dictionaries.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        List[Dict[str, str]] | None: List of dictionaries or None if failed.

    Raises:
        FileNotFoundError: If file not found.
    """
```

**Назначение**: Читает содержимое CSV файла и возвращает его в виде списка словарей.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `exc_info` (bool): Включать ли информацию об исключении в логи.

**Возвращает**:
- `List[Dict[str, str]] | None`: Список словарей, представляющий содержимое CSV файла, или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Как работает функция**:
1. Открывает CSV файл для чтения с кодировкой `utf-8`.
2. Создает объект `csv.DictReader` для чтения CSV файла как списка словарей.
3. Читает все строки из CSV файла и преобразует их в список словарей.
4. Возвращает список словарей.
5. В случае ошибки `FileNotFoundError` логирует ошибку и возвращает `None`.
6. В случае другой ошибки логирует ошибку и возвращает `None`.

```
Начало
  │
  ├── Открытие файла (CSV)
  │   │
  │   ├── Создание reader
  │   │   │
  │   │   ├── Чтение данных из CSV
  │   │   │   │
  │   │   │   ├── Преобразование в List[Dict]
  │   │   │   │   │
  │   │   │   │   └── Успех: List[Dict]
  │   │   │   │
  │   │   │   └── Закрытие файла
  │   │   │
  │   │   └── Обработка исключений
  │   │       └── FileNotFoundError
  │   │           └── Логирование ошибки
  │   │           └── Возврат None
  │   │
  │   └── Обработка исключений
  │       └── Логирование ошибки
  │           └── Возврат None
  │
  └── Конец
```

**Примеры**:

```python
file_path = 'data.csv'
data = read_csv_file(file_path)
if data:
    print(data)  # Вывод: [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
else:
    print('Failed to read CSV file.')
```

### `read_csv_as_json`

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Convert a CSV file to JSON format and save it.

    Args:
        csv_file_path (Union[str, Path]): Path to the CSV file.
        json_file_path (Union[str, Path]): Path to save the JSON file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if conversion is successful, else False.
    """
```

**Назначение**: Конвертирует CSV файл в JSON формат и сохраняет его.

**Параметры**:
- `csv_file_path` (Union[str, Path]): Путь к CSV файлу.
- `json_file_path` (Union[str, Path]): Путь для сохранения JSON файла.
- `exc_info` (bool): Включать ли информацию об исключении в логи.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `False`.

**Как работает функция**:
1. Читает CSV файл с помощью функции `read_csv_file`.
2. Если чтение CSV файла не удалось, возвращает `False`.
3. Открывает JSON файл для записи с кодировкой `utf-8`.
4. Записывает данные в JSON файл с отступом 4 для читаемости.
5. Возвращает `True`, если конвертация и запись прошли успешно.
6. В случае ошибки логирует ошибку и возвращает `False`.

```
Начало
  │
  ├── Чтение CSV файла (read_csv_file)
  │   │
  │   ├── Если чтение не удалось: False
  │   │
  │   ├── Открытие файла (JSON)
  │   │   │
  │   │   ├── Запись данных в JSON
  │   │   │   │
  │   │   │   └── Успех: True
  │   │   │
  │   │   └── Закрытие файла
  │   │
  │   └── Обработка исключений
  │       └── Логирование ошибки
  │           └── Возврат False
  │
  └── Конец
```

**Примеры**:

```python
csv_file_path = 'data.csv'
json_file_path = 'data.json'
result = read_csv_as_json(csv_file_path, json_file_path)
print(result)  # Вывод: True
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Convert CSV content to a dictionary.

    Args:
        csv_file (Union[str, Path]): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.
    """
```

**Назначение**: Конвертирует содержимое CSV файла в словарь.

**Параметры**:
- `csv_file` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `dict | None`: Словарь, представляющий содержимое CSV файла, или `None` в случае ошибки.

**Как работает функция**:
1. Открывает CSV файл для чтения с кодировкой `utf-8`.
2. Создает объект `csv.DictReader` для чтения CSV файла как списка словарей.
3. Читает все строки из CSV файла и преобразует их в список словарей.
4. Возвращает словарь, содержащий список словарей под ключом "data".
5. В случае ошибки логирует ошибку и возвращает `None`.

```
Начало
  │
  ├── Открытие файла (CSV)
  │   │
  │   ├── Создание reader
  │   │   │
  │   │   ├── Чтение данных из CSV
  │   │   │   │
  │   │   │   ├── Преобразование в Dict
  │   │   │   │   │
  │   │   │   │   └── Успех: Dict
  │   │   │   │
  │   │   │   └── Закрытие файла
  │   │   │
  │   │   └── Обработка исключений
  │   │       └── Логирование ошибки
  │   │           └── Возврат None
  │
  └── Конец
```

**Примеры**:

```python
csv_file = 'data.csv'
data = read_csv_as_dict(csv_file)
if data:
    print(data)
    # Вывод: {'data': [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]}
else:
    print('Failed to read CSV file as dictionary.')
```

### `read_csv_as_ns`

```python
def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """!
    Load CSV data into a list of dictionaries using Pandas.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.

    Returns:
        List[dict]: List of dictionaries representing the CSV content.

    Raises:
        FileNotFoundError: If file not found.
    """
```

**Назначение**: Загружает CSV данные в список словарей с использованием Pandas.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `List[dict]`: Список словарей, представляющий содержимое CSV файла.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Как работает функция**:
1. Читает CSV файл с использованием `pandas.read_csv`.
2. Преобразует данные в список словарей с использованием `df.to_dict(orient='records')`.
3. Возвращает список словарей.
4. В случае `FileNotFoundError` логирует ошибку и возвращает пустой список.
5. В случае другой ошибки логирует ошибку и возвращает пустой список.

```
Начало
  │
  ├── Чтение CSV файла (pandas.read_csv)
  │   │
  │   ├── Преобразование в List[dict]
  │   │   │
  │   │   └── Успех: List[dict]
  │   │
  │   └── Обработка исключений
  │       └── FileNotFoundError
  │           └── Логирование ошибки
  │           └── Возврат []
  │
  └── Обработка исключений
      └── Логирование ошибки
          └── Возврат []
  │
  └── Конец
```

**Примеры**:

```python
file_path = 'data.csv'
data = read_csv_as_ns(file_path)
print(data)
# Вывод: [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]