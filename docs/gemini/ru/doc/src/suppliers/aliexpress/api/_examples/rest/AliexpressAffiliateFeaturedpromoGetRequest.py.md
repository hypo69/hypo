# AliexpressAffiliateFeaturedpromoGetRequest

## Обзор

Этот модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, который используется для выполнения запроса к API AliExpress для получения информации о рекомендуемых акциях.

## Оглавление

- [Классы](#классы)
  - [AliexpressAffiliateFeaturedpromoGetRequest](#AliexpressAffiliateFeaturedpromoGetRequest)

## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс для создания запроса на получение информации о рекомендуемых акциях от AliExpress.

**Методы**:

- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API-метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    
    Returns:
        None
    """
```
**Описание**: Конструктор класса `AliexpressAffiliateFeaturedpromoGetRequest`. Инициализирует домен и порт, а также атрибуты `app_signature` и `fields` как `None`.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
- `port` (int, optional): Порт API. По умолчанию 80.

**Возвращает**:

- `None`: Метод ничего не возвращает.

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Returns:
        str: Имя API-метода 'aliexpress.affiliate.featuredpromo.get'.
    """
```
**Описание**: Метод возвращает имя API-метода, к которому будет отправлен запрос.

**Возвращает**:

- `str`: Строка, представляющая имя API-метода: `'aliexpress.affiliate.featuredpromo.get'`.