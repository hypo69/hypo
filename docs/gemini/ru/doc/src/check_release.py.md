# `check_release.py`

## Обзор

Модуль `check_release.py` предназначен для проверки последней версии релиза на GitHub. Он использует API GitHub для получения информации о последнем релизе и возвращает его версию.

## Содержание

1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`check_latest_release`](#check_latest_release)

## Функции

### `check_latest_release`

**Описание**: Проверяет последнюю версию релиза в репозитории GitHub.

**Параметры**:
- `owner` (str): Владелец репозитория.
- `repo` (str): Название репозитория.

**Возвращает**:
- `str`: Последняя версия релиза, если она доступна, иначе `None`.

**Пример использования:**
```python
from src.check_release import check_latest_release

owner = "owner"
repo = "repo"
latest_release = check_latest_release(owner, repo)
if latest_release:
    print(f"Latest release: {latest_release}")
else:
    print("Could not fetch the latest release version.")
```