# Модуль `Qwen_Qwen_2_5`

## Обзор

Модуль `Qwen_Qwen_2_5` представляет собой реализацию асинхронного генератора, взаимодействующего с моделью Qwen Qwen-2.5 через API Hugging Face Space. Он обеспечивает потоковую передачу данных и поддерживает системные сообщения.

## Подробнее

Модуль предназначен для интеграции модели Qwen Qwen-2.5 в систему генерации текста. Он использует асинхронные запросы для взаимодействия с API и обеспечивает потоковую передачу сгенерированного текста. Поддерживает настройку системных сообщений, что позволяет задавать контекст для генерации текста.

## Классы

### `Qwen_Qwen_2_5`

**Описание**: Класс `Qwen_Qwen_2_5` реализует асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Позволяет использовать общие методы и атрибуты для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, `"Qwen Qwen-2.5"`.
- `url` (str): URL сервиса Hugging Face Space, `"https://qwen-qwen2-5.hf.space"`.
- `api_endpoint` (str): URL API для присоединения к очереди, `"https://qwen-qwen2-5.hf.space/queue/join"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, `True`.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи, `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений, `True`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений, `False`.
- `default_model` (str): Модель по умолчанию, `"qwen-qwen2-5"`.
- `model_aliases` (dict): Псевдонимы моделей, `{"qwen-2.5": default_model}`.
- `models` (list): Список поддерживаемых моделей, `list(model_aliases.keys())`.

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
    Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.5.

    Args:
        model (str): Название используемой модели.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от модели.

    Как работает функция:
    1. Генерирует уникальный идентификатор сессии (`session_hash`) с помощью функции `generate_session_hash`.
    2. Формирует заголовки (`headers_join`) для запроса на присоединение к очереди.
    3. Извлекает системные сообщения из списка сообщений и формирует системный промпт (`system_prompt`).
    4. Формирует запрос (`payload_join`) для отправки на API.
    5. Отправляет POST-запрос на API для присоединения к очереди и получает идентификатор события (`event_id`).
    6. Формирует URL (`url_data`) и заголовки (`headers_data`) для запроса потока данных.
    7. Отправляет GET-запрос для получения потока данных и обрабатывает каждый фрагмент ответа.
    8. Извлекает и фильтрует текстовые фрагменты из JSON-данных, полученных в потоке.
    9. Проверяет наличие сообщений о завершении процесса (`process_completed`) и извлекает окончательный текст ответа.
    10. Возвращает асинхронный генератор, выдающий фрагменты текста.
    
    Блоки логики:
    1.  Генерация session_hash:
        ```
        session_hash_generation --> session_hash
        ```
    2.  Подготовка системного промпта:
        ```
        extract_system_messages --> system_prompt
        ```
    3.  Формирование запроса на подключение:
        ```
        system_prompt, prompt, session_hash --> payload_join
        ```
    4.  Запрос на подключение и получение event_id:
        ```
        payload_join --> event_id
        ```
    5.  Обработка потока данных и извлечение текста:
        ```
        session_hash --> data_stream --> text_fragments
        ```
    6.  Проверка завершения и извлечение финального ответа:
        ```
        data_stream --> final_response
        ```

    Примеры:
        >>> async def run_generator():
        ...     messages = [{"role": "user", "content": "Hello, Qwen!"}]
        ...     async for message in Qwen_Qwen_2_5.create_async_generator(model="qwen-2.5", messages=messages):
        ...         print(message, end="")

    """
    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:10]

    # Generate a unique session hash
    session_hash = generate_session_hash()

    headers_join = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': f'{cls.url}/?__theme=system',
        'content-type': 'application/json',
        'Origin': cls.url,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    # Prepare the prompt
    system_prompt = "\n".join([message["content"] for message in messages if message["role"] == "system"])
    if not system_prompt:
        system_prompt = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
    messages = [message for message in messages if message["role"] != "system"]
    prompt = format_prompt(messages)

    payload_join = {
        "data": [prompt, [], system_prompt, "72B"],
        "event_data": None,
        "fn_index": 3,
        "trigger_id": 25,
        "session_hash": session_hash
    }

    async with aiohttp.ClientSession() as session:
        # Send join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # Prepare data stream request
        url_data = f'{cls.url}/queue/data'

        headers_data = {
            'Accept': 'text/event-stream',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': f'{cls.url}/?__theme=system',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0',
        }

        params_data = {
            'session_hash': session_hash
        }

        # Send data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
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
                                            # Extract the fragment, handling both string and dict types
                                            fragment = item[1]
                                            if isinstance(fragment, dict) and 'text' in fragment:
                                                # For the first chunk, extract only the text part
                                                fragment = fragment['text']
                                            else:
                                                fragment = str(fragment)
                                            
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
                                    # Get the final response text
                                    response_item = output_data[1][0][1]
                                    if isinstance(response_item, dict) and 'text' in response_item:
                                        final_full_response = response_item['text']
                                    else:
                                        final_full_response = str(response_item)
                                    
                                    # Clean up the final response
                                    if isinstance(final_full_response, str) and final_full_response.startswith(full_response):
                                        final_text = final_full_response[len(full_response):]
                                    else:
                                        final_text = final_full_response
                                    
                                    # Yield the remaining part of the final response
                                    if final_text and final_text != full_response:
                                        yield final_text
                            break

                    except json.JSONDecodeError as ex:
                        debug.log("Could not parse JSON:", decoded_line)
```

#### Внутренние функции:
Внутри `create_async_generator` определена внутренняя функция `generate_session_hash`.

#### `generate_session_hash`
```python
    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:10]
```
**Назначение**: Генерирует уникальный идентификатор сессии.

**Параметры**: Отсутствуют.

**Возвращает**: `str`: Уникальный идентификатор сессии, полученный путем удаления дефисов из UUID и взятия первых 10 символов.

**Как работает функция**:
1. Генерирует UUID с помощью `uuid.uuid4()`.
2. Преобразует UUID в строку.
3. Удаляет дефисы из строки UUID.
4. Возвращает первые 10 символов полученной строки.

**Примеры**:

```python
>>> generate_session_hash()
'a1b2c3d4e5'