# Модуль для взаимодействия с FTP серверами

## Обзор

Модуль `src.utils.ftp` предоставляет интерфейс для взаимодействия с FTP серверами. Он включает функции для отправки, получения и удаления файлов с FTP сервера.

## Подробней

Этот модуль предназначен для обеспечения возможности передачи медиафайлов (изображений, видео), электронных таблиц и других файлов на FTP-сервер и с него. Он использует библиотеку `ftplib` для установления соединения и выполнения операций с FTP-сервером. Модуль также включает обработку исключений и ведение журнала для обеспечения надежности и информативности.

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

**Параметры**:
- `source_file_path` (str): Путь к файлу, который необходимо отправить.
- `dest_dir` (str): Каталог назначения на FTP-сервере.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `bool`: `True`, если файл успешно отправлен, `False` в противном случае.

**Вызывает исключения**:
- `ftplib.Error`: Возникает при ошибках соединения с FTP-сервером или при передаче файла.

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

**Параметры**:
- `source_file_path` (str): Путь, по которому файл будет сохранен локально.
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `Union[str, bytes, None]`: Содержимое файла, если он успешно получен, `None` в противном случае.

**Вызывает исключения**:
- `ftplib.Error`: Возникает при ошибках соединения с FTP-сервером или при получении файла.

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

**Параметры**:
- `source_file_path` (str): Локальный путь к файлу (не используется).
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `bool`: `True`, если файл успешно удален, `False` в противном случае.

**Вызывает исключения**:
- `ftplib.Error`: Возникает при ошибках соединения с FTP-сервером или при удалении файла.

**Примеры**:

```python
success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)