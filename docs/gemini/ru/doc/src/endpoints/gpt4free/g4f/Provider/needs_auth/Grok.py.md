# Модуль Grok

## Обзор

Модуль `Grok` предназначен для взаимодействия с Grok AI, предоставляя функциональность для аутентификации, создания бесед и получения ответов от модели. Он включает в себя классы `Conversation` и `Grok`, а также методы для подготовки полезной нагрузки и обработки ответов от API Grok AI.

## Подробней

Модуль `Grok` является частью проекта `hypotez` и обеспечивает интеграцию с платформой Grok AI. Он позволяет пользователям аутентифицироваться, начинать новые беседы и получать ответы от моделей Grok AI. Модуль включает в себя классы `Conversation` для представления беседы и `Grok` для взаимодействия с API Grok AI.

## Классы

### `Conversation`

**Описание**: Представляет собой класс для хранения информации о беседе.

**Аттрибуты**:
- `conversation_id` (str): Идентификатор беседы.

```python
class Conversation(JsonConversation):
    """
    Args:
        conversation_id (str): Идентификатор беседы.
    """
    def __init__(self, conversation_id: str) -> None:
        """
        Args:
            conversation_id (str): Идентификатор беседы.
        """
        ...
```

### `Grok`

**Описание**: Класс для взаимодействия с Grok AI.

**Наследует**:
- `AsyncAuthedProvider`: Обеспечивает асинхронную аутентификацию.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Grok AI").
- `url` (str): URL Grok AI ("https://grok.com").
- `cookie_domain` (str): Домен для куки (".grok.com").
- `assets_url` (str): URL для ресурсов Grok AI ("https://assets.grok.com").
- `conversation_url` (str): URL для управления беседами ("https://grok.com/rest/app-chat/conversations").
- `needs_auth` (bool): Требуется ли аутентификация (True).
- `working` (bool): Указывает, работает ли провайдер (True).
- `default_model` (str): Модель по умолчанию ("grok-3").
- `models` (List[str]): Список поддерживаемых моделей (["grok-3", "grok-3-thinking", "grok-2"]).
- `model_aliases` (Dict[str, str]): Псевдонимы моделей ({"grok-3-r1": "grok-3-thinking"}).

**Методы**:
- `on_auth_async`: Асинхронно аутентифицирует пользователя.
- `_prepare_payload`: Подготавливает полезную нагрузку для запроса к API.
- `create_authed`: Создает аутентифицированный запрос и обрабатывает ответ.

## Функции

### `on_auth_async`

```python
    @classmethod
    async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
        """
        Асинхронно аутентифицирует пользователя, используя cookies или логин/пароль.

        Args:
            cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            AuthResult: Результат аутентификации с cookies, заголовками и прокси.
            RequestLogin: Запрос на ввод логина/пароля, если cookies отсутствуют.

        Пример использования:
            auth_result = Grok.on_auth_async(cookies={'sso': 'your_sso_cookie'})
        """
        ...
```

**Назначение**: Асинхронная аутентификация пользователя.

**Параметры**:
- `cls`: Ссылка на класс `Grok`.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncIterator`: Асинхронный итератор, возвращающий результаты аутентификации или запрос на ввод логина/пароля.

**Как работает функция**:
1. Проверяет наличие переданных `cookies`.
2. Если `cookies` содержат ключ "sso", возвращает `AuthResult` с информацией об аутентификации.
3. Если `cookies` отсутствуют, запрашивает логин/пароль через `RequestLogin`.
4. После успешной аутентификации возвращает `AuthResult` с обновленными `cookies` и заголовками.

```
A: Проверка наличия cookies
|
B: Cookies содержат "sso"?
|   \
|   No -> C
|   /
Yes
|
D: Возврат AuthResult с cookies
|
E: Запрос логина/пароля через RequestLogin
|
F: Получение аргументов из веб-драйвера
|
G: Возврат AuthResult с обновленными cookies
```

**Примеры**:
```python
# Пример использования с cookies
auth_result = Grok.on_auth_async(cookies={'sso': 'your_sso_cookie'})

# Пример использования без cookies (запрос логина/пароля)
auth_result = Grok.on_auth_async()
```

### `_prepare_payload`

```python
    @classmethod
    async def _prepare_payload(cls, model: str, message: str) -> Dict[str, Any]:
        """
        Подготавливает полезную нагрузку (payload) для запроса к API Grok AI.

        Args:
            model (str): Название используемой модели.
            message (str): Текст сообщения для отправки.

        Returns:
            Dict[str, Any]: Словарь с данными для отправки в запросе.

        Пример:
            payload = Grok._prepare_payload(model='grok-3', message='Hello, Grok!')
        """
        ...
```

**Назначение**: Подготовка полезной нагрузки для запроса к API Grok AI.

**Параметры**:
- `cls`: Ссылка на класс `Grok`.
- `model` (str): Название используемой модели.
- `message` (str): Текст сообщения для отправки.

**Возвращает**:
- `Dict[str, Any]`: Словарь с данными для отправки в запросе.

**Как работает функция**:
1. Определяет, какую версию модели использовать (grok-latest для "grok-2" или grok-3 для остальных).
2. Формирует словарь с параметрами, необходимыми для запроса к API Grok AI, такими как текст сообщения, вложения файлов и изображений, настройки поиска и генерации изображений.
3. Возвращает словарь с подготовленной полезной нагрузкой.

```
A: Определение версии модели
|
B: Формирование словаря с параметрами запроса
|
C: Возврат словаря с полезной нагрузкой
```

**Примеры**:
```python
# Пример подготовки payload для модели grok-3
payload = Grok._prepare_payload(model='grok-3', message='Hello, Grok!')

# Пример подготовки payload для модели grok-2
payload = Grok._prepare_payload(model='grok-2', message='Hello, Grok!')
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
        Создает аутентифицированный запрос к API Grok AI и обрабатывает ответ.

        Args:
            cls: Ссылка на класс `Grok`.
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки.
            auth_result (AuthResult): Результат аутентификации.
            cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
            return_conversation (bool, optional): Возвращать ли объект беседы. По умолчанию `False`.
            conversation (Conversation, optional): Объект беседы (если есть). По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            ImagePreview: Предварительный просмотр сгенерированного изображения.
            Reasoning: Промежуточные результаты размышлений модели.
            token: Текст ответа модели.
            ImageResponse: Сгенерированные изображения.
            TitleGeneration: Сгенерированный заголовок беседы.
            Conversation: Объект беседы (если `return_conversation` is True).

        Пример:
            async for result in Grok.create_authed(model='grok-3', messages=[{'role': 'user', 'content': 'Hello!'}], auth_result=auth_result):
                print(result)
        """
        ...
```

**Назначение**: Создание аутентифицированного запроса к API Grok AI и обработка ответа.

**Параметры**:
- `cls`: Ссылка на класс `Grok`.
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки.
- `auth_result` (AuthResult): Результат аутентификации.
- `cookies` (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
- `return_conversation` (bool, optional): Возвращать ли объект беседы. По умолчанию `False`.
- `conversation` (Conversation, optional): Объект беседы (если есть). По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный итератор, возвращающий различные типы ответов от API Grok AI, такие как предварительный просмотр изображений, промежуточные результаты размышлений, текст ответа, сгенерированные изображения и заголовок беседы.

**Как работает функция**:
1. Определяет идентификатор беседы (conversation_id), если он существует.
2. Форматирует запрос в зависимости от наличия идентификатора беседы.
3. Подготавливает полезную нагрузку с помощью `_prepare_payload`.
4. Отправляет POST-запрос к API Grok AI.
5. Обрабатывает ответ построчно, извлекая данные о сгенерированных изображениях, промежуточных результатах размышлений, тексте ответа и заголовке беседы.
6. Возвращает результаты в виде асинхронного итератора.

```
A: Определение идентификатора беседы
|
B: Форматирование запроса
|
C: Подготовка полезной нагрузки
|
D: Отправка POST-запроса к API
|
E: Обработка ответа построчно
|
F: Извлечение данных (изображения, размышления, текст, заголовок)
|
G: Возврат результатов в виде асинхронного итератора
```

**Примеры**:
```python
# Пример создания запроса с новой беседой
async for result in Grok.create_authed(model='grok-3', messages=[{'role': 'user', 'content': 'Hello!'}], auth_result=auth_result):
    print(result)

# Пример создания запроса с существующей беседой
conversation = Conversation(conversation_id='your_conversation_id')
async for result in Grok.create_authed(model='grok-3', messages=[{'role': 'user', 'content': 'How are you?'}], auth_result=auth_result, conversation=conversation):
    print(result)