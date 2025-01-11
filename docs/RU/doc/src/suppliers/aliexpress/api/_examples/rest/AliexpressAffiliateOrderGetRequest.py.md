# Модуль `AliexpressAffiliateOrderGetRequest`

## Обзор

Модуль `AliexpressAffiliateOrderGetRequest` предоставляет класс `AliexpressAffiliateOrderGetRequest`, который используется для отправки запроса на получение информации о заказе через API AliExpress.

## Оглавление

1. [Классы](#Классы)
    - [`AliexpressAffiliateOrderGetRequest`](#AliexpressAffiliateOrderGetRequest)
2. [Функции](#Функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс для формирования запроса на получение информации о заказе. Наследуется от класса `RestApi`.

**Методы**:
- `__init__`: Инициализация экземпляра класса.
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

**Описание**: Конструктор класса `AliexpressAffiliateOrderGetRequest`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

**Возвращает**:
- `None`: Метод ничего не возвращает.

## Функции

### `getapiname`

```python
def getapiname(self) -> str:
    """
    Args:
        self: Экземпляр класса `AliexpressAffiliateOrderGetRequest`

    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.order.get'.
    """
```
**Описание**: Метод для получения имени API метода.

**Параметры**:
- `self`: Экземпляр класса `AliexpressAffiliateOrderGetRequest`.

**Возвращает**:
- `str`: Возвращает имя API метода `'aliexpress.affiliate.order.get'`.