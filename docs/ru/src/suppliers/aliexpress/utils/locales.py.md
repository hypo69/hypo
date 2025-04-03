# Модуль для загрузки данных о локалях из JSON файла
## Обзор

Модуль `locales.py` предназначен для загрузки и обработки данных о локалях из JSON-файла. Он предоставляет функции для получения данных о локалях, которые используются в проекте `hypotez` для работы с поставщиком AliExpress.

## Подробней

Этот модуль содержит функцию `get_locales`, которая загружает данные о локалях из JSON файла, используя `j_loads_ns` из модуля `src.utils.jjson`. Данные о локалях представляют собой список словарей, где каждый словарь содержит информацию о соответствии языка и валюты. Эти данные используются для настройки и запуска рекламных кампаний.

## Функции

### `get_locales`

```python
def get_locales(locales_path: Path | str) -> list[dict[str, str]] | None:
    """ Функция загружает данные о локалях из JSON-файла.

    Args:
        locales_path (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

    Returns:
        list[dict[str, str]] | None: Список словарей с парами локаль и валюта. Возвращает `None`, если данные о локалях не найдены.

    Raises:
        FileNotFoundError: Если файл по указанному пути не найден.
        json.JSONDecodeError: Если файл содержит некорректный JSON.

    Example:
        >>> from pathlib import Path
        >>> locales_path = Path('path/to/locales.json')
        >>> locales = get_locales(locales_path)
        >>> if locales:
        ...     print(locales)
        ... else:
        ...     print("Locales not found.")
        [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
    """
    ...
```

**Назначение**: Загрузка данных о локалях из JSON-файла.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей с парами локаль и валюта. Возвращает `None`, если данные о локалях не найдены.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл по указанному пути не найден.
- `json.JSONDecodeError`: Если файл содержит некорректный JSON.

**Как работает функция**:

1.  Функция `get_locales` принимает путь к JSON файлу с данными о локалях.
2.  Она использует функцию `j_loads_ns` для загрузки данных из JSON файла.
3.  Из загруженных данных извлекается список локалей, хранящийся в поле `locales`.
4.  Если список локалей существует, он возвращается. В противном случае возвращается `None`.

```
    locales_path
    |
    j_loads_ns(locales_path) --> Загрузка JSON данных
    |
    locales.locales --> Извлечение списка локалей
    |
    Возврат списка локалей или None
```

**Примеры**:

```python
from pathlib import Path
from src.suppliers.aliexpress.utils.locales import get_locales

# Пример 1: Загрузка локалей из файла
locales_path = Path('path/to/locales.json')
locales = get_locales(locales_path)
if locales:
    print(locales)
else:
    print("Locales not found.")

# Пример 2: Обработка случая, когда файл не найден
locales_path = 'non_existent_file.json'
locales = get_locales(locales_path)
if locales:
    print(locales)
else:
    print("Locales not found.")
```

### `locales`

```python
locales: list[dict[str, str]] | None = get_locales (gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json') # defined locales for campaigns
```

**Назначение**: Определены локали для рекламных кампаний.

**Описание**:
Переменная `locales` содержит список словарей, полученный путем вызова функции `get_locales` с путем к файлу `locales.json`. Этот список используется для настройки рекламных кампаний. Путь к файлу формируется с использованием объекта `gs.path.src`.
```