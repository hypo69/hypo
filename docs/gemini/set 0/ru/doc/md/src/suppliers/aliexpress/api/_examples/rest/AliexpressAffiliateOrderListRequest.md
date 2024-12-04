# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListRequest.py`

## Обзор

Данный модуль содержит класс `AliexpressAffiliateOrderListRequest`, предназначенный для запроса списка заказов аффилиата на AliExpress.  Класс наследуется от базового класса `RestApi` и предоставляет методы для инициализации и получения имени API.


## Классы

### `AliexpressAffiliateOrderListRequest`

**Описание**: Класс `AliexpressAffiliateOrderListRequest` реализует запрос списка заказов аффилиата на AliExpress через REST API.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект `AliexpressAffiliateOrderListRequest`.
    **Параметры**:
        - `domain` (str, опционально, по умолчанию "api-sg.aliexpress.com"): Домен API.
        - `port` (int, опционально, по умолчанию 80): Порт API.
    **Возвращает**:
        - `None`

- `getapiname(self)`:
    **Описание**: Возвращает имя API.
    **Параметры**:
        - Нет.
    **Возвращает**:
        - `str`: Имя API (`aliexpress.affiliate.order.list`).

**Атрибуты**:

- `app_signature`: Приложение подписи.
- `end_time`: Конечная дата.
- `fields`: Поля.
- `locale_site`: Местный сайт.
- `page_no`: Номер страницы.
- `page_size`: Размер страницы.
- `start_time`: Начальная дата.
- `status`: Статус.


## Функции

В данном модуле нет других функций, кроме методов класса.