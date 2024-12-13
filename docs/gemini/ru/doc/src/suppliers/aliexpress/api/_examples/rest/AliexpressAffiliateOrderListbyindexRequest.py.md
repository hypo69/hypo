# Модуль `AliexpressAffiliateOrderListbyindexRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, который используется для создания запроса к API AliExpress для получения списка заказов аффилиата по индексу.

## Оглавление

1. [Классы](#классы)
   - [`AliexpressAffiliateOrderListbyindexRequest`](#AliexpressAffiliateOrderListbyindexRequest)
2. [Функции](#функции)
   - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateOrderListbyindexRequest`

**Описание**: Класс для создания запроса на получение списка заказов аффилиата по индексу.

**Методы**:

- `__init__`: Инициализирует объект класса `AliexpressAffiliateOrderListbyindexRequest`.
- `getapiname`: Возвращает имя API для данного запроса.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
```

**Описание**: Инициализирует объект класса `AliexpressAffiliateOrderListbyindexRequest`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Возвращает имя API для данного запроса.

**Параметры**:
- `self` (AliexpressAffiliateOrderListbyindexRequest): Экземпляр класса.

**Возвращает**:
- `str`: Имя API - `aliexpress.affiliate.order.listbyindex`.

## Функции

### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Возвращает имя API для данного запроса.

**Параметры**:
- `self` (AliexpressAffiliateOrderListbyindexRequest): Экземпляр класса.

**Возвращает**:
- `str`: Имя API - `aliexpress.affiliate.order.listbyindex`.