# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderListbyindexRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderListbyindexRequest`, который представляет собой запрос к API AliExpress для получения списка заказов филиала.  Класс наследуется от базового класса `RestApi`.

## Классы

### `AliexpressAffiliateOrderListbyindexRequest`

**Описание**:  Класс представляет собой запрос к API AliExpress для получения списка заказов филиала.  Он настраивает параметры запроса и содержит методы для получения имени API.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует экземпляр класса.
    **Параметры**:
        - `domain` (str, опционально): Домен API. По умолчанию `api-sg.aliexpress.com`.
        - `port` (int, опционально): Порт API. По умолчанию `80`.
    **Возвращает**:
        - `None`


- `getapiname(self)`:
    **Описание**: Возвращает имя API запроса.
    **Параметры**:
        -  Нет
    **Возвращает**:
        - `str`: Название API - `aliexpress.affiliate.order.listbyindex`.


**Атрибуты**:

- `app_signature`:  (тип не указан)
- `end_time`: (тип не указан)
- `fields`: (тип не указан)
- `page_size`: (тип не указан)
- `start_query_index_id`: (тип не указан)
- `start_time`: (тип не указан)
- `status`: (тип не указан)


**Примечания**:  Этот класс, вероятно, предназначен для использования с другим кодом для подготовки и выполнения запросов к API.  Необходимо определить типы данных для атрибутов.