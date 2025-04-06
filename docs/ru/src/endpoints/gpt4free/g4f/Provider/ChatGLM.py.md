# Модуль для работы с провайдером ChatGLM
=========================================

Модуль предоставляет класс `ChatGLM`, который используется для взаимодействия с API ChatGLM для генерации текста.

## Обзор

Этот модуль является частью проекта `hypotez` и отвечает за интеграцию с провайдером ChatGLM, позволяя использовать его модели для генерации текста на основе предоставленных сообщений. Модуль асинхронный и использует `aiohttp` для выполнения HTTP-запросов.

## Подробнее

Модуль содержит класс `ChatGLM`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`. Он определяет параметры подключения к API ChatGLM, такие как URL, endpoint и заголовки.  `ChatGLM` поддерживает потоковую передачу данных и предоставляет асинхронный генератор для получения ответов от API ChatGLM.

## Классы

### `ChatGLM`

**Описание**: Класс для взаимодействия с API ChatGLM.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями провайдеров.

**Атрибуты**:
- `url` (str): URL сервиса ChatGLM (`https://chatglm.cn`).
- `api_endpoint` (str): Endpoint API для обмена сообщениями (`https://chatglm.cn/chatglm/mainchat-api/guest/stream`).
- `working` (bool): Флаг, указывающий, работает ли провайдер (по умолчанию `True`).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу (`True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (`False`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (`False`).
- `default_model` (str): Модель, используемая по умолчанию (`glm-4`).
- `models` (List[str]): Список поддерживаемых моделей ([`glm-4`]).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с API ChatGLM.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от API ChatGLM.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий текстовые фрагменты ответа.

    Raises:
        Exception: В случае ошибки при взаимодействии с API.

    """
```

**Назначение**: Функция создает асинхронный генератор для взаимодействия с API ChatGLM.

**Параметры**:
- `cls` (ChatGLM): Ссылка на класс `ChatGLM`.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий текстовые фрагменты ответа.

**Вызывает исключения**:
- `aiohttp.ClientResponseError`: Если HTTP-запрос завершается с ошибкой.
- `json.JSONDecodeError`: Если не удается декодировать JSON-ответ от API.

**Как работает функция**:

1. **Генерация `device_id`**: Генерируется уникальный `device_id` для идентификации устройства.
2. **Формирование заголовков**: Создаются необходимые HTTP-заголовки, включая `X-Device-Id` и `Content-Type`.
3. **Создание `ClientSession`**: Создается асинхронная сессия `aiohttp.ClientSession` с установленными заголовками.
4. **Формирование данных запроса**: Создается JSON-структура данных для отправки в API, включающая `assistant_id`, `conversation_id`, `meta_data` и `messages`.
5. **Отправка POST-запроса**: Отправляется POST-запрос к `cls.api_endpoint` с использованием `session.post` с данными в формате JSON и прокси (если указан).
6. **Обработка ответа**: Читаются данные из ответа по частям (chunks).
7. **Декодирование чанков**: Каждый чанк декодируется из `utf-8`.
8. **Извлечение JSON**: Извлекается JSON из чанка (если чанк начинается с `'data: '`).
9. **Извлечение текста**: Извлекается текстовое содержимое из JSON и передается через `yield`.
10. **Обработка статуса завершения**: Если в JSON присутствует статус `'finish'`, возвращается `FinishReason("stop")`.

```
Генерация device_id
↓
Формирование заголовков
↓
Создание ClientSession
↓
Формирование данных запроса
↓
Отправка POST-запроса
↓
Чтение данных из ответа по частям (chunks)
│
├──→  Декодирование чанков
│   │
│   └──→ Извлечение JSON
│       │
│       └──→ Извлечение текста и передача через yield
│           │
│           └──→ Обработка статуса завершения ("finish")
│
└──→  Завершение
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ChatGLM import ChatGLM

async def main():
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    async for response in ChatGLM.create_async_generator(model="glm-4", messages=messages):
        print(response, end="")

if __name__ == "__main__":
    asyncio.run(main())
```
Этот пример показывает, как использовать `create_async_generator` для получения ответа от API ChatGLM.
```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ChatGLM import ChatGLM

async def main():
    messages = [
        {"role": "user", "content": "What is the capital of France?"}
    ]
    async for response in ChatGLM.create_async_generator(model="glm-4", messages=messages, proxy="http://your_proxy:8080"):
        print(response, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

Этот пример показывает, как использовать `create_async_generator` с прокси-сервером.