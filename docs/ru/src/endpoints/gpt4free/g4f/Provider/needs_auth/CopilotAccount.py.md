# Модуль CopilotAccount

## Обзор

Модуль `CopilotAccount` предоставляет класс `CopilotAccount`, который используется для аутентификации и взаимодействия с Copilot API. Он наследуется от `AsyncAuthedProvider` и `Copilot`, обеспечивая асинхронную аутентификацию и функциональность для создания запросов к API.

## Подробнее

Этот модуль предназначен для упрощения процесса аутентификации и выполнения запросов к Copilot API. Он использует HAR-файлы для получения токенов доступа и cookies, а также предоставляет возможность автоматической аутентификации через веб-драйвер, если HAR-файл недействителен. Класс `CopilotAccount` позволяет создавать запросы к API Copilot с использованием полученных учетных данных.

## Классы

### `CopilotAccount`

**Описание**: Класс `CopilotAccount` предоставляет механизм для аутентификации и взаимодействия с API Copilot. Он наследуется от `AsyncAuthedProvider` и `Copilot`.

**Наследует**:

- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `Copilot`: Предоставляет методы для взаимодействия с API Copilot.

**Атрибуты**:

- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования этого провайдера. Значение `True`.
- `use_nodriver` (bool): Указывает, следует ли использовать безголовый браузер для аутентификации. Значение `True`.
- `parent` (str): Имя родительского класса. Значение `"Copilot"`.
- `default_model` (str): Модель, используемая по умолчанию. Значение `"Copilot"`.
- `default_vision_model` (str): Модель для работы с изображениями, используемая по умолчанию. Значение совпадает с `default_model`.

**Методы**:

- `on_auth_async`: Асинхронно обрабатывает аутентификацию.
- `create_authed`: Создает аутентифицированный запрос к API Copilot.

## Функции

### `cookies_to_dict`

```python
def cookies_to_dict():
    """Функция преобразует cookies в словарь.

    Returns:
        dict: Словарь, содержащий cookies, где ключами являются имена cookies, а значениями - их значения.
    """
    ...
```

**Назначение**: Преобразование cookies из формата `SimpleCookie` или списка объектов `Cookie` в словарь.

**Возвращает**:

- `dict`: Словарь, где ключи - имена файлов cookie, а значения - их значения.

**Как работает функция**:

1.  **Проверка типа `Copilot._cookies`**: Функция проверяет, является ли `Copilot._cookies` экземпляром словаря (`dict`).
2.  **Преобразование в словарь**: Если `Copilot._cookies` является списком или другим итерируемым объектом, функция преобразует его в словарь, используя имена файлов cookie в качестве ключей и их значения в качестве значений.

**Примеры**:

```python
# Пример, если Copilot._cookies - это список объектов Cookie
Copilot._cookies = [Cookie(name='cookie1', value='value1'), Cookie(name='cookie2', value='value2')]
cookies_dict = cookies_to_dict()
print(cookies_dict)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2'}

# Пример, если Copilot._cookies - это словарь
Copilot._cookies = {'cookie1': 'value1', 'cookie2': 'value2'}
cookies_dict = cookies_to_dict()
print(cookies_dict)  # Вывод: {'cookie1': 'value1', 'cookie2': 'value2'}
```

---

### `CopilotAccount.on_auth_async`

```python
@classmethod
async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
    """Асинхронно обрабатывает аутентификацию.

    Args:
        proxy (str, optional): Прокси-сервер для использования при аутентификации. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AuthResult: Результат аутентификации, содержащий токен API и cookies.

    Raises:
        NoValidHarFileError: Если не удается прочитать HAR-файл.
        Exception: Если возникает ошибка при получении токена доступа и cookies.
    """
    ...
```

**Назначение**: Асинхронная аутентификация для получения токена доступа и cookies.

**Параметры**:

- `proxy` (str, optional): Прокси-сервер для использования при аутентификации. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncIterator[AuthResult]`: Асинхронный итератор, возвращающий объект `AuthResult` с токеном API и cookies.

**Вызывает исключения**:

- `NoValidHarFileError`: Если не удается прочитать HAR-файл.
- `Exception`: Если возникает ошибка при получении токена доступа и cookies.

**Как работает функция**:

1.  **Чтение HAR-файла**: Функция пытается прочитать HAR-файл, чтобы получить токен доступа и cookies.
2.  **Обработка ошибки чтения HAR-файла**: Если HAR-файл недействителен, функция проверяет, доступен ли веб-драйвер.
3.  **Автоматическая аутентификация через веб-драйвер**: Если веб-драйвер доступен, функция запрашивает URL для входа и получает токен доступа и cookies с помощью веб-драйвера.
4.  **Возврат результата аутентификации**: Функция возвращает объект `AuthResult`, содержащий токен API и cookies.

```
A [Чтение HAR-файла]
|
B [Проверка на NoValidHarFileError]
|
C [Проверка доступности веб-драйвера]
|
D [Запрос URL для входа через веб-драйвер]
|
E [Получение токена и cookies]
|
F [Возврат AuthResult]
```

**Примеры**:

```python
# Пример использования с прокси
async for result in CopilotAccount.on_auth_async(proxy='http://proxy.example.com'):
    print(result.api_key)
    print(result.cookies)

# Пример использования без прокси
async for result in CopilotAccount.on_auth_async():
    print(result.api_key)
    print(result.cookies)
```

---

### `CopilotAccount.create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    **kwargs
) -> AsyncResult:
    """Создает аутентифицированный запрос к API Copilot.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        auth_result (AuthResult): Объект AuthResult, содержащий токен API и cookies.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Части ответа от API Copilot.

    """
    ...
```

**Назначение**: Создание аутентифицированного запроса к API Copilot с использованием предоставленных учетных данных.

**Параметры**:

- `model` (str): Имя используемой модели.
- `messages` (Messages): Список сообщений для отправки в API.
- `auth_result` (AuthResult): Объект `AuthResult`, содержащий токен API и cookies.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncResult`: Асинхронный итератор, возвращающий части ответа от API Copilot.

**Как работает функция**:

1.  **Установка токена доступа и cookies**: Функция устанавливает токен доступа и cookies из объекта `AuthResult` в класс `Copilot`.
2.  **Создание запроса к API**: Функция вызывает метод `create_completion` класса `Copilot` для создания запроса к API с использованием предоставленных параметров.
3.  **Возврат результата**: Функция возвращает асинхронный итератор, возвращающий части ответа от API.

```
A [Установка токена и cookies из auth_result]
|
B [Вызов Copilot.create_completion]
|
C [Возврат результата]
```

**Примеры**:

```python
# Пример использования
auth_result = AuthResult(api_key='test_token', cookies={'cookie1': 'value1'})
async for chunk in CopilotAccount.create_authed(model='default', messages=[{'role': 'user', 'content': 'Hello'}], auth_result=auth_result):
    print(chunk)