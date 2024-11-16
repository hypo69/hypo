```markdown
# AliexpressAffiliateHotproductDownloadRequest.py

**Расположение:** `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\_examples\rest\AliexpressAffiliateHotproductDownloadRequest.py`

**Роль:** `doc_creator`

**Описание:**

Этот файл содержит класс `AliexpressAffiliateHotproductDownloadRequest`, представляющий собой запрос к API AliExpress для получения горячих продуктов по партнерской программе. Класс наследуется от базового класса `RestApi`.

**Класс `AliexpressAffiliateHotproductDownloadRequest`:**

Класс `AliexpressAffiliateHotproductDownloadRequest` предназначен для взаимодействия с API AliExpress для загрузки горячих продуктов, предоставляемых через партнерскую программу. Он позволяет задавать параметры для запроса, такие как ID категории, страна, поля для возврата и т.д.

**Атрибуты класса:**

* `app_signature`: Приложение подписи.
* `category_id`: ID категории.
* `country`: Страна.
* `fields`: Поля для возврата.
* `scenario_language_site`: Язык и сайт сценария.
* `page_no`: Номер страницы.
* `page_size`: Размер страницы.
* `target_currency`: Целевая валюта.
* `target_language`: Целевой язык.
* `tracking_id`: ID отслеживания.

**Методы:**

* `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса. Инициализирует базовые атрибуты, настроенные для работы с API AliExpress.
* `getapiname(self)`: Возвращает имя API-метода `aliexpress.affiliate.hotproduct.download`.

**Использование:**

Для использования класса `AliexpressAffiliateHotproductDownloadRequest`, необходимо создать его экземпляр, задать значения атрибутов и вызвать необходимые методы.

**Пример:**

```python
from aliexpress.api._examples.rest.AliexpressAffiliateHotproductDownloadRequest import AliexpressAffiliateHotproductDownloadRequest

# Создание экземпляра класса
request = AliexpressAffiliateHotproductDownloadRequest()

# Установка значений атрибутов
request.category_id = 123
request.country = "US"
request.fields = ["title", "price"]

# Вызов метода для получения данных
# ... (Обработка результата) ...
```

**Комментарии:**

Файл содержит два идентичных комментария `MODE = 'debug'`. Необходимо убрать дубликат.

**Дополнительные замечания:**

* Файл следует доработать, добавив документацию к параметрам, возвращаемым значениям и возможным исключениям.
* Необходимо добавить примеры использования с обработкой результатов.
* Рекомендовано добавить обработку ошибок (например, проверку корректности введённых параметров).


**Модуль:** `src.suppliers.aliexpress.api._examples.rest`

**Дата создания:** 2021.05.12
```