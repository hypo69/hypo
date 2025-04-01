# Модуль для работы с Gravityengine
## Обзор

Модуль предоставляет интерфейс для взаимодействия с сервисом Gravityengine для генерации текста на основе моделей GPT. Он включает в себя функцию для создания запросов к API Gravityengine и получения ответов.

## Подробней

Этот модуль предназначен для интеграции с сервисом Gravityengine, который предоставляет доступ к моделям GPT через API. Модуль содержит функцию `_create_completion`, которая отправляет запросы к API Gravityengine и возвращает сгенерированный текст.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """
    Создает запрос к API Gravityengine для генерации текста.

    Args:
        model (str): Имя используемой модели GPT.
        messages (list): Список сообщений для отправки в модель.
        stream (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
        **kwargs: Дополнительные аргументы.

    Yields:
        str: Сгенерированный текст.

    Raises:
        Exception: Если возникает ошибка при отправке запроса или обработке ответа.

    """
```

**Параметры**:

-   `model` (str): Имя используемой модели GPT.
-   `messages` (list): Список сообщений для отправки в модель.
-   `stream` (bool): Флаг, указывающий, следует ли использовать потоковую передачу данных.
-   `**kwargs`: Дополнительные аргументы.

**Возвращает**:

-   `str`: Сгенерированный текст.

**Как работает функция**:

1.  Функция `_create_completion` принимает параметры `model`, `messages`, `stream` и `kwargs`.
2.  Определяются заголовки запроса, включающие `Content-Type`.
3.  Формируется тело запроса `data`, включающее модель, температуру, штраф за присутствие и сообщения.
4.  Отправляется POST-запрос к API Gravityengine по адресу `url + '/api/openai/v1/chat/completions'` с указанными заголовками и телом запроса. Используется потоковый режим (`stream=True`).
5.  Функция генерирует (yield) содержимое первого выбора (`choices`) из JSON-ответа, а именно поле `content` из `message`.

**Примеры**:

```python
# Пример использования функции _create_completion
model = "gpt-3.5-turbo-16k"
messages = [{"role": "user", "content": "Привет, как дела?"}]
stream = True
for chunk in _create_completion(model=model, messages=messages, stream=stream):
    print(chunk)
```

## Переменные

### `url`

```python
url = 'https://gpt4.gravityengine.cc'
```

**Описание**:
URL-адрес API Gravityengine.

### `model`

```python
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
```

**Описание**:
Список поддерживаемых моделей GPT.

### `supports_stream`

```python
supports_stream = True
```

**Описание**:
Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.

### `needs_auth`

```python
needs_auth = False
```

**Описание**:
Флаг, указывающий, требуется ли аутентификация для доступа к API.

### `params`

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    ' (%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

**Описание**:
Строка, содержащая информацию о поддерживаемых параметрах функции `_create_completion`.