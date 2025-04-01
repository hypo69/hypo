# `api_async.py`

## Обзор

Модуль `api_async.py` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с API PrestaShop.
Он поддерживает операции CRUD, поиск, загрузку изображений и обработку ошибок, возвращая данные в формате JSON или XML.

## Содержание
- [Классы](#классы)
  - [`Format`](#format)
  - [`PrestaShopAsync`](#prestashopasync)
- [Функции](#функции)
  - [`ping`](#ping)
  - [`_check_response`](#_check_response)
  - [`_parse_response_error`](#_parse_response_error)
  - [`_prepare`](#_prepare)
  - [`_exec`](#_exec)
  - [`_parse`](#_parse)
  - [`create`](#create)
  - [`read`](#read)
  - [`write`](#write)
  - [`unlink`](#unlink)
  - [`search`](#search)
  - [`create_binary`](#create_binary)
  - [`_save`](#_save)
  - [`get_data`](#get_data)
  - [`remove_file`](#remove_file)
  - [`get_apis`](#get_apis)
  - [`get_languages_schema`](#get_languages_schema)
  - [`upload_image_async`](#upload_image_async)
  - [`upload_image`](#upload_image)
  - [`get_product_images`](#get_product_images)

## Классы

### `Format`

**Описание**:
Перечисление для определения формата данных (JSON, XML).

**Значения**:
- `JSON`
- `XML`

### `PrestaShopAsync`

**Описание**:
Асинхронный класс для взаимодействия с API PrestaShop.
Предоставляет методы для выполнения CRUD операций, поиска и загрузки изображений.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Включает режим отладки. По умолчанию `True`.

**Атрибуты**:
- `client` (ClientSession): Асинхронный HTTP клиент для взаимодействия с API.
- `debug` (bool): Режим отладки.
- `lang_index` (Optional[int]): Индекс языка по умолчанию.
- `data_format` (str): Формат данных по умолчанию.
- `ps_version` (str): Версия PrestaShop.
- `API_DOMAIN` (str): Домен API.
- `API_KEY` (str): Ключ API.

**Методы**:

-   [`__init__`](#__init__)
-   [`ping`](#ping)
-   [`_check_response`](#_check_response)
-   [`_parse_response_error`](#_parse_response_error)
-   [`_prepare`](#_prepare)
-   [`_exec`](#_exec)
-   [`_parse`](#_parse)
-   [`create`](#create)
-   [`read`](#read)
-   [`write`](#write)
-   [`unlink`](#unlink)
-   [`search`](#search)
-   [`create_binary`](#create_binary)
-   [`_save`](#_save)
-   [`get_data`](#get_data)
-   [`remove_file`](#remove_file)
-   [`get_apis`](#get_apis)
-   [`get_languages_schema`](#get_languages_schema)
-   [`upload_image_async`](#upload_image_async)
-   [`upload_image`](#upload_image)
-   [`get_product_images`](#get_product_images)
   
#### `__init__`
```python
def __init__(self, api_domain: str, api_key: str, data_format: str = 'JSON', debug: bool = True) -> None:
```

**Описание**:
Инициализирует класс `PrestaShopAsync`.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Включает режим отладки. По умолчанию `True`.

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Когда ключ API неверен или не существует.
- `PrestaShopException`: Для общих ошибок PrestaShop WebServices.

## Функции

### `ping`
```python
async def ping(self) -> bool:
```
**Описание**:
Проверяет работоспособность веб-сервиса асинхронно.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

### `_check_response`
```python
async def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
```

**Описание**:
Проверяет код ответа HTTP и обрабатывает ошибки асинхронно.

**Параметры**:
- `status_code` (int): Код статуса HTTP ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP ответа.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код статуса 200 или 201, иначе `False`.

### `_parse_response_error`
```python
async def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None, headers: Optional[dict] = None, data: Optional[dict] = None):
```
**Описание**:
Разбирает ответ с ошибкой от API PrestaShop асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP ответа от сервера.
- `method` (str, optional): HTTP метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

### `_prepare`
```python
def _prepare(self, url: str, params: dict) -> str:
```
**Описание**:
Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

### `_exec`
```python
async def _exec(self, resource: str, resource_id: Optional[Union[int, str]] = None, resource_ids: Optional[Union[int, Tuple[int]]] = None, method: str = 'GET', data: Optional[dict] = None, headers: Optional[dict] = None, search_filter: Optional[Union[str, dict]] = None, display: Optional[Union[str, list]] = 'full', schema: Optional[str] = None, sort: Optional[str] = None, limit: Optional[str] = None, language: Optional[int] = None, io_format: str = 'JSON') -> Optional[dict]:
```
**Описание**:
Выполняет HTTP запрос к API PrestaShop асинхронно.

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
- `limit` (str, optional): Ограничение результатов для запроса.
- `language` (int, optional): ID языка для запроса.
- `io_format` (str, optional): Формат данных ('JSON' или 'XML').

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

### `_parse`
```python
async def _parse(self, text: str) -> Union[dict, ElementTree.Element, bool]:
```
**Описание**:
Разбирает XML или JSON ответ от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае ошибки.

### `create`
```python
async def create(self, resource: str, data: dict) -> Optional[dict]:
```
**Описание**:
Создает новый ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `read`
```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
```
**Описание**:
Читает ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `write`
```python
async def write(self, resource: str, data: dict) -> Optional[dict]:
```
**Описание**:
Обновляет существующий ресурс в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

### `unlink`
```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
```
**Описание**:
Удаляет ресурс из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, иначе `False`.

### `search`
```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
```
**Описание**:
Ищет ресурсы в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

### `create_binary`
```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
```
**Описание**:
Загружает бинарный файл в ресурс API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

### `_save`
```python
def _save(self, file_name: str, data: dict):
```
**Описание**:
Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

### `get_data`
```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
```
**Описание**:
Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для запроса API.

**Возвращает**:
- `dict | None`: Данные от API или `False` в случае ошибки.

### `remove_file`
```python
def remove_file(self, file_path: str):
```
**Описание**:
Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

### `get_apis`
```python
async def get_apis(self) -> Optional[dict]:
```
**Описание**:
Получает список всех доступных API асинхронно.

**Возвращает**:
- `dict`: Список доступных API.

### `get_languages_schema`
```python
async def get_languages_schema(self) -> Optional[dict]:
```
**Описание**:
Получает схему для языков асинхронно.

**Возвращает**:
- `dict`: Схема языков или `None` в случае ошибки.

### `upload_image_async`
```python
async def upload_image_async(self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]:
```
**Описание**:
Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

### `upload_image`
```python
async def upload_image(self, resource: str, resource_id: int, img_url: str, img_name: Optional[str] = None) -> Optional[dict]:
```
**Описание**:
Загружает изображение в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае ошибки.

### `get_product_images`
```python
async def get_product_images(self, product_id: int) -> Optional[dict]:
```
**Описание**:
Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае ошибки.