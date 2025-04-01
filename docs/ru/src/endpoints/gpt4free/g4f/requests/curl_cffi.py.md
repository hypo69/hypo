# Модуль для работы с асинхронными запросами и потоковыми ответами с использованием `curl_cffi`

## Обзор

Модуль предоставляет классы для выполнения асинхронных HTTP-запросов с поддержкой потоковых ответов, работы с формами данных (FormData) и WebSocket-соединениями. Он использует библиотеку `curl_cffi` для эффективного выполнения сетевых операций.

## Подробней

Этот модуль предназначен для обработки асинхронных HTTP-запросов и потоковых ответов. Он предоставляет инструменты для упрощения работы с серверами, отправляющими данные большими блоками или в режиме реального времени.
Основные компоненты модуля:

- Класс `StreamResponse`: Обертка для обработки асинхронных потоковых ответов.
- Класс `StreamSession`: Асинхронная сессия для выполнения HTTP-запросов с потоковыми ответами.
- Класс `FormData`:  Для создания и управления данными формы, включая добавление полей с файлами.
- Класс `WebSocket`: Для установления и управления WebSocket-соединениями.

## Классы

### `StreamResponse`

**Описание**: Класс-обертка для обработки асинхронных потоковых ответов.

**Принцип работы**: Предоставляет методы для асинхронного получения текста ответа, проверки статуса, разбора JSON-контента, итерации по строкам и содержимому ответа, а также обработки Server-Sent Events (SSE).

**Аттрибуты**:
- `inner` (Response): Оригинальный объект `Response` из библиотеки `curl_cffi`.
- `url` (str): URL запроса.
- `method` (str): HTTP-метод запроса.
- `request` (Any): Объект запроса.
- `status` (int): HTTP-статус код ответа.
- `reason` (str): Описание статуса ответа.
- `ok` (bool): `True`, если статус код находится в диапазоне 200-300, иначе `False`.
- `headers` (Any): Заголовки ответа.
- `cookies` (Any): Куки ответа.

**Методы**:
- `__init__(self, inner: Response) -> None`: Инициализирует `StreamResponse` с предоставленным объектом `Response`.
- `text(self) -> str`: Асинхронно получает текст ответа.
- `raise_for_status(self) -> None`: Вызывает исключение `HTTPError`, если произошла ошибка.
- `json(self, **kwargs) -> Any`: Асинхронно разбирает JSON-контент ответа.
- `iter_lines(self) -> AsyncGenerator[bytes, None]`: Асинхронно итерируется по строкам ответа.
- `iter_content(self) -> AsyncGenerator[bytes, None]`: Асинхронно итерируется по содержимому ответа.
- `sse(self) -> AsyncGenerator[dict, None]`: Асинхронно итерируется по Server-Sent Events ответа.
- `__aenter__(self)`: Асинхронно входит в контекст выполнения для объекта ответа.
- `__aexit__(self, *args)`: Асинхронно выходит из контекста выполнения для объекта ответа.

### `StreamSession`

**Описание**: Асинхронный класс сессии для обработки HTTP-запросов с потоковой передачей.

**Принцип работы**: Наследуется от `AsyncSession` и предоставляет методы для выполнения HTTP-запросов с поддержкой потоковых ответов.

**Методы**:
- `request(self, method: str, url: str, ssl = None, **kwargs) -> StreamResponse`: Создает и возвращает объект `StreamResponse` для данного HTTP-запроса.
- `ws_connect(self, url, *args, **kwargs)`: Устанавливает WebSocket-соединение.
- `_ws_connect(self, url, **kwargs)`: Внутренний метод для установки WebSocket-соединения.
- `head = partialmethod(request, "HEAD")`: Определяет метод `head` как сокращение для `request` с методом "HEAD".
- `get = partialmethod(request, "GET")`: Определяет метод `get` как сокращение для `request` с методом "GET".
- `post = partialmethod(request, "POST")`: Определяет метод `post` как сокращение для `request` с методом "POST".
- `put = partialmethod(request, "PUT")`: Определяет метод `put` как сокращение для `request` с методом "PUT".
- `patch = partialmethod(request, "PATCH")`: Определяет метод `patch` как сокращение для `request` с методом "PATCH".
- `delete = partialmethod(request, "DELETE")`: Определяет метод `delete` как сокращение для `request` с методом "DELETE".
- `options = partialmethod(request, "OPTIONS")`: Определяет метод `options` как сокращение для `request` с методом "OPTIONS".

### `FormData`

**Описание**: Класс для создания и управления данными формы (multipart/form-data).

**Принцип работы**: Если `curl_mime` доступен, класс наследуется от `CurlMime` и предоставляет метод для добавления полей формы. В противном случае, класс выдает исключение `RuntimeError`.

**Методы**:
- `add_field(self, name, data=None, content_type: str = None, filename: str = None) -> None`: Добавляет поле в форму данных.

### `WebSocket`

**Описание**: Класс для работы с WebSocket-соединениями.

**Принцип работы**: Управляет установлением, отправкой и получением данных через WebSocket-соединение.

**Методы**:
- `__init__(self, session, url, **kwargs) -> None`: Инициализирует объект `WebSocket`.
- `__aenter__(self)`: Асинхронно входит в контекст выполнения для объекта `WebSocket`.
- `__aexit__(self, *args)`: Асинхронно выходит из контекста выполнения для объекта `WebSocket`.
- `receive_str(self, **kwargs) -> str`: Асинхронно получает строковые данные из WebSocket-соединения.
- `send_str(self, data: str)`: Асинхронно отправляет строковые данные через WebSocket-соединение.

## Функции

В данном модуле отсутствуют отдельные функции, не относящиеся к классам. Однако, каждый класс содержит методы, которые выполняют определенные функции.

### `StreamResponse.text`

```python
async def text(self) -> str:
    """Asynchronously get the response text."""
    return await self.inner.atext()
```

**Назначение**: Асинхронно получает текстовое представление ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `str`: Текстовое содержимое ответа.

**Как работает функция**:
1. Вызывает метод `atext()` объекта `self.inner` (типа `Response`) для асинхронного получения текста ответа.
2. Возвращает полученный текст.

```
A: Вызов atext()
|
B: Получение текста ответа
|
C: Возврат текста
```

**Примеры**:
```python
async with session.get('https://example.com') as response:
    text_content = await response.text()
    print(text_content)
```

### `StreamResponse.raise_for_status`

```python
def raise_for_status(self) -> None:
    """Raise an HTTPError if one occurred."""
    self.inner.raise_for_status()
```

**Назначение**: Вызывает исключение `HTTPError`, если в процессе выполнения запроса возникла ошибка HTTP.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Как работает функция**:
1. Вызывает метод `raise_for_status()` объекта `self.inner` (типа `Response`). Этот метод проверяет HTTP-статус код ответа и, если он указывает на ошибку (например, 404, 500), вызывает исключение `HTTPError`.

```
A: Вызов raise_for_status()
|
B: Проверка HTTP-статуса
|
C: Вызов исключения HTTPError (если статус код ошибочный)
```

**Примеры**:
```python
async with session.get('https://example.com/nonexistent_page') as response:
    try:
        response.raise_for_status()
    except HTTPError as ex:
        print(f"HTTP error occurred: {ex}")
```

### `StreamResponse.json`

```python
async def json(self, **kwargs) -> Any:
    """Asynchronously parse the JSON response content."""
    return json.loads(await self.inner.acontent(), **kwargs)
```

**Назначение**: Асинхронно разбирает содержимое ответа в формате JSON.

**Параметры**:
- `self`: Ссылка на экземпляр класса.
- `**kwargs`: Дополнительные аргументы, передаваемые в `json.loads()`.

**Возвращает**:
- `Any`: Десериализованный JSON-объект (словарь, список и т.д.).

**Как работает функция**:
1. Асинхронно получает содержимое ответа с помощью `await self.inner.acontent()`.
2. Использует `json.loads()` для десериализации полученного содержимого в JSON-объект.
3. Возвращает десериализованный объект.

```
A: Асинхронное получение контента
|
B: Десериализация JSON
|
C: Возврат JSON-объекта
```

**Примеры**:
```python
async with session.get('https://api.example.com/data') as response:
    data = await response.json()
    print(data['key'])
```

### `StreamResponse.iter_lines`

```python
def iter_lines(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the lines of the response."""
    return  self.inner.aiter_lines()
```

**Назначение**: Асинхронно итерируется по строкам ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор, возвращающий строки ответа в виде байтов.

**Как работает функция**:
1. Возвращает результат вызова `self.inner.aiter_lines()`, который является асинхронным генератором строк ответа.

```
A: Вызов aiter_lines()
|
B: Возврат асинхронного генератора строк
```

**Примеры**:
```python
async with session.get('https://example.com/stream') as response:
    async for line in response.iter_lines():
        print(line)
```

### `StreamResponse.iter_content`

```python
def iter_content(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the response content."""
    return self.inner.aiter_content()
```

**Назначение**: Асинхронно итерируется по содержимому ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор, возвращающий содержимое ответа в виде байтов.

**Как работает функция**:
1. Возвращает результат вызова `self.inner.aiter_content()`, который является асинхронным генератором содержимого ответа.

```
A: Вызов aiter_content()
|
B: Возврат асинхронного генератора содержимого
```

**Примеры**:
```python
async with session.get('https://example.com/image.jpg') as response:
    async for chunk in response.iter_content():
        # Обработка чанка данных
        pass
```

### `StreamResponse.sse`

```python
async def sse(self) -> AsyncGenerator[dict, None]:
    """Asynchronously iterate over the Server-Sent Events of the response."""
    async for line in self.iter_lines():
        if line.startswith(b"data: "):
            chunk = line[6:]
            if chunk == b"[DONE]":
                break
            try:
                yield json.loads(chunk)
            except json.JSONDecodeError:
                continue
```

**Назначение**: Асинхронно итерируется по Server-Sent Events (SSE) ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `AsyncGenerator[dict, None]`: Асинхронный генератор, возвращающий события SSE в виде словарей.

**Как работает функция**:
1. Итерируется по строкам ответа с помощью `self.iter_lines()`.
2. Для каждой строки проверяет, начинается ли она с `b"data: "`.
3. Если строка является SSE-событием, извлекает данные (`chunk`) из строки, удаляя префикс `b"data: "`.
4. Проверяет, является ли `chunk` строкой `b"[DONE]"`. Если да, завершает итерацию.
5. Пытается десериализовать `chunk` из JSON.
6. Если десериализация прошла успешно, возвращает полученный словарь. Если произошла ошибка `JSONDecodeError`, переходит к следующей строке.

```
A: Итерация по строкам ответа
|
B: Проверка на "data: "
|
C: Извлечение данных
|
D: Проверка на "[DONE]"
|
E: Десериализация JSON
|
F: Возврат словаря (если успешно)
```

**Примеры**:
```python
async with session.get('https://example.com/events') as response:
    async for event in response.sse():
        print(event)
```

### `StreamResponse.__aenter__`

```python
async def __aenter__(self):
    """Asynchronously enter the runtime context for the response object."""
    inner: Response = await self.inner
    self.inner = inner
    self.url = inner.url
    self.method = inner.request.method
    self.request = inner.request
    self.status: int = inner.status_code
    self.reason: str = inner.reason
    self.ok: bool = inner.ok
    self.headers = inner.headers
    self.cookies = inner.cookies
    return self
```

**Назначение**: Асинхронно входит в контекст выполнения для объекта ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `self`: Текущий экземпляр класса.

**Как работает функция**:
1. Асинхронно ожидает завершения получения ответа из `self.inner`.
2. Обновляет `self.inner` полученным ответом.
3. Извлекает информацию из `inner` (URL, метод, запрос, статус, причина, заголовки, cookies) и сохраняет их в атрибутах `self`.
4. Возвращает `self`.

```
A: Асинхронное ожидание получения ответа
|
B: Обновление self.inner
|
C: Извлечение данных из inner
|
D: Возврат self
```

**Примеры**:
```python
async with session.get('https://example.com') as response:
    print(response.status)
```

### `StreamResponse.__aexit__`

```python
async def __aexit__(self, *args):
    """Asynchronously exit the runtime context for the response object."""
    await self.inner.aclose()
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта ответа.

**Параметры**:
- `self`: Ссылка на экземпляр класса.
- `*args`: Аргументы, передаваемые при выходе из контекста.

**Как работает функция**:
1. Асинхронно закрывает соединение с помощью `await self.inner.aclose()`.

```
A: Закрытие соединения
```

**Примеры**:
```python
async with session.get('https://example.com') as response:
    # Работа с ответом
    pass
# Соединение автоматически закроется после выхода из блока with
```

### `StreamSession.request`

```python
def request(
    self, method: str, url: str, ssl = None, **kwargs
) -> StreamResponse:
    if kwargs.get("data") and isinstance(kwargs.get("data"), CurlMime):
        kwargs["multipart"] = kwargs.pop("data")
    """Create and return a StreamResponse object for the given HTTP request."""
    return StreamResponse(super().request(method, url, stream=True, verify=ssl, **kwargs))
```

**Назначение**: Создает и возвращает объект `StreamResponse` для данного HTTP-запроса.

**Параметры**:
- `method` (str): HTTP-метод запроса (GET, POST, и т.д.).
- `url` (str): URL запроса.
- `ssl`: Параметры SSL.
- `**kwargs`: Дополнительные аргументы, передаваемые в `super().request()`.

**Возвращает**:
- `StreamResponse`: Объект `StreamResponse`, представляющий ответ на запрос.

**Как работает функция**:
1. Проверяет, переданы ли данные (`kwargs.get("data")`) и являются ли они экземпляром `CurlMime`. Если да, то данные перемещаются из `kwargs["data"]` в `kwargs["multipart"]`.
2. Вызывает метод `super().request()` с параметром `stream=True` и передает ему все аргументы.
3. Создает объект `StreamResponse` на основе полученного ответа и возвращает его.

```
A: Проверка данных и CurlMime
|
B: Вызов super().request() с stream=True
|
C: Создание StreamResponse
|
D: Возврат StreamResponse
```

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
- `url` (str): URL для подключения к WebSocket.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `WebSocket`: Объект `WebSocket`, представляющий соединение.

**Как работает функция**:
1. Создает объект `WebSocket` с использованием текущей сессии, URL и дополнительных аргументов.
2. Возвращает созданный объект `WebSocket`.

```
A: Создание WebSocket
|
B: Возврат WebSocket
```

**Примеры**:
```python
ws = session.ws_connect('wss://example.com')
```

### `WebSocket.__init__`

```python
def __init__(self, session, url, **kwargs) -> None:
    if not has_curl_ws:
        raise RuntimeError("CurlWsFlag in curl_cffi is missing | pip install -U curl_cffi")
    self.session: StreamSession = session
    self.url: str = url
    del kwargs["autoping"]
    self.options: dict = kwargs
```

**Назначение**: Инициализирует объект `WebSocket`.

**Параметры**:
- `session`: Сессия `StreamSession`, используемая для соединения.
- `url` (str): URL для подключения к WebSocket.
- `**kwargs`: Дополнительные именованные аргументы.

**Как работает функция**:
1. Проверяет, доступен ли `CurlWsFlag`. Если нет, вызывает исключение `RuntimeError`.
2. Сохраняет сессию и URL в атрибутах объекта.
3. Удаляет параметр "autoping" из `kwargs`.
4. Сохраняет оставшиеся параметры в атрибуте `options`.

```
A: Проверка CurlWsFlag
|
B: Сохранение сессии и URL
|
C: Удаление "autoping"
|
D: Сохранение опций
```

**Примеры**:
```python
ws = WebSocket(session, 'wss://example.com', autoping=True)
```

### `WebSocket.__aenter__`

```python
async def __aenter__(self):
    self.inner = await self.session._ws_connect(self.url, **self.options)
    return self
```

**Назначение**: Асинхронно входит в контекст выполнения для объекта `WebSocket`.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `self`: Текущий экземпляр класса.

**Как работает функция**:
1. Вызывает `self.session._ws_connect()` для установления WebSocket-соединения.
2. Сохраняет результат (внутренний объект соединения) в `self.inner`.
3. Возвращает `self`.

```
A: Установление соединения
|
B: Сохранение внутреннего объекта
|
C: Возврат self
```

**Примеры**:
```python
async with session.ws_connect('wss://example.com') as ws:
    # Работа с ws
    pass
```

### `WebSocket.__aexit__`

```python
async def __aexit__(self, *args):
    await self.inner.aclose() if hasattr(self.inner, "aclose") else await self.inner.close()
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта `WebSocket`.

**Параметры**:
- `self`: Ссылка на экземпляр класса.
- `*args`: Аргументы, передаваемые при выходе из контекста.

**Как работает функция**:
1. Проверяет, есть ли у `self.inner` метод `aclose()`. Если есть, вызывает его. Иначе вызывает метод `close()`.

```
A: Проверка наличия aclose()
|
B: Вызов aclose() или close()
```

**Примеры**:
```python
async with session.ws_connect('wss://example.com') as ws:
    # Работа с ws
    pass
# Соединение закроется автоматически
```

### `WebSocket.receive_str`

```python
async def receive_str(self, **kwargs) -> str:
    method = self.inner.arecv if hasattr(self.inner, "arecv") else self.inner.recv
    bytes, _ = await method()
    return bytes.decode(errors="ignore")
```

**Назначение**: Асинхронно получает строковые данные из WebSocket-соединения.

**Параметры**:
- `self`: Ссылка на экземпляр класса.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `str`: Полученные строковые данные.

**Как работает функция**:
1. Определяет метод для получения данных: `arecv`, если он существует у `self.inner`, иначе `recv`.
2. Вызывает выбранный метод для получения данных в виде байтов.
3. Декодирует полученные байты в строку с обработкой ошибок.

```
A: Определение метода получения
|
B: Получение байтов
|
C: Декодирование в строку
|
D: Возврат строки
```

**Примеры**:
```python
async with session.ws_connect('wss://example.com') as ws:
    data = await ws.receive_str()
    print(data)
```

### `WebSocket.send_str`

```python
async def send_str(self, data: str):
    method = self.inner.asend if hasattr(self.inner, "asend") else self.inner.send
    await method(data.encode(), CurlWsFlag.TEXT)
```

**Назначение**: Асинхронно отправляет строковые данные через WebSocket-соединение.

**Параметры**:
- `self`: Ссылка на экземпляр класса.
- `data` (str): Строковые данные для отправки.

**Как работает функция**:
1. Определяет метод для отправки данных: `asend`, если он существует у `self.inner`, иначе `send`.
2. Кодирует строку `data` в байты.
3. Вызывает выбранный метод для отправки байтов с флагом `CurlWsFlag.TEXT`.

```
A: Определение метода отправки
|
B: Кодирование в байты
|
C: Отправка байтов
```

**Примеры**:
```python
async with session.ws_connect('wss://example.com') as ws:
    await ws.send_str("Hello, WebSocket!")