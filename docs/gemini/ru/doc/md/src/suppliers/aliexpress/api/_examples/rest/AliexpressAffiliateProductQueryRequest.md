# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Обзор

Модуль `AliexpressAffiliateProductQueryRequest` предоставляет класс для запроса информации о продуктах на платформе AliExpress через API.  Он наследуется от базового класса `RestApi` и позволяет задавать различные параметры фильтрации и сортировки для получения необходимых данных.

## Классы

### `AliexpressAffiliateProductQueryRequest`

**Описание**: Класс, представляющий запрос к API AliExpress для получения информации о продуктах.

**Методы**:

- `__init__`

    **Описание**: Инициализирует объект запроса.

    **Параметры**:
    - `domain` (str, optional): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
    - `port` (int, optional): Порт API. По умолчанию `80`.
    - `app_signature` (None, optional): Подпись приложения.
    - `category_ids` (None, optional): Список идентификаторов категорий.
    - `delivery_days` (None, optional): Количество дней доставки.
    - `fields` (None, optional): Список полей для возврата.
    - `keywords` (None, optional): Список ключевых слов для поиска.
    - `max_sale_price` (None, optional): Максимальная цена продажи.
    - `min_sale_price` (None, optional): Минимальная цена продажи.
    - `page_no` (None, optional): Номер страницы результатов.
    - `page_size` (None, optional): Размер страницы результатов.
    - `platform_product_type` (None, optional): Тип продукта на платформе.
    - `ship_to_country` (None, optional): Страна доставки.
    - `sort` (None, optional): Сортировка результатов.
    - `target_currency` (None, optional): Целевая валюта.
    - `target_language` (None, optional): Целевой язык.
    - `tracking_id` (None, optional): Идентификатор отслеживания.

    **Возвращает**:
    - `None`


- `getapiname`

    **Описание**: Возвращает имя API-метода.

    **Параметры**:
    - `None`

    **Возвращает**:
    - `str`: Имя API-метода `aliexpress.affiliate.product.query`.