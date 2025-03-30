# Модуль `csv`

## Обзор

Модуль `csv` предоставляет утилиты для работы с CSV и JSON файлами. Он включает функции для сохранения данных в CSV файлы, чтения данных из CSV файлов в различных форматах (список словарей, JSON, словарь), а также для преобразования CSV файлов в JSON формат. Модуль использует библиотеку `csv` для работы с CSV файлами, библиотеку `json` для работы с JSON файлами, библиотеку `pathlib` для работы с путями к файлам и библиотеку `pandas` для чтения CSV в формате списка словарей. Также используется модуль `logger` из `src.logger.logger` для логирования ошибок и исключений.

## Подробней

Этот модуль предназначен для упрощения операций чтения и записи CSV и JSON файлов, предоставляя удобные функции для работы с данными в различных форматах. Он позволяет сохранять данные в CSV файлы, читать CSV файлы и преобразовывать их в JSON формат, а также читать CSV файлы в формате списка словарей или словаря. Модуль обеспечивает обработку исключений и логирование ошибок для повышения надежности и удобства использования. Расположение файла в проекте `hypotez/src/utils/csv.py` указывает на то, что он является частью утилитного функционала, используемого в других частях проекта.

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

    **Как работает функция**:

    Функция `save_csv_file` сохраняет список словарей в CSV файл.
    Сначала проверяется, что входные данные являются списком словарей и не пусты.
    Затем создается путь к файлу, при необходимости создаются родительские директории.
    Файл открывается в указанном режиме (добавление или перезапись).
    Если файл открывается для записи или не существует, записывается заголовок CSV файла.
    Затем записываются данные в CSV файл.
    В случае успеха возвращается `True`, в случае ошибки - `False`.
    Ошибки логируются с использованием модуля `logger`.


    ```mermaid
graph TD
    A[Начало: Проверка типа данных] --> B(Преобразование file_path в Path)
    B --> C{Создание директорий}
    C --> D[Открытие файла]
    D --> E(Запись заголовка)
    E --> F{Запись данных}
    F --> G[Завершение: Возврат результата]
    ```
    
    # Saves a list of dictionaries to a CSV file.
```

**Описание**: Сохраняет список словарей в CSV файл.

**Параметры**:
- `data` (List[Dict[str, str]]): Список словарей для сохранения.
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `mode` (str, optional): Режим открытия файла ('a' - добавление, 'w' - перезапись). По умолчанию 'a'.
- `exc_info` (bool, optional): Включать ли информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, иначе `False`.

**Вызывает исключения**:
- `TypeError`: Если входные данные не являются списком словарей.
- `ValueError`: Если входные данные пусты.

**Примеры**:

```python
data = [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col2': 'data4'}]
file_path = 'output.csv'
result = save_csv_file(data, file_path, mode='w')
print(f"CSV file saved successfully: {result}")
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

    **Как работает функция**:

    Функция `read_csv_file` читает содержимое CSV файла и возвращает его в виде списка словарей.
    Сначала открывается файл по указанному пути.
    Затем создается `csv.DictReader` для чтения данных из файла.
    Данные считываются и преобразуются в список словарей.
    В случае успеха возвращается список словарей, в случае ошибки (например, файл не найден) - `None`.
    Ошибки логируются с использованием модуля `logger`.
    ```
    st=>start: Открытие файла
    op1=>operation: Чтение данных из файла
    op2=>operation: Преобразование данных в список словарей
    e=>end: Возврат результата

    st->op1->op2->e
    ```
    """
    # Reads CSV content as a list of dictionaries.
```

**Описание**: Читает содержимое CSV файла в виде списка словарей.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.
- `exc_info` (bool, optional): Включать ли информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Список словарей или `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'input.csv'
data = read_csv_file(file_path)
if data:
    print(f"CSV data: {data}")
else:
    print("Failed to read CSV file.")
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

    **Как работает функция**:

    Функция `read_csv_as_json` преобразует CSV файл в JSON формат и сохраняет его в указанный файл.
    Сначала считываются данные из CSV файла с помощью функции `read_csv_file`.
    Если данные успешно считаны, они записываются в JSON файл с отступом 4 для удобочитаемости.
    В случае успеха возвращается `True`, в случае ошибки - `False`.
    Ошибки логируются с использованием модуля `logger`.
    ```
    st=>start: Чтение данных из CSV файла
    op1=>operation: Запись данных в JSON файл
    e=>end: Возврат результата

    st->op1->e
    ```
    """
    # Convert a CSV file to JSON format and save it.
```

**Описание**: Преобразует CSV файл в JSON формат и сохраняет его.

**Параметры**:
- `csv_file_path` (Union[str, Path]): Путь к CSV файлу.
- `json_file_path` (Union[str, Path]): Путь для сохранения JSON файла.
- `exc_info` (bool, optional): Включать ли информацию об исключении в логи. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, иначе `False`.

**Примеры**:

```python
csv_file_path = 'input.csv'
json_file_path = 'output.json'
result = read_csv_as_json(csv_file_path, json_file_path)
print(f"CSV to JSON conversion successful: {result}")
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

    **Как работает функция**:

    Функция `read_csv_as_dict` читает содержимое CSV файла и возвращает его в виде словаря, где ключ "data" содержит список словарей, представляющих строки CSV файла.
    Сначала открывается файл по указанному пути.
    Затем создается `csv.DictReader` для чтения данных из файла.
    Данные считываются и преобразуются в словарь.
    В случае успеха возвращается словарь, в случае ошибки - `None`.
    Ошибки логируются с использованием модуля `logger`.
    ```
    st=>start: Открытие файла
    op1=>operation: Чтение данных из файла
    op2=>operation: Преобразование данных в словарь
    e=>end: Возврат результата

    st->op1->op2->e
    ```
    """
    # Convert CSV content to a dictionary.
```

**Описание**: Преобразует содержимое CSV файла в словарь.

**Параметры**:
- `csv_file` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `dict | None`: Словарь, представляющий содержимое CSV файла, или `None` в случае ошибки.

**Примеры**:

```python
csv_file = 'input.csv'
data = read_csv_as_dict(csv_file)
if data:
    print(f"CSV data as dictionary: {data}")
else:
    print("Failed to read CSV as dictionary.")
```

### `read_csv_as_ns`

```python
def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """
    Load CSV data into a list of dictionaries using Pandas.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.

    Returns:
        List[dict]: List of dictionaries representing the CSV content.

    Raises:
        FileNotFoundError: If file not found.

    **Как работает функция**:

    Функция `read_csv_as_ns` читает содержимое CSV файла с использованием библиотеки Pandas и возвращает его в виде списка словарей.
    Сначала считываются данные из CSV файла с помощью `pd.read_csv`.
    Затем данные преобразуются в список словарей с помощью `df.to_dict(orient='records')`.
    В случае успеха возвращается список словарей, в случае ошибки (например, файл не найден) - пустой список.
    Ошибки логируются с использованием модуля `logger`.
    ```
    st=>start: Чтение данных из CSV файла с использованием Pandas
    op1=>operation: Преобразование данных в список словарей
    e=>end: Возврат результата

    st->op1->e
    ```
    """
    # Load CSV data into a list of dictionaries using Pandas.
```

**Описание**: Загружает данные CSV в список словарей с использованием Pandas.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу.

**Возвращает**:
- `List[dict]`: Список словарей, представляющий содержимое CSV файла.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'input.csv'
data = read_csv_as_ns(file_path)
print(f"CSV data as list of dictionaries (Pandas): {data}")