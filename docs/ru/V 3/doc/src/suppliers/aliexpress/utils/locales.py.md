# Модуль `locales`

## Обзор

Модуль `locales` предназначен для загрузки и обработки данных локалей из JSON-файла. Он предоставляет функцию `get_locales` для получения списка словарей, содержащих пары "локаль-валюта".

## Подробней

Этот модуль используется для загрузки данных о локалях, необходимых для работы с AliExpress. Данные о локалях хранятся в JSON-файле и используются для определения валюты, соответствующей определенной стране или региону. Функция `get_locales` считывает данные из JSON-файла и возвращает их в виде списка словарей. Этот список используется в других частях проекта для обработки цен и других данных, связанных с локалями.

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

**Описание**: Загружает данные локалей из JSON-файла.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные локалей.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей, где каждый словарь содержит пару "локаль-валюта". Возвращает `None`, если файл не найден или имеет неверный формат.

**Примеры**:

```python
from pathlib import Path
from src.suppliers.aliexpress.utils.locales import get_locales

# Предположим, что locales.json содержит:
# {"locales": [{"EN": "USD"}, {"HE": "ILS"}, {"RU": "ILS"}, {"EN": "EUR"}, {"EN": "GBR"}, {"RU": "EUR"}]}

locales_path = Path('путь/к/locales.json')
locales = get_locales(locales_path)
print(locales)
# Вывод: [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]