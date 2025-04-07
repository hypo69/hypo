# Модуль для работы с провайдером H2o
=================================================

Модуль содержит функции для взаимодействия с H2o AI моделями, такими как `falcon-40b`, `falcon-7b` и `llama-13b`.
Он предоставляет возможность отправлять запросы к моделям и получать ответы в потоковом режиме.

## Обзор

Модуль `H2o.py` предоставляет функциональность для взаимодействия с моделями H2o AI через API `gpt-gm.h2o.ai`.
Он поддерживает потоковую передачу ответов и не требует аутентификации. Модуль определяет список поддерживаемых моделей и
содержит функцию `_create_completion` для создания и отправки запросов к API.

## Подробней

Модуль предназначен для интеграции с другими частями проекта `hypotez`, которые требуют взаимодействия с AI-моделями H2o.
Он использует библиотеку `requests` для отправки HTTP-запросов и `uuid` для генерации уникальных идентификаторов.
Модуль также использует модуль `logger` из `src.logger` для логирования ошибок и отладочной информации.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает и отправляет запрос к H2o AI моделям для получения ответа.

    Args:
        model (str): Название модели для использования (например, 'falcon-40b').
        messages (list): Список сообщений в формате [{"role": "user" | "assistant", "content": "text"}].
        stream (bool): Флаг, указывающий, следует ли возвращать ответ в потоковом режиме.
        **kwargs: Дополнительные параметры для запроса, такие как temperature, truncate, max_new_tokens и др.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа, если stream=True.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса.

    Как работает функция:
    1. Формирует строку conversation из списка сообщений, добавляя префиксы "user:" и "assistant:".
    2. Создает HTTP-клиент `Session` и устанавливает заголовки для запроса.
    3. Выполняет GET-запрос к `https://gpt-gm.h2o.ai/` для установки cookies.
    4. Выполняет POST-запрос к `https://gpt-gm.h2o.ai/settings` для принятия настроек.
    5. Выполняет POST-запрос к `https://gpt-gm.h2o.ai/conversation` для получения conversationId.
    6. Выполняет POST-запрос к `https://gpt-gm.h2o.ai/conversation/{conversationId}` с conversation, parameters и options.
    7. В цикле читает ответ в потоковом режиме и извлекает токены.
    8. Возвращает токен, если он не равен '<|endoftext|>'.

    ASCII flowchart:

    FormConversation --> CreateClient --> GetCookies --> PostSettings --> GetConversationId --> CompletionRequest --> IterLines --> ExtractToken --> YieldToken

    Примеры:
    Пример 1:
    >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
    >>> for token in _create_completion(model='falcon-7b', messages=messages, stream=True):
    ...     print(token, end='')

    Пример 2:
    >>> messages = [{"role": "user", "content": "Tell me a joke."}]
    >>> for token in _create_completion(model='falcon-40b', messages=messages, stream=True, temperature=0.7):
    ...     print(token, end='')
    """
    conversation = 'instruction: this is a conversation beween, a user and an AI assistant, respond to the latest message, referring to the conversation if needed\n'
    for message in messages:
        conversation += '%s: %s\n' % (message['role'], message['content'])
    conversation += 'assistant:'
    
    client = Session()
    client.headers = {
        'authority': 'gpt-gm.h2o.ai',
        'origin': 'https://gpt-gm.h2o.ai',
        'referer': 'https://gpt-gm.h2o.ai/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    client.get('https://gpt-gm.h2o.ai/')
    response = client.post('https://gpt-gm.h2o.ai/settings', data={
        'ethicsModalAccepted': 'true',
        'shareConversationsWithModelAuthors': 'true',
        'ethicsModalAcceptedAt': '',
        'activeModel': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1',
        'searchEnabled': 'true',
    })

    headers = {
        'authority': 'gpt-gm.h2o.ai',
        'accept': '*/*',
        'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
        'origin': 'https://gpt-gm.h2o.ai',
        'referer': 'https://gpt-gm.h2o.ai/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    json_data = {
        'model': models[model]
    }

    response = client.post('https://gpt-gm.h2o.ai/conversation',
                            headers=headers, json=json_data)
    conversationId = response.json()['conversationId']


    completion = client.post(f'https://gpt-gm.h2o.ai/conversation/{conversationId}', stream=True, json = {
        'inputs': conversation,
        'parameters': {
            'temperature': kwargs.get('temperature', 0.4),
            'truncate': kwargs.get('truncate', 2048),
            'max_new_tokens': kwargs.get('max_new_tokens', 1024),
            'do_sample': kwargs.get('do_sample', True),
            'repetition_penalty': kwargs.get('repetition_penalty', 1.2),
            'return_full_text': kwargs.get('return_full_text', False)
        },
        'stream': True,
        'options': {
            'id': kwargs.get('id', str(uuid4())),
            'response_id': kwargs.get('response_id', str(uuid4())),
            'is_retry': False,
            'use_cache': False,
            'web_search_id': ''
        }
    })

    for line in completion.iter_lines():
        if b'data' in line:
            line = loads(line.decode('utf-8').replace('data:', ''))
            token = line['token']['text']
            
            if token == '<|endoftext|>':
                break
            else:
                yield (token)

```

### `params`

```python
params: str
```

Строка, содержащая информацию о поддерживаемых параметрах функцией `_create_completion`.

## Переменные

### `url`

```python
url: str = 'https://gpt-gm.h2o.ai'
```
URL для взаимодействия с H2o AI API.

### `model`

```python
model: list = ['falcon-40b', 'falcon-7b', 'llama-13b']
```

Список поддерживаемых моделей H2o AI.

### `supports_stream`

```python
supports_stream: bool = True
```

Флаг, указывающий, поддерживает ли провайдер потоковую передачу ответов.

### `needs_auth`

```python
needs_auth: bool = False
```

Флаг, указывающий, требуется ли аутентификация для взаимодействия с провайдером.

### `models`

```python
models: Dict[str, str] = {
    'falcon-7b': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3',
    'falcon-40b': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1',
    'llama-13b': 'h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b'
}
```

Словарь, сопоставляющий названия моделей с их идентификаторами в H2o AI API.