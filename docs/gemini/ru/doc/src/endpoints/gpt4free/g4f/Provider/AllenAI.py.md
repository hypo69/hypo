# Модуль AllenAI для взаимодействия с Ai2 Playground
## Обзор

Модуль `AllenAI` предоставляет асинхронный генератор для взаимодействия с Ai2 Playground, используя API AllenAI. Он поддерживает потоковую передачу данных и предназначен для работы с различными моделями, предоставляемыми Ai2 Playground.

## Подробнее

Этот модуль позволяет интегрировать функциональность AI2 Playground в проект `hypotez`. Он включает в себя классы для управления диалогом (`Conversation`) и асинхронный провайдер (`AllenAI`), который обрабатывает запросы к API AllenAI. Модуль поддерживает выбор модели, передачу истории сообщений и обработку ответов в потоковом режиме.

## Классы

### `Conversation`

**Описание**: Класс для хранения информации о текущем диалоге. Наследует `JsonConversation`.

**Наследует**:
- `JsonConversation`

**Атрибуты**:
- `parent` (str | None): Идентификатор родительского сообщения в диалоге. По умолчанию `None`.
- `x_anonymous_user_id` (str | None): Анонимный идентификатор пользователя. Генерируется случайным образом при создании экземпляра класса, если не задан.
- `model` (str): Модель, используемая в текущем диалоге.
- `messages` (list): Список сообщений в текущем диалоге.

**Методы**:
- `__init__(self, model: str)`: Инициализирует новый экземпляр класса `Conversation`.

     **Параметры**:
     - `model` (str): Модель, используемая в текущем диалоге.

     **Как работает метод**:
     1. Вызывает конструктор родительского класса `JsonConversation`.
     2. Устанавливает атрибут `model` равным переданному значению.
     3. Инициализирует пустой список `messages` для хранения сообщений диалога.
     4. Если `x_anonymous_user_id` не установлен, генерирует новый UUID и присваивает его атрибуту `x_anonymous_user_id`.

### `AllenAI`

**Описание**: Класс, предоставляющий асинхронный генератор для взаимодействия с API Ai2 Playground.

**Наследует**:
- `AsyncGeneratorProvider`
- `ProviderModelMixin`

**Атрибуты**:
- `label` (str): Метка провайдера ("Ai2 Playground").
- `url` (str): URL Ai2 Playground ("https://playground.allenai.org").
- `login_url` (str | None): URL для входа (в данном случае `None`, так как аутентификация не требуется).
- `api_endpoint` (str): URL API для отправки сообщений ("https://olmo-api.allen.ai/v4/message/stream").
- `working` (bool): Флаг, указывающий, работает ли провайдер (в данном случае `True`).
- `needs_auth` (bool): Флаг, указывающий, требуется ли аутентификация (в данном случае `False`).
- `use_nodriver` (bool): Флаг, указывающий, нужно ли использовать веб-драйвер (в данном случае `False`).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (в данном случае `True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (в данном случае `False`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию ('tulu3-405b').
- `models` (list): Список поддерживаемых моделей.
- `model_aliases` (dict): Словарь псевдонимов моделей для удобства использования.

**Методы**:
- `create_async_generator(cls, model: str, messages: Messages, proxy: str = None, host: str = "inferd", private: bool = True, top_p: float = None, temperature: float = None, conversation: Conversation = None, return_conversation: bool = False, **kwargs) -> AsyncResult`

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    host: str = "inferd",
    private: bool = True,
    top_p: float = None,
    temperature: float = None,
    conversation: Conversation = None,
    return_conversation: bool = False,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с API AllenAI.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        host (str, optional): Хост. По умолчанию "inferd".
        private (bool, optional): Флаг, указывающий, является ли диалог приватным. По умолчанию `True`.
        top_p (float, optional): Значение top_p. По умолчанию `None`.
        temperature (float, optional): Значение temperature. По умолчанию `None`.
        conversation (Conversation, optional): Объект диалога. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект диалога. По умолчанию `False`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API AllenAI.

    Raises:
        Exception: В случае ошибки при взаимодействии с API.
    """
```

**Назначение**:
Создает асинхронный генератор для взаимодействия с API AllenAI. Этот генератор отправляет сообщения в API и возвращает ответы в потоковом режиме.

**Параметры**:
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `host` (str, optional): Хост. По умолчанию "inferd".
- `private` (bool, optional): Флаг, указывающий, является ли диалог приватным. По умолчанию `True`.
- `top_p` (float, optional): Значение top_p. По умолчанию `None`.
- `temperature` (float, optional): Значение temperature. По умолчанию `None`.
- `conversation` (Conversation, optional): Объект диалога. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект диалога. По умолчанию `False`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API AllenAI.

**Вызывает исключения**:
- `Exception`: В случае ошибки при взаимодействии с API.

**Внутренние функции**:
Отсутствуют

**Как работает функция**:

 1. Функция принимает параметры для настройки запроса к API AllenAI, включая модель, сообщения, прокси, хост, параметры приватности, значения `top_p` и `temperature`, а также объект диалога `conversation`.
 2. Форматирует промпт на основе переданных сообщений. Если объект диалога `conversation` не передан, используется функция `format_prompt` для форматирования всех сообщений, иначе используется функция `get_last_user_message` для извлечения последнего сообщения пользователя.
 3. Инициализирует или обновляет объект диалога `conversation`. Если `conversation` не передан, создается новый объект `Conversation` с указанной моделью.
 4. Генерирует уникальную границу (boundary) для multipart/form-data.
 5. Формирует заголовки запроса, включая `content-type`, `origin`, `referer`, `user-agent` и `x-anonymous-user-id` (из объекта `conversation`).
 6. Создает тело запроса в формате multipart/form-data, добавляя параметры, такие как модель, хост, контент (промпт) и флаг приватности.
 7. Если в объекте `conversation` присутствует `parent` (идентификатор родительского сообщения), он также добавляется в тело запроса.
 8. Опционально добавляются параметры `temperature` и `top_p`, если они переданы.
 9. Отправляет POST-запрос к API AllenAI с использованием `ClientSession` из библиотеки `aiohttp`.
 10. Обрабатывает ответ от API в асинхронном режиме, читая его по частям (chunks).
 11. Декодирует каждую часть ответа, извлекает данные в формате JSON из каждой строки и обрабатывает их.
 12. Обновляет `current_parent` (идентификатор текущего родительского сообщения) на основе данных, полученных от API.
 13. Извлекает контент из сообщений с ролью "assistant" и возвращает его через генератор.
 14. При получении финального ответа или при достижении `finish_reason` равного "stop", обновляет объект `conversation`, добавляет сообщения в историю и возвращает объект `conversation`, если `return_conversation` установлен в `True`.
 15. Завершает работу генератора, возвращая `FinishReason("stop")`.

**ASCII flowchart**:

```
    [Начало]
       |
    [Форматирование промпта]
       |
    [Инициализация/Обновление conversation]
       |
    [Генерация boundary]
       |
    [Формирование заголовков]
       |
    [Создание тела запроса (form-data)]
       |
    [Отправка POST-запроса к API]
       |
    [Обработка ответа по частям (chunks)]
       |
    [Декодирование и извлечение JSON]
       |
    [Обновление current_parent]
       |
    [Извлечение контента assistant]
       |
    [Получен final или finish_reason=stop?]
    ----Нет----->[Вернуть контент]
       |Да
    [Обновление conversation]
       |
    [Возврат conversation (если return_conversation)]
       |
    [Возврат FinishReason("stop")]
       |
    [Конец]
```

**Примеры**:

```python
# Пример 1: Создание асинхронного генератора с минимальными параметрами
model = "tulu3-405b"
messages = [{"role": "user", "content": "Hello, how are you?"}]
async_generator = AllenAI.create_async_generator(model=model, messages=messages)

# Пример 2: Создание асинхронного генератора с указанием прокси и температуры
model = "tulu3-405b"
messages = [{"role": "user", "content": "Tell me a joke."}]
proxy = "http://your-proxy-url:8080"
temperature = 0.7
async_generator = AllenAI.create_async_generator(model=model, messages=messages, proxy=proxy, temperature=temperature)

# Пример 3: Создание асинхронного генератора с использованием существующего объекта conversation
model = "tulu3-405b"
messages = [{"role": "user", "content": "What is the capital of France?"}]
conversation = Conversation(model=model)
async_generator = AllenAI.create_async_generator(model=model, messages=messages, conversation=conversation, return_conversation=True)