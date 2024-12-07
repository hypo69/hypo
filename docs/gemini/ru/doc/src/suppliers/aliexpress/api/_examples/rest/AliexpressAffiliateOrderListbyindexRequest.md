# Модуль aliexpress/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py

## Обзор

Этот модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, который представляет собой запрос для получения списка заказов аффилированного партнера AliExpress по индексу.  Он наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Классы

### `AliexpressAffiliateOrderListbyindexRequest`

**Описание**:  Класс для формирования запроса на получение списка заказов аффилированного партнера AliExpress по индексу.

**Методы**:

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Инициализирует объект запроса.

    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.

    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.end_time = None
    self.fields = None
    self.page_size = None
    self.start_query_index_id = None
    self.start_time = None
    self.status = None
```

#### `getapiname`

```python
def getapiname(self):
    """
    Возвращает имя API.

    Returns:
        str: Имя API, в данном случае 'aliexpress.affiliate.order.listbyindex'.
    """
    return 'aliexpress.affiliate.order.listbyindex'
```


## Атрибуты класса:

* `app_signature`:  Значение приложения.
* `end_time`: Конечная дата.
* `fields`: Список полей.
* `page_size`: Размер страницы.
* `start_query_index_id`: Идентификатор начала запроса.
* `start_time`: Начальная дата.
* `status`: Статус.


```
```