# Модуль для работы с асинхронными HTTP-запросами с использованием aiohttp
====================================================================

Модуль предоставляет классы и функции для выполнения асинхронных HTTP-запросов, включая поддержку потоковой передачи данных, прокси и Server-Sent Events (SSE).

## Оглавление
- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [StreamResponse](#streamresponse)
    - [StreamSession](#streamsession)
- [Функции](#функции)
    - [get_connector](#get_connector)

## Обзор

Этот модуль предназначен для упрощения работы с асинхронными HTTP-запросами в Python, используя библиотеку `aiohttp`. Он предоставляет удобные классы для обработки потоковых ответов и Server-Sent Events, а также поддерживает использование прокси-серверов.

## Подробнее

Модуль содержит классы `StreamResponse` и `StreamSession`, которые расширяют возможности стандартных классов `aiohttp` для обработки потоковых данных и Server-Sent Events. Функция `get_connector` используется для создания коннектора `aiohttp` с поддержкой прокси.

## Классы

### `StreamResponse`

**Описание**: Класс `StreamResponse` расширяет класс `ClientResponse` из библиотеки `aiohttp` и предоставляет методы для асинхронной итерации по строкам, содержимому и событиям, отправленным сервером (SSE).

**Наследует**: `aiohttp.ClientResponse`

**Методы**:

- `iter_lines()`: Асинхронный итератор по строкам ответа.
- `iter_content()`: Асинхронный итератор по содержимому ответа.
- `json(content_type: str = None)`: Асинхронно загружает JSON из ответа.
- `sse()`: Асинхронный итератор по Server-Sent Events ответа.

#### `iter_lines`
```python
    async def iter_lines(self) -> AsyncIterator[bytes]:
        """Асинхронно перебирает строки ответа."""
        ...
```

**Назначение**: Асинхронно перебирает строки ответа, удаляя завершающие символы новой строки.

**Параметры**:
- Нет

**Возвращает**:
- `AsyncIterator[bytes]`: Асинхронный итератор по строкам ответа в байтах.

**Как работает функция**:
1.  Функция итерируется по содержимому ответа, используя `self.content`.
2.  Для каждой строки удаляются завершающие символы новой строки (`\r\n`).
3.  Возвращается строка в байтах.

```
    A (Начало)
    ↓
    B (Итерация по содержимому ответа: async for line in self.content)
    ↓
    C (Удаление завершающих символов новой строки: yield line.rstrip(b"\r\n"))
    ↓
    D (Конец)
```

**Примеры**:
```python
async for line in response.iter_lines():
    print(line)
```
#### `iter_content`
```python
    async def iter_content(self) -> AsyncIterator[bytes]:
        """Асинхронно перебирает содержимое ответа."""
        ...
```

**Назначение**: Асинхронно перебирает содержимое ответа по частям (chunks).

**Параметры**:
- Нет

**Возвращает**:
- `AsyncIterator[bytes]`: Асинхронный итератор по частям содержимого ответа в байтах.

**Как работает функция**:
1. Функция итерируется по содержимому ответа, используя `self.content.iter_any()`.
2. Для каждой части содержимого возвращается эта часть в байтах.

```
    A (Начало)
    ↓
    B (Итерация по частям содержимого: async for chunk in self.content.iter_any())
    ↓
    C (Возврат части содержимого: yield chunk)
    ↓
    D (Конец)
```

**Примеры**:
```python
async for chunk in response.iter_content():
    print(chunk)
```
#### `json`
```python
    async def json(self, content_type: str = None) -> Any:
        """Асинхронно загружает JSON из ответа."""
        ...
```

**Назначение**: Асинхронно загружает JSON из тела ответа.

**Параметры**:
- `content_type` (str, optional): Тип содержимого. По умолчанию `None`.

**Возвращает**:
- `Any`: Десериализованный объект JSON.

**Как работает функция**:
1.  Функция вызывает метод `json` родительского класса `ClientResponse`.
2.  Возвращает десериализованный объект JSON.

```
    A (Начало)
    ↓
    B (Вызов метода json родительского класса: super().json(content_type=content_type))
    ↓
    C (Конец)
```

**Примеры**:
```python
data = await response.json()
print(data)
```
#### `sse`
```python
    async def sse(self) -> AsyncIterator[dict]:
        """Асинхронно перебирает Server-Sent Events ответа."""
        ...
```

**Назначение**: Асинхронно перебирает Server-Sent Events (SSE) ответа.

**Параметры**:
- Нет

**Возвращает**:
- `AsyncIterator[dict]`: Асинхронный итератор по событиям SSE, представленным в виде словарей.

**Как работает функция**:
1.  Функция итерируется по строкам содержимого ответа.
2.  Если строка начинается с "data: ", извлекается полезная нагрузка события.
3.  Если полезная нагрузка начинается с "[DONE]", итерация прекращается.
4.  Полезная нагрузка десериализуется из JSON и возвращается.
5.  Ошибки декодирования JSON игнорируются.

```
    A (Начало)
    ↓
    B (Итерация по строкам содержимого: async for line in self.content)
    ↓
    C (Проверка, начинается ли строка с "data: ": if line.startswith(b"data: "))
    ↓
    D (Извлечение полезной нагрузки: chunk = line[6:])
    ↓
    E (Проверка, начинается ли полезная нагрузка с "[DONE]": if chunk.startswith(b"[DONE]"))
    ↓
    F (Десериализация JSON: json.loads(chunk))
    ↓
    G (Возврат события: yield json.loads(chunk))
    ↓
    H (Обработка ошибок JSONDecodeError)
    ↓
    I (Конец)
```

**Примеры**:
```python
async for event in response.sse():
    print(event)
```

### `StreamSession`

**Описание**: Класс `StreamSession` расширяет класс `ClientSession` из библиотеки `aiohttp` и предоставляет возможность настройки сессии с поддержкой потоковых ответов, прокси и пользовательских заголовков.

**Наследует**: `aiohttp.ClientSession`

**Атрибуты**:
- `headers` (dict): Заголовки HTTP-запроса.
- `timeout` (int): Время ожидания запроса.
- `connector` (BaseConnector): Коннектор для управления подключениями.
- `proxy` (str): URL прокси-сервера.
- `proxies` (dict): Словарь URL прокси-серверов для разных протоколов.
- `impersonate`: Флаг для имитации пользовательского агента.

**Методы**:
- `__init__(self, headers: dict = {}, timeout: int = None, connector: BaseConnector = None, proxy: str = None, proxies: dict = {}, impersonate = None, **kwargs)`: Инициализирует экземпляр класса `StreamSession`.

#### `__init__`

```python
    def __init__(
        self,
        headers: dict = {},\n
        timeout: int = None,\n
        connector: BaseConnector = None,\n
        proxy: str = None,\n
        proxies: dict = {},\n
        impersonate = None,\n
        **kwargs\n
    ):
        """Инициализирует экземпляр класса `StreamSession`."""
        ...
```

**Назначение**: Инициализирует экземпляр класса `StreamSession` с заданными параметрами, такими как заголовки, время ожидания, коннектор, прокси и другие параметры.

**Параметры**:
- `headers` (dict, optional): Заголовки HTTP-запроса. По умолчанию `{}`.
- `timeout` (int, optional): Время ожидания запроса. По умолчанию `None`.
- `connector` (BaseConnector, optional): Коннектор для управления подключениями. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `proxies` (dict, optional): Словарь URL прокси-серверов для разных протоколов. По умолчанию `{}`.
- `impersonate` (optional): Флаг для имитации пользовательского агента. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, передаваемые в конструктор `ClientSession`.

**Как работает функция**:
1. Если указан параметр `impersonate`, добавляет стандартные заголовки в `headers`.
2.  Если `timeout` задан как кортеж, разделяет его на `connect` и `timeout`.
3.  Создает объект `ClientTimeout` на основе переданного `timeout`.
4.  Определяет URL прокси-сервера из параметров `proxy` или `proxies`.
5.  Вызывает конструктор родительского класса `ClientSession` с заданными параметрами.

```
    A (Начало)
    ↓
    B (Если impersonate, добавляет стандартные заголовки)
    ↓
    C (Если timeout - кортеж, разделяет его)
    ↓
    D (Создает ClientTimeout)
    ↓
    E (Определяет URL прокси-сервера)
    ↓
    F (Вызывает конструктор ClientSession)
    ↓
    G (Конец)
```

**Примеры**:
```python
session = StreamSession(headers={'User-Agent': 'MyAgent'}, timeout=30, proxy='http://proxy.example.com')
```

## Функции

### `get_connector`

```python
def get_connector(connector: BaseConnector = None, proxy: str = None, rdns: bool = False) -> Optional[BaseConnector]:
    """Создает коннектор aiohttp с поддержкой прокси."""
    ...
```

**Назначение**: Создает коннектор `aiohttp` с поддержкой прокси, если указан URL прокси-сервера.

**Параметры**:
- `connector` (BaseConnector, optional): Существующий коннектор. По умолчанию `None`.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `rdns` (bool, optional): Флаг для включения удаленного разрешения DNS для SOCKS5 прокси. По умолчанию `False`.

**Возвращает**:
- `Optional[BaseConnector]`: Коннектор `aiohttp` с поддержкой прокси или `None`, если прокси не указан.

**Вызывает исключения**:
- `MissingRequirementsError`: Если не установлен пакет `aiohttp_socks`, необходимый для поддержки прокси.

**Как работает функция**:
1.  Если указан URL прокси-сервера и не передан существующий коннектор, пытается создать `ProxyConnector` из пакета `aiohttp_socks`.
2.  Если `proxy` начинается с "socks5h://", заменяет его на "socks5://", и устанавливает `rdns = True`
3.  Если пакет `aiohttp_socks` не установлен, вызывает исключение `MissingRequirementsError`.
4.  Возвращает созданный коннектор или переданный существующий коннектор.

```
    A (Начало)
    ↓
    B (Если указан прокси и нет коннектора)
    ↓
    C (Пытается создать ProxyConnector)
    ↓
    D (Если прокси начинается с "socks5h://", заменяет его на "socks5://", и устанавливает rdns = True)
    ↓
    E (Если aiohttp_socks не установлен, вызывает MissingRequirementsError)
    ↓
    F (Возвращает коннектор)
    ↓
    G (Конец)
```

**Примеры**:
```python
connector = get_connector(proxy='http://proxy.example.com')
session = StreamSession(connector=connector)
```
```python
connector = get_connector(proxy='socks5://proxy.example.com', rdns=True)
session = StreamSession(connector=connector)
```