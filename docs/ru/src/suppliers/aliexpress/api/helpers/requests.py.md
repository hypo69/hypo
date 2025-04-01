# Модуль для выполнения API-запросов к AliExpress

## Обзор

Модуль `requests.py` содержит функцию `api_request`, которая отправляет запросы к API AliExpress, обрабатывает ответы и возвращает результаты. Он включает обработку ошибок, логирование и преобразование ответов в удобный формат.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с API AliExpress. Он обрабатывает запросы, проверяет коды ответов и преобразует JSON-ответы в объекты `SimpleNamespace` для удобного доступа к данным.

## Функции

### `api_request`

```python
def api_request(request, response_name, attemps: int = 1) -> SimpleNamespace | None:
    """
    Выполняет API-запрос, обрабатывает ответ и возвращает результат.

    Args:
        request: Объект запроса, содержащий метод `getResponse()` для отправки запроса.
        response_name (str): Имя поля в ответе, содержащего полезные данные.
        attemps (int): Количество попыток выполнения запроса. По умолчанию 1.

    Returns:
        SimpleNamespace | None: Результат запроса в виде объекта `SimpleNamespace` или `None` в случае ошибки.

    Raises:
        ApiRequestException: Если при выполнении запроса возникает исключение.
        ApiRequestResponseException: Если ответ API содержит ошибку.
    """
```

**Как работает функция**:

1. **Выполнение запроса**:
   - Функция пытается выполнить запрос с помощью метода `getResponse()` объекта `request`.
   - Если происходит исключение, оно регистрируется в логе.

2. **Обработка ответа**:
   - Извлекается поле `response_name` из ответа, а затем поле `resp_result`.
   - Ответ преобразуется из JSON-строки в объект `SimpleNamespace` для удобного доступа к данным.

3. **Проверка кода ответа**:
   - Проверяется поле `resp_code` в ответе. Если код равен 200, возвращается поле `result`.
   - Если код отличается от 200, в лог записывается предупреждение.

4. **Обработка ошибок**:
   - Если на каком-либо этапе возникает исключение, оно логируется и возвращается `None`.

**Примеры**:

```python
# Пример использования функции api_request
from types import SimpleNamespace
class MockRequest:
    def getResponse(self):
        return {
            'some_response': {
                'resp_result': {
                    'resp_code': 200,
                    'result': {'data': 'example data'}
                }
            }
        }

request = MockRequest()
response_name = 'some_response'
result = api_request(request, response_name)
if result:
    print(result.data)  # Вывод: example data