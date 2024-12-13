# Модуль `AliexpressAffiliateOrderListRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderListRequest`, который используется для запроса списка заказов через AliExpress Affiliate API.

## Оглавление

- [Классы](#Классы)
    - [`AliexpressAffiliateOrderListRequest`](#AliexpressAffiliateOrderListRequest)
        - [`__init__`](#__init__)
        - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс для запроса списка заказов через AliExpress Affiliate API.

**Методы**:
- [`__init__`](#__init__): Конструктор класса.
- [`getapiname`](#getapiname): Возвращает имя API-метода.

#### `__init__`
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80) -> None:
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.

    Returns:
        None: Функция ничего не возвращает.
    """
```
**Описание**: Конструктор класса `AliexpressAffiliateOrderListRequest`. Инициализирует параметры запроса.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Метод ничего не возвращает.

#### `getapiname`
```python
def getapiname(self) -> str:
    """
    Args:
        self: Экземпляр класса.

    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.order.list'.
    """
```
**Описание**: Возвращает имя API-метода для запроса списка заказов.

**Параметры**:
- `self`: Экземпляр класса.

**Возвращает**:
- `str`: Имя API метода - `"aliexpress.affiliate.order.list"`.