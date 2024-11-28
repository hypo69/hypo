# Модуль hypotez/src/suppliers/aliexpress/api/errors/exceptions.py

## Обзор

Данный модуль содержит пользовательские исключения для работы с API AliExpress.  Он определяет базовый класс исключений `AliexpressException` и ряд дочерних классов для различных ситуаций ошибок.

## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений, связанных с API AliExpress.  Содержит причину ошибки.

**Методы**:

- `__init__(self, reason: str)`: Инициализирует исключение с указанием причины.
- `__str__(self) -> str`: Возвращает строковое представление исключения, содержащее причину.


### `InvalidArgumentException`

**Описание**:  Исключение, которое возникает, когда переданные аргументы некорректны.

**Наследуется от**: `AliexpressException`


### `ProductIdNotFoundException`

**Описание**: Исключение, которое возникает, если идентификатор продукта не найден.

**Наследуется от**: `AliexpressException`


### `ApiRequestException`

**Описание**: Исключение, возникающее при сбое запроса к API AliExpress.

**Наследуется от**: `AliexpressException`


### `ApiRequestResponseException`

**Описание**: Исключение, возникающее, если ответ от API AliExpress не является валидным.

**Наследуется от**: `AliexpressException`


### `ProductsNotFoudException`

**Описание**: Исключение, которое возникает, если не найдено ни одного продукта.

**Наследуется от**: `AliexpressException`


### `CategoriesNotFoudException`

**Описание**: Исключение, которое возникает, если не найдено ни одной категории.

**Наследуется от**: `AliexpressException`


### `InvalidTrackingIdException`

**Описание**: Исключение, которое возникает, если идентификатор отслеживания отсутствует или некорректен.

**Наследуется от**: `AliexpressException`