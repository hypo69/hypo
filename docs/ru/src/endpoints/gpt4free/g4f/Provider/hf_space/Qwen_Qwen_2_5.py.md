# Модуль `Qwen_Qwen_2_5`

## Обзор

Модуль `Qwen_Qwen_2_5` предоставляет асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5 через Hugging Face Space. Он поддерживает потоковую передачу данных, системные сообщения и предоставляет базовые функции для работы с моделью. Модуль использует `aiohttp` для асинхронных HTTP-запросов и `json` для обработки JSON-данных.

## Подробнее

Модуль предназначен для асинхронного взаимодействия с моделью Qwen Qwen-2.5, размещенной на Hugging Face Space. Он обеспечивает возможность отправки запросов к модели и получения ответов в режиме реального времени благодаря поддержке потоковой передачи данных.
Модуль может быть использован для интеграции с другими системами, требующими асинхронного взаимодействия с языковой моделью Qwen Qwen-2.5.

## Классы

### `Qwen_Qwen_2_5`

**Описание**: Класс `Qwen_Qwen_2_5` реализует асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5.

**Наследует**:
- `AsyncGeneratorProvider`: Предоставляет базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями провайдера.

**Атрибуты**:
- `label` (str): Метка провайдера, значение: `"Qwen Qwen-2.5"`.
- `url` (str): URL Hugging Face Space, значение: `"https://qwen-qwen2-5.hf.space"`.
- `api_endpoint` (str): URL API для присоединения к очереди, значение: `"https://qwen-qwen2-5.hf.space/queue/join"`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера, значение: `True`.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных, значение: `True`.
- `supports_system_message` (bool): Флаг, указывающий на поддержку системных сообщений, значение: `True`.
- `supports_message_history` (bool): Флаг, указывающий на поддержку истории сообщений, значение: `False`.
- `default_model` (str): Модель по умолчанию, значение: `"qwen-qwen2-5"`.
- `model_aliases` (dict): Псевдонимы моделей, значение: `{"qwen-2.5": default_model}`.
- `models` (list): Список поддерживаемых моделей, значение: `list(model_aliases.keys())`.

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
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для взаимодействия с моделью Qwen Qwen-2.5.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в модель.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, который возвращает ответы от модели.

    Как работает функция:
    1. **Генерация уникального идентификатора сессии (`session_hash`)**:
       - Функция `generate_session_hash` генерирует случайный UUID и преобразует его в строку, убирая дефисы и обрезая до 10 символов.
    2. **Подготовка заголовков для запроса (`headers_join`)**:
       - Формируются HTTP-заголовки, которые будут отправлены вместе с запросом на сервер. Заголовки включают `User-Agent`, `Accept`, `Accept-Language`, `Accept-Encoding`, `Referer`, `content-type`, `Origin`, `Connection`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site`, `Pragma` и `Cache-Control`.
    3. **Подготовка содержимого запроса (`payload_join`)**:
       - Из списка сообщений извлекается системное сообщение (если оно есть) и формируется запрос к модели. Системное сообщение используется для установки контекста для модели. Если системное сообщение отсутствует, используется сообщение по умолчанию.
       - Подготавливается полезная нагрузка (payload) для отправки запроса, включающая prompt, пустой список, системное сообщение, константу `"72B"`, `event_data`, `fn_index`, `trigger_id` и сгенерированный `session_hash`.
    4. **Отправка запроса на присоединение и получение `event_id`**:
       - Отправляется POST-запрос к `api_endpoint` с использованием `aiohttp.ClientSession`.
       - Полученный ответ преобразуется в JSON, из которого извлекается `event_id`.
    5. **Подготовка параметров для запроса потока данных (`headers_data`, `params_data`)**:
       - Формируются заголовки (`headers_data`) и параметры (`params_data`) для запроса потока данных. Заголовки включают `Accept`, `Accept-Language`, `Referer` и `User-Agent`. Параметры включают `session_hash`.
    6. **Отправка запроса потока данных и обработка ответов**:
       - Отправляется GET-запрос к `url_data` с использованием `aiohttp.ClientSession`.
       - Полученные данные построчно декодируются из формата `utf-8`.
       - Если строка начинается с `data: `, то извлекается JSON-данные из этой строки.
       - Если `json_data` содержит сообщение `process_generating`, то извлекается фрагмент текста из `output_data` и передается в генератор.
       - Если `json_data` содержит сообщение `process_completed`, то извлекается окончательный текст ответа из `output_data`, очищается от дубликатов и передается в генератор.
       - В случае ошибки декодирования JSON, информация об ошибке логируется.

    7. **Обработка фрагментов текста**:
       - Для каждого фрагмента текста проверяется, чтобы он не был дубликатом и не соответствовал определенному шаблону (например, `[0, 1]`). Это нужно, чтобы избежать повторов и лишних данных в ответе.
    8. **Завершение**:
       - Когда приходит сообщение о завершении (`process_completed`), извлекается итоговый текст, удаляются лишние части (например, префикс, который уже был выдан ранее), и остаток текста выдается через `yield`.

    Raises:
        aiohttp.ClientError: Если возникает ошибка при выполнении HTTP-запроса.
        json.JSONDecodeError: Если не удается декодировать JSON-ответ.
    """

    def generate_session_hash() -> str:
        """Генерирует уникальный идентификатор сессии.

        Returns:
            str: Уникальный идентификатор сессии.
        """
        return str(uuid.uuid4()).replace('-', '')[:10]

    # ASII flowchart функции:

    # Генерация session_hash
    #      |
    # Подготовка headers_join, payload_join
    #      |
    # Отправка POST запроса на api_endpoint -> response
    #      |
    # Извлечение event_id из response
    #      |
    # Подготовка headers_data, params_data
    #      |
    # Отправка GET запроса на url_data -> response
    #      |
    # Обработка каждой строки из response.content
    #      |
    # Проверка decoded_line.startswith('data: ')
    #      |
    # Извлечение json_data
    #      |
    # Проверка json_data.get('msg') == 'process_generating' или 'process_completed'
    #      |
    # Извлечение и фильтрация фрагментов текста из json_data
    #      |
    # Выдача фрагмента текста через yield
    #      |
    # Завершение

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
        "session_hash": generate_session_hash()
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
            'session_hash': generate_session_hash()
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

    """
    ```
    Примеры:
    ```python
    # Пример вызова функции create_async_generator
    import asyncio
    
    async def main():
        model = "qwen-2.5"
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ]
        
        generator = await Qwen_Qwen_2_5.create_async_generator(model=model, messages=messages)
        
        async for message in generator:
            print(message, end="")
    
    if __name__ == "__main__":
        asyncio.run(main())