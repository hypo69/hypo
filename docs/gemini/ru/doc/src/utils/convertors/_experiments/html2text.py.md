# Модуль `html2text.py`

## Обзор

Модуль `html2text.py` предназначен для конвертации HTML-контента в текстовый формат. Он содержит функции и методы, позволяющие извлекать текст из HTML-файлов и сохранять его в текстовом виде.

## Подробней

Этот модуль является частью пакета `src.utils.convertors._experiments` и используется для экспериментов с конвертацией HTML в текст. Он может быть полезен для обработки HTML-контента, извлечения информации и сохранения ее в более удобном формате для дальнейшего анализа или обработки. В данном коде происходит чтение HTML-файла, конвертация его в текст и сохранение результата в текстовый файл.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `read_text_file`

```python
def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Считывает содержимое файла (или файлов из каталога) с использованием генератора для экономии памяти.

    :param file_path: Путь к файлу или каталогу.
    :param as_list: Если `True`, возвращает генератор строк.
    :param extensions: Список расширений файлов для чтения из каталога.
    :param chunk_size: Размер чанков для чтения файла в байтах.

    :returns: Генератор строк, объединенная строка или `None` в случае ошибки.

    :raises Exception: Если возникает ошибка при чтении файла.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
```

**Описание**: Функция `read_text_file` считывает содержимое текстового файла.

**Параметры**:
- `file_path` (str | Path): Путь к файлу, который нужно прочитать.
- `as_list` (bool, optional): Если установлено значение `True`, функция возвращает содержимое файла в виде списка строк. По умолчанию `False`.
- `extensions` (Optional[list[str]], optional): Список расширений файлов для чтения. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанков для чтения файла. По умолчанию `8192`.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла.

**Примеры**:
```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
   print(f'File content: {content[:100]}...')
```

### `save_text_file`

```python
def save_text_file(text: str, file_path: str | Path, encoding: str = 'utf-8') -> bool:
    """
    Сохраняет текст в файл.

    Args:
        text (str): Текст для сохранения.
        file_path (str | Path): Путь к файлу для сохранения текста.
        encoding (str, optional): Кодировка файла. По умолчанию 'utf-8'.

    Returns:
        bool: True, если сохранение прошло успешно, False в случае ошибки.

    Raises:
        OSError: Если возникает ошибка ввода-вывода при сохранении файла.

    Example:
        >>> file_path = 'output.txt'
        >>> text = 'Hello, world!'
        >>> save_text_file(text, file_path)
        True
    """
```

**Описание**: Функция `save_text_file` сохраняет переданный текст в указанный файл.

**Параметры**:
- `text` (str): Текст, который необходимо сохранить в файл.
- `file_path` (str | Path): Путь к файлу, в который нужно сохранить текст.
- `encoding` (str, optional): Кодировка файла. По умолчанию используется 'utf-8'.

**Возвращает**:
- `bool`: `True`, если сохранение прошло успешно, `False` в случае ошибки.

**Вызывает исключения**:
- `OSError`: Если возникает ошибка ввода-вывода при сохранении файла.

**Примеры**:
```python
file_path = 'output.txt'
text = 'Hello, world!'
save_text_file(text, file_path)
```

### `html2text`

```python
def html2text(html: str, baseurl: str = '') -> str:
    """
    Конвертирует HTML в текст.

    Args:
        html (str): HTML для конвертации.
        baseurl (str, optional): Базовый URL. По умолчанию ''.

    Returns:
        str: Текст, извлеченный из HTML.

    Raises:
        Exception: Если возникает ошибка при конвертации HTML в текст.

    Example:
        >>> html_content = '<p>Hello, world!</p>'
        >>> text_content = html2text(html_content)
        >>> print(text_content)
        Hello, world!
    """
```

**Описание**: Функция `html2text` конвертирует HTML-код в текстовый формат.

**Параметры**:
- `html` (str): HTML-код, который необходимо конвертировать в текст.
- `baseurl` (str, optional): Базовый URL для разрешения относительных ссылок. По умолчанию ''.

**Возвращает**:
- `str`: Текст, извлеченный из HTML-кода.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при конвертации HTML в текст.

**Примеры**:
```python
html_content = '<p>Hello, world!</p>'
text_content = html2text(html_content)
print(text_content)
```