# Модуль `src.suppliers.aliexpress.api._examples.iop.test_get.py`

## Обзор

Модуль представляет собой пример использования API AliExpress для получения адресов продавца с помощью IopClient. Он демонстрирует создание запроса с методом GET, установку параметров и обработку ответа.

## Оглавление

- [Обзор](#обзор)
- [Импорт](#импорт)
- [Настройка клиента](#настройка-клиента)
- [Создание и выполнение запроса](#создание-и-выполнение-запроса)
- [Обработка ответа](#обработка-ответа)

## Импорт

```python
import iop
```
Импортируется модуль `iop`, который используется для взаимодействия с API AliExpress.

## Настройка клиента

```python
client = iop.IopClient('https://api-pre.aliexpress.com/sync', '33505222', 'e1fed6b34feb26aabc391d187732af93')
```
Создается экземпляр класса `IopClient` для взаимодействия с API AliExpress.
- Параметр 1: URL шлюза API.
- Параметр 2: Appkey.
- Параметр 3: AppSecret.

## Создание и выполнение запроса

```python
request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST')
request.set_simplify()
request.add_api_param('seller_address_query','pickup')
response = client.execute(request,"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL")
```

Здесь происходит создание запроса `IopRequest` и его выполнение:
   - Создается запрос с указанием метода POST и названия API.
   - Устанавливается упрощенный формат ответа.
   - Добавляется параметр `seller_address_query` со значением `pickup`.
   - Запрос выполняется с помощью метода `execute` клиента, передавая токен.

## Обработка ответа

```python
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```
Обработка ответа API:
- `response.type`: Тип ответа (`nil`, `ISP`, `ISV`, `SYSTEM`).
- `response.code`: Код ответа (0 - нет ошибок).
- `response.message`: Сообщение об ошибке (если есть).
- `response.request_id`: Уникальный идентификатор запроса.
- `response.body`: Полное тело ответа в формате JSON.