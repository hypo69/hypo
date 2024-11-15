```markdown
# AliexpressAffiliateLinkGenerateRequest.py

Файл: `C:\Users\user\Documents\repos\hypotez\src\suppliers\aliexpress\api\skd\api\rest\AliexpressAffiliateLinkGenerateRequest.py`

**Роль:** `doc_creator` (генерация документации)

**Описание:**

Данный Python-файл определяет класс `AliexpressAffiliateLinkGenerateRequest`, представляющий собой запрос к API AliExpress для генерации аффилиатной ссылки. Он наследуется от базового класса `RestApi`.

**Класс `AliexpressAffiliateLinkGenerateRequest`:**

Этот класс предназначен для взаимодействия с API AliExpress и подготовки запроса на генерацию аффилиатной ссылки.

**Атрибуты:**

* `domain`: Строка, содержащая доменное имя API (по умолчанию `api-sg.aliexpress.com`).
* `port`: Целое число, представляющее порт API (по умолчанию `80`).
* `app_signature`:  Вероятно, подпись приложения, используемая для аутентификации.
* `promotion_link_type`: Тип промо-ссылки.
* `source_values`:  Данные источника, используемые для отслеживания.
* `tracking_id`:  Идентификатор отслеживания.

**Методы:**

* `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса. Инициализирует атрибуты класса и вызывает конструктор базового класса `RestApi`.
* `getapiname(self)`: Возвращает имя API-метода, используемого для генерации аффилиатной ссылки (`aliexpress.affiliate.link.generate`).

**Использование:**

Для использования класса необходимо создать экземпляр `AliexpressAffiliateLinkGenerateRequest`, задав необходимые параметры (например, `app_signature`, `promotion_link_type`, `source_values`, `tracking_id`). Затем, используя методы базового класса `RestApi`, можно отправить запрос к API и получить ответ.

**Примечания:**

* Код предполагает наличие базового класса `RestApi`, который отвечает за взаимодействие с API.  В документации необходимо указать  функциональность этого класса для полной картины.
* Комментарии `""" module: src.suppliers.aliexpress.api.skd.api.rest """` и `""" Created by auto_sdk on 2020.03.09 """` указывают на автоматическую генерацию кода и дату создания.  Это полезная информация для понимания происхождения файла.
* Вероятно, необходимо заполнять атрибуты `app_signature`, `promotion_link_type`, `source_values` и `tracking_id` перед использованием метода `RestApi.execute` для отправки запроса.
* Необходимо уточнить тип данных для каждого атрибута и описать, как их использовать в запросе.
*  Добавьте пример использования класса, чтобы продемонстрировать, как отправлять запрос и обрабатывать ответ.


**Пример использования (неполный):**

```python
from ...aliexpress.api.skd.api.rest import AliexpressAffiliateLinkGenerateRequest


request = AliexpressAffiliateLinkGenerateRequest()
request.app_signature = "your_app_signature"
request.promotion_link_type = "type_of_link"
# ... другие значения

response = request.execute() # Предполагается, что execute есть в RestApi

# Обработка ответа...
```
