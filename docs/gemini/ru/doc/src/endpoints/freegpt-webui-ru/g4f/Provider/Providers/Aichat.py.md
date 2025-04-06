# Модуль Aichat

## Обзор

Модуль предоставляет класс для взаимодействия с провайдером Aichat. Он определяет параметры подключения и функцию для создания запросов к API `chat-gpt.org`.

## Подробнее

Этот модуль используется для обмена сообщениями с сервисом `chat-gpt.org`. Он отправляет POST-запросы к API и возвращает сгенерированный ответ. Модуль включает в себя настройки заголовков и параметров запроса, необходимых для успешного взаимодействия с API.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Функция создает запрос к API `chat-gpt.org` и возвращает ответ.

    Args:
        model (str): Модель для использования.
        messages (list): Список сообщений для отправки.
        stream (bool): Флаг потоковой передачи (не используется).
        **kwargs: Дополнительные аргументы.

    Returns:
        yield response.json()['message']: Возвращает ответ от API в формате JSON.

    Raises:
        Exception: Если возникает ошибка при отправке запроса.
    """
```

**Как работает функция**:

1.  Формирует базовый текст запроса из списка сообщений, объединяя роль и содержимое каждого сообщения.
2.  Определяет заголовки HTTP-запроса, включая `authority`, `accept`, `content-type`, `origin` и `user-agent`.
3.  Формирует JSON-данные для отправки, включая сообщение, температуру, штрафы за присутствие и частоту, а также `top_p`.
4.  Отправляет POST-запрос к API `chat-gpt.org/api/text` с установленными заголовками и JSON-данными.
5.  Извлекает сообщение из JSON-ответа и возвращает его с использованием `yield`.

**ASII flowchart**:

```
Начало
  ↓
Формирование текста запроса (base)
  ↓
Определение заголовков запроса (headers)
  ↓
Формирование JSON данных (json_data)
  ↓
Отправка POST запроса (requests.post)
  ↓
Извлечение сообщения из JSON ответа (response.json()['message'])
  ↓
Возврат сообщения (yield)
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции _create_completion
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = False
# Генерация ответа от API
response = _create_completion(model=model, messages=messages, stream=stream)
# Итерация по ответу для получения содержимого
for message in response:
    print(message)
```

## Переменные

### `url`

```python
url = 'https://chat-gpt.org/chat'
```

URL для доступа к чату.

### `model`

```python
model = ['gpt-3.5-turbo']
```

Список поддерживаемых моделей.

### `supports_stream`

```python
supports_stream = False
```

Указывает, поддерживает ли провайдер потоковую передачу данных.

### `needs_auth`

```python
needs_auth = False
```

Указывает, требуется ли аутентификация для использования провайдера.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '({%s})' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Строка, формирующая информацию о поддерживаемых параметрах функции `_create_completion`.  Она использует `os.path.basename(__file__)` для получения имени текущего файла (модуля), `get_type_hints` для получения аннотаций типов параметров функции `_create_completion`, и `_create_completion.__code__.co_varnames` для получения имен параметров функции.