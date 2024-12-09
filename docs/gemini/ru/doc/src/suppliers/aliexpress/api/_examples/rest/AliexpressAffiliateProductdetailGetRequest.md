# Модуль AliexpressAffiliateProductdetailGetRequest

## Обзор

Этот модуль содержит класс `AliexpressAffiliateProductdetailGetRequest`, который представляет собой запрос для получения подробной информации о продукте на AliExpress.  Класс наследуется от базового класса `RestApi` и предоставляет методы для настройки параметров запроса и получения имени API.

## Оглавление

- [Модуль AliexpressAffiliateProductdetailGetRequest](#модуль-aliexpressaffiliateproductdetailgetrequest)
    - [Обзор](#обзор)
    - [Класс AliexpressAffiliateProductdetailGetRequest](#класс-aliexpressaffiliateproductdetailgetrequest)
        - [Метод `__init__`](#метод-init)
        - [Метод `getapiname`](#метод-getapiname)

## Класс AliexpressAffiliateProductdetailGetRequest

### Описание

Класс `AliexpressAffiliateProductdetailGetRequest` представляет собой запрос к API AliExpress для получения подробной информации о продуктах. Он содержит параметры для настройки запроса и предоставляет метод для получения имени API.

### Метод `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.

    Returns:
        None
    """
    RestApi.__init__(self, domain, port)
    self.app_signature = None
    self.country = None
    self.fields = None
    self.product_ids = None
    self.target_currency = None
    self.target_language = None
    self.tracking_id = None
```

### Метод `getapiname`

```python
def getapiname(self):
    """
    Returns:
        str: Имя API.
    """
    return 'aliexpress.affiliate.productdetail.get'
```