# Модуль `hypotez/src/suppliers/aliexpress/api/errors/exceptions.py`

## Обзор

Модуль `exceptions.py` содержит пользовательские исключения, предназначенные для обработки ошибок, возникающих при взаимодействии с API AliExpress.  Он определяет базовый класс `AliexpressException` и ряд специфических исключений для различных сценариев ошибок.

## Оглавление

- [Модуль `exceptions.py`](#модуль-exceptionspy)
- [Класс `AliexpressException`](#класс-aliexpressexception)
- [Класс `InvalidArgumentException`](#класс-invalidargumentexception)
- [Класс `ProductIdNotFoundException`](#класс-productidnotfoundexception)
- [Класс `ApiRequestException`](#класс-apirequestexception)
- [Класс `ApiRequestResponseException`](#класс-apirequestresponseexception)
- [Класс `ProductsNotFoudException`](#класс-productsnotfoudexception)
- [Класс `CategoriesNotFoudException`](#класс-categoriesnotfoudexception)
- [Класс `InvalidTrackingIdException`](#класс-invalidtrackingidexception)


## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений, связанных с API AliExpress. Содержит причину ошибки.

**Методы**:

- `__init__(self, reason: str)`:
    **Описание**: Инициализирует экземпляр исключения с причиной.
    **Параметры**:
    - `reason` (str): Текстовое описание причины ошибки.
    **Возвращает**:
    - None

- `__str__(self) -> str`:
    **Описание**: Возвращает строковое представление исключения, содержащее причину.
    **Параметры**:
    - None
    **Возвращает**:
    - str: Строковое представление исключения.


### `InvalidArgumentException`

**Описание**: Исключение, выбрасывается, когда предоставленные аргументы некорректны.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `ProductIdNotFoundException`

**Описание**: Исключение, выбрасывается, когда указанный ID продукта не найден.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `ApiRequestException`

**Описание**: Исключение, выбрасывается, когда запрос к API AliExpress завершился неудачно.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `ApiRequestResponseException`

**Описание**: Исключение, выбрасывается, когда ответ от API AliExpress некорректен.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `ProductsNotFoudException`

**Описание**: Исключение, выбрасывается, когда не найдены продукты.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `CategoriesNotFoudException`

**Описание**: Исключение, выбрасывается, когда не найдены категории.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)


### `InvalidTrackingIdException`

**Описание**: Исключение, выбрасывается, когда идентификатор отслеживания не существует или некорректен.

**Наследует**: `AliexpressException`

**Методы**:
 - `__init__` (унаследован от `AliexpressException`)