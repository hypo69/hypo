# Модуль `Qwen_Qwen_2_5M`

## Обзор

Модуль `Qwen_Qwen_2_5M` предоставляет асинхронный генератор для взаимодействия с моделью Qwen-2.5M через API сервиса Hugging Face Space. Он позволяет отправлять запросы к модели и получать ответы в режиме реального времени, поддерживая потоковую передачу данных.

## Подробней

Этот модуль предназначен для интеграции с AI-моделью Qwen-2.5M, размещенной на Hugging Face Space. Он использует асинхронные HTTP-запросы для взаимодействия с API, обеспечивая эффективную обработку данных в реальном времени. Модуль поддерживает настройку прокси-сервера, системные сообщения и ведение истории сообщений.

## Классы

### `Qwen_Qwen_2_5M`

**Описание**: Класс `Qwen_Qwen_2_5M` реализует асинхронный генератор для взаимодействия с моделью Qwen-2.5M.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность асинхронного генератора.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, отображаемая как "Qwen Qwen-2.5M".
- `url` (str): URL сервиса Hugging Face Space.
- `api_endpoint` (str): URL API для отправки запросов.
- `working` (bool): Указывает, что провайдер находится в рабочем состоянии.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных.
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений.
- `default_model` (str): Модель по умолчанию ("qwen-2.5-1m-demo").
- `model_aliases` (dict): Псевдонимы моделей.
- `models` (list): Список поддерживаемых моделей.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью.

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
    """
    Создает асинхронный генератор для взаимодействия с моделью Qwen-2.5M.

    Args:
        model (str): Имя используемой модели.
        messages (Messages): Список сообщений для отправки.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект разговора. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект разговора для поддержания состояния. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий результаты взаимодействия с моделью.

    Как работает функция:
    1. **Генерация уникального идентификатора сессии**: Если объект разговора отсутствует, генерируется уникальный идентификатор сессии (`session_hash`).
    2. **Инициализация объекта разговора (опционально)**: Если `return_conversation` имеет значение `True`, функция создает и выдает объект `JsonConversation` с идентификатором сессии.
    3. **Форматирование промпта**: Если объект разговора отсутствует, сообщения форматируются в промпт. В противном случае, извлекается последнее сообщение пользователя.
    4. **Подготовка заголовков HTTP-запроса**: Определяются заголовки, необходимые для выполнения запроса к API.
    5. **Подготовка полезной нагрузки (payload) для запроса**: Формируется JSON-структура с данными для отправки, включая промпт и идентификатор сессии.
    6. **Отправка запроса к API**: Используется `aiohttp.ClientSession` для отправки POST-запроса к API.
    7. **Обработка ответа**: Извлекаются данные из JSON-ответа.
    8. **Отправка запроса на присоединение к очереди**: Отправляется POST-запрос для присоединения к очереди обработки.
    9. **Извлечение идентификатора события**: Извлекается `event_id` из ответа.
    10. **Подготовка запроса на получение потока данных**: Формируется URL для получения потока данных.
    11. **Отправка запроса на получение потока данных**: Отправляется GET-запрос для получения потока данных.
    12. **Обработка потока данных**: Асинхронно обрабатываются строки из потока данных, декодируются и преобразуются в JSON.
    13. **Извлечение и выдача данных генерации**: Извлекаются данные генерации из JSON и выдаются как результат работы генератора.
    14. **Проверка завершения процесса**: Проверяется, завершен ли процесс генерации, и извлекаются финальные данные.
    15. **Обработка ошибок JSON**: В случае ошибки декодирования JSON, информация об ошибке логируется.

    Внутренние функции:
    ### `generate_session_hash`
    ```python
    def generate_session_hash() -> str:
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:12]
    ```

    **Назначение**:
    - Генерирует уникальный идентификатор сессии (session hash).

    **Как работает функция**:
    1. Создает UUID (Universally Unique Identifier) с использованием `uuid.uuid4()`.
    2. Преобразует UUID в строку.
    3. Удаляет все дефисы из строки.
    4. Возвращает первые 12 символов полученной строки.

    **Примеры**:
    ```python
    >>> generate_session_hash()
    'a1b2c3d4e5f6'
    ```

    flowchart:
    A[Генерация UUID]
    B[Преобразование в строку]
    C[Удаление дефисов]
    D[Получение первых 12 символов]
    A --> B
    B --> C
    C --> D

    Raises:
        JSONDecodeError: Если не удается распарсить JSON.
    """
    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:12]

    # Generate a unique session hash
    session_hash = generate_session_hash() if conversation is None else getattr(conversation, "session_hash")
    if return_conversation:
        yield JsonConversation(session_hash=session_hash)

    prompt = format_prompt(messages) if conversation is None else get_last_user_message(messages)

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US',
        'content-type': 'application/json',
        'origin': cls.url,
        'referer': f'{cls.url}/?__theme=light',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    payload_predict = {
        "data":[{"files":[],"text":prompt},[],[]],
        "event_data": None,
        "fn_index": 1,
        "trigger_id": 5,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # Send join request
        async with session.post(cls.api_endpoint, headers=headers, json=payload_predict) as response:
            data = (await response.json())['data']

        join_url = f"{cls.url}/queue/join?__theme=light"
        join_data = {"data":[[[{"id":None,"elem_id":None,"elem_classes":None,"name":None,"text":prompt,"flushing":None,"avatar":"","files":[]},None]],None,0],"event_data":None,"fn_index":2,"trigger_id":5,"session_hash":session_hash}

        async with session.post(join_url, headers=headers, json=join_data) as response:
            event_id = (await response.json())['event_id']

        # Prepare data stream request
        url_data = f'{cls.url}/queue/data?session_hash={session_hash}'

        headers_data = {
            'accept': 'text/event-stream',
            'referer': f'{cls.url}/?__theme=light',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
        }
        # Send data stream request
        async with session.get(url_data, headers=headers_data) as response:
            yield_response = ""
            yield_response_len = 0
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # Look for generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output'] and json_data['output']['data'][0]:
                                output_data = json_data['output']['data'][0][0]
                                if len(output_data) > 2:
                                    text = output_data[2].split("\\n<summary>")[0]
                                    if text == "Qwen is thinking...":
                                        yield Reasoning(None, text)
                                    elif text.startswith(yield_response):
                                        yield text[yield_response_len:]
                                    else:
                                        yield text
                                    yield_response_len = len(text)
                                    yield_response = text

                        # Check for completion
                        if json_data.get('msg') == 'process_completed':
                            # Final check to ensure we get the complete response
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data'][0][0][1][0]["text"].split("\\n<summary>")[0]
                                yield output_data[yield_response_len:]
                                yield_response_len = len(text)
                            break

                    except json.JSONDecodeError as ex:
                        debug.log("Could not parse JSON:", decoded_line)
## Примеры

```python
# Пример использования асинхронного генератора:
import asyncio
from typing import AsyncGenerator, List

async def main():
    messages = [
        {"role": "user", "content": "Hello, Qwen!"}
    ]
    async for response in Qwen_Qwen_2_5M.create_async_generator(model="qwen-2.5-1m-demo", messages=messages):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

```python
# Пример с использованием прокси:
import asyncio
from typing import AsyncGenerator, List

async def main():
    messages = [
        {"role": "user", "content": "Tell me a joke."}
    ]
    proxy = "http://your_proxy:8080"
    async for response in Qwen_Qwen_2_5M.create_async_generator(model="qwen-2.5-1m-demo", messages=messages, proxy=proxy):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```