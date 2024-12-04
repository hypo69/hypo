# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Обзор

Модуль `AliexpressAffiliateProductQueryRequest` предоставляет класс для запроса информации о продуктах на AliExpress через API. Он наследуется от базового класса `RestApi`.  Этот класс предназначен для создания запросов на поиск продуктов, связанных с партнерской программой AliExpress.

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**:  Класс для создания запросов на поиск продуктов на AliExpress через API, ориентированный на партнерскую программу.

**Атрибуты**:

- `app_signature`:  (тип: `None`) Подпись приложения.
- `category_ids`: (тип: `None`) Список идентификаторов категорий для фильтрации результатов.
- `delivery_days`: (тип: `None`)  Количество дней доставки.
- `fields`: (тип: `None`) Список требуемых полей в ответе.
- `keywords`: (тип: `None`)  Ключевые слова для поиска.
- `max_sale_price`: (тип: `None`) Максимальная цена продукта.
- `min_sale_price`: (тип: `None`) Минимальная цена продукта.
- `page_no`: (тип: `None`) Номер страницы результатов поиска.
- `page_size`: (тип: `None`) Размер страницы результатов поиска.
- `platform_product_type`: (тип: `None`) Тип продукта на платформе.
- `ship_to_country`: (тип: `None`) Страна доставки.
- `sort`: (тип: `None`)  Параметр сортировки результатов.
- `target_currency`: (тип: `None`) Целевая валюта.
- `target_language`: (тип: `None`) Целевой язык.
- `tracking_id`: (тип: `None`) Идентификатор отслеживания.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует экземпляр класса.

**Параметры**:
- `domain` (str, опционально "api-sg.aliexpress.com"): Домен API.
- `port` (int, опционально 80): Порт API.

**Возвращает**:
-  None (Возвращает `None`, поскольку инициализирует объект)


#### `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Параметры**:
-  Нет

**Возвращает**:
- str: Имя API-метода `aliexpress.affiliate.product.query`.