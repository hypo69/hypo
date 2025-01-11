# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductdetailGetRequest.py`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateProductdetailGetRequest`, предназначенный для взаимодействия с API AliExpress для получения деталей продукта.  Он наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**:  Класс для запроса деталей продукта через API AliExpress Affiliate.

**Методы**:

- `__init__`: Конструктор класса.


#### `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateProductdetailGetRequest`.

**Параметры**:

- `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально, по умолчанию 80): Порт API.


**Атрибуты**:

- `app_signature`:  (None) - Подпись приложения.
- `country`:  (None) - Страна.
- `fields`:  (None) - Поля.
- `product_ids`:  (None) - Идентификаторы продуктов.
- `target_currency`: (None) - Ценовая валюта.
- `target_language`: (None) - Целевой язык.
- `tracking_id`: (None) - Идентификатор отслеживания.



#### `getapiname`

**Описание**: Возвращает имя API метода.

**Возвращает**:
- `str`: Имя API метода (`aliexpress.affiliate.productdetail.get`).