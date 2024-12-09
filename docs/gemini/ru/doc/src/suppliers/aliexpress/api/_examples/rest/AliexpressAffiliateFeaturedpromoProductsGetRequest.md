# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, представляющий запрос к API AliExpress для получения данных о продуктах с выделенными промоакциями. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.


## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс представляет запрос к API AliExpress для получения данных о продуктах с выделенными промоакциями.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект класса.

**Параметры**:
- `domain` (str, опционально): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, опционально): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`


#### `getapiname(self)`

**Описание**: Возвращает имя API.

**Параметры**:
- Нет

**Возвращает**:
- str: Имя API `"aliexpress.affiliate.featuredpromo.products.get"`.


**Атрибуты**:

- `app_signature`: (тип не указан)
- `category_id`: (тип не указан)
- `country`: (тип не указан)
- `fields`: (тип не указан)
- `page_no`: (тип не указан)
- `page_size`: (тип не указан)
- `promotion_end_time`: (тип не указан)
- `promotion_name`: (тип не указан)
- `promotion_start_time`: (тип не указан)
- `sort`: (тип не указан)
- `target_currency`: (тип не указан)
- `target_language`: (тип не указан)
- `tracking_id`: (тип не указан)


## Функции


(В данном модуле нет функций, кроме методов класса)