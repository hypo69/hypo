# Модуль для работы с Grok AI
==================================

Модуль содержит класс `Grok`, который используется для взаимодействия с AI-моделью Grok через API grok.com. Он предоставляет функциональность для аутентификации, создания бесед и получения ответов от модели.

## Обзор

Модуль `Grok` является асинхронным провайдером, предназначенным для интеграции с сервисом Grok AI. Он поддерживает аутентификацию с использованием cookie-файлов или через URL для входа, а также позволяет создавать и поддерживать беседы с моделью Grok.

## Подробнее

Этот модуль обеспечивает взаимодействие с Grok AI, позволяя отправлять запросы к модели и получать ответы. Он включает в себя механизмы для аутентификации, подготовки полезной нагрузки запроса и обработки потоковых ответов от сервера Grok. Расположение файла в проекте указывает на его роль как одного из провайдеров для g4f (gpt4free), что подразумевает его использование для предоставления доступа к модели Grok через этот проект.

## Классы

### `Conversation`

**Описание**: Класс для представления идентификатора беседы.

**Атрибуты**:
- `conversation_id` (str): Уникальный идентификатор беседы.

### `Grok`

**Описание**: Класс, представляющий провайдера Grok AI.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера ("Grok AI").
- `url` (str): URL сервиса Grok ("https://grok.com").
- `cookie_domain` (str): Домен для cookie-файлов (".grok.com").
- `assets_url` (str): URL для статических ресурсов ("https://assets.grok.com").
- `conversation_url` (str): URL для управления беседами ("https://grok.com/rest/app-chat/conversations").
- `needs_auth` (bool): Указывает, требуется ли аутентификация (True).
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ("grok-3").
- `models` (List[str]): Список поддерживаемых моделей (["grok-3", "grok-3-thinking", "grok-2"]).
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей ({"grok-3-r1": "grok-3-thinking"}).

**Методы**:

- `on_auth_async(cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator`: Асинхронный метод для аутентификации пользователя.
- `_prepare_payload(model: str, message: str) -> Dict[str, Any]`: Асинхронный метод для подготовки полезной нагрузки запроса.
- `create_authed(model: str, messages: Messages, auth_result: AuthResult, cookies: Cookies = None, return_conversation: bool = False, conversation: Conversation = None, **kwargs) -> AsyncResult`: Асинхронный метод для создания аутентифицированного запроса и получения ответа от модели.

## Функции

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
    """
    Асинхронно аутентифицирует пользователя, используя либо существующие cookie, либо URL для входа.

    Args:
        cookies (Cookies, optional): Cookie-файлы для аутентификации. По умолчанию None.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Yields:
        AuthResult: Результат аутентификации, содержащий cookie, заголовки и прокси.
        RequestLogin: Объект запроса на вход, если требуются учетные данные.

    Как работает функция:
    1. Проверяет наличие переданных cookie.
    2. Если cookie отсутствуют, пытается получить их из домена .grok.com.
    3. Если cookie найдены и содержат "sso", возвращает результат аутентификации с cookie.
    4. Если cookie не содержат "sso", запрашивает URL для входа из переменной окружения G4F_LOGIN_URL или пустой строки.
    5. Возвращает результат аутентификации, полученный с использованием аргументов из nodriver.

    A. Проверка cookie
    |
    B. Получение cookie из домена .grok.com
    |
    C. Проверка наличия "sso" в cookie
    |
    D. Возврат результата аутентификации или запроса на вход

    Примеры:
    1. Аутентификация с использованием существующих cookie:
       ```python
       async for result in Grok.on_auth_async(cookies={"sso": "some_sso_token"}):
           print(result)
       ```

    2. Запрос URL для входа:
       ```python
       async for result in Grok.on_auth_async():
           print(result)
       ```
    """
    ...
```

### `_prepare_payload`

```python
@classmethod
async def _prepare_payload(cls, model: str, message: str) -> Dict[str, Any]:
    """
    Подготавливает полезную нагрузку (payload) для запроса к API Grok.

    Args:
        model (str): Название используемой модели Grok.
        message (str): Текст сообщения для отправки.

    Returns:
        Dict[str, Any]: Словарь, содержащий полезную нагрузку для запроса.

    Как работает функция:
    1. Определяет, какую модель использовать ("grok-latest" для "grok-2", "grok-3" в остальных случаях).
    2. Формирует словарь с параметрами запроса, такими как текст сообщения, вложения файлов и изображений, а также настройки генерации изображений и поиска.
    3. Возвращает сформированный словарь.

    A. Определение модели
    |
    B. Формирование словаря с параметрами запроса
    |
    C. Возврат сформированного словаря

    Примеры:
    1. Подготовка payload для модели "grok-3":
       ```python
       payload = await Grok._prepare_payload("grok-3", "Hello, Grok!")
       print(payload)
       ```

    2. Подготовка payload для модели "grok-2":
       ```python
       payload = await Grok._prepare_payload("grok-2", "Tell me a joke.")
       print(payload)
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
    cookies: Cookies = None,
    return_conversation: bool = False,
    conversation: Conversation = None,
    **kwargs
) -> AsyncResult:
    """
    Создает аутентифицированный запрос к API Grok и обрабатывает потоковый ответ.

    Args:
        model (str): Название используемой модели Grok.
        messages (Messages): Список сообщений для отправки.
        auth_result (AuthResult): Результат аутентификации, содержащий cookie и заголовки.
        cookies (Cookies, optional): Cookie-файлы для запроса. По умолчанию None.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект беседы. По умолчанию False.
        conversation (Conversation, optional): Объект беседы, если беседа уже существует. По умолчанию None.
        **kwargs: Дополнительные аргументы.

    Yields:
        ImagePreview: Превью сгенерированного изображения.
        Reasoning: Промежуточные результаты размышлений модели.
        str: Текст ответа от модели.
        ImageResponse: Сгенерированные изображения.
        TitleGeneration: Сгенерированный заголовок беседы.
        Conversation: Объект беседы, если `return_conversation` равен True.

    Как работает функция:
    1. Определяет идентификатор беседы (conversation_id), если беседа уже существует.
    2. Форматирует сообщение (prompt) для отправки, используя либо весь список сообщений для новой беседы, либо последнее сообщение пользователя для продолжения существующей.
    3. Создает сессию StreamSession с использованием данных аутентификации.
    4. Подготавливает полезную нагрузку для запроса с использованием метода `_prepare_payload`.
    5. Отправляет POST-запрос на URL создания новой беседы или добавления ответа в существующую беседу.
    6. Обрабатывает потоковый ответ от сервера, извлекая из JSON-строк различные типы данных: превью изображений, промежуточные размышления модели, текст ответа, сгенерированные изображения и заголовок беседы.
    7. Возвращает объекты ImagePreview, Reasoning, текст ответа, ImageResponse и TitleGeneration по мере их получения из потока.
    8. Если `return_conversation` равен True, возвращает объект Conversation с идентификатором беседы.

    A. Определение conversation_id
    |
    B. Форматирование сообщения (prompt)
    |
    C. Создание сессии StreamSession
    |
    D. Подготовка полезной нагрузки (payload)
    |
    E. Отправка POST-запроса
    |
    F. Обработка потокового ответа

    Примеры:
    1. Создание новой беседы:
       ```python
       auth_result = AuthResult(cookies={"sso": "some_sso_token"}, headers={})
       async for result in Grok.create_authed("grok-3", [{"role": "user", "content": "Hello, Grok!"}], auth_result, return_conversation=True):
           print(result)
       ```

    2. Продолжение существующей беседы:
       ```python
       auth_result = AuthResult(cookies={"sso": "some_sso_token"}, headers={})
       conversation = Conversation(conversation_id="some_conversation_id")
       async for result in Grok.create_authed("grok-3", [{"role": "user", "content": "Tell me more."}], auth_result, conversation=conversation):
           print(result)
       ```
    """
    ...