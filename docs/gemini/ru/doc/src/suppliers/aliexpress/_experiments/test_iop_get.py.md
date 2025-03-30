# Модуль для экспериментов с IOP и AliExpress

## Обзор

Этот модуль содержит эксперименты по работе с API AliExpress через IOP (IopClient). Включает в себя примеры запросов к API для генерации партнерских ссылок.

## Подробнее

Модуль предназначен для тестирования и демонстрации взаимодействия с API AliExpress с использованием библиотеки `iop`. Он содержит примеры создания запросов, добавления параметров и обработки ответов от API.

## Функции

### `IopClient`

**Описание**:

Пример инициализации клиента `IopClient` для взаимодействия с API AliExpress.

```python
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
```

**Параметры**:

- `url` (str): URL API AliExpress.
- `appkey` (str): Ключ приложения.
- `appSecret` (str): Секрет приложения.

**Примеры**:

```python
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
client.log_level = iop.P_LOG_LEVEL_DEBUG
```

### `IopRequest`

**Описание**:

Пример создания и выполнения запроса к API AliExpress для генерации партнерской ссылки.

```python
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')
response = client.execute(request)
```

**Параметры**:

- `api_name` (str): Название API метода.
- `params` (dict): Параметры запроса.

**Примеры**:

```python
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')
response = client.execute(request)

print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

### Обработка ответа

**Описание**:

Примеры обработки ответа от API, включая вывод тела ответа, типа, кода, сообщения и ID запроса.

```python
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

**Параметры**:

- `response` (iop.IopResponse): Объект ответа от API.

**Примеры**:

```python
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```