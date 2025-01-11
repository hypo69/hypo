# Модуль `AliexpressAffiliateLinkGenerateRequest`

## Обзор

Модуль `AliexpressAffiliateLinkGenerateRequest` представляет собой пример использования REST API для генерации партнерских ссылок AliExpress.

## Оглавление
1. [Классы](#Классы)
    - [`AliexpressAffiliateLinkGenerateRequest`](#AliexpressAffiliateLinkGenerateRequest)
        - [`__init__`](#__init__)
        - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**: Класс для запроса генерации партнерских ссылок через AliExpress API.

**Методы**:
- [`__init__`](#__init__)
- [`getapiname`](#getapiname)

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80) -> None:
    """
    Args:
        domain (str): Доменное имя API AliExpress. По умолчанию "api-sg.aliexpress.com".
        port (int): Порт API AliExpress. По умолчанию 80.

    Returns:
        None:
    """
```
**Описание**: Инициализирует экземпляр класса `AliexpressAffiliateLinkGenerateRequest`.

**Параметры**:
- `domain` (str): Доменное имя API AliExpress. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int): Порт API AliExpress. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода - 'aliexpress.affiliate.link.generate'.
    """
```
**Описание**: Возвращает имя API метода для генерации партнерских ссылок.

**Параметры**:
- `self` : Экземпляр класса.

**Возвращает**:
- `str`: Имя API метода - `'aliexpress.affiliate.link.generate'`.