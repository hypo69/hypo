# Модуль для асинхронного взаимодействия с PrestaShop API

## Обзор

Модуль предоставляет класс `PrestaShopAsync` для асинхронного взаимодействия с PrestaShop API. Он поддерживает операции CRUD, поиск и загрузку изображений. Модуль также включает обработку ошибок и методы для управления данными API.

## Подробнее

Этот модуль предназначен для упрощения взаимодействия с PrestaShop API в асинхронном режиме. Он позволяет выполнять различные операции, такие как создание, чтение, обновление и удаление ресурсов, а также поиск и загрузку изображений.

## Классы

### `Format`

**Описание**:
Перечисление, определяющее формат данных (JSON или XML).

**Принцип работы**:
Используется для указания формата данных при взаимодействии с API. Предпочтительным форматом является JSON.

### `PrestaShopAsync`

**Описание**:
Асинхронный класс для взаимодействия с PrestaShop API.

**Принцип работы**:
Этот класс предоставляет асинхронные методы для взаимодействия с PrestaShop API, позволяя выполнять операции CRUD, поиск и загрузку изображений. Он также обеспечивает обработку ошибок для ответов и методы для обработки данных API.

**Атрибуты**:

- `client` (ClientSession): Асинхронный HTTP-клиент для выполнения запросов.
- `debug` (bool): Флаг для включения режима отладки.
- `lang_index` (Optional[int]): Индекс языка по умолчанию.
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML').
- `ps_version` (str): Версия PrestaShop.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Методы**:

- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse`: Разбирает XML или JSON ответ от API.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Выполняет поиск ресурсов в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API.
- `get_languages_schema`: Получает схему для языков.
- `upload_image_async`: Загружает изображение в PrestaShop API асинхронно.
- `upload_image`: Загружает изображение в PrestaShop API асинхронно.
- `get_product_images`: Получает изображения для продукта.

## Функции

### `__init__`

```python
def __init__(self, api_domain: str, api_key: str, data_format: str = 'JSON', debug: bool = True) -> None
```

**Назначение**:
Инициализирует класс `PrestaShopAsync` с параметрами подключения к API.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Флаг для включения режима отладки. По умолчанию `True`.

**Возвращает**:
`None`

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверен или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Как работает функция**:

1. Сохраняет параметры `api_domain`, `api_key`, `debug` и `data_format` в атрибуты экземпляра класса.
2. Создает асинхронный HTTP-клиент `ClientSession` с использованием ключа API для аутентификации и устанавливает таймаут для запросов.

```
Инициализация параметров -> Создание ClientSession
```

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key', data_format='JSON', debug=True)
```

### `ping`

```python
async def ping(self) -> bool
```

**Назначение**:
Проверяет, работает ли веб-сервис асинхронно.

**Параметры**:
Нет

**Возвращает**:
`bool`: `True`, если веб-сервис работает, иначе `False`.

**Как работает функция**:

1. Отправляет HEAD-запрос к домену API.
2. Проверяет код ответа с помощью `_check_response`.

```
Отправка HEAD-запроса -> Проверка ответа
```

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

**Назначение**:
Проверяет код состояния ответа и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): HTTP-код состояния ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
`bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Как работает функция**:

1. Проверяет, находится ли код состояния в диапазоне (200, 201).
2. Если код состояния не входит в этот диапазон, вызывает `_parse_response_error` для обработки ошибки и возвращает `False`.

```
Проверка status_code -> Обработка ошибки (если необходимо)
```

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

**Назначение**:
Разбирает ответ об ошибке от PrestaShop API асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа от сервера.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
`None`

**Как работает функция**:

1. Проверяет формат данных (`self.data_format`).
2. Если формат JSON:
   - Получает код состояния ответа.
   - Если код состояния не 200 или 201, логирует критическую ошибку с информацией о запросе и ответе.
3. Если формат XML:
   - Вызывает `_parse` для разбора XML-ответа.
   - Извлекает код и сообщение об ошибке из XML-ответа.
   - Логирует ошибку с кодом и сообщением.

```
Проверка data_format -> Разбор JSON/XML -> Логирование ошибки
```

**Примеры**:

```python
api._parse_response_error(response)
```

### `_prepare`

```python
def _prepare(self, url: str, params: dict) -> str
```

**Назначение**:
Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
`str`: Подготовленный URL с параметрами.

**Как работает функция**:

1. Создает объект `PreparedRequest`.
2. Подготавливает URL с параметрами с помощью `req.prepare_url`.
3. Возвращает подготовленный URL.

```
Создание PreparedRequest -> Подготовка URL -> Возврат URL
```

**Примеры**:

```python
url = api._prepare('https://your-prestashop-domain.com/api/products', {'display': 'full'})
print(url)
```

### `_exec`

```python
async def _exec(self, resource: str, resource_id: Optional[Union[int, str]] = None, resource_ids: Optional[Union[int, Tuple[int]]] = None, method: str = 'GET', data: Optional[dict] = None, headers: Optional[dict] = None, search_filter: Optional[Union[str, dict]] = None, display: Optional[Union[str, list]] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, io_format: str = 'JSON') -> Optional[dict]
```

**Назначение**:
Выполняет HTTP-запрос к PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products', 'categories').
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP-метод (GET, POST, PUT, DELETE).
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
`dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1. Формирует URL на основе переданных параметров.
2. Преобразует данные в XML, если `io_format` равен 'XML'.
3. Выполняет HTTP-запрос с использованием `aiohttp.ClientSession`.
4. Проверяет ответ с помощью `_check_response`.
5. Разбирает ответ (JSON или XML) и возвращает результат.

```
Формирование URL -> Преобразование данных (если XML) -> Выполнение HTTP-запроса -> Проверка ответа -> Разбор ответа -> Возврат результата
```

**Примеры**:

```python
data = await api._exec(resource='products', method='GET', io_format='JSON')
print(data)
```

### `_parse`

```python
def _parse(self, text: str) -> dict | ElementTree.Element | bool
```

**Назначение**:
Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
`dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае неудачи.

**Как работает функция**:

1. Проверяет формат данных (`self.data_format`).
2. Если формат JSON:
   - Использует `j_loads` для разбора JSON.
   - Возвращает данные из ключа 'PrestaShop', если он есть.
3. Если формат XML:
   - Использует `ElementTree.fromstring` для разбора XML.
   - Возвращает дерево элементов.
4. В случае ошибки разбора логирует ошибку и возвращает `False`.

```
Проверка data_format -> Разбор JSON/XML -> Возврат данных
```

**Примеры**:

```python
data = api._parse(text)
print(data)
```

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]
```

**Назначение**:
Создает новый ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
`dict`: Ответ от API.

**Как работает функция**:

1. Вызывает `_exec` с методом 'POST' и переданными данными.

```
Вызов _exec с методом POST -> Возврат ответа
```

**Примеры**:

```python
data = await api.create(resource='products', data=product_data)
print(data)
```

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]
```

**Назначение**:
Читает ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.
- `**kwargs`: Дополнительные параметры для запроса.

**Возвращает**:
`dict`: Ответ от API.

**Как работает функция**:

1. Вызывает `_exec` с методом 'GET' и переданными параметрами.

```
Вызов _exec с методом GET -> Возврат ответа
```

**Примеры**:

```python
data = await api.read(resource='products', resource_id=123)
print(data)
```

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]
```

**Назначение**:
Обновляет существующий ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
`dict`: Ответ от API.

**Как работает функция**:

1. Вызывает `_exec` с методом 'PUT' и переданными данными.

```
Вызов _exec с методом PUT -> Возврат ответа
```

**Примеры**:

```python
data = await api.write(resource='products', data=product_data)
print(data)
```

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool
```

**Назначение**:
Удаляет ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
`bool`: `True`, если успешно, `False` иначе.

**Как работает функция**:

1. Вызывает `_exec` с методом 'DELETE' и переданными параметрами.

```
Вызов _exec с методом DELETE -> Возврат ответа
```

**Примеры**:

```python
result = await api.unlink(resource='products', resource_id=123)
print(result)
```

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]
```

**Назначение**:
Выполняет поиск ресурсов в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.
- `**kwargs`: Дополнительные параметры для запроса.

**Возвращает**:
`List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Как работает функция**:

1. Вызывает `_exec` с методом 'GET', фильтром и дополнительными параметрами.

```
Вызов _exec с методом GET и фильтром -> Возврат ответа
```

**Примеры**:

```python
results = await api.search(resource='products', filter='[name]=%keyword%')
print(results)
```

### `create_binary`

```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict
```

**Назначение**:
Загружает бинарный файл в ресурс PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
`dict`: Ответ от API.

**Как работает функция**:

1. Открывает файл в бинарном режиме.
2. Устанавливает заголовок `Content-Type` в `application/octet-stream`.
3. Выполняет POST-запрос с использованием `aiohttp.ClientSession` и отправляет содержимое файла в теле запроса.
4. Возвращает JSON-ответ.

```
Открытие файла -> Установка заголовков -> Выполнение POST-запроса -> Возврат JSON-ответа
```

**Примеры**:

```python
response = await api.create_binary(resource='images/products/22', file_path='img.jpg', file_name='image')
print(response)
```

### `_save`

```python
def _save(self, file_name: str, data: dict)
```

**Назначение**:
Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

**Как работает функция**:

1. Использует `save_text_file` для сохранения данных в формате JSON с отступами и отключенным ASCII.

```
Сохранение данных в файл
```

**Примеры**:

```python
api._save(file_name='products.json', data=products)
```

### `get_data`

```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]
```

**Назначение**:
Получает данные из ресурса PrestaShop API и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для API-запроса.

**Возвращает**:
`dict | None`: Данные из API или `False` в случае неудачи.

**Как работает функция**:

1. Вызывает `_exec` для получения данных.
2. Если данные получены, сохраняет их в файл с помощью `_save`.
3. Возвращает данные.

```
Вызов _exec -> Сохранение данных (если есть) -> Возврат данных
```

**Примеры**:

```python
data = await api.get_data(resource='products', display='full')
print(data)
```

### `remove_file`

```python
def remove_file(self, file_path: str)
```

**Назначение**:
Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Как работает функция**:

1. Пытается удалить файл с помощью `os.remove`.
2. В случае ошибки логирует ошибку.

```
Удаление файла -> Логирование ошибки (если необходимо)
```

**Примеры**:

```python
api.remove_file(file_path='img.png')
```

### `get_apis`

```python
async def get_apis(self) -> Optional[dict]
```

**Назначение**:
Получает список всех доступных API асинхронно.

**Параметры**:
Нет

**Возвращает**:
`dict`: Список доступных API.

**Как работает функция**:

1. Вызывает `_exec` для получения списка API.

```
Вызов _exec для получения списка API -> Возврат списка API
```

**Примеры**:

```python
apis = await api.get_apis()
print(apis)
```

### `get_languages_schema`

```python
async def get_languages_schema(self) -> Optional[dict]
```

**Назначение**:
Получает схему для языков асинхронно.

**Параметры**:
Нет

**Возвращает**:
`dict`: Схема языков или `None` в случае неудачи.

**Как работает функция**:

1. Вызывает `_exec` для получения схемы языков.
2. В случае ошибки логирует ошибку и возвращает `None`.

```
Вызов _exec для получения схемы языков -> Возврат схемы языков или None
```

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

**Назначение**:
Загружает изображение в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
`dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1. Разбивает URL изображения на части, чтобы получить расширение.
2. Формирует имя файла.
3. Сохраняет изображение из URL во временный файл.
4. Загружает изображение с помощью `create_binary`.
5. Удаляет временный файл.
6. Возвращает ответ от API.

```
Разбиение URL -> Формирование имени файла -> Сохранение изображения -> Загрузка изображения -> Удаление временного файла -> Возврат ответа
```

**Примеры**:

```python
response = await api.upload_image_async(resource='images/products/22', resource_id=22, img_url='https://example.com/image.jpg', img_name='image')
print(response)
```

### `upload_image`

```python
async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]
```

**Назначение**:
Загружает изображение в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
`dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:

1. Разбивает URL изображения на части, чтобы получить расширение.
2. Формирует имя файла.
3. Сохраняет изображение из URL во временный файл.
4. Загружает изображение с помощью `create_binary`.
5. Удаляет временный файл.
6. Возвращает ответ от API.

```
Разбиение URL -> Формирование имени файла -> Сохранение изображения -> Загрузка изображения -> Удаление временного файла -> Возврат ответа
```

**Примеры**:

```python
response = await api.upload_image(resource='images/products/22', resource_id=22, img_url='https://example.com/image.jpg', img_name='image')
print(response)
```

### `get_product_images`

```python
async def get_product_images(self, product_id: int) -> Optional[dict]
```

**Назначение**:
Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
`dict | None`: Список изображений продукта или `False` в случае неудачи.

**Как работает функция**:

1. Вызывает `_exec` для получения изображений продукта.

```
Вызов _exec для получения изображений продукта -> Возврат изображений продукта или False
```

**Примеры**:

```python
images = await api.get_product_images(product_id=123)
print(images)