# Модуль `locales`

## Обзор

Модуль `locales` предназначен для загрузки данных о локалях из JSON-файла. Он предоставляет функцию `get_locales`, которая загружает данные о локалях и возвращает список словарей, содержащих пары локаль-валюта. Этот модуль используется для определения локалей для рекламных кампаний AliExpress.

## Подробней

Модуль содержит функции для загрузки и обработки данных о локалях из JSON-файла. Он использует функции `j_loads` или `j_loads_ns` для чтения JSON-файлов, что обеспечивает более удобный и безопасный способ работы с данными конфигурации. Данные о локалях хранятся в файле `locales.json` и используются для настройки рекламных кампаний AliExpress.

## Функции

### `get_locales`

```python
def get_locales(locales_path: Path | str) -> list[dict[str, str]] | None:
    """
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
```

**Описание**: Загружает данные о локалях из JSON-файла.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей с парами локаль и валюта. Возвращает `None`, если данные не найдены.

**Примеры**:

Пример использования функции `get_locales`:

```python
from pathlib import Path
from src.suppliers.aliexpress.utils.locales import get_locales

locales_path = Path('src/suppliers/aliexpress/utils/locales.json')
locales = get_locales(locales_path)

if locales:
    print(locales)