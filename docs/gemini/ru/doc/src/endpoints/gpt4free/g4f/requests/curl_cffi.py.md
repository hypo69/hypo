# Модуль для работы с асинхронными запросами и потоковыми ответами с использованием curl_cffi
=========================================================================================

Модуль предоставляет классы для выполнения асинхронных HTTP-запросов с поддержкой потоковых ответов, WebSocket и FormData.
Он использует библиотеку `curl_cffi` для эффективной работы с HTTP-запросами.

## Обзор

Модуль содержит классы `StreamResponse`, `StreamSession`, `FormData` и `WebSocket`, которые позволяют выполнять асинхронные HTTP-запросы и обрабатывать потоковые ответы.
Класс `StreamSession` наследуется от `AsyncSession` и предоставляет методы для выполнения HTTP-запросов с потоковой передачей данных.
Класс `FormData` используется для создания multipart/form-data запросов.
Класс `WebSocket` обеспечивает поддержку WebSocket соединений.

## Подробнее

Этот модуль предназначен для упрощения работы с асинхронными HTTP-запросами, особенно при необходимости обрабатывать большие объемы данных потоково.
Он предоставляет удобные интерфейсы для выполнения запросов, обработки ответов и работы с WebSocket соединениями.
Модуль использует библиотеку `curl_cffi`, которая обеспечивает высокую производительность и гибкость при выполнении HTTP-запросов.

## Классы

### `StreamResponse`

**Описание**: Класс-обертка для обработки асинхронных потоковых ответов.

**Принцип работы**:
Класс `StreamResponse` оборачивает объект `Response` из библиотеки `curl_cffi` и предоставляет методы для асинхронного чтения текста, JSON-данных, итерации по строкам и содержимому ответа.
Он также поддерживает асинхронный контекстный менеджер для автоматического закрытия соединения.

**Атрибуты**:
- `inner` (Response): Оригинальный объект `Response`.

**Методы**:
- `__init__(self, inner: Response) -> None`: Инициализирует `StreamResponse` с предоставленным объектом `Response`.
- `text(self) -> str`: Асинхронно получает текст ответа.
- `raise_for_status(self) -> None`: Вызывает исключение `HTTPError`, если произошла ошибка.
- `json(self, **kwargs) -> Any`: Асинхронно разбирает содержимое JSON-ответа.
- `iter_lines(self) -> AsyncGenerator[bytes, None]`: Асинхронно итерируется по строкам ответа.
- `iter_content(self) -> AsyncGenerator[bytes, None]`: Асинхронно итерируется по содержимому ответа.
- `sse(self) -> AsyncGenerator[dict, None]`: Асинхронно итерируется по Server-Sent Events (SSE) ответа.
- `__aenter__(self)`: Асинхронно входит в контекст выполнения для объекта ответа.
- `__aexit__(self, *args)`: Асинхронно выходит из контекста выполнения для объекта ответа и закрывает соединение.

### `StreamSession`

**Описание**: Асинхронный класс сессии для обработки HTTP-запросов с потоковой передачей.

**Наследует**:
- `AsyncSession`: Наследует от класса `AsyncSession` из библиотеки `curl_cffi`.

**Принцип работы**:
Класс `StreamSession` наследуется от `AsyncSession` и переопределяет метод `request` для возврата объекта `StreamResponse`.
Он также предоставляет методы для выполнения HTTP-запросов с использованием различных HTTP-методов (GET, POST, PUT, DELETE и т.д.).

**Методы**:
- `request(self, method: str, url: str, ssl = None, **kwargs) -> StreamResponse`: Создает и возвращает объект `StreamResponse` для заданного HTTP-запроса.
- `ws_connect(self, url, *args, **kwargs)`: Устанавливает WebSocket-соединение.
- `_ws_connect(self, url, **kwargs)`: Внутренний метод для установки WebSocket-соединения.
- `head = partialmethod(request, "HEAD")`: Определяет метод `head` как partialmethod для выполнения HTTP-запроса с методом HEAD.
- `get = partialmethod(request, "GET")`: Определяет метод `get` как partialmethod для выполнения HTTP-запроса с методом GET.
- `post = partialmethod(request, "POST")`: Определяет метод `post` как partialmethod для выполнения HTTP-запроса с методом POST.
- `put = partialmethod(request, "PUT")`: Определяет метод `put` как partialmethod для выполнения HTTP-запроса с методом PUT.
- `patch = partialmethod(request, "PATCH")`: Определяет метод `patch` как partialmethod для выполнения HTTP-запроса с методом PATCH.
- `delete = partialmethod(request, "DELETE")`: Определяет метод `delete` как partialmethod для выполнения HTTP-запроса с методом DELETE.
- `options = partialmethod(request, "OPTIONS")`: Определяет метод `options` как partialmethod для выполнения HTTP-запроса с методом OPTIONS.

### `FormData`

**Описание**: Класс для создания multipart/form-data запросов.

**Принцип работы**:
Класс `FormData` предоставляет интерфейс для создания multipart/form-data запросов.
Если библиотека `curl_cffi` имеет поддержку `CurlMime`, то `FormData` наследуется от `CurlMime` и использует его методы для добавления полей.
В противном случае, `FormData` выбрасывает исключение `RuntimeError`.

**Методы**:
- `add_field(self, name, data=None, content_type: str = None, filename: str = None) -> None`: Добавляет поле в multipart/form-data запрос.

### `WebSocket`

**Описание**: Класс для работы с WebSocket соединениями.

**Принцип работы**:
Класс `WebSocket` предоставляет интерфейс для установления и управления WebSocket соединениями.
Он использует методы `curl_cffi` для отправки и получения данных через WebSocket.

**Методы**:
- `__init__(self, session, url, **kwargs) -> None`: Инициализирует объект `WebSocket`.
- `__aenter__(self)`: Асинхронно входит в контекст выполнения для объекта WebSocket.
- `__aexit__(self, *args)`: Асинхронно выходит из контекста выполнения для объекта WebSocket и закрывает соединение.
- `receive_str(self, **kwargs) -> str`: Асинхронно получает строковые данные из WebSocket соединения.
- `send_str(self, data: str)`: Асинхронно отправляет строковые данные через WebSocket соединение.

## Функции

### `StreamResponse.text`

```python
async def text(self) -> str:
    """Asynchronously get the response text."""
    ...
```

**Назначение**: Асинхронно получает текст ответа.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Текст ответа.

**Как работает функция**:
1. Функция `text` вызывает метод `atext()` объекта `self.inner` (типа `Response`), который асинхронно получает текст ответа.
2. Возвращает полученный текст.

**Примеры**:

```python
async with session.get('https://example.com') as response:
    text = await response.text()
    print(text)
```

### `StreamResponse.raise_for_status`

```python
def raise_for_status(self) -> None:
    """Raise an HTTPError if one occurred."""
    ...
```

**Назначение**: Вызывает исключение `HTTPError`, если произошла ошибка.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Функция `raise_for_status` вызывает метод `raise_for_status()` объекта `self.inner` (типа `Response`), который проверяет статус код ответа и вызывает исключение `HTTPError`, если статус код указывает на ошибку (например, 404, 500).
2.  Если статус код не указывает на ошибку, функция ничего не делает.

**Примеры**:

```python
async with session.get('https://example.com/nonexistent') as response:
    try:
        response.raise_for_status()
    except HTTPError as ex:
        print(f"HTTP error occurred: {ex}")
```

### `StreamResponse.json`

```python
async def json(self, **kwargs) -> Any:
    """Asynchronously parse the JSON response content."""
    ...
```

**Назначение**: Асинхронно разбирает содержимое JSON-ответа.

**Параметры**:
- `**kwargs`: Дополнительные аргументы, которые передаются в функцию `json.loads`.

**Возвращает**:
- `Any`: Разобранное содержимое JSON-ответа.

**Как работает функция**:
1.  Функция `json` вызывает метод `acontent()` объекта `self.inner` (типа `Response`), который асинхронно получает содержимое ответа в виде байтов.
2.  Затем функция вызывает `json.loads` для разбора содержимого JSON.
3.  Возвращает разобранное содержимое JSON.

**Примеры**:

```python
async with session.get('https://example.com/api/data') as response:
    data = await response.json()
    print(data)
```

### `StreamResponse.iter_lines`

```python
def iter_lines(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the lines of the response."""
    ...
```

**Назначение**: Асинхронно итерируется по строкам ответа.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор, который выдает строки ответа в виде байтов.

**Как работает функция**:
1. Функция `iter_lines` вызывает метод `aiter_lines()` объекта `self.inner` (типа `Response`), который возвращает асинхронный генератор строк ответа.
2. Функция возвращает полученный генератор.

**Примеры**:

```python
async with session.get('https://example.com/large_text_file') as response:
    async for line in response.iter_lines():
        print(line)
```

### `StreamResponse.iter_content`

```python
def iter_content(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the response content."""
    ...
```

**Назначение**: Асинхронно итерируется по содержимому ответа.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор, который выдает содержимое ответа в виде байтов.

**Как работает функция**:
1. Функция `iter_content` вызывает метод `aiter_content()` объекта `self.inner` (типа `Response`), который возвращает асинхронный генератор содержимого ответа.
2. Функция возвращает полученный генератор.

**Примеры**:

```python
async with session.get('https://example.com/large_image.jpg') as response:
    async for chunk in response.iter_content():
        # Обработка чанков изображения
        pass
```

### `StreamResponse.sse`

```python
async def sse(self) -> AsyncGenerator[dict, None]:
    """Asynchronously iterate over the Server-Sent Events of the response."""
    ...
```

**Назначение**: Асинхронно итерируется по Server-Sent Events (SSE) ответа.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `AsyncGenerator[dict, None]`: Асинхронный генератор, который выдает события SSE в виде словарей.

**Как работает функция**:
1.  Функция `sse` вызывает метод `iter_lines()` для получения асинхронного генератора строк ответа.
2.  Затем функция итерируется по строкам ответа и проверяет, начинается ли строка с `b"data: "`.
3.  Если строка начинается с `b"data: "`, функция извлекает данные события и пытается разобрать их как JSON.
4.  Если разбор JSON успешен, функция выдает событие в виде словаря.
5.  Если встречается строка `b"[DONE]"`, функция завершает итерацию.

**Примеры**:

```python
async with session.get('https://example.com/sse_stream') as response:
    async for event in response.sse():
        print(event)
```

### `StreamResponse.__aenter__`

```python
async def __aenter__(self):
    """Asynchronously enter the runtime context for the response object."""
    ...
```

**Назначение**: Асинхронно входит в контекст выполнения для объекта ответа.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `self`: Объект `StreamResponse`.

**Как работает функция**:
1.  Функция `__aenter__` ожидает завершения асинхронной операции `self.inner`.
2.  После завершения асинхронной операции функция обновляет атрибут `self.inner` результатом этой операции (объектом `Response`).
3.  Функция устанавливает атрибуты `url`, `method`, `request`, `status`, `reason`, `ok`, `headers` и `cookies` объекта `StreamResponse` на значения соответствующих атрибутов объекта `self.inner`.
4.  Возвращает объект `self`.

**Примеры**:

```python
async with session.get('https://example.com') as response:
    print(response.status)
```

### `StreamResponse.__aexit__`

```python
async def __aexit__(self, *args):
    """Asynchronously exit the runtime context for the response object."""
    ...
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта ответа и закрывает соединение.

**Параметры**:
- `*args`: Аргументы исключения, переданные из блока `with`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Функция `__aexit__` вызывает метод `aclose()` объекта `self.inner`, который асинхронно закрывает соединение.

**Примеры**:

```python
async with session.get('https://example.com') as response:
    # Обработка ответа
    pass
# Соединение будет автоматически закрыто после выхода из блока with
```

### `StreamSession.request`

```python
def request(
    self, method: str, url: str, ssl = None, **kwargs
) -> StreamResponse:
    if kwargs.get("data") and isinstance(kwargs.get("data"), CurlMime):
        kwargs["multipart"] = kwargs.pop("data")
    """Create and return a StreamResponse object for the given HTTP request."""
    ...
```

**Назначение**: Создает и возвращает объект `StreamResponse` для заданного HTTP-запроса.

**Параметры**:
- `method` (str): HTTP-метод (GET, POST, PUT, DELETE и т.д.).
- `url` (str): URL-адрес запроса.
- `ssl`: Параметры SSL. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы, которые передаются в функцию `super().request`.

**Возвращает**:
- `StreamResponse`: Объект `StreamResponse`.

**Как работает функция**:
1.  Функция `request` проверяет, передан ли параметр `data` и является ли он экземпляром класса `CurlMime`. Если это так, то параметр `data` переименовывается в `multipart`.
2.  Функция вызывает метод `super().request` с параметрами `method`, `url`, `stream=True`, `verify=ssl` и `**kwargs`.
    Метод `super().request` выполняет HTTP-запрос и возвращает объект `Response`.
3.  Функция создает объект `StreamResponse` с полученным объектом `Response`.
4.  Функция возвращает объект `StreamResponse`.

**Примеры**:

```python
response = session.get('https://example.com')
```

### `StreamSession.ws_connect`

```python
def ws_connect(self, url, *args, **kwargs):
    return WebSocket(self, url, **kwargs)
```

**Назначение**: Устанавливает WebSocket-соединение.

**Параметры**:
- `url`: URL-адрес WebSocket-соединения.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `WebSocket`: Объект `WebSocket`.

**Как работает функция**:
1.  Функция `ws_connect` создает объект `WebSocket` с параметрами `self`, `url` и `**kwargs`.
2.  Возвращает объект `WebSocket`.

**Примеры**:

```python
async with session.ws_connect('wss://example.com') as ws:
    await ws.send_str('Hello, WebSocket!')
```

### `StreamSession._ws_connect`

```python
def _ws_connect(self, url, **kwargs):
    return super().ws_connect(url, **kwargs)
```

**Назначение**: Внутренний метод для установки WebSocket-соединения.

**Параметры**:
- `url`: URL-адрес WebSocket-соединения.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- Результат вызова `super().ws_connect(url, **kwargs)`.

**Как работает функция**:
1.  Функция `_ws_connect` вызывает метод `super().ws_connect` с параметрами `url` и `**kwargs`.
2.  Возвращает результат вызова `super().ws_connect(url, **kwargs)`.

### `FormData.add_field`

```python
def add_field(self, name, data=None, content_type: str = None, filename: str = None) -> None:
    self.addpart(name, content_type=content_type, filename=filename, data=data)
```

**Назначение**: Добавляет поле в multipart/form-data запрос.

**Параметры**:
- `name`: Имя поля.
- `data`: Данные поля. По умолчанию `None`.
- `content_type`: Тип содержимого поля. По умолчанию `None`.
- `filename`: Имя файла поля. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Функция `add_field` вызывает метод `addpart` объекта `self` (типа `CurlMime`) с параметрами `name`, `content_type`, `filename` и `data`.
    Метод `addpart` добавляет поле в multipart/form-data запрос.

**Примеры**:

```python
form = FormData()
form.add_field('name', 'John Doe')
form.add_field('file', data=b'file content', filename='example.txt', content_type='text/plain')
```

### `WebSocket.__aenter__`

```python
async def __aenter__(self):
    self.inner = await self.session._ws_connect(self.url, **self.options)
    return self
```

**Назначение**: Асинхронно входит в контекст выполнения для объекта WebSocket.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `self`: Объект `WebSocket`.

**Как работает функция**:
1. Функция `__aenter__` вызывает метод `_ws_connect` объекта `self.session` с параметрами `self.url` и `**self.options`.
2. Функция ожидает завершения асинхронной операции `self.session._ws_connect`.
3. Функция устанавливает атрибут `self.inner` результатом этой операции.
4. Возвращает объект `self`.

### `WebSocket.__aexit__`

```python
async def __aexit__(self, *args):
    await self.inner.aclose() if hasattr(self.inner, "aclose") else await self.inner.close()
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта WebSocket и закрывает соединение.

**Параметры**:
- `*args`: Аргументы исключения, переданные из блока `with`.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Функция `__aexit__` проверяет, есть ли у объекта `self.inner` метод `aclose`.
2.  Если метод `aclose` есть, функция вызывает его асинхронно.
3.  Если метода `aclose` нет, функция вызывает метод `close` асинхронно.

### `WebSocket.receive_str`

```python
async def receive_str(self, **kwargs) -> str:
    method = self.inner.arecv if hasattr(self.inner, "arecv") else self.inner.recv
    bytes, _ = await method()
    return bytes.decode(errors="ignore")
```

**Назначение**: Асинхронно получает строковые данные из WebSocket соединения.

**Параметры**:
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `str`: Строковые данные, полученные из WebSocket соединения.

**Как работает функция**:
1.  Функция `receive_str` проверяет, есть ли у объекта `self.inner` метод `arecv`.
2.  Если метод `arecv` есть, функция присваивает его переменной `method`.
3.  Если метода `arecv` нет, функция присваивает переменной `method` метод `recv`.
4.  Функция вызывает метод `method` асинхронно и получает байты и флаги.
5.  Функция декодирует полученные байты в строку, игнорируя ошибки декодирования.
6.  Возвращает полученную строку.

### `WebSocket.send_str`

```python
async def send_str(self, data: str):
    method = self.inner.asend if hasattr(self.inner, "asend") else self.inner.send
    await method(data.encode(), CurlWsFlag.TEXT)
```

**Назначение**: Асинхронно отправляет строковые данные через WebSocket соединение.

**Параметры**:
- `data` (str): Строковые данные для отправки.

**Возвращает**:
- `None`

**Как работает функция**:
1.  Функция `send_str` проверяет, есть ли у объекта `self.inner` метод `asend`.
2.  Если метод `asend` есть, функция присваивает его переменной `method`.
3.  Если метода `asend` нет, функция присваивает переменной `method` метод `send`.
4.  Функция кодирует строку `data` в байты.
5.  Функция вызывает метод `method` асинхронно с параметрами `data.encode()` и `CurlWsFlag.TEXT`.