# Документация модуля `exceptions.py`

## Обзор

Модуль содержит пользовательские исключения, специфичные для работы с AliExpress API. Эти исключения используются для обработки различных ошибок, которые могут возникнуть в процессе взаимодействия с API, таких как некорректные аргументы, отсутствие продуктов, неверные идентификаторы и т.д.

## Оглавление

- [Классы](#Классы)
  - [`AliexpressException`](#AliexpressException)
  - [`InvalidArgumentException`](#InvalidArgumentException)
  - [`ProductIdNotFoundException`](#ProductIdNotFoundException)
  - [`ApiRequestException`](#ApiRequestException)
  - [`ApiRequestResponseException`](#ApiRequestResponseException)
  - [`ProductsNotFoudException`](#ProductsNotFoudException)
  - [`CategoriesNotFoudException`](#CategoriesNotFoudException)
  - [`InvalidTrackingIdException`](#InvalidTrackingIdException)

## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений, связанных с AliExpress API.

**Методы**:
- `__init__`:
    
    **Описание**: Конструктор класса `AliexpressException`.
    
    **Параметры**:
        - `reason` (str):  Причина исключения.
- `__str__`:
   
   **Описание**: Возвращает строковое представление исключения.
   
   **Возвращает**:
        - `str`:  Строковое представление причины исключения.

### `InvalidArgumentException`

**Описание**: Исключение, возникающее при передаче некорректных аргументов.

### `ProductIdNotFoundException`

**Описание**: Исключение, возникающее, если продукт с заданным ID не найден.

### `ApiRequestException`

**Описание**: Исключение, возникающее при неудачном запросе к AliExpress API.

### `ApiRequestResponseException`

**Описание**: Исключение, возникающее, если ответ от AliExpress API не является валидным.

### `ProductsNotFoudException`

**Описание**: Исключение, возникающее, если не найдено ни одного продукта.

### `CategoriesNotFoudException`

**Описание**: Исключение, возникающее, если не найдено ни одной категории.

### `InvalidTrackingIdException`

**Описание**: Исключение, возникающее, если идентификатор отслеживания недействителен.