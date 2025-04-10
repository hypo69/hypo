# Модуль Equing

## Обзор

Модуль предоставляет класс `Equing`, который является провайдером для работы с сервисом Equing (next.eqing.tech). Он поддерживает модели `gpt-3.5-turbo` и потоковую передачу данных. Класс наследуется от `AbstractProvider` и реализует метод для создания завершений (completions) на основе запросов к API Equing.

## Подробней

Модуль предназначен для интеграции с сервисом Equing для генерации текста на основе предоставленных сообщений. Он использует API Equing для создания и получения ответов, поддерживая потоковый режим для постепенной выдачи результатов.

## Классы

### `Equing(AbstractProvider)`

**Описание**: Класс `Equing` представляет собой провайдера для работы с сервисом Equing.

**Наследует**: `AbstractProvider`

**Атрибуты**:
- `url` (str): URL сервиса Equing (`https://next.eqing.tech/`).
- `working` (bool): Флаг, указывающий на работоспособность провайдера (в данном случае `False`).
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных (`True`).
- `supports_gpt_35_turbo` (bool): Флаг, указывающий на поддержку модели `gpt-3.5-turbo` (`True`).
- `supports_gpt_4` (bool): Флаг, указывающий на поддержку модели `gpt-4` (`False`).

**Методы**:
- `create_completion`: Создает запрос к API Equing и возвращает результат.

## Функции

### `create_completion`

```python
def create_completion(
    model: str,
    messages: list[dict[str, str]],
    stream: bool, **kwargs: Any) -> CreateResult:
    """
    Создает запрос к API Equing для генерации текста на основе предоставленных сообщений.

    Args:
        model (str): Имя модели для использования.
        messages (list[dict[str, str]]): Список сообщений для передачи в API.
        stream (bool): Флаг, указывающий на необходимость потоковой передачи данных.
        **kwargs (Any): Дополнительные параметры для передачи в API.

    Returns:
        CreateResult: Генератор текста, возвращаемый из API Equing.

    Raises:
        requests.exceptions.RequestException: Если возникает ошибка при выполнении HTTP-запроса.
        json.JSONDecodeError: Если возникает ошибка при декодировании JSON-ответа.

    """
```

**Назначение**: Метод `create_completion` отправляет запрос к API Equing для генерации текста на основе предоставленных сообщений и параметров.

**Параметры**:
- `model` (str): Имя модели для использования (например, "gpt-3.5-turbo").
- `messages` (list[dict[str, str]]): Список сообщений, где каждое сообщение представляет собой словарь с ключами "role" и "content".
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковый режим.
- `**kwargs` (Any): Дополнительные параметры, такие как `temperature`, `presence_penalty`, `frequency_penalty` и `top_p`.

**Возвращает**:
- `CreateResult`: Генератор, который выдает текст по частям (в потоковом режиме) или полную строку (в не потоковом режиме).

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Если возникает ошибка при выполнении HTTP-запроса.
- `json.JSONDecodeError`: Если возникает ошибка при декодировании JSON-ответа.

**Как работает функция**:

1.  **Формирование заголовков и данных**:
    *   Создаются заголовки `headers` для HTTP-запроса, включающие информацию о типе контента, User-Agent и другие необходимые параметры.
    *   Формируются данные `json_data` для отправки в теле запроса, включающие сообщения, имя модели, флаг потоковой передачи и дополнительные параметры, такие как температура, штрафы за присутствие и частоту, а также значение `top_p`.

2.  **Отправка запроса к API**:
    *   Отправляется POST-запрос к API Equing (`https://next.eqing.tech/api/openai/v1/chat/completions`) с использованием библиотеки `requests`. Указываются заголовки, данные в формате JSON и флаг потоковой передачи.

3.  **Обработка ответа**:
    *   Если `stream` равен `False` (не потоковый режим):
        *   Извлекается содержимое первого сообщения из ответа JSON и возвращается как результат.
    *   Если `stream` равен `True` (потоковый режим):
        *   Итерируется по содержимому ответа чанками размером 1024 байта.
        *   Для каждой строки проверяется наличие подстроки `b'content'`. Если она присутствует, строка декодируется из UTF-8, разделяется по `data: `, и полученная JSON-строка загружается.
        *   Извлекается содержимое из поля `content` в секции `delta` и возвращается как токен.

4.  **Возврат результата**:
    *   Функция возвращает генератор, который выдает токены текста по мере их поступления из API Equing (в потоковом режиме) или сразу весь текст (в не потоковом режиме).

```
    Формирование заголовков и данных   Отправка запроса к API
    ---------------------------------   -----------------------
    │                                 │                       │
    │  headers, json_data               │  POST request         │
    │                                 │                       │
    ---------------------------------   -----------------------
    │
    │  stream == False?
    ├──Да──────────────────────────────────
    │
    │  Извлечение контента
    │  response.json()["choices"][0]["message"]["content"]
    │
    └──Возврат результата

    │
    │  stream == True?
    ├──Да──────────────────────────────────
    │
    │  Итерация по чанкам
    │  response.iter_content(chunk_size=1024)
    │
    │  b'content' in line?
    ├──Да──────────────────────────────────
    │
    │  Извлечение токена
    │  token = line_json['choices'][0]['delta'].get('content')
    │
    └──Возврат токена
```

**Примеры**:

```python
# Пример использования в не потоковом режиме
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = False
result = Equing.create_completion(model=model, messages=messages, stream=stream)
for item in result:
    print(item)

# Пример использования в потоковом режиме
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Tell me a story."}]
stream = True
result = Equing.create_completion(model=model, messages=messages, stream=stream)
for item in result:
    print(item, end="", flush=True)