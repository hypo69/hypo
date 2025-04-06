# Модуль `api_async`

## Обзор

Модуль `api_async` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop, используя JSON и XML форматы данных. Он обеспечивает выполнение операций CRUD, поиска и загрузки изображений. Класс также включает обработку ошибок и методы для управления данными API.

## Подробнее

Этот модуль предназначен для асинхронного взаимодействия с API PrestaShop. Он позволяет выполнять такие операции, как создание, чтение, обновление и удаление ресурсов, а также поиск и загрузку изображений. Модуль использует асинхронные запросы для повышения производительности и эффективности.

## Классы

### `Format`

**Описание**: Перечисление, определяющее форматы данных для взаимодействия с API (JSON, XML).

**Принцип работы**:
Определяет два возможных формата данных: JSON и XML. JSON предпочтительнее.

**Аттрибуты**:
- `JSON`: Строковое значение "JSON", представляющее формат JSON.
- `XML`: Строковое значение "XML", представляющее формат XML.

### `PrestaShopAsync`

**Описание**: Асинхронный класс для взаимодействия с API PrestaShop.

**Принцип работы**:
Класс инициализируется с параметрами подключения к API PrestaShop, такими как домен API и ключ API. Он предоставляет методы для выполнения различных операций с API, включая отправку запросов, обработку ответов и загрузку изображений.

**Аттрибуты**:
- `client` (ClientSession): Асинхронный HTTP клиент для выполнения запросов.
- `debug` (bool): Флаг для включения режима отладки.
- `lang_index` (Optional[int]): Индекс языка по умолчанию.
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML').
- `ps_version` (str): Версия PrestaShop.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса асинхронно.
- `_check_response`: Проверяет статус ответа и обрабатывает ошибки асинхронно.
- `_parse_response_error`: Разбирает ошибки в ответе от API PrestaShop асинхронно.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop асинхронно.
- `_parse`: Разбирает XML или JSON ответ от API асинхронно.
- `create`: Создает новый ресурс в API PrestaShop асинхронно.
- `read`: Читает ресурс из API PrestaShop асинхронно.
- `write`: Обновляет существующий ресурс в API PrestaShop асинхронно.
- `unlink`: Удаляет ресурс из API PrestaShop асинхронно.
- `search`: Выполняет поиск ресурсов в API PrestaShop асинхронно.
- `create_binary`: Загружает бинарный файл в ресурс API PrestaShop асинхронно.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из API PrestaShop и сохраняет их асинхронно.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API асинхронно.
- `get_languages_schema`: Получает схему для языков асинхронно.
- `upload_image_async`: Загружает изображение в API PrestaShop асинхронно.
- `upload_image`: Загружает изображение в API PrestaShop асинхронно.
- `get_product_images`: Получает изображения для продукта асинхронно.

## Функции

### `__init__`

```python
def __init__(self, api_domain: str, api_key: str, data_format: str = 'JSON', debug: bool = True) -> None
```

**Назначение**: Инициализирует класс `PrestaShopAsync`.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Флаг для включения режима отладки. По умолчанию `True`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверен или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Как работает функция**:

1.  Сохраняет переданные значения `api_domain`, `api_key`, `debug`, `data_format` в атрибуты экземпляра класса.
2.  Создает экземпляр `ClientSession` с использованием переданного API-ключа для аутентификации и устанавливает таймаут для запросов.

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
```

### `ping`

```python
async def ping(self) -> bool
```

**Назначение**: Проверяет работоспособность веб-сервиса асинхронно.

**Параметры**:
- `None`

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Как работает функция**:

1.  Выполняет HEAD-запрос к домену API.
2.  Проверяет статус ответа с помощью `_check_response`.
3.  Возвращает `True`, если статус код 200 или 201, иначе `False`.

**Примеры**:

```python
result = await api.ping()
print(result)
```

### `_check_response`

```python
def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                        headers: Optional[dict] = None, data: Optional[dict] = None) -> bool
```

**Назначение**: Проверяет статус ответа и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): HTTP статус код ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP ответа.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если статус код 200 или 201, иначе `False`.

**Как работает функция**:

1.  Проверяет, находится ли статус код в диапазоне 200-201.
2.  Если статус код не в диапазоне 200-201, вызывает `_parse_response_error` для обработки ошибки.
3.  Возвращает `True`, если статус код 200 или 201, иначе `False`.

**Примеры**:

```python
result = api._check_response(response.status, response)
print(result)
```

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None)
```

**Назначение**: Разбирает ошибки в ответе от API PrestaShop асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP ответа от сервера.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `response` (aiohttp.ClientResponse): Возвращает объект `response` если `self.data_format == 'JSON'`
- `code, message` (str, str): код и сообщение ошибки если `self.data_format == 'XML'`

**Как работает функция**:

1.  Проверяет формат данных (`self.data_format`).
2.  Если формат JSON, извлекает статус код и текст ответа, логирует их с использованием `logger.critical`.
3.  Если формат XML, разбирает XML ответ, извлекает код и сообщение об ошибке, логирует их с использованием `logger.error`.

**Примеры**:

```python
api._parse_response_error(response)
```

### `_prepare`

```python
def _prepare(self, url: str, params: dict) -> str
```

**Назначение**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Как работает функция**:

1.  Создает объект `PreparedRequest`.
2.  Подготавливает URL с использованием базового URL и параметров.
3.  Возвращает подготовленный URL.

**Примеры**:

```python
url = api._prepare('https://your-prestashop-domain.com/api/products', {'id': 1})
print(url)
```

### `_exec`

```python
async def _exec(self, resource: str, resource_id: Optional[Union[int, str]] = None, resource_ids: Optional[Union[int, Tuple[int]]] = None, method: str = 'GET', data: Optional[dict] = None, headers: Optional[dict] = None, search_filter: Optional[Union[str, dict]] = None, display: Optional[Union[str, list]] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, io_format: str = 'JSON') -> Optional[dict]
```

**Назначение**: Выполняет HTTP-запрос к API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products', 'categories').
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE).
- `data` (dict, optional): Данные для отправки с запросом.
- `headers` (dict, optional): Дополнительные заголовки для запроса.
- `search_filter` (str | dict, optional): Фильтр для запроса.
- `display` (str | list, optional): Поля для отображения в ответе.
- `schema` (str, optional): Схема данных.
- `sort` (str, optional): Параметр сортировки для запроса.
- `limit` (str, optional): Лимит результатов для запроса.
- `language` (int, optional): ID языка для запроса.
- `io_format` (str, optional): Формат данных ('JSON' или 'XML').

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1.  Подготавливает URL с использованием `_prepare`.
2.  Преобразует данные в XML, если `data` предоставлены и `io_format` равен 'XML'.
3.  Выполняет HTTP-запрос с использованием `aiohttp.ClientSession`.
4.  Проверяет статус ответа с помощью `_check_response`.
5.  Разбирает ответ в формате JSON или XML с использованием `_parse`.
6.  Возвращает разобранные данные или `False` в случае неудачи.

**Примеры**:

```python
data = await api._exec(resource='products', method='GET', limit='5')
print(data)
```

### `_parse`

```python
def _parse(self, text: str) -> dict | ElementTree.Element | bool
```

**Назначение**: Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае неудачи.

**Как работает функция**:

1.  Проверяет формат данных (`self.data_format`).
2.  Если формат JSON, разбирает текст с использованием `j_loads` и возвращает данные.
3.  Если формат XML, разбирает текст с использованием `ElementTree.fromstring` и возвращает дерево элементов.
4.  В случае ошибки разбора, логирует ошибку и возвращает `False`.

**Примеры**:

```python
data = api._parse(response.text)
print(data)
```

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]
```

**Назначение**: Создает новый ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1.  Вызывает `_exec` с методом 'POST' и переданными данными.
2.  Возвращает ответ от API.

**Примеры**:

```python
data = {'product': {'name': 'Test Product'}}
response = await api.create(resource='products', data=data)
print(response)
```

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]
```

**Назначение**: Читает ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1.  Вызывает `_exec` с методом 'GET' и переданными параметрами.
2.  Возвращает ответ от API.

**Примеры**:

```python
response = await api.read(resource='products', resource_id=1)
print(response)
```

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]
```

**Назначение**: Обновляет существующий ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1.  Извлекает ID ресурса из `data`.
2.  Вызывает `_exec` с методом 'PUT' и переданными данными.
3.  Возвращает ответ от API.

**Примеры**:

```python
data = {'product': {'id': 1, 'name': 'Updated Product'}}
response = await api.write(resource='products', data=data)
print(response)
```

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool
```

**Назначение**: Удаляет ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает `_exec` с методом 'DELETE' и переданными параметрами.
2.  Возвращает `True`, если успешно, иначе `False`.

**Примеры**:

```python
result = await api.unlink(resource='products', resource_id=1)
print(result)
```

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]
```

**Назначение**: Выполняет поиск ресурсов в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Как работает функция**:

1.  Вызывает `_exec` с методом 'GET' и переданными параметрами.
2.  Возвращает список ресурсов, соответствующих критериям поиска.

**Примеры**:

```python
results = await api.search(resource='products', filter='[name]=%Test%')
print(results)
```

### `create_binary`

```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict
```

**Назначение**: Загружает бинарный файл в ресурс API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1.  Открывает файл в бинарном режиме.
2.  Устанавливает заголовок 'Content-Type' в 'application/octet-stream'.
3.  Выполняет POST-запрос с файлом в теле запроса.
4.  Возвращает ответ от API.

**Примеры**:

```python
response = await api.create_binary(resource='images/products/22', file_path='img.jpg', file_name='img.jpg')
print(response)
```

### `_save`

```python
def _save(self, file_name: str, data: dict)
```

**Назначение**: Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

**Как работает функция**:

1.  Сохраняет данные в формате JSON в файл с использованием `save_text_file`.

**Примеры**:

```python
api._save(file_name='products.json', data={'products': []})
```

### `get_data`

```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]
```

**Назначение**: Получает данные из API PrestaShop и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для запроса API.

**Возвращает**:
- `dict | None`: Данные от API или `False` в случае неудачи.

**Как работает функция**:

1.  Вызывает `_exec` для получения данных из API.
2.  Сохраняет данные в файл с использованием `_save`.
3.  Возвращает данные или `False` в случае неудачи.

**Примеры**:

```python
data = await api.get_data(resource='products', limit='5')
print(data)
```

### `remove_file`

```python
def remove_file(self, file_path: str)
```

**Назначение**: Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Как работает функция**:

1.  Удаляет файл с использованием `os.remove`.
2.  Логирует ошибку, если файл не удалось удалить.

**Примеры**:

```python
api.remove_file(file_path='products.json')
```

### `get_apis`

```python
async def get_apis(self) -> Optional[dict]
```

**Назначение**: Получает список всех доступных API асинхронно.

**Параметры**:
- `None`

**Возвращает**:
- `dict`: Список доступных API.

**Как работает функция**:

1.  Вызывает `_exec` для получения списка API.
2.  Возвращает список API.

**Примеры**:

```python
apis = await api.get_apis()
print(apis)
```

### `get_languages_schema`

```python
async def get_languages_schema(self) -> Optional[dict]
```

**Назначение**: Получает схему для языков асинхронно.

**Параметры**:
- `None`

**Возвращает**:
- `dict`: Схема языков или `None` в случае неудачи.

**Как работает функция**:

1.  Вызывает `_exec` для получения схемы языков.
2.  Возвращает схему языков или `None` в случае ошибки.

**Примеры**:

```python
schema = await api.get_languages_schema()
print(schema)
```

### `upload_image_async`

```python
async def upload_image_async(self, resource: str, resource_id: int, img_url: str,
                           img_name: Optional[str] = None) -> Optional[dict]
```

**Назначение**: Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1.  Разделяет URL изображения на имя файла и расширение.
2.  Создает имя файла с использованием ID ресурса и имени изображения.
3.  Сохраняет изображение с использованием `save_image_from_url`.
4.  Загружает изображение в API с использованием `create_binary`.
5.  Удаляет временный файл изображения.
6.  Возвращает ответ от API.

**Примеры**:

```python
response = await api.upload_image_async(resource='images/products/22', resource_id=22, img_url='https://example.com/img.jpg', img_name='img')
print(response)
```

### `upload_image`

```python
async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]
```

**Назначение**: Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1.  Разделяет URL изображения на имя файла и расширение.
2.  Создает имя файла с использованием ID ресурса и имени изображения.
3.  Сохраняет изображение с использованием `save_image_from_url`.
4.  Загружает изображение в API с использованием `create_binary`.
5.  Удаляет временный файл изображения.
6.  Возвращает ответ от API.

**Примеры**:

```python
response = await api.upload_image(resource='images/products/22', resource_id=22, img_url='https://example.com/img.jpg', img_name='img')
print(response)
```

### `get_product_images`

```python
async def get_product_images(self, product_id: int) -> Optional[dict]
```

**Назначение**: Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае неудачи.

**Как работает функция**:

1.  Вызывает `_exec` для получения списка изображений продукта.
2.  Возвращает список изображений продукта или `False` в случае неудачи.

**Примеры**:

```python
images = await api.get_product_images(product_id=22)
print(images)