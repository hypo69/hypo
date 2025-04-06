# Модуль для работы с GitHub Copilot
## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с GitHub Copilot для генерации текста. Он включает в себя поддержку потоковой передачи, аутентификации и управления беседами.

## Подробней

Данный код обеспечивает интеграцию с GitHub Copilot, позволяя использовать его возможности для генерации текста в асинхронном режиме. Он обрабатывает аутентификацию, создание бесед и потоковую передачу данных, а также поддерживает различные модели.

## Классы

### `Conversation`

**Описание**: Класс для представления беседы с GitHub Copilot.

**Атрибуты**:

-   `conversation_id` (str): Идентификатор беседы.

**Методы**:

-   `__init__(self, conversation_id: str)`: Конструктор класса, инициализирует объект беседы с заданным идентификатором.

### `GithubCopilot`

**Описание**: Класс, предоставляющий асинхронный генератор для взаимодействия с GitHub Copilot.

**Наследует**:

-   `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронной генерации.
-   `ProviderModelMixin`: Добавляет функциональность для работы с моделями.

**Атрибуты**:

-   `label` (str): Метка провайдера ("GitHub Copilot").
-   `url` (str): URL GitHub Copilot ("https://github.com/copilot").
-   `working` (bool): Указывает, что провайдер работает (True).
-   `needs_auth` (bool): Указывает, что требуется аутентификация (True).
-   `supports_stream` (bool): Указывает, что поддерживается потоковая передача (True).
-   `default_model` (str): Модель по умолчанию ("gpt-4o").
-   `models` (List[str]): Список поддерживаемых моделей (\["gpt-4o", "o1-mini", "o1-preview", "claude-3.5-sonnet"] ).

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
        """Создает асинхронный генератор для взаимодействия с GitHub Copilot.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию False.
            api_key (str, optional): API ключ для аутентификации. По умолчанию None.
            proxy (str, optional): URL прокси-сервера. По умолчанию None.
            cookies (Cookies, optional): Cookie для аутентификации. По умолчанию None.
            conversation_id (str, optional): Идентификатор беседы. По умолчанию None.
            conversation (Conversation, optional): Объект беседы. По умолчанию None.
            return_conversation (bool, optional): Флаг, указывающий, возвращать ли объект беседы. По умолчанию False.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий результаты взаимодействия с GitHub Copilot.

        Как работает функция:
        1.  Определяет модель для использования, если она не указана.
        2.  Получает cookies для аутентификации, если они не предоставлены.
        3.  Создает асинхронную сессию с использованием `ClientSession` и переданных параметров (proxy, cookies, headers).
        4.  Получает токен API, если он не предоставлен.
        5.  Определяет идентификатор беседы, если он не предоставлен.
        6.  Если `return_conversation` установлен в `True`, возвращает объект `Conversation` с идентификатором беседы.
        7.  Форматирует запрос и отправляет его в GitHub Copilot.
        8.  Получает ответы от GitHub Copilot и возвращает их через асинхронный генератор.

        ASCII flowchart:

        Определение_модели_и_cookies
        ↓
        Создание_асинхронной_сессии
        ↓
        Получение_токена_API
        ↓
        Определение_идентификатора_беседы
        ↓
        Возврат_объекта_беседы_или_форматирование_запроса
        ↓
        Отправка_запроса_и_получение_ответов

        Примеры:
        >>> messages = [{"role": "user", "content": "Hello, Copilot!"}]
        >>> async def run():
        ...     async for message in GithubCopilot.create_async_generator(model="gpt-4o", messages=messages, api_key="your_api_key"):
        ...         print(message)
        >>> import asyncio
        >>> asyncio.run(run())
        """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с GitHub Copilot.

**Параметры**:

-   `model` (str): Модель для использования.
-   `messages` (Messages): Список сообщений для отправки.
-   `stream` (bool, optional): Флаг, указывающий, использовать ли потоковую передачу. По умолчанию `False`.
-   `api_key` (str, optional): API ключ для аутентификации. По умолчанию `None`.
-   `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
-   `cookies` (Cookies, optional): Cookie для аутентификации. По умолчанию `None`.
-   `conversation_id` (str, optional): Идентификатор беседы. По умолчанию `None`.
-   `conversation` (Conversation, optional): Объект беседы. По умолчанию `None`.
-   `return_conversation` (bool, optional): Флаг, указывающий, возвращать ли объект беседы. По умолчанию `False`.
-   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, возвращающий результаты взаимодействия с GitHub Copilot.

**Как работает функция**:

1.  **Определение модели и cookies**: Определяется модель для использования (если не указана, используется `default_model`) и получаются cookies для аутентификации (если не предоставлены).
2.  **Создание асинхронной сессии**: Создается асинхронная сессия с использованием `ClientSession` и переданных параметров (proxy, cookies, headers).
3.  **Получение токена API**: Получается токен API, если он не предоставлен. Если `api_key` не передан, функция отправляет запрос к `https://github.com/github-copilot/chat/token` для получения токена.
4.  **Определение идентификатора беседы**: Определяется идентификатор беседы, если он не предоставлен. Если `conversation_id` не передан, функция отправляет запрос к `https://api.individual.githubcopilot.com/github/chat/threads` для получения `thread_id`.
5.  **Возврат объекта беседы или форматирование запроса**: Если `return_conversation` установлен в `True`, возвращается объект `Conversation` с идентификатором беседы. В противном случае форматируется запрос с использованием `format_prompt` или `get_last_user_message`.
6.  **Отправка запроса и получение ответов**: Отправляется запрос к GitHub Copilot и получается ответы через асинхронный генератор. Функция отправляет POST-запрос к `https://api.individual.githubcopilot.com/github/chat/threads/{conversation_id}/messages` и обрабатывает потоковые данные ответа.

**ASCII flowchart**:

```
Определение_модели_и_cookies
    ↓
Создание_асинхронной_сессии
    ↓
Получение_токена_API
    ↓
Определение_идентификатора_беседы
    ↓
Возврат_объекта_беседы_или_форматирование_запроса
    ↓
Отправка_запроса_и_получение_ответов
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, Copilot!"}]
async def run():
    async for message in GithubCopilot.create_async_generator(model="gpt-4o", messages=messages, api_key="your_api_key"):
        print(message)
import asyncio
asyncio.run(run())