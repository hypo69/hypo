# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductdetailGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductdetailGetRequest`, представляющий запрос к API AliExpress для получения подробной информации о продуктах. Класс наследуется от `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**: Класс для получения подробной информации о продуктах со связанными данными посредством API AliExpress.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- None

#### `getapiname`

**Описание**: Возвращает имя API метода.

**Параметры**:

- Нет

**Возвращает**:
- str: Название метода API (`aliexpress.affiliate.productdetail.get`).


```python
from ..base import RestApi
class AliexpressAffiliateProductdetailGetRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.country = None
		self.fields = None
		self.product_ids = None
		self.target_currency = None
		self.target_language = None
		self.tracking_id = None

	def getapiname(self):
		return 'aliexpress.affiliate.productdetail.get'
```