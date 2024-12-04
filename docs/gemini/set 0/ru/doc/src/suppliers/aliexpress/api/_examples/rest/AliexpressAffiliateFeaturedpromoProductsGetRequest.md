# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Данный модуль предоставляет класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, который реализует REST API для получения данных о продуктах с акциями на AliExpress.  Этот класс наследуется от базового класса `RestApi`.

## Оглавление

- [Модуль `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#модуль-aliexpressaffiliatefeaturedpromo產品sgetrequest)
    - [Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#класс-aliexpressaffiliatefeaturedpromoproductsgetrequest)
        - [Метод `__init__`](#метод-init)
        - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс представляет собой запрос для получения данных о продуктах с акциями на AliExpress.

### Метод `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Доменное имя API.
- `port` (int, опционально, по умолчанию 80): Порт API.

**Атрибуты**:

- `app_signature`: (не описано)
- `category_id`: (не описано)
- `country`: (не описано)
- `fields`: (не описано)
- `page_no`: (не описано)
- `page_size`: (не описано)
- `promotion_end_time`: (не описано)
- `promotion_name`: (не описано)
- `promotion_start_time`: (не описано)
- `sort`: (не описано)
- `target_currency`: (не описано)
- `target_language`: (не описано)
- `tracking_id`: (не описано)


**Возвращает**:
- `None`

**Вызывает исключения**:
- (Нет описания)


### Метод `getapiname`

**Описание**: Возвращает имя API-метода.

**Параметры**:
- (Нет параметров)

**Возвращает**:
- str: Имя API-метода "aliexpress.affiliate.featuredpromo.products.get".

**Вызывает исключения**:
- (Нет описания)