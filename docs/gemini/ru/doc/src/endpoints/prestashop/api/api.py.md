# Модуль для взаимодействия с PrestaShop API

## Обзор

Модуль `src.endpoints.prestashop.api` предоставляет класс `PrestaShop` для взаимодействия с PrestaShop webservice API, используя JSON и XML для форматирования сообщений. Он поддерживает CRUD операции, поиск, и загрузку изображений, с обработкой ошибок для ответов.

## Подробней

Этот модуль предназначен для упрощения интеграции с PrestaShop API. Он предоставляет удобный интерфейс для выполнения различных операций, таких как создание, чтение, обновление и удаление данных, а также для загрузки изображений. Модуль автоматически преобразует данные в нужный формат (JSON или XML) и обрабатывает ответы от API, предоставляя разработчику простой и понятный способ взаимодействия с PrestaShop.

## Классы

### `Config`

**Описание**: Конфигурационный класс для PrestaShop API.

**Принцип работы**:
Класс `Config` предназначен для хранения и управления конфигурационными параметрами, необходимыми для взаимодействия с PrestaShop API. Он определяет параметры, такие как язык, версия PrestaShop, режим работы (разработка или продакшн), формат данных для отправки запросов и учетные данные API (домен и ключ). Класс использует переменные окружения, если они доступны, или значения по умолчанию, заданные в коде.

**Атрибуты**:
- `language` (str): Язык.
- `ps_version` (str): Версия PrestaShop (по умолчанию '').
- `MODE` (str): Определяет конечную точку API ('dev', 'dev8', 'prod').
- `POST_FORMAT` (str): Формат данных для отправки запросов ('XML').
- `API_DOMAIN` (str): Домен API.
- `API_KEY` (str): Ключ API.

### `PrestaShop`

**Описание**: Класс для взаимодействия с PrestaShop API.

**Принцип работы**:
Класс `PrestaShop` предоставляет методы для взаимодействия с PrestaShop API, обеспечивая выполнение CRUD-операций, поиска и загрузки изображений. Он поддерживает форматы данных JSON и XML, обрабатывает ошибки и обеспечивает удобный интерфейс для работы с API.

**Атрибуты**:
- `client` (Session): Сессия requests для выполнения HTTP-запросов.
- `debug` (bool): Флаг для активации режима отладки (по умолчанию `False`).
- `language` (Optional[int]): ID языка (по умолчанию `None`).
- `data_format` (str): Формат данных ('JSON' или 'XML') (по умолчанию 'JSON').
- `ps_version` (str): Версия PrestaShop.
- `api_domain` (str): Домен API.
- `api_key` (str): Ключ API.

**Методы**:

- `__init__`: Инициализирует класс `PrestaShop`.
- `ping`: Проверяет доступность веб-сервиса.
- `_check_response`: Проверяет статус ответа и обрабатывает ошибки.
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

## Функции

### `main`

**Назначение**: Функция для проверки сущностей Prestashop.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Определение данных для налога (`tax_data`):** Определяет структуру данных, описывающую налог, который будет создан или обновлен в PrestaShop. Включает ставку налога, активность и название налога на разных языках.
2. **Создание экземпляра `PrestaShop`:** Инициализирует экземпляр класса `PrestaShop` с использованием параметров конфигурации из класса `Config`. Это включает домен API, ключ API, язык по умолчанию и формат данных.
3. **Создание налога:** Использует метод `api.create` для создания нового налога в PrestaShop с использованием определенных ранее данных.
4. **Обновление налога:** Использует метод `api.write` для обновления существующего налога в PrestaShop с использованием тех же данных, что и при создании.

```
Определение tax_data
│
│
↓
Создание экземпляра PrestaShop с параметрами из Config
│
│
↓
Вызов api.create для создания налога
│
│
↓
Вызов api.write для обновления налога
```

**Примеры**:

```python
from src.endpoints.prestashop.api.api import main
main()
```

### `PrestaShop.__init__`

```python
def __init__(
    self,
    api_key: str,
    api_domain: str,
    data_format: str = 'JSON',
    default_lang: int = 1,
    debug: bool = False,
) -> None:
```

**Назначение**: Инициализация класса `PrestaShop`.

**Параметры**:
- `api_key` (str): Ключ API, сгенерированный в PrestaShop.
- `api_domain` (str): Домен магазина PrestaShop (например, https://myPrestaShop.com).
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `default_lang` (int): ID языка по умолчанию. По умолчанию 1.
- `debug` (bool): Активировать режим отладки. По умолчанию `False`.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Инициализация атрибутов экземпляра класса:**
   - Устанавливает значения атрибутов `api_domain`, `api_key`, `debug`, `language` и `data_format` на основе переданных аргументов.
2. **Настройка аутентификации:**
   - Если у клиента `self.client` отсутствует аутентификация, устанавливает ее, используя `api_key` и пустой пароль.
3. **Проверка соединения:**
   - Отправляет `HEAD` запрос к `api_domain` для проверки соединения с сервером PrestaShop.
   - Если соединение не установлено (`response.ok` is `False`), логирует ошибку и завершает работу.
4. **Получение версии PrestaShop:**
   - Получает версию PrestaShop из заголовка ответа `psws-version` и сохраняет ее в атрибуте `ps_version`.

```
Присваивание значений атрибутам экземпляра класса
│
│
↓
Установка аутентификации, если она отсутствует
│
│
↓
Отправка HEAD запроса для проверки соединения
│
│
↓
Получение и сохранение версии PrestaShop из заголовка ответа
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)
```

### `PrestaShop.ping`

```python
def ping(self) -> bool:
```

**Назначение**: Проверка работоспособности веб-сервиса.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `bool`: Результат проверки. Возвращает `True`, если веб-сервис работает, иначе `False`.

**Как работает функция**:

1. **Отправка HEAD-запроса:**
   - Отправляет `HEAD` запрос к `api_domain`.
2. **Проверка ответа:**
   - Вызывает метод `_check_response` для проверки статуса ответа.

```
Отправка HEAD запроса к API_DOMAIN
│
│
↓
Вызов _check_response для проверки статуса ответа
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

if api.ping():
    print('Webservice is working perfectly.')
else:
    print('Webservice is not working.')
```

### `PrestaShop._check_response`

```python
def _check_response(
    self,
    status_code: int,
    response: requests.Response,
    method: Optional[str] = None,
    url: Optional[str] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
) -> bool:
```

**Назначение**: Проверка кода состояния HTTP-ответа и обработка ошибок.

**Параметры**:
- `status_code` (int): Код состояния HTTP-ответа.
- `response` (requests.Response): Объект HTTP-ответа.
- `method` (Optional[str]): HTTP-метод, использованный для запроса.
- `url` (Optional[str]): URL запроса.
- `headers` (Optional[dict]): Заголовки, использованные в запросе.
- `data` (Optional[dict]): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Как работает функция**:

1. **Проверка кода состояния:**
   - Проверяет, находится ли код состояния в диапазоне (200, 201).
   - Если код состояния находится в этом диапазоне, возвращает `True`.
2. **Обработка ошибок:**
   - Если код состояния не находится в диапазоне (200, 201), вызывает метод `_parse_response_error` для обработки ошибки.
   - Возвращает `False`.

```
Проверка status_code на 200 или 201
│
├─── True ───> Возврат True
│
└─── False ──> Вызов _parse_response_error и возврат False
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop
import requests

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = requests.get('https://your-prestashop-domain.com/api/products')
status_ok = api._check_response(response.status_code, response)

if status_ok:
    print('Request was successful.')
else:
    print('Request failed.')
```

### `PrestaShop._parse_response_error`

```python
def _parse_response_error(
    self,
    response: requests.Response,
    method: Optional[str] = None,
    url: Optional[str] = None,
    headers: Optional[dict] = None,
    data: Optional[dict] = None,
) -> None:
```

**Назначение**: Разбор ответа об ошибке от PrestaShop API.

**Параметры**:
- `response` (requests.Response): Объект HTTP-ответа от сервера.
- `method` (Optional[str]): HTTP-метод, использованный для запроса.
- `url` (Optional[str]): URL запроса.
- `headers` (Optional[dict]): Заголовки, использованные в запросе.
- `data` (Optional[dict]): Данные, отправленные в запросе.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Обработка JSON-ответа:**
   - Если формат данных `data_format` равен 'JSON', проверяет код состояния ответа.
   - Если код состояния не находится в диапазоне (200, 201), выполняет `j_dumps` для форматирования JSON-ответа и логирует ошибку с подробной информацией о запросе и ответе.
2. **Обработка XML-ответа:**
   - Если формат данных `data_format` не равен 'JSON', пытается разобрать XML-ответ с помощью метода `_parse_response`.
   - Извлекает код и сообщение об ошибке из XML-ответа.
   - Логирует ошибку с кодом и сообщением.

```
Проверка формата данных (JSON/XML)
│
├─── JSON ───> Проверка status_code, логирование ошибки с JSON-ответом
│
└─── XML ───> Разбор XML-ответа, извлечение кода и сообщения об ошибке, логирование ошибки
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop
import requests

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = requests.get('https://your-prestashop-domain.com/api/nonexistent_resource')
api._parse_response_error(response)
```

### `PrestaShop._prepare_url`

```python
def _prepare_url(self, url: str, params: dict) -> str:
```

**Назначение**: Подготовка URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Как работает функция**:

1. **Подготовка URL с параметрами:**
   - Создает объект `PreparedRequest`.
   - Использует метод `prepare_url` для добавления параметров к базовому URL.
   - Возвращает подготовленный URL.

```
Создание PreparedRequest
│
│
↓
Подготовка URL с параметрами
│
│
↓
Возврат подготовленного URL
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

url = 'https://your-prestashop-domain.com/api/products'
params = {'display': 'full', 'limit': '1'}
prepared_url = api._prepare_url(url, params)
print(prepared_url)
```

### `PrestaShop._exec`

```python
def _exec(
    self,
    resource: str,
    resource_id: Optional[int | str] = None,
    resource_ids: Optional[int | Tuple[int]] = None,
    method: str = 'GET',
    data: Optional[dict | str] = None,
    headers: Optional[dict] = None,
    search_filter: Optional[str | dict] = None,
    display: Optional[str | list] = 'full',
    schema: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[str] = None,
    language: Optional[int] = None,
    data_format: str = 'JSON',
) -> Optional[dict]:
```

**Назначение**: Выполнение HTTP-запроса к PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (Optional[int  |  str]): ID ресурса.
- `resource_ids` (Optional[int  |  Tuple[int]]): ID ресурсов.
- `method` (str): HTTP метод ('GET', 'POST', 'PUT', 'DELETE'). По умолчанию 'GET'.
- `data` (Optional[dict  |  str]): Данные для запроса.
- `headers` (Optional[dict]): Заголовки запроса.
- `search_filter` (Optional[str  |  dict]): Фильтр для поиска.
- `display` (Optional[str  |  list]): Поля для отображения. По умолчанию 'full'.
- `schema` (Optional[str]): Схема для запроса.
- `sort` (Optional[str]): Параметры сортировки.
- `limit` (Optional[str]): Лимит количества возвращаемых ресурсов.
- `language` (Optional[int]): ID языка.
- `data_format` (str): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `Optional[dict]`: Ответ от API.

**Как работает функция**:

1. **Настройка отладки HTTP-соединения:**
   - Устанавливает уровень отладки HTTP-соединения на основе значения `self.debug`.
2. **Подготовка URL:**
   - Подготавливает URL для запроса, используя базовый URL, ресурс и ID ресурса (если указан).
   - Добавляет параметры запроса (фильтр, отображение, схема, сортировка, лимит, язык и формат данных).
3. **Настройка заголовков запроса:**
   - Устанавливает заголовки запроса в зависимости от формата данных (`Content-Type` и `Accept`).
   - Если переданы дополнительные заголовки, добавляет их к основным.
4. **Выполнение HTTP-запроса:**
   - Выполняет HTTP-запрос с использованием метода `self.client.request`.
   - Передает метод, URL, данные и заголовки запроса.
5. **Проверка ответа:**
   - Проверяет статус ответа с помощью метода `_check_response`.
   - Если ответ содержит ошибку, логирует ее и возвращает `False`.
6. **Разбор ответа:**
   - Разбирает ответ с помощью метода `_parse_response`.
   - Возвращает разобранные данные.
7. **Обработка исключений:**
   - Обрабатывает исключения, которые могут возникнуть в процессе выполнения запроса.
   - Логирует ошибку и возвращает `None`.

```
Настройка отладки HTTP-соединения
│
│
↓
Подготовка URL с параметрами
│
│
↓
Настройка заголовков запроса
│
│
↓
Выполнение HTTP-запроса
│
│
↓
Проверка ответа
│
├─── Успех ───> Разбор ответа
│   │
│   ↓
│   Возврат разобранных данных
│
└─── Ошибка ───> Логирование ошибки и возврат False
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

products = api._exec(resource='products', limit='3')
print(products)
```

### `PrestaShop._parse_response`

```python
def _parse_response(self, response: Response, data_format: Optional[str] = 'JSON') -> dict | None:
```

**Назначение**: Разбор XML или JSON ответа от API в структуру dict.

**Параметры**:
- `response` (Response): Объект ответа requests.
- `data_format` (Optional[str]): Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.

**Возвращает**:
- `dict | None`: Разобранные данные или `False` в случае неудачи.

**Как работает функция**:

1. **Определение формата данных:**
   - Определяет, какой формат данных используется (JSON или XML) на основе значения `self.data_format`.
2. **Разбор ответа:**
   - Если формат данных JSON, использует метод `response.json()` для разбора ответа.
   - Если формат данных XML, использует метод `xml2dict` для разбора XML-ответа.
3. **Извлечение данных:**
   - Извлекает данные из разобранного ответа, проверяя наличие ключа 'prestashop'.
   - Если ключ 'prestashop' присутствует, возвращает значение, связанное с этим ключом.
   - В противном случае возвращает весь разобранный ответ.
4. **Обработка исключений:**
   - Обрабатывает исключения, которые могут возникнуть в процессе разбора ответа.
   - Логирует ошибку и возвращает пустой словарь.

```
Определение формата данных (JSON/XML)
│
├─── JSON ───> Разбор JSON-ответа с помощью response.json()
│
└─── XML ───> Разбор XML-ответа с помощью xml2dict
│
↓
Извлечение данных из разобранного ответа
│
├─── Ключ 'prestashop' присутствует ───> Возврат значения, связанного с ключом 'prestashop'
│
└─── Ключ 'prestashop' отсутствует ───> Возврат всего разобранного ответа
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop
import requests

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = requests.get('https://your-prestashop-domain.com/api/products?output_format=JSON')
parsed_data = api._parse_response(response)
print(parsed_data)
```

### `PrestaShop.create`

```python
def create(self, resource: str, data: dict, *args, **kwards) -> Optional[dict]:
```

**Назначение**: Создание нового ресурса в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: API ресурс.
     - `method`: 'POST'.
     - `data`: Данные для нового ресурса.
     - `*args`: Дополнительные аргументы.
     - `**kwards`: Дополнительные именованные аргументы.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, method='POST', data и дополнительными аргументами
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

data = {
    'product': {
        'name': {'language': {'attrs': {'id': '1'}, 'value': 'Test Product'}},
        'active': '1',
    }
}

response = api.create(resource='products', data=data)
print(response)
```

### `PrestaShop.read`

```python
def read(self, resource: str, resource_id: int | str, **kwargs) -> Optional[dict]:
```

**Назначение**: Чтение ресурса из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int  |  str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: API ресурс.
     - `resource_id`: ID ресурса.
     - `method`: 'GET'.
     - `**kwargs`: Дополнительные именованные аргументы.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, resource_id, method='GET' и дополнительными аргументами
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = api.read(resource='products', resource_id=1)
print(response)
```

### `PrestaShop.write`

```python
def write(self, resource: str, data: dict) -> Optional[dict]:
```

**Назначение**: Обновление существующего ресурса в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: API ресурс.
     - `resource_id`: ID ресурса, полученный из `data.get('id')`.
     - `method`: 'PUT'.
     - `data`: Данные для ресурса.
     - `data_format`: Формат данных.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, resource_id, method='PUT', data и data_format
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

data = {
    'product': {
        'id': '1',
        'name': {'language': {'attrs': {'id': '1'}, 'value': 'Updated Product'}},
        'active': '1',
    }
}

response = api.write(resource='products', data=data)
print(response)
```

### `PrestaShop.unlink`

```python
def unlink(self, resource: str, resource_id: int | str) -> bool:
```

**Назначение**: Удаление ресурса из PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int  |  str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, `False` в противном случае.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: API ресурс.
     - `resource_id`: ID ресурса.
     - `method`: 'DELETE'.
     - `data_format`: Формат данных.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, resource_id, method='DELETE' и data_format
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = api.unlink(resource='products', resource_id=1)
print(response)
```

### `PrestaShop.search`

```python
def search(self, resource: str, filter: Optional[str | dict] = None, **kwargs) -> List[dict]:
```

**Назначение**: Поиск ресурсов в PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (Optional[str  |  dict]): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: API ресурс.
     - `search_filter`: Фильтр для поиска.
     - `method`: 'GET'.
     - `**kwargs`: Дополнительные именованные аргументы.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, search_filter, method='GET' и дополнительными аргументами
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = api.search(resource='products', filter='[name]=%Test%')
print(response)
```

### `PrestaShop.create_binary`

```python
def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
```

**Назначение**: Загрузка бинарного файла в ресурс PrestaShop API.

**Параметры**:
- `resource` (str): API ресурс (например, 'images/products/22').
- `file_path` (str): Путь к файлу.
- `file_name` (str): Имя файла.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:

1. **Открытие файла:**
   - Открывает файл по указанному пути в бинарном режиме.
2. **Подготовка данных для запроса:**
   - Создает словарь `files`, содержащий информацию о загружаемом файле (имя, содержимое, MIME-тип).
3. **Выполнение POST-запроса:**
   - Выполняет POST-запрос к указанному ресурсу API с передачей файла в параметре `files`.
   - Передает данные аутентификации.
4. **Обработка ответа:**
   - Проверяет статус ответа на наличие HTTP-ошибок.
   - Разбирает ответ с помощью метода `_parse_response` и возвращает результат.
5. **Обработка исключений:**
   - Обрабатывает исключения, которые могут возникнуть в процессе выполнения запроса.
   - Логирует ошибку и возвращает словарь с информацией об ошибке.

```
Открытие файла в бинарном режиме
│
│
↓
Подготовка данных для POST-запроса (files)
│
│
↓
Выполнение POST-запроса к API с передачей файла
│
│
↓
Проверка статуса ответа на наличие HTTP-ошибок
│
│
↓
Разбор ответа с помощью _parse_response
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(
    api_domain='https://your-prestashop-domain.com',
    api_key='your_api_key',
    default_lang=1,
    debug=True,
    data_format='JSON',
)

response = api.create_binary(resource='images/products/1', file_path='path/to/image.jpg', file_name='image.jpg')
print(response)
```

### `PrestaShop.get_schema`

```python
def get_schema(
    self, resource: Optional[str] = None, resource_id: Optional[int] = None, schema: Optional[str] = 'blank', **kwards
) -> dict | None:
```

**Назначение**: Получение схемы заданного ресурса из PrestaShop API.

**Параметры**:
- `resource` (str): Имя ресурса (например, 'products', 'customers'). Если не указано - вернется список всех схем сущностей, доступных для API ключа.
- `resource_id` (Optinal[str]): ID ресурса.
- `schema` (Optional[str]): Тип схемы:
    - 'blank': Возвращает пустую схему ресурса.
    - 'synopsis': Возвращает упрощенную схему.
    - 'full': Возвращает полную схему.

**Возвращает**:
- `dict  |  None`: Схема запрошенного ресурса или `None` в случае ошибки.

**Как работает функция**:

1. **Вызов метода `_exec`:**
   - Вызывает метод `_exec` с параметрами:
     - `resource`: Имя ресурса.
     - `resource_id`: ID ресурса.
     - `schema`: Тип схемы.
     - `method`: "GET".
     - `**kwards`: Дополнительные именованные аргументы.
   - Возвращает результат выполнения метода `_exec`.

```
Вызов _exec с параметрами resource, resource_id, schema, method="GET" и дополнительными аргументами
│
│
↓
Возврат результата выполнения _exec
```

**Примеры**:

```python
from src.endpoints.prestashop.api import PrestaShop

api = PrestaShop(