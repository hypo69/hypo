# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, представляющий запрос к API AliExpress для получения информации о популярных продуктах. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateHotproductQueryRequest`](#модуль-aliexpressaffiliatehotproductqueryrequest)
  - [Класс `AliexpressAffiliateHotproductQueryRequest`](#класс-aliexpressaffiliatehotproductqueryrequest)
    - [`__init__`](#init)
    - [`getapiname`](#getapiname)


## Класс `AliexpressAffiliateHotproductQueryRequest`

**Описание**: Класс `AliexpressAffiliateHotproductQueryRequest` представляет запрос к API AliExpress для получения информации о популярных продуктах. Он наследуется от `RestApi` и предоставляет набор параметров для настройки запроса.

### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateHotproductQueryRequest`.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

**Возвращает**:
- `None`: Не возвращает значение.

### `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.hotproduct.query`).


**Примечания**:
- Дополнительные параметры класса (например, `app_signature`, `category_ids`, и т.д.) задаются при инициализации объекта и используются для формирования запроса к API.
- Модуль использует соглашение именования параметров, соответствующее стандартам REST API.
- Требуется библиотека `RestApi` (предполагается, что она импортирована из `..base`).