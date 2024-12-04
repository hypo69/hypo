# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` предоставляет класс для запроса списка заказов филиала AliExpress.  Он наследуется от базового класса `RestApi` и содержит методы для настройки параметров запроса и получения имени API.


## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс для запроса списка заказов филиала AliExpress.

**Методы**:

- `__init__`
- `getapiname`


#### `__init__`

**Описание**: Инициализирует объект класса.

**Параметры**:

- `domain` (str, опционально "api-sg.aliexpress.com"): Доменное имя API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, опционально 80): Порт API. По умолчанию 80.

**Возвращает**:
- None


#### `getapiname`

**Описание**: Возвращает имя API.

**Параметры**:

- Нет

**Возвращает**:
- str: Имя API (`aliexpress.affiliate.order.list`).

**Примечания**:

- В методе `__init__` определяются параметры, необходимые для запроса списка заказов филиала AliExpress.
- Параметры `app_signature`, `end_time`, `fields`, `locale_site`, `page_no`, `page_size`, `start_time` и `status` являются атрибутами объекта и могут быть установлены перед вызовом метода `getapiname`.

```
```python
from ..base import RestApi
class AliexpressAffiliateOrderListRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.end_time = None
		self.fields = None
		self.locale_site = None
		self.page_no = None
		self.page_size = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'aliexpress.affiliate.order.list'
```