# Модуль `locales`

## Обзор

Модуль предназначен для загрузки данных о локалях из JSON-файла. Он содержит функции для загрузки и обработки данных о локалях, которые используются для определения валюты для разных языков.

## Подробнее

Этот модуль предоставляет функциональность для загрузки и обработки данных о локалях, которые используются для определения валюты для разных языков. Он использует функции `j_loads` и `j_loads_ns` для загрузки данных из JSON-файла. Расположение файла в проекте: `hypotez/src/suppliers/aliexpress/utils/locales.py`.

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
    ...
```

**Назначение**: Загружает данные о локалях из JSON-файла.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей с парами локаль и валюта или `None`, если данные о локалях отсутствуют.

**Как работает функция**:
1. Функция использует `j_loads_ns` для загрузки данных из JSON-файла, указанного в `locales_path`.
2. После загрузки данных функция пытается получить доступ к атрибуту `locales` загруженного объекта.
3. Если атрибут `locales` существует, функция возвращает его значение. В противном случае возвращается `None`.

**Примеры**:

```python
from pathlib import Path
from src.suppliers.aliexpress.utils.locales import get_locales

# Пример использования с указанием пути к файлу
locales_path = Path('путь/к/locales.json')
locales = get_locales(locales_path)

if locales:
    print(locales)
else:
    print('Данные о локалях не найдены.')
```

### `locales`

```python
locales: list[dict[str, str]] | None = get_locales (gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json') # defined locales for campaigns
```

**Назначение**: Определены локали для рекламных кампаний. Переменная `locales` содержит список словарей, где каждый словарь представляет собой пару локаль-валюта. Значение инициализируется путем вызова функции `get_locales` с путем к файлу `locales.json`.