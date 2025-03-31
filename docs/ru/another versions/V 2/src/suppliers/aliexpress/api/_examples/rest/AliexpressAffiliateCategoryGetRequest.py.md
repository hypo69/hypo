# Модуль `AliexpressAffiliateCategoryGetRequest`

## Обзор

Модуль содержит пример реализации запроса для получения категорий товаров через REST API AliExpress.

## Оглавление

- [Классы](#классы)
    - [`AliexpressAffiliateCategoryGetRequest`](#aliexpressaffiliatecategorygetrequest)
        - [Метод `__init__`](#__init__)
        - [Метод `getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateCategoryGetRequest`

**Описание**: Класс, представляющий запрос для получения категорий товаров через REST API AliExpress.

**Методы**:
- [`__init__`](#__init__): Инициализирует объект запроса.
- [`getapiname`](#getapiname): Возвращает имя API.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80) -> None:
    """
    Args:
        domain (str, optional): Домен API. По умолчанию "api-sg.aliexpress.com".
        port (int, optional): Порт API. По умолчанию 80.

    Returns:
        None: 
    """
```
**Описание**: Инициализирует объект `AliexpressAffiliateCategoryGetRequest`.
        
**Параметры**:
    - `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
    - `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
    - `None`: Метод ничего не возвращает.

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Args:
        self: Экземпляр класса.

    Returns:
        str: Имя API запроса 'aliexpress.affiliate.category.get'.
    """
```
**Описание**: Возвращает имя API запроса.

**Параметры**:
   - `self`: Экземпляр класса.
    
**Возвращает**:
    - `str`: Имя API запроса `'aliexpress.affiliate.category.get'`.