# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Обзор

Модуль `AliexpressAffiliateProductQueryRequest` предоставляет класс для работы с API AliExpress для получения информации о продуктах, связанных с программой аффилированного маркетинга. Класс наследуется от `RestApi` и предоставляет методы для настройки запроса и получения данных.

## Оглавление

- [Модуль `AliexpressAffiliateProductQueryRequest`](#модуль-aliexpressaffiliateproductqueryrequest)
    - [Класс `AliexpressAffiliateProductQueryRequest`](#класс-aliexpressaffiliateproductqueryrequest)
        - [Метод `__init__`](#метод-init)
        - [Метод `getapiname`](#метод-getapiname)


## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**: Класс для запроса информации о продуктах AliExpress в рамках аффилированной программы.

**Методы**:

- `__init__`
- `getapiname`


#### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateProductQueryRequest`.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API AliExpress.
- `port` (int, опционально, по умолчанию 80): Порт API AliExpress.


**Возвращает**:
- None


#### Метод `getapiname`

**Описание**: Возвращает имя API-метода для запроса.

**Параметры**:

- Нет

**Возвращает**:
- str: Название API-метода ('aliexpress.affiliate.product.query').