# Модуль для конвертации Base64 в файл
## Обзор

Модуль `base64.py` предоставляет функции для работы с кодировкой Base64, включая декодирование Base64 контента в временный файл и кодирование изображений в Base64. Это может быть полезно, когда необходимо обрабатывать данные, представленные в формате Base64, например, при работе с API или при передаче файлов через сеть.

## Подробней

Модуль содержит две основные функции: `base64_to_tmpfile` и `base64encode`.
- `base64_to_tmpfile` декодирует Base64 контент и сохраняет его во временный файл с определенным расширением.
- `base64encode` кодирует содержимое изображения в формат Base64.

## Функции

### `base64_to_tmpfile`

```python
def base64_to_tmpfile(content: str, file_name: str) -> str:
    """
    Convert Base64 encoded content to a temporary file.

    This function decodes the Base64 encoded content and writes it to a temporary file with the same extension as the provided file name. 
    The path to the temporary file is returned.

    Args:
        content (str): Base64 encoded content to be decoded and written to the file.
        file_name (str): Name of the file used to extract the file extension for the temporary file.

    Returns:
        str: Path to the temporary file.

    Example:
        >>> base64_content = "SGVsbG8gd29ybGQh"  # Base64 encoded content "Hello world!"
        >>> file_name = "example.txt"
        >>> tmp_file_path = base64_to_tmpfile(base64_content, file_name)
        >>> print(f"Temporary file created at: {tmp_file_path}")
        Temporary file created at: /tmp/tmpfile.txt
    """
    ...
```

**Назначение**: Преобразует Base64-закодированный контент во временный файл.

**Параметры**:
- `content` (str): Base64-закодированный контент, который нужно декодировать и записать в файл.
- `file_name` (str): Имя файла, используемое для извлечения расширения для временного файла.

**Возвращает**:
- `str`: Путь к временному файлу.

**Как работает функция**:
1. Извлекается расширение файла из `file_name`.
2. Создается временный файл с использованием `tempfile.NamedTemporaryFile`, при этом указывается расширение файла, полученное на предыдущем шаге. Файл создается с параметром `delete=False`, чтобы он не был автоматически удален после закрытия.
3. Декодируется Base64 контент с помощью `base64.b64decode(content)`.
4. Декодированный контент записывается во временный файл.
5. Получается путь к созданному временному файлу.
6. Возвращается путь к временному файлу.

```text
Контент Base64
     ↓
Извлечение расширения файла
     ↓
Создание временного файла
     ↓
Декодирование Base64 контента
     ↓
Запись декодированного контента во временный файл
     ↓
Получение пути к временному файлу
     ↓
Возврат пути к временному файлу
```

**Примеры**:

```python
>>> base64_content = "SGVsbG8gd29ybGQh"  # Base64 encoded content "Hello world!"
>>> file_name = "example.txt"
>>> tmp_file_path = base64_to_tmpfile(base64_content, file_name)
>>> print(f"Temporary file created at: {tmp_file_path}")
Temporary file created at: /tmp/tmpfile.txt
```

### `base64encode`

```python
def base64encode(image_path):
    # Function to encode the image
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
```

**Назначение**: Кодирует содержимое изображения в формат Base64.

**Параметры**:
- `image_path` (str): Путь к файлу изображения, который нужно закодировать.

**Возвращает**:
- `str`: Base64-закодированное представление изображения.

**Как работает функция**:
1. Открывает файл изображения по указанному пути в режиме чтения байтов (`"rb"`).
2. Считывает содержимое файла изображения целиком с помощью `image_file.read()`.
3. Кодирует содержимое изображения в формат Base64 с помощью `base64.b64encode()`.
4. Декодирует полученное Base64-представление в строку UTF-8 с помощью `.decode('utf-8')`.
5. Возвращает Base64-закодированную строку.

```text
Путь к файлу изображения
     ↓
Открытие файла изображения в режиме чтения байтов
     ↓
Чтение содержимого файла
     ↓
Кодирование содержимого в Base64
     ↓
Декодирование Base64 в строку UTF-8
     ↓
Возврат Base64-закодированной строки
```

**Примеры**:

```python
>>> image_path = "example.jpg"
>>> base64_string = base64encode(image_path)
>>> print(f"Base64 encoded string: {base64_string[:100]}...")  # Вывод первых 100 символов
Base64 encoded string: /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpL...