# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py`

## Обзор

Модуль содержит класс `AliexpressAffiliateFeaturedpromoGetRequest`, представляющий API-запрос для получения данных о выделенных промоакциях на AliExpress.  Класс наследуется от `RestApi` и предоставляет методы для взаимодействия с API.


## Классы

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Описание**: Класс представляет API-запрос для получения данных о выделенных промоакциях на AliExpress.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект запроса.
    **Параметры**:
        - `domain` (str, опционально "api-sg.aliexpress.com"): Домен API.
        - `port` (int, опционально 80): Порт API.
    **Возвращает**:
        - None.


- `getapiname(self)`:
    **Описание**: Возвращает имя API-метода.
    **Параметры**:
        - Нет.
    **Возвращает**:
        - str: Имя API-метода ('aliexpress.affiliate.featuredpromo.get').


## Функции

(Нет функций в этом модуле)