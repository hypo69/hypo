# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py`

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` предоставляет класс для работы с API AliExpress, позволяющий получать список заказов.  Он наследуется от базового класса `RestApi` и содержит необходимые атрибуты и методы для формирования и отправки запроса на сервер.

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс представляет собой запрос к API AliExpress для получения списка заказов партнера.

**Атрибуты**:

- `app_signature`:  Значение приложения.
- `end_time`: Конечная дата/время.
- `fields`: Список полей для возврата.
- `locale_site`: Местная страница.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `start_time`: Начальная дата/время.
- `status`: Статус заказа.


**Методы**:

#### `getapiname()`

**Описание**: Возвращает имя API-метода.

**Возвращает**:
- `str`: Имя метода API (`aliexpress.affiliate.order.list`).


```python
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

**Примечание**:  Данный класс пока не содержит методов для работы с запросом. Для работы с API необходимо дополнить методы для установки значений атрибутов и отправки запроса.