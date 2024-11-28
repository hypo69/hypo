# Модуль AliexpressAffiliateHotproductDownloadRequest

## Обзор

Модуль `AliexpressAffiliateHotproductDownloadRequest` предоставляет класс для запроса горячих продуктов на платформе AliExpress через API.  Он наследуется от базового класса `RestApi` и реализует необходимые методы для взаимодействия с API.

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**:  Класс для отправки запросов на получение списка горячих продуктов с AliExpress.

**Инициализация (`__init__`)**:

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
    self.category_id = None
    self.country = None
    self.fields = None
    self.scenario_language_site = None
    self.page_no = None
    self.page_size = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None
```

**Методы**:

- `getapiname()`: Возвращает имя API-метода для запроса.

```python
def getapiname(self):
    """
    Возвращает имя API-метода.

    Returns:
        str: Имя API-метода ('aliexpress.affiliate.hotproduct.download').
    """
    return 'aliexpress.affiliate.hotproduct.download'
```


## Параметры класса

Класс `AliexpressAffiliateHotproductDownloadRequest` принимает следующие параметры при инициализации:

- `domain`: Домен API (строка, по умолчанию `api-sg.aliexpress.com`).
- `port`: Порт API (целое число, по умолчанию `80`).

##  Атрибуты класса

Класс имеет следующие атрибуты:

- `app_signature`:  (Тип: Не определен).
- `category_id`: (Тип: Не определен).
- `country`: (Тип: Не определен).
- `fields`: (Тип: Не определен).
- `scenario_language_site`: (Тип: Не определен).
- `page_no`: (Тип: Не определен).
- `page_size`: (Тип: Не определен).
- `target_currency`: (Тип: Не определен).
- `target_language`: (Тип: Не определен).
- `tracking_id`: (Тип: Не определен).

**Примечание:**  Типы данных для атрибутов не указаны в коде. Должны быть указаны более конкретные типы данных (например, `str`, `int`, `dict`).