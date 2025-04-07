# Модуль для аутентификации в Copilot с использованием аккаунта
=============================================================

Модуль содержит класс `CopilotAccount`, который является подклассом `AsyncAuthedProvider` и `Copilot`. 
Он предоставляет функциональность для аутентификации в Copilot с использованием HAR-файла или через веб-интерфейс.

## Обзор

Этот модуль предназначен для автоматической аутентификации в сервисе Copilot. Он использует HAR-файлы для получения токена доступа и cookies, либо, если HAR-файл недействителен или отсутствует, пытается получить их через веб-интерфейс, используя драйвер браузера. Модуль обеспечивает асинхронную аутентификацию и предоставляет методы для создания аутентифицированных запросов.

## Подробней

Модуль `CopilotAccount` позволяет аутентифицироваться в Copilot, используя либо HAR-файл (HTTP Archive), содержащий необходимые данные для аутентификации, либо, если HAR-файл не найден или не содержит нужной информации, модуль пытается получить `access_token` и `cookies` через веб-интерфейс. Для этого используется `nodriver`, который позволяет автоматизировать процесс в браузере.

## Классы

### `CopilotAccount`

**Описание**: Класс `CopilotAccount` предоставляет функциональность для аутентификации в Copilot с использованием аккаунта.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `Copilot`: Предоставляет методы для взаимодействия с Copilot API.

**Атрибуты**:
- `needs_auth (bool)`: Указывает, требуется ли аутентификация (всегда `True`).
- `use_nodriver (bool)`: Указывает, использовать ли `nodriver` для аутентификации (всегда `True`).
- `parent (str)`: Указывает родительский класс (всегда `"Copilot"`).
- `default_model (str)`: Модель, используемая по умолчанию (всегда `"Copilot"`).
- `default_vision_model (str)`: Модель для работы с изображениями по умолчанию (всегда `default_model`).

### `CopilotAccount.on_auth_async`

```python
    @classmethod
    async def on_auth_async(cls, proxy: str = None, **kwargs) -> AsyncIterator:
        """Асинхронно аутентифицируется в Copilot, используя HAR-файл или веб-интерфейс.

        Args:
            proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Yields:
            AuthResult: Результат аутентификации, содержащий `api_key` и `cookies`.
            RequestLogin: Если требуется логин через веб-интерфейс, возвращает запрос на логин.

        Raises:
            NoValidHarFileError: Если не удается прочитать HAR-файл и `has_nodriver` равно `False`.

        Как работает функция:
        1. Пытается прочитать `access_token` и `cookies` из HAR-файла.
        2. Если HAR-файл недействителен, проверяет наличие `nodriver`.
        3. Если `nodriver` доступен, запрашивает логин через веб-интерфейс и получает `access_token` и `cookies`.
        4. Если `nodriver` недоступен, выбрасывает исключение `NoValidHarFileError`.
        5. Возвращает результат аутентификации с `api_key` и `cookies`.

        Внутренние функции:
            cookies_to_dict(): Преобразует cookies в словарь.

        ASCII flowchart:
        Начало --> Чтение HAR-файла
        Чтение HAR-файла --(Ошибка)--> Проверка наличия nodriver
        Проверка наличия nodriver --(Есть nodriver)--> Запрос логина через веб-интерфейс
        Запрос логина через веб-интерфейс --> Получение access_token и cookies
        Проверка наличия nodriver --(Нет nodriver)--> Выброс NoValidHarFileError
        Получение access_token и cookies --> Возврат AuthResult
        Выброс NoValidHarFileError --> Конец

        Примеры:
            >>> async for result in CopilotAccount.on_auth_async():
            ...     if isinstance(result, AuthResult):
            ...         print(f"API Key: {result.api_key}")
            ...         print(f"Cookies: {result.cookies}")
        """
        try:
            Copilot._access_token, Copilot._cookies = readHAR(cls.url)
        except NoValidHarFileError as h:
            debug.log(f"Copilot: {h}")
            if has_nodriver:
                yield RequestLogin(cls.label, os.environ.get("G4F_LOGIN_URL", ""))
                Copilot._access_token, Copilot._cookies = await get_access_token_and_cookies(cls.url, proxy)
            else:
                raise h
        yield AuthResult(
            api_key=Copilot._access_token,
            cookies=cookies_to_dict()
        )
```

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
        """Создает аутентифицированный запрос к Copilot.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            auth_result (AuthResult): Результат аутентификации, содержащий `api_key` и `cookies`.
            **kwargs: Дополнительные параметры для передачи в `Copilot.create_completion`.

        Yields:
            str: Части ответа от Copilot.

        Как работает функция:
        1. Устанавливает `access_token` и `cookies` из `auth_result` в статические переменные класса `Copilot`.
        2. Вызывает `Copilot.create_completion` для создания запроса к Copilot API.
        3. Возвращает части ответа от Copilot.

        ASCII flowchart:

        Начало --> Установка access_token и cookies
        Установка access_token и cookies --> Вызов Copilot.create_completion
        Вызов Copilot.create_completion --> Возврат частей ответа
        Возврат частей ответа --> Конец

        Примеры:
            >>> auth_result = AuthResult(api_key="test_key", cookies={"test": "test"})
            >>> async for chunk in CopilotAccount.create_authed("Copilot", [], auth_result):
            ...     print(chunk)
        """
        Copilot._access_token = getattr(auth_result, "api_key")
        Copilot._cookies = getattr(auth_result, "cookies")
        Copilot.needs_auth = cls.needs_auth
        for chunk in Copilot.create_completion(model, messages, **kwargs):
            yield chunk
        auth_result.cookies = cookies_to_dict()
```

## Функции

### `cookies_to_dict`

```python
def cookies_to_dict():
    """Преобразует cookies в словарь.

    Returns:
        dict: Словарь, содержащий cookies, где ключи - имена cookies, значения - их значения.
        
    Как работает функция:
    1. Проверяет, являются ли `Copilot._cookies` словарем.
    2. Если нет, преобразует список cookies в словарь.

    ASCII flowchart:
        Начало --> Проверка типа Copilot._cookies
        Проверка типа Copilot._cookies --(Словарь)--> Возврат Copilot._cookies
        Проверка типа Copilot._cookies --(Не словарь)--> Преобразование в словарь
        Преобразование в словарь --> Возврат словаря
        Конец

    Примеры:
        >>> Copilot._cookies = [{"name": "test", "value": "test_value"}]
        >>> cookies_to_dict()
        {'test': 'test_value'}
    """
    return Copilot._cookies if isinstance(Copilot._cookies, dict) else {c.name: c.value for c in Copilot._cookies}