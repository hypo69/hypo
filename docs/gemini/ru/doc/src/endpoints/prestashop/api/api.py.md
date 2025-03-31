# Модуль для взаимодействия с PrestaShop API

## Обзор

Модуль предоставляет класс `PrestaShop` для взаимодействия с веб-сервисом PrestaShop API, используя JSON и XML для форматирования сообщений. Он поддерживает операции CRUD, поиск и загрузку изображений, с обработкой ошибок для ответов.

## Подробней

Этот модуль предназначен для упрощения взаимодействия с API PrestaShop, предоставляя удобный интерфейс для выполнения различных операций, таких как создание, чтение, обновление и удаление ресурсов, а также для поиска и загрузки изображений. Он использует библиотеки `requests` и `xml.etree.ElementTree` для отправки HTTP-запросов и обработки ответов в форматах JSON и XML. Модуль также включает обработку ошибок и ведение журнала для облегчения отладки и мониторинга.

## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop API.

**Как работает класс**:
Класс `PrestaShop` предоставляет интерфейс для взаимодействия с PrestaShop API. При инициализации класса устанавливается соединение с API, проверяется его работоспособность и определяется версия PrestaShop. Класс предоставляет методы для выполнения CRUD-операций, поиска ресурсов, загрузки изображений и получения схем ресурсов.

- Инициализация класса: при создании экземпляра класса `PrestaShop` происходит установка соединения с API, проверка его работоспособности и определение версии PrestaShop.
- Выполнение запросов: методы `create`, `read`, `write`, `unlink`, `search` и `create_binary` используют метод `_exec` для выполнения HTTP-запросов к API PrestaShop.
- Обработка ответов: методы `_check_response` и `_parse_response` используются для проверки статуса ответа и разбора данных, возвращаемых API.
- Загрузка изображений: методы `upload_image_async` и `upload_image_from_url` используются для загрузки изображений в PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс PrestaShop.
- `ping`: Проверяет, работает ли веб-сервис.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает сообщение об ошибке от PrestaShop API.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse_response`: Разбирает XML или JSON ответ от API в структуру dict.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Выполняет поиск ресурсов в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `get_schema`: Получает схему данного ресурса из PrestaShop API.
- `get_data`: Извлекает данные из ресурса PrestaShop API и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в PrestaShop API.
- `upload_image_from_url`: Загружает изображение в PrestaShop API.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `api_key` (str): API ключ, сгенерированный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию True.

## Функции

### `__init__`

```python
def __init__(api_key: str, api_domain: str, data_format: str = 'JSON', default_lang: int = 1, debug: bool = False) -> None
```

**Назначение**: Инициализирует класс PrestaShop.

**Как работает функция**:
Функция инициализирует экземпляр класса `PrestaShop`, устанавливая значения атрибутов, такие как `api_domain`, `api_key`, `debug`, `language` и `data_format`. Она также устанавливает аутентификацию для HTTP-клиента и проверяет соединение с API PrestaShop, определяя версию PrestaShop.

Внутри функции происходят следующие действия и преобразования:
A. Присваивание значений атрибутам экземпляра класса.
|
B. Установка аутентификации для HTTP-клиента.
|
C. Проверка соединения с API PrestaShop и определение версии PrestaShop.

**Параметры**:
- `api_key` (str): API ключ, сгенерированный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию True.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если API ключ неверен или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Примеры**:
```python
api = PrestaShop(
    api_key='your_api_key',
    api_domain='https://your-prestashop-domain.com',
    data_format='JSON',
    default_lang=1,
    debug=True
)
```

### `ping`

```python
def ping() -> bool
```

**Назначение**: Проверяет, работает ли веб-сервис.

**Как работает функция**:
Функция отправляет HEAD-запрос к API PrestaShop и проверяет статус ответа. Возвращает `True`, если веб-сервис работает, и `False` в противном случае.

Внутри функции происходят следующие действия и преобразования:
A. Отправка HEAD-запроса к API PrestaShop.
|
B. Проверка статуса ответа с помощью метода `_check_response`.
|
C. Возврат `True`, если веб-сервис работает, и `False` в противном случае.

**Возвращает**:
- `bool`: Результат проверки связи. Возвращает `True`, если веб-сервис работает, иначе `False`.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
if api.ping():
    print('Webservice is working.')
else:
    print('Webservice is not working.')
```

### `_check_response`

```python
def _check_response(status_code: int, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> bool
```

**Назначение**: Проверяет код состояния ответа и обрабатывает ошибки.

**Как работает функция**:
Функция проверяет код состояния HTTP-ответа. Если код состояния находится в диапазоне 200-201, функция возвращает `True`. В противном случае функция вызывает метод `_parse_response_error` для обработки ошибки и возвращает `False`.

Внутри функции происходят следующие действия и преобразования:
A. Проверка кода состояния HTTP-ответа.
|
B. Если код состояния находится в диапазоне 200-201, функция возвращает `True`.
|
C. В противном случае функция вызывает метод `_parse_response_error` для обработки ошибки и возвращает `False`.

**Параметры**:
- `status_code` (int): Код состояния HTTP-ответа.
- `response`: Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.client.get('https://your-prestashop-domain.com/api/products')
if api._check_response(response.status_code, response):
    print('Request was successful.')
else:
    print('Request failed.')
```

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None)
```

**Назначение**: Разбирает сообщение об ошибке от PrestaShop API.

**Как работает функция**:
Функция разбирает ответ об ошибке от API PrestaShop. Если формат данных JSON, она извлекает код состояния и содержимое ответа, а затем регистрирует ошибку с помощью `logger.error`. Если формат данных XML, она использует `_parse_response` для преобразования XML в словарь, а затем извлекает код и сообщение об ошибке из структуры XML.

Внутри функции происходят следующие действия и преобразования:
A. Проверка формата данных (`self.data_format`).
|
B. Если формат данных JSON:
   - Извлекается код состояния (`response.status_code`).
   - Если код состояния не 200 или 201:
     - Вызывается `j_dumps` для форматирования JSON-ответа.
     - Регистрируется ошибка с использованием `logger.error`, включающая код состояния, URL запроса, заголовки и текст ответа.
|
C. Если формат данных XML:
   - Вызывается `self._parse_response(response)` для преобразования XML в словарь.
   - Извлекается код и сообщение об ошибке из структуры XML.
   - Регистрируется ошибка с использованием `logger.error`, включающая сообщение и код ошибки.

**Параметры**:
- `response`: Объект HTTP-ответа от сервера.
- `method` (Optional[str], optional): HTTP-метод, использованный для запроса. По умолчанию `None`.
- `url` (Optional[str], optional): URL запроса. По умолчанию `None`.
- `headers` (Optional[dict], optional): Заголовки запроса. По умолчанию `None`.
- `data` (Optional[dict], optional): Данные запроса. По умолчанию `None`.

**Возвращает**:
- `response` (requests.Response) в случае формата JSON.
- `Tuple[code, message]` в случае формата XML.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.client.get('https://your-prestashop-domain.com/api/products')
if not api._check_response(response.status_code, response):
    api._parse_response_error(response)
```

### `_prepare_url`

```python
def _prepare_url(url: str, params: dict) -> str
```

**Назначение**: Подготавливает URL для запроса.

**Как работает функция**:
Функция подготавливает URL для запроса, добавляя параметры к базовому URL. Она использует класс `PreparedRequest` из библиотеки `requests` для добавления параметров к URL.

Внутри функции происходят следующие действия и преобразования:
A. Создание экземпляра класса `PreparedRequest`.
|
B. Подготовка URL с параметрами с помощью метода `req.prepare_url(url, params)`.
|
C. Возврат подготовленного URL.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '10'}
prepared_url = api._prepare_url(url, params)
print(prepared_url)
```

### `_exec`

```python
def _exec(resource: str, resource_id: Optional[int | str] = None, resource_ids: Optional[int | Tuple[int]] = None, method: str = 'GET', data: Optional[dict | str] = None, headers: Optional[dict] = None, search_filter: Optional[str | dict] = None, display: Optional[str | list] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, data_format: str = 'JSON') -> Optional[dict]
```

**Назначение**: Выполняет HTTP-запрос к PrestaShop API.

**Как работает функция**:
Функция выполняет HTTP-запрос к API PrestaShop с указанными параметрами. Она формирует URL, устанавливает заголовки запроса, отправляет запрос и обрабатывает ответ.

Внутри функции происходят следующие действия и преобразования:
A. Установка уровня отладки HTTP-соединения.
|
B. Формирование URL запроса на основе переданных параметров.
|
C. Установка заголовков запроса в зависимости от формата данных (JSON или XML).
|
D. Отправка HTTP-запроса с использованием библиотеки `requests`.
|
E. Проверка ответа с использованием метода `_check_response`.
|
F. Разбор ответа с использованием метода `_parse_response`.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (Optional[int | str], optional): ID ресурса.
- `resource_ids` (Optional[int | Tuple[int]], optional): ID ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE). По умолчанию 'GET'.
- `data` (Optional[dict | str], optional): Данные для отправки в запросе.
- `headers` (Optional[dict], optional): Дополнительные заголовки для запроса.
- `search_filter` (Optional[str | dict], optional): Фильтр для поиска ресурсов.
- `display` (Optional[str | list], optional): Параметр отображения ресурсов. По умолчанию 'full'.
- `schema` (Optional[str], optional): Схема ресурса.
- `sort` (Optional[str], optional): Параметр сортировки ресурсов.
- `limit` (Optional[str], optional): Лимит количества возвращаемых ресурсов.
- `language` (Optional[int], optional): ID языка.
- `data_format` (str, optional): Формат данных (JSON или XML). По умолчанию 'JSON'.

**Возвращает**:
- `Optional[dict]`: Ответ от API в виде словаря или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
products = api._exec(resource='products', method='GET', limit='5')
print(products)
```

### `_parse_response`

```python
def _parse_response(response: Response, data_format: Optional[str] = 'JSON') -> dict | None
```

**Назначение**: Разбирает XML или JSON ответ от API в структуру dict.

**Как работает функция**:
Функция разбирает ответ от API PrestaShop в формате JSON или XML и преобразует его в структуру dict. Она использует методы `response.json()` для разбора JSON и `xml2dict()` для разбора XML.

Внутри функции происходят следующие действия и преобразования:
A. Определение формата данных ответа (`self.data_format`).
|
B. Если формат данных JSON:
   - Вызывается `response.json()` для разбора JSON-ответа и преобразования его в словарь.
|
C. Если формат данных XML:
   - Вызывается `xml2dict(response.text)` для разбора XML-ответа и преобразования его в словарь.
|
D. Извлечение данных из структуры ответа. Если в данных присутствует ключ 'prestashop', возвращается значение этого ключа. В противном случае возвращаются все данные.

**Параметры**:
- `response` (Response): Объект HTTP-ответа от сервера.
- `data_format` (Optional[str], optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `dict | None`: Разобранные данные в виде словаря или `None` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.client.get('https://your-prestashop-domain.com/api/products')
data = api._parse_response(response)
print(data)
```

### `create`

```python
def create(self, resource: str, data: dict, *args, **kwards) -> Optional[dict]
```

**Назначение**: Создает новый ресурс в PrestaShop API.

**Как работает функция**:
Функция создает новый ресурс в API PrestaShop, отправляя POST-запрос к указанному ресурсу с переданными данными. Она использует метод `_exec` для выполнения запроса.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `method`: 'POST' (указывает на создание нового ресурса).
   - `data`: Данные для создания ресурса.
   - `*args`: Дополнительные позиционные аргументы, переданные в функцию.
   - `**kwards`: Дополнительные именованные аргументы, переданные в функцию.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.
- `*args`: Дополнительные позиционные аргументы.
- `**kwards`: Дополнительные именованные аргументы.

**Возвращает**:
- `Optional[dict]`: Ответ от API в виде словаря.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
data = {'product': {'name': 'Test Product', 'price': 10.0}}
response = api.create(resource='products', data=data)
print(response)
```

### `read`

```python
def read(self, resource: str, resource_id: int | str, **kwargs) -> Optional[dict]
```

**Назначение**: Читает ресурс из PrestaShop API.

**Как работает функция**:
Функция читает ресурс из API PrestaShop, отправляя GET-запрос к указанному ресурсу с указанным ID. Она использует метод `_exec` для выполнения запроса.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `resource_id`: ID ресурса.
   - `method`: 'GET' (указывает на чтение ресурса).
   - `**kwargs`: Дополнительные именованные аргументы, переданные в функцию.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `Optional[dict]`: Ответ от API в виде словаря.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.read(resource='products', resource_id=1)
print(response)
```

### `write`

```python
def write(self, resource: str, data: dict) -> Optional[dict]
```

**Назначение**: Обновляет существующий ресурс в PrestaShop API.

**Как работает функция**:
Функция обновляет существующий ресурс в API PrestaShop, отправляя PUT-запрос к указанному ресурсу с переданными данными. Она использует метод `_exec` для выполнения запроса.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `resource_id`: ID ресурса, извлеченный из данных (`data.get('id')`).
   - `method`: 'PUT' (указывает на обновление ресурса).
   - `data`: Данные для обновления ресурса.
   - `data_format`: Формат данных (`self.data_format`).

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API в виде словаря.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
data = {'id': 1, 'product': {'name': 'Updated Product', 'price': 12.0}}
response = api.write(resource='products', data=data)
print(response)
```

### `unlink`

```python
def unlink(self, resource: str, resource_id: int | str) -> bool
```

**Назначение**: Удаляет ресурс из PrestaShop API.

**Как работает функция**:
Функция удаляет ресурс из API PrestaShop, отправляя DELETE-запрос к указанному ресурсу с указанным ID. Она использует метод `_exec` для выполнения запроса.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `resource_id`: ID ресурса.
   - `method`: 'DELETE' (указывает на удаление ресурса).
   - `data_format`: Формат данных (`self.data_format`).

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если удаление прошло успешно, `False` в противном случае.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.unlink(resource='products', resource_id=1)
print(response)
```

### `search`

```python
def search(self, resource: str, filter: Optional[str | dict] = None, **kwargs) -> List[dict]
```

**Назначение**: Выполняет поиск ресурсов в PrestaShop API.

**Как работает функция**:
Функция выполняет поиск ресурсов в API PrestaShop, отправляя GET-запрос к указанному ресурсу с указанным фильтром. Она использует метод `_exec` для выполнения запроса.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `search_filter`: Фильтр для поиска ресурсов.
   - `method`: 'GET' (указывает на поиск ресурсов).
   - `**kwargs`: Дополнительные именованные аргументы, переданные в функцию.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (Optional[str | dict], optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.search(resource='products', filter='[name]=%Test%')
print(response)
```

### `create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict
```

**Назначение**: Загружает бинарный файл в ресурс PrestaShop API.

**Как работает функция**:
Функция загружает бинарный файл (например, изображение) в указанный ресурс API PrestaShop. Она открывает файл в бинарном режиме, формирует словарь `files` для передачи файла в запросе, отправляет POST-запрос к API и обрабатывает ответ.

Внутри функции происходят следующие действия и преобразования:
A. Открытие файла по указанному пути в бинарном режиме (`with open(file_path, 'rb') as file:`).
|
B. Формирование словаря `files` для передачи файла в запросе.
|
C. Отправка POST-запроса к API с использованием библиотеки `requests`.
   - URL запроса формируется как `f'{self.api_domain}/images/{resource}'`.
   - Файл передается в параметре `files`.
   - Аутентификация передается в параметре `auth`.
|
D. Проверка на HTTP-ошибки с помощью `response.raise_for_status()`.
|
E. Разбор ответа с использованием метода `_parse_response`.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.create_binary(resource='images/products/22', file_path='img.jpg', file_name='image')
print(response)
```

### `get_schema`

```python
def get_schema(self, resource: Optional[str] = None, resource_id: Optional[int] = None, schema: Optional[str] = 'blank', **kwards) -> dict | None
```

**Назначение**: Получает схему данного ресурса из PrestaShop API.

**Как работает функция**:
Функция получает схему указанного ресурса из API PrestaShop. Схема определяет структуру данных, которые можно получить или отправить для данного ресурса. Она использует метод `_exec` для выполнения GET-запроса к API с параметром `schema`.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: Имя ресурса (например, 'products', 'customers').
   - `resource_id`: ID ресурса.
   - `schema`: Тип схемы ('blank', 'synopsis', 'full', 'form'). По умолчанию 'blank'.
   - `method`: 'GET' (указывает на получение данных).
   - `**kwards`: Дополнительные именованные аргументы, переданные в функцию.

**Параметры**:
- `resource` (str, optional): Имя ресурса (например, 'products', 'customers'). Если не указано, возвращается список всех схем сущностей, доступных для API ключа.
- `resource_id` (Optional[str], optional): ID ресурса.
- `schema` (Optional[str], optional): Тип схемы ('blank', 'synopsis', 'full', 'form'). По умолчанию 'blank'.

**Возвращает**:
- `dict | None`: Схема запрошенного ресурса или `None` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
schema = api.get_schema(resource='products', schema='blank')
print(schema)
```

### `get_data`

```python
def get_data(self, resource: str, **kwargs) -> Optional[dict]
```

**Назначение**: Извлекает данные из ресурса PrestaShop API и сохраняет их.

**Как работает функция**:
Функция извлекает данные из указанного ресурса API PrestaShop. Она использует метод `_exec` для выполнения GET-запроса к API.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: API ресурс (например, 'products').
   - `method`: 'GET' (указывает на получение данных).
   - `**kwargs`: Дополнительные именованные аргументы, переданные в функцию.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API-запроса.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
data = api.get_data(resource='products', display='full', limit='1')
print(data)
```

### `get_apis`

```python
def get_apis() -> Optional[dict]
```

**Назначение**: Получает список всех доступных API.

**Как работает функция**:
Функция получает список всех доступных API из PrestaShop. Она использует метод `_exec` для выполнения GET-запроса к ресурсу 'apis'.

Внутри функции происходят следующие действия и преобразования:
A. Вызов метода `_exec` с параметрами:
   - `resource`: 'apis' (указывает на получение списка доступных API).
   - `method`: 'GET' (указывает на получение данных).
   - `data_format`: Формат данных (`self.data_format`).

**Возвращает**:
- `dict`: Список доступных API.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
apis = api.get_apis()
print(apis)
```

### `upload_image_async`

```python
def upload_image_async(self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]
```

**Назначение**: Асинхронно загружает изображение в PrestaShop API.

**Как работает функция**:
Функция асинхронно загружает изображение в PrestaShop API. Она разбивает URL изображения на части, формирует имя файла, сохраняет изображение с URL, загружает изображение в API и удаляет временный файл.

Внутри функции происходят следующие действия и преобразования:
A. Разбиение URL изображения на части для получения расширения файла.
|
B. Формирование имени файла на основе ID ресурса и имени изображения.
|
C. Сохранение изображения с URL с использованием функции `save_image_from_url`.
|
D. Загрузка изображения в API с использованием функции `create_binary`.
|
E. Удаление временного файла с изображением с использованием функции `self.remove_file`.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.upload_image_async(resource='images/products/22', resource_id=22, img_url='https://example.com/image.jpg', img_name='product_image')
print(response)
```

### `upload_image_from_url`

```python
def upload_image_from_url(self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]
```

**Назначение**: Загружает изображение в PrestaShop API.

**Как работает функция**:
Функция загружает изображение в PrestaShop API. Она разбивает URL изображения на части, формирует имя файла, сохраняет изображение с URL, загружает изображение в API и удаляет временный файл.

Внутри функции происходят следующие действия и преобразования:
A. Разбиение URL изображения на части для получения расширения файла.
|
B. Формирование имени файла на основе ID ресурса и имени изображения.
|
C. Сохранение изображения с URL с использованием функции `save_image_from_url`.
|
D. Загрузка изображения в API с использованием функции `create_binary`.
|
E. Удаление временного файла с изображением с использованием функции `self.remove_file`.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

**Примеры**:
```python
api = PrestaShop(api_key='your_api_key', api_domain='https://your-prestashop-domain.com')
response = api.upload_image_from_url(resource='images/products/2