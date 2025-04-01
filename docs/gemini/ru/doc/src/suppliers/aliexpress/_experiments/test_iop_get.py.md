# Модуль для экспериментов с IOP и AliExpress API

## Обзор

Модуль `test_iop_get.py` предназначен для экспериментов с IOP (Internet Open Protocol) клиентом для взаимодействия с AliExpress API. Он демонстрирует процесс создания запросов к API AliExpress и обработки ответов.

## Подробнее

Данный модуль содержит примеры запросов к AliExpress API с использованием библиотеки `iop`. Он демонстрирует создание IOP клиента, формирование запросов к API AliExpress и обработку полученных ответов. Модуль предназначен для тестирования и отладки взаимодействия с AliExpress API.

## Функции

### `IopClient`

```python
class IopClient:
    """
    Args:
        url (str): URL для подключения к API.
        appkey (str): Ключ приложения.
        appSecret (str): Секрет приложения.
    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
```

### `IopRequest`

```python
class IopRequest:
    """
    Args:
        method (str): Метод API для выполнения запроса.
    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
```

## Пример использования

```python
import iop

# Создание клиента IOP для взаимодействия с API AliExpress
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
client.log_level = iop.P_LOG_LEVEL_DEBUG

# Создание запроса к API для генерации партнерской ссылки
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')

# Выполнение запроса и получение ответа
response = client.execute(request)

# Вывод информации об ответе
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
...
```