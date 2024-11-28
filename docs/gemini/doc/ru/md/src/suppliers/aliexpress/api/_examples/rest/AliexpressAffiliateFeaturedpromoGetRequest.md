# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py`

## Обзор

Данный модуль предоставляет класс `AliexpressAffiliateFeaturedpromoGetRequest`, который наследуется от `RestApi` и используется для получения данных о промо-акциях на AliExpress.

## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**:  Класс для запроса данных о промо-акциях на AliExpress через API.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект класса.
    **Параметры**:
        - `domain` (str, optional): Домен API. По умолчанию `api-sg.aliexpress.com`.
        - `port` (int, optional): Порт API. По умолчанию `80`.
    **Возвращает**:
        - None
- `getapiname(self)`:
    **Описание**: Возвращает имя API-метода.
    **Параметры**:
        - Нет
    **Возвращает**:
        - str: Имя API-метода (`aliexpress.affiliate.featuredpromo.get`).