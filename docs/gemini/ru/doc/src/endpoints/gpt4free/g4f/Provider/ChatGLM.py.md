# Модуль для работы с ChatGLM
====================================

Модуль содержит класс `ChatGLM`, который используется для взаимодействия с моделью ChatGLM.
Он поддерживает асинхронную генерацию текста и предоставляет возможность взаимодействия с API ChatGLM.

## Обзор

Этот модуль обеспечивает интеграцию с API ChatGLM для генерации текста. Он поддерживает потоковую передачу ответов, что позволяет получать результаты по частям в асинхронном режиме.

## Подробней

Модуль `ChatGLM` является асинхронным провайдером, который использует `aiohttp` для выполнения HTTP-запросов к API ChatGLM. Он обрабатывает входящие сообщения, формирует запросы и возвращает результаты генерации текста. Модуль также обрабатывает ошибки декодирования JSON и обеспечивает потоковую передачу данных.

## Классы

### `ChatGLM`

**Описание**: Класс `ChatGLM` предоставляет функциональность для взаимодействия с API ChatGLM.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): URL сервиса ChatGLM (`https://chatglm.cn`).
- `api_endpoint` (str): URL API endpoint для stream (`https://chatglm.cn/chatglm/mainchat-api/guest/stream`).
- `working` (bool): Флаг, указывающий, работает ли провайдер (по умолчанию `True`).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу (по умолчанию `True`).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (по умолчанию `False`).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (по умолчанию `False`).
- `default_model` (str): Модель, используемая по умолчанию (`glm-4`).
- `models` (List[str]): Список поддерживаемых моделей (содержит только `default_model`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API ChatGLM.

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
        Создает асинхронный генератор для получения ответов от API ChatGLM.

        Args:
            model (str): Модель, используемая для генерации.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий ответы от API.

        Raises:
            aiohttp.ClientResponseError: Если возникает ошибка при выполнении HTTP-запроса.
            json.JSONDecodeError: Если не удается декодировать JSON из ответа API.

        Внутренние функции:
            отсутствуют

        Как работает функция:
        1.  Генерируется уникальный `device_id` для идентификации устройства.
        2.  Формируются HTTP-заголовки, включая `device_id` и другие метаданные.
        3.  Создается `ClientSession` с заданными заголовками.
        4.  Формируется JSON-тело запроса с сообщениями, ролями и контентом.
        5.  Выполняется POST-запрос к `api_endpoint` с использованием `ClientSession`.
        6.  Обрабатывается каждый чанк (chunk) ответа:
            - Декодируется чанк из `utf-8`.
            - Если чанк начинается с `'data: '`, извлекается JSON.
            - Извлекается `content` из `parts` JSON.
            - Извлекается `text_content` из `content`.
            - Извлекается и возвращается новый текст (`text`) из `text_content`.
            - Если `status` в JSON равен `'finish'`, возвращается `FinishReason("stop")`.
        7.  Обрабатываются исключения `json.JSONDecodeError` при декодировании JSON.

        ASCII flowchart:

        Генерация Device ID
        ↓
        Формирование HTTP Headers
        ↓
        Создание ClientSession
        ↓
        Формирование JSON Data
        ↓
        POST Request to API Endpoint
        ↓
        Обработка Chunks ответа
        |
        JSON Decode Error? --> Игнорировать
        |
        Извлечение и возврат текста
        |
        Status == 'finish'? --> Return FinishReason("stop")
        """
```

**Примеры**:

```python
# Пример использования create_async_generator
import asyncio
from typing import AsyncGenerator, List, Dict

from aiohttp import ClientSession

# Определение типа Messages
Messages = List[Dict[str, str]]

async def main():
    model: str = "glm-4"
    messages: Messages = [
        {"role": "user", "content": "Привет, как дела?"},
        {"role": "assistant", "content": "У меня все хорошо, спасибо!"}
    ]
    proxy: str = None

    # Mock класс ChatGLM для примера
    class ChatGLM:
        url = "https://chatglm.cn"
        api_endpoint = "https://chatglm.cn/chatglm/mainchat-api/guest/stream"

        working = True
        supports_stream = True
        supports_system_message = False
        supports_message_history = False

        default_model = "glm-4"
        models = [default_model]

        @classmethod
        async def create_async_generator(
            cls,
            model: str,
            messages: Messages,
            proxy: str = None,
            **kwargs
        ) -> AsyncGenerator[str, None]:
            device_id = str(uuid.uuid4()).replace('-', '')

            headers = {
                'Accept-Language': 'en-US,en;q=0.9',
                'App-Name': 'chatglm',
                'Authorization': 'undefined',
                'Content-Type': 'application/json',
                'Origin': 'https://chatglm.cn',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'X-App-Platform': 'pc',
                'X-App-Version': '0.0.1',
                'X-Device-Id': device_id,
                'Accept': 'text/event-stream'
            }

            async with ClientSession(headers=headers) as session:
                data = {
                    "assistant_id": "65940acff94777010aa6b796",
                    "conversation_id": "",
                    "meta_data": {
                        "if_plus_model": False,
                        "is_test": False,
                        "input_question_type": "xxxx",
                        "channel": "",
                        "draft_id": "",
                        "quote_log_id": "",
                        "platform": "pc"
                    },
                    "messages": [
                        {
                            "role": message["role"],
                            "content": [
                                {
                                    "type": "text",
                                    "text": message["content"]
                                }
                            ]
                        }
                        for message in messages
                    ]
                }

                yield_text = 0
                async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
                    # Mock raise_for_status
                    if response.status >= 400:
                        raise Exception(f"HTTP error {response.status}")

                    async for chunk in response.content:
                        if chunk:
                            decoded_chunk = chunk.decode('utf-8')
                            if decoded_chunk.startswith('data: '):
                                try:
                                    json_data = json.loads(decoded_chunk[6:])
                                    parts = json_data.get('parts', [])
                                    if parts:
                                        content = parts[0].get('content', [])
                                        if content:
                                            text_content = content[0].get('text', '')
                                            text = text_content[yield_text:]
                                            if text:
                                                yield text
                                                yield_text += len(text)
                                    if json_data.get('status') == 'finish':
                                        yield "stop"  # Mock FinishReason
                                except json.JSONDecodeError as ex:
                                    print(f"JSONDecodeError: {ex}")
                                    pass

    # Использование mock класса
    async def print_generator_content(generator: AsyncGenerator[str, None]):
        async for item in generator:
            print(item, end="")

    generator = ChatGLM.create_async_generator(model, messages, proxy)
    await print_generator_content(await generator)

if __name__ == "__main__":
    asyncio.run(main())