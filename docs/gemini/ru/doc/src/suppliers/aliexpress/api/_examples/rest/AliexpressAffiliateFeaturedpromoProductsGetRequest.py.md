# Модуль `aliexpress.affiliate.featuredpromo.products.get`

## Обзор

Этот модуль содержит класс `AliexpressAffiliateFeaturedpromoProductsGetRequest`, который используется для отправки запроса на получение списка акционных товаров AliExpress.

## Оглавление
1. [Классы](#Классы)
    - [`AliexpressAffiliateFeaturedpromoProductsGetRequest`](#AliexpressAffiliateFeaturedpromoProductsGetRequest)
2. [Функции](#Функции)
    - [`getapiname`](#getapiname)

## Классы

### `AliexpressAffiliateFeaturedpromoProductsGetRequest`

**Описание**: Класс для отправки запроса на получение списка акционных товаров AliExpress.

**Методы**:
- `__init__`: Инициализирует объект класса.
- `getapiname`: Возвращает имя API-метода.

#### `__init__`

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80)
```

**Описание**: Конструктор класса `AliexpressAffiliateFeaturedpromoProductsGetRequest`.

**Параметры**:
- `domain` (str, optional): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Возвращает**:
- `None`: Метод не возвращает значение.

#### `getapiname`

```python
def getapiname(self) -> str:
```

**Описание**: Возвращает имя API-метода.

**Параметры**:
- `self` : Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Строка, представляющая имя API-метода: `aliexpress.affiliate.featuredpromo.products.get`.

## Функции
### `getapiname`
```python
def getapiname(self) -> str:
```
**Описание**: Возвращает имя API метода.

**Параметры**:
   - `self` : Ссылка на экземпляр класса.

**Возвращает**:
   - `str`: Возвращает имя API метода 'aliexpress.affiliate.featuredpromo.products.get'.