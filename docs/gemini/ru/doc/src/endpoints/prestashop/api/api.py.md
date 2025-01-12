# Модуль для взаимодействия с API PrestaShop

## Обзор

Этот модуль предоставляет класс `PrestaShop` для взаимодействия с API PrestaShop, используя JSON и XML для форматирования сообщений. Он поддерживает операции CRUD, поиск и загрузку изображений, а также обработку ошибок для ответов.

## Содержание

- [Классы](#Классы)
    - [`PrestaShop`](#PrestaShop)
- [Функции](#Функции)
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

### `PrestaShop`

**Описание**: Класс для взаимодействия с API PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс PrestaShop.
- `ping`: Проверяет работоспособность веб-сервиса.
- `_check_response`: Проверяет статус ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop.
- `_parse`: Разбирает XML или JSON ответ от API.
- `create`: Создает новый ресурс в API PrestaShop.
- `read`: Получает ресурс из API PrestaShop.
- `write`: Обновляет существующий ресурс в API PrestaShop.
- `unlink`: Удаляет ресурс из API PrestaShop.
- `search`: Выполняет поиск ресурсов в API PrestaShop.
- `create_binary`: Загружает бинарный файл в API PrestaShop.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса API PrestaShop и сохраняет их.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API.
- `get_languages_schema`: Получает схему для языков.
- `upload_image_async`: Асинхронно загружает изображение в API PrestaShop.
- `upload_image`: Загружает изображение в API PrestaShop.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `API_KEY` (str): API ключ, сгенерированный в PrestaShop.
- `API_DOMAIN` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int, optional): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool, optional): Активировать режим отладки. По умолчанию True.

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Вызывается, если API ключ неверный или не существует.
- `PrestaShopException`: Вызывается для общих ошибок веб-сервисов PrestaShop.

## Функции

### `ping`

**Описание**: Проверяет, работает ли веб-сервис PrestaShop.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

### `_check_response`

**Описание**: Проверяет код состояния ответа и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): HTTP-код состояния ответа.
- `response` (requests.Response): Объект HTTP-ответа.
- `method` (Optional[str], optional): HTTP метод, использованный в запросе.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

### `_parse_response_error`

**Описание**: Разбирает ответ об ошибке от API PrestaShop.

**Параметры**:
- `response` (requests.Response): Объект HTTP-ответа от сервера.
- `method` (Optional[str], optional): HTTP метод, использованный в запросе.
- `url` (Optional[str], optional): URL запроса.
- `headers` (Optional[dict], optional): Заголовки, использованные в запросе.
- `data` (Optional[dict], optional): Данные, отправленные в запросе.

**Возвращает**:
- `requests.Response`: Объект ответа, если формат данных JSON.
- `tuple[str, str]`: Код и сообщение об ошибке, если формат данных XML.

### `_prepare`

**Описание**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

### `_exec`

**Описание**: Выполняет HTTP-запрос к API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products', 'categories').
- `resource_id` (Optional[Union[int, str]], optional): ID ресурса.
- `resource_ids` (Optional[Union[int, Tuple[int]]], optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE). По умолчанию 'GET'.
- `data` (Optional[dict], optional): Данные для отправки с запросом.
- `headers` (Optional[dict], optional): Дополнительные заголовки для запроса.
- `search_filter` (Optional[Union[str, dict]], optional): Фильтр для запроса.
- `display` (Optional[Union[str, list]], optional): Поля для отображения в ответе. По умолчанию 'full'.
- `schema` (Optional[str], optional): Схема данных.
- `sort` (Optional[str], optional): Параметр сортировки для запроса.
- `limit` (Optional[str], optional): Лимит результатов для запроса.
- `language` (Optional[int], optional): ID языка для запроса.
- `io_format` (str, optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `Optional[dict]`: Ответ от API или `False` в случае неудачи.

### `_parse`

**Описание**: Разбирает XML или JSON ответ от API.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `Union[dict, ElementTree.Element, bool]`: Разобранные данные, объект `ElementTree` или `False` при неудаче.

### `create`

**Описание**: Создает новый ресурс в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

### `read`

**Описание**: Получает ресурс из API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `resource_id` (Union[int, str]): ID ресурса.
- `**kwargs`: Дополнительные параметры для запроса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

### `write`

**Описание**: Обновляет существующий ресурс в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

### `unlink`

**Описание**: Удаляет ресурс из API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `resource_id` (Union[int, str]): ID ресурса.

**Возвращает**:
- `bool`: `True`, если удаление прошло успешно, `False` в противном случае.

### `search`

**Описание**: Выполняет поиск ресурсов в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `filter` (Optional[Union[str, dict]], optional): Фильтр для поиска.
- `**kwargs`: Дополнительные параметры для запроса.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

### `create_binary`

**Описание**: Загружает бинарный файл в ресурс API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

### `_save`

**Описание**: Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.

### `get_data`

**Описание**: Получает данные из ресурса API PrestaShop и сохраняет их.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products').
- `**kwargs`: Дополнительные аргументы для запроса API.

**Возвращает**:
- `Optional[dict]`: Данные от API или `False` при неудаче.

### `remove_file`

**Описание**: Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

### `get_apis`

**Описание**: Получает список всех доступных API.

**Возвращает**:
- `Optional[dict]`: Список доступных API.

### `get_languages_schema`

**Описание**: Получает схему для языков.

**Возвращает**:
- `Optional[dict]`: Схема языков или `None` в случае неудачи.

### `upload_image_async`

**Описание**: Асинхронно загружает изображение в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `Optional[dict]`: Ответ от API или `False` при неудаче.

### `upload_image`

**Описание**: Загружает изображение в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (Optional[str], optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `Optional[dict]`: Ответ от API или `False` при неудаче.

### `get_product_images`

**Описание**: Получает изображения для продукта.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `Optional[dict]`: Список изображений продукта или `False` в случае неудачи.