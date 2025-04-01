# Модуль `FastGpt`

## Обзор

Модуль `FastGpt` предоставляет класс `FastGpt`, который является провайдером для работы с сервисом `chat9.fastgpt.me`. Этот сервис предоставляет API для создания и обработки чат-комплишенов, аналогичных OpenAI. Модуль поддерживает потоковую передачу данных, а также модели `gpt-3.5-turbo`.

## Подробней

Данный модуль используется для интеграции с сервисом FastGpt. Он позволяет отправлять запросы на генерацию текста и получать ответы в режиме реального времени благодаря поддержке потоковой передачи. Класс `FastGpt` наследуется от `AbstractProvider`, что позволяет единообразно использовать его в рамках общей архитектуры провайдеров.

## Классы

### `FastGpt(AbstractProvider)`

**Описание**: Класс `FastGpt` является провайдером для работы с сервисом `chat9.fastgpt.me`.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для всех провайдеров.

**Аттрибуты**:
- `url` (str): URL сервиса `chat9.fastgpt.me`.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (по умолчанию `False`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (по умолчанию `False`).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи (по умолчанию `True`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo` (по умолчанию `True`).
- `supports_gpt_4` (bool): Флаг, указывающий на поддержку модели `gpt-4` (по умолчанию `False`).

**Методы**:
- `create_completion()`: Статический метод для создания комплишенов.

## Функции

### `create_completion`

```python
@staticmethod
def create_completion(
    model: str,
    messages: list[dict[str, str]],
    stream: bool, **kwargs: Any) -> CreateResult:
    """
    Функция создает комплишены, отправляя запросы к API `chat9.fastgpt.me`.

    Args:
        model (str): Имя модели для использования.
        messages (list[dict[str, str]]): Список сообщений в формате словарей.
        stream (bool): Флаг, указывающий на необходимость потоковой передачи.
        **kwargs (Any): Дополнительные параметры запроса.

    Returns:
        CreateResult: Результат создания комплишена. Является генератором токенов.

    Как работает функция:
    1. Формирует заголовки запроса (`headers`) для отправки к API `chat9.fastgpt.me`.
    2. Формирует JSON-данные (`json_data`) для запроса, включая сообщения, модель, параметры температуры, и т.д.
    3. Выбирает случайный поддомен (`subdomain`) из списка `['jdaen979ew', 'chat9']`.
    4. Отправляет POST-запрос к API с использованием `requests.post`.
    5. Итерируется по строкам ответа, полученного от API.
    6. Если строка содержит данные (`content`), пытается извлечь токен из JSON.
    7. Если токен успешно извлечен, передает его через `yield`.
    8. В случае возникновения исключения при обработке строки, пропускает её.

    ASCII flowchart:
    A [Формирование заголовков запроса]
    ↓
    B [Формирование JSON-данных]
    ↓
    C [Выбор случайного поддомена]
    ↓
    D [Отправка POST-запроса к API]
    ↓
    E [Итерация по строкам ответа]
    ↓
    F [Проверка наличия данных в строке]
    ↓
    G [Извлечение токена из JSON]
    ↓
    H [Передача токена через yield]

    Примеры:
    - Создание комплишена с использованием потоковой передачи:
        >>> model = "gpt-3.5-turbo"
        >>> messages = [{"role": "user", "content": "Hello, world!"}]
        >>> stream = True
        >>> result = FastGpt.create_completion(model, messages, stream)
        >>> for token in result:
        ...     print(token, end="")

    - Создание комплишена без потоковой передачи:
        >>> model = "gpt-3.5-turbo"
        >>> messages = [{"role": "user", "content": "Hello, world!"}]
        >>> stream = False
        >>> result = FastGpt.create_completion(model, messages, stream)
        >>> for token in result:
        ...     print(token, end="")

    """
    headers = {
        'authority'         : 'chat9.fastgpt.me',
        'accept'            : 'text/event-stream',
        'accept-language'   : 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
        'cache-control'     : 'no-cache',
        'content-type'      : 'application/json',
        'origin'            : 'https://chat9.fastgpt.me',
        'plugins'           : '0',
        'pragma'            : 'no-cache',
        'referer'           : 'https://chat9.fastgpt.me/',
        'sec-ch-ua'         : '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile'  : '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest'    : 'empty',
        'sec-fetch-mode'    : 'cors',
        'sec-fetch-site'    : 'same-origin',
        'user-agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'usesearch'         : 'false',
        'x-requested-with'  : 'XMLHttpRequest',
    }

    json_data = {
        'messages'          : messages,
        'stream'            : stream,
        'model'             : model,
        'temperature'       : kwargs.get('temperature', 0.5),
        'presence_penalty'  : kwargs.get('presence_penalty', 0),
        'frequency_penalty' : kwargs.get('frequency_penalty', 0),
        'top_p'             : kwargs.get('top_p', 1),
    }

    subdomain = random.choice([
        'jdaen979ew',
        'chat9'
    ])

    response = requests.post(f'https://{subdomain}.fastgpt.me/api/openai/v1/chat/completions',
                             headers=headers, json=json_data, stream=stream)

    for line in response.iter_lines():
        if line:
            try:
                if b'content' in line:
                    line_json = json.loads(line.decode('utf-8').split('data: ')[1])
                    token = line_json['choices'][0]['delta'].get(
                        'content'
                    )
                    
                    if token:
                        yield token
            except:
                continue