# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py`

## Обзор

Модуль `AliexpressAffiliateOrderListRequest` предоставляет класс для работы с API AliExpress, позволяющий получать список заказов партнера.  Этот класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс `AliexpressAffiliateOrderListRequest` реализует взаимодействие с API AliExpress для получения списка заказов партнера.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект запроса.
    **Параметры**:
        - `domain` (str, опционально "api-sg.aliexpress.com"): Домен API. По умолчанию "api-sg.aliexpress.com".
        - `port` (int, опционально 80): Порт API. По умолчанию 80.
    **Возвращает**:
        - None
- `getapiname(self)`:
    **Описание**: Возвращает имя API-метода.
    **Параметры**:
        - Нет
    **Возвращает**:
        - str: Имя API-метода (`aliexpress.affiliate.order.list`).