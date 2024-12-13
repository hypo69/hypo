# Документация модуля `test_get.py`

## Обзор

Данный модуль демонстрирует пример использования `IopClient` и `IopRequest` для отправки запроса к API AliExpress с методом GET и получения ответа.

## Оглавление

- [Обзор](#обзор)
- [Импорт](#импорт)
- [Пример использования](#пример-использования)
- [Описание переменных и объектов](#описание-переменных-и-объектов)

## Импорт

```python
import iop
```

## Пример использования

```python
client = iop.IopClient('https://api-pre.aliexpress.com/sync', '33505222', 'e1fed6b34feb26aabc391d187732af93')

request = iop.IopRequest('aliexpress.logistics.redefining.getlogisticsselleraddresses', 'POST')
request.set_simplify()
request.add_api_param('seller_address_query','pickup')

response = client.execute(request,"50000001a27l15rndYBjw6PrtFFHPGZfy09k1Cp1bd8597fsduP0RStringNormalizery0jhF6FL")

print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

## Описание переменных и объектов

### `client`

**Описание**: Экземпляр класса `IopClient` для взаимодействия с API AliExpress.

**Параметры**:

- `gateway url` (str): URL шлюза API.
- `appkey` (str): Ключ приложения.
- `appSecret` (str): Секретный ключ приложения.

### `request`

**Описание**: Экземпляр класса `IopRequest` для формирования запроса к API.

**Методы**:

- `set_simplify()`: Устанавливает упрощенный тип запроса.
- `add_api_param(param_name: str, param_value: str)`: Добавляет параметр запроса.
  - `param_name` (str): Имя параметра.
  - `param_value` (str): Значение параметра.

### `response`

**Описание**: Экземпляр класса `IopResponse`, содержащий ответ от API.

**Атрибуты**:

- `type` (str): Тип ответа (nil, ISP, ISV, SYSTEM).
- `code` (int): Код ответа (0 - нет ошибки).
- `message` (str): Сообщение об ошибке (если есть).
- `request_id` (str): Уникальный ID запроса.
- `body` (dict): Тело ответа.

**Значения атрибута `type`**:

- `nil`: Нет ошибки.
- `ISP`: Ошибка провайдера API.
- `ISV`: Ошибка запроса клиента API.
- `SYSTEM`: Ошибка платформы Iop.