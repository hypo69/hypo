# src.suppliers.aliexpress.api.errors.exceptions

## Обзор

Модуль содержит пользовательские исключения, используемые в API AliExpress. Эти исключения наследуются от общего класса `AliexpressException` и предназначены для обработки различных ошибок, которые могут возникнуть при взаимодействии с API AliExpress.

## Подробней

Модуль предоставляет набор исключений, специфичных для API AliExpress, что позволяет более точно обрабатывать ошибки и предоставлять информативные сообщения об ошибках. Исключения охватывают различные сценарии, такие как неверные аргументы, отсутствие идентификатора продукта, сбои запросов к API и неверные ответы API.

## Классы

### `AliexpressException`

**Описание**: Общий базовый класс для всех исключений API AliExpress.

**Методы**:
- `__init__`: Инициализирует исключение с указанием причины.
- `__str__`: Возвращает строковое представление причины исключения.

**Параметры**:
- `reason` (str): Причина возникновения исключения.

**Примеры**
```python
try:
    raise AliexpressException('Ошибка подключения к API')
except AliexpressException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `InvalidArgumentException`

**Описание**: Исключение, возникающее, когда аргументы неверны.

**Примеры**
```python
try:
    raise InvalidArgumentException('Неверный формат аргумента')
except InvalidArgumentException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `ProductIdNotFoundException`

**Описание**: Исключение, возникающее, если идентификатор продукта не найден.

**Примеры**
```python
try:
    raise ProductIdNotFoundException('Идентификатор продукта не найден')
except ProductIdNotFoundException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `ApiRequestException`

**Описание**: Исключение, возникающее, если запрос к API AliExpress завершается неудачей.

**Примеры**
```python
try:
    raise ApiRequestException('Сбой запроса к API AliExpress')
except ApiRequestException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `ApiRequestResponseException`

**Описание**: Исключение, возникающее, если ответ на запрос недействителен.

**Примеры**
```python
try:
    raise ApiRequestResponseException('Недействительный ответ на запрос')
except ApiRequestResponseException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `ProductsNotFoudException`

**Описание**: Исключение, возникающее, если продукты не найдены.

**Примеры**
```python
try:
    raise ProductsNotFoudException('Продукты не найдены')
except ProductsNotFoudException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `CategoriesNotFoudException`

**Описание**: Исключение, возникающее, если категории не найдены.

**Примеры**
```python
try:
    raise CategoriesNotFoudException('Категории не найдены')
except CategoriesNotFoudException as ex:
    print(f'Произошла ошибка: {ex}')
```

### `InvalidTrackingIdException`

**Описание**: Исключение, возникающее, если идентификатор отслеживания отсутствует или недействителен.

**Примеры**
```python
try:
    raise InvalidTrackingIdException('Недопустимый идентификатор отслеживания')
except InvalidTrackingIdException as ex:
    print(f'Произошла ошибка: {ex}')
```