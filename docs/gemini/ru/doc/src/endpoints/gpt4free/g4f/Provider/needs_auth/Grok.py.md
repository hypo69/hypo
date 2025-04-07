# Модуль Grok.py для взаимодействия с Grok AI
## Обзор

Модуль `Grok.py` предназначен для обеспечения взаимодействия с Grok AI через API, требующее аутентификации. Он включает в себя функциональность для аутентификации, создания запросов и обработки ответов от Grok AI, включая текстовые и графические данные.
Модуль содержит класс `Grok`, который реализует асинхронное взаимодействие с Grok AI.

## Подробней

Модуль `Grok` предоставляет асинхронные методы для аутентификации и создания запросов к Grok AI. Он поддерживает как текстовые, так и графические ответы.

## Классы

### `Conversation`
**Описание**: Класс для представления идентификатора разговора с Grok AI.
**Принцип работы**:
Содержит только идентификатор разговора `conversation_id`.
#### **Аттрибуты**:
- `conversation_id` (str): Идентификатор разговора.

### `Grok`
**Описание**: Класс для взаимодействия с Grok AI, требующий аутентификации.

**Принцип работы**:
Предоставляет методы для аутентификации, подготовки запросов и обработки ответов от Grok AI.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `ProviderModelMixin`: Добавляет функциональность выбора модели.

#### **Аттрибуты**:
- `label` (str): Метка провайдера ("Grok AI").
- `url` (str): URL Grok AI ("https://grok.com").
- `cookie_domain` (str): Домен для cookie (".grok.com").
- `assets_url` (str): URL для статических ресурсов ("https://assets.grok.com").
- `conversation_url` (str): URL для управления разговорами ("https://grok.com/rest/app-chat/conversations").
- `needs_auth` (bool): Требуется ли аутентификация (True).
- `working` (bool): Указывает, что провайдер работает (True).
- `default_model` (str): Модель по умолчанию ("grok-3").
- `models` (List[str]): Список поддерживаемых моделей (["grok-3", "grok-3-thinking", "grok-2"]).
- `model_aliases` (Dict[str, str]): Псевдонимы моделей ({"grok-3-r1": "grok-3-thinking"}).

#### **Методы**:
- `on_auth_async`: Асинхронный метод для аутентификации.
- `_prepare_payload`: Асинхронный метод для подготовки полезной нагрузки запроса.
- `create_authed`: Асинхронный метод для создания аутентифицированного запроса.

## Методы

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Асинхронно аутентифицируется в Grok AI, используя предоставленные cookies или логин через URL.

    Args:
        cookies (Cookies, optional): Cookie для аутентификации. Defaults to None.
        proxy (str, optional): Прокси-сервер для использования. Defaults to None.

    Yields:
        AsyncIterator: Объект AuthResult с данными аутентификации или RequestLogin для запроса URL логина.
    """
```

**Назначение**:
Асинхронный метод выполняет аутентификацию в Grok AI. Он проверяет наличие cookies и, если они действительны, использует их для аутентификации. Если cookies отсутствуют или недействительны, запрашивает URL для логина.

**Параметры**:
- `cookies` (Cookies, optional): Cookie для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncIterator`: Асинхронный итератор, возвращающий объект `AuthResult` с данными аутентификации или `RequestLogin` для запроса URL логина.

**Как работает функция**:

1. **Проверка Cookies**: Сначала функция пытается получить cookies из указанного домена (`cls.cookie_domain`).
2. **Аутентификация с Cookies**: Если cookies найдены и содержат ключ `"sso"`, функция возвращает объект `AuthResult` с этими cookies, указывая на успешную аутентификацию.
3. **Запрос URL для логина**: Если cookies отсутствуют или не содержат необходимый ключ, функция возвращает объект `RequestLogin`, который запрашивает URL для логина.
4. **Завершение аутентификации**: После выполнения логина через URL, функция получает cookies и возвращает объект `AuthResult` с новыми cookies.

```
Проверка Cookies --> Cookies найдены и содержат "sso"?
|                                        |
Да                                       Нет
|                                        |
Возврат AuthResult с Cookies           Запрос URL для логина (RequestLogin)
|                                        |
Конец                                    Получение Cookies после логина
                                         |
                                         Возврат AuthResult с новыми Cookies
                                         |
                                         Конец
```

**Примеры**:

Пример использования с cookies:
```python
cookies = {"sso": "some_sso_token"}
async for result in Grok.on_auth_async(cookies=cookies):
    print(result)
```

Пример использования без cookies (требуется логин через URL):

```python
async for result in Grok.on_auth_async():
    print(result)
```

### `_prepare_payload`

```python
@classmethod
async def _prepare_payload(cls, model: str, message: str) -> Dict[str, Any]:
    """
    Подготавливает полезную нагрузку (payload) для запроса к Grok AI.

    Args:
        model (str): Используемая модель Grok AI.
        message (str): Сообщение для отправки в Grok AI.

    Returns:
        Dict[str, Any]: Словарь с подготовленной полезной нагрузкой.
    """
```

**Назначение**:
Асинхронный метод подготавливает полезную нагрузку (payload) для запроса к Grok AI. Он формирует словарь с параметрами, необходимыми для запроса, включая модель, сообщение и другие настройки.

**Параметры**:
- `model` (str): Используемая модель Grok AI.
- `message` (str): Сообщение для отправки в Grok AI.

**Возвращает**:
- `Dict[str, Any]`: Словарь с подготовленной полезной нагрузкой.

**Как работает функция**:

1. **Определение модели**: Определяет, какую модель Grok AI использовать (grok-latest для grok-2 или grok-3 для остальных).
2. **Формирование словаря**: Создает словарь с параметрами запроса, такими как сообщение, модель, прикрепленные файлы и изображения, а также настройки для поиска, генерации изображений и других функций.

```
Определение модели --> Формирование словаря с параметрами запроса
|                                        |
Создание словаря с:                      Настройки для поиска и генерации изображений
- modelName                              |
- message                                Настройки для forceConcise и toolOverrides
|                                        |
Возврат словаря                           Определение isReasoning на основе модели
|                                        |
Конец
```

**Примеры**:

Пример использования:

```python
model = "grok-3"
message = "Hello, Grok AI!"
payload = await Grok._prepare_payload(model, message)
print(payload)
```

### `create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    cookies: Cookies = None,
    return_conversation: bool = False,
    conversation: Conversation = None,
    **kwargs
) -> AsyncResult:
    """
    Создает аутентифицированный запрос к Grok AI и обрабатывает ответ.

    Args:
        model (str): Используемая модель Grok AI.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат аутентификации.
        cookies (Cookies, optional): Cookie для аутентификации. Defaults to None.
        return_conversation (bool, optional): Возвращать ли объект Conversation. Defaults to False.
        conversation (Conversation, optional): Объект Conversation для продолжения разговора. Defaults to None.

    Yields:
        AsyncResult: Асинхронный итератор, возвращающий результаты обработки ответа от Grok AI (текст, изображения, заголовки).
    """
```

**Назначение**:
Асинхронный метод создаёт аутентифицированный запрос к Grok AI и обрабатывает полученные ответы. Он поддерживает как создание новых разговоров, так и продолжение существующих.

**Параметры**:
- `model` (str): Используемая модель Grok AI.
- `messages` (Messages): Список сообщений для отправки.
- `auth_result` (AuthResult): Результат аутентификации.
- `cookies` (Cookies, optional): Cookie для аутентификации. По умолчанию `None`.
- `return_conversation` (bool, optional): Возвращать ли объект `Conversation`. По умолчанию `False`.
- `conversation` (Conversation, optional): Объект `Conversation` для продолжения разговора. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный итератор, возвращающий результаты обработки ответа от Grok AI (текст, изображения, заголовок).

**Как работает функция**:

1. **Определение ID разговора**: Если передан объект `conversation`, извлекается его ID. Если нет, то `conversation_id = None`.
2. **Форматирование сообщения**: Если это новый разговор (`conversation_id is None`), форматируются все сообщения. Иначе берётся последнее сообщение пользователя.
3. **Создание сессии**: Создаётся асинхронная сессия с использованием данных аутентификации.
4. **Подготовка Payload**: Подготавливается полезная нагрузка с помощью метода `_prepare_payload`.
5. **Определение URL**: Определяется URL для отправки запроса (новый разговор или продолжение существующего).
6. **Отправка запроса**: Отправляется POST-запрос к Grok AI.
7. **Обработка ответа**: Обрабатывается каждая строка ответа, извлекая данные (текст, изображения, заголовок). Возвращаются объекты `ImagePreview`, `Reasoning`, `ImageResponse`, `TitleGeneration`.
8. **Возврат Conversation**: Если `return_conversation = True` и `conversation_id` существует, возвращается объект `Conversation`.

```
Определение ID разговора --> Форматирование сообщения
|                                        |
Создание сессии                         Подготовка Payload
|                                        |
Определение URL                         Отправка POST-запроса
|                                        |
Обработка ответа (текст, изображения, заголовок)
|                                        |
Возврат Conversation (если требуется)
|                                        |
Конец
```

**Примеры**:

Пример создания нового разговора:

```python
messages = [{"role": "user", "content": "Hello, Grok AI!"}]
auth_result = AuthResult(cookies={"sso": "some_sso_token"})
async for result in Grok.create_authed(model="grok-3", messages=messages, auth_result=auth_result, return_conversation=True):
    print(result)
```

Пример продолжения существующего разговора:

```python
conversation = Conversation(conversation_id="some_conversation_id")
messages = [{"role": "user", "content": "How are you?"}]
auth_result = AuthResult(cookies={"sso": "some_sso_token"})
async for result in Grok.create_authed(model="grok-3", messages=messages, auth_result=auth_result, conversation=conversation):
    print(result)