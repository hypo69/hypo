# Модуль test_upload

## Обзор

Этот модуль содержит пример использования API для загрузки файлов через IopClient. Он демонстрирует как создавать запрос, добавлять параметры, выполнять запрос и обрабатывать ответ.

## Функции

### `client.execute`

**Описание**: Выполняет запрос к API через IopClient.

**Параметры**:
- `request` (IopRequest): Объект запроса.
- `access_token` (Optional[str], optional): Токен доступа. По умолчанию None.


**Возвращает**:
- `IopResponse`: Объект ответа с результатами запроса.

**Вызывает исключения**:
- `Exception`: Возникает в случае ошибки при выполнении запроса.


### `IopClient`

**Описание**: Класс для взаимодействия с Iop API.

**Параметры**:
- `gateway_url` (str): URL шлюза API.
- `app_key` (str): Ключ приложения.
- `app_secret` (str): Секрет приложения.


**Методы**:
- `execute(request, access_token=None)`: Выполняет запрос к API.


### `IopRequest`

**Описание**: Класс для создания запросов к Iop API.

**Параметры**:
- `path` (str): Путь к ресурсу API.


**Методы**:
- `add_api_param(key, value)`: Добавляет параметр к запросу.
- `add_file_param(key, value)`: Добавляет параметр файла к запросу.  


## Пример использования

```python
import iop

# Замените на реальные значения
gateway_url = 'https://api.taobao.tw/rest'
app_key = '${appKey}'
app_secret = '${appSecret}'

client = iop.IopClient(gateway_url, app_key, app_secret)

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

**Примечания**:

- В примере предполагается, что файл `/Users/xt/Documents/work/tasp/tasp/pom.xml` существует.
-  Замените `'${appKey}'` и `'${appSecret}'` на ваши реальные значения.
- Обратите внимание на обработку ошибок (response.type, response.code, response.message). Необходимо добавить соответствующую обработку исключений в реальном коде.


```