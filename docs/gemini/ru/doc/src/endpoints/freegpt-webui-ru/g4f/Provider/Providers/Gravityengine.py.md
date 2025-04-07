# Модуль `Gravityengine.py`

## Обзор

Модуль предоставляет реализацию провайдера `Gravityengine` для взаимодействия с моделями GPT через API `gpt4.gravityengine.cc`. Он поддерживает модели `gpt-3.5-turbo-16k` и `gpt-3.5-turbo-0613`, а также потоковую передачу данных. Не требует аутентификации.

## Подробней

Этот модуль используется для интеграции с сервисом `Gravityengine`, предоставляющим доступ к моделям GPT. Он содержит функцию `_create_completion`, которая отправляет запросы к API и возвращает ответы. Модуль предназначен для использования в составе фреймворка `g4f` (GenerativeForFree) для обеспечения доступа к генеративным моделям.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос на завершение текста к API Gravityengine.

    Args:
        model (str): Идентификатор модели, используемой для генерации.
        messages (list): Список сообщений, формирующих контекст запроса.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        **kwargs: Дополнительные параметры запроса.

    Returns:
        Generator[str, None, None]: Генератор, возвращающий контент ответа от API Gravityengine.

    Raises:
        requests.exceptions.RequestException: Если при выполнении запроса возникает ошибка.

    Example:
        >>> model = 'gpt-3.5-turbo-16k'
        >>> messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
        >>> stream = True
        >>> for chunk in _create_completion(model, messages, stream):
        ...     print(chunk)
        'I am doing well, thank you for asking!'
    """
```

**Назначение**: Функция `_create_completion` отправляет запрос к API `Gravityengine` для генерации текста на основе предоставленной модели и сообщений.

**Параметры**:

-   `model` (str): Идентификатор модели, используемой для генерации текста. Допустимые значения: `'gpt-3.5-turbo-16k'`, `'gpt-3.5-turbo-0613'`.
-   `messages` (list): Список сообщений, формирующих контекст запроса. Каждое сообщение представляет собой словарь с ключами `'role'` (роль отправителя: `'user'` или `'assistant'`) и `'content'` (текст сообщения).
-   `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных. Если `True`, функция возвращает генератор, который выдает части ответа по мере их поступления. Если `False`, функция возвращает полный ответ после его получения.
-   `**kwargs`: Дополнительные параметры запроса, такие как `temperature`, `presence_penalty` и другие.

**Возвращает**:

-   `Generator[str, None, None]`: Генератор, возвращающий части контента ответа от API `Gravityengine`.

**Вызывает исключения**:

-   `requests.exceptions.RequestException`: Если при выполнении запроса возникает ошибка соединения, таймаута или другая ошибка HTTP.

**Как работает функция**:

1.  Формирование заголовков запроса (`headers`) с указанием типа контента (`application/json`).
2.  Формирование тела запроса (`data`) с указанием модели, температуры, штрафа за присутствие и сообщений.
3.  Отправка POST-запроса к API `gpt4.gravityengine.cc` по адресу `/api/openai/v1/chat/completions` с использованием библиотеки `requests`. Указывается, что ответ должен быть потоковым (`stream=True`).
4.  Получение ответа от API и извлечение контента первого сообщения из списка `choices`.
5.  Генерация контента извлеченного сообщения.

```
A: Формирование заголовков и тела запроса
|
-- B: Отправка POST-запроса к API Gravityengine
|
C: Получение ответа от API
|
D: Извлечение контента сообщения из ответа
|
E: Генерация контента сообщения
```

**Примеры**:

```python
model = 'gpt-3.5-turbo-16k'
messages = [{'role': 'user', 'content': 'Напиши короткое стихотворение о весне.'}]
stream = True

for chunk in _create_completion(model, messages, stream):
    print(chunk)
```

```python
model = 'gpt-3.5-turbo-0613'
messages = [{'role': 'user', 'content': 'Как решить квадратное уравнение?'}]
stream = True

for chunk in _create_completion(model, messages, stream):
    print(chunk)
```

## Переменные

### `url`

```python
url = 'https://gpt4.gravityengine.cc'
```

URL-адрес API `Gravityengine`.

### `model`

```python
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
```

Список поддерживаемых моделей GPT.

### `supports_stream`

```python
supports_stream = True
```

Флаг, указывающий на поддержку потоковой передачи данных.

### `needs_auth`

```python
needs_auth = False
```

Флаг, указывающий на необходимость аутентификации. В данном случае аутентификация не требуется.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`. Используется для динамического формирования описания поддерживаемых параметров провайдера.