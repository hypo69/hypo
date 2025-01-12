# Модуль: src.suppliers.aliexpress.api._examples.iop

## Обзор

Данный модуль содержит пример использования библиотеки `iop` для выполнения запросов к API. В частности, он демонстрирует, как создать и выполнить GET-запрос к API для получения информации о товаре.

## Содержание

- [Обзор](#обзор)
- [Импорт библиотек](#импорт-библиотек)
- [Настройка клиента IOP](#настройка-клиента-iop)
- [Создание и выполнение запроса](#создание-и-выполнение-запроса)
- [Обработка ответа](#обработка-ответа)

## Импорт библиотек

```python
import iop
import time
```
Модуль импортирует библиотеки `iop` для работы с API и `time` для получения текущего времени.

## Настройка клиента IOP

```python
client = iop.IopClient('https://api-pre.taobao.tw/rest', '100240', 'hLeciS15d7UsmXKoND76sBVPpkzepxex')
# client.log_level = iop.P_LOG_LEVEL_DEBUG
```

Создается экземпляр клиента `IopClient` с указанием URL-адреса шлюза, ключа приложения и секрета приложения. Закомментированная строка устанавливает уровень логирования в режим отладки.

## Создание и выполнение запроса

```python
request = iop.IopRequest('/product/item/get', 'GET')

request.add_api_param('itemId','157432005')
request.add_api_param('authDO', '{"sellerId":2000000016002}')

response = client.execute(request)
```
Здесь создается запрос `IopRequest` с указанием пути API-метода и HTTP-метода (GET). Затем добавляются параметры запроса `itemId` и `authDO`. Выполняется запрос с помощью метода `execute` клиента, результат сохраняется в переменную `response`.

## Обработка ответа

```python
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)

print(str(round(time.time())) + '000')
```

Код обрабатывает и выводит данные ответа:
- `response.type`: Тип ответа (nil, ISP, ISV, SYSTEM).
- `response.code`: Код ответа (0 означает отсутствие ошибок).
- `response.message`: Сообщение об ошибке (если есть).
- `response.request_id`: Уникальный идентификатор запроса.
- `response.body`: Полный текст ответа.
Также выводится текущее время в формате Unix timestamp с добавлением '000'.