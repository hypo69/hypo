# Модуль parse_data_types

## Обзор

Модуль `parse_data_types` определяет типы данных входящих данных и преобразует их в требуемый формат.

## Функции

### `parse_data`

**Описание**: Парсит входящие данные, определяет тип и возвращает преобразованные данные.

**Параметры**:

- `data` (dict): Словарь данных.

**Возвращает**:

- `dict | None`: Преобразованный словарь данных или `None`, если входные данные некорректны или не поддерживаются.

**Вызывает исключения**:

- `TypeError`: Если тип данных входных данных не соответствует ожидаемому.
- `ValueError`: При некорректном формате входных данных.
- `json.JSONDecodeError`: При ошибке декодирования JSON.

```
```python
def parse_data(data: dict) -> dict | None:
    """
    Args:
        data (dict): Словарь данных.

    Returns:
        dict | None: Преобразованный словарь данных или None, если входные данные некорректны или не поддерживаются.

    Raises:
        TypeError: Если тип данных входных данных не соответствует ожидаемому.
        ValueError: При некорректном формате входных данных.
        json.JSONDecodeError: При ошибке декодирования JSON.
    """
    try:
        # Обработка различных типов данных
        if isinstance(data, dict):
            # Парсинг JSON
            return data  # или преобразовать dict к нужному формату
        elif isinstance(data, str):
          try:
            return json.loads(data)
          except json.JSONDecodeError as ex:
            raise ValueError(f"Не удалось декодировать JSON: {ex}") from ex
        else:
            raise TypeError(f"Неподдерживаемый тип данных: {type(data)}")
    except (TypeError, ValueError) as ex:
        raise ValueError(f"Ошибка при обработке данных: {ex}") from ex


```

## Поддержка

Подробная документация по использованию модуля и обработке различных типов данных будет дополнена в ближайшее время.


```