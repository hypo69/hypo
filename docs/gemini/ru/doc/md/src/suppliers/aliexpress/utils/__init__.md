# Модуль hypotez/src/suppliers/aliexpress/utils

## Обзор

Этот модуль предоставляет утилиты для работы с данными AliExpress.  В нем находятся функции для извлечения идентификаторов продуктов, перевода ссылок в HTTPS и работы с локалями.


## Функции

### `extract_prod_ids`

**Описание**: Функция извлекает идентификаторы продуктов из входных данных.

**Параметры**:
- `data` (dict): Словарь данных, содержащий информацию о продуктах.

**Возвращает**:
- `list`: Список идентификаторов продуктов.


### `ensure_https`

**Описание**: Функция преобразует URL-адреса в HTTPS, если они не HTTPS.

**Параметры**:
- `url` (str): URL-адрес.

**Возвращает**:
- `str`: URL-адрес в формате HTTPS.


### `locales`

**Описание**: Функция возвращает список локалей.

**Возвращает**:
- `list`: Список локалей.


## Использование

```python
# Пример использования функции extract_prod_ids
from hypotez.src.suppliers.aliexpress.utils import extract_prod_ids

data = {
    'products': [
        {'id': '123'},
        {'id': '456'},
    ]
}

product_ids = extract_prod_ids(data)
print(product_ids)

# Пример использования функции ensure_https
from hypotez.src.suppliers.aliexpress.utils import ensure_https

url = 'http://example.com'
https_url = ensure_https(url)
print(https_url)

# Пример использования функции locales
from hypotez.src.suppliers.aliexpress.utils import locales
print(locales)
```

## Модульные переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev', 'prod').


```python
MODE = 'dev'
```

##  Структура модуля

Модуль `hypotez/src/suppliers/aliexpress/utils` состоит из следующих модулей:

- `extract_product_id`: содержит функцию `extract_prod_ids`.
- `ensure_https`: содержит функцию `ensure_https`.
- `locales`: содержит функцию `locales`.



```
```
```