# Модуль `AliexpressAffiliateFeaturedpromoGetRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, который используется для отправки запросов к API AliExpress для получения информации об акциях.

## Оглавление

1. [Классы](#классы)
    - [`AliexpressAffiliateFeaturedpromoGetRequest`](#aliexpressaffiliatefeaturedpromogetrequest)
2. [Функции](#функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс для создания запроса на получение информации об акциях.

**Методы**:

- `__init__`: Инициализирует объект класса с доменом и портом.
- `getapiname`: Возвращает имя API метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80)
```

**Описание**: Конструктор класса `AliexpressAffiliateFeaturedpromoGetRequest`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

#### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Метод возвращает имя API метода.

**Возвращает**:
- `str`: Имя API метода `'aliexpress.affiliate.featuredpromo.get'`.

## Функции

### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Метод возвращает имя API метода.

**Возвращает**:
- `str`: Имя API метода `'aliexpress.affiliate.featuredpromo.get'`.