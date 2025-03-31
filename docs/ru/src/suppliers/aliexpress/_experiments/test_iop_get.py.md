# Модуль для экспериментов с IOP и AliExpress API

## Обзор

Этот модуль предназначен для экспериментов с использованием IOP (IopClient) для взаимодействия с API AliExpress. Он содержит примеры запросов к API AliExpress, такие как генерация партнерских ссылок.

## Подробней

Модуль `test_iop_get.py` демонстрирует, как использовать библиотеку `iop` для выполнения запросов к API AliExpress. В коде создается экземпляр `IopClient` с учетными данными, необходимыми для аутентификации. Затем создается и выполняется запрос на генерацию партнерской ссылки. Результаты запроса, такие как тело ответа, тип, код, сообщение и идентификатор запроса, выводятся в консоль. Этот модуль полезен для тестирования и отладки взаимодействия с API AliExpress через `iop`.

## Функции

### `IopClient`

**Описание**: Класс для взаимодействия с API AliExpress через IOP.

**Как работает класс**:

1.  Создается экземпляр класса `IopClient` с URL шлюза, ключом приложения и секретным ключом приложения.

    ```python
    client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
    ```

2.  Устанавливается уровень логирования для клиента.

    ```python
    client.log_level = iop.P_LOG_LEVEL_DEBUG
    ```

### `IopRequest`

**Описание**: Класс для создания запросов к API AliExpress.

**Как работает класс**:

1.  Создается экземпляр класса `IopRequest` с указанием метода API (`aliexpress.affiliate.link.generate`).

    ```python
    request = iop.IopRequest('aliexpress.affiliate.link.generate')
    ```

2.  Добавляются параметры запроса, такие как тип партнерской ссылки, исходное значение (URL товара) и идентификатор отслеживания.

    ```python
    request.add_api_param('promotion_link_type', '0')
    request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
    request.add_api_param('tracking_id', 'default')
    ```

### `client.execute(request)`

**Описание**: Выполняет запрос к API AliExpress.

**Как работает функция**:

1.  Выполняется запрос с использованием метода `execute` клиента `IopClient`.

    ```python
    response = client.execute(request)
    ```

### `response`

**Описание**: Объект, содержащий ответ от API AliExpress.

**Как работает функция**:

1.  Выводятся различные атрибуты ответа, такие как тело ответа, тип, код, сообщение и идентификатор запроса.

    ```python
    print(response.body)
    print(response.type)
    print(response.code)
    print(response.message)
    print(response.request_id)
    print(response.body)
    ```

## Примеры

```python
import iop

# Создание клиента IOP
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
client.log_level = iop.P_LOG_LEVEL_DEBUG

# Создание запроса на генерацию партнерской ссылки
request = iop.IopRequest('aliexpress.affiliate.link.generate')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')

# Выполнение запроса
response = client.execute(request)

# Вывод результатов
print(response.body)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```