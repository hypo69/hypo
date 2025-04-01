# Модуль для автоматического анализа Pull Request с использованием G4F
=======================================================================

Модуль предназначен для автоматического анализа изменений кода в Pull Request на GitHub с использованием моделей G4F (GPT for Free). Он позволяет генерировать комментарии к изменениям и создавать ревью, помогая улучшить качество кода и автоматизировать процесс проверки.

## Обзор

Модуль выполняет следующие основные задачи:

1.  Получение информации о Pull Request из GitHub.
2.  Получение diff изменений кода.
3.  Анализ изменений кода с использованием G4F.
4.  Создание комментариев и ревью на основе результатов анализа.

## Подробнее

Этот модуль предназначен для автоматизации процесса анализа кода в Pull Request. Он использует G4F для генерации комментариев и предложений по улучшению кода. Модуль интегрируется с GitHub API для получения информации о Pull Request и публикации результатов анализа.

## Функции

### `get_pr_details`

```python
def get_pr_details(github: Github) -> PullRequest:
    """
    Retrieves the details of the pull request from GitHub.

    Args:
        github (Github): The Github object to interact with the GitHub API.

    Returns:
        PullRequest: An object representing the pull request.
    """
```

**Назначение**: Получает детали Pull Request из GitHub.

**Параметры**:

*   `github` (Github): Объект Github для взаимодействия с GitHub API.

**Возвращает**:

*   `PullRequest`: Объект, представляющий Pull Request.

**Как работает функция**:

1.  Читает номер Pull Request из файла `./pr_number`.
2.  Если номер Pull Request не найден, возвращает `None`.
3.  Получает репозиторий из GitHub.
4.  Получает Pull Request по номеру.
5.  Возвращает объект Pull Request.

```
A: Чтение номера PR из файла
|
B: Проверка наличия номера PR
|
C: Получение репозитория из GitHub
|
D: Получение PR по номеру
|
E: Возврат объекта PR
```

**Примеры**:

```python
# Пример использования функции
from github import Github
# Предполгается, что GITHUB_TOKEN уже установлен
github = Github(os.getenv('GITHUB_TOKEN'))
pull_request = get_pr_details(github)
if pull_request:
    print(f"Pull Request title: {pull_request.title}")
else:
    print("Pull Request not found")
```

### `get_diff`

```python
def get_diff(diff_url: str) -> str:
    """
    Fetches the diff of the pull request from a given URL.

    Args:
        diff_url (str): URL to the pull request diff.

    Returns:
        str: The diff of the pull request.
    """
```

**Назначение**: Получает diff Pull Request по заданному URL.

**Параметры**:

*   `diff_url` (str): URL diff Pull Request.

**Возвращает**:

*   `str`: Diff Pull Request.

**Как работает функция**:

1.  Выполняет GET-запрос по указанному URL.
2.  Проверяет статус ответа (должен быть 200 OK).
3.  Возвращает текст ответа, который является diff Pull Request.

```
A: Выполнение GET-запроса по URL
|
B: Проверка статуса ответа
|
C: Возврат текста ответа
```

**Примеры**:

```python
# Пример использования функции
diff_url = "https://github.com/owner/repo/pull/123.diff"
diff = get_diff(diff_url)
print(f"Diff: {diff[:100]}...")
```

### `read_json`

```python
def read_json(text: str) -> dict:
    """
    Parses JSON code block from a string.

    Args:
        text (str): A string containing a JSON code block.

    Returns:
        dict: A dictionary parsed from the JSON code block.
    """
```

**Назначение**: Извлекает и парсит JSON из строки.

**Параметры**:

*   `text` (str): Строка, содержащая JSON код.

**Возвращает**:

*   `dict`: Словарь, полученный из JSON.

**Вызывает исключения**:

*   `RuntimeError`: Если JSON невалиден.

**Как работает функция**:

1.  Ищет блок кода JSON в строке, используя регулярное выражение.
2.  Извлекает JSON из найденного блока.
3.  Парсит JSON и возвращает словарь.
4.  При ошибке парсинга JSON выбрасывает исключение `RuntimeError`.

```
A: Поиск блока кода JSON в строке
|
B: Извлечение JSON из блока
|
C: Парсинг JSON
|
D: Возврат словаря или исключения
```

**Примеры**:

```python
# Пример использования функции
json_text = "```json\n{\"key\": \"value\"}\n```"
data = read_json(json_text)
print(f"Data: {data}")
```

### `read_text`

```python
def read_text(text: str) -> str:
    """
    Extracts text from a markdown code block.

    Args:
        text (str): A string containing a markdown code block.

    Returns:
        str: The extracted text.
    """
```

**Назначение**: Извлекает текст из блока кода markdown.

**Параметры**:

*   `text` (str): Строка, содержащая блок кода markdown.

**Возвращает**:

*   `str`: Извлеченный текст.

**Вызывает исключения**:

*   `RuntimeError`: Если markdown невалиден.

**Как работает функция**:

1.  Ищет блок кода markdown в строке, используя регулярное выражение.
2.  Извлекает текст из найденного блока.
3.  Возвращает извлеченный текст.
4.  Если блок кода markdown не найден, выбрасывает исключение `RuntimeError`.

```
A: Поиск блока кода markdown в строке
|
B: Извлечение текста из блока
|
C: Возврат извлеченного текста или исключения
```

**Примеры**:

```python
# Пример использования функции
markdown_text = "```markdown\nThis is some text.\n```"
text = read_text(markdown_text)
print(f"Text: {text}")
```

### `get_ai_response`

```python
def get_ai_response(prompt: str, as_json: bool = True) -> Union[dict, str]:
    """
    Gets a response from g4f API based on the prompt.

    Args:
        prompt (str): The prompt to send to g4f.
        as_json (bool): Whether to parse the response as JSON.

    Returns:
        Union[dict, str]: The parsed response from g4f, either as a dictionary or a string.
    """
```

**Назначение**: Получает ответ от API g4f на основе запроса.

**Параметры**:

*   `prompt` (str): Запрос для отправки в g4f.
*   `as_json` (bool): Флаг, указывающий, нужно ли парсить ответ как JSON.

**Возвращает**:

*   `Union[dict, str]`: Распарсенный ответ от g4f, либо в виде словаря, либо в виде строки.

**Как работает функция**:

1.  Отправляет запрос в API g4f.
2.  Если `as_json` равен `True`, парсит ответ как JSON и возвращает словарь.
3.  Если `as_json` равен `False`, извлекает текст из ответа и возвращает строку.

```
A: Отправка запроса в API g4f
|
B: Проверка флага as_json
|
C: Парсинг ответа как JSON или извлечение текста
|
D: Возврат ответа в виде словаря или строки
```

**Примеры**:

```python
# Пример использования функции
prompt = "What is the capital of France?"
response = get_ai_response(prompt)
print(f"Response: {response}")
```

### `analyze_code`

```python
def analyze_code(pull: PullRequest, diff: str) -> list[dict]:
    """
    Analyzes the code changes in the pull request.

    Args:
        pull (PullRequest): The pull request object.
        diff (str): The diff of the pull request.

    Returns:
        list[dict]: A list of comments generated by the analysis.
    """
```

**Назначение**: Анализирует изменения кода в Pull Request.

**Параметры**:

*   `pull` (PullRequest): Объект Pull Request.
*   `diff` (str): Diff Pull Request.

**Возвращает**:

*   `list[dict]`: Список комментариев, сгенерированных анализом.

**Как работает функция**:

1.  Инициализирует пустой список `comments` для хранения комментариев.
2.  Разбивает diff на строки.
3.  Итерируется по строкам diff.
4.  Определяет путь к текущему файлу на основе строк, начинающихся с `+++ b/`.
5.  Определяет смещение строки на основе строк, начинающихся с `@@`.
6.  Собирает измененные строки кода.
7.  Когда встречается строка, начинающаяся с `\` или `diff`, генерирует запрос к AI для анализа измененных строк.
8.  Добавляет полученные комментарии в список `comments`.
9.  Возвращает список комментариев.

```
A: Инициализация списка комментариев
|
B: Разбиение diff на строки
|
C: Итерация по строкам diff
|
D: Определение пути к файлу и смещения строки
|
E: Сбор измененных строк кода
|
F: Генерация запроса к AI для анализа кода
|
G: Добавление комментариев в список
|
H: Возврат списка комментариев
```

**Примеры**:

```python
# Пример использования функции
from github import Github
github = Github(os.getenv('GITHUB_TOKEN'))
pull = github.get_repo(os.getenv('GITHUB_REPOSITORY')).get_pull(123)
diff = get_diff(pull.diff_url)
comments = analyze_code(pull, diff)
print(f"Comments: {comments}")
```

### `create_analyze_prompt`

```python
def create_analyze_prompt(changed_lines: list[str], pull: PullRequest, file_path: str):
    """
    Creates a prompt for the g4f model.

    Args:
        changed_lines (list[str]): The lines of code that have changed.
        pull (PullRequest): The pull request object.
        file_path (str): The path to the file being reviewed.

    Returns:
        str: The generated prompt.
    """
```

**Назначение**: Создает запрос для модели g4f.

**Параметры**:

*   `changed_lines` (list[str]): Измененные строки кода.
*   `pull` (PullRequest): Объект Pull Request.
*   `file_path` (str): Путь к файлу, который анализируется.

**Возвращает**:

*   `str`: Сгенерированный запрос.

**Как работает функция**:

1.  Формирует запрос на основе измененных строк кода, заголовка и описания Pull Request.
2.  Указывает модели g4f, что нужно предоставить комментарии только в случае, если есть что улучшить.
3.  Указывает, что комментарии должны быть в формате GitHub Markdown.
4.  Запрещает добавление комментариев в код.

```
A: Формирование запроса на основе измененных строк, заголовка и описания PR
|
B: Указание модели g4f предоставить комментарии только при необходимости
|
C: Указание формата GitHub Markdown
|
D: Запрет добавления комментариев в код
|
E: Возврат сгенерированного запроса
```

**Примеры**:

```python
# Пример использования функции
from github import Github
github = Github(os.getenv('GITHUB_TOKEN'))
pull = github.get_repo(os.getenv('GITHUB_REPOSITORY')).get_pull(123)
diff = get_diff(pull.diff_url)
changed_lines = diff.split('\n')
file_path = "example.py"
prompt = create_analyze_prompt(changed_lines, pull, file_path)
print(f"Prompt: {prompt}")
```

### `create_review_prompt`

```python
def create_review_prompt(pull: PullRequest, diff: str):
    """
    Creates a prompt to create a review comment.

    Args:
        pull (PullRequest): The pull request object.
        diff (str): The diff of the pull request.

    Returns:
        str: The generated prompt for review.
    """
```

**Назначение**: Создает запрос для создания комментария к ревью.

**Параметры**:

*   `pull` (PullRequest): Объект Pull Request.
*   `diff` (str): Diff Pull Request.

**Возвращает**:

*   `str`: Сгенерированный запрос для ревью.

**Как работает функция**:

1.  Формирует запрос на основе заголовка, описания и diff Pull Request.
2.  Указывает модели g4f, что нужно написать ревью от имени g4f copilot.
3.  Указывает, что ревью должно быть в формате GitHub Markdown.
4.  Предлагает поблагодарить автора за вклад в проект.

```
A: Формирование запроса на основе заголовка, описания и diff PR
|
B: Указание модели g4f написать ревью от имени g4f copilot
|
C: Указание формата GitHub Markdown
|
D: Предложение поблагодарить автора
|
E: Возврат сгенерированного запроса
```

**Примеры**:

```python
# Пример использования функции
from github import Github
github = Github(os.getenv('GITHUB_TOKEN'))
pull = github.get_repo(os.getenv('GITHUB_REPOSITORY')).get_pull(123)
diff = get_diff(pull.diff_url)
prompt = create_review_prompt(pull, diff)
print(f"Prompt: {prompt}")
```

### `main`

```python
def main():
    try:
        github = Github(GITHUB_TOKEN)
        pull = get_pr_details(github)
        if not pull:
            print(f"No PR number found")
            exit()
        diff = get_diff(pull.diff_url)
    except Exception as e:
        print(f"Error get details: {e.__class__.__name__}: {e}")
        exit(1)
    try:
        review = get_ai_response(create_review_prompt(pull, diff), False)
    except Exception as e:
        print(f"Error create review: {e}")
        exit(1)
    if pull.get_reviews().totalCount > 0 or pull.get_issue_comments().totalCount > 0:
        pull.create_issue_comment(body=review)
        return
    try:
        comments = analyze_code(pull, diff)
    except Exception as e:
        print(f"Error analyze: {e}")
        exit(1)
    print("Comments:", comments)
    try:
        if comments:
            pull.create_review(body=review, comments=comments)
        else:
            pull.create_issue_comment(body=review)
    except Exception as e:
        print(f"Error posting review: {e}")
        exit(1)
```

**Назначение**: Главная функция модуля, которая выполняет анализ Pull Request и создает ревью.

**Как работает функция**:

1.  Инициализирует объект `Github` с использованием токена доступа.
2.  Получает детали Pull Request с использованием функции `get_pr_details`.
3.  Получает diff Pull Request с использованием функции `get_diff`.
4.  Создает ревью с использованием функции `create_review_prompt` и отправляет запрос в g4f.
5.  Если у Pull Request уже есть ревью или комментарии, создает комментарий к задаче.
6.  Анализирует код с использованием функции `analyze_code`.
7.  Если есть комментарии, создает ревью с комментариями.
8.  Иначе создает комментарий к задаче с общим ревью.
9.  Обрабатывает исключения, которые могут возникнуть в процессе анализа и создания ревью.

```
A: Инициализация объекта Github
|
B: Получение деталей PR
|
C: Получение diff PR
|
D: Создание ревью
|
E: Проверка наличия ревью или комментариев
|
F: Анализ кода
|
G: Создание ревью с комментариями или комментария к задаче
|
H: Обработка исключений
```

**Примеры**:

Для запуска этого модуля необходимо установить переменные окружения `GITHUB_TOKEN` и `GITHUB_REPOSITORY`. Затем можно запустить модуль как скрипт Python.
```python
# Пример запуска модуля
if __name__ == "__main__":
    main()