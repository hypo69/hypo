# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateProductSmartmatchRequest`, представляющий запрос к API для поиска продуктов на AliExpress с использованием функции smartmatch.  Этот класс наследуется от базового класса `RestApi`.

## Оглавление

- [Модуль `AliexpressAffiliateProductSmartmatchRequest`](#модуль-aliexpressaffiliateproductsmartmatchrequest)
- [Класс `AliexpressAffiliateProductSmartmatchRequest`](#класс-aliexpressaffiliateproductsmartmatchrequest)
    - [Метод `getapiname`](#метод-getapiname)


## Класс `AliexpressAffiliateProductSmartmatchRequest`

**Описание**:  Класс представляет собой запрос к API для поиска продуктов на AliExpress. Он позволяет настраивать параметры поиска, такие как ключевые слова, страна, язык и другие.

**Инициализация**:

```python
def __init__(self, domain="api-sg.aliexpress.com", port=80):
```

**Параметры**:
- `domain` (str, optional): Доменное имя API. По умолчанию `api-sg.aliexpress.com`.
- `port` (int, optional): Порт API. По умолчанию `80`.

**Атрибуты**:

- `app`:  Не описано.
- `app_signature`: Не описано.
- `country`: Не описано.
- `device`: Не описано.
- `device_id`: Не описано.
- `fields`: Не описано.
- `keywords`: Не описано.
- `page_no`: Не описано.
- `product_id`: Не описано.
- `site`: Не описано.
- `target_currency`: Не описано.
- `target_language`: Не описано.
- `tracking_id`: Не описано.
- `user`: Не описано.


## Методы

### `getapiname`

**Описание**: Возвращает имя API метода.

**Возвращает**:
- `str`: Имя API метода (`aliexpress.affiliate.product.smartmatch`).