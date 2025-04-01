# Модуль для работы с Github Copilot
## Обзор

Модуль предоставляет класс `GithubCopilot` для взаимодействия с сервисом Github Copilot через API. Он позволяет создавать асинхронные генераторы для получения ответов от модели, поддерживать стриминг, аутентификацию и управление conversation_id.

## Подробней

Этот модуль используется для интеграции с Github Copilot, предоставляя возможность использовать его возможности в асинхронном режиме. Он поддерживает стриминг ответов, что позволяет получать ответы частями, а также требует аутентификацию через API key. Также модуль позволяет управлять conversation_id для поддержания контекста беседы.

## Классы

### `Conversation`

**Описание**: Класс для представления conversation_id.

    **Аттрибуты**:
    - `conversation_id` (str): Идентификатор беседы.

    **Методы**:
    - `__init__(conversation_id: str)`: Конструктор класса.

### `GithubCopilot`

**Описание**: Класс для взаимодействия с Github Copilot.

    **Наследует**:
    - `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
    - `ProviderModelMixin`: Добавляет поддержку выбора модели.

    **Аттрибуты**:
    - `label` (str): Метка провайдера ("GitHub Copilot").
    - `url` (str): URL Github Copilot ("https://github.com/copilot").
    - `working` (bool): Указывает, что провайдер работает (True).
    - `needs_auth` (bool): Указывает, что требуется аутентификация (True).
    - `supports_stream` (bool): Указывает, что поддерживается стриминг (True).
    - `default_model` (str): Модель по умолчанию ("gpt-4o").
    - `models` (List[str]): Список поддерживаемых моделей (["gpt-4o", "o1-mini", "o1-preview", "claude-3.5-sonnet"]).

    **Методы**:
    - `create_async_generator(...)`: Создает асинхронный генератор для получения ответов от модели.

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
        """Создает асинхронный генератор для получения ответов от модели Github Copilot.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool, optional): Включить ли стриминг. По умолчанию False.
            api_key (str, optional): API ключ для аутентификации. По умолчанию None.
            proxy (str, optional): Прокси сервер для использования. По умолчанию None.
            cookies (Cookies, optional): Cookies для использования. По умолчанию None.
            conversation_id (str, optional): ID беседы. По умолчанию None.
            conversation (Conversation, optional): Объект беседы. По умолчанию None.
            return_conversation (bool, optional): Вернуть ли объект беседы. По умолчанию False.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от модели.

        Raises:
            Exception: В случае ошибки при получении токена или отправке запроса.

        """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с Github Copilot.

**Параметры**:

- `cls`: Ссылка на класс `GithubCopilot`.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `stream` (bool, optional): Включить ли стриминг. По умолчанию `False`.
- `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
- `proxy` (str, optional): Прокси сервер для использования. По умолчанию `None`.
- `cookies` (Cookies, optional): Cookies для использования. По умолчанию `None`.
- `conversation_id` (str, optional): ID беседы. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект беседы. По умолчанию `None`.
- `return_conversation` (bool, optional): Вернуть ли объект беседы. По умолчанию `False`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:

- `AsyncResult`: Асинхронный генератор, возвращающий ответы от модели.

**Вызывает исключения**:

- `Exception`: В случае ошибки при получении токена или отправке запроса.

**Как работает функция**:

1.  **Инициализация**:
    *   Устанавливает модель по умолчанию, если она не указана.
    *   Получает cookies, если они не предоставлены.
    *   Создает асинхронную сессию `ClientSession` с заданными параметрами (proxy, cookies, headers).

2.  **Получение API ключа (если необходимо)**:
    *   Если `api_key` не предоставлен, пытается получить его, отправляя POST запрос на `"https://github.com/github-copilot/chat/token"`.
    *   Извлекает токен из JSON ответа.

3.  **Определение `conversation_id`**:
    *   Если `conversation` предоставлен, использует его `conversation_id`.
    *   Если `conversation_id` не предоставлен, отправляет POST запрос на `"https://api.individual.githubcopilot.com/github/chat/threads"` для создания новой беседы и извлекает `thread_id` из JSON ответа.

4.  **Формирование данных запроса**:
    *   Если `return_conversation` установлен в `True`, возвращает объект `Conversation` с `conversation_id`.
    *   Формирует тело запроса `json_data`, включающее контент сообщения, модель, режим и другие параметры.

5.  **Отправка запроса и обработка ответа**:
    *   Отправляет POST запрос на `"https://api.individual.githubcopilot.com/github/chat/threads/{conversation_id}/messages"` с сформированным телом запроса и заголовками.
    *   Асинхронно читает ответ построчно.
    *   Если строка начинается с `b"data: "`, пытается загрузить JSON из этой строки.
    *   Если в JSON есть ключ `"type"` со значением `"content"`, возвращает значение ключа `"body"`.

6.  **Обработка ошибок**:
    *   Использует `raise_for_status` для проверки статуса ответа и вызывает исключение в случае ошибки.

```
        Инициализация сессии и данных
        │
        ├───> Получение API ключа (если не предоставлен)
        │     │
        │     └───> POST "https://github.com/github-copilot/chat/token" -> Получение токена
        │
        └───> Определение conversation_id (если не предоставлен)
              │
              └───> POST "https://api.individual.githubcopilot.com/github/chat/threads" -> Получение thread_id
              │
              └───> Формирование json_data
              │
              └───> Отправка запроса
              │
              └───> POST "https://api.individual.githubcopilot.com/github/chat/threads/{conversation_id}/messages"
              │
              └───> Обработка стримингового ответа
                    │
                    └───> Проверка каждой строки на "data: "
                          │
                          └───> Извлечение JSON и проверка на type="content"
                          │
                          └───> Возврат body
```

**Примеры**:

```python
# Пример использования create_async_generator
model = "gpt-4o"
messages = [{"role": "user", "content": "Hello, how are you?"}]
api_key = "your_api_key"
proxy = "http://your_proxy:8080"
cookies = {"your_cookie": "your_cookie_value"}
conversation_id = "your_conversation_id"

async def main():
    async for response in GithubCopilot.create_async_generator(
        model=model,
        messages=messages,
        api_key=api_key,
        proxy=proxy,
        cookies=cookies,
        conversation_id=conversation_id,
    ):
        print(response)

# Запуск примера
# asyncio.run(main())