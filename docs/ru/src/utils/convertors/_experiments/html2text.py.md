# Модуль `html2text`

## Обзор

Модуль `html2text` предназначен для конвертации HTML-контента в текстовый формат. Он использует сторонние библиотеки и утилиты для извлечения текста из HTML-файлов и сохранения его в текстовом виде. Этот модуль является частью экспериментов в проекте `hypotez`.

## Подробней

Модуль предназначен для преобразования HTML-файлов в текст, что может быть полезно для извлечения информации из веб-страниц или документов HTML для дальнейшей обработки или анализа. Он использует функции `html2text` и `html2text_file` из модуля `src.utils.convertors` для выполнения преобразования. Результат сохраняется в текстовом файле.

## Функции

### `read_text_file`

```python
def read_text_file(file_path: str | Path, as_list: bool = False, extensions: Optional[list[str]] = None, chunk_size: int = 8192) -> Generator[str, None, None] | str | None:
    """ This if example function
    Args:
        file_path (str): Описание параметра `file_path`.
        as_list (bool): Описание параметра `as_list`.
        extensions (Optional[list[str]], optional): Описание параметра `extensions`. По умолчанию None.
        chunk_size (int): Описание параметра `chunk_size`.
    Returns:
        Generator[str, None, None] | str | None: Описание возвращаемого значения. Возвращает `True` или `False`.

     Raises:
          Ошибка выполнение

     Example:
         Примеры вызовов

    """
    # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**:
Чтение текстового файла.

**Как работает функция**:
Функция `read_text_file` считывает содержимое текстового файла по указанному пути. Она может возвращать содержимое в виде генератора строк (если `as_list=True`) или в виде одной строки.

**Параметры**:
- `file_path` (str | Path): Путь к файлу, который нужно прочитать.
- `as_list` (bool, optional): Если `True`, функция возвращает генератор строк. По умолчанию `False`.
- `extensions` (Optional[list[str]], optional): Список расширений файлов для чтения из каталога. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанков для чтения файла в байтах. По умолчанию `8192`.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

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
    """ This if example function
    Args:
        text (str): Описание параметра `text`.
        file_path (str): Описание параметра `file_path`.
        encoding (str): Описание параметра `encoding`.
    Returns:
        bool: Описание возвращаемого значения. Возвращает `True` или `False`.

     Raises:
          Ошибка выполнение

     Example:
         Примеры вызовов

    """
    # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**:
Сохранение текстового файла.

**Как работает функция**:
Функция `save_text_file` сохраняет предоставленный текстовый контент в файл по указанному пути.

**Параметры**:
- `text` (str): Текст, который нужно сохранить в файл.
- `file_path` (str | Path): Путь к файлу, в который нужно сохранить текст.
- `encoding` (str, optional): Кодировка файла. По умолчанию `'utf-8'`.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, иначе `False`.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
text = 'Example text'
save_text_file(text, file_path)
```

### `html2text`

```python
def html2text(html: str, bodywidth: int = 0,  override: Optional[dict] = None) -> str:
    """ This if example function
    Args:
        html (str): Описание параметра `html`.
        bodywidth (int): Описание параметра `bodywidth`.
        override (Optional[dict], optional): Описание параметра `override`. По умолчанию None.
    Returns:
        str: Описание возвращаемого значения. Возвращает `True` или `False`.

     Raises:
          Ошибка выполнение

     Example:
         Примеры вызовов

    """
    # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**:
Конвертация HTML в текст.

**Как работает функция**:
Функция `html2text` преобразует HTML-контент в текстовый формат, удаляя HTML-теги и форматирование.

**Параметры**:
- `html` (str): HTML-контент для преобразования.
- `bodywidth` (int, optional): Ширина текста. По умолчанию `0`.
- `override` (Optional[dict], optional): Переопределение параметров. По умолчанию `None`.

**Возвращает**:
- `str`: Текстовое представление HTML-контента.

**Примеры**:

```python
html = '<p>Example text</p>'
text = html2text(html)
print(text)
```

### `html2text_file`

```python
def html2text_file(file_path: str | Path, bodywidth: int = 0,  override: Optional[dict] = None) -> str:
    """ This if example function
    Args:
        file_path (str): Описание параметра `file_path`.
        bodywidth (int): Описание параметра `bodywidth`.
        override (Optional[dict], optional): Описание параметра `override`. По умолчанию None.
    Returns:
        str: Описание возвращаемого значения. Возвращает `True` или `False`.

     Raises:
          Ошибка выполнение

     Example:
         Примеры вызовов

    """
    # Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**:
Конвертация HTML-файла в текст.

**Как работает функция**:
Функция `html2text_file` считывает HTML-контент из файла по указанному пути и преобразует его в текстовый формат.

**Параметры**:
- `file_path` (str | Path): Путь к HTML-файлу.
- `bodywidth` (int, optional): Ширина текста. По умолчанию `0`.
- `override` (Optional[dict], optional): Переопределение параметров. По умолчанию `None`.

**Возвращает**:
- `str`: Текстовое представление HTML-контента из файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.html')
text = html2text_file(file_path)
print(text)
```

## Переменные

- `html`: HTML-контент, прочитанный из файла `index.html`.
- `text_from_html`: Текст, извлеченный из HTML-контента с использованием функции `html2text`.