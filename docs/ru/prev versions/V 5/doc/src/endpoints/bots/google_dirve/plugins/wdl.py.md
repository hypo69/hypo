# Модуль для загрузки файлов с использованием wget

## Обзор

Этот модуль содержит функцию `wget_dl`, которая загружает файлы из интернета с использованием утилиты `wget`. Функция обрабатывает исключения и возвращает имя загруженного файла или сообщение об ошибке.

## Подробней

Модуль `wdl.py` предоставляет простой интерфейс для загрузки файлов по URL-адресу с использованием команды `wget`. Он предназначен для использования в тех случаях, когда необходимо загрузить файл из внешнего источника в рамках работы других модулей или плагинов.

## Функции

### `wget_dl`

```python
def wget_dl(url: str) -> str | tuple[str, str]:
    """
    Загружает файл с использованием wget.

    Args:
        url (str): URL-адрес файла для загрузки.

    Returns:
        str | tuple[str, str]: Имя загруженного файла в случае успеха, или кортеж ("error", filename) в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при выполнении команды wget.

    Example:
        >>> wget_dl('https://example.com/file.txt')
        Downloading Started
        Downloading Complete file.txt
        'file.txt'

        >>> wget_dl('https://example.com/nonexistent_file.txt')
        Downloading Started
        DOWNLAOD ERROR : ...
        ('error', 'nonexistent_file.txt')
    """
```

**Как работает функция**:
1.  Функция принимает URL-адрес файла для загрузки в качестве аргумента.
2.  Выводит сообщение "Downloading Started" в консоль.
3.  Извлекает имя файла из URL-адреса с помощью `os.path.basename(url)`.
4.  Выполняет команду `wget` с использованием `subprocess.check_output` для загрузки файла.
    *   `'--output-document\' \'{}\' \'{}\' '.format(filename , url)`:  Формирует команду `wget` для загрузки файла по указанному URL-адресу (`url`) и сохранения его под именем `filename`. Опция `--output-document` указывает имя файла, в который будет сохранено содержимое загруженного URL.
5.  В случае успешной загрузки выводит сообщение "Downloading Complete" и имя файла в консоль.
6.  Возвращает имя загруженного файла.
7.  В случае возникновения ошибки выводит сообщение об ошибке в консоль.
8.  Возвращает кортеж `("error", filename)`, где `filename` - имя файла, который пытались загрузить.

**Параметры**:

*   `url` (str): URL-адрес файла для загрузки.

**Возвращает**:

*   `str | tuple[str, str]`: Имя загруженного файла в случае успеха, или кортеж ("error", filename) в случае ошибки.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при выполнении команды `wget`.

**Примеры**:

```python
>>> wget_dl('https://example.com/file.txt')
Downloading Started
Downloading Complete file.txt
'file.txt'

>>> wget_dl('https://example.com/nonexistent_file.txt')
Downloading Started
DOWNLAOD ERROR : ...
('error', 'nonexistent_file.txt')
```