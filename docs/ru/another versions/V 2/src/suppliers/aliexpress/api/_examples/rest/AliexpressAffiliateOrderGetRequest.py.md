# Документация для `AliexpressAffiliateOrderGetRequest.py`

## Оглавление
1. [Обзор](#обзор)
2. [Классы](#классы)
    - [`AliexpressAffiliateOrderGetRequest`](#aliexpressaffiliateordergetrequest)
3. [Функции](#функции)
    - [`getapiname`](#getapiname)

## Обзор

Файл `AliexpressAffiliateOrderGetRequest.py` содержит класс `AliexpressAffiliateOrderGetRequest`, который используется для выполнения запроса на получение информации о заказе через AliExpress Affiliate API. Этот класс наследуется от `RestApi` и предназначен для работы с REST API AliExpress.

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс, представляющий запрос на получение информации о заказе через AliExpress Affiliate API.

**Методы**:
- `__init__`: Конструктор класса, инициализирует параметры запроса.
- `getapiname`: Возвращает имя API метода.

#### `__init__`
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    """
```
**Описание**: Конструктор класса, инициализирует параметры запроса, включая домен и порт API, а также устанавливает значения по умолчанию для `app_signature`, `fields`, и `order_ids`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

#### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Имя API метода ('aliexpress.affiliate.order.get').
    """
```
**Описание**: Метод возвращает имя API метода, который используется для получения информации о заказе.

**Возвращает**:
- `str`: Имя API метода (`aliexpress.affiliate.order.get`).

## Функции

### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Имя API метода ('aliexpress.affiliate.order.get').
    """
```
**Описание**: Метод возвращает имя API метода, который используется для получения информации о заказе.

**Возвращает**:
- `str`: Имя API метода (`aliexpress.affiliate.order.get`).