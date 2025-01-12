# Модуль `src.suppliers.aliexpress.api.errors`

## Обзор

Модуль `src.suppliers.aliexpress.api.errors` предназначен для управления исключениями, специфичными для API AliExpress. Он импортирует все исключения, определенные в подмодуле `exceptions`.

## Оглавление

- [Исключения](#Исключения)

## Исключения

### Импортированные исключения

Этот раздел включает в себя все исключения, импортированные из модуля `exceptions`. Детали этих исключений можно найти в документации к модулю `exceptions`.

- `AliexpressAPIError`: Базовый класс для всех исключений, специфичных для API AliExpress.
- `AliexpressRequestError`: Исключение, возникающее при ошибке запроса к API AliExpress.
- `AliexpressResponseError`: Исключение, возникающее при ошибке ответа от API AliExpress.
- `AliexpressAuthError`: Исключение, возникающее при ошибке аутентификации в API AliExpress.
- `AliexpressRateLimitError`: Исключение, возникающее при достижении лимита запросов к API AliExpress.
- `AliexpressNotFoundError`: Исключение, возникающее, когда запрашиваемый ресурс не найден в API AliExpress.
- `AliexpressInternalServerError`: Исключение, возникающее при внутренней ошибке сервера API AliExpress.
- `AliexpressInvalidParameterError`: Исключение, возникающее при передаче неверных параметров в API AliExpress.
- `AliexpressTimeoutError`: Исключение, возникающее, когда время ожидания ответа от API AliExpress истекло.
- `AliexpressUnknownError`: Исключение, возникающее при неизвестной ошибке от API AliExpress.