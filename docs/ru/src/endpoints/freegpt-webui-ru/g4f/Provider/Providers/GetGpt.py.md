# Документация модуля GetGpt.py

## Обзор

Модуль `GetGpt.py` предоставляет реализацию провайдера `GetGpt` для взаимодействия с API `chat.getgpt.world`. Он включает в себя функции для шифрования данных, отправки запросов к API и получения ответов в потоковом режиме.

## Подробней

Модуль предназначен для использования в проекте `hypotez` как один из провайдеров для получения ответов от языковой модели `gpt-3.5-turbo`.
Он содержит функции шифрования данных, необходимых для безопасной передачи запросов к API `chat.getgpt.world`.
Модуль использует библиотеку `requests` для выполнения HTTP-запросов и библиотеку `Crypto` для шифрования данных.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция отправляет запрос к API chat.getgpt.world и возвращает ответ в потоковом режиме.

    Args:
        model (str): Имя модели для использования (например, 'gpt-3.5-turbo').
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли возвращать ответ в потоковом режиме.
        **kwargs: Дополнительные параметры для передачи в API.

    Returns:
        Generator[str, None, None]: Генератор, возвращающий части ответа от API.

    Raises:
        requests.exceptions.RequestException: В случае ошибок при отправке запроса к API.

    Внутренние функции:
        encrypt(e: str) -> str: Шифрует строку с использованием AES.
        pad_data(data: bytes) -> bytes: Дополняет данные до размера блока AES.

    Как работает функция:
    1. Определяет две внутренние функции: `encrypt` и `pad_data`.
    2. Функция `encrypt` шифрует входящие данные с использованием алгоритма AES. Она генерирует случайные значения для ключа и вектора инициализации, дополняет ключ пробелами, если он короткий, создает шифр AES в режиме CBC, шифрует данные и возвращает зашифрованные данные вместе с ключом и вектором инициализации.
    3. Функция `pad_data` дополняет входящие данные до размера блока, требуемого алгоритмом AES, добавляя байты с информацией о размере дополнения.
    4. Создаются заголовки HTTP-запроса, включая `Content-Type`, `Referer` и `User-Agent`.
    5. Данные запроса формируются в формате JSON, включая сообщения, параметры модели и другие параметры, переданные через `kwargs`.
    6. Сформированные данные шифруются с использованием функции `encrypt` и оборачиваются в JSON для отправки POST-запроса.
    7. Отправляется POST-запрос к API `chat.getgpt.world/api/chat/stream` с использованием библиотеки `requests`.
    8. Обрабатывается потоковый ответ от API, извлекая содержимое каждого чанка данных и возвращая его через генератор.

    ASCII Flowchart:

    messages, kwargs
    |
    -- JSON data
    |
    encrypt(data)
    |
    signature in JSON
    |
    POST request -> chat.getgpt.world/api/chat/stream
    |
    Iterate over stream -> extract content
    |
    yield content

    Примеры:
        >>> messages = [{"role": "user", "content": "Hello, world!"}]
        >>> for chunk in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
        ...     print(chunk, end='')
        Hello, world!
    """

    def encrypt(e: str) -> str:
        """ Шифрует строку с использованием AES.

        Args:
            e (str): Строка для шифрования.

        Returns:
            str: Зашифрованная строка.

        Как работает функция:
        1. Генерирует случайные значения для ключа `t` и вектора инициализации `n` в формате hex.
        2. Преобразует строку `e` в байты.
        3. Создает шифр AES в режиме CBC с использованием ключа `t` и вектора инициализации `n`.
        4. Дополняет данные с использованием функции `pad_data`.
        5. Шифрует дополненные данные и возвращает зашифрованную строку в формате hex, добавляя ключ и вектор инициализации.
        """
        ...

    def pad_data(data: bytes) -> bytes:
        """ Дополняет данные до размера блока AES.

        Args:
            data (bytes): Данные для дополнения.

        Returns:
            bytes: Дополненные данные.

        Как работает функция:
        1. Определяет размер блока AES.
        2. Вычисляет размер дополнения, необходимого для достижения размера блока.
        3. Создает байтовую строку, содержащую байты, указывающие на размер дополнения.
        4. Добавляет строку дополнения к данным и возвращает результат.
        """
        ...

    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://chat.getgpt.world/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    data = json.dumps({
        'messages': messages,
        'frequency_penalty': kwargs.get('frequency_penalty', 0),
        'max_tokens': kwargs.get('max_tokens', 4000),
        'model': 'gpt-3.5-turbo',
        'presence_penalty': kwargs.get('presence_penalty', 0),
        'temperature': kwargs.get('temperature', 1),
        'top_p': kwargs.get('top_p', 1),
        'stream': True,
        'uuid': str(uuid.uuid4())
    })

    res = requests.post('https://chat.getgpt.world/api/chat/stream',
                        headers=headers, json={'signature': encrypt(data)}, stream=True)

    for line in res.iter_lines():
        if b'content' in line:
            line_json = json.loads(line.decode('utf-8').split('data: ')[1])
            yield (line_json['choices'][0]['delta']['content'])

## Переменные

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f'{name}: {get_type_hints(_create_completion)[name].__name__}' for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Содержит строку с информацией о поддержке параметров функцией `_create_completion`. Используется для документирования поддерживаемых параметров провайдера.