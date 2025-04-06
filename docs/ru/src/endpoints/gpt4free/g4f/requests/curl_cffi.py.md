# Модуль для обработки асинхронных запросов с использованием curl_cffi

## Обзор

Модуль предоставляет классы для выполнения асинхронных HTTP-запросов с поддержкой потоковой передачи данных, WebSocket-соединений и работы с формами FormData. Он использует библиотеку `curl_cffi` для обеспечения высокой производительности и гибкости при взаимодействии с HTTP-серверами.

## Подробней

Этот модуль предоставляет инструменты для асинхронной работы с HTTP-запросами, включая поддержку потоковой передачи данных, WebSocket-соединений и форм FormData. Он предназначен для использования в проектах, требующих эффективного взаимодействия с веб-серверами.

## Классы

### `StreamResponse`

**Описание**: Обертка для обработки асинхронных потоковых ответов.

**Принцип работы**: Класс `StreamResponse` оборачивает объект `Response` из библиотеки `curl_cffi` и предоставляет асинхронные методы для работы с потоковым содержимым ответа. Это позволяет эффективно обрабатывать большие объемы данных, не загружая их все в память сразу.

**Аттрибуты**:
- `inner` (Response): Оригинальный объект `Response`.

**Методы**:
- `text()`: Асинхронно возвращает текстовое представление ответа.
- `raise_for_status()`: Вызывает исключение `HTTPError`, если произошла ошибка.
- `json(**kwargs)`: Асинхронно разбирает JSON-содержимое ответа.
- `iter_lines()`: Асинхронно итерируется по строкам ответа.
- `iter_content()`: Асинхронно итерируется по содержимому ответа.
- `sse()`: Асинхронно итерируется по Server-Sent Events ответа.
- `__aenter__()`: Асинхронно входит в контекст выполнения для объекта ответа.
- `__aexit__(*args)`: Асинхронно выходит из контекста выполнения для объекта ответа.

### `StreamSession`

**Описание**: Асинхронный класс сессии для обработки HTTP-запросов с потоковой передачей.

**Принцип работы**: Класс `StreamSession` наследуется от `AsyncSession` и предоставляет методы для выполнения HTTP-запросов с поддержкой потоковой передачи данных. Он также включает поддержку WebSocket-соединений и форм FormData.

**Методы**:
- `request(method: str, url: str, ssl = None, **kwargs) -> StreamResponse`: Создает и возвращает объект `StreamResponse` для заданного HTTP-запроса.
- `ws_connect(url, *args, **kwargs)`: Устанавливает WebSocket-соединение.
- `_ws_connect(url, **kwargs)`: Внутренний метод для установки WebSocket-соединения.
- `head = partialmethod(request, "HEAD")`: Отправляет HEAD-запрос.
- `get = partialmethod(request, "GET")`: Отправляет GET-запрос.
- `post = partialmethod(request, "POST")`: Отправляет POST-запрос.
- `put = partialmethod(request, "PUT")`: Отправляет PUT-запрос.
- `patch = partialmethod(request, "PATCH")`: Отправляет PATCH-запрос.
- `delete = partialmethod(request, "DELETE")`: Отправляет DELETE-запрос.
- `options = partialmethod(request, "OPTIONS")`: Отправляет OPTIONS-запрос.

### `FormData`

**Описание**: Класс для создания и управления формами FormData.

**Принцип работы**: Класс `FormData` предоставляет методы для добавления полей в форму FormData, включая возможность указания имени поля, данных, типа контента и имени файла.

**Методы**:
- `add_field(self, name, data=None, content_type: str = None, filename: str = None) -> None`: Добавляет поле в форму FormData.

### `WebSocket`

**Описание**: Класс для работы с WebSocket-соединениями.

**Принцип работы**: Класс `WebSocket` предоставляет методы для установки и управления WebSocket-соединениями. Он позволяет отправлять и получать данные через WebSocket, а также закрывать соединение.

**Методы**:
- `__aenter__()`: Асинхронно входит в контекст выполнения для объекта WebSocket.
- `__aexit__(*args)`: Асинхронно выходит из контекста выполнения для объекта WebSocket.
- `receive_str(**kwargs) -> str`: Асинхронно получает строковое сообщение из WebSocket.
- `send_str(data: str)`: Асинхронно отправляет строковое сообщение через WebSocket.

## Функции

### `StreamResponse.text`

```python
async def text(self) -> str:
    """Asynchronously get the response text."""
    return await self.inner.atext()
```

**Назначение**: Асинхронно получает текстовое представление ответа.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Текстовое представление ответа.

**Как работает функция**:
1. Функция вызывает метод `atext()` объекта `inner` (типа `Response`), который асинхронно получает текстовое представление ответа.
2. Возвращает полученное текстовое представление.

```
A: Вызов atext()
|
B: Получение текстового представления ответа
|
C: Возврат текстового представления
```

### `StreamResponse.raise_for_status`

```python
def raise_for_status(self) -> None:
    """Raise an HTTPError if one occurred."""
    self.inner.raise_for_status()
```

**Назначение**: Вызывает исключение `HTTPError`, если произошла ошибка.

**Параметры**:
- Нет

**Возвращает**:
- `None`

**Вызывает исключения**:
- `HTTPError`: Если произошла HTTP-ошибка.

**Как работает функция**:
1. Функция вызывает метод `raise_for_status()` объекта `inner` (типа `Response`), который проверяет статус ответа и вызывает исключение `HTTPError`, если статус указывает на ошибку.

```
A: Вызов raise_for_status()
|
B: Проверка статуса ответа
|
C: Вызов исключения HTTPError (если необходимо)
```

### `StreamResponse.json`

```python
async def json(self, **kwargs) -> Any:
    """Asynchronously parse the JSON response content."""
    return json.loads(await self.inner.acontent(), **kwargs)
```

**Назначение**: Асинхронно разбирает JSON-содержимое ответа.

**Параметры**:
- `**kwargs`: Дополнительные аргументы, которые передаются в функцию `json.loads()`.

**Возвращает**:
- `Any`: Разобранное JSON-содержимое ответа.

**Вызывает исключения**:
- `json.JSONDecodeError`: Если не удалось разобрать JSON-содержимое.

**Как работает функция**:
1. Функция вызывает метод `acontent()` объекта `inner` (типа `Response`), который асинхронно получает содержимое ответа.
2. Использует функцию `json.loads()` для разбора JSON-содержимого.
3. Возвращает разобранное JSON-содержимое.

```
A: Вызов acontent()
|
B: Получение содержимого ответа
|
C: Разбор JSON-содержимого с помощью json.loads()
|
D: Возврат разобранного JSON-содержимого
```

### `StreamResponse.iter_lines`

```python
def iter_lines(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the lines of the response."""
    return  self.inner.aiter_lines()
```

**Назначение**: Асинхронно итерируется по строкам ответа.

**Параметры**:
- Нет

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор строк ответа.

**Как работает функция**:
1. Функция вызывает метод `aiter_lines()` объекта `inner` (типа `Response`), который возвращает асинхронный генератор строк ответа.
2. Возвращает полученный асинхронный генератор.

```
A: Вызов aiter_lines()
|
B: Получение асинхронного генератора строк
|
C: Возврат асинхронного генератора
```

### `StreamResponse.iter_content`

```python
def iter_content(self) -> AsyncGenerator[bytes, None]:
    """Asynchronously iterate over the response content."""
    return self.inner.aiter_content()
```

**Назначение**: Асинхронно итерируется по содержимому ответа.

**Параметры**:
- Нет

**Возвращает**:
- `AsyncGenerator[bytes, None]`: Асинхронный генератор содержимого ответа.

**Как работает функция**:
1. Функция вызывает метод `aiter_content()` объекта `inner` (типа `Response`), который возвращает асинхронный генератор содержимого ответа.
2. Возвращает полученный асинхронный генератор.

```
A: Вызов aiter_content()
|
B: Получение асинхронного генератора содержимого
|
C: Возврат асинхронного генератора
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
- Нет

**Возвращает**:
- `AsyncGenerator[dict, None]`: Асинхронный генератор словарей, представляющих SSE.

**Как работает функция**:
1. Функция асинхронно итерируется по строкам ответа с помощью `self.iter_lines()`.
2. Для каждой строки проверяется, начинается ли она с `b"data: "`.
3. Если строка начинается с `b"data: "`, извлекается содержимое после префикса (chunk).
4. Если chunk равен `b"[DONE]"`, итерация прекращается.
5. Попытка разбора chunk как JSON с помощью `json.loads()`.
6. Если разбор JSON успешен, словарь возвращается через `yield`.
7. Если происходит ошибка `json.JSONDecodeError`, итерация продолжается.

```
A: Итерация по строкам ответа с помощью iter_lines()
|
B: Проверка, начинается ли строка с "data: "
|
C: Извлечение содержимого после "data: " (chunk)
|
D: Проверка, равен ли chunk "[DONE]"
|
E: Попытка разбора chunk как JSON с помощью json.loads()
|
F: Возврат словаря через yield (если разбор JSON успешен)
|
G: Продолжение итерации (если произошла ошибка JSONDecodeError)
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
- Нет

**Возвращает**:
- `self`: Объект `StreamResponse`.

**Как работает функция**:
1. Функция асинхронно ожидает завершения `self.inner` (объекта `Response`).
2. Обновляет `self.inner` полученным результатом.
3. Извлекает и сохраняет атрибуты из `inner`, такие как `url`, `method`, `request`, `status`, `reason`, `ok`, `headers` и `cookies`.
4. Возвращает `self`.

```
A: Ожидание завершения self.inner
|
B: Обновление self.inner
|
C: Извлечение и сохранение атрибутов из inner
|
D: Возврат self
```

### `StreamResponse.__aexit__`

```python
async def __aexit__(self, *args):
    """Asynchronously exit the runtime context for the response object."""
    await self.inner.aclose()
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта ответа.

**Параметры**:
- `*args`: Произвольные аргументы.

**Возвращает**:
- Нет

**Как работает функция**:
1. Функция асинхронно закрывает соединение, вызывая метод `aclose()` объекта `self.inner`.

```
A: Закрытие соединения с помощью aclose()
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

**Назначение**: Создает и возвращает объект `StreamResponse` для заданного HTTP-запроса.

**Параметры**:
- `method` (str): HTTP-метод (например, "GET", "POST").
- `url` (str): URL-адрес запроса.
- `ssl`: Параметры SSL.
- `**kwargs`: Дополнительные аргументы для запроса.

**Возвращает**:
- `StreamResponse`: Объект `StreamResponse`, представляющий HTTP-ответ.

**Как работает функция**:
1. Проверяет, содержит ли `kwargs` ключ "data" и является ли его значение экземпляром `CurlMime`.
2. Если да, то заменяет "data" на "multipart" в `kwargs`.
3. Вызывает метод `request` родительского класса (`AsyncSession`) с параметром `stream=True`.
4. Создает и возвращает объект `StreamResponse`, оборачивающий результат вызова `super().request()`.

```
A: Проверка наличия "data" в kwargs и его типа
|
B: Замена "data" на "multipart" в kwargs (если необходимо)
|
C: Вызов super().request() с stream=True
|
D: Создание и возврат объекта StreamResponse
```

### `StreamSession.ws_connect`

```python
def ws_connect(self, url, *args, **kwargs):
    return WebSocket(self, url, **kwargs)
```

**Назначение**: Устанавливает WebSocket-соединение.

**Параметры**:
- `url`: URL-адрес WebSocket-сервера.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `WebSocket`: Объект `WebSocket`, представляющий WebSocket-соединение.

**Как работает функция**:
1. Создает и возвращает объект `WebSocket` с использованием переданных аргументов.

```
A: Создание объекта WebSocket
|
B: Возврат объекта WebSocket
```

### `StreamSession._ws_connect`

```python
def _ws_connect(self, url, **kwargs):
    return super().ws_connect(url, **kwargs)
```

**Назначение**: Внутренний метод для установки WebSocket-соединения.

**Параметры**:
- `url`: URL-адрес WebSocket-сервера.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- Результат вызова `super().ws_connect()`.

**Как работает функция**:
1. Вызывает метод `ws_connect` родительского класса (`AsyncSession`) с переданными аргументами и возвращает результат.

```
A: Вызов super().ws_connect()
|
B: Возврат результата
```

### `WebSocket.__aenter__`

```python
async def __aenter__(self):
    self.inner = await self.session._ws_connect(self.url, **self.options)
    return self
```

**Назначение**: Асинхронно входит в контекст выполнения для объекта WebSocket.

**Параметры**:
- Нет

**Возвращает**:
- `self`: Объект `WebSocket`.

**Как работает функция**:
1. Асинхронно устанавливает WebSocket-соединение с использованием `self.session._ws_connect()`.
2. Сохраняет результат в `self.inner`.
3. Возвращает `self`.

```
A: Асинхронная установка WebSocket-соединения
|
B: Сохранение результата в self.inner
|
C: Возврат self
```

### `WebSocket.__aexit__`

```python
async def __aexit__(self, *args):
    await self.inner.aclose() if hasattr(self.inner, "aclose") else await self.inner.close()
```

**Назначение**: Асинхронно выходит из контекста выполнения для объекта WebSocket.

**Параметры**:
- `*args`: Произвольные аргументы.

**Возвращает**:
- Нет

**Как работает функция**:
1. Асинхронно закрывает WebSocket-соединение.
2. Если у `self.inner` есть метод `aclose()`, то вызывается он, иначе вызывается метод `close()`.

```
A: Проверка наличия метода aclose() у self.inner
|
B: Вызов aclose() или close() в зависимости от результата проверки
```

### `WebSocket.receive_str`

```python
async def receive_str(self, **kwargs) -> str:
    method = self.inner.arecv if hasattr(self.inner, "arecv") else self.inner.recv
    bytes, _ = await method()
    return bytes.decode(errors="ignore")
```

**Назначение**: Асинхронно получает строковое сообщение из WebSocket.

**Параметры**:
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- `str`: Строковое сообщение, полученное из WebSocket.

**Как работает функция**:
1. Определяет метод для получения данных из WebSocket. Если у `self.inner` есть метод `arecv`, то используется он, иначе используется метод `recv`.
2. Асинхронно получает данные из WebSocket с помощью выбранного метода.
3. Декодирует полученные байты в строку с использованием кодировки UTF-8 и обработкой ошибок.
4. Возвращает полученную строку.

```
A: Определение метода для получения данных (arecv или recv)
|
B: Асинхронное получение данных из WebSocket
|
C: Декодирование байтов в строку
|
D: Возврат полученной строки
```

### `WebSocket.send_str`

```python
async def send_str(self, data: str):
    method = self.inner.asend if hasattr(self.inner, "asend") else self.inner.send
    await method(data.encode(), CurlWsFlag.TEXT)
```

**Назначение**: Асинхронно отправляет строковое сообщение через WebSocket.

**Параметры**:
- `data` (str): Строковое сообщение для отправки.

**Возвращает**:
- Нет

**Как работает функция**:
1. Определяет метод для отправки данных через WebSocket. Если у `self.inner` есть метод `asend`, то используется он, иначе используется метод `send`.
2. Кодирует строку `data` в байты с использованием кодировки UTF-8.
3. Асинхронно отправляет закодированные данные через WebSocket с использованием выбранного метода и флага `CurlWsFlag.TEXT`.

```
A: Определение метода для отправки данных (asend или send)
|
B: Кодирование строки в байты
|
C: Асинхронная отправка данных через WebSocket