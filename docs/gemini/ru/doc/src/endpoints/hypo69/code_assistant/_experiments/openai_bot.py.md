# Модуль для экспериментов с моделью AI OpenAI

## Обзор

Модуль предназначен для экспериментов с моделью OpenAI. Он обрабатывает исходный код или документацию, отправляет их в модель для анализа и получения ответов.

## Подробнее

Этот модуль является частью проекта `hypotez` и используется для автоматической генерации документации или анализа кода с использованием AI моделей OpenAI.
Он конфигурируется с помощью роли выполнения, которая определяет, какие действия следует предпринять (например, `doc_writer` для создания документации).
Основная цель модуля - упростить процесс документирования и анализа кода, позволяя разработчикам использовать возможности AI для автоматического создания необходимой документации.

## Функции

### `main`

```python
def main() -> None:
    """ Main function to process files and interact with the model.

    This function reads a comment file, iterates over specified files in the source directory,
    and sends the file content to a model for analysis. It then processes the model's response.
    """
```

**Назначение**: Основная функция для обработки файлов и взаимодействия с моделью.

**Как работает функция**:

1.  Устанавливает глобальную переменную `role` (роль) для определения текущей задачи (например, `doc_writer`).
2.  Если роль `doc_writer`, определяет имена файлов с комментариями и системными инструкциями для модели.
3.  Читает содержимое файлов с комментариями и системными инструкциями.
4.  Инициализирует объект `OpenAIModel` с системными инструкциями, именем модели и идентификатором ассистента.
5.  Перебирает файлы в указанной директории (`gs.path.src`) с использованием заданных паттернов (`*.py`, `README.MD`).
6.  Формирует контент для отправки в модель, включая комментарии, расположение файла и сам код.
7.  Получает ответ от модели, используя метод `ask`.
8.  Сохраняет полученный ответ в файл с помощью функции `save_response`.
9.  Обрабатывает возможные исключения и логирует ошибки.
10. Делает паузу в 20 секунд, чтобы избежать ограничений API.

**Внутренние функции**: Нет

**Пример**:
```python
from src.endpoints.hypo69.code_assistant._experiments.openai_bot import main

main()
```

### `save_response`

```python
def save_response(file_path: Path, response: str, from_model: str) -> None:
    """ Save the model's response to a markdown file with updated path based on role.

    Args:
        file_path (Path): The original file path being processed.
        response (str): The response from the model to be saved.
    """
```

**Назначение**: Сохраняет ответ модели в файл Markdown с обновленным путем на основе роли.

**Параметры**:

*   `file_path` (Path): Исходный путь к обрабатываемому файлу.
*   `response` (str): Ответ от модели, который необходимо сохранить.
*   `from_model` (str):  Название модели, от которой получен ответ.

**Как работает функция**:

1.  Определяет словарь `role_directories`, связывающий роли с директориями для сохранения файлов.
2.  Проверяет, присутствует ли текущая роль в словаре. Если нет, логирует ошибку и выходит из функции.
3.  Получает директорию, соответствующую текущей роли.
4.  Формирует новый путь для сохранения файла, заменяя часть пути `'src'` на директорию, соответствующую роли.
5.  Изменяет суффикс файла на `.md`.
6.  Создает родительские директории, если они не существуют.
7.  Сохраняет ответ модели в новый файл с кодировкой UTF-8.

**Примеры**:

```python
from pathlib import Path
from src.endpoints.hypo69.code_assistant._experiments.openai_bot import save_response

file_path = Path('src/example.py')
response = "This is a sample response from the model."
from_model = 'openai'
save_response(file_path, response, from_model)
```

### `yield_files_content`

```python
def yield_files_content(
    src_path: Path, patterns: list[str]
) -> Iterator[tuple[Path, str]]:
    """ Yield file content based on patterns from the source directory, excluding certain patterns and directories.

    Args:
        src_path (Path): The base directory to search for files.
        patterns (list[str]): List of file patterns to include (e.g., ['*.py', '*.txt']).

    Yields:
        Iterator[tuple[Path, str]]: A tuple of file path and its content as a string.
    """
```

**Назначение**: Генерирует содержимое файлов на основе заданных шаблонов из исходной директории, исключая определенные шаблоны и директории.

**Параметры**:

*   `src_path` (Path): Базовая директория для поиска файлов.
*   `patterns` (list[str]): Список шаблонов файлов для включения (например, `['*.py', '*.txt']`).

**Возвращает**:
Iterator[tuple[Path, str]]: Итератор, возвращающий кортеж из пути к файлу и его содержимого в виде строки.

**Как работает функция**:

1.  Определяет регулярные выражения для исключаемых файлов и директорий (содержащих круглые скобки, начинающихся с трех и более подчеркиваний).
2.  Определяет список исключаемых директорий (`.ipynb_checkpoints`, `_experiments`, `__pycache__`, `.git`, `.venv`).
3.  Перебирает шаблоны файлов и использует `rglob` для рекурсивного поиска файлов, соответствующих шаблону.
4.  Пропускает файлы, находящиеся в исключаемых директориях.
5.  Пропускает файлы, соответствующие исключаемым шаблонам.
6.  Читает содержимое файла с кодировкой UTF-8 и возвращает путь к файлу и его содержимое в виде кортежа.

**Примеры**:

```python
from pathlib import Path
from src.endpoints.hypo69.code_assistant._experiments.openai_bot import yield_files_content

src_path = Path('src')
patterns = ['*.py', 'README.md']

for file_path, content in yield_files_content(src_path, patterns):
    print(f"File: {file_path}")
    print(f"Content: {content[:100]}...")  # Вывод первых 100 символов