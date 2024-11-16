```markdown
# Файл: `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductQueryRequest.py`

Файл описывает класс `AliexpressAffiliateProductQueryRequest`, предназначенный для запроса информации о продуктах на платформе AliExpress через API.  Класс наследуется от базового класса `RestApi`.

**Расположение:** `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\_examples\rest\AliexpressAffiliateProductQueryRequest.py`

**Роль:** `doc_creator` (создание документации)

**Описание класса `AliexpressAffiliateProductQueryRequest`:**

Класс `AliexpressAffiliateProductQueryRequest` реализует API-запрос для получения списка продуктов из партнерской программы AliExpress. Он позволяет фильтровать результаты по различным параметрам.

**Атрибуты:**

* `app_signature`:  (тип: `None`) — подпись приложения (необходимо для аутентификации).
* `category_ids`: (тип: `None`) — список идентификаторов категорий для фильтрации по категориям.
* `delivery_days`: (тип: `None`) — количество дней доставки.
* `fields`: (тип: `None`) — список полей, которые нужно вернуть в ответе.
* `keywords`: (тип: `None`) — ключевые слова для поиска.
* `max_sale_price`: (тип: `None`) — максимальная цена продажи.
* `min_sale_price`: (тип: `None`) — минимальная цена продажи.
* `page_no`: (тип: `None`) — номер страницы результатов.
* `page_size`: (тип: `None`) — размер страницы результатов.
* `platform_product_type`: (тип: `None`) — тип продукта на платформе.
* `ship_to_country`: (тип: `None`) — страна доставки.
* `sort`: (тип: `None`) — поле для сортировки результатов.
* `target_currency`: (тип: `None`) — целевая валюта.
* `target_language`: (тип: `None`) — целевой язык.
* `tracking_id`: (тип: `None`) — идентификатор отслеживания (возможно, для внутреннего использования).

**Методы:**

* `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса. Инициализирует базовый класс `RestApi` с заданными значениями `domain` и `port`. Инициализирует атрибуты класса с значениями по умолчанию `None`.
* `getapiname(self)`: Возвращает имя API-метода, который должен быть использован для запроса. В данном случае это `aliexpress.affiliate.product.query`.


**Примечание:**

* Документация к API AliExpress должна быть использована для получения точной информации о параметрах и их значениях.
* Необходимо указать значения для параметров, чтобы получить полезные результаты.
*  Код использует `RestApi` как базовый класс.  Документация к `RestApi` необходима для полного понимания работы класса.


**Пример использования (предполагается, что `RestApi` имеет подходящие методы):**

```python
# Пример использования
request = AliexpressAffiliateProductQueryRequest()
request.keywords = "iphone 14"
request.page_size = 10
response = request.execute() # Предполагается, что у RestApi есть execute метод
# Обработка ответа
```

**Важно:** Данный класс является примером.  Нужно указать точное описание параметров и значений для конкретного API-запроса.
