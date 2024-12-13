# Модуль `aliexpress.affiliate.hotproduct.query`

## Обзор

Модуль содержит пример использования API для запроса горячих товаров Aliexpress через REST.

## Содержание

- [Классы](#Классы)
    - [`AliexpressAffiliateHotproductQueryRequest`](#AliexpressAffiliateHotproductQueryRequest)

## Классы

### `AliexpressAffiliateHotproductQueryRequest`

**Описание**: Класс для выполнения запроса горячих товаров через API Aliexpress.

**Методы**:
- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    
    """
```

**Описание**: Конструктор класса `AliexpressAffiliateHotproductQueryRequest`. Инициализирует экземпляр класса с заданным доменом и портом, а также устанавливает значения параметров запроса в `None`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API 'aliexpress.affiliate.hotproduct.query'.
    """
```

**Описание**: Метод возвращает имя API, которое используется для запроса горячих товаров.

**Возвращает**:
- `str`: Возвращает имя API 'aliexpress.affiliate.hotproduct.query'.