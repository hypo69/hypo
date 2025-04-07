# Модуль для экспериментов с IOP (aliexpress)

## Обзор

Этот модуль содержит экспериментальный код для взаимодействия с API AliExpress через протокол IOP. В частности, он демонстрирует, как генерировать партнерские ссылки с использованием API `aliexpress.affiliate.link.generate`.

## Подробней

Этот код предназначен для тестирования и демонстрации взаимодействия с API AliExpress с использованием библиотеки `iop`. Он содержит примеры создания запросов, установки параметров и обработки ответов. Этот модуль может служить отправной точкой для разработчиков, желающих интегрировать функциональность AliExpress в свои приложения.

## Функции

### `IopClient`

```python
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
```

**Назначение**: Создание клиента IOP для взаимодействия с API AliExpress.

**Параметры**:

-   `url` (str): URL-адрес gateway API AliExpress.
-   `appkey` (str): Ключ приложения, полученный от AliExpress.
-   `appSecret` (str): Секрет приложения, полученный от AliExpress.

**Как работает функция**:

1.  Создается экземпляр класса `IopClient` с переданными параметрами.
2.  Устанавливается уровень логирования клиента на `iop.P_LOG_LEVEL_DEBUG`.

### `IopRequest`

```python
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')
```

**Назначение**: Создание запроса к API AliExpress для генерации партнерской ссылки.

**Параметры**:

-   `api_method` (str): Название вызываемого API метода (`aliexpress.affiliate.link.generate`).
-   `promotion_link_type` (str): Тип партнерской ссылки (в данном случае `'0'`).
-   `source_values` (str): URL товара на AliExpress, для которого необходимо сгенерировать ссылку.
-   `tracking_id` (str): Идентификатор отслеживания, используемый для учета переходов по ссылке.

**Как работает функция**:

1.  Создается экземпляр класса `IopRequest` с указанным API методом.
2.  Добавляются параметры запроса с помощью метода `add_api_param`.

```
Начало
│
├── Создание запроса (IopRequest)
│
├── Добавление параметров (add_api_param)
│
Конец
```

### `client.execute`

```python
response = client.execute(request)
```

**Назначение**: Выполнение запроса к API AliExpress.

**Параметры**:

-   `request` (iop.IopRequest): Объект запроса, созданный ранее.

**Как работает функция**:

1.  Выполняется запрос к API AliExpress с использованием метода `execute` объекта `IopClient`.
2.  Полученный ответ сохраняется в переменной `response`.

```
Начало
│
├── Выполнение запроса (client.execute)
│
├── Получение ответа (response)
│
Конец
```

### Обработка ответа

```python
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

**Назначение**: Вывод информации об ответе, полученном от API AliExpress.

**Параметры**:

-   `response` (iop.IopResponse): Объект ответа, полученный после выполнения запроса.

**Как работает функция**:

1.  Выводится тело ответа (`response.body`).
2.  Выводится тип ответа (`response.type`).
3.  Выводится код ответа (`response.code`).
4.  Выводится сообщение об ошибке (`response.message`).
5.  Выводится уникальный идентификатор запроса (`response.request_id`).
6.  Повторно выводится тело ответа (`response.body`).

## Примеры

```python
import iop

# Создание клиента IOP
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
client.log_level = iop.P_LOG_LEVEL_DEBUG

# Создание запроса для генерации партнерской ссылки
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')

# Выполнение запроса
response = client.execute(request)

# Вывод информации об ответе
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)