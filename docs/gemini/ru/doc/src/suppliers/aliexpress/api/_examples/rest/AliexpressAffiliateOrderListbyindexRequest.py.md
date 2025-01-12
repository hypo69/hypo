# AliexpressAffiliateOrderListbyindexRequest

## Обзор

Модуль `AliexpressAffiliateOrderListbyindexRequest` предоставляет класс `AliexpressAffiliateOrderListbyindexRequest`, который используется для получения списка заказов аффилиата AliExpress с помощью API. Этот класс является частью более широкой системы для работы с API AliExpress.

## Оглавление

1. [Классы](#Классы)
    - [AliexpressAffiliateOrderListbyindexRequest](#AliexpressAffiliateOrderListbyindexRequest)
2. [Функции](#Функции)
    - [getapiname](#getapiname)

## Классы

### `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс для выполнения запроса на получение списка заказов аффилиата AliExpress по индексу.

**Методы**:

- `__init__`: Инициализирует экземпляр класса с параметрами домена и порта.
- `getapiname`: Возвращает имя API метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80) -> None:
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    
    Returns:
        None: Метод ничего не возвращает.
    """
```

**Описание**: Инициализирует новый экземпляр класса `AliexpressAffiliateOrderListbyindexRequest`. Устанавливает домен и порт для запросов API, а также инициализирует атрибуты запроса как `None`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.order.listbyindex'.
    """
```

**Описание**: Метод возвращает имя API метода для запроса списка заказов.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Имя API метода: `aliexpress.affiliate.order.listbyindex`.

## Функции

### `getapiname`
**Описание**: Метод возвращает имя API метода для запроса списка заказов.

```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.order.listbyindex'.
    """
```

**Параметры**:
- Нет

**Возвращает**:
- `str`: Имя API метода: `aliexpress.affiliate.order.listbyindex`.