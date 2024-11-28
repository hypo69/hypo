# Модуль `hypotez/src/suppliers/aliexpress/utils/locales.py`

## Обзор

Модуль `locales.py` предназначен для загрузки данных о локалях из файла JSON.  Он содержит функцию `load_locales_data` для работы с данными локалей и валют.

## Функции

### `get_locales`

**Описание**: Загружает данные о локалях из файла JSON.

**Параметры**:
- `locales_path` (Path | str): Путь к файлу JSON с данными о локалях.

**Возвращает**:
- `list[dict[str, str]] | None`: Список словарей с парами "локаль-валюта". Возвращает `None`, если данные не загружены или файл не найден.

**Примеры**:
```python
from src.suppliers.aliexpress.utils.locales import get_locales
from pathlib import Path

locales = get_locales(Path('/path/to/locales.json'))
print(locales)
```

**Примечания**: Использует функцию `j_loads_ns` для парсинга JSON.  Возвращает значение `locales` из загруженного словаря или `None`, если поле `locales` отсутствует в загруженных данных.

## Постоянные значения

### `locales`

**Описание**: Список словарей с парами "локаль-валюта", загруженный из файла `locales.json` в корневой директории `suppliers/aliexpress/utils`.

**Тип**: `list[dict[str, str]] | None`

**Примечания**: Значение этой переменной инициализируется в момент выполнения и может быть `None` если файл не найден или JSON-данные неверны.