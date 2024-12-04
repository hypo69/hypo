# Модуль `hypotez/src/check_release.py`

## Обзор

Этот модуль предоставляет функцию для проверки последней версии релиза на GitHub.


## Функции

### `check_latest_release`

**Описание**: Проверяет последнюю версию релиза на GitHub по заданному владельцу и имени репозитория.

**Параметры**:
- `owner` (str): Владелец репозитория на GitHub.
- `repo` (str): Имя репозитория на GitHub.

**Возвращает**:
- str: Последняя версия релиза в формате строки, если доступна. В противном случае возвращает `None`.

**Вызывает исключения**:
- Возможны исключения, возникающие при запросе к API GitHub (например, `requests.exceptions.RequestException`).  Необходимо обработать возможные ошибки, используя блок `try...except`.

**Пример использования**:

```python
owner = "your_github_username"
repo = "your_repository_name"

latest_version = check_latest_release(owner, repo)

if latest_version:
    print(f"Latest release version: {latest_version}")
else:
    print("No latest release found.")
```


**Код функции**:

```python
import requests
from src.logger import logger

def check_latest_release(owner: str, repo: str):
    """Check the latest release version of a GitHub repository.

    Args:
        owner (str): The owner of the repository.
        repo (str): The name of the repository.

    Returns:
        str: The latest release version if available, else None.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    try:
        response = requests.get(url)
        response.raise_for_status() #Обрабатывает ошибки HTTP статусы, отличные от 200
        latest_release = response.json()
        return latest_release['tag_name']
    except requests.exceptions.RequestException as ex:
        logger.error(f"Ошибка при запросе к API GitHub: {ex}")
        return None
    except KeyError as ex:
        logger.error(f"Ошибка при парсинге ответа API GitHub: {ex}")
        return None
```


**Примечания**:

- Функция `check_latest_release` использует библиотеку `requests` для запроса данных к API GitHub.
- Обработка ошибок позволяет избежать неожиданных завершений выполнения при сбоях во время запроса или некорректных ответах от API.
-  Важно включить обработку исключений `KeyError` для случая, когда ожидаемый ключ `tag_name` отсутствует в ответе.
-  В примере добавлен блок `try...except` для правильной обработки возможных ошибок и логирования.

## Модуль `src.logger`

**Описание**: Этот модуль содержит функции для логирования ошибок и сообщений.  Должен быть импортирован и использован для улучшения отладки.


**Примечание**: Документация для модуля `src.logger` не предоставлена, и её необходимо создать отдельно, следуя тем же принципам.