```markdown
# Файл: `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

## Модуль: `src.suppliers.aliexpress.api._examples.rest`

**Описание:** Данный модуль содержит класс `AliexpressAffiliateProductQueryRequest`, представляющий собой запрос к API AliExpress для получения информации о продуктах, связанных с партнерской программой.

**Дата создания:** 2021.05.20

**Класс:** `AliexpressAffiliateProductQueryRequest`

**Наследуется от:** `RestApi`

**Описание класса:**

Класс `AliexpressAffiliateProductQueryRequest` предназначен для формирования запросов к API AliExpress для поиска продуктов. Он расширяет базовый класс `RestApi`, добавляя необходимые параметры для конкретного запроса.

**Методы:**

* `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    * Конструктор класса.
    * Инициализирует параметры запроса, задавая значения по умолчанию для `domain` и `port`.
    *  Инициализирует атрибуты для следующих параметров запроса:
        * `app_signature`:  (Описание, если есть)
        * `category_ids`: (Описание, если есть)
        * `delivery_days`: (Описание, если есть)
        * `fields`: (Описание, если есть)
        * `keywords`: (Описание, если есть)
        * `max_sale_price`: (Описание, если есть)
        * `min_sale_price`: (Описание, если есть)
        * `page_no`: (Описание, если есть)
        * `page_size`: (Описание, если есть)
        * `platform_product_type`: (Описание, если есть)
        * `ship_to_country`: (Описание, если есть)
        * `sort`: (Описание, если есть)
        * `target_currency`: (Описание, если есть)
        * `target_language`: (Описание, если есть)
        * `tracking_id`: (Описание, если есть)

* `getapiname(self)`:
    * Возвращает имя API-метода, к которому отправляется запрос. В данном случае это `aliexpress.affiliate.product.query`.

**Использование:**

Для использования класса `AliexpressAffiliateProductQueryRequest`, необходимо создать экземпляр класса и задать необходимые параметры.  Затем, можно использовать методы `RestApi` для отправки запроса и обработки результата.

**Пример (Примерный):**

```python
from ...base import RestApi  # Предполагается, что RestApi импортируется из соответствующего места

request = AliexpressAffiliateProductQueryRequest()
request.keywords = "t-shirt"
request.page_size = 10
response = request.execute()  # Предполагается, что у RestApi есть метод execute
# Далее обработка результата response
```


**Важно:**

* Добавьте подробные описания для каждого атрибута, чтобы четко указать их назначение.
* Если возможны значения по умолчанию, укажите их.
* Добавьте информацию о допустимых типах данных для параметров запроса.
* Укажите, куда отправляется запрос (API-эндпоинт).
* Опишите формат ответа API.
* Приведите примеры корректных значений параметров.
* Добавьте ссылку на документацию API AliExpress, если она доступна.
```