# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, представляющий запрос к API AliExpress для получения данных о продуктах с акциями.  Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс представляет собой запрос к API AliExpress для получения данных о продуктах с акциями. Он предоставляет методы для инициализации запроса и получения имени API.

**Атрибуты**:

- `app_signature`: Значение для подписи приложения.
- `category_id`: Идентификатор категории.
- `country`: Страна.
- `fields`: Поля.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `promotion_end_time`: Дата окончания акции.
- `promotion_name`: Название акции.
- `promotion_start_time`: Дата начала акции.
- `sort`: Сортировка.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.


**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:
-  Нет

**Возвращает**:
- str: Имя API  `aliexpress.affiliate.featuredpromo.products.get`.