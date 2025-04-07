# Модуль `Liaobots.py`

## Обзор

Модуль `Liaobots.py` предоставляет интерфейс для взаимодействия с сервисом Liaobots, который предлагает доступ к моделям GPT-3.5 и GPT-4. Модуль определяет конфигурацию моделей, поддерживает потоковую передачу данных и требует аутентификацию.

## Подробней

Модуль содержит информацию о поддерживаемых моделях (`gpt-3.5-turbo`, `gpt-4`), их параметрах (максимальная длина и лимит токенов), а также функцию `_create_completion`, которая отправляет запросы к API Liaobots и возвращает ответы в потоковом режиме.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция отправляет запрос к API Liaobots для генерации текста на основе предоставленных сообщений и параметров.

    Args:
        model (str): Идентификатор модели для использования (например, 'gpt-3.5-turbo' или 'gpt-4').
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        **kwargs: Дополнительные аргументы, включая ключ аутентификации (`auth`).

    Returns:
        Generator[str, None, None]: Генератор токенов, полученных от API.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при отправке запроса к API.

    **Как работает функция**:

    1. **Подготовка заголовков**: Функция создает заголовки HTTP-запроса, включая `authority`, `content-type`, `origin`, `referer`, `user-agent` и `x-auth-code` (ключ аутентификации).
    2. **Формирование данных JSON**: Функция формирует JSON-данные для отправки в API, включая `conversationId` (уникальный идентификатор разговора), `model` (информация о модели), `messages` (список сообщений), `key` (пустая строка) и `prompt` (инструкция для модели).
    3. **Отправка POST-запроса**: Функция отправляет POST-запрос к API `https://liaobots.com/api/chat` с использованием библиотеки `requests`.
    4. **Обработка потока ответов**: Функция итерирует по содержимому ответа, полученного от API, с заданным размером чанка (2046 байт).
    5. **Декодирование и выдача токенов**: Каждый чанк декодируется из UTF-8 и выдается как токен через генератор.

    **Внутренние функции**:
    Внутри функции `_create_completion` не определены внутренние функции.

    **Flowchart**:

    ```
    Начало
     ↓
    Подготовка заголовков HTTP-запроса
     ↓
    Формирование JSON-данных для запроса
     ↓
    Отправка POST-запроса к API Liaobots
     ↓
    Итерация по содержимому ответа (по чанкам)
     ↓
    Декодирование чанка из UTF-8
     ↓
    Выдача токена через генератор
     ↓
    Конец (пока есть токены)
    ```
    **Примеры**:

    1.  Вызов функции с моделью `gpt-3.5-turbo` и списком сообщений:

        ```python
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        stream = True
        kwargs = {"auth": "your_auth_key"}

        for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=stream, **kwargs):
            print(token, end="")
        ```

    2.  Вызов функции с моделью `gpt-4` и пустым списком сообщений:

        ```python
        messages = []
        stream = False
        kwargs = {"auth": "your_auth_key"}

        for token in _create_completion(model='gpt-4', messages=messages, stream=stream, **kwargs):
            print(token, end="")
        ```
    """
    print(kwargs)

    headers = {
        'authority': 'liaobots.com',
        'content-type': 'application/json',
        'origin': 'https://liaobots.com',
        'referer': 'https://liaobots.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-auth-code': kwargs.get('auth')
    }

    json_data = {
        'conversationId': str(uuid.uuid4()),
        'model': models[model],
        'messages': messages,
        'key': '',
        'prompt': "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
    }

    response = requests.post('https://liaobots.com/api/chat',
                             headers=headers, json=json_data, stream=True)

    for token in response.iter_content(chunk_size=2046):
        yield (token.decode('utf-8'))
```

## Переменные

-   `url`: URL сервиса Liaobots (`https://liaobots.com`).
-   `model`: Список поддерживаемых моделей (`['gpt-3.5-turbo', 'gpt-4']`).
-   `supports_stream`: Флаг, указывающий на поддержку потоковой передачи данных (`True`).
-   `needs_auth`: Флаг, указывающий на необходимость аутентификации (`True`).
-   `models`: Словарь, содержащий информацию о поддерживаемых моделях, включая их идентификаторы, имена, максимальную длину и лимит токенов.
-   `params`: Строка, формирующая описание поддерживаемых параметров для функции `_create_completion`.