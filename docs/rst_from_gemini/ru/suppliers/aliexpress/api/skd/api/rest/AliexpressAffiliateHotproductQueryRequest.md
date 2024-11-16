```markdown
# AliexpressAffiliateHotproductQueryRequest.py

**Расположение:** `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\skd\api\rest\AliexpressAffiliateHotproductQueryRequest.py`

**Роль:** `doc_creator`

**Описание:**

Этот файл содержит класс `AliexpressAffiliateHotproductQueryRequest`, представляющий запрос к API AliExpress для получения горячих продуктов по партнерской программе. Класс наследуется от `RestApi`, обеспечивая базовый функционал для работы с API.

**Класс `AliexpressAffiliateHotproductQueryRequest`:**

Класс предназначен для формирования запросов к API AliExpress для получения списка горячих продуктов.  Он позволяет указать различные параметры для фильтрации и сортировки результатов.

**Атрибуты:**

* `app_signature`:  (тип данных: None) - Подпись приложения.
* `category_ids`: (тип данных: None) - ID категорий товаров.
* `delivery_days`: (тип данных: None) -  Количество дней доставки.
* `fields`: (тип данных: None) -  Список требуемых полей для возвращаемых результатов.
* `keywords`: (тип данных: None) - Ключевые слова для поиска товаров.
* `max_sale_price`: (тип данных: None) - Максимальная цена продажи.
* `min_sale_price`: (тип данных: None) - Минимальная цена продажи.
* `page_no`: (тип данных: None) - Номер страницы для постраничного вывода.
* `page_size`: (тип данных: None) - Размер страницы для постраничного вывода.
* `platform_product_type`: (тип данных: None) - Тип продукта на платформе.
* `ship_to_country`: (тип данных: None) - Страна доставки.
* `sort`: (тип данных: None) - Сортировка результатов.
* `target_currency`: (тип данных: None) - Целевая валюта.
* `target_language`: (тип данных: None) - Целевой язык.
* `tracking_id`: (тип данных: None) - ID отслеживания.

**Методы:**

* `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса. Инициализирует базовые параметры запроса, такие как домен и порт API.
* `getapiname(self)`: Возвращает имя API-метода, используемого для запроса (`aliexpress.affiliate.hotproduct.query`).

**Примечания:**

* Атрибуты, имеющие значение `None`, не заполнены по умолчанию и должны быть заданы перед использованием класса для построения запроса.
* Документация к API AliExpress необходима для точной информации о параметрах и их значениях.
* Для эффективного использования класса, необходимо знать структуру данных, которые возвращает API в ответе.


**Пример использования (псевдокод):**

```python
from AliexpressAffiliateHotproductQueryRequest import AliexpressAffiliateHotproductQueryRequest

request = AliexpressAffiliateHotproductQueryRequest()
request.keywords = "iphone"
request.page_size = 10
response = request.execute()  # Вызов метода execute для отправки запроса
# Обработка ответа от API
```

**Важно:**  Добавить примеры использования конкретных методов для более полного документа.  Добавить ссылки на соответствующую документацию API AliExpress.
```