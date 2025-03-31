# Модуль `AliexpressAffiliateHotproductDownloadRequest`

## Обзор

Модуль `AliexpressAffiliateHotproductDownloadRequest` представляет собой класс для выполнения запроса на загрузку горячих товаров через API AliExpress.

## Оглавление

- [Классы](#классы)
  - [`AliexpressAffiliateHotproductDownloadRequest`](#aliexpressaffiliatehotproductdownloadrequest)
    - [Методы](#методы)
      - [`__init__`](#__init__)
      - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateHotproductDownloadRequest`

**Описание**: Класс для создания запроса на загрузку горячих товаров через API AliExpress.

**Методы**:

- [`__init__`](#__init__)
- [`getapiname`](#getapiname)

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

**Описание**: Конструктор класса `AliexpressAffiliateHotproductDownloadRequest`. Инициализирует объект с параметрами домена и порта, а также атрибутами для хранения параметров запроса.

**Параметры**:

- `domain` (str, optional): Домен API. По умолчанию `"api-sg.aliexpress.com"`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`

#### `getapiname`

```python
def getapiname(self) -> str:
    """
    Args:
        None

    Returns:
        str: Возвращает имя API-метода 'aliexpress.affiliate.hotproduct.download'.
    """
```

**Описание**: Метод возвращает имя API-метода для запроса горячих товаров.

**Параметры**:
- `None`

**Возвращает**:
- `str`: Имя API-метода `'aliexpress.affiliate.hotproduct.download'`.