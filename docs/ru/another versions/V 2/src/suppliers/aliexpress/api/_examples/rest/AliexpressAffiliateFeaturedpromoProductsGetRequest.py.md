# Документация для `AliexpressAffiliateFeaturedpromoProductsGetRequest.py`

## Оглавление
1. [Обзор](#обзор)
2. [Классы](#классы)
    - [`AliexpressAffiliateFeaturedpromoProductsGetRequest`](#aliexpressaffiliatefeaturedpromoproductsgetrequest)
3. [Функции](#функции)
    - [`getapiname`](#getapiname)

## Обзор

Файл содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, который является примером запроса к API AliExpress для получения списка продвигаемых товаров.

## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс, представляющий запрос для получения продвигаемых товаров AliExpress.

**Методы**:
- `__init__`: Конструктор класса.
- `getapiname`: Возвращает имя API метода.

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
**Описание**: Конструктор класса `AliexpressAffiliateFeaturedpromoProductsGetRequest`. Инициализирует объект запроса, устанавливая домен и порт API, а также атрибуты для параметров запроса.

**Параметры**:
- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

#### `getapiname`
```python
def getapiname(self) -> str:
    """
    Returns:
        str: Возвращает имя API метода 'aliexpress.affiliate.featuredpromo.products.get'.
    """
```
**Описание**: Метод возвращает имя API метода, которое используется для запроса.

**Возвращает**:
- `str`: Имя API метода: `'aliexpress.affiliate.featuredpromo.products.get'`.

## Функции

В данном файле нет отдельных функций, кроме методов класса.