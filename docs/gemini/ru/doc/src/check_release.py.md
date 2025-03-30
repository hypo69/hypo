# Модуль check_release

## Обзор

Модуль `check_release` предназначен для проверки последней версии релиза репозитория на GitHub. Он использует API GitHub для получения информации о релизах и возвращает тег последней версии.

## Подробней

Этот модуль полезен для автоматической проверки наличия новых версий программного обеспечения или библиотек, размещенных на GitHub. Он может быть использован в скриптах развертывания, системах мониторинга или других автоматизированных процессах для обновления до последней версии.

## Функции

### `check_latest_release`

```python
def check_latest_release(owner: str, repo: str) -> str:
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
    #  url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    #  response = requests.get(url)
    #
    #  if response.status_code == 200:
    #      latest_release = response.json()
    #      return latest_release['tag_name']
    #  else:
    #      #logger.error(f"Error fetching data: {response.status_code}")
    #      #TODO: Код не проверен
    #      return 
```

**Описание**: Функция `check_latest_release` проверяет последнюю версию релиза указанного репозитория на GitHub.

**Параметры**:

- `owner` (str): Имя владельца репозитория.
- `repo` (str): Имя репозитория.

**Возвращает**:

- `str`: Тег последней версии релиза, если он доступен. В противном случае возвращает `None`.

**Как работает функция**:

1. Формируется URL для запроса к API GitHub для получения информации о последнем релизе репозитория.
2. Отправляется GET-запрос к API GitHub.
3. Если статус код ответа равен 200 (успешный запрос), извлекается JSON-ответ, содержащий информацию о последнем релизе.
4. Извлекается значение поля `tag_name` из JSON-ответа, которое представляет собой тег последней версии релиза.
5. Если статус код ответа не равен 200, возвращается `None`.

**Примеры**:

```python
from src.check_release import check_latest_release

owner = 'octocat'
repo = 'Spoon-Knife'
latest_version = check_latest_release(owner, repo)
if latest_version:
    print(f"Latest version of {owner}/{repo}: {latest_version}")
else:
    print(f"Could not retrieve the latest version of {owner}/{repo}")
```
```python
from src.check_release import check_latest_release

owner = 'google'
repo = 'jax'
latest_version = check_latest_release(owner, repo)
if latest_version:
    print(f"Latest version of {owner}/{repo}: {latest_version}")
else:
    print(f"Could not retrieve the latest version of {owner}/{repo}")
```
```python
from src.check_release import check_latest_release

owner = 'unknown'
repo = 'unknown'
latest_version = check_latest_release(owner, repo)
if latest_version:
    print(f"Latest version of {owner}/{repo}: {latest_version}")
else:
    print(f"Could not retrieve the latest version of {owner}/{repo}")