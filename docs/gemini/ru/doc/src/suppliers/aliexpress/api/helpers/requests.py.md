# Модуль для выполнения API запросов к AliExpress

## Обзор

Модуль `requests.py` содержит функции для выполнения API запросов к AliExpress. Он обрабатывает запросы, проверяет ответы и возвращает результаты.
Он содержит функцию `api_request`, которая выполняет запрос к API и обрабатывает возможные ошибки и исключения.

## Подробнее

Этот модуль предназначен для упрощения процесса выполнения API запросов к AliExpress. Он предоставляет единую точку входа для выполнения запросов, обработки ответов и обработки ошибок. Модуль использует библиотеку `logger` для логирования ошибок и предупреждений, что упрощает отладку и мониторинг.

## Функции

### `api_request`

```python
def api_request(request, response_name, attemps:int = 1) -> SimpleNamespace | None:
    """
    Выполняет API запрос и обрабатывает ответ.

    Args:
        request: Объект запроса, содержащий метод `getResponse()`.
        response_name (str): Имя поля в ответе, содержащего результат.
        attemps (int, optional): Количество попыток выполнения запроса. По умолчанию 1.

    Returns:
        SimpleNamespace | None: Результат запроса в виде объекта SimpleNamespace или None в случае ошибки.

    Raises:
        ApiRequestException: Если при выполнении запроса произошла ошибка.
        ApiRequestResponseException: Если код ответа не равен 200.

    Example:
        >>> request = SomeRequestObject()
        >>> response = api_request(request, 'some_response')
        >>> if response:
        >>>     print(response.some_field)
    """
```

**Назначение**:
Функция `api_request` выполняет API запрос, обрабатывает ответ и возвращает результат в виде объекта `SimpleNamespace`. Функция также обрабатывает исключения, которые могут возникнуть в процессе выполнения запроса или обработки ответа.

**Параметры**:
- `request`: Объект запроса, содержащий метод `getResponse()`.
- `response_name` (str): Имя поля в ответе, содержащего результат.
- `attemps` (int, optional): Количество попыток выполнения запроса. По умолчанию `1`.

**Возвращает**:
- `SimpleNamespace | None`: Результат запроса в виде объекта `SimpleNamespace` или `None` в случае ошибки.

**Вызывает исключения**:
- `ApiRequestException`: Если при выполнении запроса произошла ошибка.
- `ApiRequestResponseException`: Если код ответа не равен 200.

**Как работает функция**:

1.  **Попытка выполнения запроса**: Функция пытается выполнить запрос, вызывая метод `getResponse()` объекта `request`.
2.  **Обработка исключений при выполнении запроса**: Если при выполнении запроса возникает исключение, оно перехватывается.  В случае возникновения исключения, функция возвращает `None`.
3.  **Обработка ответа**: Если запрос выполнен успешно, функция пытается извлечь результат из ответа.
    - Извлекает значение из поля `response_name` ответа.
    - Преобразует результат в JSON-строку, а затем в объект `SimpleNamespace`.
4.  **Обработка исключений при обработке ответа**: Если при обработке ответа возникает исключение, оно перехватывается, логируется с использованием `logger.critical` и возвращается `None`.
5.  **Проверка кода ответа**: Функция проверяет код ответа `response.resp_code`. Если код ответа равен 200, функция возвращает результат `response.result`. В противном случае логирует предупреждение с использованием `logger.warning` и возвращает `None`.
6.  **Обработка исключений при проверке ответа**: Если при проверке ответа возникает исключение, оно перехватывается, логируется с использованием `logger.error`, при этом  передавая информацию об исключении в `logger`, и возвращает `None`.

**ASCII flowchart**:

```
Начало
    ↓
Попытка получить ответ от API (request.getResponse())
    ↓
Успех?
    ├── Да → Извлечение и преобразование данных из ответа
    │       ↓
    │       Успешно?
    │       ├── Да → Проверка кода ответа (response.resp_code == 200)
    │       │       ↓
    │       │       Код 200?
    │       │       ├── Да → Возврат response.result
    │       │       └── Нет → Логирование предупреждения и возврат None
    │       └── Нет → Логирование критической ошибки и возврат None
    └── Нет →  Возврат None
```

**Примеры**:

```python
# Пример 1: Успешный запрос
request = MockRequest()  # Объект, имитирующий запрос
request.response_data = {"some_response": {"resp_result": {"resp_code": 200, "result": {"data": "some data"}}}}
response = api_request(request, "some_response")
if response:
    print(response.data)  # Вывод: some data

# Пример 2: Неуспешный запрос (код ответа не 200)
request = MockRequest()
request.response_data = {"some_response": {"resp_result": {"resp_code": 400, "resp_msg": "Bad Request"}}}
response = api_request(request, "some_response")
if not response:
    print("Request failed")  # Вывод: Request failed

# Пример 3: Исключение при выполнении запроса
request = MockRequest()
request.raise_exception = True  # Имитация ошибки при запросе
response = api_request(request, "some_response")
if not response:
    print("Request failed due to exception")  # Вывод: Request failed due to exception