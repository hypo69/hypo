# Модуль `AliexpressAffiliateProductdetailGetRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductdetailGetRequest`, который используется для запроса детальной информации о продуктах AliExpress через API. Этот класс является частью более крупной системы для работы с API AliExpress.

## Оглавление

1. [Классы](#классы)
   - [`AliexpressAffiliateProductdetailGetRequest`](#AliexpressAffiliateProductdetailGetRequest)
2. [Функции](#функции)
   - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**: Класс для отправки запроса на получение детальной информации о продуктах AliExpress.

**Методы**:

- `__init__`: Конструктор класса.
- `getapiname`: Метод для получения имени API.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

```python
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Args:
            domain (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
            port (int, optional): Порт API. По умолчанию `80`.
        """
        RestApi.__init__(self,domain, port)
        self.app_signature = None
        self.country = None
        self.fields = None
        self.product_ids = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None
```

## Функции

### `getapiname`

**Описание**: Возвращает имя API для запроса деталей продукта.

**Возвращает**:

- `str`: Имя API `'aliexpress.affiliate.productdetail.get'`.

```python
    def getapiname(self) -> str:
        """
        Returns:
            str: Имя API `'aliexpress.affiliate.productdetail.get'`.
        """
        return 'aliexpress.affiliate.productdetail.get'
```