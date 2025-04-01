# Модуль исключений для API AliExpress

## Обзор

Модуль содержит пользовательские исключения, используемые для обработки ошибок, возникающих при взаимодействии с API AliExpress. Он определяет базовый класс `AliexpressException`, от которого наследуются все остальные исключения, специфичные для API AliExpress.

## Подробнее

Этот модуль предоставляет набор исключений, которые могут быть вызваны при различных сценариях ошибок, таких как неверные аргументы, отсутствие идентификатора продукта, сбои запросов к API и т.д. Использование этих исключений позволяет более эффективно обрабатывать ошибки и предоставлять информативные сообщения об ошибках.

## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений API AliExpress.

**Методы**:
- `__init__`: Конструктор класса, принимающий причину исключения.
- `__str__`: Возвращает строковое представление исключения.

**Параметры**:
- `reason` (str): Причина исключения.

**Примеры**

```python
    try:
        raise AliexpressException('Произошла ошибка при работе с API AliExpress')
    except AliexpressException as ex:
        print(f'Ошибка: {ex}')
```

### `InvalidArgumentException`

**Описание**: Исключение, вызываемое при некорректных аргументах.

**Примеры**

```python
    try:
        raise InvalidArgumentException('Неверный аргумент')
    except InvalidArgumentException as ex:
        print(f'Ошибка: {ex}')
```

### `ProductIdNotFoundException`

**Описание**: Исключение, вызываемое, если идентификатор продукта не найден.

**Примеры**

```python
    try:
        raise ProductIdNotFoundException('Идентификатор продукта не найден')
    except ProductIdNotFoundException as ex:
        print(f'Ошибка: {ex}')
```

### `ApiRequestException`

**Описание**: Исключение, вызываемое при сбое запроса к API AliExpress.

**Примеры**

```python
    try:
        raise ApiRequestException('Сбой запроса к API AliExpress')
    except ApiRequestException as ex:
        print(f'Ошибка: {ex}')
```

### `ApiRequestResponseException`

**Описание**: Исключение, вызываемое, если ответ API-запроса недействителен.

**Примеры**

```python
    try:
        raise ApiRequestResponseException('Недействительный ответ API-запроса')
    except ApiRequestResponseException as ex:
        print(f'Ошибка: {ex}')
```

### `ProductsNotFoudException`

**Описание**: Исключение, вызываемое, если продукты не найдены.

**Примеры**

```python
    try:
        raise ProductsNotFoudException('Продукты не найдены')
    except ProductsNotFoudException as ex:
        print(f'Ошибка: {ex}')
```

### `CategoriesNotFoudException`

**Описание**: Исключение, вызываемое, если категории не найдены.

**Примеры**

```python
    try:
        raise CategoriesNotFoudException('Категории не найдены')
    except CategoriesNotFoudException as ex:
        print(f'Ошибка: {ex}')
```

### `InvalidTrackingIdException`

**Описание**: Исключение, вызываемое, если идентификатор отслеживания отсутствует или недействителен.

**Примеры**

```python
    try:
        raise InvalidTrackingIdException('Недействительный идентификатор отслеживания')
    except InvalidTrackingIdException as ex:
        print(f'Ошибка: {ex}')
```