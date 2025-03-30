# Модуль `requests`

## Обзор

Модуль `requests` предоставляет функцию `api_request`, которая используется для выполнения запросов к API AliExpress и обработки ответов. Она включает в себя обработку ошибок, логирование и преобразование JSON-ответов в объекты `SimpleNamespace`.

## Подробней

Этот модуль разработан для упрощения взаимодействия с API AliExpress. Он оборачивает запросы, обрабатывает возможные исключения и преобразует ответы в удобный формат для дальнейшего использования. Функция `api_request` принимает запрос, имя ожидаемого ответа и количество попыток выполнения запроса. В случае успеха возвращает результат, в противном случае логирует ошибку и возвращает `None`.

## Функции

### `api_request`

```python
def api_request(request, response_name, attemps:int = 1) -> SimpleNamespace | None:
    """
    Args:
        request: Объект запроса, содержащий метод `getResponse` для получения ответа от API.
        response_name (str): Ключ, используемый для извлечения полезных данных из ответа.
        attemps (int, optional): Количество попыток выполнения запроса. По умолчанию равен 1.

    Returns:
        SimpleNamespace | None: Преобразованный ответ API в виде объекта SimpleNamespace,
                            или None в случае ошибки.

    Raises:
        ApiRequestException: Если происходит ошибка при выполнении запроса.
        ApiRequestResponseException: Если получен некорректный ответ от API.

    Example:
        Предположим, у вас есть объект `request` и имя ответа `products`:

        >>> request_object = ...  # Объект запроса, который можно вызвать request_object.getResponse()
        >>> response = api_request(request_object, 'products')
        >>> if response:
        ...     print(response.product_list[0].name)  # Пример доступа к данным
    """
    ...
```

**Описание**: Функция выполняет запрос к API, обрабатывает ответ и возвращает результат.

**Параметры**:
- `request`: Объект запроса, содержащий метод `getResponse` для получения ответа от API.
- `response_name` (str): Ключ, используемый для извлечения полезных данных из ответа.
- `attemps` (int, optional): Количество попыток выполнения запроса. По умолчанию равен 1.

**Возвращает**:
- `SimpleNamespace | None`: Преобразованный ответ API в виде объекта `SimpleNamespace`, или `None` в случае ошибки.

**Вызывает исключения**:
- `ApiRequestException`: Если происходит ошибка при выполнении запроса.
- `ApiRequestResponseException`: Если получен некорректный ответ от API.

**Примеры**:

Пример успешного выполнения запроса:

```python
request_object = ...  # Объект запроса, который можно вызвать request_object.getResponse()
response = api_request(request_object, 'products')
if response:
    print(response.product_list[0].name)  # Пример доступа к данным
```

Пример обработки ошибки:

```python
request_object = ...  # Объект запроса, который может вызвать исключение
response = api_request(request_object, 'products')
if response is None:
    print("Запрос не удался.")
```