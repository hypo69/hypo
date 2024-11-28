# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, представляющий запрос для получения горячих продуктов на AliExpress через API. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль `AliexpressAffiliateHotproductQueryRequest`](#модуль-aliexpressaffiliatehotproductqueryrequest)
- [Класс `AliexpressAffiliateHotproductQueryRequest`](#класс-aliexpressaffiliatehotproductqueryrequest)
    - [Метод `__init__`](#метод-init)
    - [Метод `getapiname`](#метод-getapiname)

## Класс `AliexpressAffiliateHotproductQueryRequest`

**Описание**:  Класс `AliexpressAffiliateHotproductQueryRequest` представляет собой запрос для получения горячих продуктов на AliExpress. Наследуется от базового класса `RestApi`.

**Атрибуты**:

- `app_signature`: (Тип данных не указан)  Параметр приложения.
- `category_ids`: (Тип данных не указан) Список идентификаторов категорий.
- `delivery_days`: (Тип данных не указан)  Срок доставки.
- `fields`: (Тип данных не указан) Поля для возврата.
- `keywords`: (Тип данных не указан)  Ключевые слова для поиска.
- `max_sale_price`: (Тип данных не указан) Максимальная цена продажи.
- `min_sale_price`: (Тип данных не указан) Минимальная цена продажи.
- `page_no`: (Тип данных не указан) Номер страницы.
- `page_size`: (Тип данных не указан) Размер страницы.
- `platform_product_type`: (Тип данных не указан) Тип продукта на платформе.
- `ship_to_country`: (Тип данных не указан) Страна доставки.
- `sort`: (Тип данных не указан) Сортировка результатов.
- `target_currency`: (Тип данных не указан) Целевая валюта.
- `target_language`: (Тип данных не указан) Целевой язык.
- `tracking_id`: (Тип данных не указан) Идентификатор отслеживания.


### Метод `__init__`

**Описание**: Инициализирует объект класса `AliexpressAffiliateHotproductQueryRequest`.

**Параметры**:

- `domain` (строка, по умолчанию `"api-sg.aliexpress.com"`): Домен API.
- `port` (целое число, по умолчанию `80`): Порт API.

**Возвращает**:  None

### Метод `getapiname`

**Описание**: Возвращает имя API.

**Параметры**: Нет

**Возвращает**: Строка - имя API (`aliexpress.affiliate.hotproduct.query`).

**Примечания**: Метод предназначен для получения имени API, используемого для запроса.