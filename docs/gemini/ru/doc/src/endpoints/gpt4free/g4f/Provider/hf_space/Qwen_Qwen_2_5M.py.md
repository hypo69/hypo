# Модуль Qwen_Qwen_2_5M

## Обзор

Модуль `Qwen_Qwen_2_5M` предоставляет асинхронный генератор для взаимодействия с моделью Qwen-2.5M через Hugging Face Space. Он поддерживает потоковую передачу ответов, системные сообщения и предоставляет возможность ведения истории сообщений.

## Подробнее

Этот модуль используется для подключения к сервису Qwen-2.5M, размещенному на Hugging Face Space, и получения ответов от модели. Он обрабатывает запросы к API, потоковую передачу данных и форматирование сообщений.

## Классы

### `Qwen_Qwen_2_5M`

**Описание**: Класс `Qwen_Qwen_2_5M` является провайдером асинхронного генератора, который также реализует `ProviderModelMixin`. Он предназначен для взаимодействия с моделью Qwen Qwen-2.5M.

**Принцип работы**:
1.  Инициализируется с параметрами, необходимыми для подключения к Hugging Face Space.
2.  Генерирует уникальный идентификатор сессии (session hash) для каждого разговора.
3.  Форматирует сообщения и отправляет их в API Hugging Face Space.
4.  Получает потоковые ответы и извлекает текст из JSON.
5.  Возвращает текст ответа по частям, используя генератор.

**Атрибуты**:
-   `label` (str): Метка провайдера, "Qwen Qwen-2.5M".
-   `url` (str): URL Hugging Face Space, "https://qwen-qwen2-5-1m-demo.hf.space".
-   `api_endpoint` (str): URL API endpoint, формируется из `url`.
-   `working` (bool): Флаг, указывающий, что провайдер работает (True).
-   `supports_stream` (bool): Флаг, указывающий, что провайдер поддерживает потоковую передачу (True).
-   `supports_system_message` (bool): Флаг, указывающий, что провайдер поддерживает системные сообщения (True).
-   `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений (False).
-   `default_model` (str): Модель по умолчанию, "qwen-2.5-1m-demo".
-   `model_aliases` (dict): Псевдонимы моделей, {"qwen-2.5-1m": default\_model}.
-   `models` (list): Список моделей, полученный из ключей `model_aliases`.

**Методы**:

-   `create_async_generator`: Создает асинхронный генератор для получения ответов от модели.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от модели Qwen-2.5M.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию None.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект conversation. По умолчанию False.
        conversation (JsonConversation, optional): Объект conversation для поддержания сессии. По умолчанию None.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа модели.

    Raises:
        aiohttp.ClientError: В случае ошибки при подключении к API.
        json.JSONDecodeError: Если не удается декодировать JSON из ответа.

    """
```

**Назначение**: Создание асинхронного генератора для взаимодействия с моделью Qwen-2.5M.

**Параметры**:

-   `cls` (Qwen_Qwen_2_5M): Ссылка на класс.
-   `model` (str): Имя модели, которую нужно использовать.
-   `messages` (Messages): Список сообщений, отправляемых модели.
-   `proxy` (str, optional): URL прокси-сервера, если необходимо. По умолчанию `None`.
-   `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект разговора (JsonConversation). По умолчанию `False`.
-   `conversation` (JsonConversation, optional): Объект разговора, содержащий информацию о текущей сессии. По умолчанию `None`.
-   `**kwargs`: Дополнительные параметры.

**Возвращает**:

-   `AsyncResult`: Асинхронный генератор, выдающий части ответа модели.

**Вызывает исключения**:

-   `aiohttp.ClientError`: Если возникает ошибка при подключении к API.
-   `json.JSONDecodeError`: Если не удается декодировать JSON из ответа.

**Как работает функция**:

1.  **Генерация идентификатора сессии**: Если объект `conversation` не передан, генерируется уникальный идентификатор сессии (`session_hash`).
2.  **Формирование запроса**: Формируется `prompt` для отправки. Если `conversation` не передан, используется вся история сообщений, иначе – только последнее сообщение пользователя.
3.  **Подготовка заголовков и полезной нагрузки (payload)**:
    -   Определяются необходимые HTTP-заголовки, такие как `accept`, `content-type`, `origin`, `referer` и `user-agent`.
    -   Создается полезная нагрузка `payload_predict` с данными для запроса `predict` к API.
4.  **Отправка запроса predict**: Отправляется POST-запрос к `cls.api_endpoint` с заголовками и полезной нагрузкой. Полученный ответ преобразуется в JSON.
5.  **Отправка запроса join**:
    -   Формируется URL `join_url` для присоединения к очереди обработки запросов.
    -   Создается полезная нагрузка `join_data` с информацией о запросе.
    -   Отправляется POST-запрос к `join_url` с заголовками и полезной нагрузкой. Полученный ответ преобразуется в JSON и извлекается `event_id`.
6.  **Подготовка к потоковой передаче данных**:
    -   Формируется URL `url_data` для получения потоковых данных.
    -   Определяются HTTP-заголовки `headers_data` для потокового запроса.
7.  **Отправка запроса на получение потоковых данных**:
    -   Отправляется GET-запрос к `url_data` с заголовками `headers_data`.
    -   В цикле обрабатываются строки ответа:
        -   Декодируются строки в UTF-8.
        -   Если строка начинается с `data: `, извлекается JSON-данные.
        -   Если `msg` равно `process_generating`, извлекается текст из `output_data` и передается в генератор.
        -   Если `msg` равно `process_completed`, извлекается полный текст ответа и передается в генератор.
8.  **Обработка ошибок**: В случае ошибки декодирования JSON, информация об ошибке логируется.

**ASCII flowchart**:

```
A [Генерация session_hash (если conversation отсутствует)]
|
B [Формирование prompt (из messages или conversation)]
|
C [Подготовка headers и payload_predict]
|
D [POST-запрос к cls.api_endpoint]
|
E [Обработка ответа (JSON)]
|
F [Подготовка join_url и join_data]
|
G [POST-запрос к join_url]
|
H [Обработка ответа (JSON), получение event_id]
|
I [Подготовка url_data и headers_data]
|
J [GET-запрос к url_data (потоковая передача)]
|
K [Обработка потоковых данных]
|
L [Извлечение и передача текста в генератор]
|
M [Обработка ошибок JSONDecodeError]

```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Hello, Qwen!"}]
async for response_part in Qwen_Qwen_2_5M.create_async_generator(model="qwen-2.5-1m-demo", messages=messages):
    print(response_part, end="")

# Пример использования с прокси
messages = [{"role": "user", "content": "Tell me a joke."}]
async for response_part in Qwen_Qwen_2_5M.create_async_generator(model="qwen-2.5-1m-demo", messages=messages, proxy="http://proxy.example.com"):
    print(response_part, end="")

# Пример использования с conversation
from g4f.providers.response import JsonConversation
conversation = JsonConversation(session_hash="123456789012")
messages = [{"role": "user", "content": "Continue the joke."}]
async for response_part in Qwen_Qwen_2_5M.create_async_generator(model="qwen-2.5-1m-demo", messages=messages, conversation=conversation):
    print(response_part, end="")