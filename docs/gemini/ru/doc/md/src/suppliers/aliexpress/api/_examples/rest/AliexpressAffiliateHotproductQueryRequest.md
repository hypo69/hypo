# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, который представляет запрос к API AliExpress для получения горячих продуктов по партнерской программе.  Класс наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateHotproductQueryRequest`

**Описание**:  Класс для формирования запросов к API AliExpress для получения горячих продуктов по партнерской программе.

**Инициализация (`__init__`)**:

**Параметры**:
- `domain` (str, опционально, по умолчанию `"api-sg.aliexpress.com"`): Домен API.
- `port` (int, опционально, по умолчанию `80`): Порт API.

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


**Методы**:

#### `getapiname`

**Описание**: Возвращает имя API.

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.hotproduct.query`).