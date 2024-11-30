# Модуль hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py

## Обзор

Модуль содержит класс `AliexpressAffiliateOrderGetRequest`, предназначенный для выполнения запроса к API AliExpress для получения данных о заказах аффилированного партнера. Класс наследуется от `RestApi` и предоставляет методы для инициализации, получения имени API и, предположительно, для выполнения самого запроса (методы для работы с запросом отсутствуют).

## Классы

### `AliexpressAffiliateOrderGetRequest`

**Описание**: Класс для взаимодействия с API AliExpress для получения данных о заказах аффилированного партнера.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует экземпляр класса.
    **Параметры**:
        - `domain` (str, опционально "api-sg.aliexpress.com"): Домен API.
        - `port` (int, опционально 80): Порт API.
    **Возвращает**:
        - None

- `getapiname(self)`:
    **Описание**: Возвращает имя API метода для получения данных о заказах.
    **Параметры**:
        - Нет
    **Возвращает**:
        - str: Имя API метода (`aliexpress.affiliate.order.get`).