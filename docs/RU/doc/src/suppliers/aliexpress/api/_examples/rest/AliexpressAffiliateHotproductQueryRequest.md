# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateHotproductQueryRequest`, представляющий запрос к API для получения горячих продуктов на AliExpress. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateHotproductQueryRequest`

**Описание**: Класс для создания запросов к API AliExpress для получения горячих продуктов.

**Атрибуты**:

- `app_signature`:  Значение подписи приложения.
- `category_ids`: Список идентификаторов категорий.
- `delivery_days`: Количество дней доставки.
- `fields`: Список полей для возврата.
- `keywords`: Ключевые слова для поиска.
- `max_sale_price`: Максимальная цена продажи.
- `min_sale_price`: Минимальная цена продажи.
- `page_no`: Номер страницы (для пагинации).
- `page_size`: Размер страницы (для пагинации).
- `platform_product_type`: Тип продукта на платформе.
- `ship_to_country`: Страна доставки.
- `sort`: Сортировка результатов.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.
- `domain`: Домен API (по умолчанию `api-sg.aliexpress.com`).
- `port`: Порт API (по умолчанию `80`).

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Конструктор класса. Инициализирует атрибуты класса и родительский класс `RestApi`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.


#### `getapiname(self)`

**Описание**: Возвращает имя API.

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.hotproduct.query`).


## Функции

(В данном модуле нет функций, только класс)


## Примеры использования (если есть):

```python
# Пример использования (если есть):
# from AliexpressAffiliateHotproductQueryRequest import AliexpressAffiliateHotproductQueryRequest
# request = AliexpressAffiliateHotproductQueryRequest()
# request.keywords = "some keywords"
# result = request.execute()  # Вызов метода execute() отсутствует в коде.  Предполагается, что это метод родительского класса
# print(result)
```

**Примечание:**  Код содержит примеры, однако, для полноценной демонстрации, необходимы дополнительные фрагменты кода, связанные с методами, которые не определены в данном модуле, например, `execute()`.  Также желательно добавить примеры, как настраивать параметры.