# Модуль `ftp`

## Обзор

Модуль предоставляет интерфейс для взаимодействия с FTP-серверами. Он включает в себя функции для отправки, получения и удаления файлов с FTP-сервера.

## Подробнее

Этот модуль предназначен для обеспечения возможности отправки медиафайлов (изображений, видео), электронных таблиц и других файлов на FTP-сервер и обратно. Он использует библиотеку `ftplib` для установления соединения с FTP-сервером и выполнения операций передачи файлов.

Модуль включает в себя следующие функции:

- `write`: Отправляет файл на FTP-сервер.
- `read`: Получает файл с FTP-сервера.
- `delete`: Удаляет файл с FTP-сервера.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `write`

```python
def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Sends a file to an FTP server.

    Args:
        source_file_path (str): The path of the file to be sent.
        dest_dir (str): The destination directory on the FTP server.
        dest_file_name (str): The name of the file on the FTP server.

    Returns:
        bool: True if the file is successfully sent, False otherwise.

    Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
```

**Описание**: Отправляет файл на FTP-сервер.

**Как работает функция**: Функция `write` устанавливает соединение с FTP-сервером, используя параметры из словаря `_connection` (предполагается, что он определен где-то в другом месте). Затем она переходит в указанный каталог на сервере и отправляет файл, расположенный по пути `source_file_path`, в этот каталог под именем `dest_file_name`. В случае успеха возвращает `True`, иначе — `False`.  В блоке `finally` происходит закрытие FTP-соединения, даже если возникли ошибки в процессе передачи файла.

**Параметры**:

- `source_file_path` (str): Путь к файлу, который необходимо отправить.
- `dest_dir` (str): Каталог назначения на FTP-сервере.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:

- `bool`: `True`, если файл успешно отправлен, `False` в противном случае.

**Вызывает исключения**:

- `ftplib.all_errors`: Общие исключения, связанные с FTP.
- `OSError`: Ошибки, связанные с файловой системой.

**Примеры**:

```python
success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
```

### `read`

```python
def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Retrieves a file from an FTP server.

    Args:
        source_file_path (str): The path where the file will be saved locally.
        dest_dir (str): The directory on the FTP server where the file is located.
        dest_file_name (str): The name of the file on the FTP server.

    Returns:
        Union[str, bytes, None]: The file content if successfully retrieved, None otherwise.

    Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
```

**Описание**: Получает файл с FTP-сервера.

**Как работает функция**: Функция `read` устанавливает соединение с FTP-сервером, используя параметры из словаря `_connection`. Затем она переходит в указанный каталог на сервере и скачивает файл `dest_file_name` в локальный файл `source_file_path`. В случае успеха возвращает содержимое файла в виде байтов, иначе — `None`. В блоке `finally` происходит закрытие FTP-соединения.

**Параметры**:

- `source_file_path` (str): Локальный путь, где будет сохранен файл.
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:

- `Union[str, bytes, None]`: Содержимое файла в виде байтов, если файл успешно получен, `None` в противном случае.

**Вызывает исключения**:

- `ftplib.all_errors`: Общие исключения, связанные с FTP.
- `OSError`: Ошибки, связанные с файловой системой.

**Примеры**:

```python
content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(content)
```

### `delete`

```python
def delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Deletes a file from an FTP server.

    Args:
        source_file_path (str): The path where the file is located locally (not used).
        dest_dir (str): The directory on the FTP server where the file is located.
        dest_file_name (str): The name of the file on the FTP server.

    Returns:
        bool: True if the file is successfully deleted, False otherwise.

    Example:
        >>> success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
```

**Описание**: Удаляет файл с FTP-сервера.

**Как работает функция**: Функция `delete` устанавливает соединение с FTP-сервером, используя параметры из словаря `_connection`. Затем она переходит в указанный каталог на сервере и удаляет файл `dest_file_name`. В случае успеха возвращает `True`, иначе — `False`.  В блоке `finally` происходит закрытие FTP-соединения.

**Параметры**:

- `source_file_path` (str): Локальный путь к файлу (не используется).
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:

- `bool`: `True`, если файл успешно удален, `False` в противном случае.

**Вызывает исключения**:

- `ftplib.all_errors`: Общие исключения, связанные с FTP.

**Примеры**:

```python
success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)