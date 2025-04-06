# Модуль для экспериментов с моделями машинного обучения для AliExpress

## Обзор

Модуль предназначен для экспериментов с моделями машинного обучения, такими как OpenAI и Google Gemini, для обработки данных, связанных с AliExpress. В частности, он предназначен для работы с заголовками продуктов и создания рекламных кампаний.

## Подробней

Модуль выполняет следующие основные задачи:

1.  **Поиск файлов с заголовками продуктов**: Рекурсивно ищет файлы с именами `product_titles.txt` в указанной директории на Google Drive.
2.  **Чтение системной инструкции**: Загружает системную инструкцию из файла `system_instruction.txt`, которая используется для настройки моделей OpenAI и Gemini.
3.  **Инициализация моделей**: Создает экземпляры моделей OpenAI и Gemini, передавая им системную инструкцию.
4.  **Обработка файлов и запросы к моделям**: Для каждого найденного файла с заголовками продуктов выполняет чтение содержимого, отправляет запросы к моделям OpenAI и Gemini, и обрабатывает полученные ответы.

Модуль использует `gs.path` для определения путей к файлам, `OpenAIModel` и `GoogleGenerativeAI` для взаимодействия с моделями машинного обучения, а также функции `recursively_get_filenames` и `read_text_file` для работы с файловой системой.

## Функции

### `recursively_get_filenames`

```python
from src.utils.file import recursively_get_filenames
def recursively_get_filenames(dir_path: str, file_pattern: str) -> list[str]:
    """
    Рекурсивно получает список имен файлов, соответствующих заданному шаблону, в указанной директории.

    Args:
        dir_path (str): Путь к директории для поиска файлов.
        file_pattern (str): Шаблон имени файла для поиска.

    Returns:
        list[str]: Список имен файлов, соответствующих заданному шаблону.

    Raises:
        - Отсутствуют явные исключения.

    Как работает функция:
        1. Функция начинает с указанной директории `dir_path`.
        2. Использует модуль `os` для рекурсивного обхода директории и всех ее поддиректорий.
        3. Для каждого файла проверяет, соответствует ли его имя заданному шаблону `file_pattern`.
        4. Если имя файла соответствует шаблону, добавляет его в список результатов.
        5. Возвращает список всех найденных файлов, соответствующих шаблону.

     A(Начало)
     |
     B(Обход директории) - C(Проверка соответствия шаблону)
     | Да
     D(Добавление в список)
     | Нет
     E(Завершение)
     
    Примеры:
        >>> recursively_get_filenames('/path/to/directory', 'example.txt')
        ['/path/to/directory/example.txt', '/path/to/directory/subdir/example.txt']
    """
    ...
```

### `read_text_file`

```python
from src.utils.file import read_text_file
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

### `csv2json_csv2dict`

```python
from src.utils.convertors import csv2json_csv2dict
def csv2json_csv2dict(
    csv_file_path: str,
    encoding: str = "utf-8",
    delimiter: str = ",",
    doublequote: bool = False,
    quotechar: str = '"',
    escapechar: str = None,
    skipinitialspace: bool = False,
) -> list[dict] | None:
    """
    Преобразует CSV-файл в JSON-формат (список словарей).

    Args:
        csv_file_path (str): Путь к CSV-файлу.
        encoding (str, optional): Кодировка файла. По умолчанию "utf-8".
        delimiter (str, optional): Разделитель полей. По умолчанию ",".
        doublequote (bool, optional): Обрабатывать двойные кавычки внутри полей. По умолчанию False.
        quotechar (str, optional): Символ кавычки. По умолчанию '"'.
        escapechar (str, optional): Символ экранирования. По умолчанию None.
        skipinitialspace (bool, optional): Игнорировать начальные пробелы после разделителя. По умолчанию False.

    Returns:
        list[dict] | None: Список словарей, представляющий данные из CSV-файла, или None в случае ошибки.

    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: Если возникает ошибка при чтении или обработке CSV-файла.

    Как работает функция:
        1. Открывает CSV-файл по указанному пути.
        2. Создает объект `csv.DictReader` для чтения данных в виде словарей.
        3. Читает каждую строку CSV-файла и преобразует ее в словарь.
        4. Добавляет каждый словарь в список результатов.
        5. Возвращает список словарей.
        6. В случае возникновения исключения, логирует ошибку и возвращает None.

     A(Начало)
     |
     B(Открытие файла)
     |
     C(Чтение CSV) - D(Преобразование в словарь)
     |
     E(Добавление в список)
     |
     F(Завершение)
     
    Примеры:
        >>> csv2json_csv2dict('data.csv')
        [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]
    """
    ...
```

### `OpenAIModel`

```python
from src.ai import OpenAIModel
class OpenAIModel:
    """
    Класс для взаимодействия с моделью OpenAI.

    Attributes:
        system_instruction (str): Инструкция для настройки поведения модели.

    Methods:
        ask(product_titles: str) -> str: Отправляет запрос в модель OpenAI и возвращает ответ.
    """
    ...
```

### `GoogleGenerativeAI`

```python
from src.ai import GoogleGenerativeAI
class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделью Google Gemini.

    Attributes:
        system_instruction (str): Инструкция для настройки поведения модели.

    Methods:
        ask(product_titles: str) -> str: Отправляет запрос в модель Gemini и возвращает ответ.
    """
    ...
```

## Переменные

-   `product_titles_files (list)`: Список файлов, содержащих заголовки продуктов, полученный с использованием функции `recursively_get_filenames`.
-   `system_instruction_path (Path)`: Путь к файлу, содержащему системную инструкцию для моделей OpenAI и Gemini.
-   `system_instruction (str)`: Системная инструкция, прочитанная из файла `system_instruction_path`.
-   `openai (OpenAIModel)`: Экземпляр класса `OpenAIModel`, используемый для взаимодействия с моделью OpenAI.
-   `gemini (GoogleGenerativeAI)`: Экземпляр класса `GoogleGenerativeAI`, используемый для взаимодействия с моделью Google Gemini.
-   `file (str)`: Переменная цикла, представляющая текущий файл с заголовками продуктов.
-   `product_titles (str)`: Содержимое файла с заголовками продуктов, прочитанное с использованием функции `read_text_file`.
-   `response_openai (str)`: Ответ, полученный от модели OpenAI на запрос с заголовками продуктов.
-   `response_gemini (str)`: Ответ, полученный от модели Gemini на запрос с заголовками продуктов.