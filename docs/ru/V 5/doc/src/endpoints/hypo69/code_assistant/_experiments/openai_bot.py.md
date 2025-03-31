# Модуль для экспериментов с OpenAI

## Обзор

Модуль `openai_bot.py` предназначен для экспериментов с моделью AI OpenAI. Он обрабатывает исходный код или документацию, отправляет их в модель для анализа и получения ответов.

## Подробнее

Основная задача модуля - автоматическая генерация документации или выполнение других задач обработки текста с использованием OpenAI GPT-4. Модуль использует роль выполнения, установленную внутри кода, для взаимодействия с моделью. Входные данные для модели включают комментарии и код/документацию, которые передаются в модель для обработки. Ответ модели сохраняется в файл с расширением `.md` в зависимости от роли.

## Функции

### `main`

```python
def main() -> None:
    """ Main function to process files and interact with the model.

    This function reads a comment file, iterates over specified files in the source directory,
    and sends the file content to a model for analysis. It then processes the model's response.
    """
    global role

    role = role if role else 'doc_writer'

    if role == 'doc_writer':
        comment_for_model_about_piece_of_code = 'doc_writer.md'
        system_instruction: str = 'create_documentation.md'
```

**Как работает функция**:

Функция `main` является основной точкой входа для обработки файлов и взаимодействия с моделью OpenAI. Она выполняет следующие шаги:

1.  Определяет роль выполнения (по умолчанию `doc_writer`).
2.  Для роли `doc_writer` устанавливает имена файлов с комментариями для модели и системными инструкциями.
3.  Считывает содержимое файлов с комментариями и системными инструкциями.
4.  Инициализирует модель OpenAI с системными инструкциями, именем модели и ID ассистента.
5.  Итерирует по файлам в указанной директории, используя функцию `yield_files_content`.
6.  Формирует входные данные для модели, включая комментарии, расположение файла и содержимое файла.
7.  Отправляет запрос в модель OpenAI и получает ответ.
8.  Сохраняет ответ модели в файл с помощью функции `save_response`.
9.  Обрабатывает возможные исключения и логирует ошибки.
10. Приостанавливает выполнение на 20 секунд для предотвращения превышения лимитов API.

**Параметры**:

*   Нет параметров.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `Exception`: В случае ошибки при взаимодействии с моделью OpenAI или при обработке файлов.

**Примеры**:

```python
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
    global role

    # Словарь, ассоциирующий роли с директориями
    role_directories = {
        'doc_writer': f'docs/{from_model}/raw_rst_from_ai',
    }

    # Проверка наличия роли в словаре
    if role not in role_directories:
        logger.error(f"Неизвестная роль: {role}. Файл не будет сохранен.")
        return

    # Получаем директорию, соответствующую роли
    role_directory = role_directories[role]

    # Формируем новый путь с учетом роли
    export_file_path = file_path.parts
    new_parts = []

    for part in export_file_path:
        if part == 'src':
            new_parts.append(role_directory)
        else:
            new_parts.append(part)

    # Сформировать новый путь с замененной частью
    export_file_path = Path(*new_parts)

    # Изменить суффикс файла на .md
    export_file_path = export_file_path.with_suffix(".md")

    # Убедиться, что директория существует
    export_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Сохранить ответ в новый файл
    export_file_path.write_text(response, encoding="utf-8")
    print(f"Response saved to: {export_file_path}")
```

**Как работает функция**:

Функция `save_response` сохраняет ответ модели в файл с расширением `.md`. Она выполняет следующие шаги:

1.  Определяет директорию для сохранения файла на основе текущей роли.
2.  Формирует новый путь к файлу, заменяя часть пути `'src'` на директорию, соответствующую роли.
3.  Изменяет суффикс файла на `.md`.
4.  Создает директорию для сохранения файла, если она не существует.
5.  Сохраняет ответ модели в файл с использованием кодировки UTF-8.

**Параметры**:

*   `file_path` (Path): Исходный путь к файлу, который был обработан.
*   `response` (str): Ответ от модели, который нужно сохранить.
*   `from_model` (str): Указывает, от какой модели получен ответ (например, 'openai').

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `OSError`: В случае ошибки при создании директории или записи файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('src/example.py')
response = 'This is a sample response from the model.'
save_response(file_path, response, 'openai')
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

    # Регулярные выражения для исключаемых файлов и директорий
    exclude_file_patterns = [
        re.compile(r'.*\\(.*\\).*\'),  # Файлы и директории, содержащие круглые скобки
        re.compile(r'___+.*\'),      # Файлы или директории, начинающиеся с трех и более подчеркиваний
    ]

    # Список служебных директорий, которые необходимо исключить
    exclude_dirs = {'.ipynb_checkpoints', '_experiments', '__pycache__', '.git', '.venv'}

    for pattern in patterns:
        for file_path in src_path.rglob(pattern):
            # Пропустить файлы, которые находятся в исключаемых директориях
            if any(exclude_dir in file_path.parts for exclude_dir in exclude_dirs):
                continue

            # Пропустить файлы, соответствующие исключаемым паттернам
            if any(exclude.match(str(file_path)) for exclude in exclude_file_patterns):
                continue

            # Чтение содержимого файла
            content = file_path.read_text(encoding="utf-8")
            yield file_path, content
```

**Как работает функция**:

Функция `yield_files_content` является генератором, который обходит файлы в указанной директории и возвращает их содержимое. Она выполняет следующие шаги:

1.  Определяет регулярные выражения для исключения файлов и директорий, содержащих определенные символы или начинающихся с определенного количества подчеркиваний.
2.  Определяет список директорий, которые нужно исключить из поиска.
3.  Итерирует по указанным шаблонам файлов в директории `src_path`.
4.  Проверяет, находится ли файл в исключенной директории.
5.  Проверяет, соответствует ли имя файла исключающему шаблону.
6.  Читает содержимое файла и возвращает его вместе с путем к файлу.

**Параметры**:

*   `src_path` (Path): Базовая директория для поиска файлов.
*   `patterns` (list\[str]): Список шаблонов файлов для включения (например, `['*.py', '*.txt']`).

**Возвращает**:

*   `Iterator[tuple[Path, str]]`: Итератор, возвращающий кортеж, содержащий путь к файлу и его содержимое в виде строки.

**Вызывает исключения**:

*   `OSError`: В случае ошибки при чтении файла.

**Примеры**:

```python
from pathlib import Path
src_path = Path('src')
patterns = ['*.py', 'README.MD']
for file_path, content in yield_files_content(src_path, patterns):
    print(f'File: {file_path}')
    print(f'Content: {content[:100]}...')