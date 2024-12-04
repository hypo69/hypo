# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductSmartmatchRequest`, представляющий собой запрос к API AliExpress для поиска продуктов.  Этот класс наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateProductSmartmatchRequest`](#модуль-aliexpressaffiliateproductsmartmatchrequest)
- [Класс `AliexpressAffiliateProductSmartmatchRequest`](#класс-aliexpressaffiliateproductsmartmatchrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс `AliexpressAffiliateProductSmartmatchRequest` представляет собой запрос к API AliExpress для поиска продуктов по умному совпадению. Он настраивает параметры запроса и предоставляет имя API.

### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateProductSmartmatchRequest`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:

- Не имеет возвращаемого значения.


### Метод `getapiname`

**Описание**: Возвращает имя API запроса.

**Возвращает**:

- str: Имя API запроса, в данном случае `'aliexpress.affiliate.product.smartmatch'`.