# Модуль `locales`

## Обзор

Модуль `locales` предназначен для загрузки и обработки данных о локалях из JSON-файла. Он предоставляет функцию `get_locales` для чтения данных о локалях и валютах, которые используются в кампаниях.

## Оглавление

- [Функции](#функции)
    - [`get_locales`](#get_locales)

## Функции

### `get_locales`

**Описание**: Загружает данные о локалях из JSON-файла.

**Параметры**:
- `locales_path` (Path | str): Путь к JSON-файлу, содержащему данные о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей, содержащих пары "локаль-валюта", или `None`, если данные не найдены.

**Примеры использования**:
```python
>>> from pathlib import Path
>>> from src.suppliers.aliexpress.utils.locales import get_locales
>>> locales = get_locales(Path('/path/to/locales.json'))
>>> print(locales)
[{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
```