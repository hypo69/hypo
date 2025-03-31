# Модуль `src.utils.csv`

## Обзор

Модуль `src.utils.csv` предоставляет набор утилит для работы с файлами CSV и JSON. Он включает функции для сохранения данных в формате CSV, чтения данных из CSV файлов, преобразования CSV в JSON и представления CSV в виде словаря. Модуль использует библиотеку `csv` для работы с CSV файлами, библиотеку `json` для работы с JSON файлами, а также библиотеку `pandas` для более удобной работы с данными в формате DataFrame.

## Подорбней

Этот модуль предназначен для облегчения операций чтения и записи данных в форматах CSV и JSON. Он предоставляет функции для сохранения списков словарей в CSV файлы, чтения CSV файлов в списки словарей, конвертации CSV файлов в JSON формат, и чтения CSV файлов в виде словарей. Модуль также использует логирование для отслеживания ошибок и предупреждений. <инструкция для модели gemini:Более подробное описание модуля и его использования в проекте hypotez.>

## Функции

### `save_csv_file`

```python
def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """    Saves a list of dictionaries to a CSV file.

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
    ...
```

**Описание**: Сохраняет список словарей в CSV файл.

**Как работает функция**:
1. Проверяет, что входные данные являются списком словарей. Если нет, вызывает исключение `TypeError`.
2. Проверяет, что входные данные не пусты. Если пусты, вызывает исключение `ValueError`.
3. Преобразует `file_path` в объект `Path`.
4. Создает родительские каталоги, если они не существуют.
5. Открывает файл в указанном режиме (`a` - добавление, `w` - перезапись) с кодировкой UTF-8.
6. Создает объект `DictWriter` для записи словарей в CSV файл.
7. Если файл открыт для записи (`mode == 'w'`) или файл не существует, записывает заголовок CSV файла, используя ключи первого словаря в списке.
8. Записывает все словари из списка в CSV файл.
9. В случае успеха возвращает `True`, иначе логирует ошибку и возвращает `False`.

**Параметры**:
- `data` (List[Dict[str, str]]): Список словарей для сохранения в CSV файл. Каждый словарь представляет строку данных, где ключи - это заголовки столбцов.
- `file_path` (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом `Path`.
- `mode` (str, optional): Режим открытия файла. `'a'` - добавление в конец файла, `'w'` - перезапись файла. По умолчанию `'a'`.
- `exc_info` (bool, optional): Определяет, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если запись в файл прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `data` не является списком словарей.
- `ValueError`: Если `data` пустой.

**Примеры**:

```python
data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
file_path = 'data.csv'
success = save_csv_file(data, file_path, mode='w')
if success:
    print(f'CSV file saved to {file_path}')
```

### `read_csv_file`

```python
def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """    Reads CSV content as a list of dictionaries.

    Args:
        file_path (Union[str, Path]): Path to the CSV file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        List[Dict[str, str]] | None: List of dictionaries or None if failed.

    Raises:
        FileNotFoundError: If file not found.
    """
    ...
```

**Описание**: Читает содержимое CSV файла и возвращает его в виде списка словарей.

**Как работает функция**:
1. Открывает CSV файл по указанному пути в режиме чтения (`'r'`) с кодировкой UTF-8.
2. Создает объект `DictReader` для чтения CSV файла как словаря.
3. Преобразует содержимое файла в список словарей, где каждый словарь представляет строку данных, а ключи - это заголовки столбцов.
4. В случае успеха возвращает список словарей. Если файл не найден, логирует ошибку и возвращает `None`. В случае другой ошибки также логирует ошибку и возвращает `None`.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом `Path`.
- `exc_info` (bool, optional): Определяет, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `List[Dict[str, str]] | None`: Список словарей, представляющих данные из CSV файла. Возвращает `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'data.csv'
data = read_csv_file(file_path)
if data:
    for row in data:
        print(row)
```

### `read_csv_as_json`

```python
def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """    Convert a CSV file to JSON format and save it.

    Args:
        csv_file_path (Union[str, Path]): Path to the CSV file.
        json_file_path (Union[str, Path]): Path to save the JSON file.
        exc_info (bool): Include traceback information in logs.

    Returns:
        bool: True if conversion is successful, else False.
    """
    ...
```

**Описание**: Преобразует CSV файл в JSON формат и сохраняет его в указанный файл.

**Как работает функция**:
1. Считывает данные из CSV файла с помощью функции `read_csv_file`.
2. Если чтение CSV файла не удалось, возвращает `False`.
3. Открывает JSON файл в режиме записи (`'w'`) с кодировкой UTF-8.
4. Записывает данные в JSON файл с отступом 4 для удобочитаемости.
5. В случае успеха возвращает `True`, иначе логирует ошибку и возвращает `False`.

**Параметры**:
- `csv_file_path` (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом `Path`.
- `json_file_path` (Union[str, Path]): Путь к JSON файлу, в который будет сохранено преобразованное содержимое. Может быть строкой или объектом `Path`.
- `exc_info` (bool, optional): Определяет, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если преобразование и сохранение прошли успешно, `False` в противном случае.

**Примеры**:

```python
csv_file_path = 'data.csv'
json_file_path = 'data.json'
success = read_csv_as_json(csv_file_path, json_file_path)
if success:
    print(f'CSV file converted to JSON and saved to {json_file_path}')
```

### `read_csv_as_dict`

```python
def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """    Convert CSV content to a dictionary.

    Args:
        csv_file (Union[str, Path]): Path to the CSV file.

    Returns:
        dict | None: Dictionary representation of CSV content, or None if failed.
    """
    ...
```

**Описание**: Преобразует содержимое CSV файла в словарь.

**Как работает функция**:
1. Открывает CSV файл по указанному пути в режиме чтения (`'r'`) с кодировкой UTF-8.
2. Создает объект `DictReader` для чтения CSV файла как словаря.
3. Преобразует содержимое файла в словарь, где ключ `"data"` содержит список словарей, представляющих строки данных.
4. В случае успеха возвращает словарь, иначе логирует ошибку и возвращает `None`.

**Параметры**:
- `csv_file` (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом `Path`.

**Возвращает**:
- `dict | None`: Словарь, содержащий данные из CSV файла. Возвращает `None` в случае ошибки.

**Примеры**:

```python
csv_file = 'data.csv'
data = read_csv_as_dict(csv_file)
if data:
    print(data)
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
    ...
```

**Описание**: Загружает данные из CSV файла в список словарей, используя библиотеку `pandas`.

**Как работает функция**:
1. Читает CSV файл с использованием `pd.read_csv`, создавая DataFrame.
2. Преобразует DataFrame в список словарей, где каждый словарь представляет строку данных.
3. В случае успеха возвращает список словарей. Если файл не найден, логирует ошибку и возвращает пустой список. В случае другой ошибки также логирует ошибку и возвращает пустой список.

**Параметры**:
- `file_path` (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом `Path`.

**Возвращает**:
- `List[dict]`: Список словарей, представляющих данные из CSV файла. Возвращает пустой список в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.

**Примеры**:

```python
file_path = 'data.csv'
data = read_csv_as_ns(file_path)
if data:
    for row in data:
        print(row)
```