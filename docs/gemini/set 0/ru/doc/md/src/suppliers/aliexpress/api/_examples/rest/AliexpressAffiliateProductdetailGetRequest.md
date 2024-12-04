# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductdetailGetRequest.py`

## Обзор

Модуль `AliexpressAffiliateProductdetailGetRequest` предоставляет класс для работы с API AliExpress, позволяя получать детали продукта для аффилиатных программ.  Он наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**:  Класс для получения деталей продукта на AliExpress для аффилиатных программ.  Он настраивает параметры запроса и предоставляет имя API.

**Атрибуты**:

- `app_signature`:  Значение приложения.
- `country`: Страна.
- `fields`: Поля для возвращаемых данных.
- `product_ids`: Идентификаторы продуктов.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект класса `AliexpressAffiliateProductdetailGetRequest`.

**Параметры**:

- `domain` (str, опционально): Домен API (по умолчанию `api-sg.aliexpress.com`).
- `port` (int, опционально): Порт API (по умолчанию `80`).


#### `getapiname(self)`

**Описание**: Возвращает имя API.

**Возвращает**:
- str: Название API `aliexpress.affiliate.productdetail.get`.