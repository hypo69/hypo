# Модуль `Qwen_Qwen_2_72B`

## Обзор

Модуль `Qwen_Qwen_2_72B` предоставляет асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.72B, размещенной на платформе Hugging Face Space. Он позволяет отправлять запросы к модели и получать ответы в режиме реального времени.

## Подробней

Модуль использует асинхронные запросы для взаимодействия с API модели Qwen Qwen-2.72B. Он поддерживает потоковую передачу данных, что позволяет получать ответы по частям, а не ждать полной генерации. Модуль также поддерживает отправку системных сообщений для задания контекста модели.

## Классы

### `Qwen_Qwen_2_72B`

**Описание**: Класс `Qwen_Qwen_2_72B` реализует взаимодействие с моделью Qwen Qwen-2.72B через Hugging Face Space.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Qwen Qwen-2.72B"`.
- `url` (str): URL главной страницы модели, `"https://qwen-qwen2-72b-instruct.hf.space"`.
- `api_endpoint` (str): URL API для отправки запросов, `"https://qwen-qwen2-72b-instruct.hf.space/queue/join?"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, `True`.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи, `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений, `True`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений, `False`.
- `default_model` (str): Модель по умолчанию, `"qwen-qwen2-72b-instruct"`.
- `model_aliases` (dict): Псевдонимы моделей, `{"qwen-2-72b": default_model}`.
- `models` (list): Список поддерживаемых моделей, `["qwen-2-72b"]`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от модели.

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
    Создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.72B.

    Args:
        cls (Qwen_Qwen_2_72B): Ссылка на класс.
        model (str): Имя модели.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий части ответа от модели.

    Как работает функция:
    1. **Генерация уникального идентификатора сессии**:
       - Вызывается внутренняя функция `generate_session_hash()` для создания уникального идентификатора сессии. Этот идентификатор используется для связи между запросами к API.
    2. **Подготовка заголовков и полезной нагрузки для запроса `join`**:
       - Определяются заголовки (`headers_join`), необходимые для запроса. Эти заголовки включают информацию о типе контента, источнике запроса и User-Agent.
       - Извлекается системный промт (если есть) из списка сообщений и удаляется из общего списка сообщений.
       - Подготавливается полезная нагрузка (`payload_join`) для запроса, которая включает промт пользователя, системный промт и идентификатор сессии.
    3. **Отправка запроса `join`**:
       - Используется `aiohttp.ClientSession` для отправки асинхронного `POST` запроса к `cls.api_endpoint` с заголовками и полезной нагрузкой.
       - Получается `event_id` из JSON ответа.
    4. **Подготовка заголовков и параметров для запроса `data`**:
       - Определяется URL (`url_data`) для запроса данных.
       - Определяются заголовки (`headers_data`), необходимые для запроса данных, включая информацию о типе контента и User-Agent.
       - Подготавливаются параметры (`params_data`) для запроса данных, которые включают идентификатор сессии.
    5. **Отправка запроса `data` и обработка потока данных**:
       - Используется `aiohttp.ClientSession` для отправки асинхронного `GET` запроса к `url_data` с заголовками и параметрами.
       - Читается поток данных из ответа. Каждая строка декодируется и проверяется на наличие префикса `data:`.
       - Если строка содержит данные JSON, она парсится.
       - Проверяется наличие сообщения `process_generating` в JSON данных. Если оно присутствует, извлекаются фрагменты текста из поля `output` и генерируются (yield) по частям.
       - Проверяется наличие сообщения `process_completed` в JSON данных. Если оно присутствует, извлекается окончательный ответ из поля `output`, очищается от дубликатов и генерируется.
    6. **Обработка ошибок**:
       - Если возникает ошибка при парсинге JSON, она логируется с использованием `debug.log`.

    Внутренние функции:
    - `generate_session_hash()`:
        ```python
        def generate_session_hash():
            """Generate a unique session hash."""
            return str(uuid.uuid4()).replace('-', '')[:12]
        ```
        **Назначение**: Генерирует уникальный идентификатор сессии.

        **Как работает функция**:
        1. Генерирует UUID (Universally Unique Identifier) с помощью `uuid.uuid4()`.
        2. Преобразует UUID в строку и удаляет все дефисы (`-`) с помощью `replace('-', '')`.
        3. Берет первые 12 символов строки с помощью `[:12]`.
        4. Возвращает полученную строку.

        ASCII flowchart:
        ```
        UUID generation --> UUID to string --> Remove hyphens --> Take first 12 chars --> Return
        ```
    """

    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:12]

    # Generate a unique session hash
    session_hash = generate_session_hash()

    headers_join = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': f'{cls.url}',
        'referer': f'{cls.url}/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    # Prepare the prompt
    system_prompt = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    messages = [message for message in messages if message["role"] != "system"]
    prompt = format_prompt(messages)

    payload_join = {
        "data": [prompt, [], system_prompt],
        "event_data": None,
        "fn_index": 0,
        "trigger_id": 11,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # Send join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # Prepare data stream request
        url_data = f'{cls.url}/queue/data'

        headers_data = {
            'accept': 'text/event-stream',
            'accept-language': 'en-US,en;q=0.9',
            'referer': f'{cls.url}/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        params_data = {
            'session_hash': session_hash
        }

        # Send data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
            final_full_response = ""
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # Look for generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    for item in output_data[1]:
                                        if isinstance(item, list) and len(item) > 1:
                                            fragment = str(item[1])
                                            # Ignore [0, 1] type fragments and duplicates
                                            if not re.match(r'^\\[.*\\]$', fragment) and not full_response.endswith(fragment):
                                                full_response += fragment
                                                yield fragment

                        # Check for completion
                        if json_data.get('msg') == 'process_completed':
                            # Final check to ensure we get the complete response
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    final_full_response = output_data[1][0][1]
                                    
                                    # Clean up the final response
                                    if final_full_response.startswith(full_response):
                                        final_full_response = final_full_response[len(full_response):]
                                    
                                    # Yield the remaining part of the final response
                                    if final_full_response:
                                        yield final_full_response
                            break

                    except json.JSONDecodeError:
                        debug.log("Could not parse JSON:", decoded_line)
```

**Параметры**:
- `cls` (Qwen_Qwen_2_72B): Ссылка на класс.
- `model` (str): Имя модели.
- `messages` (Messages): Список сообщений для отправки модели.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части ответа от модели.

**Примеры**:
```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Hello, how are you?"}]
async def run():
    generator = await Qwen_Qwen_2_72B.create_async_generator(model="qwen-2-72b", messages=messages)
    async for fragment in generator:
        print(fragment, end="")

import asyncio
asyncio.run(run())
```

ASCII flowchart:

```
+-----------------------+
| Generate session_hash |
+-----------------------+
       |
       V
+-----------------------+
| Prepare headers_join  |
| and payload_join      |
+-----------------------+
       |
       V
+-----------------------+
| Send POST request to  |
| cls.api_endpoint      |
+-----------------------+
       |
       V
+-----------------------+
| Prepare headers_data  |
| and params_data       |
+-----------------------+
       |
       V
+-----------------------+
| Send GET request to   |
| url_data              |
+-----------------------+
       |
       V
+-----------------------+
| Process stream data   |
| and yield fragments   |
+-----------------------+