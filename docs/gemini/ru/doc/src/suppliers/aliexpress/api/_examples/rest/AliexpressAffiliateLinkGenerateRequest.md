# Модуль aliexpress/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateLinkGenerateRequest.py

## Обзор

Этот модуль содержит класс `AliexpressAffiliateLinkGenerateRequest`, представляющий собой запрос для генерации ссылки партнера AliExpress. Он наследуется от базового класса `RestApi` и предоставляет методы для инициализации запроса и получения имени API.

## Классы

### `AliexpressAffiliateLinkGenerateRequest`

**Описание**: Класс, реализующий запрос для генерации ссылки партнера AliExpress.

**Методы**:

- `__init__(self, domain="api-sg.aliexpress.com", port=80)`:
    **Описание**: Инициализирует объект запроса.
    
    **Параметры**:
    - `domain` (str, опционально "api-sg.aliexpress.com"): Домен API. По умолчанию "api-sg.aliexpress.com".
    - `port` (int, опционально 80): Порт API. По умолчанию 80.
    
    **Возвращает**:
    - `None`


- `getapiname(self)`:
    **Описание**: Возвращает имя API запроса.
    
    **Параметры**:
    - Нет

    **Возвращает**:
    - `str`: Имя API запроса - "aliexpress.affiliate.link.generate".