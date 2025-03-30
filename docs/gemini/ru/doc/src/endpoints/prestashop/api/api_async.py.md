# Модуль `api_async` для асинхронного взаимодействия с PrestaShop API

## Обзор

Модуль `api_async` предоставляет асинхронный класс `PrestaShopAsync` для взаимодействия с PrestaShop API. Он поддерживает операции CRUD (создание, чтение, обновление, удаление), поиск и загрузку изображений. Модуль предназначен для использования в асинхронных приложениях, обеспечивая неблокирующие вызовы API.

## Подробней

Этот модуль позволяет взаимодействовать с API PrestaShop асинхронно, что особенно полезно для приложений, требующих высокой производительности и отзывчивости. Он включает в себя обработку ошибок, поддержку форматов данных JSON и XML, а также методы для управления ресурсами PrestaShop, такими как продукты, категории и изображения.

## Классы

### `Format`

**Описание**:
Перечисление, определяющее форматы данных для взаимодействия с API (JSON, XML).

**Методы**:
- `JSON`: Представляет формат JSON.
- `XML`: Представляет формат XML.

### `PrestaShopAsync`

**Описание**:
Асинхронный класс для взаимодействия с PrestaShop API.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса асинхронно.
- `_check_response`: Проверяет код ответа HTTP и обрабатывает ошибки асинхронно.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API асинхронно.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API асинхронно.
- `_parse`: Разбирает XML или JSON-ответ от API асинхронно.
- `create`: Создает новый ресурс в PrestaShop API асинхронно.
- `read`: Читает ресурс из PrestaShop API асинхронно.
- `write`: Обновляет существующий ресурс в PrestaShop API асинхронно.
- `unlink`: Удаляет ресурс из PrestaShop API асинхронно.
- `search`: Ищет ресурсы в PrestaShop API асинхронно.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API асинхронно.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их асинхронно.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API асинхронно.
- `get_languages_schema`: Получает схему для языков асинхронно.
- `upload_image_async`: Загружает изображение в PrestaShop API асинхронно.
- `upload_image`: Загружает изображение в PrestaShop API асинхронно.
- `get_product_images`: Получает изображения для продукта асинхронно.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Включает режим отладки. По умолчанию `True`.

**Примеры**
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )

        await api.ping()

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
        rec = await api.create('taxes', data)

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

        update_rec = await api.write('taxes', update_data)

        # Remove this tax
        await api.unlink('taxes', str(rec['id']))

        # Search the first 3 taxes with '5' in the name
        import pprint
        recs = await api.search('taxes', filter='[name]=%[5]%', limit='3')

        for rec in recs:
            pprint(rec)

        # Create binary (product image)
        await api.create_binary('images/products/22', 'img.jpeg', 'image')

    if __name__ == "__main__":
        asyncio.run(main())
```

## Функции

### `ping`

```python
async def ping(self) -> bool:
    """! Test if the webservice is working perfectly asynchronously.

    Returns:
        bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    """
    ...
```

**Описание**:
Проверяет, работает ли веб-сервис PrestaShop асинхронно.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, `False` в противном случае.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        result = await api.ping()
        print(result)
```

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]:
    """! Create a new resource in PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the new resource.

    Returns:
         dict: Response from the API.
    """
    ...
```

**Описание**:
Создает новый ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
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
        rec = await api.create('taxes', data)
        print(rec)
```

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
    """! Read a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**:
Читает ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        rec = await api.read('taxes', 1)
        print(rec)
```

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]:
    """! Update an existing resource in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the resource.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**:
Обновляет существующий ресурс в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict | None`: Ответ от API.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        data = {
            'tax': {
                'id': '1',
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
        rec = await api.write('taxes', data)
        print(rec)
```

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
    """! Delete a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        bool: `True` if successful, `False` otherwise.
    """
    ...
```

**Описание**:
Удаляет ресурс из PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если удаление успешно, `False` в противном случае.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        result = await api.unlink('taxes', 1)
        print(result)
```

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
    """! Search for resources in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        filter (str | dict, optional): Filter for the search.

    Returns:
         List[dict]: List of resources matching the search criteria.
    """
    ...
```

**Описание**:
Выполняет поиск ресурсов в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        recs = await api.search('taxes', filter='[name]=%[5]%', limit='3')
        print(recs)
```

### `create_binary`

```python
async def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
    """! Upload a binary file to a PrestaShop API resource asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        file_path (str): Path to the binary file.
        file_name (str): File name.

    Returns:
        dict: Response from the API.
    """
    ...
```

**Описание**:
Загружает бинарный файл в ресурс PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к бинарному файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        rec = await api.create_binary('images/products/22', 'img.jpeg', 'image')
        print(rec)
```

### `get_data`

```python
async def get_data(self, resource: str, **kwargs) -> Optional[dict]:
    """! Fetch data from a PrestaShop API resource and save it asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        **kwargs: Additional arguments for the API request.

    Returns:
        dict | None: Data from the API or `False` on failure.
    """
    ...
```

**Описание**:
Получает данные из ресурса PrestaShop API и сохраняет их асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `**kwargs`: Дополнительные аргументы для запроса API.

**Возвращает**:
- `dict | None`: Данные из API или `False` в случае неудачи.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        data = await api.get_data('products')
        print(data)
```

### `get_apis`

```python
async def get_apis(self) -> Optional[dict]:
    """! Get a list of all available APIs asynchronously.

    Returns:
         dict: List of available APIs.
    """
    ...
```

**Описание**:
Получает список всех доступных API асинхронно.

**Возвращает**:
- `dict | None`: Список доступных API.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        apis = await api.get_apis()
        print(apis)
```

### `get_languages_schema`

```python
async def get_languages_schema(self) -> Optional[dict]:
    """! Get the schema for languages asynchronously.

    Returns:
        dict: Language schema or `None` on failure.
    """
    ...
```

**Описание**:
Получает схему для языков асинхронно.

**Возвращает**:
- `dict | None`: Схема языков или `None` в случае неудачи.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        schema = await api.get_languages_schema()
        print(schema)
```

### `upload_image`

```python
async def upload_image(self, resource: str, resource_id: int, img_url: str,
                     img_name: Optional[str] = None) -> Optional[dict]:
    """! Upload an image to PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'images/products/22').
        resource_id (int): Resource ID.
        img_url (str): URL of the image.
        img_name (str, optional): Name of the image file, defaults to None.

    Returns:
        dict | None: Response from the API or `False` on failure.
    """
    ...
```

**Описание**:
Загружает изображение в PrestaShop API асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `resource_id` (int): ID ресурса.
- `img_url` (str): URL изображения.
- `img_name` (str, optional): Имя файла изображения, по умолчанию `None`.

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        response = await api.upload_image('images/products/22', 22, 'https://example.com/image.jpg', 'image')
        print(response)
```

### `get_product_images`

```python
async def get_product_images(self, product_id: int) -> Optional[dict]:
    """! Get images for a product asynchronously.

    Args:
        product_id (int): Product ID.

    Returns:
        dict | None: List of product images or `False` on failure.
    """
    ...
```

**Описание**:
Получает изображения для продукта асинхронно.

**Параметры**:
- `product_id` (int): ID продукта.

**Возвращает**:
- `dict | None`: Список изображений продукта или `False` в случае неудачи.

**Примеры**:
```python
    async def main():
        api = PrestaShopAsync(
            API_DOMAIN='https://your-prestashop-domain.com',
            API_KEY='your_api_key',
            default_lang=1,
            debug=True,
            data_format='JSON',
        )
        images = await api.get_product_images(22)
        print(images)