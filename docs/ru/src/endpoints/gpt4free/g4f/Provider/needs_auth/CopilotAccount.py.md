# Модуль CopilotAccount

## Обзор

Модуль `CopilotAccount` предоставляет класс `CopilotAccount`, который является асинхронным провайдером авторизации для работы с Copilot. Он использует файлы HAR для получения токена доступа и cookies, а также поддерживает авторизацию через веб-интерфейс, если файл HAR недействителен.

## Подробнее

Этот модуль является частью системы провайдеров в проекте `hypotez` и предназначен для интеграции с сервисом Copilot. Он обеспечивает автоматическую аутентификацию и позволяет использовать Copilot для генерации текста.

## Классы

### `CopilotAccount`

**Описание**: Класс `CopilotAccount` является наследником `AsyncAuthedProvider` и `Copilot`. Он реализует асинхронную авторизацию и предоставляет методы для взаимодействия с Copilot.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную авторизацию.
- `Copilot`: Предоставляет методы для взаимодействия с Copilot API.

**Атрибуты**:
- `needs_auth` (bool): Указывает, требуется ли авторизация для использования данного провайдера. Всегда `True`.
- `use_nodriver` (bool): Указывает, использовать ли "nodriver" для авторизации. Всегда `True`.
- `parent` (str): Указывает на родительский класс `"Copilot"`.
- `default_model` (str): Модель по умолчанию для Copilot. Всегда `"Copilot"`.
- `default_vision_model` (str): Модель для работы с vision Copilot. Всегда `"Copilot"`.

### `cookies_to_dict`

**Описание**: Преобразует cookies в словарь.

```python
def cookies_to_dict():
    """Преобразует cookies в словарь.

    Returns:
        dict: Словарь, содержащий cookies.
    """
    ...
```

**Как работает функция**:

1.  Функция проверяет, является ли `Copilot._cookies` словарем.
2.  Если `Copilot._cookies` является словарем, он возвращается без изменений.
3.  Если `Copilot._cookies` является списком объектов cookies, то функция преобразует список в словарь, где ключами являются имена cookies, а значениями - их значения.

**Примеры**:

```python
# Пример, когда Copilot._cookies является списком cookies
Copilot._cookies = [Cookie(name='cookie1', value='value1'), Cookie(name='cookie2', value='value2')]
result = cookies_to_dict()
print(result)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2'}

# Пример, когда Copilot._cookies является словарем
Copilot._cookies = {'cookie1': 'value1', 'cookie2': 'value2'}
result = cookies_to_dict()
print(result)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2'}
```

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
    """Асинхронно обрабатывает процесс аутентификации.

    Args:
        proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AuthResult: Результат авторизации, содержащий токен API и cookies.
        RequestLogin: Объект, представляющий запрос на логин, если требуется интерактивная авторизация.

    Raises:
        NoValidHarFileError: Если не удается прочитать токен и cookies из HAR-файла и `has_nodriver` равен `False`.

        Exception: Если происходит какая-либо ошибка при чтении файла.
    """
    ...
```

**Назначение**: Асинхронно обрабатывает процесс аутентификации, получая токен доступа и cookies из HAR-файла или через веб-интерфейс.

**Параметры**:
- `cls` (type): Ссылка на класс `CopilotAccount`.
- `proxy` (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncIterator`: Асинхронный итератор, возвращающий `AuthResult` с токеном API и cookies или `RequestLogin`, если требуется интерактивная авторизация.

**Вызывает исключения**:
- `NoValidHarFileError`: Если не удается прочитать токен и cookies из HAR-файла и `has_nodriver` равен `False`.

**Как работает функция**:

1.  **Чтение из HAR-файла**: Пытается прочитать токен доступа и cookies из HAR-файла, используя `Copilot.readHAR(cls.url)`.
2.  **Обработка ошибки чтения HAR-файла**: Если возникает ошибка `NoValidHarFileError`:
    *   Логирует ошибку с использованием `debug.log(f"Copilot: {ex}")`.
    *   Проверяет, доступен ли "nodriver" (`has_nodriver`).
    *   Если "nodriver" доступен, создает объект `RequestLogin` и передаёт в `yield` для запроса URL для логина. Затем пытается получить токен доступа и cookies с использованием `get_access_token_and_cookies(cls.url, proxy)`.
    *   Если "nodriver" не доступен, вызывает исключение `h`.
3.  **Возврат результата авторизации**: Передаёт в `yield` объект `AuthResult`, содержащий токен API и cookies (преобразованные в словарь с помощью `cookies_to_dict()`).

**Примеры**:

```python
# Пример успешной аутентификации с использованием HAR-файла
async for result in CopilotAccount.on_auth_async():
    if isinstance(result, AuthResult):
        print(f"Токен API: {result.api_key}")
        print(f"Cookies: {result.cookies}")
        break

# Пример запроса на логин через веб-интерфейс
async for result in CopilotAccount.on_auth_async():
    if isinstance(result, RequestLogin):
        print(f"Требуется логин по адресу: {result.url}")
        break
```

```
AuthProcess
│
├─── Чтение токена и cookies из HAR-файла (Copilot.readHAR(cls.url))
│   │
│   ├─── Успешно:
│   │   │
│   │   └─── Возврат AuthResult с токеном и cookies
│   │
│   └─── Ошибка (NoValidHarFileError):
│       │
│       ├─── Логирование ошибки (debug.log)
│       │
│       ├─── Проверка has_nodriver
│       │   │
│       │   ├─── True:
│       │   │   │
│       │   │   ├─── Возврат RequestLogin с URL для логина
│       │   │   │
│       │   │   └─── Получение токена и cookies через веб-интерфейс (get_access_token_and_cookies)
│       │   │
│       │   └─── False:
│       │       │
│       │       └─── Вызов исключения h
│       │
│       └─── Конец обработки ошибки
│
└─── Конец AuthProcess
```

### `create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    **kwargs
) -> AsyncResult:
    """Создает аутентифицированный запрос к Copilot.

    Args:
        cls (type): Ссылка на класс.
        model (str): Название модели для запроса.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат авторизации, содержащий токен API и cookies.
        **kwargs: Дополнительные аргументы для запроса.

    Yields:
        str: Части ответа от Copilot.

    """
    ...
```

**Назначение**: Создает аутентифицированный запрос к Copilot, используя предоставленные учетные данные.

**Параметры**:
- `cls` (type): Ссылка на класс `CopilotAccount`.
- `model` (str): Название модели для запроса.
- `messages` (Messages): Список сообщений для отправки.
- `auth_result` (AuthResult): Результат авторизации, содержащий токен API и cookies.
- `**kwargs`: Дополнительные аргументы для запроса.

**Возвращает**:
- `AsyncResult`: Асинхронный итератор, возвращающий части ответа от Copilot.

**Как работает функция**:

1.  **Установка учетных данных**: Устанавливает токен доступа и cookies из `auth_result` в статические атрибуты класса `Copilot`.
2.  **Установка флага авторизации**: Устанавливает `Copilot.needs_auth` в значение `cls.needs_auth`.
3.  **Создание запроса**: Вызывает `Copilot.create_completion` для создания запроса к Copilot, передавая модель, сообщения и дополнительные аргументы.
4.  **Получение ответа**: Итерирует по частям ответа, возвращаемым `Copilot.create_completion`, и передаёт каждую часть в `yield`.
5.  **Обновление cookies**: Обновляет cookies в `auth_result` после получения ответа.

**Примеры**:

```python
# Пример создания аутентифицированного запроса к Copilot
auth_result = AuthResult(api_key="test_token", cookies={"cookie1": "value1"})
messages = [{"role": "user", "content": "Hello, Copilot!"}]

async for chunk in CopilotAccount.create_authed(model="default", messages=messages, auth_result=auth_result):
    print(chunk, end="")
```

```
CreateAuthedProcess
│
├─── Установка токена и cookies (Copilot._access_token, Copilot._cookies)
│   │
│   └─── Установка флага авторизации (Copilot.needs_auth)
│       │
│       └─── Создание запроса (Copilot.create_completion)
│           │
│           └─── Получение и передача частей ответа
│               │
│               └─── Обновление cookies (auth_result.cookies)
│
└─── Конец CreateAuthedProcess