# Модуль `locales`

## Обзор

Модуль `locales` предназначен для загрузки данных о локалях из JSON-файла. Он предоставляет функции для получения списка словарей, содержащих информацию о соответствии локалей и валют. Этот модуль используется для настройки и поддержки различных локалей в проекте AliExpress.

## Подробней

Модуль содержит функцию `get_locales`, которая загружает данные из JSON-файла, используя `j_loads_ns` из модуля `src.utils.jjson`. Полученные данные используются для определения локалей для рекламных кампаний.

## Функции

### `get_locales`

```python
def get_locales(locales_path: Path | str) -> list[dict[str, str]] | None:
    """Load locales data from a JSON file.

    Args:
        path (Path): Path to the JSON file containing locales data.

    Returns:
        list[dict[str, str]]: List of dictionaries with locale and currency pairs.

    Examples:
        >>> from src.suppliers.aliexpress.utils.locales import load_locales_data
        >>> locales = load_locales_data(Path('/path/to/locales.json'))
        >>> print(locales)
        [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
    """
    locales = j_loads_ns(locales_path)
    return locales.locales or None
```

**Описание**:
Загружает данные о локалях из JSON-файла.

**Как работает функция**:
1. Функция принимает путь к JSON-файлу с данными о локалях.
2. Использует `j_loads_ns` для загрузки данных из файла. `j_loads_ns`  - это функция из модуля `src.utils.jjson`, предназначенная для чтения JSON или конфигурационных файлов.
3. Возвращает список словарей, содержащих пары локаль-валюта, если данные успешно загружены. В случае отсутствия данных возвращает `None`.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей с парами локаль и валюта или `None`, если данные отсутствуют.

**Примеры**:

```python
>>> from pathlib import Path
>>> from src.suppliers.aliexpress.utils.locales import get_locales
>>> file_path = Path('путь/к/locales.json')
>>> locales = get_locales(file_path)
>>> if locales:
...     print(locales)
... else:
...     print('Локали не найдены')
```

## Переменные

### `locales`

```python
locales: list[dict[str, str]] | None = get_locales (gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json') # defined locales for campaigns
```

**Описание**:
Определенные локали для кампаний.

**Назначение**:
Переменная `locales` содержит список словарей, полученных из JSON-файла, который определяет соответствие локалей и валют для рекламных кампаний AliExpress. Этот список используется для настройки и поддержки различных локалей в проекте.