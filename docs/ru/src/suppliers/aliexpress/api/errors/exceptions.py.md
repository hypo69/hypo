# Модуль `exceptions.py`

## Обзор

Модуль содержит пользовательские исключения для работы с API AliExpress. Он определяет базовый класс `AliexpressException`, от которого наследуются все остальные исключения, специфичные для AliExpress.

## Подробнее

Этот модуль предназначен для централизованной обработки ошибок, возникающих при взаимодействии с API AliExpress. Он предоставляет набор исключений, которые могут быть вызваны в различных ситуациях, таких как некорректные аргументы, отсутствие продукта по идентификатору, сбои запросов к API и т.д. Использование пользовательских исключений позволяет более четко и структурированно обрабатывать ошибки в коде, а также предоставляет возможность для более детальной диагностики проблем.

## Классы

### `AliexpressException`

**Описание**: Базовый класс для всех исключений, связанных с API AliExpress.

**Принцип работы**:
Класс `AliexpressException` наследуется от стандартного класса `Exception` и служит базовым классом для всех пользовательских исключений, определенных в этом модуле. Он принимает аргумент `reason`, который содержит описание причины возникновения исключения.

**Методы**:
- `__init__(self, reason: str)`: Конструктор класса, принимающий строку с описанием причины исключения.
- `__str__(self) -> str`: Возвращает строковое представление исключения, содержащее причину ошибки.

**Параметры**:
- `reason` (str): Описание причины возникновения исключения.

**Примеры**:
```python
try:
    raise AliexpressException('Some error occurred')
except AliexpressException as ex:
    print(ex)  # Вывод: Some error occurred
```

### `InvalidArgumentException`

**Описание**: Исключение, вызываемое при некорректных аргументах.

**Принцип работы**:
Класс `InvalidArgumentException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда аргументы, переданные в функцию или метод, не соответствуют ожидаемым значениям или типам.

**Примеры**:
```python
try:
    raise InvalidArgumentException('Invalid argument provided')
except InvalidArgumentException as ex:
    print(ex)  # Вывод: Invalid argument provided
```

### `ProductIdNotFoundException`

**Описание**: Исключение, вызываемое, если идентификатор продукта не найден.

**Принцип работы**:
Класс `ProductIdNotFoundException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда продукт с указанным идентификатором не найден в базе данных или API AliExpress.

**Примеры**:
```python
try:
    raise ProductIdNotFoundException('Product ID not found')
except ProductIdNotFoundException as ex:
    print(ex)  # Вывод: Product ID not found
```

### `ApiRequestException`

**Описание**: Исключение, вызываемое при неудачном запросе к API AliExpress.

**Принцип работы**:
Класс `ApiRequestException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда запрос к API AliExpress завершается неудачей из-за сетевых проблем, недоступности сервера или других причин.

**Примеры**:
```python
try:
    raise ApiRequestException('API request failed')
except ApiRequestException as ex:
    print(ex)  # Вывод: API request failed
```

### `ApiRequestResponseException`

**Описание**: Исключение, вызываемое, если ответ API является недействительным.

**Принцип работы**:
Класс `ApiRequestResponseException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда ответ, полученный от API AliExpress, не соответствует ожидаемому формату или содержит некорректные данные.

**Примеры**:
```python
try:
    raise ApiRequestResponseException('Invalid API response')
except ApiRequestResponseException as ex:
    print(ex)  # Вывод: Invalid API response
```

### `ProductsNotFoudException`

**Описание**: Исключение, вызываемое, если продукты не найдены.

**Принцип работы**:
Класс `ProductsNotFoudException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда в результате запроса не найдено ни одного продукта.

**Примеры**:
```python
try:
    raise ProductsNotFoudException('Products not found')
except ProductsNotFoudException as ex:
    print(ex)  # Вывод: Products not found
```

### `CategoriesNotFoudException`

**Описание**: Исключение, вызываемое, если категории не найдены.

**Принцип работы**:
Класс `CategoriesNotFoudException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда в результате запроса не найдено ни одной категории.

**Примеры**:
```python
try:
    raise CategoriesNotFoudException('Categories not found')
except CategoriesNotFoudException as ex:
    print(ex)  # Вывод: Categories not found
```

### `InvalidTrackingIdException`

**Описание**: Исключение, вызываемое, если идентификатор отслеживания отсутствует или является недействительным.

**Принцип работы**:
Класс `InvalidTrackingIdException` наследуется от класса `AliexpressException` и представляет собой исключение, которое возникает, когда идентификатор отслеживания не предоставлен или имеет неверный формат.

**Примеры**:
```python
try:
    raise InvalidTrackingIdException('Invalid tracking ID')
except InvalidTrackingIdException as ex:
    print(ex)  # Вывод: Invalid tracking ID
```