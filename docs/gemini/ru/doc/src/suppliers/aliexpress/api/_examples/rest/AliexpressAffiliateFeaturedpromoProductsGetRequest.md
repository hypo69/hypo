# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, представляющий запрос к API AliExpress для получения данных о продуктах с выделенными промоакциями. Он наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс представляет собой запрос к API AliExpress для получения списка продуктов, участвующих в промоакциях.

**Методы**:

#### `__init__(self, domain="api-sg.aliexpress.com", port=80)`

**Описание**: Инициализирует объект запроса.

**Параметры**:

- `domain` (str, опционально): Домен API AliExpress. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, опционально): Порт API. По умолчанию `80`.


#### `getapiname(self)`

**Описание**: Возвращает имя API-метода.

**Возвращает**:

- `str`: Имя API-метода `aliexpress.affiliate.featuredpromo.products.get`.
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Инициализирует объект запроса.

    Args:
        domain (str, optional): Домен API AliExpress. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    """
    RestApi.__init__(self,domain, port)
    self.app_signature = None
    self.category_id = None
    self.country = None
    self.fields = None
    self.page_no = None
    self.page_size = None
    self.promotion_end_time = None
    self.promotion_name = None
    self.promotion_start_time = None
    self.sort = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None


def getapiname(self):
    """
    Возвращает имя API-метода.

    Returns:
        str: Имя API-метода "aliexpress.affiliate.featuredpromo.products.get".
    """
    return 'aliexpress.affiliate.featuredpromo.products.get'
```

**Примечания**:

- Переменные `self.app_signature`, `self.category_id`, и т.д. представляют параметры запроса, которые должны быть установлены перед вызовом метода `do_request`.
- Их значения не указаны в документации метода `__init__`, но предполагается, что они необходимы для формирования корректного запроса к API.


**Описания дополнительных параметров**:

- `self.app_signature`: Подпись приложения
- `self.category_id`: Идентификатор категории
- `self.country`: Страна
- `self.fields`: Поля
- `self.page_no`: Номер страницы
- `self.page_size`: Размер страницы
- `self.promotion_end_time`: Конечная дата промоакции
- `self.promotion_name`: Название промоакции
- `self.promotion_start_time`: Начальная дата промоакции
- `self.sort`: Сортировка
- `self.target_currency`: Целевая валюта
- `self.target_language`: Целевой язык
- `self.tracking_id`: Идентификатор отслеживания


Этот класс предоставляет основу для создания запросов к API AliExpress для получения информации о продуктах, участвующих в промоакциях.  Он требует настройки параметров, чтобы получить данные в необходимом формате.