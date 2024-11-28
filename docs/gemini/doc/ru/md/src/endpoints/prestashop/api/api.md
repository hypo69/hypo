# Модуль hypotez/src/endpoints/prestashop/api/api.py

## Обзор

Этот модуль предоставляет класс `PrestaShop`, позволяющий взаимодействовать с веб-сервисом API PrestaShop.  Он поддерживает операции CRUD, поиск и загрузку изображений, используя JSON и XML для обмена данными.  Модуль обрабатывает ошибки ответов API и предоставляет инструменты для работы с полученными данными.

## Перечисления

### `Format`

**Описание**: Перечисление `Format` определяет типы данных, возвращаемые API (JSON или XML). По умолчанию используется JSON.

**Значения**:
- `JSON`: JSON формат.
- `XML`: XML формат.


## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с API PrestaShop.

**Методы**:

#### `__init__`

**Описание**: Инициализирует класс `PrestaShop`.

**Параметры**:
- `data_format` (str, optional): Формат данных (JSON или XML). По умолчанию JSON.
- `default_lang` (int, optional): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool, optional): Включить режим отладки. По умолчанию True.

**API ключи**:
- `API_DOMAIN` (str): Домен API Престашопа.
- `API_KEY` (str): API ключ.

**Возвращает**:
- `None`

#### `ping`

**Описание**: Проверяет работоспособность веб-сервиса.

**Параметры**:
- Нет

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.


#### `_check_response`

**Описание**: Проверяет код ответа и обрабатывает ошибки.

**Параметры**:
- `status_code` (int): Код HTTP ответа.
- `response` (requests.Response): Объект HTTP ответа.
- `method` (str, optional): HTTP метод.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки запроса.
- `data` (dict, optional): Данные запроса.

**Возвращает**:
- `bool`: `True`, если код ответа 200 или 201, иначе `False`.


#### `_parse_response_error`

**Описание**: Парсит ответ с ошибкой от API PrestaShop.

**Параметры**:
- `response` (requests.Response): Ответ сервера.

**Возвращает**:
- Возвращает `requests.Response` при возникновении ошибки JSON, и код и сообщение об ошибке в случае XML


#### `_prepare`

**Описание**: Подготавливает URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.


#### `_exec`

**Описание**: Выполняет HTTP запрос к API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'products', 'categories').
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE). По умолчанию GET.
- `data` (dict, optional): Данные для отправки.
- `headers` (dict, optional): Дополнительные заголовки.
- `search_filter` (str | dict, optional): Фильтр для поиска.
- `display` (str | list, optional): Поля для отображения в ответе.
- `schema` (str | None, optional): Схема данных.
- `sort` (str, optional): Параметр сортировки.
- `limit` (str, optional): Ограничение результатов.
- `language` (int, optional): ID языка.
- `io_format` (str, optional): Формат данных (JSON или XML). По умолчанию JSON.

**Возвращает**:
- `dict | None`: Ответ от API или `False` при ошибке.


#### `_parse`

**Описание**: Парсит XML или JSON ответ от API.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разбор данных или `False` при ошибке.


#### `create`

**Описание**: Создает новый ресурс в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

#### `read`

**Описание**: Читает ресурс из API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `resource_id` (int | str): ID ресурса.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `dict`: Ответ от API.

#### `write`

**Описание**: Обновляет существующий ресурс в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

#### `unlink`

**Описание**: Удаляет ресурс из API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True` при успехе, `False` в противном случае.

#### `search`

**Описание**: Ищет ресурсы в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

#### `create_binary`

**Описание**: Загружает бинарный файл в ресурс API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.


#### `_save`

**Описание**: Сохраняет данные в файл.

**Параметры**:
- `file_name` (str): Имя файла.
- `data` (dict): Данные для сохранения.


#### `get_data`

**Описание**: Получает данные из ресурса API PrestaShop и сохраняет их в файл.

**Параметры**:
- `resource` (str): Ресурс API.
- `**kwargs`: Дополнительные аргументы для запроса API.

**Возвращает**:
- `dict | None`: Данные из API или `False` при ошибке.



#### `remove_file`

**Описание**: Удаляет файл из файловой системы.

**Параметры**:
- `file_path` (str): Путь к файлу.

**Возвращает**:
- Нет


#### `get_apis`

**Описание**: Получает список доступных API.

**Параметры**:
- Нет

**Возвращает**:
- `dict`: Список доступных API.


#### `get_languages_schema`

**Описание**: Получает схему для языков.

**Параметры**:
- Нет

**Возвращает**:
- `dict`: Схема языков или `None` при ошибке.


#### `upload_image_async`

**Описание**: Асинхронно загружает изображение в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения.

**Возвращает**:
- `dict | None`: Ответ API или `None` при ошибке.


#### `upload_image`

**Описание**: Загружает изображение в API PrestaShop.

**Параметры**:
- `resource` (str): Ресурс API.
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения.

**Возвращает**:
- `dict | None`: Ответ API или `None` при ошибке.

#### `get_product_images`

**Описание**: Получает список изображений для продукта.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` при ошибке.