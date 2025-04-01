# Модуль для работы с ассистентом программиста Copilot
=========================================================

Модуль предназначен для автоматического анализа Pull Request'ов в репозитории GitHub с использованием AI моделей (g4f). Он позволяет генерировать комментарии к изменениям в коде и создавать ревью для Pull Request'ов.

## Обзор

Данный модуль автоматизирует процесс анализа изменений в коде, представленных в Pull Request'ах GitHub. Он использует модель g4f для генерации комментариев и ревью, что помогает улучшить качество кода и ускорить процесс code review. Модуль интегрируется с GitHub API и позволяет автоматически создавать issue comments и code review comments.

## Подробнее

Модуль предназначен для автоматизации анализа изменений в коде в Pull Request'ах GitHub. Он использует AI модель для генерации комментариев к коду и общего ревью. Это позволяет улучшить качество кода и ускорить процесс code review.

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
    ...
```

**Назначение**: Получает детали Pull Request из GitHub.

**Параметры**:
- `github` (`Github`): Объект Github для взаимодействия с API GitHub.

**Возвращает**:
- `PullRequest`: Объект, представляющий Pull Request.

**Как работает функция**:

1.  Функция пытается открыть файл `./pr_number` и прочитать номер Pull Request из него.
2.  Если номер Pull Request отсутствует, функция возвращает `None`.
3.  Используя номер Pull Request и объект `github`, функция получает Pull Request из репозитория GitHub.
4.  Возвращает объект Pull Request.

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
    ...
```

**Назначение**: Получает diff Pull Request по заданному URL.

**Параметры**:
- `diff_url` (`str`): URL к diff Pull Request.

**Возвращает**:
- `str`: Diff Pull Request.

**Как работает функция**:

1.  Функция выполняет GET-запрос к указанному `diff_url`.
2.  Проверяет статус ответа и вызывает исключение, если статус указывает на ошибку.
3.  Возвращает текст ответа, содержащий diff Pull Request.

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
    ...
```

**Назначение**: Извлекает JSON код из строки и преобразует его в словарь.

**Параметры**:
- `text` (`str`): Строка, содержащая JSON код.

**Возвращает**:
- `dict`: Словарь, полученный из JSON кода.

**Вызывает исключения**:
- `RuntimeError`: Если входная строка не содержит валидный JSON.

**Как работает функция**:

1.  Функция ищет JSON код внутри markdown-подобного блока кода (```json ... ```).
2.  Если находит, извлекает JSON код.
3.  Пытается преобразовать JSON код в словарь Python с помощью `json.loads()`.
4.  Если преобразование успешно, возвращает полученный словарь.
5.  Если преобразование не удается (JSONDecodeError), вызывает исключение RuntimeError.

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
    ...
```

**Назначение**: Извлекает текст из markdown-подобного блока кода.

**Параметры**:
- `text` (`str`): Строка, содержащая markdown-подобный блок кода.

**Возвращает**:
- `str`: Извлеченный текст.

**Вызывает исключения**:
- `RuntimeError`: Если входная строка не содержит валидный markdown блок кода.

**Как работает функция**:

1.  Функция ищет текст внутри markdown-подобного блока кода (```markdown ... ```).
2.  Если находит, извлекает текст.
3.  Возвращает извлеченный текст.
4.  Если блок кода не найден, вызывает исключение RuntimeError.

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
    ...
```

**Назначение**: Получает ответ от API g4f на основе предоставленного запроса.

**Параметры**:
- `prompt` (`str`): Запрос для отправки в g4f.
- `as_json` (`bool`): Определяет, нужно ли разбирать ответ как JSON. По умолчанию `True`.

**Возвращает**:
- `Union[dict, str]`: Разобранный ответ от g4f, либо как словарь (если `as_json=True`), либо как строка.

**Как работает функция**:

1.  Функция отправляет запрос в API g4f, используя предоставленный `prompt`.
2.  Если `as_json=True`, функция пытается разобрать полученный ответ как JSON с помощью функции `read_json()`.
3.  Если `as_json=False`, функция извлекает текст из ответа с помощью функции `read_text()`.
4.  Возвращает разобранный ответ.

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
    ...
```

**Назначение**: Анализирует изменения в коде в Pull Request.

**Параметры**:
- `pull` (`PullRequest`): Объект Pull Request.
- `diff` (`str`): Diff Pull Request.

**Возвращает**:
- `list[dict]`: Список комментариев, сгенерированных анализом.

**Как работает функция**:

1.  Функция проходит по каждой строке в diff Pull Request.
2.  Определяет текущий путь к файлу и измененные строки.
3.  Когда находит блок измененных строк, формирует запрос к AI модели с помощью функции `create_analyze_prompt()`.
4.  Получает ответ от AI модели с помощью функции `get_ai_response()`.
5.  Извлекает комментарии из ответа и добавляет их в список комментариев.
6.  Возвращает список комментариев.

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
    ...
```

**Назначение**: Создает запрос для модели g4f для анализа изменений в коде.

**Параметры**:
- `changed_lines` (`list[str]`): Список измененных строк кода.
- `pull` (`PullRequest`): Объект Pull Request.
- `file_path` (`str`): Путь к файлу, который анализируется.

**Возвращает**:
- `str`: Сгенерированный запрос.

**Как работает функция**:

1.  Функция принимает список измененных строк кода, объект Pull Request и путь к файлу.
2.  Формирует запрос для модели g4f, включая инструкции по форматированию ответа в виде JSON.
3.  В запрос включается заголовок и описание Pull Request, а также измененный код.
4.  Возвращает сформированный запрос.

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
    ...
```

**Назначение**: Создает запрос для создания review comment.

**Параметры**:
- `pull` (`PullRequest`): Объект Pull Request.
- `diff` (`str`): Diff Pull Request.

**Возвращает**:
- `str`: Сгенерированный запрос для review.

**Как работает функция**:

1.  Формирует запрос для AI модели, чтобы создать ревью для Pull Request.
2.  В запрос включается информация об авторе Pull Request, заголовке, описании и diff.
3.  В запрос включаются инструкции по стилю и формату ответа.
4.  Возвращает сформированный запрос.

### `main`

```python
def main():
    """
    """
    ...
```

**Назначение**: Главная функция, запускающая процесс анализа Pull Request и создания ревью.

**Как работает функция**:

1.  Инициализирует подключение к GitHub API с использованием токена.
2.  Получает детали Pull Request с помощью функции `get_pr_details()`.
3.  Получает diff Pull Request с помощью функции `get_diff()`.
4.  Создает ревью с помощью AI модели, используя функцию `create_review_prompt()`.
5.  Анализирует код в Pull Request с помощью функции `analyze_code()`.
6.  Публикует ревью и комментарии к коду в Pull Request.

## Примеры

Пример использования модуля для анализа Pull Request и создания ревью:

```python
# Для начала работы необходимо установить переменные окружения GITHUB_TOKEN, GITHUB_REPOSITORY, G4F_PROVIDER, G4F_MODEL
# GITHUB_TOKEN - токен для доступа к GitHub API
# GITHUB_REPOSITORY - имя репозитория в формате owner/repository
# G4F_PROVIDER - провайдер g4f
# G4F_MODEL - модель g4f

# Пример вызова функции main()
if __name__ == "__main__":
    main()