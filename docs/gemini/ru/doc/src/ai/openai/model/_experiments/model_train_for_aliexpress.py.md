# Модуль для экспериментов с моделями OpenAI для AliExpress
## Обзор

Модуль предназначен для экспериментов с моделями OpenAI и Google Gemini для обработки данных, связанных с AliExpress кампаниями. Он включает в себя чтение текстовых файлов с заголовками продуктов, использование моделей OpenAI и Gemini для обработки этих заголовков, и сохранение результатов.

## Подробней

Модуль предназначен для автоматизации задач, связанных с AliExpress кампаниями, используя возможности AI. Он загружает заголовки продуктов, передает их в модели OpenAI и Gemini, получает ответы и сохраняет их для дальнейшего использования. Расположение файла в структуре проекта указывает на его экспериментальный характер и использование для тестирования различных подходов к обработке данных.

## Функции

### `recursively_get_filenames`

```python
from src.utils.file import recursively_get_filenames

def recursively_get_filenames(dir_path: str, file_extension: str) -> list:
    """ Функция рекурсивно получает список файлов с указанным расширением из директории.
    Args:
        dir_path (str): Путь к директории.
        file_extension (str): Расширение файлов для поиска.

    Returns:
        list: Список полных путей к файлам с указанным расширением.

    Raises:
        OSError: Если директория не существует или нет прав доступа.

    Example:
        >>> from pathlib import Path
        >>> dir_path = Path('./')
        >>> file_extension = 'txt'
        >>> filenames = recursively_get_filenames(dir_path, file_extension)
    """
    ...
```

**Как работает функция**:

1. Функция принимает путь к директории `dir_path` и расширение файла `file_extension` в качестве аргументов.
2. Она рекурсивно обходит все поддиректории в указанной директории.
3. Для каждого файла проверяется, соответствует ли его расширение заданному.
4. Если расширение совпадает, полный путь к файлу добавляется в список результатов.
5. В конце функция возвращает список всех найденных файлов.

**Пример**:

```python
from pathlib import Path
from src.utils.file import recursively_get_filenames
import os

# Создадим временные файлы и директории для примера
os.makedirs('temp_dir/subdir', exist_ok=True)
Path('temp_dir/file1.txt').touch()
Path('temp_dir/file2.csv').touch()
Path('temp_dir/subdir/file3.txt').touch()

dir_path = 'temp_dir'
file_extension = 'txt'
filenames = recursively_get_filenames(dir_path, file_extension)
print(filenames)  # Вывод: ['temp_dir/file1.txt', 'temp_dir/subdir/file3.txt']

# Удалим временные файлы и директории
import shutil
shutil.rmtree('temp_dir')

```

### `read_text_file`

```python
from src.utils.file import read_text_file

def read_text_file(file_path: str, as_list: bool = False, extensions: Optional[List[str]] = None, chunk_size: int = 8192) -> Generator[str, None, None] | str | None:
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

**Как работает функция**:

1. Функция принимает путь к файлу `file_path`, флаг `as_list` (возвращать ли список строк), список расширений `extensions` и размер чанка `chunk_size`.
2. Она открывает файл в режиме чтения.
3. Если `as_list` равен `True`, функция возвращает генератор строк, читая файл построчно.
4. Если `as_list` равен `False`, функция читает весь файл целиком и возвращает его содержимое в виде строки.
5. В случае возникновения ошибки, функция возвращает `None`.

**Пример**:

```python
from pathlib import Path
from src.utils.file import read_text_file

# Создадим временный файл для примера
file_path = 'temp_file.txt'
with open(file_path, 'w') as f:
    f.write('Line 1\nLine 2\nLine 3')

# Пример чтения файла как одной строки
content = read_text_file(file_path)
print(f'Content as string: {content}')

# Пример чтения файла как списка строк
content_list = read_text_file(file_path, as_list=True)
print(f'Content as list: {list(content_list)}')

# Удалим временный файл
import os
os.remove(file_path)
```

### `csv2json_csv2dict`

```python
from src.utils.convertors import csv2json_csv2dict

def csv2json_csv2dict(csv_file_path: str) -> list[dict]:
    """Преобразует CSV файл в список словарей.

    Args:
        csv_file_path (str): Путь к CSV файлу.

    Returns:
        list[dict]: Список словарей, представляющих строки CSV файла.

    Raises:
        FileNotFoundError: Если CSV файл не найден.
        Exception: При возникновении других ошибок чтения и обработки CSV файла.

    Example:
        >>> data = csv2json_csv2dict('path/to/your/file.csv')
        >>> print(data)
        [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]
    """
    ...
```

**Как работает функция**:

1. Функция принимает путь к CSV файлу `csv_file_path`.
2. Она открывает CSV файл для чтения.
3. Читает CSV файл, используя `csv.DictReader`, который преобразует каждую строку CSV файла в словарь, где ключами являются заголовки столбцов.
4. Возвращает список словарей, где каждый словарь представляет строку из CSV файла.

**Пример**:

```python
import csv
import os
from src.utils.convertors import csv2json_csv2dict

# Создаем временный CSV файл
csv_data = "header1,header2\nvalue1,value2\nvalue3,value4"
csv_file_path = "temp_csv_file.csv"
with open(csv_file_path, "w") as csv_file:
    csv_file.write(csv_data)

# Преобразуем CSV файл в список словарей
data = csv2json_csv2dict(csv_file_path)
print(data)
# Ожидаемый вывод:
# [{'header1': 'value1', 'header2': 'value2'}, {'header1': 'value3', 'header2': 'value4'}]

# Удаляем временный CSV файл
os.remove(csv_file_path)
```

### `pprint`

```python
from src.utils.printer import pprint

def pprint(obj: any) -> None:
    """Печатает объект в удобочитаемом формате, используя json.dumps.

    Args:
        obj (any): Объект для печати. Может быть любым объектом, который можно сериализовать в JSON.

    Returns:
        None

    Raises:
        TypeError: Если объект не может быть сериализован в JSON.

    Example:
        >>> data = {'key1': 'value1', 'key2': 'value2'}
        >>> pprint(data)
        {
            "key1": "value1",
            "key2": "value2"
        }
    """
    ...
```

**Как работает функция**:

1. Функция принимает объект `obj` любого типа в качестве аргумента.
2. Она использует `json.dumps` для преобразования объекта в строку JSON. Параметр `indent=4` добавляет отступы для удобочитаемости.
3. Функция печатает полученную строку JSON в консоль.

**Пример**:

```python
from src.utils.printer import pprint

data = {'key1': 'value1', 'key2': 'value2'}
pprint(data)
# Ожидаемый вывод:
# {
#     "key1": "value1",
#     "key2": "value2"
# }
```

## Переменные

- `product_titles_files (list)`: Список файлов, содержащих заголовки продуктов. Заполняется путем рекурсивного поиска файлов с именем `product_titles.txt` в директории `gs.path.google_drive / 'aliexpress' / 'campaigns'`.
- `system_instruction_path (str)`: Путь к файлу с системной инструкцией для моделей OpenAI и Gemini. Определен как `gs.path.src / 'ai' / 'prompts' / 'aliexpress_campaign' / 'system_instruction.txt'`.
- `system_instruction (str)`: Содержимое файла с системной инструкцией, прочитанное с использованием функции `read_text_file`.
- `openai (OpenAIModel)`: Экземпляр класса `OpenAIModel`, инициализированный с использованием системной инструкции.
- `gemini (GoogleGenerativeAI)`: Экземпляр класса `GoogleGenerativeAI`, инициализированный с использованием той же системной инструкции.

## Цикл обработки файлов

Основная часть модуля представляет собой цикл, который проходит по списку файлов с заголовками продуктов:

```python
for file in product_titles_files:
    ...
    product_titles = read_text_file(file)
    response_openai = openai.ask(product_titles)
    response_gemini = gemini.ask(product_titles)
    ...
```

1. **Итерация по файлам**: Цикл `for file in product_titles_files:` перебирает каждый файл, содержащий заголовки продуктов.
2. **Чтение заголовков продуктов**: Внутри цикла вызывается функция `read_text_file(file)` для чтения содержимого текущего файла. Результат сохраняется в переменной `product_titles`.
3. **Обращение к OpenAI**: Метод `openai.ask(product_titles)` отправляет заголовки продуктов в модель OpenAI для обработки. Ответ сохраняется в переменной `response_openai`.
4. **Обращение к Gemini**: Аналогично, метод `gemini.ask(product_titles)` отправляет заголовки продуктов в модель Gemini для обработки. Ответ сохраняется в переменной `response_gemini`.
5. **Дальнейшая обработка**: Многоточие `...` указывает на то, что в этой части кода должна быть логика для обработки ответов от моделей OpenAI и Gemini.

## OpenAIModel

```python
from src.ai import OpenAIModel

class OpenAIModel:
    """
    Класс для взаимодействия с OpenAI API.
    Attributes:
        system_instruction (str): Инструкция для системы, задающая контекст и цели взаимодействия.

    Methods:
        ask(prompt: str) -> str: Отправляет запрос в OpenAI API и возвращает ответ.
    """

    def __init__(self, system_instruction: str):
        """
        Инициализирует объект OpenAIModel.
        Args:
            system_instruction (str): Инструкция для системы.
        """
        ...

    def ask(self, prompt: str) -> str:
        """
        Отправляет запрос в OpenAI API и возвращает ответ.
        Args:
            prompt (str): Текст запроса.
        Returns:
            str: Ответ от OpenAI API.
        """
        ...
```

## GoogleGenerativeAI

```python
from src.ai import GoogleGenerativeAI

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с Google Generative AI API.
    Attributes:
        system_instruction (str): Инструкция для системы, задающая контекст и цели взаимодействия.

    Methods:
        ask(prompt: str) -> str: Отправляет запрос в Google Generative AI API и возвращает ответ.
    """

    def __init__(self, system_instruction: str):
        """
        Инициализирует объект GoogleGenerativeAI.
        Args:
            system_instruction (str): Инструкция для системы.
        """
        ...

    def ask(self, prompt: str) -> str:
        """
        Отправляет запрос в Google Generative AI API и возвращает ответ.
        Args:
            prompt (str): Текст запроса.
        Returns:
            str: Ответ от Google Generative AI API.
        """
        ...