# Модуль `CopilotAccount.py`

## Обзор

Модуль `CopilotAccount.py` является частью проекта `hypotez` и предназначен для организации взаимодействия с Copilot через аккаунт. Он предоставляет асинхронный интерфейс для аутентификации и выполнения запросов к Copilot, используя либо HAR-файлы, либо автоматическое получение токена доступа и cookies.

## Подробнее

Модуль `CopilotAccount` наследует функциональность от `AsyncAuthedProvider` и `Copilot`. Он предназначен для обработки аутентификации и создания сессий с использованием Copilot. Класс использует HAR-файлы для хранения данных аутентификации или, если HAR-файл отсутствует или недействителен, пытается получить токен доступа и cookies автоматически через веб-драйвер (если доступен) или запрашивает URL для логина. Этот модуль важен для интеграции с Copilot, требующей аутентификации, и обеспечивает удобный способ управления сессиями.

## Классы

### `CopilotAccount`

**Описание**: Класс `CopilotAccount` предоставляет асинхронный интерфейс для аутентификации и взаимодействия с Copilot.

**Наследует**:
- `AsyncAuthedProvider`: Предоставляет базовую функциональность для асинхронных провайдеров, требующих аутентификации.
- `Copilot`: Предоставляет методы для взаимодействия с API Copilot.

**Атрибуты**:
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования этого провайдера. Всегда `True`.
- `use_nodriver` (bool): Указывает, следует ли использовать безголовый режим драйвера. Всегда `True`.
- `parent` (str): Указывает родительский класс. Всегда `"Copilot"`.
- `default_model` (str): Модель, используемая по умолчанию. Всегда `"Copilot"`.
- `default_vision_model` (str): Модель для обработки изображений, используемая по умолчанию. Всегда совпадает с `default_model`.

**Методы**:
- `on_auth_async`: Асинхронный метод для аутентификации.
- `create_authed`: Асинхронный метод для создания аутентифицированной сессии и выполнения запросов.

## Функции

### `cookies_to_dict`

```python
def cookies_to_dict() -> dict:
    """
    Преобразует cookies в словарь.

    Args:
        Нет

    Returns:
        dict: Словарь, содержащий cookies, где ключом является имя cookie, а значением - значение cookie.

    Как работает функция:
    1. Проверяет, является ли атрибут `Copilot._cookies` словарем.
    2. Если да, возвращает его без изменений.
    3. Если нет (например, это список объектов cookie), преобразует список в словарь, где ключами являются имена cookie, а значениями - их значения.

    ASCII flowchart:
    Проверка типа Copilot._cookies --> Преобразование в словарь --> Возврат словаря

    Примеры:
    Предположим, что `Copilot._cookies` - это список объектов cookie:
    >>> Copilot._cookies = [Cookie(name='test', value='test_value')]
    >>> cookies_to_dict()
    {'test': 'test_value'}
    """
    ...
```

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Асинхронно выполняет аутентификацию, используя HAR-файл или получая токен и cookies.

    Args:
        cls (CopilotAccount): Класс `CopilotAccount`.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Yields:
        AuthResult: Результат аутентификации, содержащий токен API и cookies.
        RequestLogin: Запрос на ввод URL для логина, если HAR-файл не найден и используется безголовый драйвер.

    Raises:
        NoValidHarFileError: Если не удается прочитать HAR-файл и безголовый драйвер недоступен.

    Как работает функция:
    1. Пытается прочитать токен доступа и cookies из HAR-файла, используя `Copilot.readHAR(cls.url)`.
    2. Если `NoValidHarFileError` возникает:
        - Логирует ошибку, используя `debug.log`.
        - Если `has_nodriver` (безголовый драйвер доступен):
            - Отправляет запрос на ввод URL для логина, используя `yield RequestLogin`.
            - Пытается получить токен доступа и cookies, используя `get_access_token_and_cookies`.
        - Если `has_nodriver` недоступен, вызывает исключение `h`.
    3. Возвращает результат аутентификации с токеном API и cookies, используя `yield AuthResult`.

    ASCII flowchart:
    A. Попытка чтения из HAR --> B. Если ошибка --> C. Проверка наличия безголового драйвера --> D1. Запрос URL для логина (если драйвер есть)
    |NO                                       |YES
    D2. Генерация исключения (если драйвера нет)
    |
    E. Получение токена и cookies --> F. Возврат результата аутентификации
    Примеры:
    Предположим, что HAR-файл не найден, и доступен безголовый драйвер:
    ```python
    class MockCopilotAccount(CopilotAccount):
        url = 'http://example.com'
        label = 'MockCopilot'
    async for result in MockCopilotAccount.on_auth_async():
        print(result)
    ```
    """
    ...
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
    """
    Создает аутентифицированную сессию и выполняет запрос к Copilot.

    Args:
        cls (CopilotAccount): Класс `CopilotAccount`.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат аутентификации, содержащий токен API и cookies.
        **kwargs: Дополнительные аргументы для `Copilot.create_completion`.

    Yields:
        str: Части ответа от Copilot.

    Как работает функция:
    1. Извлекает токен доступа и cookies из `auth_result` и присваивает их `Copilot._access_token` и `Copilot._cookies` соответственно.
    2. Устанавливает `Copilot.needs_auth` в значение `cls.needs_auth`.
    3. Вызывает `Copilot.create_completion` с переданными аргументами и генерирует части ответа.
    4. Обновляет `auth_result.cookies` текущими cookies (преобразованными в словарь) после завершения запроса.

    ASCII flowchart:
    A. Извлечение токена и cookies --> B. Установка флага аутентификации --> C. Вызов Copilot.create_completion --> D. Обновление cookies в auth_result
    
    Примеры:
    ```python
    class MockCopilotAccount(CopilotAccount):
        url = 'http://example.com'
        label = 'MockCopilot'
    async for chunk in MockCopilotAccount.create_authed(model='default', messages=[{'role': 'user', 'content': 'Hello'}], auth_result=AuthResult(api_key='test_token', cookies={'test': 'test_value'})):
        print(chunk)
    ```
    """
    ...