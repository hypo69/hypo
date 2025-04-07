# Модуль для работы с GitHub Copilot
## Обзор

Модуль предоставляет класс `GithubCopilot` для взаимодействия с сервисом GitHub Copilot от имени пользователя.
Он поддерживает асинхронный стриминг ответов и требует аутентификации.

## Подробней

Этот модуль позволяет интегрировать функциональность GitHub Copilot в проект `hypotez`.
Он обеспечивает возможность создания диалогов с использованием различных моделей, поддерживаемых GitHub Copilot,
включая `gpt-4o`, `o1-mini`, `o1-preview` и `claude-3.5-sonnet`.

## Классы

### `Conversation`

**Описание**: Представляет собой класс для хранения информации о диалоге с GitHub Copilot.

**Атрибуты**:
- `conversation_id` (str): Идентификатор диалога.

**Методы**:
- `__init__(self, conversation_id: str)`: Конструктор класса, принимающий идентификатор диалога.

### `GithubCopilot`

**Описание**: Класс для взаимодействия с GitHub Copilot.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Добавляет поддержку выбора модели.

**Атрибуты**:
- `label` (str): Метка провайдера ("GitHub Copilot").
- `url` (str): URL сервиса ("https://github.com/copilot").
- `working` (bool): Флаг, указывающий на работоспособность провайдера (`True`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (`True`).
- `supports_stream` (bool): Флаг, указывающий на поддержку стриминга (`True`).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o").
- `models` (List[str]): Список поддерживаемых моделей.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    stream: bool = False,
    api_key: str = None,
    proxy: str = None,
    cookies: Cookies = None,
    conversation_id: str = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с GitHub Copilot.

    Args:
        cls: Ссылка на класс.
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        stream (bool, optional): Флаг, указывающий на использование стриминга. По умолчанию `False`.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        cookies (Cookies, optional): Cookies для аутентификации. По умолчанию `None`.
        conversation_id (str, optional): Идентификатор диалога. По умолчанию `None`.
        conversation (Conversation, optional): Объект диалога. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий на необходимость возврата объекта диалога. По умолчанию `False`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от GitHub Copilot.
    """
```

**Назначение**:
Функция `create_async_generator` создает и возвращает асинхронный генератор, который используется для взаимодействия с API GitHub Copilot. Она отвечает за установку соединения, аутентификацию, отправку сообщений и получение ответов от модели, выбранной пользователем.

**Параметры**:
- `cls`: Ссылка на класс `GithubCopilot`.
- `model` (str): Имя модели, которую следует использовать для генерации ответов. Если не указана, используется `default_model`.
- `messages (Messages)`: Список сообщений, составляющих контекст диалога. Обычно это список словарей, где каждый словарь содержит ключи `role` (например, "user" или "assistant") и `content` (текст сообщения).
- `stream (bool, optional)`: Определяет, будет ли ответ генерироваться потоково (streaming) или целиком. По умолчанию `False`.
- `api_key (str, optional)`: API-ключ для аутентификации в GitHub Copilot. Если не предоставлен, функция пытается получить его автоматически. По умолчанию `None`.
- `proxy (str, optional)`: URL прокси-сервера, если необходимо использовать прокси для подключения к API. По умолчанию `None`.
- `cookies (Cookies, optional)`: Cookie-файлы для аутентификации. Если не предоставлены, функция пытается получить их автоматически для домена "github.com". По умолчанию `None`.
- `conversation_id (str, optional)`: Идентификатор существующего диалога. Если не предоставлен, создается новый диалог. По умолчанию `None`.
- `conversation (Conversation, optional)`: Объект класса `Conversation`, содержащий информацию о диалоге. Если предоставлен, используется его `conversation_id`. По умолчанию `None`.
- `return_conversation (bool, optional)`: Если `True`, генератор сначала вернет объект `Conversation` с `conversation_id`. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API GitHub Copilot.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает текстовые фрагменты ответа от GitHub Copilot.

**Как работает функция**:

1. **Инициализация**:
   - Устанавливает модель, если она не была указана.
   - Получает или устанавливает cookies для github.com
   - Создает асинхронную сессию `aiohttp.ClientSession` для выполнения HTTP-запросов. Сессия использует `connector` для обработки прокси и передает cookies и заголовки.

2. **Аутентификация**:
   - Если `api_key` не предоставлен, функция запрашивает токен аутентификации, отправляя POST-запрос на `https://github.com/github-copilot/chat/token`.
   - Полученный токен используется для формирования заголовка `Authorization`.

3. **Управление диалогом**:
   - Если `conversation_id` не предоставлен, функция создает новый диалог, отправляя POST-запрос на `https://api.individual.githubcopilot.com/github/chat/threads`.
   - Полученный `thread_id` используется в качестве `conversation_id`.
   - Если `return_conversation` установлен в `True`, генератор сначала выдает объект `Conversation` с полученным или предоставленным `conversation_id`.

4. **Формирование и отправка запроса**:
   - Формирует JSON-данные запроса, включая `content` (сообщение пользователя), `intent`, `references`, `context`, `currentURL`, `streaming`, `confirmations`, `customInstructions`, `model` и `mode`.
   - Отправляет POST-запрос на `https://api.individual.githubcopilot.com/github/chat/threads/{conversation_id}/messages` с JSON-данными и заголовками аутентификации.

5. **Обработка потокового ответа**:
   - Асинхронно читает ответ от сервера построчно.
   - Каждая строка, начинающаяся с `b"data: "`, содержит JSON-данные.
   - Если `data.get("type") == "content"`, извлекает `data.get("body")` и выдает его как фрагмент ответа.

```text
   Начало
   │
   ├──► Проверка наличия model, cookies, api_key
   │   │
   │   └──► Если не указаны, получение значений по умолчанию или через запросы
   │       │
   │       └──► Создание ClientSession с headers, cookies, proxy
   │           │
   │           ├──► Получение api_key (если не предоставлен)
   │           │   │
   │           │   └──► POST запрос на "https://github.com/github-copilot/chat/token"
   │           │       │
   │           │       └──► Извлечение токена из ответа
   │           │
   │           └──► Получение conversation_id (если не предоставлен)
   │               │
   │               └──► POST запрос на "https://api.individual.githubcopilot.com/github/chat/threads"
   │                   │
   │                   └──► Извлечение thread_id из ответа
   │
   │
   └──► Формирование json_data
   │   │
   │   └──► POST запрос на "https://api.individual.githubcopilot.com/github/chat/threads/{conversation_id}/messages"
   │       │
   │       └──► Асинхронное чтение ответа
   │           │
   │           └──► Обработка каждой строки ответа
   │               │
   │               └──► Если строка начинается с "data: ", извлечение данных
   │                   │
   │                   └──► Если type == "content", извлечение body и yield
   │
   │
   Конец
```

**Примеры**:

```python
# Пример 1: Создание генератора с использованием модели по умолчанию и списком сообщений.
messages = [{"role": "user", "content": "Hello, Copilot!"}]
generator = GithubCopilot.create_async_generator(model=None, messages=messages)

# Пример 2: Создание генератора с указанием API-ключа и прокси.
messages = [{"role": "user", "content": "Как мне отсортировать список в Python?"}]
generator = GithubCopilot.create_async_generator(
    model="gpt-4", messages=messages, api_key="YOUR_API_KEY", proxy="http://your.proxy:8080"
)

# Пример 3: Создание генератора с использованием существующего conversation_id.
messages = [{"role": "user", "content": "Продолжи, пожалуйста."}]
generator = GithubCopilot.create_async_generator(
    model="gpt-4", messages=messages, conversation_id="existing_conversation_id"
)