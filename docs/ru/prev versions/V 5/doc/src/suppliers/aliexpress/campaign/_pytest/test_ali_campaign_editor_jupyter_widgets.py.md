# Модуль тестирования виджетов редактора кампаний AliExpress

## Обзор

Этот модуль содержит набор тестов для функций, связанных с файловой системой, таких как сохранение, чтение и получение имен файлов и директорий. Модуль использует `pytest` для организации тестов и `unittest.mock` для изоляции тестируемых функций от реальной файловой системы.

## Подробней

Этот модуль тестирует функции, которые оперируют с файлами и директориями. Он использует `mock` для создания заглушек файловой системы, что позволяет проводить тесты без реального взаимодействия с файловой системой. Это особенно полезно для обеспечения стабильности и предсказуемости тестов.
Расположение модуля в структуре проекта указывает на то, что он предназначен для тестирования функциональности, связанной с редактором кампаний AliExpress, а именно с операциями над файлами, используемыми в этих кампаниях.

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
```

**Описание**: Тестирует сохранение текста в файл.

**Как работает функция**:

1.  Использует декораторы `@patch` для замены реальных объектов `Path.open`, `Path.mkdir` и `logger` моками (`MagicMock`).
2.  Вызывает функцию `save_text_file` с именем файла "test.txt" и содержимым "This is a test.".
3.  Проверяет, что метод `open` мок-объекта `mock_file_open` был вызван с параметрами "w" (режим записи) и кодировкой "utf-8".
4.  Проверяет, что метод `write` мок-объекта `mock_file_open` был вызван с содержимым "This is a test.".
5.  Проверяет, что метод `mkdir` мок-объекта `mock_mkdir` был вызван (единожды).

**Параметры**:

*   `mock_logger` (MagicMock): Заглушка для логгера.
*   `mock_mkdir` (MagicMock): Заглушка для метода создания директории.
*   `mock_file_open` (MagicMock): Заглушка для метода открытия файла.

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
```

**Описание**: Тестирует чтение текста из файла.

**Как работает функция**:

1.  Использует декоратор `@patch` для замены реального объекта `Path.open` моком (`MagicMock`), который при открытии возвращает строку "This is a test.".
2.  Вызывает функцию `read_text_file` с именем файла "test.txt".
3.  Проверяет, что возвращаемое значение функции `read_text_file` равно "This is a test.".
4.  Проверяет, что метод `open` мок-объекта `mock_file_open` был вызван с параметрами "r" (режим чтения) и кодировкой "utf-8".

**Параметры**:

*   `mock_file_open` (MagicMock): Заглушка для метода открытия файла.

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
```

**Описание**: Тестирует получение списка имен файлов из директории.

**Как работает функция**:

1.  Использует `patch` для замены `Path.iterdir` моком, который возвращает список объектов `Path` для файлов "file1.txt" и "file2.txt".
2.  Вызывает функцию `get_filenames` с путем к директории "/some/dir".
3.  Проверяет, что возвращаемый список имен файлов равен `["file1.txt", "file2.txt"]`.

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
```

**Описание**: Тестирует получение списка имен поддиректорий из директории.

**Как работает функция**:

1.  Использует `patch` для замены `Path.iterdir` моком, который возвращает список объектов `Path` для директорий "dir1" и "dir2".
2.  Вызывает функцию `get_directory_names` с путем к директории "/some/dir".
3.  Проверяет, что возвращаемый список имен директорий равен `["dir1", "dir2"]`.

**Примеры**:

```python
directories: list[str] = test_get_directory_names()
print(directories)