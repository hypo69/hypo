# Модуль `requests.py`

## Обзор

Модуль `requests.py` предоставляет вспомогательную функцию `api_request` для выполнения API-запросов и обработки ответов. Он предназначен для упрощения процесса запросов к API AliExpress, обработки возможных ошибок и возврата результатов.

## Подробней

Этот модуль играет важную роль в проекте `hypotez`, поскольку он абстрагирует детали выполнения HTTP-запросов к API AliExpress и обработки ответов. Функция `api_request` обрабатывает повторные попытки запросов, ошибки соединения и формат ответа, что упрощает остальным частям проекта взаимодействие с API. Он также использует логирование для записи ошибок и предупреждений, что полезно для отладки и мониторинга.

## Функции

### `api_request`

```python
def api_request(request, response_name, attemps:int = 1):
    """
    Args:
        request:
        response_name:
        attemps (int, optional):  Defaults to 1.

    Returns:
        :

    Raises:
        :
    """
```

**Описание**: Выполняет API-запрос и обрабатывает ответ.

**Параметры**:

- `request`: Объект запроса, содержащий информацию для выполнения HTTP-запроса.
- `response_name` (str): Имя поля в ответе, содержащего полезные данные.
- `attemps` (int, optional): Количество попыток выполнения запроса. По умолчанию `1`.

**Возвращает**:

- `SimpleNamespace`: Объект, содержащий результат API-запроса, если запрос выполнен успешно и код ответа равен 200.
- `None`: В случае ошибки или если код ответа не равен 200.

**Вызывает исключения**:

- `ApiRequestException`: Возникает в случае ошибок при выполнении запроса.
- `ApiRequestResponseException`: Возникает в случае ошибок в формате ответа.

**Примеры**:

```python
# Пример вызова функции api_request
# result = api_request(request_object, 'item_detail', attemps=3)
# if result:
#     print(result.title)
```
```python
# Пример обработки ошибок при вызове функции
# try:
#     result = api_request(request_object, 'item_detail')
#     if result:
#         print(result.title)
# except ApiRequestException as ex:
#     logger.error('Ошибка при выполнении запроса', ex, exc_info=True)
```
```python
# Пример обработки ответа с кодом, отличным от 200
# result = api_request(request_object, 'item_detail')
# if result is None:
#     logger.warning('Запрос выполнен, но код ответа не 200')