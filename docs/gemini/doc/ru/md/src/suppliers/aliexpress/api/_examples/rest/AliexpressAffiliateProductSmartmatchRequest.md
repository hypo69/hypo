# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py`

## Обзор

Этот модуль предоставляет класс `AliexpressAffiliateProductSmartmatchRequest`, который используется для запроса информации о продуктах на AliExpress с использованием API.  Класс наследуется от `RestApi`.

## Классы

### `AliexpressAffiliateProductSmartmatchRequest`

**Описание**: Класс для отправки запросов на получение информации о продуктах AliExpress, используя функцию smartmatch.

**Атрибуты**:

- `app`:  Значение для идентификации приложения.
- `app_signature`: Подпись приложения.
- `country`: Страна.
- `device`: Тип устройства.
- `device_id`: Идентификатор устройства.
- `fields`: Список полей, которые нужно вернуть.
- `keywords`: Список ключевых слов для поиска.
- `page_no`: Номер страницы результатов поиска.
- `product_id`: Идентификатор продукта.
- `site`: Сайт AliExpress.
- `target_currency`: Целевая валюта.
- `target_language`: Целевой язык.
- `tracking_id`: Идентификатор отслеживания.
- `user`: Идентификатор пользователя.

**Методы**:

#### `getapiname()`

**Описание**: Возвращает имя API-метода для запроса.

**Возвращает**:
- `str`: Имя API-метода (`aliexpress.affiliate.product.smartmatch`).