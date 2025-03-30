# Модуль `AliexpressAffiliateLinkGenerateRequest`

## Обзор

Модуль содержит класс `AliexpressAffiliateLinkGenerateRequest`, который используется для генерации партнерских ссылок AliExpress через REST API.

## Оглавление

1. [Классы](#Классы)
    - [`AliexpressAffiliateLinkGenerateRequest`](#AliexpressAffiliateLinkGenerateRequest)

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**:
Класс для формирования запроса на генерацию партнерских ссылок AliExpress.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`: Конструктор класса.
- `getapiname(self)`: Возвращает имя API метода.

#### `__init__`
```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.
    """
```
**Описание**:
Конструктор класса `AliexpressAffiliateLinkGenerateRequest`. Инициализирует базовый класс `RestApi` и устанавливает параметры запроса.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

#### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода - 'aliexpress.affiliate.link.generate'.
    """
```
**Описание**:
Возвращает имя API метода для генерации партнерских ссылок.

**Возвращает**:
- `str`: Строка `'aliexpress.affiliate.link.generate'`, представляющая имя API метода.