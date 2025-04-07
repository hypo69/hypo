# Модуль html2text

## Обзор

Модуль `html2text.py` предназначен для преобразования HTML-контента в текстовый формат. Он использует функции из других модулей проекта для чтения HTML-файлов, конвертации их в текст и сохранения результата.

## Подробней

Этот модуль является частью подсистемы конвертации форматов в проекте `hypotez`. Он предоставляет возможность извлекать текстовое содержимое из HTML-страниц, что может быть полезно для дальнейшей обработки, анализа или индексации данных. Модуль читает HTML-файл, преобразует его в текст и сохраняет результат в текстовый файл.

## Функции

### `read_text_file`

```python
def read_text_file(file_path: str | Path, as_list: bool = False, extensions: Optional[List[str]] = None, chunk_size: int = 8192) -> Generator[str, None, None] | str | None:
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

**Назначение**: Считывает содержимое текстового файла по указанному пути.

**Параметры**:

-   `file_path` (str | Path): Путь к файлу, который нужно прочитать. Может быть строкой или объектом `Path`.
-   `as_list` (bool, optional): Если установлено в `True`, возвращает содержимое файла в виде списка строк. По умолчанию `False`.
-   `extensions` (Optional[List[str]], optional): Список расширений файлов для чтения, если `file_path` указывает на директорию. По умолчанию `None`.
-   `chunk_size` (int, optional): Размер чанка в байтах для чтения файла. По умолчанию `8192`.

**Возвращает**:

-   `Generator[str, None, None] | str | None`: Генератор строк, если `as_list` равен `True`, иначе – строка с содержимым файла. Возвращает `None` в случае ошибки.

**Вызывает исключения**:

-   `Exception`: Если возникает ошибка при чтении файла.

**Как работает функция**:

1.  Функция определяет, является ли `file_path` файлом или директорией.
2.  Если `file_path` - это файл, функция открывает файл и читает его содержимое.
3.  Если `as_list` равно `True`, функция возвращает генератор строк.
4.  Если `as_list` равно `False`, функция возвращает строку с содержимым файла.
5.  Если `file_path` - это директория, функция итерируется по всем файлам в директории с указанными расширениями и читает их содержимое.

**Примеры**:

```python
from pathlib import Path
# Чтение файла как строки
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')

# Чтение файла как списка строк
file_path = Path('example.txt')
content = read_text_file(file_path, as_list=True)
if content:
    for line in content:
        print(line)
        break
```

### `html2text`

```python
def html2text(html: str, baseurl: str = '') -> str:
    """
    Конвертирует HTML в текст, удаляя HTML-теги и преобразуя HTML-сущности.

    Args:
        html (str): HTML-контент для конвертации.
        baseurl (str, optional): Базовый URL для разрешения относительных ссылок. По умолчанию ''.

    Returns:
        str: Текстовое представление HTML-контента.

    Raises:
        Ошибка преобразования HTML в текст.

    Example:
        >>> html_content = '<p>Hello, <b>world!</b></p>'
        >>> text_content = html2text(html_content)
        >>> print(text_content)
        Hello, world!
    """
    ...
```

**Назначение**: Преобразует HTML-код в текст, удаляя HTML-теги и преобразуя HTML-сущности.

**Параметры**:

-   `html` (str): Строка, содержащая HTML-код, который необходимо преобразовать.
-   `baseurl` (str, optional): Базовый URL для разрешения относительных ссылок. По умолчанию пустая строка.

**Возвращает**:

-   `str`: Текстовое представление HTML-кода.

**Вызывает исключения**:

-   `Ошибка преобразования HTML в текст`.

**Как работает функция**:

1.  Функция принимает HTML-код в виде строки.
2.  Удаляет все HTML-теги из входной строки.
3.  Преобразует HTML-сущности (например, `&nbsp;`) в соответствующие символы.
4.  Возвращает текстовое представление HTML-кода.

**Примеры**:

```python
html_content = '<p>Hello, <b>world!</b></p>'
text_content = html2text(html_content)
print(text_content)

html_content = '<a href="/about">About Us</a>'
text_content = html2text(html_content, baseurl='https://example.com')
print(text_content)
```

### `html2text_file`

```python
def html2text_file(file_path: str, baseurl: str = '') -> str:
    """
    Конвертирует HTML-файл в текст, используя `html2text`.

    Args:
        file_path (str): Путь к HTML-файлу.
        baseurl (str, optional): Базовый URL для разрешения относительных ссылок. По умолчанию ''.

    Returns:
        str: Текстовое представление HTML-файла.

    Raises:
        Ошибка при чтении или преобразовании HTML-файла.

    Example:
        >>> file_path = 'example.html'
        >>> text_content = html2text_file(file_path)
        >>> print(text_content)
        Текст из HTML-файла.
    """
    ...
```

**Назначение**: Преобразует HTML-файл в текст, используя функцию `html2text`.

**Параметры**:

-   `file_path` (str): Путь к HTML-файлу, который необходимо преобразовать.
-   `baseurl` (str, optional): Базовый URL для разрешения относительных ссылок. По умолчанию пустая строка.

**Возвращает**:

-   `str`: Текстовое представление HTML-файла.

**Вызывает исключения**:

-   `Ошибка при чтении или преобразовании HTML-файла`.

**Как работает функция**:

1.  Функция принимает путь к HTML-файлу.
2.  Читает содержимое HTML-файла.
3.  Вызывает функцию `html2text` для преобразования HTML-кода в текст.
4.  Возвращает текстовое представление HTML-файла.

**Примеры**:

```python
file_path = 'example.html'
text_content = html2text_file(file_path)
print(text_content)
```

### `save_text_file`

```python
def save_text_file(text: str, file_path: str) -> None:
    """
    Сохраняет текст в файл.

    Args:
        text (str): Текст для сохранения.
        file_path (str): Путь к файлу для сохранения текста.

    Raises:
        Ошибка при сохранении текста в файл.

    Example:
        >>> text = "Hello, world!"
        >>> file_path = "output.txt"
        >>> save_text_file(text, file_path)
    """
    ...
```

**Назначение**: Сохраняет переданный текст в файл по указанному пути.

**Параметры**:

-   `text` (str): Текст, который необходимо сохранить в файл.
-   `file_path` (str): Путь к файлу, в который нужно сохранить текст.

**Возвращает**:

-   `None`: Функция ничего не возвращает.

**Вызывает исключения**:

-   `Ошибка при сохранении текста в файл`.

**Как работает функция**:

1.  Функция принимает текст и путь к файлу.
2.  Открывает файл для записи.
3.  Записывает переданный текст в файл.
4.  Закрывает файл.

**Примеры**:

```python
text = "Hello, world!"
file_path = "output.txt"
save_text_file(text, file_path)
```

## Как работает модуль

1.  Импортируются необходимые модули и функции: `header`, `gs`, `html2text`, `html2text_file`, `read_text_file`, `save_text_file`.
2.  Читается HTML-файл `index.html` из директории `gs.path.google_drive / 'html2text'`.
3.  HTML-контент преобразуется в текст с помощью функции `html2text`.
4.  Полученный текст сохраняется в файл `index.txt` в той же директории.

## ASCII flowchart

```
A[Чтение HTML-файла]
|
B[Преобразование HTML в текст]
|
C[Сохранение текста в файл]
```

## Переменные

-   `html`: Содержит HTML-код, прочитанный из файла `index.html`.
-   `text_from_html`: Содержит текст, полученный после преобразования HTML-кода.