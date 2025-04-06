# Модуль `html2text`

## Обзор

Модуль содержит экспериментальные функции для конвертации HTML-контента в текстовый формат. Включает в себя функциональность чтения HTML-файлов, конвертации их в текст и сохранения полученного текста в файл.

## Подробней

Этот модуль предназначен для извлечения текстового содержимого из HTML-документов. Он использует функции `html2text` и `html2text_file` для конвертации HTML в текст, а также функции `read_text_file` и `save_text_file` для чтения и записи файлов.
Модуль `html2text` является частью пакета `src.utils.convertors` и предназначен для работы с преобразованием данных.

## Функции

### `html2text`

```python
def html2text(html: str) -> str:
    """
    Конвертирует HTML-контент в текстовый формат.

    Args:
        html (str): HTML-контент для конвертации.

    Returns:
        str: Текстовое представление HTML-контента.

    Raises:
        Exception: Если возникает ошибка при конвертации HTML в текст.

    Example:
        >>> html_content = '<p>Hello, world!</p>'
        >>> text_content = html2text(html_content)
        >>> print(text_content)
        Hello, world!
    """
    ...
```

**Назначение**: Конвертирует HTML-код в его текстовое представление.

**Параметры**:
- `html` (str): HTML-код, который необходимо преобразовать в текст.

**Возвращает**:
- `str`: Текстовое представление переданного HTML-кода.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при конвертации HTML в текст.

**Как работает функция**:
1. Функция принимает HTML-код в качестве входных данных.
2. Затем, функция использует модуль `html2text` из пакета `src.utils.convertors` для преобразования HTML в текст.
3. Возвращает текстовое представление HTML.

**ASCII Flowchart**:

```
HTML-код
  ↓
Преобразование в текст (html2text)
  ↓
Текстовое представление
```

**Примеры**:
```python
from src.utils.convertors import html2text
html_content = '<p>Пример текста <b>с форматированием</b>.</p>'
text_content = html2text(html_content)
print(text_content)
# Вывод: Пример текста с форматированием.
```

### `html2text_file`

```python
def html2text_file(html_file: str) -> str:
    """
    Конвертирует HTML-файл в текстовый формат.

    Args:
        html_file (str): Путь к HTML-файлу.

    Returns:
        str: Текстовое представление HTML-файла.

    Raises:
        Exception: Если возникает ошибка при конвертации HTML-файла в текст.

    Example:
        >>> text_content = html2text_file('example.html')
        >>> print(text_content)
        Example text content from HTML file.
    """
    ...
```

**Назначение**: Конвертирует содержимое HTML-файла в текстовый формат.

**Параметры**:
- `html_file` (str): Путь к HTML-файлу, который необходимо преобразовать в текст.

**Возвращает**:
- `str`: Текстовое представление содержимого HTML-файла.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при конвертации HTML-файла в текст.

**Как работает функция**:
1. Функция принимает путь к HTML-файлу в качестве входных данных.
2. Затем функция использует модуль `html2text_file` из пакета `src.utils.convertors` для преобразования HTML-файла в текст.
3. Возвращает текстовое представление HTML-файла.

**ASCII Flowchart**:

```
Путь к HTML-файлу
  ↓
Преобразование в текст (html2text_file)
  ↓
Текстовое представление
```

**Примеры**:
```python
from src.utils.convertors import html2text_file
text_content = html2text_file('example.html')
print(text_content)
# Вывод: Example text content from HTML file.
```

## Функции

### `read_text_file`

```python
from typing import Generator, Optional, List
from pathlib import Path


def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[List[str]] = None,
    chunk_size: int = 8192,
) -> Generator[str, None, None] | str | None:
    """
    Считывает содержимое файла (или файлов из каталога) с использованием генератора для экономии памяти.

    Args:
        file_path (str | Path): Путь к файлу или каталогу.
        as_list (bool): Если `True`, возвращает генератор строк.
        extensions (Optional[List[str]]): Список расширений файлов для чтения из каталога.
        chunk_size (int): Размер чанков для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или `None` в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при чтении файла.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
    ...
```

**Назначение**: Считывает содержимое текстового файла (или файлов из каталога) с использованием генератора для экономии памяти.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или каталогу.
- `as_list` (bool): Если `True`, возвращает генератор строк.
- `extensions` (Optional[List[str]]): Список расширений файлов для чтения из каталога.
- `chunk_size` (int): Размер чанков для чтения файла в байтах.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла.

**Как работает функция**:
1. Функция принимает путь к файлу (или каталогу) в качестве входных данных.
2. В зависимости от аргумента `as_list`, функция либо возвращает генератор строк, либо объединенную строку.
3. Если `file_path` указывает на каталог и указаны расширения, функция считывает файлы с указанными расширениями.
4. Чтение файла происходит чанками для экономии памяти.
5. Возвращает генератор строк, объединенную строку или `None` в случае ошибки.

**ASCII Flowchart**:

```
Путь к файлу/каталогу
  ↓
Проверка: файл или каталог?
  ↓
Если файл: Чтение файла чанками
  ↓
Если каталог: Поиск файлов с указанными расширениями
  ↓
Возврат: генератор строк или объединенная строка
```

**Примеры**:
```python
from pathlib import Path
from src.utils.file import read_text_file

file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
# Вывод: File content: Example text...
```

### `save_text_file`

```python
def save_text_file(text: str, file_path: str | Path) -> None:
    """
    Сохраняет текст в файл.

    Args:
        text (str): Текст для сохранения.
        file_path (str | Path): Путь к файлу для сохранения текста.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при сохранении текста в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> save_text_file('Пример текста', file_path)
    """
    ...
```

**Назначение**: Сохраняет текст в файл.

**Параметры**:
- `text` (str): Текст, который необходимо сохранить в файл.
- `file_path` (str | Path): Путь к файлу, в который необходимо сохранить текст.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при сохранении текста в файл.

**Как работает функция**:
1. Функция принимает текст и путь к файлу в качестве входных данных.
2. Функция сохраняет переданный текст в указанный файл.

**ASCII Flowchart**:

```
Текст и путь к файлу
  ↓
Сохранение текста в файл
```

**Примеры**:
```python
from pathlib import Path
from src.utils.file import save_text_file

file_path = Path('example.txt')
save_text_file('Пример текста', file_path)
```

## Использование

В модуле происходит чтение HTML-файла, конвертация его в текст и сохранение полученного текста в файл:

```python
import header
from src import gs
from src.utils.convertors import html2text, html2text_file
from src.utils.file import read_text_file, save_text_file

html = read_text_file(gs.path.google_drive / 'html2text' / 'index.html')
text_from_html = html2text(html)
save_text_file(text_from_html, gs.path.google_drive / 'html2text' / 'index.txt')
...
```

Здесь, сначала читается HTML-файл `index.html` из директории `html2text` в Google Drive. Затем, содержимое этого файла конвертируется в текст с использованием функции `html2text`. Полученный текст сохраняется в файл `index.txt` в той же директории.

## Переменные

- `html`: Содержит HTML-код, прочитанный из файла `index.html`.
- `text_from_html`: Содержит текстовое представление HTML-кода после конвертации.