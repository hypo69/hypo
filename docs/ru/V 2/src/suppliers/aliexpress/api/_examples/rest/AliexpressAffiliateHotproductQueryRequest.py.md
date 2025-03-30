# Модуль `aliexpress.affiliate.hotproduct.query`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, который используется для выполнения запроса к API AliExpress для получения списка горячих товаров.

## Оглавление

1. [Классы](#классы)
    - [`AliexpressAffiliateHotproductQueryRequest`](#aliexpressaffiliatehotproductqueryrequest)

## Классы

### `AliexpressAffiliateHotproductQueryRequest`

**Описание**:
Класс `AliexpressAffiliateHotproductQueryRequest` представляет собой запрос к API AliExpress для получения списка горячих товаров. Он наследуется от класса `RestApi`.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса. Инициализирует экземпляр класса с заданным доменом и портом.
- `getapiname(self)`: Возвращает имя API метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    """
```

**Описание**:
Конструктор класса `AliexpressAffiliateHotproductQueryRequest`. Инициализирует экземпляр класса с заданным доменом и портом, а также устанавливает значения атрибутов запроса в `None`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.hotproduct.query'.
    """
```

**Описание**:
Метод возвращает имя API метода, которое используется для выполнения запроса.

**Параметры**:
- `self` (AliexpressAffiliateHotproductQueryRequest): Экземпляр класса.

**Возвращает**:
- `str`: Имя API метода `"aliexpress.affiliate.hotproduct.query"`.