# Документация модуля `test_internal.py`

## Оглавление
1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Клиент IOP](#клиент-iop)
4. [Запрос API](#запрос-api)
5. [Обработка ответа](#обработка-ответа)

## Обзор

Данный модуль `test_internal.py` предназначен для демонстрации работы с API через библиотеку `iop`. Он устанавливает соединение с API, выполняет запрос и обрабатывает полученный ответ. Основная цель этого модуля — показать, как использовать `iop` для отправки GET-запросов с параметрами и как анализировать ответ сервера.

## Импорты

В этом модуле используются следующие импорты:

- `iop`: Библиотека для взаимодействия с API.
- `time`: Модуль для работы со временем.

## Клиент IOP

### `IopClient`

**Описание**:
Создается экземпляр клиента `IopClient` для взаимодействия с API.

**Параметры**:
- `url` (str): URL-адрес API-шлюза.
- `appkey` (str): Ключ приложения.
- `appSecret` (str): Секретный ключ приложения.

```python
client = iop.IopClient('https://api-pre.taobao.tw/rest', '100240', 'hLeciS15d7UsmXKoND76sBVPpkzepxex')
```

## Запрос API

### `IopRequest`

**Описание**:
Создается запрос `IopRequest` к API.

**Параметры**:
- `api_path` (str): Путь к API-методу.
- `http_method` (str): HTTP метод запроса (например, 'GET').

```python
request = iop.IopRequest('/product/item/get', 'GET')
```

### `add_api_param`

**Описание**:
Добавляются параметры к запросу.

**Параметры**:
- `param_name` (str): Имя параметра.
- `param_value` (str): Значение параметра.

```python
request.add_api_param('itemId','157432005')
request.add_api_param('authDO', '{"sellerId":2000000016002}')
```

### `execute`

**Описание**:
Выполняется запрос к API с помощью клиента `IopClient`.

**Параметры**:
- `request` (iop.IopRequest): Экземпляр запроса `IopRequest`.

**Возвращает**:
- `response` (iop.IopResponse): Объект ответа `IopResponse`, содержащий информацию о результате запроса.

```python
response = client.execute(request)
```
## Обработка ответа

**Описание**:
После выполнения запроса обрабатывается ответ, печатаются различные атрибуты ответа, включая тип, код, сообщение, идентификатор запроса и тело ответа.

```python
# response type nil,ISP,ISV,SYSTEM
# nil ：no error
# ISP : API Service Provider Error
# ISV : API Request Client Error
# SYSTEM : Iop platform Error
print(response.type)

# response code, 0 is no error
print(response.code)

# response error message
print(response.message)

# response unique id
print(response.request_id)

# full response
print(response.body)
```
**Описание**:
Вывод текущего времени в формате timestamp.
```python
print(str(round(time.time())) + '000')
```