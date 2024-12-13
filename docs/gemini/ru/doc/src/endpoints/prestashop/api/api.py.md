# Модуль `src.endpoints.prestashop.api.api.py`

## Обзор

Модуль `api.py` предоставляет класс `PrestaShop` для взаимодействия с веб-сервисом PrestaShop API. Он поддерживает операции CRUD, поиск и загрузку изображений, а также обеспечивает обработку ошибок и преобразование данных между форматами JSON и XML.

## Оглавление

- [Классы](#классы)
    - [`Format`](#class-format)
    - [`PrestaShop`](#class-prestashop)
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
   
   **Описание**: Представляет собой перечисление (Enum) с возможными форматами данных для ответа (JSON, XML).

   **Детали**:
   - `JSON`: Представляет формат JSON.
   - `XML`: Представляет формат XML.
   - `@deprecated` - Предпочтительный формат - JSON.

### `PrestaShop`
   
   **Описание**: Класс для взаимодействия с API PrestaShop, поддерживающий JSON и XML форматы.

   **Детали**:
   - Предоставляет методы для выполнения CRUD-операций, поиска и загрузки изображений.
   - Обрабатывает ошибки ответов от API.
   - Позволяет взаимодействовать с данными, используя JSON и XML.
    
   **Параметры**:
     - `API_KEY` (`str`): API-ключ, полученный в PrestaShop.
     - `API_DOMAIN` (`str`): Домен PrestaShop (например, `https://myPrestaShop.com`).
     - `data_format` (`str`): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
     - `default_lang` (`int`): ID языка по умолчанию. По умолчанию 1.
     - `debug` (`bool`): Включение режима отладки. По умолчанию `True`.
   
   **Вызывает исключения**:
     - `PrestaShopAuthenticationError`: Если API-ключ неверный или отсутствует.
     - `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.
   
   **Пример использования**:
    ```python
    from PrestaShop import PrestaShop, Format
    
    api = PrestaShop(
    API_DOMAIN = "https://myPrestaShop.com",
    API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    default_lang=1,
    debug=True,
    data_format='JSON',
    )
    
    api.ping()
    
    data = {
        'tax': {
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }
    
    # Create tax record
    rec = api.create('taxes', data)
    
    # Update the same tax record
    update_data = {
        'tax': {
            'id': str(rec['id']),
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }
    
    update_rec = api.write('taxes', update_data)
    
    # Remove this tax
    api.unlink('taxes', str(rec['id']))
    
    # Search the first 3 taxes with '5' in the name
    import pprint
    recs = api.search('taxes', filter='[name]=%[5]%', limit='3')
    
    for rec in recs:
        pprint(rec)
    
    # Create binary (product image)
    api.create_binary('images/products/22', 'img.jpeg', 'image')
    ```

### `__init__`
   
   **Описание**: Инициализация класса PrestaShop.
   
   **Параметры**:
     - `data_format` (`str`, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
     - `default_lang` (`int`, optional): ID языка по умолчанию. По умолчанию 1.
     - `debug` (`bool`, optional): Включение режима отладки. По умолчанию `True`.
    
   **Возвращает**:
      - `None`

## Функции

### `ping`
   
   **Описание**: Проверяет работоспособность веб-сервиса.
   
   **Возвращает**:
     - `bool`: `True`, если веб-сервис работает, иначе `False`.

### `_check_response`
   
   **Описание**: Проверяет код ответа HTTP и обрабатывает ошибки.
   
   **Параметры**:
     - `status_code` (`int`): Код ответа HTTP.
     - `response` (`requests.Response`): Объект ответа HTTP.
     - `method` (`str`, optional): HTTP метод, использованный для запроса.
     - `url` (`str`, optional): URL запроса.
     - `headers` (`dict`, optional): Заголовки запроса.
     - `data` (`dict`, optional): Данные запроса.
    
   **Возвращает**:
     - `bool`: `True`, если код ответа 200 или 201, иначе `False`.

### `_parse_response_error`
   
   **Описание**: Анализирует ошибку в ответе от API PrestaShop.
   
   **Параметры**:
     - `response` (`requests.Response`): Объект ответа HTTP.
     - `method` (`str`, optional): HTTP метод, использованный для запроса.
     - `url` (`str`, optional): URL запроса.
     - `headers` (`dict`, optional): Заголовки запроса.
     - `data` (`dict`, optional): Данные запроса.
    
   **Возвращает**:
      - `response` или `code, message`

### `_prepare`
   
   **Описание**: Подготавливает URL для запроса.
   
   **Параметры**:
     - `url` (`str`): Базовый URL.
     - `params` (`dict`): Параметры запроса.
   
   **Возвращает**:
      - `str`: URL с параметрами.

### `_exec`
   
   **Описание**: Выполняет HTTP-запрос к API PrestaShop.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products', 'categories').
     - `resource_id` (`int | str`, optional): ID ресурса.
     - `resource_ids` (`int | tuple`, optional): ID нескольких ресурсов.
     - `method` (`str`, optional): HTTP метод (GET, POST, PUT, DELETE). По умолчанию 'GET'.
     - `data` (`dict`, optional): Данные для запроса.
     - `headers` (`dict`, optional): Дополнительные заголовки.
     - `search_filter` (`str | dict`, optional): Фильтр для запроса.
     - `display` (`str | list`, optional): Поля для отображения в ответе. По умолчанию 'full'.
     - `schema` (`str`, optional): Схема данных.
     - `sort` (`str`, optional): Параметр сортировки.
     - `limit` (`str`, optional): Лимит результатов.
     - `language` (`int`, optional): ID языка для запроса.
     - `io_format` (`str`, optional): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.
    
   **Возвращает**:
      - `dict | None`: Ответ от API или `False` при ошибке.

### `_parse`
   
   **Описание**: Разбирает XML или JSON ответ от API.
   
   **Параметры**:
     - `text` (`str`): Текст ответа.
    
   **Возвращает**:
     - `dict | ElementTree.Element | bool`: Разобранные данные или `False` при ошибке.

### `create`
   
   **Описание**: Создает новый ресурс в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `data` (`dict`): Данные для нового ресурса.
    
   **Возвращает**:
      - `dict`: Ответ от API.

### `read`
   
   **Описание**: Читает ресурс из PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `resource_id` (`int | str`): ID ресурса.
     - `**kwargs`: Дополнительные аргументы для запроса.

   **Возвращает**:
     - `dict`: Ответ от API.

### `write`
   
   **Описание**: Обновляет существующий ресурс в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `data` (`dict`): Данные для ресурса.

   **Возвращает**:
     - `dict`: Ответ от API.

### `unlink`
   
   **Описание**: Удаляет ресурс из PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `resource_id` (`int | str`): ID ресурса.
    
   **Возвращает**:
      - `bool`: `True` при успехе, иначе `False`.

### `search`
   
   **Описание**: Поиск ресурсов в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `filter` (`str | dict`, optional): Фильтр для поиска.
     - `**kwargs`: Дополнительные аргументы для запроса.
    
   **Возвращает**:
      - `List[dict]`: Список ресурсов, соответствующих критериям поиска.

### `create_binary`
   
   **Описание**: Загружает бинарный файл в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'images/products/22').
     - `file_path` (`str`): Путь к бинарному файлу.
     - `file_name` (`str`): Имя файла.
   
   **Возвращает**:
     - `dict`: Ответ от API.

### `_save`
   
   **Описание**: Сохраняет данные в файл.
   
   **Параметры**:
     - `file_name` (`str`): Имя файла.
     - `data` (`dict`): Данные для сохранения.

### `get_data`
   
   **Описание**: Получает данные из ресурса PrestaShop API и сохраняет их.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'products').
     - `**kwargs`: Дополнительные аргументы для запроса API.
    
   **Возвращает**:
      - `dict | None`: Данные из API или `False` при ошибке.

### `remove_file`
   
   **Описание**: Удаляет файл из файловой системы.
   
   **Параметры**:
     - `file_path` (`str`): Путь к файлу.

### `get_apis`
   
   **Описание**: Возвращает список всех доступных API.
   
   **Возвращает**:
      - `dict`: Список доступных API.

### `get_languages_schema`
   
   **Описание**: Получает схему для языков.
   
   **Возвращает**:
      - `dict`: Схема языков или `None` при ошибке.

### `upload_image_async`
   
   **Описание**: Асинхронная загрузка изображения в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'images/products/22').
     - `resource_id` (`int`): ID ресурса.
     - `img_url` (`str`): URL изображения.
     - `img_name` (`str`, optional): Имя файла изображения.
    
   **Возвращает**:
      - `dict | None`: Ответ от API или `False` при ошибке.

### `upload_image`
   
   **Описание**: Загружает изображение в PrestaShop API.
   
   **Параметры**:
     - `resource` (`str`): Ресурс API (например, 'images/products/22').
     - `resource_id` (`int`): ID ресурса.
     - `img_url` (`str`): URL изображения.
     - `img_name` (`str`, optional): Имя файла изображения.
   
   **Возвращает**:
      - `dict | None`: Ответ от API или `False` при ошибке.

### `get_product_images`
   
   **Описание**: Получает изображения для продукта.
   
   **Параметры**:
     - `product_id` (`int`): ID продукта.
    
   **Возвращает**:
      - `dict | None`: Список изображений продукта или `False` при ошибке.