# Модуль для взаимодействия с Qwen Qwen-2.72B через HF Space
## Обзор

Модуль предоставляет асинхронный интерфейс для взаимодействия с моделью Qwen Qwen-2.72B, размещенной на HF Space. Он позволяет отправлять запросы к модели и получать ответы в режиме реального времени, используя асинхронные генераторы.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими компонентами, требующими доступа к языковой модели Qwen Qwen-2.72B. Он использует библиотеки `aiohttp` и `json` для асинхронного взаимодействия с API HF Space. Модуль поддерживает потоковую передачу данных, что позволяет получать ответы от модели по мере их генерации.
Расположение файла в проекте: `hypotez/src/endpoints/gpt4free/g4f/Provider/hf_space/Qwen_Qwen_2_72B.py`

## Классы

### `Qwen_Qwen_2_72B`

**Описание**: Класс реализует асинхронного провайдера для модели Qwen Qwen-2.72B, размещенной на HF Space.

**Принцип работы**:
Класс использует методы `aiohttp` для отправки асинхронных запросов к API HF Space. Он генерирует уникальный идентификатор сессии для каждого запроса и использует его для получения потока данных от модели. Полученные данные обрабатываются и передаются пользователю в виде асинхронного генератора.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных провайдеров, генерирующих данные.
- `ProviderModelMixin`: Предоставляет общие методы для работы с моделями.

**Аттрибуты**:
- `label` (str): Метка провайдера ("Qwen Qwen-2.72B").
- `url` (str): URL HF Space, где размещена модель ("https://qwen-qwen2-72b-instruct.hf.space").
- `api_endpoint` (str): URL API для присоединения к очереди запросов ("https://qwen-qwen2-72b-instruct.hf.space/queue/join?").
- `working` (bool): Флаг, указывающий, работает ли провайдер (True).
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных (True).
- `supports_system_message` (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений (False).
- `default_model` (str): Модель, используемая по умолчанию ("qwen-qwen2-72b-instruct").
- `model_aliases` (dict): Псевдонимы моделей ({"qwen-2-72b": default_model}).
- `models` (list): Список доступных моделей.

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
    """Создает асинхронный генератор для получения ответов от модели Qwen Qwen-2.72B.

    Args:
        cls (Qwen_Qwen_2_72B): Класс провайдера.
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
        **kwargs: Дополнительные параметры.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий ответы от модели.

    **Как работает функция**:

    1. **Генерация уникального идентификатора сессии**: Генерирует уникальный идентификатор сессии (`session_hash`) для каждого запроса.
    2. **Подготовка заголовков и полезной нагрузки**: Подготавливает заголовки (`headers_join`) и полезную нагрузку (`payload_join`) для отправки запроса на присоединение к очереди обработки запросов.
    3. **Формирование системного запроса**:  Извлекает системные сообщения и формирует запрос к модели.
    4. **Отправка запроса на присоединение**: Отправляет POST-запрос к API HF Space для присоединения к очереди обработки запросов.
    5. **Подготовка параметров для потока данных**: Подготавливает URL (`url_data`), заголовки (`headers_data`) и параметры (`params_data`) для запроса потока данных.
    6. **Отправка запроса на получение потока данных**: Отправляет GET-запрос для получения потока данных от модели.
    7. **Обработка потока данных**: Читает поток данных построчно, декодирует строки и извлекает полезную информацию из JSON-ответов.
    8. **Извлечение фрагментов текста**: Извлекает фрагменты текста из ответов модели и передает их через асинхронный генератор.
    9. **Обработка завершения генерации**: Определяет момент завершения генерации ответа и извлекает окончательный текст ответа.
    10. **Очистка и проверка финального ответа**: Очищает финальный ответ, удаляя повторяющиеся или неполные фрагменты, и передает его через генератор.

    **Внутренние функции**:

    ### `generate_session_hash`
    ```python
    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:12]
    ```
    **Назначение**: Генерирует уникальный идентификатор сессии.
    **Как работает функция**: Преобразует UUID в строку, удаляет дефисы и оставляет первые 12 символов.

    **Примеры**:

    ```python
    # Пример использования create_async_generator
    import asyncio
    from src.endpoints.gpt4free.g4f.Provider.hf_space.Qwen_Qwen_2_72B import Qwen_Qwen_2_72B
    from src.endpoints.gpt4free.g4f.typing import Messages

    async def main():
        messages: Messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
        async for response in Qwen_Qwen_2_72B.create_async_generator("qwen-2-72b", messages):
            print(response, end="")

    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """

    def generate_session_hash():
        """Generate a unique session hash."""
        return str(uuid.uuid4()).replace('-', '')[:12]

    # Генерируем уникальный session_hash
    session_hash = generate_session_hash()

    headers_join = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': f'{cls.url}',
        'referer': f'{cls.url}/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    # Подготавливаем prompt
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
        # Отправляем join request
        async with session.post(cls.api_endpoint, headers=headers_join, json=payload_join) as response:
            event_id = (await response.json())['event_id']

        # Подготавливаем data stream request
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

        # Отправляем data stream request
        async with session.get(url_data, headers=headers_data, params=params_data) as response:
            full_response = ""
            final_full_response = ""
            async for line in response.content:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    try:
                        json_data = json.loads(decoded_line[6:])

                        # Ищем generation stages
                        if json_data.get('msg') == 'process_generating':
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    for item in output_data[1]:
                                        if isinstance(item, list) and len(item) > 1:
                                            fragment = str(item[1])
                                            # Игнорируем [0, 1] type fragments и дубликаты
                                            if not re.match(r'^\\[.*\\]$', fragment) and not full_response.endswith(fragment):
                                                full_response += fragment
                                                yield fragment

                        # Проверяем completion
                        if json_data.get('msg') == 'process_completed':
                            # Final check для получения complete response
                            if 'output' in json_data and 'data' in json_data['output']:
                                output_data = json_data['output']['data']
                                if len(output_data) > 1 and len(output_data[1]) > 0:
                                    final_full_response = output_data[1][0][1]

                                    # Clean up final response
                                    if final_full_response.startswith(full_response):
                                        final_full_response = final_full_response[len(full_response):]

                                    # Yield remaining part of final response
                                    if final_full_response:
                                        yield final_full_response
                                break

                    except json.JSONDecodeError:
                        debug.log("Could not parse JSON:", decoded_line)

```
**Как работает функция**:

```
    [Начало]
     │
     │  Генерация session_hash
     │
     ▼
    [Подготовка запроса на подключение]
     │
     │  Формирование headers_join, payload_join
     │
     ▼
    [Отправка запроса на подключение]
     │
     │  POST запрос к api_endpoint
     │
     ▼
    [Получение event_id]
     │
     │  Извлечение event_id из ответа
     │
     ▼
    [Подготовка запроса данных]
     │
     │  Формирование url_data, headers_data, params_data
     │
     ▼
    [Отправка запроса данных]
     │
     │  GET запрос к url_data
     │
     ▼
    [Обработка потока данных]
     │
     │  Чтение и декодирование строк
     │
     ▼
    [Анализ JSON]
     │
     │  Поиск 'process_generating' и 'process_completed'
     │
     ▼
    [Извлечение фрагментов текста]
     │
     │  Выделение и фильтрация fragment
     │
     ▼
    [Вывод результата]
     │
     │  yield fragment
     │
     ▼
    [Завершение]