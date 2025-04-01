# Модуль `Liaobots.py`

## Обзор

Модуль предоставляет интерфейс для взаимодействия с провайдером Liaobots, который использует модели GPT-3.5-turbo и GPT-4. Он включает в себя функции для создания запросов к API Liaobots и получения ответов в потоковом режиме. Модуль требует аутентификации и поддерживает стриминг ответов.

## Подробней

Этот модуль предназначен для интеграции с сервисом Liaobots, позволяя использовать их модели GPT для генерации текста. Он определяет параметры подключения, необходимые заголовки и структуру запросов. Также модуль обрабатывает ответы от API, предоставляя их в удобном для дальнейшей обработки формате.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к API Liaobots и возвращает ответ в потоковом режиме.

    Args:
        model (str): Идентификатор используемой модели (например, 'gpt-3.5-turbo' или 'gpt-4').
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, нужно ли возвращать ответ в потоковом режиме.
        **kwargs: Дополнительные аргументы, такие как параметры аутентификации.

    Returns:
        Generator[str, None, None]: Генератор токенов ответа в формате UTF-8.

    Как работает функция:
    1. Функция принимает на вход идентификатор модели (`model`), список сообщений (`messages`), флаг потоковой передачи (`stream`) и дополнительные аргументы (`kwargs`).
    2. Определяются заголовки (`headers`) для HTTP-запроса, включая информацию об источнике запроса и параметры аутентификации.
    3. Формируется JSON-тело запроса (`json_data`), включающее идентификатор диалога, выбранную модель, сообщения, ключ API и начальный промт.
    4. Отправляется POST-запрос к API Liaobots (`https://liaobots.com/api/chat`) с использованием указанных заголовков и JSON-данных.
    5. Функция итерируется по содержимому ответа (`response.iter_content`) и генерирует токены ответа в формате UTF-8.

    Внутренние функции:
    - Нет внутренних функций.

    ASCII flowchart:
    Начало --> Заголовки --> JSON_данные --> POST_запрос --> Итерация_по_ответу --> Генерация_токенов --> Конец

    Примеры:
    ```python
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    auth_key = "your_auth_key"  # Замените на ваш реальный ключ аутентификации

    # Пример вызова функции с потоковой передачей
    generator = _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True, auth=auth_key)
    for token in generator:
        print(token, end="")

    # Пример вызова функции без потоковой передачи (если это поддерживается вашей реализацией)
    # response = _create_completion(model='gpt-3.5-turbo', messages=messages, stream=False, auth=auth_key)
    # print(response)
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

### `url`

```python
url = 'https://liaobots.com'
```
URL адрес сервиса Liaobots.

### `model`

```python
model = ['gpt-3.5-turbo', 'gpt-4']
```
Список поддерживаемых моделей.

### `supports_stream`

```python
supports_stream = True
```
Указывает, поддерживает ли провайдер потоковую передачу ответов.

### `needs_auth`

```python
needs_auth = True
```
Указывает, требуется ли аутентификация для работы с провайдером.

### `models`

```python
models = {
    'gpt-4': {
        "id":"gpt-4",
        "name":"GPT-4",
        "maxLength":24000,
        "tokenLimit":8000
    },
    'gpt-3.5-turbo': {
        "id":"gpt-3.5-turbo",
        "name":"GPT-3.5",
        "maxLength":12000,
        "tokenLimit":4000
    },
}
```
Словарь, содержащий информацию о поддерживаемых моделях, включая их идентификаторы, названия, максимальную длину и ограничение на количество токенов.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```
Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.