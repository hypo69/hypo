# Документация модуля Lockchat

## Обзор

Модуль `Lockchat.py` предназначен для взаимодействия с сервисом Lockchat для генерации текстовых ответов на основе предоставленных сообщений. Он предоставляет функцию `_create_completion`, которая отправляет запросы к API Lockchat и возвращает сгенерированный текст. Модуль также определяет параметры, поддерживаемые провайдером Lockchat.

## Подробней

Этот модуль является частью проекта `hypotez` и служит для интеграции с Lockchat в качестве одного из провайдеров для генерации текста. Он использует библиотеку `requests` для отправки HTTP-запросов и модуль `json` для обработки данных в формате JSON.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    """ Функция отправляет запрос к API Lockchat и возвращает сгенерированный текст.
    Args:
        model (str): Идентификатор используемой модели.
        messages (list): Список сообщений для отправки в API.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        temperature (float, optional): Параметр temperature, контролирующий случайность генерации текста. По умолчанию 0.7.
        **kwargs: Дополнительные параметры.

    Returns:
        Generator[str, None, None]: Генератор токенов сгенерированного текста.

    Raises:
        Exception: Если происходит ошибка при отправке запроса или обработке ответа.

    Example:
        >>> messages = [{"role": "user", "content": "Hello, how are you?"}]
        >>> for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
        ...     print(token, end='')
        I am doing well, thank you for asking. How can I assist you today?
    """
```

**Назначение**:
Функция `_create_completion` отправляет запрос к API Lockchat для генерации текста на основе предоставленных сообщений и параметров. Она использует потоковую передачу данных для получения текста по частям.

**Параметры**:
- `model` (str): Идентификатор используемой модели. Например, `'gpt-4'` или `'gpt-3.5-turbo'`.
- `messages` (list): Список сообщений для отправки в API. Каждое сообщение представляет собой словарь с ключами `role` и `content`.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных. Если `True`, функция возвращает генератор токенов текста.
- `temperature` (float, optional): Параметр `temperature`, контролирующий случайность генерации текста. Значение по умолчанию - `0.7`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `Generator[str, None, None]`: Генератор токенов сгенерированного текста. Каждый токен представляет собой часть сгенерированного текста.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при отправке запроса или обработке ответа.

**Как работает функция**:

1.  **Формирование полезной нагрузки (payload)**: Создается словарь `payload`, содержащий параметры запроса, такие как `temperature`, `messages`, `model` и `stream`.
2.  **Формирование заголовков (headers)**: Создается словарь `headers`, содержащий заголовок `user-agent`.
3.  **Отправка POST-запроса к API Lockchat**: Отправляется POST-запрос к API Lockchat по адресу `http://super.lockchat.app/v1/chat/completions?auth=FnMNPlwZEnGFqvEc9470Vw==` с использованием библиотеки `requests`.
4.  **Обработка ответа**: Функция итерируется по строкам ответа, полученного от API. Если в ответе содержится сообщение об ошибке (`The model: gpt-4 does not exist`), функция повторяет попытку запроса. Если в ответе содержится часть сгенерированного текста, функция извлекает текст из JSON и возвращает его в виде токена.

**ASCII flowchart**:

```
A [Формирование payload]
|
B [Формирование headers]
|
C [Отправка POST-запроса к API Lockchat]
|
D [Итерация по строкам ответа]
|
E [Проверка на наличие ошибки]
|
F [Извлечение и возврат токена]
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, how are you?"}]
for token in _create_completion(model='gpt-3.5-turbo', messages=messages, stream=True):
    print(token, end='')
```

## Переменные

### `url`

```python
url = 'http://super.lockchat.app'
```

URL-адрес API Lockchat.

### `model`

```python
model = ['gpt-4', 'gpt-3.5-turbo']
```

Список поддерживаемых моделей.

### `supports_stream`

```python
supports_stream = True
```

Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.

### `needs_auth`

```python
needs_auth = False
```

Флаг, указывающий, требуется ли аутентификация для использования провайдера.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`. Она формируется динамически на основе аннотаций типов и имен аргументов функции.