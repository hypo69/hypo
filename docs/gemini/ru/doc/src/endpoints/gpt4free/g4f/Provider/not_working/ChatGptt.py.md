# Модуль ChatGptt

## Обзор

Модуль `ChatGptt` предоставляет асинхронный генератор для взаимодействия с API `chatgptt.me`. Он позволяет отправлять сообщения и получать ответы, используя модели GPT. Модуль поддерживает потоковую передачу данных и системные сообщения, а также сохраняет историю сообщений.

## Подробней

Этот модуль предназначен для интеграции с `chatgptt.me` и обеспечивает асинхронное взаимодействие с их API. Он извлекает необходимые токены аутентификации из HTML-страницы, отправляет сообщения и возвращает результаты в виде асинхронного генератора. Этот модуль является частью проекта `hypotez` и расположен в каталоге `hypotez/src/endpoints/gpt4free/g4f/Provider/not_working`. Это указывает на то, что провайдер в данный момент не работает.

## Классы

### `ChatGptt`

**Описание**: Класс `ChatGptt` предоставляет функциональность для взаимодействия с API `chatgptt.me`. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin` и реализует методы для создания асинхронного генератора сообщений.

**Принцип работы**:
Класс использует `aiohttp` для асинхронных HTTP-запросов. Он извлекает токены аутентификации из HTML-страницы, формирует полезную нагрузку с сообщением пользователя и отправляет ее в API `chatgptt.me`. Полученные данные передаются через асинхронный генератор.

**Аттрибуты**:
- `url` (str): URL `chatgptt.me`.
- `api_endpoint` (str): URL API для отправки сообщений.
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (`True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (`True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (`True`).
- `default_model` (str): Модель по умолчанию (`gpt-4o`).
- `models` (List[str]): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для отправки сообщений и получения ответов.

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
    """
    Создает асинхронный генератор для отправки сообщений и получения ответов от API `chatgptt.me`.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий ответы от API.

    Raises:
        RuntimeError: Если не удалось извлечь токены аутентификации из HTML.
        Exception: Если возникает ошибка при выполнении HTTP-запроса.

    """
```

**Назначение**: Функция `create_async_generator` создает асинхронный генератор для взаимодействия с API `chatgptt.me`. Она отправляет сообщения и получает ответы, используя указанную модель.

**Параметры**:
- `cls` (ChatGptt): Ссылка на класс `ChatGptt`.
- `model` (str): Модель для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось извлечь токены аутентификации из HTML.
- `Exception`: Если возникает ошибка при выполнении HTTP-запроса.

**Как работает функция**:

1. **Выбор модели**:
   - Происходит получение имени модели с помощью `cls.get_model(model)`

2. **Подготовка заголовков**:
   - Формируются заголовки HTTP-запроса, включая `authority`, `accept`, `origin`, `referer` и `user-agent`.

3. **Создание сессии**:
   - Создается асинхронная сессия `ClientSession` с заданными заголовками.

4. **Получение начального содержимого страницы**:
   - Выполняется GET-запрос к `cls.url` для получения HTML-содержимого страницы.

5. **Извлечение токенов**:
   - Используются регулярные выражения для извлечения `nonce` и `post_id` из HTML-содержимого.

6. **Обработка ошибок извлечения токенов**:
   - Если `nonce` или `post_id` не найдены, выбрасывается исключение `RuntimeError`.

7. **Подготовка полезной нагрузки**:
   - Формируется полезная нагрузка (payload) для POST-запроса, включающая `_wpnonce`, `post_id`, `url`, `action`, `message`, `bot_id`, `chatbot_identity`, `wpaicg_chat_client_id` и `wpaicg_chat_history`.
   - Сообщение форматируется с использованием `format_prompt(messages)`.

8. **Отправка запроса и получение ответа**:
   - Выполняется POST-запрос к `cls.api_endpoint` с заголовками, полезной нагрузкой и прокси (если указан).

9. **Обработка ответа**:
   - Полученный JSON-ответ извлекается, и данные из ключа `data` передаются в генератор.

```
   Начало работы
   │
   ├─► Выбор модели (model = cls.get_model(model))
   │
   ├─► Формирование HTTP-заголовков
   │  headers = {
   │  "authority": "chatgptt.me",
   │  "accept": "application/json",
   │  "origin": cls.url,
   │  "referer": f"{cls.url}/chat",
   │  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
   │  }
   │
   ├─► Создание асинхронной сессии (async with ClientSession(headers=headers) as session:)
   │
   ├─► Получение HTML-содержимого страницы (initial_response = await session.get(cls.url))
   │
   ├─► Извлечение nonce и post_id (nonce_match = re.search(r'data-nonce=["\\\']([^"\\\']+)["\\\']', html), post_id_match = re.search(r'data-post-id=["\\\']([^"\\\']+)["\\\']', html))
   │
   ├─► Проверка наличия nonce и post_id
   │  │
   │  ├─► Если nonce или post_id отсутствуют, то вызывается исключение RuntimeError("Required authentication tokens not found in page HTML")
   │  │
   │  └─► Если nonce и post_id присутствуют, то payload = { ..., 'message': format_prompt(messages), ... }
   │
   ├─► Отправка POST-запроса (async with session.post(cls.api_endpoint, headers=headers, data=payload, proxy=proxy) as response:)
   │
   ├─► Извлечение данных из JSON-ответа (result = await response.json(), yield result['data'])
   │
   └─► Завершение работы
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Hello"}]
model = "gpt-4o"
# proxy = "http://your_proxy:8080"  # Optional proxy

async def main():
    async for message in ChatGptt.create_async_generator(model=model, messages=messages):
        print(message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())