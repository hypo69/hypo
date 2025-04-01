# Модуль для автоматической проверки Pull Request с использованием g4f (GPT4Free)
=======================================================================

Модуль предназначен для автоматического анализа изменений в Pull Request на GitHub с использованием AI моделей, предоставляемых библиотекой `g4f`. Он позволяет генерировать комментарии к изменениям кода и создавать общие ревью Pull Request.

## Обзор

Этот модуль автоматизирует процесс проверки Pull Request, используя AI для анализа изменений кода и генерации комментариев и ревью. Он интегрируется с GitHub API для получения информации о Pull Request и отправки результатов анализа. Модуль использует библиотеку `g4f` для взаимодействия с различными AI моделями.

## Подробнее

Модуль выполняет следующие основные задачи:

1.  Получение деталей Pull Request из GitHub.
2.  Получение diff изменений кода.
3.  Анализ изменений кода с помощью AI.
4.  Создание комментариев к изменениям кода.
5.  Создание общего ревью Pull Request.
6.  Отправка комментариев и ревью в GitHub.

Этот модуль предназначен для использования в CI/CD пайплайнах для автоматизации процесса проверки кода. Он позволяет сократить время, затрачиваемое на ручную проверку кода, и повысить качество кода.

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

**Назначение**: Извлекает детали Pull Request из GitHub.

**Параметры**:

*   `github` (Github): Объект Github для взаимодействия с GitHub API.

**Возвращает**:

*   `PullRequest`: Объект, представляющий Pull Request.

**Как работает функция**:

1.  Читает номер Pull Request из файла `./pr_number`.
2.  Если номер не найден, функция завершается.
3.  Получает репозиторий из GitHub API, используя переменную окружения `GITHUB_REPOSITORY`.
4.  Получает Pull Request по номеру из репозитория.

**Примеры**:

```python
from github import Github
# Для работы этого примера требуется предварительная настройка github и наличие файла ./pr_number с номером PR
# github = Github(GITHUB_TOKEN)
# pull = get_pr_details(github)
# if pull:
#     print(f"Pull request title: {pull.title}")
# else:
#     print("Pull request not found.")
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

**Назначение**: Получает diff Pull Request по указанному URL.

**Параметры**:

*   `diff_url` (str): URL diff Pull Request.

**Возвращает**:

*   `str`: Diff Pull Request.

**Вызывает исключения**:

*   `requests.exceptions.HTTPError`: Если запрос к `diff_url` завершается с ошибкой.

**Как работает функция**:

1.  Выполняет GET-запрос к указанному URL.
2.  Проверяет статус ответа, и вызывает исключение, если он не равен 200.
3.  Возвращает текст ответа, который является diff Pull Request.

**Примеры**:

```python
# diff_url = "https://github.com/owner/repo/pull/123.diff"  #  Замените на реальный URL
# diff = get_diff(diff_url)
# print(diff[:100]) # Вывод первых 100 символов diff
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

**Назначение**: Извлекает JSON из текстового блока кода.

**Параметры**:

*   `text` (str): Строка, содержащая блок кода JSON.

**Возвращает**:

*   `dict`: Словарь, полученный из блока кода JSON.

**Вызывает исключения**:

*   `RuntimeError`: Если JSON недействителен.

**Как работает функция**:

1.  Использует регулярное выражение для поиска блока кода JSON в строке.
2.  Если блок кода найден, извлекает код JSON.
3.  Пытается загрузить JSON из извлеченного кода.
4.  Возвращает словарь, полученный из JSON.
5.  Если JSON недействителен, вызывает исключение `RuntimeError`.

**Примеры**:

```python
# json_string = "```json\n{\"key\": \"value\"}\n```"
# data = read_json(json_string)
# print(data["key"])  # Вывод: value
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

**Назначение**: Извлекает текст из блока кода Markdown.

**Параметры**:

*   `text` (str): Строка, содержащая блок кода Markdown.

**Возвращает**:

*   `str`: Извлеченный текст.

**Вызывает исключения**:

*   `RuntimeError`: Если Markdown недействителен.

**Как работает функция**:

1.  Использует регулярное выражение для поиска блока кода Markdown в строке.
2.  Если блок кода найден, извлекает текст.
3.  Возвращает извлеченный текст.
4.  Если блок кода не найден, вызывает исключение `RuntimeError`.

**Примеры**:

```python
# markdown_string = "```markdown\nThis is some text.\n```"
# text = read_text(markdown_string)
# print(text)  # Вывод: This is some text.
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
*   `as_json` (bool): Нужно ли анализировать ответ как JSON.

**Возвращает**:

*   `Union[dict, str]`: Проанализированный ответ от g4f, либо как словарь, либо как строка.

**Как работает функция**:

1.  Отправляет запрос в API g4f, используя `g4f.ChatCompletion.create`.
    *   Использует модель, указанную в переменной окружения `G4F_MODEL` или `g4f.models.gpt_4` по умолчанию.
    *   Игнорирует потоковую передачу и аутентификацию.
2.  Если `as_json` имеет значение `True`, пытается проанализировать ответ как JSON с помощью функции `read_json`.
3.  Если `as_json` имеет значение `False`, пытается извлечь текст из ответа с помощью функции `read_text`.
4.  Возвращает проанализированный ответ.

**Примеры**:

```python
# prompt = "Translate 'hello' to Russian."
# response = get_ai_response(prompt, False)
# print(response)  # Вывод:  Привет
# prompt = "Give me a JSON object with a key 'greeting' and value 'hello'."
# response = get_ai_response(prompt, True)
# print(response["greeting"]) # Вывод: hello
```

### `analyze_code`

```python
def analyze_code(pull: PullRequest, diff: str)-> list[dict]:
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

*   `list[dict]`: Список комментариев, сгенерированных в результате анализа.

**Как работает функция**:

1.  Инициализирует пустой список `comments` для хранения сгенерированных комментариев.
2.  Разбивает diff на строки.
3.  Перебирает строки diff:
    *   Если строка начинается с `+++ b/`, извлекает путь к файлу и сбрасывает список измененных строк.
    *   Если строка начинается с `@@`, извлекает номер начальной строки.
    *   Если строка начинается с `-`, добавляет строку в список измененных строк.
    *   В противном случае добавляет строку с номером начальной строки в список измененных строк и увеличивает номер начальной строки.
    *   Если обнаружена строка `\` или строка `diff`, и список измененных строк не пуст, создает запрос для модели g4f с помощью функции `create_analyze_prompt`, получает ответ от модели с помощью функции `get_ai_response` и добавляет комментарии из ответа в список комментариев.
4.  Возвращает список комментариев.

**Примеры**:

```python
# from github import Github
# # Для работы этого примера требуется предварительная настройка github и наличие файла ./pr_number с номером PR
# github = Github(GITHUB_TOKEN)
# pull = get_pr_details(github)
# if pull:
#     diff = get_diff(pull.diff_url)
#     comments = analyze_code(pull, diff)
#     print(comments)
# else:
#     print("Pull request not found.")
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

*   `changed_lines` (list[str]): Список строк кода, которые были изменены.
*   `pull` (PullRequest): Объект Pull Request.
*   `file_path` (str): Путь к файлу, который просматривается.

**Возвращает**:

*   `str`: Сгенерированный запрос.

**Как работает функция**:

1.  Соединяет измененные строки кода в одну строку.
2.  Создает пример формата JSON для ответа.
3.  Формирует запрос, включающий инструкции для модели:
    *   Предоставить ответ в формате JSON.
    *   Не давать положительных комментариев или комплиментов.
    *   Предоставлять комментарии и предложения ТОЛЬКО если есть что улучшить, в противном случае "reviews" должен быть пустым массивом.
    *   Писать комментарий в формате GitHub Markdown.
    *   Использовать описание только для общего контекста и комментировать только код.
    *   НИКОГДА не предлагать добавлять комментарии к коду.
4.  Включает в запрос заголовок и описание Pull Request.
5.  Включает в запрос измененный код.
6.  Возвращает сформированный запрос.

**Примеры**:

```python
# from github import Github
# # Для работы этого примера требуется предварительная настройка github и наличие файла ./pr_number с номером PR
# github = Github(GITHUB_TOKEN)
# pull = get_pr_details(github)
# if pull:
#     diff = get_diff(pull.diff_url)
#     # Предположим, что у нас есть список измененных строк
#     changed_lines = diff.split('\n')[:10]  #  Возьмем первые 10 строк diff для примера
#     file_path = "example.py"  # Замените на реальный путь к файлу
#     prompt = create_analyze_prompt(changed_lines, pull, file_path)
#     print(prompt)
# else:
#     print("Pull request not found.")
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

1.  Формирует запрос, включающий инструкции для модели:
    *   Писать от имени g4f copilot. Не использовать заполнители.
    *   Писать ревью в формате GitHub Markdown.
    *   Заключать ответ в обратные кавычки ```markdown```.
    *   Благодарить автора за вклад в проект.
2.  Включает в запрос имя автора Pull Request, заголовок и описание Pull Request.
3.  Включает в запрос diff Pull Request.
4.  Возвращает сформированный запрос.

**Примеры**:

```python
# from github import Github
# # Для работы этого примера требуется предварительная настройка github и наличие файла ./pr_number с номером PR
# github = Github(GITHUB_TOKEN)
# pull = get_pr_details(github)
# if pull:
#     diff = get_diff(pull.diff_url)
#     prompt = create_review_prompt(pull, diff)
#     print(prompt)
# else:
#     print("Pull request not found.")
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

**Назначение**: Основная функция, запускающая процесс анализа Pull Request.

**Как работает функция**:

1.  Инициализирует объект `Github` с использованием токена из переменной окружения `GITHUB_TOKEN`.
2.  Получает детали Pull Request с помощью функции `get_pr_details`.
3.  Если Pull Request не найден, выводит сообщение и завершает работу.
4.  Получает diff Pull Request с помощью функции `get_diff`.
5.  Обрабатывает исключения, которые могут возникнуть при получении деталей Pull Request и diff.
6.  Создает ревью с помощью функции `create_review_prompt` и получает ответ от AI с помощью функции `get_ai_response`.
7.  Обрабатывает исключения, которые могут возникнуть при создании ревью.
8.  Если у Pull Request уже есть ревью или комментарии, создает комментарий к задаче с текстом ревью и завершает работу.
9.  Анализирует код с помощью функции `analyze_code` и получает список комментариев.
10. Обрабатывает исключения, которые могут возникнуть при анализе кода.
11. Если есть комментарии, создает ревью с комментариями и текстом ревью.
12. Если нет комментариев, создает комментарий к задаче с текстом ревью.
13. Обрабатывает исключения, которые могут возникнуть при публикации ревью.

**Примеры**:

```python
# Для работы этого примера требуется предварительная настройка github и наличие файла ./pr_number с номером PR
# export GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
# echo "123" > ./pr_number # Замените 123 на номер реального PR
# python your_script_name.py
```

## Переменные окружения

*   `GITHUB_TOKEN`: Токен GitHub для доступа к API.
*   `GITHUB_REPOSITORY`: Название репозитория GitHub в формате `owner/repo`.
*   `G4F_PROVIDER`: Провайдер g4f.
*   `G4F_MODEL`: Модель g4f (по умолчанию `g4f.models.gpt_4`).