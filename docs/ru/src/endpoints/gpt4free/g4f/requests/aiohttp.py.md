# Модуль aiohttp

## Обзор

Модуль `aiohttp` предназначен для организации асинхронных HTTP-запросов и обработки потоковых ответов. Он содержит классы и функции, упрощающие взаимодействие с серверами по протоколу HTTP, включая поддержку прокси и Server-Sent Events (SSE).

## Подробнее

Этот модуль предоставляет асинхронные инструменты для работы с HTTP-запросами, обработки потоковых данных и интеграции с прокси-серверами. Основной целью является эффективная обработка сетевых запросов в асинхронном режиме.

## Классы

### `StreamResponse`

**Описание**: Класс `StreamResponse` расширяет стандартный класс `ClientResponse` из библиотеки `aiohttp` и добавляет методы для итерации по строкам и содержимому ответа, а также для обработки Server-Sent Events (SSE).

**Принцип работы**:
Этот класс переопределяет стандартные методы `iter_lines`, `iter_content` и `json` для обеспечения более удобной работы с потоковыми данными и SSE.

**Методы**:

- `iter_lines`

```python
    async def iter_lines(self) -> AsyncIterator[bytes]:
        """
        Асинхронно итерирует по строкам ответа.

        Args:
            None

        Returns:
            AsyncIterator[bytes]: Асинхронный итератор байтовых строк, полученных из ответа.

        Raises:
            Нет.

        """
```

- `iter_content`

```python
    async def iter_content(self) -> AsyncIterator[bytes]:
        """
        Асинхронно итерирует по содержимому ответа.

        Args:
            None

        Returns:
            AsyncIterator[bytes]: Асинхронный итератор байтовых чанков, полученных из ответа.

        Raises:
            Нет.
        """
```

- `json`

```python
    async def json(self, content_type: str = None) -> Any:
        """
        Асинхронно декодирует JSON-ответ.

        Args:
            content_type (str, optional): Тип контента. По умолчанию `None`.

        Returns:
            Any: Декодированные JSON данные.

        Raises:
            Нет.
        """
```

- `sse`

```python
    async def sse(self) -> AsyncIterator[dict]:
        """
        Асинхронно итерирует по Server-Sent Events ответа.

        Args:
            None

        Returns:
            AsyncIterator[dict]: Асинхронный итератор словарей, представляющих SSE события.

        Raises:
            Нет.
        """
```

### `StreamSession`

**Описание**: Класс `StreamSession` расширяет стандартный класс `ClientSession` из библиотеки `aiohttp` и предоставляет возможность использовать прокси, устанавливать таймауты и добавлять заголовки по умолчанию.

**Принцип работы**:
Этот класс инициализирует сессию с заданными параметрами, такими как заголовки, таймауты, прокси и коннекторы. Он также позволяет имитировать определенные версии браузеров для обхода защиты от ботов.

- В конструкторе происходит следующая работа:
    1.  **Инициализация заголовков**: Если указан параметр `impersonate`, заголовки объединяются с `DEFAULT_HEADERS`.
    2.  **Обработка таймаута**: Если `timeout` является кортежем, он разделяется на `connect` и `timeout`. Затем создается объект `ClientTimeout`.
    3.  **Обработка прокси**: Если `proxy` не указан, он извлекается из словаря `proxies`.
    4.  **Инициализация сессии**: Вызывается конструктор родительского класса `ClientSession` с переданными параметрами.

**Методы**:

- `__init__`

```python
    def __init__(
        self,
        headers: dict = {},
        timeout: int = None,
        connector: BaseConnector = None,
        proxy: str = None,
        proxies: dict = {},
        impersonate = None,
        **kwargs
    ):
        """
        Инициализирует StreamSession.

        Args:
            headers (dict, optional): Заголовки для сессии. По умолчанию `{}`.
            timeout (int, optional): Таймаут для сессии. По умолчанию `None`.
            connector (BaseConnector, optional): Коннектор для сессии. По умолчанию `None`.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            proxies (dict, optional): Словарь прокси-серверов. По умолчанию `{}`.
            impersonate (optional): Параметр для имитации браузера. По умолчанию `None`.
            **kwargs: Дополнительные аргументы для ClientSession.

        Raises:
            Нет.
        """
```

## Функции

### `get_connector`

```python
def get_connector(connector: BaseConnector = None, proxy: str = None, rdns: bool = False) -> Optional[BaseConnector]:
    """
    Возвращает коннектор для aiohttp с поддержкой прокси.

    Args:
        connector (BaseConnector, optional): Существующий коннектор. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        rdns (bool, optional): Флаг для удаленного разрешения DNS. По умолчанию `False`.

    Returns:
        Optional[BaseConnector]: Коннектор с поддержкой прокси или `None`, если прокси не требуется.

    Raises:
        MissingRequirementsError: Если отсутствует пакет `aiohttp_socks` и требуется прокси.
    """
```

**Как работает функция**:

1.  **Проверка прокси и коннектора**: Функция проверяет, указан ли прокси-сервер и отсутствует ли коннектор.
2.  **Инициализация прокси-коннектора**: Если прокси указан и коннектор отсутствует, функция пытается создать прокси-коннектор с использованием библиотеки `aiohttp_socks`.
    *   Если URL прокси начинается с `socks5h://`, он заменяется на `socks5://`, и устанавливается флаг `rdns`.
    *   Создается экземпляр `ProxyConnector` из URL прокси.
3.  **Обработка ошибки импорта**: Если библиотека `aiohttp_socks` не установлена, вызывается исключение `MissingRequirementsError`.
4.  **Возврат коннектора**: Функция возвращает созданный или переданный коннектор.

**Примеры**:

```python
from aiohttp import BaseConnector
from aiohttp.connector import TCPConnector

# Пример 1: Использование функции без прокси
connector = get_connector()
print(connector)  # Output: None

# Пример 2: Использование функции с прокси
try:
    connector = get_connector(proxy="socks5://user:password@127.0.0.1:1080")
    print(type(connector))  # Output: <class 'aiohttp_socks.connector.ProxyConnector'>
except MissingRequirementsError as ex:
    print(f"Error: {ex}")

# Пример 3: Использование функции с существующим коннектором
existing_connector = TCPConnector()
connector = get_connector(connector=existing_connector, proxy="socks5://user:password@127.0.0.1:1080")
print(connector is existing_connector)  # Output: True