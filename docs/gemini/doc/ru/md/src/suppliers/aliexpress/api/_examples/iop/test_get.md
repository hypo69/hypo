# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/iop/test_get.py`

## Обзор

Этот модуль содержит пример использования библиотеки `iop` для взаимодействия с API AliExpress. Он демонстрирует, как создать запрос GET-методом к API, выполнить его и обработать полученный ответ.

## Импорты

```python
import iop
```

## Классы

### `IopClient`

**Описание**: Клиент для работы с API AliExpress, использующий библиотеку `iop`.

**Атрибуты**:

- `gateway_url` (str): URL API-шлюза.
- `appkey` (str): Ключ приложения.
- `appSecret` (str): Секрет приложения.

**Методы**:

- `execute(request, request_id)`: Выполняет API-запрос и возвращает ответ.

```python
client = iop.IopClient('https://api-pre.aliexpress.com/sync', '33505222', 'e1fed6b34feb26aabc391d187732af93')
```

### `IopRequest`

**Описание**: Представляет собой API-запрос к AliExpress.

**Атрибуты**:

- `api_name` (str): Имя API-метода.
- `http_method` (str): Тип HTTP-метода (по умолчанию POST).


**Методы**:

- `set_simplify()`: Устанавливает упрощенный режим обработки ответа.
- `add_api_param(param_name, param_value)`: Добавляет параметр к запросу.

```python
request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST')
request.set_simplify()
request.add_api_param('seller_address_query', 'pickup')
```

## Функции


### `main`

**Описание**: Основная функция модуля. Создает клиент, запрос, выполняет запрос и выводит информацию о полученном ответе.


**Параметры**:

- Нет

**Возвращает**:
- Нет

**Обрабатываемые исключения**:
- Не описаны.


```python
response = client.execute(request,"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL")
```


## Обработка ответа

**Описание**: Модуль выводит следующие атрибуты ответа:

- `response.type`: Тип ответа (nil, ISP, ISV, SYSTEM).
- `response.code`: Код ответа (0 - успех).
- `response.message`: Сообщение об ошибке (если есть).
- `response.request_id`: Уникальный идентификатор запроса.
- `response.body`: Полный ответ в формате JSON.


```python
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```
```