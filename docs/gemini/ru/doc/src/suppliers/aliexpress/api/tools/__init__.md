# Модуль hypotez/src/suppliers/aliexpress/api/tools

## Обзор

Данный модуль содержит вспомогательные инструменты для работы с API AliExpress.  Он предоставляет функции для взаимодействия с API, облегчая процесс получения данных.

## Функции

### `get_product_id`

**Описание**: Функция для получения идентификатора продукта AliExpress.


**Параметры**:

- `product_name` (str): Название продукта.


**Возвращает**:

- `int | None`: Идентификатор продукта, если успешно получен, иначе `None`.


**Вызывает исключения**:

- `ValueError`: Если `product_name` является пустой строкой или содержит некорректные символы.
- `HTTPError`: Возникает при ошибках запроса к API.
- `JSONDecodeError`: При проблемах с декодированием ответа API.
- `OtherError`: В случае возникновения непредвиденной ошибки.