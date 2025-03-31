# Модуль `ftp`

## Обзор

Модуль `ftp` предоставляет интерфейс для взаимодействия с FTP-серверами. Он включает функции для отправки, получения и удаления файлов с FTP-сервера.

## Подробней

Этот модуль позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP-сервер и с него. Он использует библиотеку `ftplib` для установления соединения и выполнения операций с FTP-сервером.

## Функции

### `write`

```python
def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Args:
        source_file_path (str): Путь к файлу, который нужно отправить.
        dest_dir (str): Целевой каталог на FTP-сервере.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        bool: `True`, если файл успешно отправлен, `False` в противном случае.
    
    Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    # Establish connection to FTP server
    # Open the file and send it to the FTP server
    # Close the FTP session
    # Log error if connection to FTP server fails
    # Log error if file transfer to FTP server fails

```

**Описание**: Отправляет файл на FTP-сервер.

**Параметры**:
- `source_file_path` (str): Путь к файлу, который нужно отправить.
- `dest_dir` (str): Целевой каталог на FTP-сервере.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `bool`: `True`, если файл успешно отправлен, `False` в противном случае.

**Вызывает исключения**:
- `ftplib.error_perm`: Ошибка, связанная с правами доступа при подключении или отправке файла.
- `ftplib.error_temp`: Временная ошибка при подключении или отправке файла.
- `OSError`: Ошибка, связанная с файловой системой, например, файл не найден.

**Как работает функция**:

```
graph LR
    A[Начало] --> B{Установить соединение с FTP сервером};
    B -- Успешно --> C{Открыть файл для чтения};
    B -- Ошибка --> E[Логировать ошибку соединения];
    C -- Успешно --> D{Отправить файл на FTP сервер};
    C -- Ошибка --> F[Логировать ошибку открытия файла];
    D -- Успешно --> G[Закрыть FTP сессию];
    D -- Ошибка --> H[Логировать ошибку отправки файла];
    E --> J[Возврат False];
    F --> J;
    H --> J;
    G --> J;
    J[Возврат bool];
```

**Пример**:

```python
success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)
```

### `read`

```python
def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Args:
        source_file_path (str): Путь, по которому файл будет сохранен локально.
        dest_dir (str): Каталог на FTP-сервере, где находится файл.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        Union[str, bytes, None]: Содержимое файла, если он успешно получен, `None` в противном случае.

    Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    # Establish connection to FTP server
    # Retrieve the file
    # Close the FTP session
    # Log error if file retrieval from FTP server fails

```

**Описание**: Получает файл с FTP-сервера.

**Параметры**:
- `source_file_path` (str): Путь, по которому файл будет сохранен локально.
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `Union[str, bytes, None]`: Содержимое файла, если он успешно получен, `None` в противном случае.

**Вызывает исключения**:
- `ftplib.error_perm`: Ошибка, связанная с правами доступа при подключении или получении файла.
- `ftplib.error_temp`: Временная ошибка при подключении или получении файла.
- `OSError`: Ошибка, связанная с файловой системой, например, нет прав на запись файла.

**Как работает функция**:

```
graph LR
    A[Начало] --> B{Установить соединение с FTP сервером};
    B -- Успешно --> C{Открыть локальный файл для записи};
    B -- Ошибка --> E[Логировать ошибку соединения];
    C -- Успешно --> D{Получить файл с FTP сервера и записать в локальный файл};
    C -- Ошибка --> F[Логировать ошибку открытия локального файла];
    D -- Успешно --> G{Открыть локальный файл для чтения};
    D -- Ошибка --> H[Логировать ошибку получения файла];
    G --> I{Прочитать содержимое файла};
    E --> J[Возврат None];
    F --> J;
    H --> J;
    I --> J;
    J[Возврат Union[str, bytes, None]];
```

**Пример**:

```python
content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(content)
```

### `delete`

```python
def delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Args:
        source_file_path (str): Путь, где находится файл локально (не используется).
        dest_dir (str): Каталог на FTP-сервере, где находится файл.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        bool: `True`, если файл успешно удален, `False` в противном случае.

    Example:
        >>> success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    # Establish connection to FTP server
    # Delete the file
    # Close the FTP session
    # Log error if file deletion from FTP server fails

```

**Описание**: Удаляет файл с FTP-сервера.

**Параметры**:
- `source_file_path` (str): Путь, где находится файл локально (не используется).
- `dest_dir` (str): Каталог на FTP-сервере, где находится файл.
- `dest_file_name` (str): Имя файла на FTP-сервере.

**Возвращает**:
- `bool`: `True`, если файл успешно удален, `False` в противном случае.

**Вызывает исключения**:
- `ftplib.error_perm`: Ошибка, связанная с правами доступа при подключении или удалении файла.
- `ftplib.error_temp`: Временная ошибка при подключении или удалении файла.

**Как работает функция**:

```
graph LR
    A[Начало] --> B{Установить соединение с FTP сервером};
    B -- Успешно --> C{Удалить файл на FTP сервере};
    B -- Ошибка --> E[Логировать ошибку соединения];
    C -- Успешно --> G[Закрыть FTP сессию];
    C -- Ошибка --> H[Логировать ошибку удаления файла];
    E --> J[Возврат False];
    H --> J;
    G --> J;
    J[Возврат bool];
```

**Пример**:

```python
success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
print(success)