# Модуль для взаимодействия с PrestaShop API

## Обзор

Модуль `api.py` предоставляет класс `PrestaShop` для взаимодействия с PrestaShop webservice API.
Он использует JSON и XML для форматирования сообщений и поддерживает CRUD операции, поиск и загрузку изображений.
Также включает обработку ошибок для ответов API.

## Подробнее

Этот модуль упрощает взаимодействие с PrestaShop API, предоставляя удобный интерфейс для выполнения различных операций,
таких как создание, чтение, обновление и удаление данных, а также поиск и загрузка изображений.
Класс `PrestaShop` абстрагирует детали реализации API, позволяя разработчикам сосредоточиться на логике своего приложения.

## Классы

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop API.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaShop`.
- `ping`: Проверяет, работает ли веб-сервис.
- `_check_response`: Проверяет код состояния HTTP-ответа и обрабатывает ошибки.
- `_parse_response_error`: Разбирает ответ об ошибке от PrestaShop API.
- `_prepare_url`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к PrestaShop API.
- `_parse_response`: Разбирает XML или JSON ответ от API в структуру dict.
- `create`: Создает новый ресурс в PrestaShop API.
- `read`: Читает ресурс из PrestaShop API.
- `write`: Обновляет существующий ресурс в PrestaShop API.
- `unlink`: Удаляет ресурс из PrestaShop API.
- `search`: Ищет ресурсы в PrestaShop API.
- `create_binary`: Загружает бинарный файл в ресурс PrestaShop API.
- `get_schema`: Получает схему заданного ресурса из PrestaShop API.
- `get_data`: Получает данные из ресурса PrestaShop API и сохраняет их.
- `get_apis`: Получает список всех доступных API.
- `upload_image_async`: Асинхронно загружает изображение в PrestaShop API.
- `upload_image_from_url`: Загружает изображение в PrestaShop API.
- `get_product_images`: Получает изображения для продукта.

**Параметры**:
- `api_key` (str): API ключ, сгенерированный из PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию `False`.

**Примеры**:

```python
from src.endpoints.prestashop.api.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
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

## Функции

### `__init__`

```python
def __init__(self,
            api_key:str,
            api_domain:str,
            data_format: str = 'JSON',
            default_lang: int = 1,
            debug: bool = False) -> None:
    """Initialize the PrestaShop class.

    :param data_format: Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
    :type data_format: str
    :param default_lang: Default language ID. Defaults to 1.
    :type default_lang: int
    :param debug: Activate debug mode. Defaults to True.
    :type debug: bool
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `PrestaShop`.

**Параметры**:
- `api_key` (str): API ключ для доступа к PrestaShop API.
- `api_domain` (str): Доменное имя магазина PrestaShop.
- `data_format` (str): Формат данных, используемый для обмена данными с API (JSON или XML). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Флаг, указывающий, включен ли режим отладки. По умолчанию `False`.

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
def ping(self) -> bool:
    """Test if the webservice is working perfectly.

    :return: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    :rtype: bool
    """
    ...
```

**Описание**: Проверяет, доступен ли веб-сервис PrestaShop API.

**Возвращает**:
- `bool`: `True`, если веб-сервис работает, иначе `False`.

**Примеры**:

```python
is_available = api.ping()
if is_available:
    print('Webservice is working')
else:
    print('Webservice is not working')
```

### `read`

```python
def read(self, resource: str, resource_id: int | str, **kwargs) -> Optional[dict]:
    """Read a resource from the PrestaShop API.

    :param resource: API resource (e.g., 'products').
    :type resource: str
    :param resource_id: Resource ID.
    :type resource_id: int | str

    :return: Response from the API.
    :rtype: dict
    """
    ...
```

**Описание**: Читает ресурс из PrestaShop API.

**Параметры**:
- `resource` (str): Тип ресурса API (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict | None`: Ответ от API или `None` в случае ошибки.

**Примеры**:

```python
product = api.read(resource='products', resource_id=1)
if product:
    print(product)
else:
    print('Product not found')
```