# Модуль test_upload.py

## Обзор

Модуль `test_upload.py` содержит пример использования API для загрузки файлов через `iop` библиотеку.  Он демонстрирует создание запроса, добавление параметров и выполнение запроса к API, а также обработку ответа.

## Оглавление

* [Модуль test_upload.py](#модуль-test_uploadpy)
* [Обзор](#обзор)
* [Функции](#функции)
    * [`IopClient`](#iopclient)
    * [`IopRequest`](#ioprequest)
    * [`execute`](#execute)


## Функции

### `IopClient`

**Описание**:  Создает экземпляр клиента для взаимодействия с API.

**Параметры**:
- `gateway_url` (str): URL шлюза API.
- `app_key` (str): Ключ приложения.
- `app_secret` (str): Секрет приложения.

**Возвращает**:
- `IopClient`: Экземпляр клиента `IopClient`.


### `IopRequest`

**Описание**: Создает запрос к API.

**Параметры**:
- `path` (str): Путь к API-методу.

**Возвращает**:
- `IopRequest`: Экземпляр запроса `IopRequest`.


### `add_api_param`

**Описание**: Добавляет параметр к запросу.

**Параметры**:
- `name` (str): Имя параметра.
- `value` (str | int | ...): Значение параметра.

**Возвращает**:
- `None`.


### `add_file_param`

**Описание**: Добавляет параметр файла к запросу.

**Параметры**:
- `name` (str): Имя параметра.
- `value` (bytes): Содержимое файла.

**Возвращает**:
- `None`.


### `execute`

**Описание**: Выполняет запрос к API.

**Параметры**:
- `request` (IopRequest): Экземпляр запроса.
- `access_token` (str, optional): Токен доступа. По умолчанию, `None`.


**Возвращает**:
- `IopResponse`: Объект с результатом выполнения запроса. Возвращает `IopResponse` объект, содержащий данные о результате запроса, включая код ошибки, сообщение об ошибке, уникальный идентификатор запроса и тело ответа. Возможные типы ответа `nil`, `ISP`, `ISV`, `SYSTEM`.


**Возможные исключения**:
- `Exception`: Возможные исключения при выполнении запроса.


## Пример использования

```python
client = iop.IopClient('https://api.taobao.tw/rest', '${appKey}', '${appSecret}')
request = iop.IopRequest('/xiaoxuan/mockfileupload')
request.add_api_param('file_name', 'pom.xml')
request.add_file_param('file_bytes', open('/Users/xt/Documents/work/tasp/tasp/pom.xml').read())
response = client.execute(request)
print(response.type)
print(response.code)
print(response.message)
print(response.request_id)
print(response.body)
```

**Примечание**:  Этот код требует наличия модуля `iop`.  Значения `'${appKey}'` и `'${appSecret}'` должны быть заменены на фактические значения ключа и секрета приложения. Путь к файлу `/Users/xt/Documents/work/tasp/tasp/pom.xml` также должен быть изменен на корректный путь.


```