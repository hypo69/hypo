# Модуль `test_ali_campaign_editor_jupyter_widgets.py`

## Обзор

Модуль содержит набор тестов для функций, связанных с файловой системой, таких как сохранение, чтение файлов, получение списка файлов и директорий. Модуль использует `pytest` для организации тестов и `unittest.mock` для создания мок-объектов, позволяющих изолировать тестируемые функции от реальной файловой системы.

## Подробней

Модуль предоставляет тесты для следующих функций:

- `save_text_file`: Проверяет сохранение текста в файл.
- `read_text_file`: Проверяет чтение текста из файла.
- `get_filenames`: Проверяет получение списка имен файлов из директории.
- `get_directory_names`: Проверяет получение списка имен директорий из пути.

Тесты используют моки для эмуляции файловой системы и логирования, что позволяет избежать реальных операций с файлами и проверить правильность вызовов функций.

## Функции

### `test_save_text_file`

```python
def test_save_text_file(mock_logger, mock_mkdir, mock_file_open):
    """Test saving text to a file.

    Args:
        mock_logger (MagicMock): Mocked logger instance.
        mock_mkdir (MagicMock): Mocked mkdir instance.
        mock_file_open (MagicMock): Mocked file open instance.

    Example:
        >>> test_save_text_file()
    """
    ...
```

**Назначение**: Тестирует функцию `save_text_file`, которая сохраняет текст в файл.

**Параметры**:

- `mock_logger` (MagicMock): Мок-объект для логирования.
- `mock_mkdir` (MagicMock): Мок-объект для создания директорий.
- `mock_file_open` (MagicMock): Мок-объект для открытия файлов.

**Возвращает**: None

**Как работает функция**:

1. Вызывает функцию `save_text_file` с тестовыми данными.
2. Проверяет, что функция `open` была вызвана с правильными аргументами (`"w"` для записи и кодировкой `"utf-8"`).
3. Проверяет, что метод `write` мок-объекта файла был вызван с правильным текстом.
4. Проверяет, что функция `mkdir` была вызвана один раз для создания директории.

**Примеры**:

```python
test_save_text_file()
```

### `test_read_text_file`

```python
def test_read_text_file(mock_file_open):
    """Test reading text from a file.

    Args:
        mock_file_open (MagicMock): Mocked file open instance.

    Returns:
        None

    Example:
        >>> content: str = test_read_text_file()
        >>> print(content)
        'This is a test.'
    """
    ...
```

**Назначение**: Тестирует функцию `read_text_file`, которая читает текст из файла.

**Параметры**:

- `mock_file_open` (MagicMock): Мок-объект для открытия файлов.

**Возвращает**: None

**Как работает функция**:

1. Вызывает функцию `read_text_file` с тестовым именем файла.
2. Проверяет, что функция возвращает ожидаемый текст ("This is a test.").
3. Проверяет, что функция `open` была вызвана с правильными аргументами (`"r"` для чтения и кодировкой `"utf-8"`).

**Примеры**:

```python
content: str = test_read_text_file()
print(content)
```

### `test_get_filenames`

```python
def test_get_filenames():
    """Test getting filenames from a directory.

    Returns:
        None

    Example:
        >>> filenames: list[str] = test_get_filenames()
        >>> print(filenames)
        ['file1.txt', 'file2.txt']
    """
    ...
```

**Назначение**: Тестирует функцию `get_filenames`, которая получает список имен файлов из директории.

**Параметры**: None

**Возвращает**: None

**Как работает функция**:

1. Использует `patch` для замены `Path.iterdir` мок-объектом, возвращающим список `Path` объектов, представляющих файлы.
2. Вызывает функцию `get_filenames` с тестовым путем директории.
3. Проверяет, что функция возвращает ожидаемый список имен файлов (`["file1.txt", "file2.txt"]`).

**Примеры**:

```python
filenames: list[str] = test_get_filenames()
print(filenames)
```

### `test_get_directory_names`

```python
def test_get_directory_names():
    """Test getting directory names from a path.

    Returns:
        None

    Example:
        >>> directories: list[str] = test_get_directory_names()
        >>> print(directories)
        ['dir1', 'dir2']
    """
    ...
```

**Назначение**: Тестирует функцию `get_directory_names`, которая получает список имен директорий из пути.

**Параметры**: None

**Возвращает**: None

**Как работает функция**:

1. Использует `patch` для замены `Path.iterdir` мок-объектом, возвращающим список `Path` объектов, представляющих директории.
2. Вызывает функцию `get_directory_names` с тестовым путем директории.
3. Проверяет, что функция возвращает ожидаемый список имен директорий (`["dir1", "dir2"]`).

**Примеры**:

```python
directories: list[str] = test_get_directory_names()
print(directories)
```