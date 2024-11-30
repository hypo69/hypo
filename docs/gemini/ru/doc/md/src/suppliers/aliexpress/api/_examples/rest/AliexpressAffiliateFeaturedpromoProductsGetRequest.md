# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, предназначенный для работы с API AliExpress. Он позволяет получать информацию о продуктах, участвующих в специальных рекламных акциях. Класс наследуется от `RestApi`.

## Оглавление

- [Модуль `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#модуль-aliexpressaffiliatefeaturedpromoproductsgetrequest)
    - [Класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`](#класс-aliexpressaffiliatefeaturedpromoproductsgetrequest)
        - [Метод `__init__`](#метод-init)
        - [Метод `getapiname`](#метод-getapiname)

## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс для получения списка продуктов, участвующих в специальных рекламных акциях на AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateFeaturedpromoProductsGetRequest`.

**Параметры**:

- `domain` (str, optional): Домен API (по умолчанию `"api-sg.aliexpress.com"`).
- `port` (int, optional): Порт API (по умолчанию `80`).

**Атрибуты**:

- `app_signature`: Значение.
- `category_id`: Значение.
- `country`: Значение.
- `fields`: Значение.
- `page_no`: Значение.
- `page_size`: Значение.
- `promotion_end_time`: Значение.
- `promotion_name`: Значение.
- `promotion_start_time`: Значение.
- `sort`: Значение.
- `target_currency`: Значение.
- `target_language`: Значение.
- `tracking_id`: Значение.

#### `getapiname`

**Описание**: Возвращает имя API-метода.

**Возвращает**:

- `str`: Имя API-метода (`"aliexpress.affiliate.featuredpromo.products.get"`).