# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, который представляет собой запрос к API AliExpress для получения горячих продуктов. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateHotproductQueryRequest`](#модуль-aliexpressaffiliatehotproductqueryrequest)
- [Класс `AliexpressAffiliateHotproductQueryRequest`](#класс-aliexpressaffiliatehotproductqueryrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateHotproductQueryRequest`

**Описание**: Класс представляет собой запрос к API AliExpress для получения горячих продуктов. Он настраивает параметры запроса и предоставляет имя API.

### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateHotproductQueryRequest`.

**Параметры**:
- `domain` (str, optional): Домен API (по умолчанию "api-sg.aliexpress.com").
- `port` (int, optional): Порт API (по умолчанию 80).

**Атрибуты**:
- `app_signature`:  
- `category_ids`:  
- `delivery_days`:  
- `fields`:  
- `keywords`:  
- `max_sale_price`:  
- `min_sale_price`:  
- `page_no`:  
- `page_size`:  
- `platform_product_type`:  
- `ship_to_country`:  
- `sort`:  
- `target_currency`:  
- `target_language`:  
- `tracking_id`: 


### Метод `getapiname`

**Описание**: Возвращает имя API.

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.hotproduct.query`).