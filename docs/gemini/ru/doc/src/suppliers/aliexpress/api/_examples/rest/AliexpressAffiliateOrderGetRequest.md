# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py

## Обзор

Данный модуль содержит класс `AliexpressAffiliateOrderGetRequest`, представляющий собой API-запрос для получения информации о заказах в программе аффилированного маркетинга AliExpress. Класс наследуется от базового класса `RestApi`. Он предоставляет методы для инициализации запроса, получения имени API-метода и, предположительно, выполнения запроса.


## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс `AliexpressAffiliateOrderGetRequest` предназначен для создания и выполнения запроса к API AliExpress для получения информации о заказах аффилированного маркетолога.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект запроса.
    **Параметры**:
    - `domain` (str, опционально "api-sg.aliexpress.com"): Доменное имя API.
    - `port` (int, опционально 80): Порт API.
    **Возвращает**:
    - `None`

- `getapiname(self)`:
    **Описание**: Возвращает имя API-метода.
    **Параметры**:
    - `self`: Объект класса.
    **Возвращает**:
    - str: Имя API-метода (`aliexpress.affiliate.order.get`).


## Функции

(Нет функций в этом модуле)