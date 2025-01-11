# Модуль `AliexpressAffiliateProductdetailGetRequest`

## Обзор

Модуль `AliexpressAffiliateProductdetailGetRequest` представляет собой реализацию REST API запроса для получения детальной информации о продуктах AliExpress через партнерскую программу. Он предназначен для использования в рамках SDK для работы с AliExpress API.

## Оглавление

1. [Классы](#классы)
    - [`AliexpressAffiliateProductdetailGetRequest`](#aliexpressaffiliateproductdetailgetrequest)
2. [Функции](#функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateProductdetailGetRequest`

**Описание**: Класс для формирования запроса на получение детальной информации о продуктах AliExpress.

**Методы**:
- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API метода.

#### `__init__`
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Доменное имя API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    """
```
**Описание**: Инициализирует объект запроса, устанавливая домен и порт API, а также параметры запроса.
    
**Параметры**:
- `domain` (str, optional): Доменное имя API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Атрибуты**:
- `app_signature` (str, optional): Подпись приложения. По умолчанию `None`.
- `country` (str, optional): Код страны. По умолчанию `None`.
- `fields` (str, optional): Список полей для возврата. По умолчанию `None`.
- `product_ids` (str, optional): Список ID продуктов. По умолчанию `None`.
- `target_currency` (str, optional): Целевая валюта. По умолчанию `None`.
- `target_language` (str, optional): Целевой язык. По умолчанию `None`.
- `tracking_id` (str, optional): ID отслеживания. По умолчанию `None`.

## Функции

### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Имя API метода 'aliexpress.affiliate.productdetail.get'.
    """
```
**Описание**: Возвращает имя API метода, который будет вызван для данного запроса.

**Возвращает**:
- `str`: Имя API метода `'aliexpress.affiliate.productdetail.get'`.