# Модуль `exceptions`

## Обзор

Модуль `exceptions` содержит пользовательские исключения, специфичные для работы с API AliExpress. Эти исключения наследуются от базового класса `AliexpressException` и используются для обработки различных ошибок, которые могут возникнуть при взаимодействии с API.

## Оглавление
1. [Классы](#классы)
    - [`AliexpressException`](#aliexpressexception)
    - [`InvalidArgumentException`](#invalidargumentexception)
    - [`ProductIdNotFoundException`](#productidnotfoundexception)
    - [`ApiRequestException`](#apirequestexception)
    - [`ApiRequestResponseException`](#apirequestresponseexception)
    - [`ProductsNotFoudException`](#productsnotfoudexception)
    - [`CategoriesNotFoudException`](#categoriesnotfoudexception)
    - [`InvalidTrackingIdException`](#invalidtrackingidexception)

## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений API AliExpress.

**Методы**:
- `__init__`: Конструктор класса.
- `__str__`: Возвращает строковое представление исключения.

#### `__init__`
**Описание**: Инициализирует объект исключения с заданной причиной.

**Параметры**:
- `reason` (str): Причина исключения.

#### `__str__`
**Описание**: Возвращает строковое представление исключения.

**Возвращает**:
- `str`: Строковое представление причины исключения.

### `InvalidArgumentException`

**Описание**: Исключение, которое возникает, когда аргументы некорректны.

### `ProductIdNotFoundException`

**Описание**: Исключение, которое возникает, если ID продукта не найден.

### `ApiRequestException`

**Описание**: Исключение, которое возникает, если запрос к API AliExpress не удался.

### `ApiRequestResponseException`

**Описание**: Исключение, которое возникает, если ответ от API AliExpress недействителен.

### `ProductsNotFoudException`

**Описание**: Исключение, которое возникает, если не найдено ни одного продукта.

### `CategoriesNotFoudException`

**Описание**: Исключение, которое возникает, если не найдено ни одной категории.

### `InvalidTrackingIdException`

**Описание**: Исключение, которое возникает, если ID отслеживания недействителен или отсутствует.