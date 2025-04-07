# Модуль для загрузки данных о локалях из JSON-файла

## Обзор

Модуль `locales` предназначен для загрузки и обработки данных о локалях из JSON-файла. Он предоставляет функцию `get_locales` для получения списка словарей, содержащих информацию о соответствии локалей и валют.

## Подробнее

Этот модуль используется для получения данных о локалях, необходимых для работы с кампаниями AliExpress. Он загружает данные из JSON-файла, расположенного в директории `src/suppliers/aliexpress/utils`.

## Функции

### `get_locales`

```python
def get_locales(locales_path: Path | str) -> list[dict[str, str]] | None:
    """Функция загружает данные о локалях из JSON-файла.

    Args:
        path (Path): Путь к JSON-файлу, содержащему данные о локалях.

    Returns:
        list[dict[str, str]]: Список словарей с парами локаль и валюта.
        None: Возвращает `None`, если данные о локалях не найдены.

    Example:
        >>> from src.suppliers.aliexpress.utils.locales import get_locales
        >>> from pathlib import Path
        >>> path_to_locales = Path('/path/to/locales.json')
        >>> locales = get_locales(path_to_locales)
        >>> print(locales)
        [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
    """
```

**Как работает функция**:

1.  Функция `get_locales` принимает путь к JSON-файлу с данными о локалях.
2.  Использует функцию `j_loads_ns` для загрузки данных из JSON-файла.
3.  Извлекает список локалей из загруженных данных (предположительно, поле `locales`).
4.  Если список локалей существует, функция возвращает его, иначе возвращает `None`.

```ascii
    A[Начало: Получение пути к файлу локалей]
    |
    B[Загрузка данных из JSON-файла с использованием j_loads_ns]
    |
    C[Извлечение списка локалей из загруженных данных]
    |
    D[Проверка наличия списка локалей]
    |
    E[Возврат списка локалей]
    |
    F[Конец: Возврат None, если список локалей отсутствует]
```

**Примеры**:

```python
from pathlib import Path
from src.suppliers.aliexpress.utils.locales import get_locales

# Пример 1: Успешная загрузка локалей
locales_path = Path('path/to/your/locales.json')  # Замените на реальный путь к файлу
locales = get_locales(locales_path)
if locales:
    print("Локали успешно загружены:", locales)
else:
    print("Не удалось загрузить локали.")

# Пример 2: Файл локалей не найден или пуст
locales_path = Path('nonexistent_locales.json')  # Замените на несуществующий путь
locales = get_locales(locales_path)
if locales:
    print("Локали успешно загружены:", locales)
else:
    print("Файл не найден или не содержит данных о локалях.")
```

## Переменные

### `locales`

```python
locales: list[dict[str, str]] | None = get_locales (gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json') # defined locales for campaigns
```

**Описание**:
- `locales` (list[dict[str, str]] | None):  Переменная содержит список словарей, представляющих локали для кампаний, или `None`, если загрузка не удалась. Инициализируется вызовом функции `get_locales` с указанием пути к файлу `locales.json`.