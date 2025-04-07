# Модуль Bard.py для работы с Bard API от Google

## Обзор

Модуль предоставляет функциональность для взаимодействия с API Bard от Google. Он позволяет отправлять текстовые запросы и получать ответы от модели Palm2. Модуль требует аутентификации и может использовать прокси для обхода географических ограничений.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями, предоставляемыми Google. Он использует библиотеку `requests` для отправки HTTP-запросов и `browser_cookie3` для получения файлов cookie аутентификации из браузера. Модуль также содержит функции для форматирования запросов и обработки ответов от API Bard.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs) -> Generator[str, None, None] | str:
    """
    Создает запрос к API Bard и возвращает ответ.

    Args:
        model (str): Идентификатор модели, используемой для генерации текста.
        messages (list): Список сообщений, составляющих контекст запроса.
                         Каждое сообщение должно быть словарем с ключами 'role' и 'content'.
        stream (bool): Флаг, указывающий, следует ли возвращать ответ в режиме потока.
        **kwargs: Дополнительные параметры запроса, такие как прокси.

    Returns:
        Generator[str, None, None] | str: Ответ от API Bard.

    Raises:
        Exception: Если возникает ошибка при отправке запроса или обработке ответа.

    Как работает функция:
    1. Извлекает cookie аутентификации `__Secure-1PSID` из браузера Chrome.
    2. Форматирует список сообщений в строку, пригодную для отправки в запросе.
    3. Проверяет наличие прокси и выводит предупреждение, если прокси не указан.
    4. Инициализирует параметры `snlm0e`, `conversation_id`, `response_id` и `choice_id`.
    5. Создает сессию `requests.Session` и устанавливает заголовки запроса, включая cookie аутентификации.
    6. Получает значение `snlm0e` из главной страницы Bard, если оно не было инициализировано ранее.
    7. Формирует параметры запроса, включая случайный идентификатор `_reqid`.
    8. Формирует данные запроса, включая отформатированный промпт и параметры разговора.
    9. Отправляет POST-запрос к API Bard и получает ответ.
    10. Извлекает данные чата из ответа и возвращает их.

    ASCII flowchart:

    Начало
    ↓
    Извлечение Cookie
    ↓
    Форматирование Сообщения
    ↓
    Проверка Прокси
    ↓
    Инициализация Параметров
    ↓
    Создание Сессии Requests
    ↓
    Получение SNlM0e
    ↓
    Формирование Параметров Запроса
    ↓
    Формирование Данных Запроса
    ↓
    Отправка POST Запроса
    ↓
    Извлечение Данных Чата
    ↓
    Конец

    Примеры:
    >>> _create_completion(model='Palm2', messages=[{'role': 'user', 'content': 'Hello'}], stream=False)
    <generator object _create_completion at 0x...>
    """
    psid = {cookie.name: cookie.value for cookie in browser_cookie3.chrome(
        domain_name='.google.com')}['__Secure-1PSID']

    formatted = '\n'.join([
        '%s: %s' % (message['role'], message['content']) for message in messages
    ])
    prompt = f'{formatted}\nAssistant:'

    proxy = kwargs.get('proxy', False)
    if proxy == False:
        print('warning!, you did not give a proxy, a lot of countries are banned from Google Bard, so it may not work')

    snlm0e = None
    conversation_id = None
    response_id = None
    choice_id = None

    client = requests.Session()
    client.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'} if proxy else None

    client.headers = {
        'authority': 'bard.google.com',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://bard.google.com',
        'referer': 'https://bard.google.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-same-domain': '1',
        'cookie': f'__Secure-1PSID={psid}'
    }

    snlm0e = re.search(r'SNlM0e\\":\\"(.*?)\\"',
                    client.get('https://bard.google.com/').text).group(1) if not snlm0e else snlm0e

    params = {
        'bl': 'boq_assistant-bard-web-server_20230326.21_p0',
        '_reqid': random.randint(1111, 9999),
        'rt': 'c'
    }

    data = {
        'at': snlm0e,
        'f.req': json.dumps([None, json.dumps([[prompt], None, [conversation_id, response_id, choice_id]])])}

    intents = '.'.join([
        'assistant',
        'lamda',
        'BardFrontendService'
    ])

    response = client.post(f'https://bard.google.com/_/BardChatUi/data/{intents}/StreamGenerate',
                        data=data, params=params)

    chat_data = json.loads(response.content.splitlines()[3])[0][2]
    if chat_data:
        json_chat_data = json.loads(chat_data)

        yield json_chat_data[0][0]
        
    else:
        yield 'error'
```

### `params`

```python
params: str
```

Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.

## Переменные

### `url`

```python
url: str = 'https://bard.google.com'
```

URL-адрес API Bard.

### `model`

```python
model: list = ['Palm2']
```

Список поддерживаемых моделей.

### `supports_stream`

```python
supports_stream: bool = False
```

Флаг, указывающий, поддерживается ли потоковая передача ответов.

### `needs_auth`

```python
needs_auth: bool = True
```

Флаг, указывающий, требуется ли аутентификация для доступа к API.