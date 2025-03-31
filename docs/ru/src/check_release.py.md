# Модуль проверки последней версии релиза

## Обзор

Модуль `check_release.py` предназначен для проверки последней версии релиза репозитория на GitHub. Он использует API GitHub для получения информации о релизах и возвращает номер последней версии.

## Подробней

Этот модуль предоставляет функцию `check_latest_release`, которая позволяет получить информацию о последней версии релиза указанного репозитория на GitHub. Это может быть полезно для автоматической проверки наличия обновлений в проекте.

## Функции

### `check_latest_release`

```python
def check_latest_release(owner: str, repo: str):
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
```

**Описание**: Проверяет последнюю версию релиза репозитория на GitHub.

**Как работает функция**:
1. Формирует URL для запроса к API GitHub для получения информации о последнем релизе репозитория.
2. Отправляет GET-запрос к API GitHub.
3. Если запрос успешен (код ответа 200), извлекает номер версии из JSON-ответа и возвращает его.
4. Если запрос не успешен, логирует ошибку и возвращает `None`.

**Параметры**:
- `owner` (str): Имя владельца репозитория.
- `repo` (str): Имя репозитория.

**Возвращает**:
- `str`: Номер последней версии релиза, если доступен.
- `None`: Если не удалось получить информацию о релизе.

**Примеры**:
```python
owner = 'your_github_username'
repo = 'your_repo_name'
latest_version = check_latest_release(owner, repo)
if latest_version:
    print(f'Latest version: {latest_version}')
else:
    print('Could not retrieve the latest version.')