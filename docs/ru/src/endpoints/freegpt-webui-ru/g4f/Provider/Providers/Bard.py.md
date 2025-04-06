# Модуль для работы с Google Bard

## Обзор

Модуль предоставляет функциональность для взаимодействия с Google Bard, используя cookies для аутентификации. Он включает в себя функцию для создания запросов к Bard и получения ответов.

## Подробнее

Этот модуль предназначен для интеграции с Google Bard, позволяя отправлять текстовые запросы и получать ответы, используя API Bard. Модуль использует cookies для аутентификации, что позволяет обходить некоторые ограничения доступа. Важно отметить, что для работы модуля требуется действующий прокси-сервер, так как Google Bard может быть недоступен в некоторых странах.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к Google Bard и возвращает ответ.

    Args:
        model (str): Название используемой модели.
        messages (list): Список сообщений для отправки в Bard.
        stream (bool): Флаг, указывающий, использовать ли потоковый режим.
        **kwargs: Дополнительные аргументы, такие как proxy.

    Returns:
        Generator[str, None, None]: Генератор, выдающий части ответа от Bard.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса.

    Как работает функция:
    1. Извлекает cookie '__Secure-1PSID' из браузера Chrome для аутентификации.
    2. Форматирует список сообщений в строку, пригодную для отправки в Bard.
    3. Проверяет наличие прокси-сервера и выводит предупреждение, если он не указан.
    4. Инициализирует параметры 'snlm0e', 'conversation_id', 'response_id', 'choice_id'.
    5. Создает сессию requests и устанавливает прокси, если он предоставлен.
    6. Устанавливает заголовки для запроса, включая cookie.
    7. Получает значение 'SNlM0e' из главной страницы Bard.
    8. Формирует параметры запроса.
    9. Формирует данные запроса, включая отформатированный prompt.
    10. Отправляет POST-запрос к Bard API.
    11. Извлекает и генерирует ответ из полученных данных.
    12. В случае ошибки возвращает 'error'.

    ASCII flowchart:

    Получение cookie  __Secure-1PSID
        ↓
    Форматирование сообщений
        ↓
    Проверка прокси
        ↓
    Инициализация параметров
        ↓
    Создание сессии requests
        ↓
    Установка заголовков
        ↓
    Получение SNlM0e
        ↓
    Формирование параметров запроса
        ↓
    Формирование данных запроса
        ↓
    Отправка POST-запроса
        ↓
    Извлечение и генерация ответа
        ↓
    Конец

    Примеры:
        >>> messages = [{'role': 'user', 'content': 'Hello, Bard!'}]
        >>> for response in _create_completion(model='Palm2', messages=messages, stream=False):
        ...     print(response)
        Привет, как я могу помочь вам сегодня?
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
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Назначение**:
Формирует строку с информацией о поддержке параметров функцией `_create_completion`.

**Как работает функция**:
1.  Извлекает имя текущего файла модуля без расширения `.py`.
2.  Получает аннотации типов параметров функции `_create_completion`.
3.  Формирует строку, содержащую информацию о поддерживаемых параметрах и их типах.

**Примеры**:

```python
print(params) # g4f.Providers.Bard supports: (model: str, messages: list, stream: bool, kwargs: dict)