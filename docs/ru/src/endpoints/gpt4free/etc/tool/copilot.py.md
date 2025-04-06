# Модуль для анализа Pull Request с использованием g4f (GPT4Free)
==============================================================

Модуль предназначен для автоматического анализа изменений в Pull Request на GitHub с использованием AI моделей через библиотеку `g4f`. Он извлекает детали PR, анализирует изменения кода и генерирует комментарии и ревью на основе анализа, используя модели, предоставляемые g4f.

## Обзор

Модуль выполняет следующие основные задачи:

1.  Извлечение информации о Pull Request из GitHub.
2.  Получение дифференциального патча (diff) изменений в PR.
3.  Анализ изменений кода с использованием AI для выявления потенциальных проблем и предложений по улучшению.
4.  Создание ревью и комментариев на основе анализа и публикация их в Pull Request.

Этот модуль автоматизирует процесс ревью кода, помогая разработчикам быстрее выявлять и устранять проблемы в коде. Он использует AI для генерации конструктивных комментариев, что может значительно сократить время, затрачиваемое на ручной анализ.

## Подробнее

Модуль интегрируется с GitHub через API, используя токен доступа, и использует библиотеку `g4f` для взаимодействия с AI моделями. Он анализирует diff изменений в PR, отправляет запросы в g4f для анализа кода и генерирует комментарии и ревью на основе полученных результатов.

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

*   `github` (Github): Объект Github для взаимодействия с API GitHub.

**Возвращает**:

*   `PullRequest`: Объект, представляющий Pull Request.

**Как работает функция**:

1.  Функция читает номер PR из файла `./pr_number`.
2.  Если номер PR не найден, функция возвращает `None`.
3.  Используя объект `github`, функция получает репозиторий и затем сам Pull Request по номеру.
4.  Возвращает объект `PullRequest`, содержащий детали PR.

```ascii
Чтение номера PR из файла -> Получение репозитория GitHub -> Получение Pull Request -> Возврат объекта PullRequest
```

**Примеры**:

```python
from github import Github
# Предполжим, что GITHUB_TOKEN содержит ваш токен GitHub
# g = Github(GITHUB_TOKEN)
# pull_request = get_pr_details(g)
# if pull_request:
#     print(f"Pull Request title: {pull_request.title}")
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

*   `diff_url` (str): URL к diff Pull Request.

**Возвращает**:

*   `str`: Diff Pull Request в виде строки.

**Как работает функция**:

1.  Функция отправляет GET запрос по указанному `diff_url`.
2.  Проверяет статус ответа и вызывает исключение, если статус не 200.
3.  Возвращает текстовое содержимое ответа, которое представляет собой diff.

```ascii
Отправка GET запроса -> Проверка статуса ответа -> Возврат diff в виде строки
```

**Примеры**:

```python
# diff_url = "https://github.com/owner/repo/pull/123.diff"
# diff_content = get_diff(diff_url)
# print(f"Diff content: {diff_content[:100]}...")
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

*   `text` (str): Строка, содержащая блок кода JSON.

**Возвращает**:

*   `dict`: Словарь, полученный из JSON.

**Вызывает исключения**:

*   `RuntimeError`: Если JSON невалиден.

**Как работает функция**:

1.  Функция ищет блок кода JSON, заключенный в тройные обратные кавычки (`````json\n...\n`````).
2.  Если блок найден, извлекает JSON из этого блока.
3.  Парсит JSON и возвращает словарь.
4.  Если JSON невалиден, вызывает `RuntimeError`.

```ascii
Поиск блока кода JSON -> Извлечение JSON -> Парсинг JSON -> Возврат словаря
```

**Примеры**:

```python
# json_string = "```json\n{\"key\": \"value\"}\n```"
# data = read_json(json_string)
# print(f"Parsed JSON: {data}")
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

**Назначение**: Извлекает текст из markdown блока кода.

**Параметры**:

*   `text` (str): Строка, содержащая markdown блок кода.

**Возвращает**:

*   `str`: Извлеченный текст.

**Вызывает исключения**:

*   `RuntimeError`: Если markdown невалиден.

**Как работает функция**:

1.  Функция ищет блок кода markdown, заключенный в тройные обратные кавычки (`````markdown\n...\n`````).
2.  Если блок найден, извлекает текст из этого блока.
3.  Если блок не найден, вызывает `RuntimeError`.
4.  Возвращает извлеченный текст.

```ascii
Поиск блока кода markdown -> Извлечение текста -> Возврат текста
```

**Примеры**:

```python
# markdown_string = "```markdown\nThis is some text.\n```"
# text = read_text(markdown_string)
# print(f"Extracted text: {text}")
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
*   `as_json` (bool): Определяет, нужно ли парсить ответ как JSON.

**Возвращает**:

*   `Union[dict, str]`: Распарсенный ответ от g4f, либо как словарь, либо как строка.

**Как работает функция**:

1.  Функция отправляет запрос в API g4f, используя предоставленный `prompt`.
2.  Если `as_json` равен `True`, функция парсит ответ как JSON и возвращает словарь.
3.  Если `as_json` равен `False`, функция извлекает текст из ответа и возвращает строку.

```ascii
Отправка запроса в g4f -> Проверка `as_json` -> Парсинг JSON (если `True`) / Извлечение текста (если `False`) -> Возврат ответа
```

**Примеры**:

```python
# prompt = "Explain the meaning of life."
# json_response = get_ai_response(prompt, as_json=True)
# text_response = get_ai_response(prompt, as_json=False)
# print(f"JSON response: {json_response}")
# print(f"Text response: {text_response}")
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

*   `list[dict]`: Список комментариев, сгенерированных анализом.

**Как работает функция**:

1.  Функция итерируется по каждой строке в diff.
2.  Определяет путь к файлу, измененные строки и смещение строк.
3.  Когда накапливается достаточно измененных строк, формируется запрос к AI модели для анализа.
4.  Полученный ответ (комментарии) добавляется в список `comments`.
5.  Возвращает список комментариев.

```ascii
Итерация по строкам diff -> Определение пути к файлу и измененных строк -> Формирование запроса к AI -> Добавление комментариев в список -> Возврат списка комментариев
```

**Примеры**:

```python
# from github import Github
# from github.PullRequest import PullRequest
# # Предположим, что у вас есть объекты pull и diff
# # pull = ...  # Объект PullRequest
# # diff = ...  # Diff в виде строки
# comments = analyze_code(pull, diff)
# print(f"Generated comments: {comments}")
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

*   `changed_lines` (list[str]): Список измененных строк кода.
*   `pull` (PullRequest): Объект Pull Request.
*   `file_path` (str): Путь к файлу, который ревьюится.

**Возвращает**:

*   `str`: Сгенерированный запрос.

**Как работает функция**:

1.  Функция принимает список измененных строк, объект Pull Request и путь к файлу.
2.  Формирует запрос для AI модели, включая инструкции о формате ответа, запрете позитивных комментариев и предложений по добавлению комментариев в код.
3.  Добавляет в запрос информацию о заголовке и описании Pull Request, а также измененный код.
4.  Возвращает сформированный запрос в виде строки.

```ascii
Формирование запроса -> Добавление инструкций и информации о PR -> Возврат запроса
```

**Примеры**:

```python
# from github.PullRequest import PullRequest
# # changed_lines = ["+def foo():", "+    print('hello')"]
# # pull = ...  # Объект PullRequest
# # file_path = "example.py"
# prompt = create_analyze_prompt(changed_lines, pull, file_path)
# print(f"Generated prompt: {prompt}")
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

**Назначение**: Создает запрос для генерации ревью.

**Параметры**:

*   `pull` (PullRequest): Объект Pull Request.
*   `diff` (str): Diff Pull Request.

**Возвращает**:

*   `str`: Сгенерированный запрос для ревью.

**Как работает функция**:

1.  Функция принимает объект Pull Request и diff.
2.  Формирует запрос для AI модели, включая инструкции о стиле ревью, формате ответа (GitHub Markdown) и необходимости поблагодарить автора за вклад в проект.
3.  Добавляет в запрос информацию об авторе, заголовке и описании Pull Request, а также diff.
4.  Возвращает сформированный запрос в виде строки.

```ascii
Формирование запроса -> Добавление инструкций и информации о PR -> Возврат запроса
```

**Примеры**:

```python
# from github.PullRequest import PullRequest
# # pull = ...  # Объект PullRequest
# # diff = ...  # Diff в виде строки
# prompt = create_review_prompt(pull, diff)
# print(f"Generated prompt: {prompt}")
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

**Назначение**: Главная функция модуля, которая выполняет анализ Pull Request и публикацию ревью.

**Как работает функция**:

1.  Инициализирует объект `Github` с использованием токена доступа.
2.  Получает детали Pull Request с использованием функции `get_pr_details`.
3.  Получает diff Pull Request с использованием функции `get_diff`.
4.  Генерирует ревью с использованием функции `get_ai_response` и `create_review_prompt`.
5.  Если ревью уже существует, добавляет комментарий к задаче.
6.  Анализирует код с использованием функции `analyze_code`.
7.  Публикует ревью с комментариями или добавляет комментарий к задаче, если комментарии отсутствуют.
8.  Обрабатывает исключения и выводит сообщения об ошибках.

```ascii
Инициализация Github -> Получение деталей PR -> Получение diff -> Генерация ревью -> Анализ кода -> Публикация ревью / комментария
```

**Примеры**:

```python
# Для запуска main необходимо установить переменные окружения GITHUB_TOKEN и GITHUB_REPOSITORY
# и создать файл ./pr_number с номером PR
# python your_script_name.py
```